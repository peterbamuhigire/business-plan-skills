"""Verify the SaaS financial-model workbooks exist, are valid OOXML zips,
and contain the expected sheet count."""
import os, sys, zipfile, re, io

# Force UTF-8 stdout on Windows consoles
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

WORKBOOKS = [
    ("skills/saas/saas-unit-economics-and-cohort-model/templates/saas-unit-economics-model.xlsx", 5,
        ["README","Inputs","Calc","Cohort","Dashboard","Africa-Notes"]),
    ("skills/saas/saas-unit-economics-and-cohort-model/templates/saas-cohort-and-retention-model.xlsx", 7,
        ["README","Inputs","Logo-Cohort","Revenue-Cohort","NRR-GRR","Involuntary-Churn","Dashboard","Africa-Notes"]),
    ("skills/pipeline/10-financial-projections/templates/saas-financial-projection-3yr-5yr.xlsx", 9,
        ["README","Inputs","ARR-Waterfall","MRR-Detail","Headcount","PnL","Cash","Sensitivity","Scenarios","Bankability-Dashboard","Africa-Notes"]),
    ("skills/pipeline/14-ai-integration/templates/saas-ai-cost-of-tenant-calculator.xlsx", 7,
        ["README","Inputs","Cost-Per-Tenant","Margin-Analysis","Sensitivity","Stress-Test","Dashboard","Africa-Notes"]),
    ("skills/meta-strategy/meta-living-plan-governance/templates/saas-living-plan-kpi-dashboard.xlsx", 4,
        ["README","Monthly-Inputs","KPI-Dashboard","Variance-Tracker","Africa-Notes"]),
    ("skills/pipeline/10-financial-projections/saas-agent-unit-economics-and-cogs/templates/saas-agent-cost-per-task-calculator.xlsx", 7,
        ["README","Inputs","Cost-Per-Task","Margin-Analysis","Sensitivity","Stress-Test","Dashboard","Africa-Notes"]),
    ("skills/pipeline/10-financial-projections/saas-agent-unit-economics-and-cogs/templates/saas-agent-unit-economics-model.xlsx", 8,
        ["README","Inputs","Cohort","Unit-Economics","Wrapper-vs-Moat-Scoring","AI-vs-Agent-Comparison","Dashboard","Stress-Test","Africa-Notes"]),
]

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

failed = 0
for rel, _min_sheets, expected in WORKBOOKS:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        print(f"MISSING: {rel}"); failed += 1; continue
    size = os.path.getsize(path)
    if size < 5000:
        print(f"TOO SMALL ({size}B): {rel}"); failed += 1; continue
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
        # Extract sheet names from workbook.xml
        with zipfile.ZipFile(path) as z:
            with z.open("xl/workbook.xml") as f:
                wb_xml = f.read().decode("utf-8", errors="ignore")
        sheets = re.findall(r'<sheet[^>]+name="([^"]+)"', wb_xml)
        if len(sheets) < _min_sheets:
            print(f"TOO FEW SHEETS ({len(sheets)} < {_min_sheets}): {rel}")
            failed += 1
            continue
        missing = [s for s in expected if s not in sheets]
        status = "OK" if not missing else f"PARTIAL (missing: {missing})"
        print(f"{status}: {rel}  size={size:,}B  sheets={len(sheets)}  -> {sheets}")
        if missing:
            failed += 1
    except Exception as e:
        print(f"ZIP-ERROR: {rel}  {e}"); failed += 1

print()
if failed == 0:
    print(f"All {len(WORKBOOKS)} workbooks verified.")
else:
    print(f"{failed} workbook(s) failed verification.")
    sys.exit(1)
