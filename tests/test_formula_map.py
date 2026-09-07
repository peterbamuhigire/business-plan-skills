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


if __name__ == "__main__":
    unittest.main()
