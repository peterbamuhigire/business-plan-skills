import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "source_ingestion_guardrail_content", ROOT / "scripts/source_ingestion_guardrail.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

DIGEST = "**Source:** Fictional Author (2001) *Fictional Book*.\n\n" + "".join(
    f"## Chapter {n} - Topic\ntext\n\n" for n in range(1, 5)
)


def make(root: str, relative: str, text: str) -> Path:
    base = Path(root)
    path = base / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return base


class ContentAwareGuardrailTests(unittest.TestCase):
    def test_single_source_chapter_structure_is_warned(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = make(temporary, "skills/demo/references/digest.md", DIGEST)
            self.assertEqual(["single-source-chapter-structure"], [w.code for w in MODULE.scan_content(root)])

    def test_key_quotes_section_is_warned(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = make(temporary, "skills/demo/references/quotes.md", "# Topic\n\n## Key Quotes\n- x\n")
            self.assertEqual(["key-quotes-section"], [w.code for w in MODULE.scan_content(root)])

    def test_task_reference_and_exempt_guides_are_not_warned(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = make(temporary, "skills/demo/references/task.md", "# Task\n\n## Step 1\ntext\n")
            make(temporary, "skills/industry-guides/x/references/profile.md", DIGEST)
            self.assertEqual([], MODULE.scan_content(root))

    def test_content_warnings_are_blocking(self):
        self.assertTrue(MODULE.CONTENT_CHECK_BLOCKING)
        with tempfile.TemporaryDirectory() as temporary:
            make(temporary, "skills/demo/references/digest.md", DIGEST)
            original = sys.argv
            try:
                sys.argv = ["guardrail", "--root", temporary]
                self.assertEqual(1, MODULE.main())
                sys.argv = ["guardrail", "--root", temporary, "--strict-content"]
                self.assertEqual(1, MODULE.main())
            finally:
                sys.argv = original


if __name__ == "__main__":
    unittest.main()
