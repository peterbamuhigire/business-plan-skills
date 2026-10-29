import importlib.util
import json
import subprocess
import tempfile
import unittest
import zipfile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "formula_map", ROOT / "tools/workbook-audit/formula_map.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FormulaMapTests(unittest.TestCase):
    @staticmethod
    def write_broken_workbook(path):
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("xl/workbook.xml", '<?xml version="1.0"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Inputs" sheetId="1" r:id="rId1"/></sheets></workbook>')
            zf.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
            zf.writestr("xl/worksheets/sheet1.xml", '<?xml version="1.0"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1"><f>#REF!+1</f><v>#REF!</v></c></row></sheetData></worksheet>')

    @staticmethod
    def write_reconciliation_workbook(path, left="100", right="100", cached="0"):
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("xl/workbook.xml", '<?xml version="1.0"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Model" sheetId="1" r:id="rId1"/></sheets></workbook>')
            zf.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
            zf.writestr("xl/worksheets/sheet1.xml", f'<?xml version="1.0"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="B1"><v>{left}</v></c><c r="B2"><v>{right}</v></c><c r="B3"><f>B1-B2</f><v>{cached}</v></c></row></sheetData></worksheet>')

    @staticmethod
    def write_reconciliation_contract(path):
        path.write_text(json.dumps({"schema_version": "1.0.0", "checks": [
            {"id": "cash-to-balance", "left_cell": "Model!B1", "right_cell": "Model!B2",
             "check_cell": "Model!B3", "tolerance": 0}
        ]}), encoding="utf-8")

    def test_repository_workbooks_have_no_broken_links(self):
        workbooks = list((ROOT / "skills").glob("**/templates/*.xlsx"))
        self.assertEqual(7, len(workbooks))
        for workbook in workbooks:
            with self.subTest(workbook=workbook):
                report = MODULE.audit_workbook(workbook)
                self.assertEqual("pass", report["status"], report["findings"])
                self.assertGreater(report["formula_count"], 0)

    def test_broken_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "broken.xlsx"
            self.write_broken_workbook(path)
            report = MODULE.audit_workbook(path)
            self.assertEqual("fail", report["status"])
            self.assertIn("broken-reference", {f["code"] for f in report["findings"]})

    def test_output_alias_matches_json_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "broken.xlsx"
            self.write_broken_workbook(path)
            original = path.read_bytes()
            expected = MODULE.audit_workbook(path)
            for option in ("--json-out", "--output"):
                with self.subTest(option=option):
                    output = Path(tmp) / option.lstrip("-") / "report.json"
                    markdown = output.with_suffix(".md")
                    result = subprocess.run(
                        [sys.executable, "-B", "-X", "utf8", str(SPEC.origin),
                         str(path), option, str(output), "--markdown-out", str(markdown)],
                        capture_output=True, text=True, encoding="utf-8", check=False,
                    )
                    self.assertEqual(1, result.returncode, result.stdout + result.stderr)
                    self.assertIn("FAIL:", result.stdout)
                    self.assertEqual(expected, json.loads(output.read_text(encoding="utf-8")))
                    self.assertEqual(MODULE.markdown_report(expected),
                                     markdown.read_text(encoding="utf-8"))
                    self.assertEqual(original, path.read_bytes())

    def test_literal_reconciliation_passes_for_matching_values(self):
        with tempfile.TemporaryDirectory() as temp:
            path, contract = Path(temp) / "matched.xlsx", Path(temp) / "checks.json"
            self.write_reconciliation_workbook(path)
            self.write_reconciliation_contract(contract)
            report = MODULE.audit_workbook(path, reconciliation_checks=contract,
                                          require_reconciliation=True)
            self.assertEqual("pass", report["reconciliation"]["status"])
            self.assertEqual("pass", report["status"])
            self.assertEqual(64, len(report["workbook_sha256"]))

    def test_literal_reconciliation_rejects_mismatch_and_stale_or_blank_cache(self):
        with tempfile.TemporaryDirectory() as temp:
            contract = Path(temp) / "checks.json"
            self.write_reconciliation_contract(contract)
            for right, cached, expected in (("80", "20", "reconciliation-values-differ"),
                                            ("80", "", "reconciliation-values-differ"),
                                            ("100", "", "reconciliation-cache-missing"),
                                            ("100", "1", "reconciliation-cache-does-not-match-inputs")):
                with self.subTest(right=right, cached=cached):
                    path = Path(temp) / f"case-{right}-{cached or 'blank'}.xlsx"
                    self.write_reconciliation_workbook(path, right=right, cached=cached)
                    report = MODULE.audit_workbook(path, reconciliation_checks=contract,
                                                  require_reconciliation=True)
                    self.assertEqual("fail", report["reconciliation"]["status"])
                    self.assertIn(expected, {finding["code"] for finding in report["findings"]})

    def test_required_reconciliation_contract_cannot_be_omitted(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "matched.xlsx"
            self.write_reconciliation_workbook(path)
            report = MODULE.audit_workbook(path, require_reconciliation=True)
            self.assertEqual("fail", report["reconciliation"]["status"])
            self.assertIn("missing-reconciliation-contract",
                          {finding["code"] for finding in report["findings"]})

    def test_non_finite_or_unrepresentable_tolerance_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path, contract = Path(temp) / "matched.xlsx", Path(temp) / "checks.json"
            self.write_reconciliation_workbook(path)
            contract.write_text(json.dumps({"schema_version": "1.0.0", "checks": [
                {"id": "huge-tolerance", "left_cell": "Model!B1", "right_cell": "Model!B2",
                 "check_cell": "Model!B3", "tolerance": 10 ** 1000}
            ]}), encoding="utf-8")
            report = MODULE.audit_workbook(path, reconciliation_checks=contract,
                                          require_reconciliation=True)
            self.assertEqual("fail", report["reconciliation"]["status"])
            self.assertIn("invalid-reconciliation-tolerance",
                          {finding["code"] for finding in report["findings"]})


if __name__ == "__main__":
    unittest.main()
