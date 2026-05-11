"""Build saas-living-plan-kpi-dashboard.xlsx.

Monthly KPI dashboard that ingests actuals (Monthly-Inputs sheet), computes the
full SaaS KPI suite, traffic-lights variance vs plan, and flags >10% deviation
per skills/meta-living-plan-governance discipline.
"""
import os, sys
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _common import make_formats, write_readme, write_africa_notes, add_named  # noqa

OUT = os.path.normpath(os.path.join(
    HERE, "..", "..", "skills", "meta-living-plan-governance",
    "templates", "saas-living-plan-kpi-dashboard.xlsx"
))

N_MONTHS = 24  # 24-month rolling history + plan


def col(idx):
    s = ""; n = idx
    while True:
        s = chr(ord('A') + n % 26) + s
        n = n // 26 - 1
        if n < 0: break
    return s


def build():
    wb = xlsxwriter.Workbook(OUT)
    fmts = make_formats(wb)

    # README
    ws_r = wb.add_worksheet("README")
    write_readme(ws_r, fmts,
        "SaaS Living-Plan KPI Dashboard (Monthly)",
        "24-month rolling dashboard for SaaS. Paste monthly actuals into Monthly-Inputs; "
        "the workbook computes ARR, MRR, MoM/YoY growth, Rule of 40, NRR, GRR, Magic Number, "
        "Burn Multiple, CAC payback, LTV:CAC, Quick Ratio — auto-traffic-lighted. Variance-Tracker "
        "flags >10% deviation between plan and actual, which triggers the variance protocol per "
        "meta-living-plan-governance.",
        sheets=[
            ("Monthly-Inputs", "Paste-in actuals: MRR, ARR, new logos, churned, expansion, S&M, headcount, GM. Plan vs actual columns."),
            ("KPI-Dashboard", "Auto-calc: ARR, MRR, growth, Rule of 40, NRR, GRR, Magic Number, Burn Multiple, CAC payback, LTV:CAC, Quick Ratio. Traffic-lighted."),
            ("Variance-Tracker", "Plan vs actual; >10% variance → REPLAN flag."),
            ("Africa-Notes", "Reporting cadence under FX volatility; mobile-money payment-rail tracking."),
        ],
        owner="CFO (founder pre-CFO). Reviewed monthly with CEO; quarterly with board.",
        cadence="Monthly close + 5 working days. Variance review same day as close.",
        sources="meta-living-plan-governance skill; OpenView SaaS Benchmarks; saas-bankability-and-investor-readiness."
    )

    # MONTHLY-INPUTS
    ws = wb.add_worksheet("Monthly-Inputs")
    ws.set_column("A:A", 30); ws.set_column("B:Z", 11); ws.set_row(0, 28)
    ws.merge_range(0, 0, 0, N_MONTHS, "Monthly Inputs — Plan vs Actual", fmts["title"])
    ws.write(2, 0, "Metric / Month", fmts["col_header"])
    for m in range(N_MONTHS):
        ws.write(2, 1+m, f"M{m+1}", fmts["col_header"])

    # Section: Plan
    ws.merge_range(3, 0, 3, N_MONTHS, "PLAN (set once; update at re-forecast)", fmts["section"])
    plan_rows = [
        ("Plan MRR ($)",            [10000 + 1500*m for m in range(N_MONTHS)]),
        ("Plan New Logos",          [5 + int(m*0.6) for m in range(N_MONTHS)]),
        ("Plan Churned Logos",      [max(0, m//4) for m in range(N_MONTHS)]),
        ("Plan Expansion MRR ($)",  [100*(m+1) for m in range(N_MONTHS)]),
        ("Plan S&M Spend ($)",      [8000 + 300*m for m in range(N_MONTHS)]),
        ("Plan Headcount",          [5 + m//3 for m in range(N_MONTHS)]),
        ("Plan Gross Margin %",     [0.70 + min(0.10, m*0.005) for m in range(N_MONTHS)]),
        ("Plan Cash Burn ($)",      [15000 - 200*m for m in range(N_MONTHS)]),
    ]
    plan_start = 4
    for i, (label, vals) in enumerate(plan_rows):
        ws.write(plan_start + i, 0, label, fmts["row_header"])
        for m in range(N_MONTHS):
            kind = "input_pct" if "%" in label else ("input_usd" if "$" in label else "input_int")
            ws.write(plan_start + i, 1+m, vals[m], fmts[kind])

    # Section: Actual
    act_start = plan_start + len(plan_rows) + 1
    ws.merge_range(act_start - 1, 0, act_start - 1, N_MONTHS, "ACTUAL (paste in from billing/HR/finance systems)", fmts["section"])
    act_rows = [
        ("Actual MRR ($)",            "input_usd"),
        ("Actual New Logos",          "input_int"),
        ("Actual Churned Logos",      "input_int"),
        ("Actual Expansion MRR ($)",  "input_usd"),
        ("Actual S&M Spend ($)",      "input_usd"),
        ("Actual Headcount",          "input_int"),
        ("Actual Gross Margin %",     "input_pct"),
        ("Actual Cash Burn ($)",      "input_usd"),
    ]
    for i, (label, kind) in enumerate(act_rows):
        ws.write(act_start + i, 0, label, fmts["row_header"])
        for m in range(N_MONTHS):
            ws.write(act_start + i, 1+m, "", fmts[kind])

    # CAC + ARPA baseline assumptions (single row for simplicity)
    cac_start = act_start + len(act_rows) + 1
    ws.merge_range(cac_start - 1, 0, cac_start - 1, N_MONTHS, "Single-value assumptions", fmts["section"])
    ws.write(cac_start, 0, "Blended CAC ($/logo)", fmts["row_header"])
    ws.write(cac_start, 1, 850, fmts["input_usd"])
    CAC_LP = cac_start + 1
    ws.write(cac_start+1, 0, "ARPA ($/mo)", fmts["row_header"])
    ws.write(cac_start+1, 1, 79, fmts["input_usd2"])
    ARPA_LP = cac_start + 2
    ws.write(cac_start+2, 0, "Variance threshold % (trigger replan)", fmts["row_header"])
    ws.write(cac_start+2, 1, 0.10, fmts["input_pct"])
    VAR_LP = cac_start + 3
    ws.write(cac_start+3, 0, "Reporting currency", fmts["row_header"])
    ws.write(cac_start+3, 1, "UGX", fmts["input_text"])
    ws.write(cac_start+4, 0, "FX (local per USD)", fmts["row_header"])
    ws.write(cac_start+4, 1, 3800, fmts["input"])

    add_named(wb, "CAC_LP", f"'Monthly-Inputs'!$B${CAC_LP}")
    add_named(wb, "ARPA_LP", f"'Monthly-Inputs'!$B${ARPA_LP}")
    add_named(wb, "Var_Thresh", f"'Monthly-Inputs'!$B${VAR_LP}")

    # KPI-DASHBOARD
    wsd = wb.add_worksheet("KPI-Dashboard")
    wsd.set_column("A:A", 28); wsd.set_column("B:Z", 11); wsd.set_row(0, 28)
    wsd.merge_range(0, 0, 0, N_MONTHS, "KPI Dashboard — Monthly", fmts["title"])
    wsd.write(2, 0, "KPI / Month", fmts["col_header"])
    for m in range(N_MONTHS):
        wsd.write(2, 1+m, f"M{m+1}", fmts["col_header"])

    # rows: MRR (actual), ARR, MoM, YoY, NRR, GRR, Magic Number, Burn Multiple, CAC payback, LTV:CAC, Quick Ratio, Rule of 40
    # Reference Monthly-Inputs rows:
    # plan_start row 4 (0-indexed) = spreadsheet row 5. plan rows: 5..12
    # act rows start at act_start (0-indexed) → spreadsheet row act_start+1. act rows 8 long.
    P_MRR_R   = plan_start + 1                # spreadsheet row of plan MRR
    A_MRR_R   = act_start + 1                 # spreadsheet row of actual MRR
    A_NEW_R   = act_start + 2
    A_CHURN_R = act_start + 3
    A_EXP_R   = act_start + 4
    A_SM_R    = act_start + 5
    A_HC_R    = act_start + 6
    A_GM_R    = act_start + 7
    A_BURN_R  = act_start + 8

    def m_inp(row, m_idx):
        return f"'Monthly-Inputs'!{col(1+m_idx)}{row}"

    dash_rows = [
        ("MRR (actual, $)",      lambda m: f"={m_inp(A_MRR_R, m)}",                                       "calc_usd"),
        ("ARR (MRR×12, $)",      lambda m: f"={m_inp(A_MRR_R, m)}*12",                                    "calc_usd"),
        ("MoM growth %",         lambda m: ("" if m == 0 else
                                            f"=IFERROR({m_inp(A_MRR_R, m)}/{m_inp(A_MRR_R, m-1)}-1,0)"),  "calc_pct"),
        ("YoY growth %",         lambda m: ("" if m < 12 else
                                            f"=IFERROR({m_inp(A_MRR_R, m)}/{m_inp(A_MRR_R, m-12)}-1,0)"), "calc_pct"),
        ("Logo Churn rate (monthly)",
            lambda m: f"=IFERROR({m_inp(A_CHURN_R, m)}/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}/ARPA_LP),0)",     "calc_pct"),
        ("Expansion rate (monthly)",
            lambda m: f"=IFERROR({m_inp(A_EXP_R, m)}/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}),0)",              "calc_pct"),
        ("NRR (annual, rolling)",
            lambda m: f"=1+(IFERROR({m_inp(A_EXP_R, m)}/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}),0)"
                       f"-IFERROR({m_inp(A_CHURN_R, m)}/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}/ARPA_LP)*ARPA_LP/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}),0))*12",
            "calc_pct"),
        ("GRR (annual, rolling)",
            lambda m: f"=MAX(0,1-IFERROR({m_inp(A_CHURN_R, m)}*ARPA_LP/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}),0)*12)",
            "calc_pct"),
        ("Magic Number (3-mo trailing)",
            lambda m: ("" if m < 3 else
                       f"=IFERROR(({m_inp(A_MRR_R, m)}-{m_inp(A_MRR_R, m-3)})*4/"
                       f"({m_inp(A_SM_R, m-1)}+{m_inp(A_SM_R, m-2)}+{m_inp(A_SM_R, m-3)}),0)"),
            "calc"),
        ("CAC Payback (mo)",
            lambda m: f"=IFERROR(CAC_LP/(ARPA_LP*{m_inp(A_GM_R, m)}),0)",
            "calc"),
        ("LTV:CAC",
            lambda m: f"=IFERROR((ARPA_LP*{m_inp(A_GM_R, m)}/MAX(0.001,IFERROR({m_inp(A_CHURN_R, m)}/MAX(1,{m_inp(A_MRR_R, max(0,m-1))}/ARPA_LP),0)))/CAC_LP,0)",
            "calc"),
        ("Burn Multiple (3-mo)",
            lambda m: ("" if m < 3 else
                       f"=IFERROR(({m_inp(A_BURN_R, m)}+{m_inp(A_BURN_R, m-1)}+{m_inp(A_BURN_R, m-2)})/"
                       f"MAX(1,({m_inp(A_MRR_R, m)}-{m_inp(A_MRR_R, m-3)})*12/3),99)"),
            "calc"),
        ("Quick Ratio",
            lambda m: f"=IFERROR(({m_inp(A_NEW_R, m)}*ARPA_LP+{m_inp(A_EXP_R, m)})/"
                       f"MAX(1,{m_inp(A_CHURN_R, m)}*ARPA_LP),0)",
            "calc"),
        ("Rule of 40 (trailing 12-mo)",
            lambda m: ("" if m < 12 else
                       f"=IFERROR({m_inp(A_MRR_R, m)}/MAX(1,{m_inp(A_MRR_R, m-12)})-1,0)+(({m_inp(A_GM_R, m)})-(IFERROR({m_inp(A_SM_R, m)}+{m_inp(A_BURN_R, m)},0))/MAX(1,{m_inp(A_MRR_R, m)}))"),
            "calc_pct"),
    ]
    for i, (label, fn, kind) in enumerate(dash_rows):
        wsd.write(3+i, 0, label, fmts["row_header"])
        for m in range(N_MONTHS):
            val = fn(m)
            if val == "":
                wsd.write(3+i, 1+m, "", fmts[kind])
            else:
                wsd.write_formula(3+i, 1+m, val, fmts[kind])

    # Traffic lights on NRR row (index 6 → row 9), Magic Number (row 12), CAC Payback (row 13), LTV:CAC (row 14), Burn Multiple (row 15), Rule of 40 (row 17)
    nrr_row = 3 + 6  # 0-idx 9 → row 10 in spreadsheet
    rng = lambda r: f"B{r+1}:{col(N_MONTHS)}{r+1}"
    wsd.conditional_format(rng(nrr_row), {"type": "cell", "criteria": ">=", "value": 1.10, "format": fmts["good"]})
    wsd.conditional_format(rng(nrr_row), {"type": "cell", "criteria": "between", "minimum": 1.00, "maximum": 1.10, "format": fmts["warn"]})
    wsd.conditional_format(rng(nrr_row), {"type": "cell", "criteria": "<", "value": 1.00, "format": fmts["bad"]})

    mn_row = 3 + 8
    wsd.conditional_format(rng(mn_row), {"type": "cell", "criteria": ">=", "value": 1.0, "format": fmts["good"]})
    wsd.conditional_format(rng(mn_row), {"type": "cell", "criteria": "between", "minimum": 0.75, "maximum": 1.0, "format": fmts["warn"]})
    wsd.conditional_format(rng(mn_row), {"type": "cell", "criteria": "<", "value": 0.75, "format": fmts["bad"]})

    pb_row = 3 + 9
    wsd.conditional_format(rng(pb_row), {"type": "cell", "criteria": "<=", "value": 18, "format": fmts["good"]})
    wsd.conditional_format(rng(pb_row), {"type": "cell", "criteria": "between", "minimum": 18, "maximum": 30, "format": fmts["warn"]})
    wsd.conditional_format(rng(pb_row), {"type": "cell", "criteria": ">", "value": 30, "format": fmts["bad"]})

    ltv_row = 3 + 10
    wsd.conditional_format(rng(ltv_row), {"type": "cell", "criteria": ">=", "value": 3, "format": fmts["good"]})
    wsd.conditional_format(rng(ltv_row), {"type": "cell", "criteria": "between", "minimum": 1.5, "maximum": 3, "format": fmts["warn"]})
    wsd.conditional_format(rng(ltv_row), {"type": "cell", "criteria": "<", "value": 1.5, "format": fmts["bad"]})

    bm_row = 3 + 11
    wsd.conditional_format(rng(bm_row), {"type": "cell", "criteria": "<=", "value": 1.0, "format": fmts["good"]})
    wsd.conditional_format(rng(bm_row), {"type": "cell", "criteria": "between", "minimum": 1.0, "maximum": 2.0, "format": fmts["warn"]})
    wsd.conditional_format(rng(bm_row), {"type": "cell", "criteria": ">", "value": 2.0, "format": fmts["bad"]})

    r40_row = 3 + 13
    wsd.conditional_format(rng(r40_row), {"type": "cell", "criteria": ">=", "value": 0.40, "format": fmts["good"]})
    wsd.conditional_format(rng(r40_row), {"type": "cell", "criteria": "between", "minimum": 0.30, "maximum": 0.40, "format": fmts["warn"]})
    wsd.conditional_format(rng(r40_row), {"type": "cell", "criteria": "<", "value": 0.30, "format": fmts["bad"]})

    # Chart: MRR plan vs actual
    ch1 = wb.add_chart({"type": "line"})
    ch1.add_series({
        "name": "Plan MRR",
        "categories": f"='Monthly-Inputs'!$B$3:${col(N_MONTHS)}$3",
        "values":     f"='Monthly-Inputs'!$B${P_MRR_R}:${col(N_MONTHS)}${P_MRR_R}",
        "line": {"color": "#1F3864", "width": 2.0, "dash_type": "dash"},
    })
    ch1.add_series({
        "name": "Actual MRR",
        "categories": f"='Monthly-Inputs'!$B$3:${col(N_MONTHS)}$3",
        "values":     f"='Monthly-Inputs'!$B${A_MRR_R}:${col(N_MONTHS)}${A_MRR_R}",
        "line": {"color": "#C65911", "width": 2.5},
    })
    ch1.set_title({"name": "MRR — Plan vs Actual"})
    ch1.set_legend({"position": "bottom"})
    wsd.insert_chart("B22", ch1, {"x_scale": 2.0, "y_scale": 1.2})

    # VARIANCE-TRACKER
    wsv = wb.add_worksheet("Variance-Tracker")
    wsv.set_column("A:A", 30); wsv.set_column("B:Z", 11); wsv.set_row(0, 28)
    wsv.merge_range(0, 0, 0, N_MONTHS, "Variance Tracker — Plan vs Actual (>10% triggers REPLAN)", fmts["title"])
    wsv.write(2, 0, "Metric / Month", fmts["col_header"])
    for m in range(N_MONTHS):
        wsv.write(2, 1+m, f"M{m+1}", fmts["col_header"])

    # variance metrics: MRR, New Logos, S&M, Headcount, GM, Burn
    var_metrics = [
        ("MRR variance %",        P_MRR_R,    A_MRR_R),
        ("New Logos variance %",  plan_start+2, A_NEW_R),
        ("S&M Spend variance %",  plan_start+5, A_SM_R),
        ("Headcount variance %",  plan_start+6, A_HC_R),
        ("Gross Margin variance pp", plan_start+7, A_GM_R),
        ("Cash Burn variance %",  plan_start+8, A_BURN_R),
    ]
    for i, (label, plan_r, act_r) in enumerate(var_metrics):
        wsv.write(3+i, 0, label, fmts["row_header"])
        for m in range(N_MONTHS):
            cur_col = col(1+m)
            plan_ref = f"'Monthly-Inputs'!{cur_col}{plan_r}"
            act_ref  = f"'Monthly-Inputs'!{cur_col}{act_r}"
            if "pp" in label:
                wsv.write_formula(3+i, 1+m, f"=IFERROR({act_ref}-{plan_ref},0)", fmts["calc_pct"])
            else:
                wsv.write_formula(3+i, 1+m, f"=IFERROR(({act_ref}-{plan_ref})/MAX(1,{plan_ref}),0)", fmts["calc_pct"])
    # Replan flag row
    wsv.write(10, 0, "REPLAN FLAG (any metric >|threshold|)", fmts["row_header"])
    for m in range(N_MONTHS):
        cur_col = col(1+m)
        wsv.write_formula(10, 1+m,
            f"=IF(MAX(ABS({cur_col}4),ABS({cur_col}5),ABS({cur_col}6),ABS({cur_col}7),ABS({cur_col}8),ABS({cur_col}9))>Var_Thresh,\"REPLAN\",\"OK\")",
            fmts["calc"])
    wsv.conditional_format(f"B11:{col(N_MONTHS)}11", {
        "type": "text", "criteria": "containing", "value": "REPLAN", "format": fmts["bad"]
    })
    wsv.conditional_format(f"B11:{col(N_MONTHS)}11", {
        "type": "text", "criteria": "containing", "value": "OK", "format": fmts["good"]
    })
    # Heatmap on variance rows
    wsv.conditional_format(f"B4:{col(N_MONTHS)}9", {
        "type": "3_color_scale",
        "min_color": "#F8696B", "mid_color": "#FFFFFF", "max_color": "#63BE7B",
        "min_type": "num", "min_value": -0.25,
        "mid_type": "num", "mid_value": 0,
        "max_type": "num", "max_value": 0.25,
    })

    # AFRICA-NOTES
    wsa = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsa, fmts, extra_notes=[
        ("Monthly Close Cadence under FX Volatility",
         "Re-cut MRR in USD and reporting-currency simultaneously each month. A 5–8% FX move can produce "
         "a >10% variance against plan even when underlying logo/usage trends are on plan. Variance-Tracker "
         "exposes this — flag FX-driven variance separately from operating variance."),
        ("Payment-Rail Reconciliation",
         "Reconcile MRR collected via M-Pesa, MoMo, and card separately each month. Track payment-failure "
         "(involuntary churn) trend per rail — a rail-specific spike (e.g., MoMo float-shortage period) is "
         "operationally different from voluntary churn and requires a different fix."),
    ])

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
