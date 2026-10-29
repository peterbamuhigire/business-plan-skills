import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "release_bundle", ROOT / "tools/release-gate/validate_release_bundle.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReleaseBundleTests(unittest.TestCase):
    @staticmethod
    def _workbook(path: Path, left: str = "100", right: str = "100", cached: str = "0") -> None:
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("xl/workbook.xml", '<?xml version="1.0"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Model" sheetId="1" r:id="rId1"/></sheets></workbook>')
            zf.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
            zf.writestr("xl/worksheets/sheet1.xml", f'<?xml version="1.0"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="B1"><v>{left}</v></c><c r="B2"><v>{right}</v></c><c r="B3"><f>B1-B2</f><v>{cached}</v></c></row></sheetData></worksheet>')

    @staticmethod
    def _audit(workbook: Path, contract: Path) -> dict:
        from runpy import run_path
        audit = run_path(str(ROOT / "tools/workbook-audit/formula_map.py"))["audit_workbook"]
        return audit(workbook, reconciliation_checks=contract, require_reconciliation=True)

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

    def test_passing_xlsx_handoff_requires_matching_reconciliation_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            path = self._bundle(directory)
            workbook = directory / "model.xlsx"
            self._workbook(workbook)
            contract_path = directory / "checks.json"
            contract_path.write_text(json.dumps({"schema_version": "1.0.0", "checks": [
                {"id": "cash", "left_cell": "Model!B1", "right_cell": "Model!B2",
                 "check_cell": "Model!B3", "tolerance": 0}
            ]}), encoding="utf-8")
            report_path = directory / "audit.json"
            report = self._audit(workbook, contract_path)
            report_path.write_text(json.dumps(report), encoding="utf-8")
            data = json.loads(path.read_text(encoding="utf-8"))
            spreadsheet = data["handoffs"]["spreadsheet"]
            spreadsheet["input_versions"] = ["model.xlsx"]
            spreadsheet["reconciliation_report"] = "audit.json"
            spreadsheet["reconciliation_contract"] = "checks.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual([], MODULE.validate(path))

            report["workbook_sha256"] = "0" * 64
            report_path.write_text(json.dumps(report), encoding="utf-8")
            self.assertTrue(any("does not match the workbook audit" in error
                                for error in MODULE.validate(path)))

            report = self._audit(workbook, contract_path)
            report["reconciliation"]["checks"][0]["status"] = "fail"
            report_path.write_text(json.dumps(report), encoding="utf-8")
            self.assertTrue(any("does not match recomputed check results" in error
                                for error in MODULE.validate(path)))

    def test_passing_xlsx_handoff_without_reconciliation_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            path = self._bundle(directory)
            workbook = directory / "model.xlsx"
            self._workbook(workbook)
            data = json.loads(path.read_text(encoding="utf-8"))
            data["handoffs"]["spreadsheet"]["input_versions"] = ["model.xlsx"]
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("requires reconciliation_report" in error
                                for error in MODULE.validate(path)))

    def test_forged_pass_report_cannot_override_a_real_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            path = self._bundle(directory)
            workbook = directory / "model.xlsx"
            self._workbook(workbook, left="100", right="80", cached="20")
            contract = directory / "checks.json"
            contract.write_text(json.dumps({"schema_version": "1.0.0", "checks": [
                {"id": "cash", "left_cell": "Model!B1", "right_cell": "Model!B2",
                 "check_cell": "Model!B3", "tolerance": 0}
            ]}), encoding="utf-8")
            forged = {"status": "pass", "workbook_sha256": "unused",
                      "reconciliation": {"status": "pass", "checks": [{"id": "cash", "status": "pass"}]}}
            report = directory / "audit.json"
            report.write_text(json.dumps(forged), encoding="utf-8")
            data = json.loads(path.read_text(encoding="utf-8"))
            data["handoffs"]["spreadsheet"]["input_versions"] = ["model.xlsx"]
            data["handoffs"]["spreadsheet"]["reconciliation_report"] = "audit.json"
            data["handoffs"]["spreadsheet"]["reconciliation_contract"] = "checks.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            errors = MODULE.validate(path)
            self.assertTrue(any("recomputed workbook reconciliation" in error for error in errors))

    def test_non_object_payloads_are_findings(self):
        with tempfile.TemporaryDirectory() as temp:
            path = self._bundle(Path(temp))
            for value in (None, [], "release", 1, True):
                with self.subTest(value=value):
                    path.write_text(json.dumps(value), encoding="utf-8")
                    self.assertEqual(["bundle must be an object"], MODULE.validate(path))

    def test_malformed_nested_fields_reject_without_crashing(self):
        fields = [
            ("stages", 0, "id"), ("stages", 0, "state"),
            ("stages", 0, "owner"), ("handoffs", "research", "state"),
            ("handoffs", "research", "receiver"),
            ("finalisation", "render", "state"),
            ("finalisation", "render", "required"),
            ("release_authority", "state"), ("release_authority", "required"),
            ("release_authority", "role"), ("release_state",),
        ]
        with tempfile.TemporaryDirectory() as temp:
            for fields_path in fields:
                for invalid in ([], {}, None):
                    with self.subTest(path=fields_path, invalid=invalid):
                        path = self._bundle(Path(temp))
                        data = json.loads(path.read_text(encoding="utf-8"))
                        target = data
                        for key in fields_path[:-1]:
                            target = target[key]
                        target[fields_path[-1]] = invalid
                        path.write_text(json.dumps(data), encoding="utf-8")
                        self.assertTrue(MODULE.validate(path))

    def test_required_flags_cannot_be_omitted(self):
        with tempfile.TemporaryDirectory() as temp:
            path = self._bundle(Path(temp))
            data = json.loads(path.read_text(encoding="utf-8"))
            del data["finalisation"]["render"]["required"]
            del data["release_authority"]["required"]
            path.write_text(json.dumps(data), encoding="utf-8")
            errors = MODULE.validate(path)
            self.assertEqual(2, sum("required must be boolean" in e for e in errors))

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
