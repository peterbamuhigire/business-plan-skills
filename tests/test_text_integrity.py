"""Text-integrity guard: wrong numbers and stripped characters must not return."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_text_integrity", ROOT / "scripts" / "check_text_integrity.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)

EN_DASH = "–"


class TextIntegrityTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "skills").mkdir()
        (self.root / "docs").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def problems(self, hashes: Path | None = None) -> list[str]:
        return MODULE.validate_text_integrity(self.root, hashes or self.root / "absent.txt")

    def test_clean_text_with_real_ranges_passes(self):
        self.write("skills/a.md", f"Inflation 3{EN_DASH}5% in 2025{EN_DASH}26; wages UGX 2,000,000{EN_DASH}6,000,000.\n")
        self.assertEqual([], self.problems())

    def test_glued_year_range_is_flagged(self):
        self.write("skills/a.md", "Uganda macroeconomic context (202526) is current.\n")
        self.assertTrue(any("glued-year-range" in item for item in self.problems()))

    def test_glued_thousands_groups_are_flagged(self):
        self.write("skills/a.md", "Professional wages UGX 2,000,0006,000,000 per month.\n")
        self.assertTrue(any("glued-thousands-groups" in item for item in self.problems()))

    def test_glued_decimal_range_is_flagged(self):
        self.write("skills/a.md", "Policy rate 9.7510.5% range.\n")
        self.assertTrue(any("glued-decimal-range" in item for item in self.problems()))

    def test_control_and_replacement_characters_are_flagged(self):
        self.write("skills/a.md", "The table below\x01consolidates the rows.\n")
        self.write("skills/b.md", "Broken � text.\n")
        found = self.problems()
        self.assertTrue(any("a.md:1" in item for item in found))
        self.assertTrue(any("b.md:1" in item for item in found))

    def test_byte_order_mark_on_first_line_is_allowed(self):
        self.write("skills/a.md", "﻿# Title\n")
        self.assertEqual([], self.problems())

    def test_known_stripped_line_is_flagged_by_hash(self):
        damaged = "| Timeline | 25 business days (online); delays possible |"
        hashes = self.root / "hashes.txt"
        hashes.write_text(MODULE.digest(damaged) + "\n", encoding="utf-8")
        self.write("skills/a.md", damaged + "\n")
        self.assertTrue(any("known stripped-operator" in item for item in self.problems(hashes)))
        self.write("skills/a.md", f"| Timeline | 2{EN_DASH}5 business days (online); delays possible |\n")
        self.assertEqual([], self.problems(hashes))

    def test_docs_history_is_out_of_scope(self):
        self.write("docs/history.md", "Old note (202526) kept as written.\n")
        self.assertEqual([], self.problems())

    def test_repository_is_clean(self):
        self.assertEqual([], MODULE.validate_text_integrity(ROOT))

    def test_repository_hash_fixture_is_present_and_non_trivial(self):
        hashes = MODULE.load_hashes(ROOT / MODULE.HASH_FIXTURE)
        self.assertGreater(len(hashes), 200)


if __name__ == "__main__":
    unittest.main()
