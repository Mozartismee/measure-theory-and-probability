#!/usr/bin/env python3
"""Read-only consistency and backlink report for the canonical lemma registry."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit


FRONTMATTER_TYPE_RE = re.compile(r"^type:\s*([^#\n]+?)\s*$", re.MULTILINE)
LEMMA_HEADING_RE = re.compile(r"^# Lemma\s+(\d+)\s+—\s+(.+?)\s*$", re.MULTILINE)
INDEX_ENTRY_RE = re.compile(
    r"^- \[Lemma\s+(\d+)\s+—\s+([^\]]+)\]\(([^)]+)\)\s*$",
    re.MULTILINE,
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIPPED_DIRS = {".git", "_Archive", "__pycache__"}


@dataclass(frozen=True)
class LemmaRecord:
    number: int
    title: str
    path: Path


@dataclass(frozen=True)
class IndexEntry:
    number: int
    title: str
    destination: str
    target: Path


@dataclass(frozen=True)
class LinkRecord:
    source: Path
    line: int
    target: Path


@dataclass
class RegistryReport:
    root: Path
    index: Path | None = None
    lemmas: list[LemmaRecord] = field(default_factory=list)
    entries: list[IndexEntry] = field(default_factory=list)
    internal_links: list[LinkRecord] = field(default_factory=list)
    backlinks: list[LinkRecord] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter_type(path: Path) -> str | None:
    text = read_text(path)
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    match = FRONTMATTER_TYPE_RE.search(text[4:end])
    return match.group(1).strip() if match else None


def resolve_local_link(source: Path, destination: str) -> Path | None:
    raw = destination.strip()
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc or raw.startswith("#"):
        return None
    decoded = unquote(parsed.path)
    if not decoded or decoded.startswith("/"):
        return None
    return (source.parent / decoded).resolve()


def markdown_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in SKIPPED_DIRS for part in path.relative_to(root).parts):
            continue
        paths.append(path)
    return sorted(paths)


def collect_links(source: Path, lemma_paths: set[Path]) -> list[LinkRecord]:
    links: list[LinkRecord] = []
    for line_number, line in enumerate(read_text(source).splitlines(), start=1):
        for match in MARKDOWN_LINK_RE.finditer(line):
            target = resolve_local_link(source, match.group(1))
            if target in lemma_paths:
                links.append(LinkRecord(source.resolve(), line_number, target))
    return links


def inspect_registry(root: Path) -> RegistryReport:
    root = root.resolve()
    report = RegistryReport(root=root)
    lemma_dir = root / "80_Lemmas"
    if not lemma_dir.is_dir():
        report.errors.append("missing lemma directory: 80_Lemmas")
        return report

    immediate_markdown = sorted(lemma_dir.glob("*.md"))
    indexes = [path for path in immediate_markdown if frontmatter_type(path) == "lemma-index"]
    if len(indexes) != 1:
        report.errors.append(
            f"expected exactly one type: lemma-index file, found {len(indexes)}"
        )
    else:
        report.index = indexes[0].resolve()

    number_to_lemmas: dict[int, list[LemmaRecord]] = {}
    path_to_lemma: dict[Path, LemmaRecord] = {}
    for path in immediate_markdown:
        if frontmatter_type(path) != "lemma":
            continue
        heading = LEMMA_HEADING_RE.search(read_text(path))
        if not heading:
            report.errors.append(f"missing canonical H1 in {path.relative_to(root)}")
            continue
        record = LemmaRecord(int(heading.group(1)), heading.group(2).strip(), path.resolve())
        report.lemmas.append(record)
        if record.number < 1:
            report.errors.append(
                f"lemma number must be positive in {path.relative_to(root)}"
            )
        number_to_lemmas.setdefault(record.number, []).append(record)
        path_to_lemma[record.path] = record

    for number, records in sorted(number_to_lemmas.items()):
        if len(records) > 1:
            names = ", ".join(str(record.path.relative_to(root)) for record in records)
            report.errors.append(f"duplicate lemma number {number}: {names}")

    if report.index:
        seen_entry_numbers: set[int] = set()
        seen_targets: set[Path] = set()
        index_text = read_text(report.index)
        for match in INDEX_ENTRY_RE.finditer(index_text):
            target = resolve_local_link(report.index, match.group(3))
            if target is None:
                target = (report.index.parent / "__invalid_destination__").resolve()
            entry = IndexEntry(
                int(match.group(1)),
                match.group(2).strip(),
                match.group(3),
                target,
            )
            report.entries.append(entry)
            if entry.number < 1:
                report.errors.append(
                    f"index lemma number must be positive: {entry.number}"
                )
            if entry.number in seen_entry_numbers:
                report.errors.append(f"duplicate index number {entry.number}")
            if entry.target in seen_targets:
                report.errors.append(
                    f"duplicate index target {entry.target.relative_to(root) if entry.target.is_relative_to(root) else entry.target}"
                )
            seen_entry_numbers.add(entry.number)
            seen_targets.add(entry.target)

            lemma = path_to_lemma.get(entry.target)
            if lemma is None:
                report.errors.append(
                    f"index entry Lemma {entry.number} points to a missing or non-lemma file: {entry.destination}"
                )
                continue
            if entry.number != lemma.number or entry.title != lemma.title:
                report.errors.append(
                    "index/H1 mismatch for "
                    f"{lemma.path.relative_to(root)}: index has Lemma {entry.number} — {entry.title}; "
                    f"file has Lemma {lemma.number} — {lemma.title}"
                )

        entry_numbers = [entry.number for entry in report.entries]
        if entry_numbers != sorted(entry_numbers):
            report.errors.append("lemma index entries are not in ascending numeric order")

        lemma_paths = set(path_to_lemma)
        missing = sorted(lemma_paths - seen_targets)
        for path in missing:
            report.errors.append(f"lemma missing from index: {path.relative_to(root)}")

    lemma_paths = set(path_to_lemma)
    for source in markdown_files(root):
        links = collect_links(source, lemma_paths)
        if source.resolve() in lemma_paths:
            report.internal_links.extend(links)
        elif report.index is None or source.resolve() != report.index:
            report.backlinks.extend(links)

    report.lemmas.sort(key=lambda record: (record.number, str(record.path)))
    report.internal_links.sort(key=lambda link: (str(link.source), link.line, str(link.target)))
    report.backlinks.sort(key=lambda link: (str(link.source), link.line, str(link.target)))
    return report


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def render_report(report: RegistryReport) -> str:
    lines: list[str] = []
    if report.index:
        lines.append(f"Registry index: {relative(report.index, report.root)}")
    lines.append(f"Canonical lemmas: {len(report.lemmas)}")
    lines.append("Intra-lemma links:")
    if report.internal_links:
        for link in report.internal_links:
            lines.append(
                f"  {relative(link.source, report.root)}:{link.line} -> {relative(link.target, report.root)}"
            )
    else:
        lines.append("  none")
    lines.append("Repository backlinks:")
    if report.backlinks:
        for link in report.backlinks:
            lines.append(
                f"  {relative(link.source, report.root)}:{link.line} -> {relative(link.target, report.root)}"
            )
    else:
        lines.append("  none")
    if report.errors:
        lines.append("Errors:")
        lines.extend(f"  - {error}" for error in report.errors)
        lines.append(f"Registry status: FAIL ({len(report.errors)} error(s))")
    else:
        lines.append("Registry status: OK")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="vault root")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    report = inspect_registry(args.root)
    print(render_report(report))
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
