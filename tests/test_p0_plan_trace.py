import copy
import importlib.util
import json
import unittest
from pathlib import Path

MODULE = importlib.util.spec_from_file_location("validate_plan_trace", Path(__file__).parents[1] / "tools" / "evidence-register" / "validate_plan_trace.py")
assert MODULE and MODULE.loader
VALIDATOR = importlib.util.module_from_spec(MODULE)
MODULE.loader.exec_module(VALIDATOR)


class PlanTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((Path(__file__).parent / "fixtures" / "p0-lender-trace.json").read_text(encoding="utf-8"))

    def test_fictional_trace_and_recalculation_pass(self):
        self.assertEqual(VALIDATOR.validate(self.data), [])

    def test_orphan_cell_fails(self):
        data = copy.deepcopy(self.data)
        data["claims"][0]["cell_ids"] = ["CELL-MISSING"]
        self.assertTrue(any("unknown cell" in e for e in VALIDATOR.validate(data)))

    def test_wrong_recalculation_fails(self):
        data = copy.deepcopy(self.data)
        data["recalculation"]["revenue"] = 1100
        self.assertIn("recalculated revenue does not equal units times price", VALIDATOR.validate(data))
