#!/usr/bin/env python3
"""Inspect XLSX formula structure using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "p": "http://schemas.openxmlformats.org/package/2006/relationships"}
ERROR_VALUES = {"#NULL!", "#DIV/0!", "#VALUE!", "#REF!", "#NAME?", "#NUM!", "#N/A"}
SCENARIO_RE = re.compile(r"\b(base|bull|bear|downside|upside|stress|scenario)\b", re.I)
BALANCE_RE = re.compile(r"balance|tie[- ]?out|reconcil|opening|closing|ending|dscr|check", re.I)
SHEET_REF_RE = re.compile(r"(?<![A-Za-z0-9_.])(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_. ]*))!")


@dataclass
class Finding:
    severity: str
    code: str
    location: str
    message: str


def _xml(zf: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(zf.read(name))


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = _xml(zf, "xl/sharedStrings.xml")
    return ["".join(t.text or "" for t in si.findall(".//m:t", NS))
            for si in root.findall("m:si", NS)]


def _cell_text(cell: ET.Element, shared: list[str]) -> str:
    value = cell.findtext("m:v", default="", namespaces=NS)
    if cell.get("t") == "s" and value.isdigit() and int(value) < len(shared):
        return shared[int(value)]
    inline = cell.find("m:is", NS)
    if inline is not None:
        return "".join(t.text or "" for t in inline.findall(".//m:t", NS))
    return value


def audit_workbook(path: str | Path, require_scenarios: bool = False,
                   require_balance_checks: bool = False) -> dict:
    workbook = Path(path)
    findings: list[Finding] = []
    formulas: list[dict] = []
    assumptions: list[dict] = []
    scenario_hits: list[dict] = []
    balance_hits: list[dict] = []
    external_links: list[dict] = []

    with zipfile.ZipFile(workbook) as zf:
        shared = _shared_strings(zf)
        wb = _xml(zf, "xl/workbook.xml")
        rels = _xml(zf, "xl/_rels/workbook.xml.rels")
        targets = {r.get("Id"): r.get("Target") for r in rels.findall("p:Relationship", NS)}
        sheets: list[tuple[str, str]] = []
        for sheet in wb.findall("m:sheets/m:sheet", NS):
            target = targets.get(sheet.get(f"{{{NS['r']}}}id"), "")
            if target.startswith("/"):
                part = target.lstrip("/")
            else:
                part = str(Path("xl") / target).replace("\\", "/")
            sheets.append((sheet.get("name", ""), part))
        sheet_names = {name for name, _ in sheets}

        defined_names = []
        for node in wb.findall("m:definedNames/m:definedName", NS):
            item = {"name": node.get("name", ""), "formula": node.text or ""}
            defined_names.append(item)
            combined = f"{item['name']} {item['formula']}"
            if SCENARIO_RE.search(combined):
                scenario_hits.append({"location": "defined-name", "value": combined})
            if BALANCE_RE.search(combined):
                balance_hits.append({"location": "defined-name", "value": combined})

        for sheet_name, part in sheets:
            if part not in zf.namelist():
                findings.append(Finding("error", "missing-sheet-part", sheet_name, part))
                continue
            root = _xml(zf, part)
            assumption_sheet = bool(re.search(r"input|assumption", sheet_name, re.I))
            if SCENARIO_RE.search(sheet_name):
                scenario_hits.append({"location": sheet_name, "value": "sheet-name"})
            if BALANCE_RE.search(sheet_name):
                balance_hits.append({"location": sheet_name, "value": "sheet-name"})
            for cell in root.findall(".//m:c", NS):
                ref = cell.get("r", "?")
                location = f"{sheet_name}!{ref}"
                formula = cell.findtext("m:f", default="", namespaces=NS)
                value = _cell_text(cell, shared)
                if assumption_sheet and not formula and value:
                    assumptions.append({"location": location, "value": value})
                combined = f"{formula} {value}"
                if SCENARIO_RE.search(combined):
                    scenario_hits.append({"location": location, "value": combined[:160]})
                if BALANCE_RE.search(combined):
                    balance_hits.append({"location": location, "value": combined[:160]})
                if not formula:
                    continue
                formulas.append({"location": location, "formula": formula, "cached_value": value})
                if "#REF!" in formula:
                    findings.append(Finding("error", "broken-reference", location, formula))
                if value in ERROR_VALUES:
                    findings.append(Finding("error", "cached-formula-error", location, value))
                if re.search(r"\[[^\]]+\]", formula):
                    external_links.append({"location": location, "formula": formula})
                    findings.append(Finding("error", "external-workbook-link", location, formula))
                for match in SHEET_REF_RE.finditer(formula):
                    referenced = (match.group(1) or match.group(2) or "").strip()
                    if referenced and referenced not in sheet_names:
                        findings.append(Finding("error", "missing-sheet-reference", location, referenced))

    if require_scenarios and not scenario_hits:
        findings.append(Finding("error", "missing-scenario-checks", str(workbook),
                                "No base, downside, stress, or scenario evidence found"))
    if require_balance_checks and not balance_hits:
        findings.append(Finding("error", "missing-balance-checks", str(workbook),
                                "No balance, reconciliation, tie-out, or check evidence found"))
    failures = [asdict(f) for f in findings if f.severity == "error"]
    return {
        "workbook": workbook.as_posix(),
        "status": "pass" if not failures else "fail",
        "sheet_count": len(sheets),
        "formula_count": len(formulas),
        "assumption_cell_count": len(assumptions),
        "scenario_check_count": len(scenario_hits),
        "balance_check_count": len(balance_hits),
        "external_link_count": len(external_links),
        "formulas": formulas,
        "assumptions": assumptions,
        "scenario_checks": scenario_hits,
        "balance_checks": balance_hits,
        "external_links": external_links,
        "findings": [asdict(f) for f in findings],
    }


def markdown_report(report: dict) -> str:
    lines = [f"# Formula map: {Path(report['workbook']).name}", "",
             f"- Status: **{report['status'].upper()}**",
             f"- Sheets: {report['sheet_count']}", f"- Formulae: {report['formula_count']}",
             f"- Assumption cells: {report['assumption_cell_count']}",
             f"- Scenario checks: {report['scenario_check_count']}",
             f"- Balance/reconciliation checks: {report['balance_check_count']}",
             f"- External links: {report['external_link_count']}", "", "## Findings", ""]
    if report["findings"]:
        lines += [f"- `{f['severity']}` `{f['code']}` at `{f['location']}`: {f['message']}"
                  for f in report["findings"]]
    else:
        lines.append("No structural formula findings.")
    lines += ["", "## Formulae", "", "| Cell | Formula | Cached value |", "| --- | --- | --- |"]
    for item in report["formulas"]:
        formula = item["formula"].replace("|", "\\|")
        lines.append(f"| `{item['location']}` | `{formula}` | `{item['cached_value']}` |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbooks", nargs="+", type=Path)
    parser.add_argument("--require-scenarios", action="store_true")
    parser.add_argument("--require-balance-checks", action="store_true")
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    args = parser.parse_args(argv)
    reports = []
    for workbook in args.workbooks:
        try:
            reports.append(audit_workbook(workbook, args.require_scenarios,
                                          args.require_balance_checks))
        except (OSError, zipfile.BadZipFile, ET.ParseError) as exc:
            reports.append({"workbook": workbook.as_posix(), "status": "fail", "findings": [
                asdict(Finding("error", "unreadable-workbook", str(workbook), str(exc)))
            ]})
    payload = reports[0] if len(reports) == 1 else {"workbooks": reports}
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.markdown_out:
        if len(reports) != 1:
            parser.error("--markdown-out requires exactly one workbook")
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(markdown_report(reports[0]), encoding="utf-8")
    for report in reports:
        print(f"{report['status'].upper()}: {report['workbook']} "
              f"({len(report.get('findings', []))} findings)")
    return 1 if any(r["status"] != "pass" for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
