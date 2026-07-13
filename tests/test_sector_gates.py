import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sector_gates", ROOT / "tools/sector-gates/validate_sector_gates.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SectorGateTests(unittest.TestCase):
    def test_repository_gate_contract(self):
        self.assertEqual([], MODULE.validate())
        self.assertEqual(4, len(MODULE.checklist(["food-processing", "retail-ecommerce-trade"])))

    def test_unknown_sector_fails(self):
        with self.assertRaises(ValueError):
            MODULE.checklist(["imaginary-sector"])


if __name__ == "__main__":
    unittest.main()
