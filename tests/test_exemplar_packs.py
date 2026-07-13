import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("packs", ROOT / "tools/exemplar-packs/validate_exemplar_packs.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ExemplarPackTests(unittest.TestCase):
    def test_complete_packs(self):
        self.assertEqual([], MODULE.validate())


if __name__ == "__main__":
    unittest.main()
