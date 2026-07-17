#!/usr/bin/env python3
"""Validate portable Markdown links and declared mirrors in this vault."""

from __future__ import annotations

import argparse
import filecmp
import os
import posixpath
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


EXTERNAL_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
INVALID_ESCAPE = re.compile(r"%(?![0-9A-Fa-f]{2})")
REFERENCE_DEFINITION = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))")


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    code: str
    detail: str

    def render(self) -> str:
        location = f"{self.path}:{self.line}" if self.line else self.path
        return f"{location}: [{self.code}] {self.detail}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate vault-local Markdown links, mirrors, and Git whitespace."
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--scope", choices=("changed", "all"), default="changed")
    parser.add_argument("--include-archive", action="store_true")
    parser.add_argument(
        "--mirror",
        action="append",
        default=[],
        metavar="LEFT=RIGHT",
        help="Require two root-relative files to be byte-identical; repeat as needed.",
    )
    parser.add_argument(
        "--no-diff-check",
        action="store_true",
        help="Skip git diff --check (useful only for isolated fixtures).",
    )
    return parser.parse_args()


def run_git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes] | None:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode == 128:
        return None
    return result


def decode_z_paths(payload: bytes) -> set[str]:
    return {
        item.decode("utf-8", errors="surrogateescape")
        for item in payload.split(b"\0")
        if item
    }


def git_paths(root: Path, *args: str) -> set[str] | None:
    result = run_git(root, *args)
    if result is None or result.returncode != 0:
        return None
    return decode_z_paths(result.stdout)


def filesystem_files(root: Path) -> set[str]:
    files: set[str] = set()
    for directory, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name != ".git"]
        base = Path(directory)
        for filename in filenames:
            files.add((base / filename).relative_to(root).as_posix())
    return files


def comparison_key(path: str) -> str:
    return unicodedata.normalize("NFC", path).casefold()


def canonical_existing_files(root: Path, actual_files: set[str]) -> set[str]:
    tracked = git_paths(root, "ls-files", "-z") or set()
    tracked_existing = {
        path for path in tracked if (root / PurePosixPath(path)).is_file()
    }
    tracked_keys = {comparison_key(path) for path in tracked_existing}
    untracked = {
        path for path in actual_files if comparison_key(path) not in tracked_keys
    }
    return tracked_existing | untracked


def changed_markdown_files(root: Path) -> set[str] | None:
    commands = (
        ("diff", "--name-only", "-z", "--diff-filter=ACMRTUXB"),
        ("diff", "--cached", "--name-only", "-z", "--diff-filter=ACMRTUXB"),
        ("ls-files", "--others", "--exclude-standard", "-z"),
    )
    changed: set[str] = set()
    for command in commands:
        paths = git_paths(root, *command)
        if paths is None:
            return None
        changed.update(paths)
    return {path for path in changed if path.lower().endswith(".md")}


def markdown_scope(
    root: Path, actual_files: set[str], scope: str, include_archive: bool
) -> list[str] | None:
    if scope == "changed":
        candidates = changed_markdown_files(root)
        if candidates is None:
            return None
    else:
        candidates = {path for path in actual_files if path.lower().endswith(".md")}

    return sorted(
        path
        for path in candidates
        if (root / PurePosixPath(path)).is_file()
        and (include_archive or not path.startswith("_Archive/"))
    )


def mask_inline_code(line: str) -> str:
    masked = list(line)
    index = 0
    while index < len(line):
        if line[index] != "`":
            index += 1
            continue
        run_end = index
        while run_end < len(line) and line[run_end] == "`":
            run_end += 1
        marker = line[index:run_end]
        closing = line.find(marker, run_end)
        if closing == -1:
            index = run_end
            continue
        for position in range(index, closing + len(marker)):
            masked[position] = " "
        index = closing + len(marker)
    return "".join(masked)


def iter_visible_lines(text: str):
    fence_char: str | None = None
    fence_length = 0
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = None
                fence_length = 0
            continue
        if fence_char is None:
            yield line_number, line, mask_inline_code(line)


def inline_destinations(original: str, visible: str):
    start = 0
    while True:
        marker = visible.find("](", start)
        if marker == -1:
            return
        index = marker + 2
        while index < len(visible) and visible[index].isspace():
            index += 1
        if index >= len(visible):
            return

        if visible[index] == "<":
            closing = visible.find(">", index + 1)
            if closing == -1:
                start = index + 1
                continue
            yield original[index + 1 : closing]
            start = closing + 1
            continue

        destination_start = index
        depth = 0
        escaped = False
        while index < len(visible):
            character = visible[index]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                depth += 1
            elif character == ")":
                if depth == 0:
                    break
                depth -= 1
            elif character.isspace() and depth == 0:
                break
            index += 1
        if index > destination_start:
            yield original[destination_start:index]
        start = max(index + 1, marker + 2)


def local_destination(raw: str) -> bool:
    if not raw or raw.startswith("#") or raw.startswith("//"):
        return False
    scheme = EXTERNAL_SCHEME.match(raw)
    return scheme is None


def expected_relative_path(source_path: str, target_path: str) -> str:
    source_directory = posixpath.dirname(source_path) or "."
    return posixpath.relpath(target_path, source_directory)


def validate_destination(
    source_path: str,
    line_number: int,
    raw: str,
    canonical_files: set[str],
    canonical_by_key: dict[str, list[str]],
) -> list[Finding]:
    findings: list[Finding] = []
    if raw.lower().startswith("file:"):
        return [Finding(source_path, line_number, "file-uri", f"forbidden destination {raw!r}")]
    if raw.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", raw):
        return [Finding(source_path, line_number, "absolute-path", f"forbidden destination {raw!r}")]
    if not local_destination(raw):
        return findings
    if "\\" in raw:
        findings.append(
            Finding(source_path, line_number, "backslash-path", f"use POSIX separators in {raw!r}")
        )
    if " " in raw:
        findings.append(
            Finding(source_path, line_number, "raw-space", f"encode ASCII spaces as %20 in {raw!r}")
        )
    if INVALID_ESCAPE.search(raw):
        findings.append(
            Finding(source_path, line_number, "invalid-percent-escape", f"invalid escape in {raw!r}")
        )

    path_part = raw.split("#", 1)[0].split("?", 1)[0]
    decoded = unquote(path_part)
    if not decoded:
        return findings
    if decoded.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", decoded):
        findings.append(
            Finding(source_path, line_number, "absolute-path", f"decoded destination is absolute: {raw!r}")
        )
        return findings
    if not PurePosixPath(decoded).suffix:
        findings.append(
            Finding(source_path, line_number, "missing-extension", f"local destination lacks an extension: {raw!r}")
        )

    source_directory = posixpath.dirname(source_path)
    resolved = posixpath.normpath(posixpath.join(source_directory, decoded))
    if resolved == ".." or resolved.startswith("../"):
        findings.append(
            Finding(source_path, line_number, "outside-root", f"destination escapes the repository: {raw!r}")
        )
        return findings

    if resolved in canonical_files:
        canonical_target = resolved
    else:
        candidates = canonical_by_key.get(comparison_key(resolved), [])
        if candidates:
            findings.append(
                Finding(
                    source_path,
                    line_number,
                    "spelling-mismatch",
                    f"{raw!r} resolves by local tolerance; use exact target {candidates[0]!r}",
                )
            )
            canonical_target = candidates[0]
        else:
            findings.append(
                Finding(source_path, line_number, "missing-target", f"no file at {resolved!r} from {raw!r}")
            )
            return findings

    expected = expected_relative_path(source_path, canonical_target)
    if decoded != expected:
        findings.append(
            Finding(
                source_path,
                line_number,
                "non-shortest-path",
                f"use {expected.replace(' ', '%20')!r} instead of {raw!r}",
            )
        )
    return findings


def validate_markdown(
    root: Path, markdown_files: list[str], canonical_files: set[str]
) -> list[Finding]:
    canonical_by_key: dict[str, list[str]] = {}
    for path in sorted(canonical_files):
        canonical_by_key.setdefault(comparison_key(path), []).append(path)

    findings: list[Finding] = []
    for relative_path in markdown_files:
        path = root / PurePosixPath(relative_path)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as error:
            findings.append(
                Finding(relative_path, 0, "utf8", f"cannot decode as UTF-8: {error}")
            )
            continue

        for line_number, original, visible in iter_visible_lines(text):
            if re.search(r"\[\[[^\]\n]+\]\]", visible):
                findings.append(
                    Finding(relative_path, line_number, "wikilink", "Obsidian wikilink syntax remains")
                )

            reference = REFERENCE_DEFINITION.match(visible)
            if reference:
                destination = reference.group(1) or reference.group(2) or ""
                if local_destination(destination):
                    findings.append(
                        Finding(
                            relative_path,
                            line_number,
                            "reference-link",
                            "internal links must use inline Markdown syntax",
                        )
                    )
                    findings.extend(
                        validate_destination(
                            relative_path,
                            line_number,
                            destination,
                            canonical_files,
                            canonical_by_key,
                        )
                    )

            for destination in inline_destinations(original, visible):
                findings.extend(
                    validate_destination(
                        relative_path,
                        line_number,
                        destination,
                        canonical_files,
                        canonical_by_key,
                    )
                )
    return findings


def resolve_mirror(root: Path, raw: str) -> tuple[Path, Path] | None:
    if "=" not in raw:
        return None
    left_raw, right_raw = raw.split("=", 1)
    left = (root / left_raw).resolve()
    right = (root / right_raw).resolve()
    root_resolved = root.resolve()
    if root_resolved not in left.parents or root_resolved not in right.parents:
        return None
    return left, right


def validate_mirrors(root: Path, mirrors: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    for raw in mirrors:
        pair = resolve_mirror(root, raw)
        if pair is None:
            findings.append(Finding("(mirror)", 0, "invalid-mirror", f"expected LEFT=RIGHT within root: {raw!r}"))
            continue
        left, right = pair
        missing = [str(path.relative_to(root.resolve())) for path in pair if not path.is_file()]
        if missing:
            findings.append(Finding("(mirror)", 0, "missing-mirror", f"missing file(s): {', '.join(missing)}"))
            continue
        if not filecmp.cmp(left, right, shallow=False):
            findings.append(Finding("(mirror)", 0, "mirror-drift", f"files differ: {raw}"))
    return findings


def validate_diff_check(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for command in (("diff", "--check"), ("diff", "--cached", "--check")):
        result = run_git(root, *command)
        if result is None or result.returncode == 0:
            continue
        output = result.stdout.decode("utf-8", errors="replace").strip()
        if not output:
            output = result.stderr.decode("utf-8", errors="replace").strip()
        findings.extend(
            Finding("(git)", 0, "diff-check", line) for line in output.splitlines()
        )
    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: root is not a directory: {root}", file=sys.stderr)
        return 2

    actual_files = filesystem_files(root)
    markdown_files = markdown_scope(root, actual_files, args.scope, args.include_archive)
    if markdown_files is None:
        print("error: --scope changed requires a Git worktree", file=sys.stderr)
        return 2

    canonical_files = canonical_existing_files(root, actual_files)
    findings = validate_markdown(root, markdown_files, canonical_files)
    findings.extend(validate_mirrors(root, args.mirror))
    if not args.no_diff_check:
        findings.extend(validate_diff_check(root))

    findings = sorted(set(findings))
    if findings:
        for finding in findings:
            print(finding.render())
        print(
            f"FAIL: {len(findings)} issue(s); scanned {len(markdown_files)} Markdown file(s).",
            file=sys.stderr,
        )
        return 1

    print(f"OK: scanned {len(markdown_files)} Markdown file(s); all requested checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
