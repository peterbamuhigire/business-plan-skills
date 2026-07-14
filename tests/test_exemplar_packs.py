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

    def test_release_bundles_are_structurally_valid_and_blocked(self):
        spec = importlib.util.spec_from_file_location(
            "release_bundle", ROOT / "tools/release-gate/validate_release_bundle.py"
        )
        release_module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = release_module
        spec.loader.exec_module(release_module)
        for pack in MODULE.EXPECTED:
            path = MODULE.PACK_ROOT / pack / "release-bundle.json"
            self.assertEqual([], release_module.validate(path), pack)


if __name__ == "__main__":
    unittest.main()
