#!/usr/bin/env python3
"""Fixtures for inspect_lemma_registry.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from inspect_lemma_registry import inspect_registry


INDEX_FRONTMATTER = "---\ntype: lemma-index\nmodule: lemmas\nstatus: canonical\n---\n\n"
LEMMA_FRONTMATTER = "---\ntype: lemma\nmodule: lemmas\nstatus: canonical\n---\n\n"


class RegistryFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "80_Lemmas").mkdir()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def seed_valid_registry(self) -> None:
        self.write(
            "80_Lemmas/INDEX.md",
            INDEX_FRONTMATTER
            + "# Lemma Index\n\n"
            + "- [Lemma 1 — First Result](First%20Result.md)\n"
            + "- [Lemma 2 — Second Result](Second%20Result.md)\n",
        )
        self.write(
            "80_Lemmas/First Result.md",
            LEMMA_FRONTMATTER + "# Lemma 1 — First Result\n",
        )
        self.write(
            "80_Lemmas/Second Result.md",
            LEMMA_FRONTMATTER
            + "# Lemma 2 — Second Result\n\n"
            + "See [Lemma 1](First%20Result.md).\n",
        )
        self.write(
            "10_Module/01_Cours/Cours.md",
            "Use [Lemma 2](../../80_Lemmas/Second%20Result.md).\n",
        )

    def test_valid_registry_and_backlinks(self) -> None:
        self.seed_valid_registry()
        report = inspect_registry(self.root)
        self.assertTrue(report.ok, report.errors)
        self.assertEqual(2, len(report.lemmas))
        self.assertEqual(1, len(report.internal_links))
        self.assertEqual(1, len(report.backlinks))
        self.assertEqual("INDEX.md", report.index.name)

    def test_duplicate_number_is_rejected(self) -> None:
        self.seed_valid_registry()
        self.write(
            "80_Lemmas/Third Result.md",
            LEMMA_FRONTMATTER + "# Lemma 2 — Third Result\n",
        )
        report = inspect_registry(self.root)
        self.assertFalse(report.ok)
        self.assertTrue(any("duplicate lemma number 2" in error for error in report.errors))

    def test_missing_index_entry_is_rejected(self) -> None:
        self.seed_valid_registry()
        self.write(
            "80_Lemmas/Third Result.md",
            LEMMA_FRONTMATTER + "# Lemma 3 — Third Result\n",
        )
        report = inspect_registry(self.root)
        self.assertFalse(report.ok)
        self.assertTrue(any("lemma missing from index" in error for error in report.errors))

    def test_title_mismatch_is_rejected(self) -> None:
        self.seed_valid_registry()
        index = self.root / "80_Lemmas/INDEX.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace("Second Result]", "Wrong Title]"),
            encoding="utf-8",
        )
        report = inspect_registry(self.root)
        self.assertFalse(report.ok)
        self.assertTrue(any("index/H1 mismatch" in error for error in report.errors))

    def test_bad_index_path_is_rejected(self) -> None:
        self.seed_valid_registry()
        index = self.root / "80_Lemmas/INDEX.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "Second%20Result.md", "Missing%20Result.md"
            ),
            encoding="utf-8",
        )
        report = inspect_registry(self.root)
        self.assertFalse(report.ok)
        self.assertTrue(
            any("missing or non-lemma file" in error for error in report.errors)
        )

    def test_nonpositive_number_is_rejected(self) -> None:
        self.write(
            "80_Lemmas/INDEX.md",
            INDEX_FRONTMATTER
            + "# Lemma Index\n\n"
            + "- [Lemma 0 — Zero Result](Zero%20Result.md)\n",
        )
        self.write(
            "80_Lemmas/Zero Result.md",
            LEMMA_FRONTMATTER + "# Lemma 0 — Zero Result\n",
        )
        report = inspect_registry(self.root)
        self.assertFalse(report.ok)
        self.assertTrue(any("must be positive" in error for error in report.errors))


if __name__ == "__main__":
    unittest.main()
