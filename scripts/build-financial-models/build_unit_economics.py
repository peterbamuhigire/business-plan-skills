"""Build saas-unit-economics-model.xlsx.

Implements the canonical SaaS unit-economics dashboard from
skills/10-financial-projections/references/saas-unit-economics-model-template.md.

Run: python scripts/build-financial-models/build_unit_economics.py
"""
import os
import sys
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _common import make_formats, write_readme, write_africa_notes, add_named  # noqa: E402

OUT = os.path.normpath(os.path.join(
    HERE, "..", "..", "skills", "saas-unit-economics-and-cohort-model",
    "templates", "saas-unit-economics-model.xlsx"
))


def build():
    wb = xlsxwriter.Workbook(OUT)
    fmts = make_formats(wb)

    # ----- README -----
    ws_readme = wb.add_worksheet("README")
    write_readme(
        ws_readme, fmts,
        "SaaS Unit Economics Model",
        "Compute and monitor the twelve canonical SaaS unit-economics metrics (LTV, CAC, "
        "Payback, LTV:CAC, GRR, NRR, Magic Number, Rule of 40, Burn Multiple, Quick Ratio, "
        "ARPA, GM) for a single steady-state period. Feeds the 3-yr / 5-yr projection model "
        "and the bankability dashboard.",
        sheets=[
            ("Inputs", "Yellow cells. Pricing, churn, expansion, CAC, S&M, GM, FX."),
            ("Calc", "All twelve metrics with three LTV formulations (simple, GM-adjusted, expansion-adjusted)."),
            ("Cohort", "24-month logo + revenue cohort matrix for six illustrative monthly cohorts."),
            ("Dashboard", "Headline KPIs, traffic-light flags, three charts (LTV:CAC, Payback trend, Cohort smile)."),
            ("Africa-Notes", "FX, M-Pesa, MoMo, USD-Enterprise tier, sales-cycle calibration."),
        ],
        owner="CFO / Finance Lead (founder pre-CFO)",
        cadence="Monthly refresh of Inputs from billing system (Stripe/Paystack/Chargebee). Quarterly review of benchmarks.",
        sources="Mersch (Hacking SaaS), Cotton (Run a SaaS Business), Skok (forentrepreneurs.com), "
                "OpenView SaaS Benchmarks, KeyBanc SaaS Survey, ChartMogul."
    )

    # ----- Inputs -----
    ws = wb.add_worksheet("Inputs")
    ws.set_column("A:A", 42)
    ws.set_column("B:B", 16)
    ws.set_column("C:C", 16)
    ws.set_column("D:D", 60)
    ws.set_row(0, 28)
    ws.merge_range("A1:D1", "Inputs — SaaS Unit Economics", fmts["title"])
    ws.write("A2", "Yellow cells are user-editable. White cells are formulas.", fmts["subtitle"])

    # Section: Pricing & ARPA
    ws.merge_range("A4:D4", "1. Pricing & ARPA (USD)", fmts["h2"])
    rows = [
        ("Tier 1 — Free / Starter MRR ($)", 0, "input_usd2", "Self-serve entry tier; can be $0."),
        ("Tier 2 — Pro MRR ($)", 79, "input_usd2", "Mid-tier monthly recurring price (USD)."),
        ("Tier 3 — Enterprise MRR ($)", 499, "input_usd2", "Enterprise tier (often invoiced USD)."),
        ("% customers Tier 1", 0.20, "input_pct", "Mix share — sum across tiers must be 100%."),
        ("% customers Tier 2", 0.60, "input_pct", ""),
        ("% customers Tier 3", 0.20, "input_pct", ""),
    ]
    r = 4
    for label, val, kind, note in rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        ws.write(r, 3, note, fmts["note"])
        r += 1
    # Blended ARPA formula
    ws.write(r, 0, "Blended monthly ARPA ($) [calc]", fmts["row_header"])
    ws.write_formula(r, 1, "=B5*B8+B6*B9+B7*B10", fmts["calc_usd2"])
    ws.write(r, 3, "Σ tier_price × tier_share.", fmts["note"])
    BLENDED_ARPA_ROW = r + 1
    r += 1
    ws.write(r, 0, "Annual ACV per customer ($)", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{BLENDED_ARPA_ROW}*12", fmts["calc_usd"])
    ws.write(r, 3, "ACV = blended ARPA × 12.", fmts["note"])
    ACV_ROW = r + 1
    r += 2

    # Section: Gross margin
    ws.merge_range(r, 0, r, 3, "2. Gross Margin", fmts["h2"])
    r += 1
    gm_rows = [
        ("Hosting / infra cost as % of revenue", 0.08, "input_pct"),
        ("Customer support cost as % of revenue", 0.06, "input_pct"),
        ("Payment-rail fee (M-Pesa/MoMo/card) % of revenue", 0.025, "input_pct"),
        ("Third-party / API / data fees % of revenue", 0.04, "input_pct"),
        ("Customer-success cost % of revenue", 0.05, "input_pct"),
    ]
    gm_start = r + 1
    for label, val, kind in gm_rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        r += 1
    ws.write(r, 0, "Total COGS % of revenue [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=SUM(B{gm_start}:B{r})", fmts["calc_pct"])
    COGS_PCT_ROW = r + 1
    r += 1
    ws.write(r, 0, "Gross margin % [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=1-B{COGS_PCT_ROW}", fmts["calc_bold_pct"])
    GM_ROW = r + 1
    r += 2

    # Section: Churn & expansion
    ws.merge_range(r, 0, r, 3, "3. Churn & Expansion (monthly)", fmts["h2"])
    r += 1
    ws.write(r, 0, "Monthly logo (gross) churn rate", fmts["row_header"])
    ws.write(r, 1, 0.025, fmts["input_pct"])
    LOGO_CHURN_ROW = r + 1
    r += 1
    ws.write(r, 0, "Monthly revenue (gross) churn rate", fmts["row_header"])
    ws.write(r, 1, 0.020, fmts["input_pct"])
    REV_CHURN_ROW = r + 1
    r += 1
    ws.write(r, 0, "Monthly expansion revenue rate (NRR uplift)", fmts["row_header"])
    ws.write(r, 1, 0.012, fmts["input_pct"])
    EXP_ROW = r + 1
    r += 1
    ws.write(r, 0, "Monthly contraction rate", fmts["row_header"])
    ws.write(r, 1, 0.004, fmts["input_pct"])
    CONTR_ROW = r + 1
    r += 1
    ws.write(r, 0, "Involuntary churn (monthly, payment failures)", fmts["row_header"])
    ws.write(r, 1, 0.004, fmts["input_pct"])
    INVOL_ROW = r + 1
    r += 2

    # Section: CAC
    ws.merge_range(r, 0, r, 3, "4. CAC (fully loaded, USD)", fmts["h2"])
    r += 1
    cac_rows = [
        ("Paid-channel CAC ($/new logo)", 1200, "input_usd"),
        ("Inbound CAC ($/new logo)", 400, "input_usd"),
        ("Outbound CAC ($/new logo)", 1800, "input_usd"),
        ("Partner / referral CAC ($/new logo)", 250, "input_usd"),
        ("% new logos via paid", 0.25, "input_pct"),
        ("% new logos via inbound", 0.40, "input_pct"),
        ("% new logos via outbound", 0.25, "input_pct"),
        ("% new logos via partner", 0.10, "input_pct"),
    ]
    cac_start = r + 1
    for label, val, kind in cac_rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        r += 1
    # Blended CAC
    ws.write(r, 0, "Blended CAC ($/new logo) [calc]", fmts["row_header"])
    ws.write_formula(r, 1,
        f"=B{cac_start}*B{cac_start+4}+B{cac_start+1}*B{cac_start+5}+B{cac_start+2}*B{cac_start+6}+B{cac_start+3}*B{cac_start+7}",
        fmts["calc_bold_usd"])
    BLENDED_CAC_ROW = r + 1
    r += 1
    ws.write(r, 0, "New logos acquired in period (count)", fmts["row_header"])
    ws.write(r, 1, 50, fmts["input_int"])
    NEW_LOGOS_ROW = r + 1
    r += 1
    ws.write(r, 0, "S&M spend in period ($)", fmts["row_header"])
    ws.write(r, 1, 60000, fmts["input_usd"])
    SM_SPEND_ROW = r + 1
    r += 1
    ws.write(r, 0, "Prior-quarter S&M spend ($)", fmts["row_header"])
    ws.write(r, 1, 55000, fmts["input_usd"])
    PRIOR_SM_ROW = r + 1
    r += 1
    ws.write(r, 0, "Net new ARR added in quarter ($)", fmts["row_header"])
    ws.write(r, 1, 90000, fmts["input_usd"])
    NEW_ARR_ROW = r + 1
    r += 1
    ws.write(r, 0, "Net cash burn in quarter ($)", fmts["row_header"])
    ws.write(r, 1, 75000, fmts["input_usd"])
    BURN_ROW = r + 1
    r += 1
    ws.write(r, 0, "YoY revenue growth %", fmts["row_header"])
    ws.write(r, 1, 1.20, fmts["input_pct"])
    GROWTH_ROW = r + 1
    r += 1
    ws.write(r, 0, "EBITDA margin %", fmts["row_header"])
    ws.write(r, 1, -0.20, fmts["input_pct"])
    EBITDA_ROW = r + 1
    r += 2

    # Section: Targets / benchmarks
    ws.merge_range(r, 0, r, 3, "5. Benchmarks / Targets", fmts["h2"])
    r += 1
    bench = [
        ("LTV:CAC target (healthy >=3, best >=5)", 3.0, "input"),
        ("CAC payback target (months)", 18, "input_int"),
        ("Rule of 40 target", 0.30, "input_pct"),
        ("NRR target", 1.10, "input_pct"),
        ("Burn Multiple target (lower is better, <2 healthy)", 2.0, "input"),
        ("Quick Ratio target (>2 healthy)", 2.0, "input"),
    ]
    for label, val, kind in bench:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        r += 1
    r += 1

    # Section: FX
    ws.merge_range(r, 0, r, 3, "6. FX & Local Currency", fmts["h2"])
    r += 1
    ws.write(r, 0, "Reporting currency code (e.g. UGX, KES, NGN, ZAR, EGP)", fmts["row_header"])
    ws.write(r, 1, "UGX", fmts["input_text"])
    r += 1
    ws.write(r, 0, "FX rate (local per 1 USD)", fmts["row_header"])
    ws.write(r, 1, 3800, fmts["input"])
    FX_ROW = r + 1
    r += 1
    ws.write(r, 0, "Expected annual FX depreciation %", fmts["row_header"])
    ws.write(r, 1, 0.05, fmts["input_pct"])
    r += 1

    # Named ranges
    add_named(wb, "Blended_ARPA", f"Inputs!$B${BLENDED_ARPA_ROW}")
    add_named(wb, "ACV", f"Inputs!$B${ACV_ROW}")
    add_named(wb, "GM_Pct", f"Inputs!$B${GM_ROW}")
    add_named(wb, "Logo_Churn", f"Inputs!$B${LOGO_CHURN_ROW}")
    add_named(wb, "Rev_Churn", f"Inputs!$B${REV_CHURN_ROW}")
    add_named(wb, "Expansion_Rate", f"Inputs!$B${EXP_ROW}")
    add_named(wb, "Contraction_Rate", f"Inputs!$B${CONTR_ROW}")
    add_named(wb, "Involuntary_Churn", f"Inputs!$B${INVOL_ROW}")
    add_named(wb, "Blended_CAC", f"Inputs!$B${BLENDED_CAC_ROW}")
    add_named(wb, "New_Logos", f"Inputs!$B${NEW_LOGOS_ROW}")
    add_named(wb, "SM_Spend", f"Inputs!$B${SM_SPEND_ROW}")
    add_named(wb, "Prior_SM", f"Inputs!$B${PRIOR_SM_ROW}")
    add_named(wb, "Net_New_ARR", f"Inputs!$B${NEW_ARR_ROW}")
    add_named(wb, "Net_Burn", f"Inputs!$B${BURN_ROW}")
    add_named(wb, "YoY_Growth", f"Inputs!$B${GROWTH_ROW}")
    add_named(wb, "EBITDA_Margin", f"Inputs!$B${EBITDA_ROW}")
    add_named(wb, "FX_Rate", f"Inputs!$B${FX_ROW}")

    # ----- Calc sheet -----
    wsc = wb.add_worksheet("Calc")
    wsc.set_column("A:A", 44)
    wsc.set_column("B:B", 18)
    wsc.set_column("C:C", 14)
    wsc.set_column("D:D", 18)
    wsc.set_column("E:E", 60)
    wsc.set_row(0, 28)
    wsc.merge_range("A1:E1", "Calc — Twelve Core Unit-Economics Metrics", fmts["title"])
    wsc.write("A2", "All formulas reference named ranges on Inputs sheet.", fmts["subtitle"])
    wsc.write("A3", "Metric", fmts["col_header"])
    wsc.write("B3", "Value", fmts["col_header"])
    wsc.write("C3", "Unit", fmts["col_header"])
    wsc.write("D3", "Target / Benchmark", fmts["col_header"])
    wsc.write("E3", "Formula", fmts["col_header"])

    metrics = [
        ("Blended ARPA",        "=Blended_ARPA",                                "$/mo", "n/a",        "Σ tier price × tier mix"),
        ("ACV (Annual Contract Value)", "=ACV",                                 "$",    "n/a",        "ARPA × 12"),
        ("Gross Margin %",      "=GM_Pct",                                      "%",    "70–85% healthy", "1 − Σ(COGS components)"),
        ("LTV (simple)",        "=Blended_ARPA/Logo_Churn",                     "$",    "n/a",        "ARPA / monthly logo churn"),
        ("LTV (gross-margin-adj)", "=Blended_ARPA*GM_Pct/Logo_Churn",           "$",    "n/a",        "ARPA × GM% / monthly churn — Skok/Mersch standard"),
        ("LTV (expansion-adj)",
            "=IF(Logo_Churn-Expansion_Rate>0, Blended_ARPA*GM_Pct/(Logo_Churn-Expansion_Rate), Blended_ARPA*GM_Pct*60)",
            "$", "Cap at 60 mo if NRR>100%", "ARPA × GM% / (churn − expansion). If negative → cap 5-yr horizon"),
        ("Blended CAC",         "=Blended_CAC",                                  "$",    "n/a",       "Σ channel CAC × channel mix"),
        ("CAC Payback (months)","=Blended_CAC/(Blended_ARPA*GM_Pct)",            "months", "<18 SMB (Africa)", "CAC / (ARPA × GM%)"),
        ("LTV:CAC",             "=(Blended_ARPA*GM_Pct/Logo_Churn)/Blended_CAC", "ratio", ">=3 healthy / >=5 best", "GM-adjusted LTV / CAC"),
        ("GRR (annual)",        "=MAX(0, 1-Rev_Churn*12)",                       "%",    ">75% SMB, >85% Mid, >90% Ent", "1 − annualised revenue churn"),
        ("NRR (annual)",        "=1+(Expansion_Rate-Rev_Churn-Contraction_Rate)*12", "%", ">100% target, >120% best", "1 + annualised (expansion − churn − contraction)"),
        ("Magic Number",        "=(Net_New_ARR*4)/Prior_SM",                     "ratio", ">1 invest more; <0.75 fix", "Net New ARR × 4 / prior-quarter S&M"),
        ("Rule of 40",          "=YoY_Growth+EBITDA_Margin",                     "%",    ">=30 (Africa Y1-3) / >=40 std", "YoY growth % + EBITDA margin %"),
        ("Burn Multiple",       "=IF(Net_New_ARR>0, Net_Burn/Net_New_ARR, 999)", "ratio", "<1 elite / <2 healthy", "Net cash burn / Net new ARR"),
        ("Quick Ratio",         "=(Net_New_ARR/3+Expansion_Rate*Blended_ARPA*New_Logos)/((Rev_Churn+Contraction_Rate)*Blended_ARPA*New_Logos+0.0001)",
                                "ratio", ">2 healthy / >4 best", "(New MRR + Expansion MRR) / (Contraction + Churn MRR)"),
        ("Annualised Involuntary Churn", "=Involuntary_Churn*12",                "%",    "<1% best / 3–6% Africa avg", "Monthly involuntary × 12"),
    ]
    r = 3
    for label, formula, unit, target, descr in metrics:
        wsc.write(r, 0, label, fmts["row_header"])
        is_pct = unit == "%"
        is_usd = unit == "$"
        if is_pct:
            wsc.write_formula(r, 1, formula, fmts["calc_pct"])
        elif is_usd:
            wsc.write_formula(r, 1, formula, fmts["calc_usd"])
        else:
            wsc.write_formula(r, 1, formula, fmts["calc"])
        wsc.write(r, 2, unit, fmts["calc"])
        wsc.write(r, 3, target, fmts["calc"])
        wsc.write(r, 4, descr, fmts["note"])
        r += 1

    # Conditional formatting on key metrics — LTV:CAC, CAC Payback, Rule of 40
    # Row indices: LTV:CAC = row 12 (0-idx 12), Payback = row 11, Rule of 40 = row 16
    # We'll target columns; specific rows by metric label index
    # Header is row 3 (0-indexed). First metric row is 3. metrics ordered above.
    # LTV:CAC = index 9 → row 12
    wsc.conditional_format(f"B{3+10}", {"type": "cell", "criteria": ">=", "value": 3, "format": fmts["good"]})
    wsc.conditional_format(f"B{3+10}", {"type": "cell", "criteria": "between", "minimum": 1.5, "maximum": 3, "format": fmts["warn"]})
    wsc.conditional_format(f"B{3+10}", {"type": "cell", "criteria": "<", "value": 1.5, "format": fmts["bad"]})
    # CAC Payback (index 8 → row 11). Lower is better.
    wsc.conditional_format(f"B{3+9}", {"type": "cell", "criteria": "<=", "value": 18, "format": fmts["good"]})
    wsc.conditional_format(f"B{3+9}", {"type": "cell", "criteria": "between", "minimum": 18, "maximum": 30, "format": fmts["warn"]})
    wsc.conditional_format(f"B{3+9}", {"type": "cell", "criteria": ">", "value": 30, "format": fmts["bad"]})
    # NRR (index 11 → row 14)
    wsc.conditional_format(f"B{3+11}", {"type": "cell", "criteria": ">=", "value": 1.10, "format": fmts["good"]})
    wsc.conditional_format(f"B{3+11}", {"type": "cell", "criteria": "between", "minimum": 1.00, "maximum": 1.10, "format": fmts["warn"]})
    wsc.conditional_format(f"B{3+11}", {"type": "cell", "criteria": "<", "value": 1.00, "format": fmts["bad"]})
    # Magic Number
    wsc.conditional_format(f"B{3+12}", {"type": "cell", "criteria": ">=", "value": 1.0, "format": fmts["good"]})
    wsc.conditional_format(f"B{3+12}", {"type": "cell", "criteria": "between", "minimum": 0.75, "maximum": 1.0, "format": fmts["warn"]})
    wsc.conditional_format(f"B{3+12}", {"type": "cell", "criteria": "<", "value": 0.75, "format": fmts["bad"]})
    # Rule of 40
    wsc.conditional_format(f"B{3+13}", {"type": "cell", "criteria": ">=", "value": 0.40, "format": fmts["good"]})
    wsc.conditional_format(f"B{3+13}", {"type": "cell", "criteria": "between", "minimum": 0.30, "maximum": 0.40, "format": fmts["warn"]})
    wsc.conditional_format(f"B{3+13}", {"type": "cell", "criteria": "<", "value": 0.30, "format": fmts["bad"]})
    # Burn Multiple (lower better)
    wsc.conditional_format(f"B{3+14}", {"type": "cell", "criteria": "<=", "value": 1.0, "format": fmts["good"]})
    wsc.conditional_format(f"B{3+14}", {"type": "cell", "criteria": "between", "minimum": 1.0, "maximum": 2.0, "format": fmts["warn"]})
    wsc.conditional_format(f"B{3+14}", {"type": "cell", "criteria": ">", "value": 2.0, "format": fmts["bad"]})

    # ----- Cohort sheet -----
    wsh = wb.add_worksheet("Cohort")
    wsh.set_column("A:A", 16)
    wsh.set_column("B:Z", 9)
    wsh.set_row(0, 26)
    wsh.merge_range("A1:Z1", "Cohort — 24-Month Logo & Revenue Retention", fmts["title"])
    wsh.write("A2", "Six illustrative monthly cohorts. Logo retention = (1-Logo_Churn)^t. Revenue retention = (1+Expansion-Rev_Churn-Contraction)^t.",
              fmts["subtitle"])

    # Logo cohorts header
    wsh.write(3, 0, "Logo Cohort (% retained)", fmts["h2"])
    wsh.write(4, 0, "Cohort \\ Months since acquisition", fmts["col_header"])
    for t in range(25):
        wsh.write(4, 1+t, f"M{t}", fmts["col_header"])
    cohort_names = ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06"]
    for i, cn in enumerate(cohort_names):
        wsh.write(5+i, 0, cn, fmts["row_header"])
        for t in range(25):
            # logo retention = (1-Logo_Churn)^t
            wsh.write_formula(5+i, 1+t, f"=(1-Logo_Churn)^{t}", fmts["calc_pct"])
    # Conditional format for cohort heatmap
    wsh.conditional_format(f"B6:Z{5+len(cohort_names)}", {
        "type": "3_color_scale",
        "min_color": "#F8696B", "mid_color": "#FFEB84", "max_color": "#63BE7B",
        "min_type": "num", "min_value": 0.3,
        "mid_type": "num", "mid_value": 0.6,
        "max_type": "num", "max_value": 1.0,
    })

    # Revenue cohort
    rev_start = 5 + len(cohort_names) + 2
    wsh.write(rev_start, 0, "Revenue Cohort (NRR per cohort)", fmts["h2"])
    wsh.write(rev_start+1, 0, "Cohort \\ Months", fmts["col_header"])
    for t in range(25):
        wsh.write(rev_start+1, 1+t, f"M{t}", fmts["col_header"])
    for i, cn in enumerate(cohort_names):
        wsh.write(rev_start+2+i, 0, cn, fmts["row_header"])
        for t in range(25):
            wsh.write_formula(rev_start+2+i, 1+t,
                f"=(1+Expansion_Rate-Rev_Churn-Contraction_Rate)^{t}",
                fmts["calc_pct"])
    wsh.conditional_format(f"B{rev_start+3}:Z{rev_start+2+len(cohort_names)}", {
        "type": "3_color_scale",
        "min_color": "#F8696B", "mid_color": "#FFEB84", "max_color": "#63BE7B",
        "min_type": "num", "min_value": 0.5,
        "mid_type": "num", "mid_value": 1.0,
        "max_type": "num", "max_value": 1.4,
    })

    # ----- Dashboard -----
    wsd = wb.add_worksheet("Dashboard")
    wsd.set_column("A:A", 30)
    wsd.set_column("B:B", 18)
    wsd.set_column("C:C", 22)
    wsd.set_column("D:D", 28)
    wsd.set_row(0, 30)
    wsd.merge_range("A1:D1", "Dashboard — SaaS Unit Economics", fmts["title"])

    kpis = [
        ("LTV:CAC",       "=(Blended_ARPA*GM_Pct/Logo_Churn)/Blended_CAC", "ratio"),
        ("CAC Payback",   "=Blended_CAC/(Blended_ARPA*GM_Pct)",            "months"),
        ("Gross Margin",  "=GM_Pct",                                       "pct"),
        ("NRR",           "=1+(Expansion_Rate-Rev_Churn-Contraction_Rate)*12", "pct"),
        ("GRR",           "=MAX(0, 1-Rev_Churn*12)",                       "pct"),
        ("Rule of 40",    "=YoY_Growth+EBITDA_Margin",                     "pct"),
        ("Magic Number",  "=(Net_New_ARR*4)/Prior_SM",                     "ratio"),
        ("Burn Multiple", "=IF(Net_New_ARR>0, Net_Burn/Net_New_ARR, 999)", "ratio"),
        ("ARPA ($/mo)",   "=Blended_ARPA",                                 "usd"),
        ("ACV ($)",       "=ACV",                                          "usd"),
    ]
    r = 3
    for label, formula, kind in kpis:
        wsd.write(r, 0, label, fmts["kpi_label"])
        if kind == "pct":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_pct"])
        elif kind == "usd":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_usd"])
        else:
            wsd.write_formula(r, 1, formula, fmts["kpi_value"])
        wsd.set_row(r, 24)
        r += 1

    # Chart: LTV vs CAC comparison
    chart1 = wb.add_chart({"type": "column"})
    # Add a small data block for chart
    wsd.write(20, 0, "Chart Data", fmts["h2"])
    wsd.write(21, 0, "LTV (GM-adj)", fmts["row_header"])
    wsd.write_formula(21, 1, "=Blended_ARPA*GM_Pct/Logo_Churn", fmts["calc_usd"])
    wsd.write(22, 0, "CAC", fmts["row_header"])
    wsd.write_formula(22, 1, "=Blended_CAC", fmts["calc_usd"])
    wsd.write(23, 0, "3× CAC (target line)", fmts["row_header"])
    wsd.write_formula(23, 1, "=3*Blended_CAC", fmts["calc_usd"])
    chart1.add_series({
        "name": "USD",
        "categories": "=Dashboard!$A$22:$A$24",
        "values":     "=Dashboard!$B$22:$B$24",
        "fill":       {"color": "#1F3864"},
    })
    chart1.set_title({"name": "LTV vs CAC vs 3× CAC Target"})
    chart1.set_y_axis({"name": "USD"})
    chart1.set_legend({"none": True})
    wsd.insert_chart("D3", chart1, {"x_scale": 1.1, "y_scale": 1.0})

    # Chart 2: cohort smile curve — use Cohort!Jan-25 revenue cohort row
    chart2 = wb.add_chart({"type": "line"})
    chart2.add_series({
        "name": "Revenue Retention (illustrative cohort)",
        "categories": f"=Cohort!$B${rev_start+1+1}:$Z${rev_start+1+1}",
        "values":     f"=Cohort!$B${rev_start+2+1}:$Z${rev_start+2+1}",
        "line": {"color": "#2E75B6", "width": 2.5},
        "marker": {"type": "circle", "size": 5, "fill": {"color": "#1F3864"}},
    })
    chart2.set_title({"name": "Revenue Cohort — Smile Curve Test"})
    chart2.set_y_axis({"name": "% of M0 Revenue", "num_format": "0%"})
    chart2.set_x_axis({"name": "Months since acquisition"})
    chart2.set_legend({"position": "bottom"})
    wsd.insert_chart("D20", chart2, {"x_scale": 1.2, "y_scale": 1.0})

    # Chart 3: Logo retention curve
    chart3 = wb.add_chart({"type": "line"})
    chart3.add_series({
        "name": "Logo Retention",
        "categories": "=Cohort!$B$5:$Z$5",
        "values":     "=Cohort!$B$6:$Z$6",
        "line": {"color": "#C65911", "width": 2.5},
    })
    chart3.set_title({"name": "Logo Cohort Retention Curve"})
    chart3.set_y_axis({"name": "% retained", "num_format": "0%"})
    chart3.set_x_axis({"name": "Months since acquisition"})
    chart3.set_legend({"position": "bottom"})
    wsd.insert_chart("D38", chart3, {"x_scale": 1.2, "y_scale": 1.0})

    # ----- Africa-Notes -----
    wsa = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsa, fmts)

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
