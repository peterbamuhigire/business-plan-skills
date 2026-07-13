import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evidence_register", ROOT / "tools/evidence-register/refresh_evidence_register.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class EvidenceRegisterTests(unittest.TestCase):
    def test_repository_register_is_current(self):
        self.assertEqual([], MODULE.validate(MODULE.DEFAULT_REGISTER, date(2026, 7, 13)))

    def test_overdue_entry_fails(self):
        source = json.loads(MODULE.DEFAULT_REGISTER.read_text(encoding="utf-8"))
        source["entries"][0]["recheck_due"] = "2026-01-01"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "register.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            errors = MODULE.validate(path, date(2026, 7, 13))
        self.assertTrue(any("overdue" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
