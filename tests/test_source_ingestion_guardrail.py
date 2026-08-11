import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WAVE_2_SYNTHESIS_PATHS = (
    ROOT / "skills/industry-guides/agriculture/references/oyster-mushroom-drying.md",
    ROOT / "skills/industry-guides/food-processing/references/water-distillation.md",
    ROOT / "skills/industry-guides/manufacturing-light/references/ptfe-coated-cookware.md",
    ROOT / "skills/industry-guides/retail/references/grain-grocery.md",
)
SPEC = importlib.util.spec_from_file_location(
    "source_ingestion_guardrail", ROOT / "scripts/source_ingestion_guardrail.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SourceIngestionGuardrailTests(unittest.TestCase):
    def test_wave_2_syntheses_are_attributed_and_independently_written(self):
        for path in WAVE_2_SYNTHESIS_PATHS:
            self.assertTrue(path.is_file(), path)
            content = path.read_text(encoding="utf-8")
            normalised = " ".join(content.split())
            self.assertIn("Source attribution:", content, path)
            self.assertIn("Independently written synthesis", content, path)
            self.assertIn("tracked raw extraction is removed", normalised, path)

    def test_raw_extraction_directory_is_blocked_even_when_fixture_is_small(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "skills/industry-guides/_extraction/fictional-test-raw.md"
            path.parent.mkdir(parents=True)
            path.write_text("TEST FIXTURE ONLY\n", encoding="utf-8")

            findings = MODULE.scan(root)

            self.assertEqual(["raw-extraction-path"], [finding.code for finding in findings])
            self.assertEqual(path.relative_to(root), findings[0].path)

    def test_book_extraction_synthesis_path_is_not_blocked_by_name_alone(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "book-extractions/fictional-test-synthesis.md"
            path.parent.mkdir(parents=True)
            path.write_text("TEST FIXTURE ONLY: concise synthesis.\n", encoding="utf-8")

            self.assertEqual([], MODULE.scan(root))

    def test_raw_extractions_variant_is_blocked_case_insensitively(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "skills/industry-guides/_EXTRACTIONS/fictional-test-raw.md"
            path.parent.mkdir(parents=True)
            path.write_text("TEST FIXTURE ONLY\n", encoding="utf-8")

            findings = MODULE.scan(root)

            self.assertEqual(["raw-extraction-path"], [finding.code for finding in findings])
            self.assertEqual(path.relative_to(root), findings[0].path)

    def test_large_full_text_renamed_outside_raw_path_is_still_blocked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "references/approved-looking-synthesis.md"
            path.parent.mkdir(parents=True)
            marker_block = "ISBN: 9781234567890\nCopyright 2024\nAll rights reserved\n"
            path.write_text(marker_block * 1000, encoding="utf-8")

            findings = MODULE.scan(root)

            self.assertEqual(["source-fulltext-markers"], [finding.code for finding in findings])
            self.assertEqual(path.relative_to(root), findings[0].path)

    def test_raw_ebook_is_blocked_regardless_of_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "tests/fixtures/fictional-test-source.epub"
            path.parent.mkdir(parents=True)
            path.write_bytes(b"TEST FIXTURE ONLY")

            findings = MODULE.scan(root)

            self.assertEqual(["raw-book-source"], [finding.code for finding in findings])


if __name__ == "__main__":
    unittest.main()
