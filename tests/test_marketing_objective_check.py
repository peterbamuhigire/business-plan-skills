import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_objectives", ROOT / "tools/objective-check/check_objectives.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
FIXTURES = json.loads((ROOT / "tests/fixtures/marketing-objectives.json").read_text(encoding="utf-8"))


class MarketingObjectiveCheckTests(unittest.TestCase):
    def test_reconciled_structured_objective_passes(self):
        for item in FIXTURES["structured_pass"]:
            self.assertEqual([], MODULE.check_structured(item))

    def test_vague_or_incomplete_structured_objectives_fail(self):
        expected = {
            "wish": {"vague-goal-phrase", "metric-undefined", "segment-generic", "place-missing-or-too-wide",
                     "baseline-missing", "target-missing", "line-source-missing", "deadline-missing", "owner-missing"},
            "no baseline or line source": {"baseline-missing", "line-source-missing"},
            "no deadline": {"deadline-missing"},
            "arithmetic not reconciled": {"arithmetic-not-reconciled"},
            "country-wide place for a city business": {"place-missing-or-too-wide"},
        }
        for item in FIXTURES["structured_fail"]:
            failures = set(MODULE.check_structured(item))
            self.assertTrue(expected[item["name"]] <= failures, (item["name"], failures))

    def test_smart_sentences_pass(self):
        for text in FIXTURES["sentence_pass"]:
            self.assertEqual([], MODULE.check_sentence(text), text)

    def test_vague_sentences_fail(self):
        for text in FIXTURES["sentence_fail"]:
            self.assertTrue(MODULE.check_sentence(text), text)


if __name__ == "__main__":
    unittest.main()
