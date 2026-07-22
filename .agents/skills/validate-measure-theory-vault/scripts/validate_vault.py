#!/usr/bin/env python3
"""Validate portable Markdown links, declared mirrors, and study-state interfaces."""

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
FRONTMATTER_KEY = re.compile(r"^([A-Za-z0-9-]+):(?:\s*(.*))?$")
COMPETENCY_DECLARATION = re.compile(
    r"^\s*-\s+`([A-Z][A-Za-z0-9-]*\.[A-Za-z0-9-]+)`[:：]",
    re.MULTILINE,
)
LEDGER_KEY = re.compile(r"^`([^`]+)`$")
RELATIVE_TIME = re.compile(
    r"\b(?:tonight|today|tomorrow|yesterday)\b|今晚|今天|今日|明天|昨日|本日|翌日",
    re.IGNORECASE,
)
ACQUIRED_STATE = re.compile(
    r"(?:state|verdict)[^\n]{0,100}\bacquired\b|use\s+`acquired`",
    re.IGNORECASE,
)

LEARNING_STATES = {"not-attempted", "rupture", "reconstructible", "deployable"}
RUPTURE_STATES = {"open", "blocked", "resolved"}
DERIVED_STUDY_TYPES = {
    "study-cycle-plan",
    "study-packet-overview",
    "study-packet-notes",
    "study-packet-work-sheet",
    "study-packet-corrige",
    "study-session-sheet",
    "study-session-hints",
    "study-session-corrige",
}
PACKET_TYPES = {
    "study-packet-overview",
    "study-packet-notes",
    "study-packet-work-sheet",
    "study-packet-carnet",
    "study-packet-corrige",
}
REQUIRED_STUDY_FIELDS = {
    "study-cycle-plan": ("status", "cycle", "start", "end", "planned-time"),
    "study-packet-overview": ("cycle", "packet", "sessions", "planned-time"),
    "study-packet-notes": ("cycle", "packet"),
    "study-packet-work-sheet": ("cycle", "packet"),
    "study-packet-carnet": ("cycle", "packet", "state", "actual-time"),
    "study-packet-corrige": ("cycle", "packet"),
    "study-session-sheet": (
        "date",
        "cycle",
        "packet",
        "session",
        "state",
        "planned-time",
        "actual-time",
    ),
    "study-session-hints": ("date", "cycle", "packet", "session"),
    "study-session-corrige": ("date", "cycle", "packet", "session"),
    "daily-study-review": (
        "date",
        "cycle",
        "primary-packet",
        "planned-time",
        "actual-time",
        "decision",
        "closed",
    ),
    "learner-current-state": (
        "updated",
        "active-cycle",
        "active-packet",
        "active-session",
        "decision",
    ),
    "learner-mastery-ledger": ("updated",),
    "learner-rupture-ledger": ("updated",),
    "learner-cycle-register": ("updated",),
}


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    code: str
    detail: str

    def render(self) -> str:
        location = f"{self.path}:{self.line}" if self.line else self.path
        return f"{location}: [{self.code}] {self.detail}"


@dataclass(frozen=True)
class Frontmatter:
    values: dict[str, str | list[str]]
    lines: dict[str, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate vault-local Markdown, mirrors, Git whitespace, and optional study state."
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
    parser.add_argument(
        "--study-state",
        action="store_true",
        help="Validate Study Log frontmatter, active IDs, competency keys, and authority boundaries.",
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


def strip_yaml_scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(relative_path: str, text: str) -> tuple[Frontmatter | None, list[Finding]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, []

    try:
        closing = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return None, [Finding(relative_path, 1, "frontmatter", "opening delimiter has no closing delimiter")]

    values: dict[str, str | list[str]] = {}
    key_lines: dict[str, int] = {}
    pending_list: str | None = None
    findings: list[Finding] = []
    for index, line in enumerate(lines[1:closing], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and pending_list is not None:
            if values[pending_list] == "":
                values[pending_list] = []
            current = values[pending_list]
            if not isinstance(current, list):
                findings.append(
                    Finding(relative_path, index, "frontmatter", f"{pending_list!r} mixes scalar and list values")
                )
                continue
            current.append(strip_yaml_scalar(line[4:]))
            continue

        match = FRONTMATTER_KEY.match(line)
        if match is None:
            findings.append(
                Finding(relative_path, index, "frontmatter", f"unsupported frontmatter line {line!r}")
            )
            pending_list = None
            continue
        key = match.group(1)
        value = strip_yaml_scalar(match.group(2) or "")
        values[key] = value
        key_lines[key] = index
        pending_list = key if value == "" else None

    return Frontmatter(values, key_lines), findings


def scalar(frontmatter: Frontmatter, key: str) -> str:
    value = frontmatter.values.get(key, "")
    return value if isinstance(value, str) else ""


def list_value(frontmatter: Frontmatter, key: str) -> list[str]:
    value = frontmatter.values.get(key, [])
    return value if isinstance(value, list) else []


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

        for line_number, line in enumerate(text.splitlines(), start=1):
            if "\t" in line:
                findings.append(
                    Finding(relative_path, line_number, "tab-character", "literal TAB is forbidden in Markdown")
                )

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


def validate_packet_dates(
    relative_path: str, document_type: str, frontmatter: Frontmatter
) -> list[Finding]:
    if document_type not in PACKET_TYPES:
        return []
    has_date = bool(scalar(frontmatter, "date"))
    has_start = bool(scalar(frontmatter, "start"))
    has_end = bool(scalar(frontmatter, "end"))
    line = frontmatter.lines.get("date", frontmatter.lines.get("start", 1))
    if has_date and (has_start or has_end):
        return [Finding(relative_path, line, "study-date", "use date for one day or start/end for a range, not both")]
    if has_date or (has_start and has_end):
        return []
    return [Finding(relative_path, line, "study-date", "packet requires date or a complete start/end range")]


def validate_canonical_sources(
    relative_path: str,
    frontmatter: Frontmatter,
    canonical_files: set[str],
) -> list[Finding]:
    findings: list[Finding] = []
    sources = list_value(frontmatter, "canonical-sources")
    line = frontmatter.lines.get("canonical-sources", 1)
    if scalar(frontmatter, "math-authority") != "derived":
        findings.append(
            Finding(relative_path, frontmatter.lines.get("math-authority", 1), "math-authority", "derived study artifact must declare math-authority: derived")
        )
    if not sources:
        findings.append(
            Finding(relative_path, line, "canonical-sources", "derived study artifact requires a nonempty canonical-sources list")
        )
        return findings

    canonical_by_key: dict[str, list[str]] = {}
    for path in sorted(canonical_files):
        canonical_by_key.setdefault(comparison_key(path), []).append(path)

    source_directory = posixpath.dirname(relative_path)
    for raw in sources:
        if not raw or raw.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", raw):
            findings.append(Finding(relative_path, line, "canonical-source", f"invalid relative source {raw!r}"))
            continue
        resolved = posixpath.normpath(posixpath.join(source_directory, raw))
        if resolved == ".." or resolved.startswith("../"):
            findings.append(Finding(relative_path, line, "canonical-source", f"source escapes repository: {raw!r}"))
            continue
        if resolved in canonical_files:
            continue
        candidates = canonical_by_key.get(comparison_key(resolved), [])
        if candidates:
            findings.append(
                Finding(relative_path, line, "canonical-source-spelling", f"use exact source path {candidates[0]!r} instead of {raw!r}")
            )
        else:
            findings.append(Finding(relative_path, line, "canonical-source", f"missing canonical source {resolved!r}"))
    return findings


def load_frontmatter(root: Path, relative_path: str) -> tuple[Frontmatter | None, list[Finding], str]:
    path = root / PurePosixPath(relative_path)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        return None, [Finding(relative_path, 0, "study-state", f"cannot read file: {error}")], ""
    frontmatter, findings = parse_frontmatter(relative_path, text)
    return frontmatter, findings, text


def validate_active_contract(
    root: Path,
    canonical_files: set[str],
    frontmatters: dict[str, Frontmatter],
) -> list[Finding]:
    findings: list[Finding] = []
    current_path = "Study Log/State/CURRENT.md"
    current = frontmatters.get(current_path)
    if current is None:
        return [Finding(current_path, 0, "active-contract", "missing readable current-state frontmatter")]

    cycle = scalar(current, "active-cycle")
    packet = scalar(current, "active-packet")
    session = scalar(current, "active-session")
    cycle_path = f"Study Log/Cycles/{cycle}/00_Plan.md"
    packet_path = f"Study Log/Cycles/{cycle}/Packets/{packet}/00_Overview.md"

    for expected, label in ((cycle_path, "cycle"), (packet_path, "packet")):
        if expected not in canonical_files:
            findings.append(
                Finding(current_path, current.lines.get(f"active-{label}", 1), "active-contract", f"active {label} does not resolve to {expected!r}")
            )

    cycle_frontmatter = frontmatters.get(cycle_path)
    if cycle_frontmatter is not None and scalar(cycle_frontmatter, "cycle") != cycle:
        findings.append(Finding(cycle_path, cycle_frontmatter.lines.get("cycle", 1), "active-contract", "cycle ID disagrees with CURRENT"))
    packet_frontmatter = frontmatters.get(packet_path)
    if packet_frontmatter is not None:
        if scalar(packet_frontmatter, "cycle") != cycle or scalar(packet_frontmatter, "packet") != packet:
            findings.append(Finding(packet_path, packet_frontmatter.lines.get("packet", 1), "active-contract", "packet IDs disagree with CURRENT"))

    session_prefix = f"Study Log/Cycles/{cycle}/Packets/{packet}/Sessions/"
    candidates = [
        path
        for path, frontmatter in frontmatters.items()
        if path.startswith(session_prefix)
        and scalar(frontmatter, "type") == "study-session-sheet"
        and scalar(frontmatter, "session") == session
    ]
    if len(candidates) != 1:
        findings.append(
            Finding(current_path, current.lines.get("active-session", 1), "active-contract", f"active session {session!r} resolves to {len(candidates)} session sheets")
        )
    else:
        session_frontmatter = frontmatters[candidates[0]]
        if scalar(session_frontmatter, "cycle") != cycle or scalar(session_frontmatter, "packet") != packet:
            findings.append(Finding(candidates[0], session_frontmatter.lines.get("session", 1), "active-contract", "session IDs disagree with CURRENT"))
    return findings


def table_rows(text: str):
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        yield line_number, [cell.strip() for cell in stripped.strip("|").split("|")]


def validate_competency_ledgers(root: Path, canonical_files: set[str]) -> list[Finding]:
    competency_keys: set[str] = set()
    for relative_path in canonical_files:
        if not relative_path.endswith("/00_Module Map.md"):
            continue
        try:
            text = (root / PurePosixPath(relative_path)).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        competency_keys.update(COMPETENCY_DECLARATION.findall(text))

    findings: list[Finding] = []
    ledger_specs = (
        ("Study Log/State/MASTERY.md", {"reconstructible", "deployable"}),
        ("Study Log/State/RUPTURES.md", RUPTURE_STATES),
    )
    for relative_path, allowed_states in ledger_specs:
        path = root / PurePosixPath(relative_path)
        if not path.is_file():
            findings.append(Finding(relative_path, 0, "competency-ledger", "missing ledger"))
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, cells in table_rows(text):
            if not cells:
                continue
            match = LEDGER_KEY.match(cells[0])
            if match is None:
                continue
            key = match.group(1)
            if key not in competency_keys:
                findings.append(Finding(relative_path, line_number, "unknown-competency", f"no Module Map declares {key!r}"))
            if relative_path.endswith("MASTERY.md") and len(cells) >= 2:
                state = cells[1].strip("`")
                if state not in allowed_states:
                    findings.append(Finding(relative_path, line_number, "mastery-state", f"invalid mastery state {state!r}"))
            if relative_path.endswith("RUPTURES.md") and cells:
                state = cells[-1].strip("`")
                normalized = "blocked" if state.startswith("blocked-by ") else state
                if normalized not in allowed_states:
                    findings.append(Finding(relative_path, line_number, "rupture-state", f"invalid rupture state {state!r}"))
    return findings


def validate_study_state(root: Path, canonical_files: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    frontmatters: dict[str, Frontmatter] = {}
    texts: dict[str, str] = {}
    for relative_path in sorted(path for path in canonical_files if path.startswith("Study Log/") and path.endswith(".md")):
        frontmatter, parse_findings, text = load_frontmatter(root, relative_path)
        findings.extend(parse_findings)
        texts[relative_path] = text
        if frontmatter is not None:
            frontmatters[relative_path] = frontmatter

    for relative_path, frontmatter in frontmatters.items():
        document_type = scalar(frontmatter, "type")
        required = REQUIRED_STUDY_FIELDS.get(document_type, ())
        for key in required:
            if key not in frontmatter.values:
                findings.append(Finding(relative_path, 1, "study-frontmatter", f"missing required field {key!r} for {document_type!r}"))
            elif key != "actual-time" and not scalar(frontmatter, key):
                findings.append(Finding(relative_path, frontmatter.lines.get(key, 1), "study-frontmatter", f"required field {key!r} is empty"))

        findings.extend(validate_packet_dates(relative_path, document_type, frontmatter))
        if document_type in DERIVED_STUDY_TYPES:
            findings.extend(validate_canonical_sources(relative_path, frontmatter, canonical_files))
        if document_type in {"study-packet-carnet", "study-session-sheet"}:
            state = scalar(frontmatter, "state")
            if state and state not in LEARNING_STATES:
                findings.append(Finding(relative_path, frontmatter.lines.get("state", 1), "learning-state", f"invalid learning state {state!r}"))

        if ACQUIRED_STATE.search(texts[relative_path]):
            line = next(
                (index for index, line_text in enumerate(texts[relative_path].splitlines(), start=1) if ACQUIRED_STATE.search(line_text)),
                1,
            )
            findings.append(Finding(relative_path, line, "learning-state", "use deployable instead of acquired"))

    relative_time_paths = {"Study Log/00_Chronology.md"} | {
        path for path in texts if path.startswith("Study Log/State/")
    }
    for relative_path in sorted(relative_time_paths):
        text = texts.get(relative_path, "")
        for line_number, line in enumerate(text.splitlines(), start=1):
            match = RELATIVE_TIME.search(line)
            if match:
                findings.append(Finding(relative_path, line_number, "relative-time", f"use an absolute date instead of {match.group(0)!r}"))

    findings.extend(validate_active_contract(root, canonical_files, frontmatters))
    findings.extend(validate_competency_ledgers(root, canonical_files))
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
    if args.study_state:
        findings.extend(validate_study_state(root, canonical_files))
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
