import importlib.util
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
            with zipfile.ZipFile(path, "w") as zf:
                zf.writestr("xl/workbook.xml", '<?xml version="1.0"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Inputs" sheetId="1" r:id="rId1"/></sheets></workbook>')
                zf.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
                zf.writestr("xl/worksheets/sheet1.xml", '<?xml version="1.0"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1"><f>#REF!+1</f><v>#REF!</v></c></row></sheetData></worksheet>')
            report = MODULE.audit_workbook(path)
            self.assertEqual("fail", report["status"])
            self.assertIn("broken-reference", {f["code"] for f in report["findings"]})


if __name__ == "__main__":
    unittest.main()
