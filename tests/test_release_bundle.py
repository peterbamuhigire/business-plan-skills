import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "release_bundle", ROOT / "tools/release-gate/validate_release_bundle.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReleaseBundleTests(unittest.TestCase):
    def _bundle(self, directory: Path) -> Path:
        evidence = directory / "evidence.txt"
        evidence.write_text("verified test evidence", encoding="utf-8")
        record = {
            "schema_version": "1.0.0",
            "artefact": "Test plan",
            "audience": "test reviewer",
            "release_state": "release",
            "release_authority": {"required": True, "state": "pass", "role": "Owner", "evidence": ["evidence.txt"]},
            "stages": [
                {"id": name, "state": "pass", "owner": "Owner", "evidence": ["evidence.txt"]}
                for name in sorted(MODULE.STAGES)
            ],
            "handoffs": {
                name: {"applicable": True, "input_versions": ["evidence.txt"], "requested_decision": f"Accept {name} handoff", "state": "pass", "receiver": "Reviewer", "evidence": ["evidence.txt"], "caveats": []}
                for name in MODULE.HANDOFFS
            },
            "finalisation": {
                "render": {"required": True, "state": "pass", "evidence": ["evidence.txt"]},
                "reviewer_notes": ["evidence.txt"],
                "audit_log": ["evidence.txt"],
                "release_checklist": ["evidence.txt"]
            },
            "blockers": []
        }
        path = directory / "release-bundle.json"
        path.write_text(json.dumps(record), encoding="utf-8")
        return path

    def test_complete_bundle_releases(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual([], MODULE.validate(self._bundle(Path(temp))))

    def test_missing_render_blocks_release(self):
        with tempfile.TemporaryDirectory() as temp:
            path = self._bundle(Path(temp))
            data = json.loads(path.read_text(encoding="utf-8"))
            data["finalisation"]["render"] = {"required": True, "state": "not-assessed", "evidence": []}
            path.write_text(json.dumps(data), encoding="utf-8")
            errors = MODULE.validate(path)
            self.assertTrue(any("blocker precedence" in error for error in errors))

    def test_non_applicable_handoff_needs_reason(self):
        with tempfile.TemporaryDirectory() as temp:
            path = self._bundle(Path(temp))
            data = json.loads(path.read_text(encoding="utf-8"))
            data["handoffs"]["security"] = {"applicable": False, "input_versions": [], "requested_decision": "Confirm exemption", "state": "not-applicable", "receiver": "Reviewer", "evidence": [], "caveats": []}
            data["release_state"] = "blocked"
            data["blockers"] = [{"id": "T", "owner": "Owner", "finding": "Reason missing", "recovery": "Add reason"}]
            path.write_text(json.dumps(data), encoding="utf-8")
            errors = MODULE.validate(path)
            self.assertTrue(any("needs reason" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
