"""Build saas-financial-projection-3yr-5yr.xlsx — the canonical 60-month SaaS model.

Implements:
- 60-month ARR Waterfall (opening + new + expansion - contraction - churned = closing)
- MRR detail by tier & channel, reconciled to ARR
- Headcount quarterly build with cost rollup
- Multi-Step P&L (Mersch format), monthly + quarterly
- Cash Flow w/ working-capital trough flagging
- Sensitivity (2-D: new logos × churn → end ARR + runway)
- Scenario toggle (Base/Bull/Bear via Scenario_Active multiplier)
- Bankability dashboard with traffic lights

Spec: skills/10-financial-projections/references/saas-financial-projection-template-3yr-5yr.md
"""
import os, sys
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _common import make_formats, write_readme, write_africa_notes, add_named  # noqa

OUT = os.path.normpath(os.path.join(
    HERE, "..", "..", "skills", "10-financial-projections",
    "templates", "saas-financial-projection-3yr-5yr.xlsx"
))

N_MONTHS = 60


def col(idx):
    """0-based index to A1 column letter."""
    s = ""; n = idx
    while True:
        s = chr(ord('A') + n % 26) + s
        n = n // 26 - 1
        if n < 0: break
    return s


def build():
    wb = xlsxwriter.Workbook(OUT)
    fmts = make_formats(wb)

    # ============= README =============
    ws_r = wb.add_worksheet("README")
    write_readme(ws_r, fmts,
        "SaaS Financial Projection — 3-Year / 5-Year (60 Months)",
        "Canonical SaaS 60-month financial model implementing Mersch's Multi-Step P&L, "
        "ARR Waterfall discipline, Cotton's headcount Rule of 3-and-10, and the "
        "Working-Capital Trough check. Single source of truth feeding the bankability "
        "dashboard, investor pitch, lender package, and quarterly board pack.",
        sheets=[
            ("Inputs", "Pricing, ACV mix, new logos by channel, growth, GM, headcount-by-role, salaries, capex, working capital, FX."),
            ("ARR-Waterfall", "60-month opening + new + expansion − contraction − churned = closing ARR."),
            ("MRR-Detail", "MRR build by tier & channel; reconciliation to ARR."),
            ("Headcount", "Quarterly headcount by role with cost rollup."),
            ("PnL", "Multi-Step P&L: Rev → COGS → GP → S&M → R&D → G&A → EBITDA → Adj → NI. Monthly + quarterly + annual."),
            ("Cash", "CFO + capex + financing; running balance; trough month flagged; runway."),
            ("Sensitivity", "2-D table: new-logo growth × churn → ending ARR + runway."),
            ("Scenarios", "Base / Bull / Bear active scenario toggle."),
            ("Bankability-Dashboard", "Rule of 40, LTV:CAC, Payback, NRR, Burn Multiple, Magic Number, Quick Ratio + traffic lights."),
            ("Africa-Notes", "FX, M-Pesa, MoMo, USD-Enterprise tier, DSO, prepayment uptake."),
        ],
        owner="CFO (founder pre-CFO). Investor-facing: review with CEO monthly.",
        cadence="Monthly: refresh actuals against plan. Quarterly: re-forecast next 4 quarters. Annually: roll forward year-by-year.",
        sources="Mersch (Hacking SaaS) ch.5-6; Cotton (Run a SaaS Business) Rule of 3-and-10; "
                "OpenView SaaS Benchmarks; KeyBanc SaaS Survey; Skok forentrepreneurs.com; "
                "this engine's saas-financial-projection-template-3yr-5yr.md.",
    )

    # ============= INPUTS =============
    ws = wb.add_worksheet("Inputs")
    ws.set_column("A:A", 42); ws.set_column("B:B", 14); ws.set_column("C:C", 14)
    ws.set_column("D:D", 14); ws.set_column("E:E", 14); ws.set_column("F:F", 14)
    ws.set_column("G:G", 56); ws.set_row(0, 28)
    ws.merge_range("A1:G1", "Inputs — SaaS 60-Month Financial Projection", fmts["title"])
    ws.write("A2", "Yellow = editable input. White = formula. Named ranges in use throughout.", fmts["subtitle"])

    r = 3
    # Scenario toggle
    ws.merge_range(r, 0, r, 6, "0. Scenario Toggle", fmts["h2"]); r += 1
    ws.write(r, 0, "Active scenario (Base / Bull / Bear)", fmts["row_header"])
    ws.write(r, 1, "Base", fmts["input_text"])
    SCEN_ROW = r + 1
    ws.write(r, 6, "Drives Scenario_Active multipliers on logos, churn, ARPA, FX.", fmts["note"])
    r += 1
    ws.write(r, 0, "Logo growth multiplier (active scenario)", fmts["row_header"])
    ws.write_formula(r, 1, f'=IF(B{SCEN_ROW}="Bull",1.25,IF(B{SCEN_ROW}="Bear",0.75,1))', fmts["calc"])
    LOGO_MULT_ROW = r + 1
    r += 1
    ws.write(r, 0, "Churn multiplier (active scenario)", fmts["row_header"])
    ws.write_formula(r, 1, f'=IF(B{SCEN_ROW}="Bull",0.75,IF(B{SCEN_ROW}="Bear",1.5,1))', fmts["calc"])
    CHURN_MULT_ROW = r + 1
    r += 1
    ws.write(r, 0, "ARPA multiplier (active scenario)", fmts["row_header"])
    ws.write_formula(r, 1, f'=IF(B{SCEN_ROW}="Bull",1.20,IF(B{SCEN_ROW}="Bear",0.85,1))', fmts["calc"])
    ARPA_MULT_ROW = r + 1
    r += 2

    # Section 1: Pricing & ARPA
    ws.merge_range(r, 0, r, 6, "1. Pricing & Tier Mix", fmts["h2"]); r += 1
    ws.write(r, 0, "Tier 1 (Free/Starter) MRR $", fmts["row_header"]); ws.write(r, 1, 0, fmts["input_usd2"])
    T1_PRICE_ROW = r+1; r += 1
    ws.write(r, 0, "Tier 2 (Pro) MRR $", fmts["row_header"]); ws.write(r, 1, 79, fmts["input_usd2"])
    T2_PRICE_ROW = r+1; r += 1
    ws.write(r, 0, "Tier 3 (Enterprise USD) MRR $", fmts["row_header"]); ws.write(r, 1, 499, fmts["input_usd2"])
    T3_PRICE_ROW = r+1; r += 1
    ws.write(r, 0, "Mix % Tier 1", fmts["row_header"]); ws.write(r, 1, 0.20, fmts["input_pct"]); T1_MIX = r+1; r += 1
    ws.write(r, 0, "Mix % Tier 2", fmts["row_header"]); ws.write(r, 1, 0.60, fmts["input_pct"]); T2_MIX = r+1; r += 1
    ws.write(r, 0, "Mix % Tier 3", fmts["row_header"]); ws.write(r, 1, 0.20, fmts["input_pct"]); T3_MIX = r+1; r += 1
    ws.write(r, 0, "Annual price escalator", fmts["row_header"]); ws.write(r, 1, 0.05, fmts["input_pct"]); ESC_ROW = r+1; r += 1
    ws.write(r, 0, "Blended ARPA ($/mo) [calc, scenario-adj]", fmts["row_header"])
    ws.write_formula(r, 1,
        f"=(B{T1_PRICE_ROW}*B{T1_MIX}+B{T2_PRICE_ROW}*B{T2_MIX}+B{T3_PRICE_ROW}*B{T3_MIX})*B{ARPA_MULT_ROW}",
        fmts["calc_bold_usd"])
    BLENDED_ARPA = r + 1; r += 2

    # Section 2: New logos by channel — monthly Y1
    ws.merge_range(r, 0, r, 6, "2. New Logos / Month (Year 1 baseline; Y2+ from growth rates)", fmts["h2"]); r += 1
    ws.write(r, 0, "M1 new logos (paid)", fmts["row_header"]); ws.write(r, 1, 3, fmts["input_int"]); NL_PAID_ROW = r+1; r += 1
    ws.write(r, 0, "M1 new logos (inbound)", fmts["row_header"]); ws.write(r, 1, 5, fmts["input_int"]); NL_IN_ROW = r+1; r += 1
    ws.write(r, 0, "M1 new logos (outbound)", fmts["row_header"]); ws.write(r, 1, 2, fmts["input_int"]); NL_OUT_ROW = r+1; r += 1
    ws.write(r, 0, "M1 new logos (partner)", fmts["row_header"]); ws.write(r, 1, 1, fmts["input_int"]); NL_PART_ROW = r+1; r += 1
    ws.write(r, 0, "Monthly new-logo growth rate Year 1", fmts["row_header"]); ws.write(r, 1, 0.10, fmts["input_pct"]); G_Y1_ROW = r+1; r += 1
    ws.write(r, 0, "Monthly new-logo growth rate Year 2", fmts["row_header"]); ws.write(r, 1, 0.07, fmts["input_pct"]); G_Y2_ROW = r+1; r += 1
    ws.write(r, 0, "Monthly new-logo growth rate Year 3", fmts["row_header"]); ws.write(r, 1, 0.05, fmts["input_pct"]); G_Y3_ROW = r+1; r += 1
    ws.write(r, 0, "Monthly new-logo growth rate Year 4", fmts["row_header"]); ws.write(r, 1, 0.04, fmts["input_pct"]); G_Y4_ROW = r+1; r += 1
    ws.write(r, 0, "Monthly new-logo growth rate Year 5", fmts["row_header"]); ws.write(r, 1, 0.03, fmts["input_pct"]); G_Y5_ROW = r+1; r += 1
    ws.write(r, 0, "M1 new logos total [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{NL_PAID_ROW}+B{NL_IN_ROW}+B{NL_OUT_ROW}+B{NL_PART_ROW}", fmts["calc_bold"])
    M1_LOGOS_ROW = r + 1; r += 2

    # Section 3: Churn & expansion
    ws.merge_range(r, 0, r, 6, "3. Churn & Expansion (monthly)", fmts["h2"]); r += 1
    ws.write(r, 0, "Logo churn (gross) monthly", fmts["row_header"]); ws.write(r, 1, 0.025, fmts["input_pct"]); LC_ROW = r+1; r += 1
    ws.write(r, 0, "Revenue churn (gross) monthly", fmts["row_header"]); ws.write(r, 1, 0.020, fmts["input_pct"]); RC_ROW = r+1; r += 1
    ws.write(r, 0, "Expansion revenue monthly rate", fmts["row_header"]); ws.write(r, 1, 0.012, fmts["input_pct"]); EX_ROW = r+1; r += 1
    ws.write(r, 0, "Contraction monthly rate", fmts["row_header"]); ws.write(r, 1, 0.004, fmts["input_pct"]); CON_ROW = r+1; r += 1
    ws.write(r, 0, "Scenario-adjusted logo churn [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{LC_ROW}*B{CHURN_MULT_ROW}", fmts["calc_pct"])
    LC_ADJ = r+1; r += 1
    ws.write(r, 0, "Scenario-adjusted revenue churn [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{RC_ROW}*B{CHURN_MULT_ROW}", fmts["calc_pct"])
    RC_ADJ = r+1; r += 2

    # Section 4: COGS / GM
    ws.merge_range(r, 0, r, 6, "4. Cost of Revenue % of revenue", fmts["h2"]); r += 1
    cogs_items = [
        ("Hosting / infra %", 0.08), ("Customer support %", 0.06),
        ("Payment-rail fee %", 0.025), ("3rd-party / API / data %", 0.04),
        ("Customer-success %", 0.05),
    ]
    cogs_start = r + 1
    for label, val in cogs_items:
        ws.write(r, 0, label, fmts["row_header"]); ws.write(r, 1, val, fmts["input_pct"]); r += 1
    ws.write(r, 0, "Total COGS % [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=SUM(B{cogs_start}:B{r})", fmts["calc_pct"])
    COGS_PCT_ROW = r+1; r += 1
    ws.write(r, 0, "Gross margin % [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=1-B{COGS_PCT_ROW}", fmts["calc_bold_pct"])
    GM_ROW = r+1; r += 2

    # Section 5: Opex
    ws.merge_range(r, 0, r, 6, "5. Opex Drivers", fmts["h2"]); r += 1
    opex_items = [
        ("S&M as % of revenue (Y1)", 0.60),
        ("S&M as % of revenue (Y2)", 0.50),
        ("S&M as % of revenue (Y3+)", 0.40),
        ("R&D as % of revenue (Y1)", 0.40),
        ("R&D as % of revenue (Y2)", 0.30),
        ("R&D as % of revenue (Y3+)", 0.25),
        ("G&A fixed monthly $ Year 1", 8000),
        ("G&A fixed monthly $ Year 2", 12000),
        ("G&A fixed monthly $ Year 3+", 18000),
        ("Annual opex inflation %", 0.06),
    ]
    OP = {}
    for label, val in opex_items:
        ws.write(r, 0, label, fmts["row_header"])
        if "$" in label:
            ws.write(r, 1, val, fmts["input_usd"])
        else:
            ws.write(r, 1, val, fmts["input_pct"])
        OP[label] = r+1
        r += 1
    r += 1

    # Section 6: Headcount build by role × quarter
    ws.merge_range(r, 0, r, 6, "6. Headcount by Role (per quarter, Y1Q1..Y5Q4)", fmts["h2"]); r += 1
    ws.write(r, 0, "Role", fmts["col_header"])
    ws.write(r, 1, "Loaded $/year", fmts["col_header"])
    ws.write(r, 2, "Bucket", fmts["col_header"])
    ws.write(r, 3, "Y1 HC (avg)", fmts["col_header"])
    ws.write(r, 4, "Y2 HC", fmts["col_header"])
    ws.write(r, 5, "Y3 HC", fmts["col_header"])
    ws.write(r, 6, "Y4–Y5 HC", fmts["col_header"])
    r += 1
    HC_START = r + 1   # 1-indexed start row for headcount table on Inputs
    roles = [
        ("Engineering Lead",       95000, "R&D",  1, 2, 3, 4),
        ("Software Engineer",      55000, "R&D",  2, 4, 7, 10),
        ("Product Manager",        65000, "R&D",  1, 1, 2, 3),
        ("Designer",               45000, "R&D",  1, 1, 2, 2),
        ("Account Executive",      55000, "S&M",  1, 3, 6, 10),
        ("SDR / BDR",              28000, "S&M",  1, 2, 5, 8),
        ("Marketing Manager",      50000, "S&M",  1, 1, 2, 3),
        ("Customer Success Mgr",   45000, "S&M",  1, 2, 4, 6),
        ("Finance / Ops",          50000, "G&A",  1, 1, 2, 3),
        ("CEO / Founder",          80000, "G&A",  1, 1, 1, 1),
    ]
    for role, salary, bucket, y1, y2, y3, y45 in roles:
        ws.write(r, 0, role, fmts["row_header"])
        ws.write(r, 1, salary, fmts["input_usd"])
        ws.write(r, 2, bucket, fmts["input_text"])
        ws.write(r, 3, y1, fmts["input_int"])
        ws.write(r, 4, y2, fmts["input_int"])
        ws.write(r, 5, y3, fmts["input_int"])
        ws.write(r, 6, y45, fmts["input_int"])
        r += 1
    HC_END = r   # 1-indexed last row of HC table
    r += 1
    # HC totals + cost rollup
    ws.write(r, 0, "Total Y1 HC", fmts["row_header"])
    ws.write_formula(r, 3, f"=SUM(D{HC_START}:D{HC_END})", fmts["calc_bold"])
    ws.write_formula(r, 4, f"=SUM(E{HC_START}:E{HC_END})", fmts["calc_bold"])
    ws.write_formula(r, 5, f"=SUM(F{HC_START}:F{HC_END})", fmts["calc_bold"])
    ws.write_formula(r, 6, f"=SUM(G{HC_START}:G{HC_END})", fmts["calc_bold"])
    HC_TOTAL_ROW = r + 1
    r += 1
    ws.write(r, 0, "Total Y1 loaded cost $", fmts["row_header"])
    ws.write_formula(r, 3, f"=SUMPRODUCT(B{HC_START}:B{HC_END},D{HC_START}:D{HC_END})", fmts["calc_bold_usd"])
    ws.write_formula(r, 4, f"=SUMPRODUCT(B{HC_START}:B{HC_END},E{HC_START}:E{HC_END})", fmts["calc_bold_usd"])
    ws.write_formula(r, 5, f"=SUMPRODUCT(B{HC_START}:B{HC_END},F{HC_START}:F{HC_END})", fmts["calc_bold_usd"])
    ws.write_formula(r, 6, f"=SUMPRODUCT(B{HC_START}:B{HC_END},G{HC_START}:G{HC_END})", fmts["calc_bold_usd"])
    HC_COST_ROW = r + 1
    r += 2

    # Section 7: Working capital + capex + financing
    ws.merge_range(r, 0, r, 6, "7. Working Capital, Capex, Financing", fmts["h2"]); r += 1
    wc_items = [
        ("DSO — days sales outstanding", 60, "input_int"),
        ("DPO — days payables outstanding", 30, "input_int"),
        ("Annual prepayment uptake (% of new contracts)", 0.30, "input_pct"),
        ("Annual prepayment discount %", 0.12, "input_pct"),
        ("Capex Year 1 ($)", 25000, "input_usd"),
        ("Capex Year 2 ($)", 20000, "input_usd"),
        ("Capex Year 3 ($)", 25000, "input_usd"),
        ("Capex Year 4 ($)", 30000, "input_usd"),
        ("Capex Year 5 ($)", 35000, "input_usd"),
        ("Starting cash ($)", 750000, "input_usd"),
        ("Equity raised (Year 1) $", 1500000, "input_usd"),
        ("Equity raised (Year 2) $", 0, "input_usd"),
        ("Equity raised (Year 3) $", 4000000, "input_usd"),
        ("Debt drawdown (Year 2) $", 0, "input_usd"),
        ("Interest rate on debt", 0.12, "input_pct"),
        ("Effective tax rate", 0.30, "input_pct"),
    ]
    WC = {}
    for label, val, kind in wc_items:
        ws.write(r, 0, label, fmts["row_header"]); ws.write(r, 1, val, fmts[kind])
        WC[label] = r+1; r += 1
    r += 1

    # Section 8: CAC for bankability
    ws.merge_range(r, 0, r, 6, "8. CAC Inputs (for bankability dashboard)", fmts["h2"]); r += 1
    ws.write(r, 0, "Blended CAC ($/new logo)", fmts["row_header"]); ws.write(r, 1, 850, fmts["input_usd"])
    CAC_ROW = r+1; r += 1

    # Section 9: FX
    ws.merge_range(r, 0, r, 6, "9. FX", fmts["h2"]); r += 1
    ws.write(r, 0, "Reporting currency", fmts["row_header"]); ws.write(r, 1, "UGX", fmts["input_text"]); r += 1
    ws.write(r, 0, "FX (local per USD)", fmts["row_header"]); ws.write(r, 1, 3800, fmts["input"]); FX_ROW_P = r+1; r += 1
    ws.write(r, 0, "Annual FX depreciation %", fmts["row_header"]); ws.write(r, 1, 0.05, fmts["input_pct"]); FX_DEP = r+1; r += 1

    # Define named ranges
    add_named(wb, "Scen_Active", f"Inputs!$B${SCEN_ROW}")
    add_named(wb, "Logo_Mult",   f"Inputs!$B${LOGO_MULT_ROW}")
    add_named(wb, "Churn_Mult",  f"Inputs!$B${CHURN_MULT_ROW}")
    add_named(wb, "ARPA_Mult",   f"Inputs!$B${ARPA_MULT_ROW}")
    add_named(wb, "ARPA_P",      f"Inputs!$B${BLENDED_ARPA}")
    add_named(wb, "M1_Logos",    f"Inputs!$B${M1_LOGOS_ROW}")
    add_named(wb, "G_Y1",        f"Inputs!$B${G_Y1_ROW}")
    add_named(wb, "G_Y2",        f"Inputs!$B${G_Y2_ROW}")
    add_named(wb, "G_Y3",        f"Inputs!$B${G_Y3_ROW}")
    add_named(wb, "G_Y4",        f"Inputs!$B${G_Y4_ROW}")
    add_named(wb, "G_Y5",        f"Inputs!$B${G_Y5_ROW}")
    add_named(wb, "Logo_Churn_P",f"Inputs!$B${LC_ADJ}")
    add_named(wb, "Rev_Churn_P", f"Inputs!$B${RC_ADJ}")
    add_named(wb, "Expansion_P", f"Inputs!$B${EX_ROW}")
    add_named(wb, "Contraction_P", f"Inputs!$B${CON_ROW}")
    add_named(wb, "GM_P",        f"Inputs!$B${GM_ROW}")
    add_named(wb, "COGS_PCT",    f"Inputs!$B${COGS_PCT_ROW}")
    add_named(wb, "SM_Y1",       f"Inputs!$B${OP['S&M as % of revenue (Y1)']}")
    add_named(wb, "SM_Y2",       f"Inputs!$B${OP['S&M as % of revenue (Y2)']}")
    add_named(wb, "SM_Y3p",      f"Inputs!$B${OP['S&M as % of revenue (Y3+)']}")
    add_named(wb, "RD_Y1",       f"Inputs!$B${OP['R&D as % of revenue (Y1)']}")
    add_named(wb, "RD_Y2",       f"Inputs!$B${OP['R&D as % of revenue (Y2)']}")
    add_named(wb, "RD_Y3p",      f"Inputs!$B${OP['R&D as % of revenue (Y3+)']}")
    add_named(wb, "GA_Y1",       f"Inputs!$B${OP['G&A fixed monthly $ Year 1']}")
    add_named(wb, "GA_Y2",       f"Inputs!$B${OP['G&A fixed monthly $ Year 2']}")
    add_named(wb, "GA_Y3p",      f"Inputs!$B${OP['G&A fixed monthly $ Year 3+']}")
    add_named(wb, "Start_Cash",  f"Inputs!$B${WC['Starting cash ($)']}")
    add_named(wb, "Eq_Y1",       f"Inputs!$B${WC['Equity raised (Year 1) $']}")
    add_named(wb, "Eq_Y2",       f"Inputs!$B${WC['Equity raised (Year 2) $']}")
    add_named(wb, "Eq_Y3",       f"Inputs!$B${WC['Equity raised (Year 3) $']}")
    add_named(wb, "Capex_Y1",    f"Inputs!$B${WC['Capex Year 1 ($)']}")
    add_named(wb, "Capex_Y2",    f"Inputs!$B${WC['Capex Year 2 ($)']}")
    add_named(wb, "Capex_Y3",    f"Inputs!$B${WC['Capex Year 3 ($)']}")
    add_named(wb, "Capex_Y4",    f"Inputs!$B${WC['Capex Year 4 ($)']}")
    add_named(wb, "Capex_Y5",    f"Inputs!$B${WC['Capex Year 5 ($)']}")
    add_named(wb, "Tax_Rate",    f"Inputs!$B${WC['Effective tax rate']}")
    add_named(wb, "CAC_P",       f"Inputs!$B${CAC_ROW}")
    add_named(wb, "FX_P",        f"Inputs!$B${FX_ROW_P}")
    add_named(wb, "HC_Total_Y1", f"Inputs!$D${HC_TOTAL_ROW}")
    add_named(wb, "HC_Cost_Y1",  f"Inputs!$D${HC_COST_ROW}")

    # ============= ARR WATERFALL =============
    wsw = wb.add_worksheet("ARR-Waterfall")
    wsw.set_column("A:A", 26); wsw.set_column("B:BH", 11); wsw.set_row(0, 28)
    wsw.merge_range(0, 0, 0, N_MONTHS, "ARR Waterfall — 60 Months", fmts["title"])
    wsw.write(2, 0, "Month", fmts["col_header"])
    for m in range(N_MONTHS):
        wsw.write(2, 1+m, f"M{m+1}", fmts["col_header"])
    # Row layout
    rows_w = {
        "Year": 3, "New logos (count)": 4, "Cum customers (end)": 5,
        "Opening ARR": 6, "New ARR": 7, "Expansion ARR": 8,
        "Contraction ARR": 9, "Churn ARR": 10, "Ending ARR": 11,
        "Net New ARR": 12, "MRR (end)": 13,
    }
    for name, rr in rows_w.items():
        wsw.write(rr, 0, name, fmts["row_header"])
    # Fill months
    for m in range(N_MONTHS):
        c = 1 + m
        # Year number
        y = (m // 12) + 1
        wsw.write(rows_w["Year"], c, y, fmts["calc_int"])
        # New logos: M1 = M1_Logos; subsequent = prev * (1 + growth_for_year) * Logo_Mult
        if m == 0:
            wsw.write_formula(rows_w["New logos (count)"], c, "=M1_Logos*Logo_Mult", fmts["calc_int"])
        else:
            prev_col = col(c-1)
            growth_pick = (
                f'IF(B{rows_w["Year"]+1}=1, G_Y1, '
                f'IF({prev_col}{rows_w["Year"]+1}=2, G_Y2, '
                f'IF({prev_col}{rows_w["Year"]+1}=3, G_Y3, '
                f'IF({prev_col}{rows_w["Year"]+1}=4, G_Y4, G_Y5))))'
            )
            # Use current-month year for growth (simpler)
            cur_col = col(c)
            growth_pick = (
                f'IF({cur_col}{rows_w["Year"]+1}=1, G_Y1, '
                f'IF({cur_col}{rows_w["Year"]+1}=2, G_Y2, '
                f'IF({cur_col}{rows_w["Year"]+1}=3, G_Y3, '
                f'IF({cur_col}{rows_w["Year"]+1}=4, G_Y4, G_Y5))))'
            )
            wsw.write_formula(rows_w["New logos (count)"], c,
                f"=ROUND({prev_col}{rows_w['New logos (count)']+1}*(1+{growth_pick}),0)",
                fmts["calc_int"])
        # Opening ARR = previous Ending ARR (M1=0)
        if m == 0:
            wsw.write(rows_w["Opening ARR"], c, 0, fmts["calc_usd"])
        else:
            prev_col = col(c-1)
            wsw.write_formula(rows_w["Opening ARR"], c, f"={prev_col}{rows_w['Ending ARR']+1}", fmts["calc_usd"])
        # New ARR = new_logos × ARPA × 12
        cur_col = col(c)
        wsw.write_formula(rows_w["New ARR"], c,
            f"={cur_col}{rows_w['New logos (count)']+1}*ARPA_P*12", fmts["calc_usd"])
        # Expansion = Opening × Expansion_P
        wsw.write_formula(rows_w["Expansion ARR"], c,
            f"={cur_col}{rows_w['Opening ARR']+1}*Expansion_P", fmts["calc_usd"])
        # Contraction = Opening × Contraction_P
        wsw.write_formula(rows_w["Contraction ARR"], c,
            f"=-{cur_col}{rows_w['Opening ARR']+1}*Contraction_P", fmts["calc_usd"])
        # Churn = Opening × Rev_Churn_P
        wsw.write_formula(rows_w["Churn ARR"], c,
            f"=-{cur_col}{rows_w['Opening ARR']+1}*Rev_Churn_P", fmts["calc_usd"])
        # Ending = sum
        wsw.write_formula(rows_w["Ending ARR"], c,
            f"={cur_col}{rows_w['Opening ARR']+1}+{cur_col}{rows_w['New ARR']+1}+"
            f"{cur_col}{rows_w['Expansion ARR']+1}+{cur_col}{rows_w['Contraction ARR']+1}+"
            f"{cur_col}{rows_w['Churn ARR']+1}",
            fmts["calc_bold_usd"])
        # Net new
        wsw.write_formula(rows_w["Net New ARR"], c,
            f"={cur_col}{rows_w['New ARR']+1}+{cur_col}{rows_w['Expansion ARR']+1}+"
            f"{cur_col}{rows_w['Contraction ARR']+1}+{cur_col}{rows_w['Churn ARR']+1}",
            fmts["calc_usd"])
        # MRR end = Ending ARR / 12
        wsw.write_formula(rows_w["MRR (end)"], c,
            f"={cur_col}{rows_w['Ending ARR']+1}/12", fmts["calc_usd"])
        # Cum customers: M1 = M1 logos; subsequent = prev × (1 - logo churn) + new logos
        if m == 0:
            wsw.write_formula(rows_w["Cum customers (end)"], c,
                f"={cur_col}{rows_w['New logos (count)']+1}", fmts["calc_int"])
        else:
            prev_col = col(c-1)
            wsw.write_formula(rows_w["Cum customers (end)"], c,
                f"={prev_col}{rows_w['Cum customers (end)']+1}*(1-Logo_Churn_P)+{cur_col}{rows_w['New logos (count)']+1}",
                fmts["calc_int"])

    # Annual ARR summary in a side block
    wsw.merge_range(15, 0, 15, N_MONTHS, "Annual Snapshot — Ending ARR & YoY Growth", fmts["h2"])
    wsw.write(16, 0, "End of Year", fmts["col_header"])
    for y in range(1, 6):
        wsw.write(16, y, f"Y{y}", fmts["col_header"])
    wsw.write(17, 0, "Ending ARR", fmts["row_header"])
    wsw.write(18, 0, "YoY Growth %", fmts["row_header"])
    for y in range(1, 6):
        last_m_col = col(y * 12)  # column index: y*12 -> M(y*12)
        wsw.write_formula(17, y, f"={last_m_col}{rows_w['Ending ARR']+1}", fmts["calc_usd"])
        if y == 1:
            wsw.write(18, y, "", fmts["calc_pct"])
        else:
            prev_m_col = col((y-1) * 12)
            wsw.write_formula(18, y,
                f"={last_m_col}{rows_w['Ending ARR']+1}/{prev_m_col}{rows_w['Ending ARR']+1}-1",
                fmts["calc_pct"])

    # ============= MRR-DETAIL =============
    wsm = wb.add_worksheet("MRR-Detail")
    wsm.set_column("A:A", 26); wsm.set_column("B:BH", 11); wsm.set_row(0, 28)
    wsm.merge_range(0, 0, 0, N_MONTHS, "MRR Detail — by Tier (reconciles to ARR Waterfall)", fmts["title"])
    wsm.write(2, 0, "Month", fmts["col_header"])
    for m in range(N_MONTHS):
        wsm.write(2, 1+m, f"M{m+1}", fmts["col_header"])
    # Pull cum customers from ARR-Waterfall and split by mix
    tier_labels = [("Tier 1 (Starter) MRR", T1_PRICE_ROW, T1_MIX),
                   ("Tier 2 (Pro) MRR",     T2_PRICE_ROW, T2_MIX),
                   ("Tier 3 (Enterprise) MRR", T3_PRICE_ROW, T3_MIX)]
    for i, (label, price_row, mix_row) in enumerate(tier_labels):
        wsm.write(3+i, 0, label, fmts["row_header"])
        for m in range(N_MONTHS):
            c = 1 + m; cur_col = col(c)
            wsm.write_formula(3+i, c,
                f"='ARR-Waterfall'!{cur_col}{rows_w['Cum customers (end)']+1}*Inputs!$B${mix_row}*Inputs!$B${price_row}",
                fmts["calc_usd"])
    wsm.write(6, 0, "Total MRR (sum)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsm.write_formula(6, c, f"=SUM({cur_col}4:{cur_col}6)", fmts["calc_bold_usd"])
    wsm.write(7, 0, "ARR check (×12)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsm.write_formula(7, c, f"={cur_col}7*12", fmts["calc_usd"])
    wsm.write(8, 0, "ARR-Waterfall Ending ARR", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsm.write_formula(8, c, f"='ARR-Waterfall'!{cur_col}{rows_w['Ending ARR']+1}", fmts["calc_usd"])
    wsm.write(9, 0, "Reconciliation Δ (should be ≈0)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsm.write_formula(9, c, f"={cur_col}8-{cur_col}9", fmts["calc_usd"])

    # ============= HEADCOUNT (quarterly) =============
    wsh = wb.add_worksheet("Headcount")
    wsh.set_column("A:A", 30); wsh.set_column("B:U", 11); wsh.set_row(0, 28)
    wsh.merge_range("A1:U1", "Headcount Plan — Quarterly Y1..Y5", fmts["title"])
    quarters = [f"Y{y}Q{q}" for y in range(1, 6) for q in range(1, 5)]
    wsh.write(2, 0, "Role", fmts["col_header"])
    for i, q in enumerate(quarters):
        wsh.write(2, 1+i, q, fmts["col_header"])
    for i, (role, salary, bucket, y1, y2, y3, y45) in enumerate(roles):
        wsh.write(3+i, 0, role, fmts["row_header"])
        for qi, q in enumerate(quarters):
            year = qi // 4 + 1
            hc = [y1, y2, y3, y45, y45][year - 1]
            wsh.write(3+i, 1+qi, hc, fmts["calc_int"])
    # Totals + costs
    nroles = len(roles)
    totrow = 3 + nroles
    wsh.write(totrow, 0, "Total Headcount", fmts["row_header"])
    for qi in range(len(quarters)):
        c = 1 + qi; cur_col = col(c)
        wsh.write_formula(totrow, c, f"=SUM({cur_col}4:{cur_col}{3+nroles})", fmts["calc_bold"])
    wsh.write(totrow+1, 0, "Quarterly Loaded Cost $", fmts["row_header"])
    for qi in range(len(quarters)):
        c = 1 + qi; cur_col = col(c)
        # cost = sum(role HC × role salary) / 4 (quarterly slice of annual loaded cost)
        wsh.write_formula(totrow+1, c,
            f"=SUMPRODUCT({cur_col}4:{cur_col}{3+nroles},Inputs!$B${HC_START}:$B${HC_END})/4",
            fmts["calc_bold_usd"])

    add_named(wb, "HC_Q_Cost_Row", f"Headcount!$A${totrow+2}")

    # ============= P&L =============
    wsp = wb.add_worksheet("PnL")
    wsp.set_column("A:A", 36); wsp.set_column("B:G", 14); wsp.set_row(0, 28)
    wsp.merge_range("A1:G1", "Multi-Step P&L (Mersch format) — Annual", fmts["title"])
    wsp.write(2, 0, "Line", fmts["col_header"])
    for y in range(1, 6):
        wsp.write(2, y, f"Year {y}", fmts["col_header"])
    # Helper: annualized revenue per year = sum of monthly MRR for that year
    # Use ARR-Waterfall MRR(end) average × 12 isn't perfect; use sum of (MRR start + MRR end)/2 per month
    # Simpler: revenue Y = average of opening+ending ARR / 12 × 12... but cleanest: SUM of MRR(end) × 1 each month.
    # Approximate: revenue = sum of monthly MRR values from ARR-Waterfall.
    def y_range(y, row_idx):
        start_col = col(1 + (y-1)*12)
        end_col   = col(1 + y*12 - 1)
        return f"'ARR-Waterfall'!{start_col}{row_idx}:{end_col}{row_idx}"

    # Revenue = SUM of monthly MRR ( =Ending ARR / 12 ) i.e. MRR(end) row
    pnl_layout = []
    rev_row = 4
    wsp.write(3, 0, "RECURRING SOFTWARE REVENUE", fmts["row_header"])
    for y in range(1, 6):
        wsp.write_formula(3, y, f"=SUM({y_range(y, rows_w['MRR (end)']+1)})", fmts["calc_usd"])
    wsp.write(4, 0, "Non-recurring (services/setup)", fmts["row_header"])
    for y in range(1, 6):
        wsp.write_formula(4, y, f"=B{rev_row}*0.05*({y}=1)+B{rev_row}*0.03*({y}=2)", fmts["calc_usd"])
    wsp.write(5, 0, "TOTAL REVENUE", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(5, y, f"={c_letter}{rev_row}+{c_letter}{rev_row+1}", fmts["calc_bold_usd"])
    wsp.write(6, 0, "COST OF REVENUE (COGS %)", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(6, y, f"={c_letter}6*COGS_PCT", fmts["calc_usd"])
    wsp.write(7, 0, "GROSS PROFIT", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(7, y, f"={c_letter}6-{c_letter}7", fmts["calc_bold_usd"])
    wsp.write(8, 0, "Gross Margin %", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(8, y, f"={c_letter}8/{c_letter}6", fmts["calc_pct"])
    # S&M
    wsp.write(9, 0, "Sales & Marketing", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        sm_pick = f'IF({y}=1,SM_Y1,IF({y}=2,SM_Y2,SM_Y3p))'
        wsp.write_formula(9, y, f"={c_letter}6*{sm_pick}", fmts["calc_usd"])
    # R&D
    wsp.write(10, 0, "Research & Development", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        rd_pick = f'IF({y}=1,RD_Y1,IF({y}=2,RD_Y2,RD_Y3p))'
        wsp.write_formula(10, y, f"={c_letter}6*{rd_pick}", fmts["calc_usd"])
    # G&A
    wsp.write(11, 0, "General & Administrative", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        ga_pick = f'IF({y}=1,GA_Y1*12,IF({y}=2,GA_Y2*12,GA_Y3p*12))'
        wsp.write_formula(11, y, f"={ga_pick}", fmts["calc_usd"])
    # Total opex
    wsp.write(12, 0, "TOTAL OPERATING EXPENSE", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(12, y, f"={c_letter}10+{c_letter}11+{c_letter}12", fmts["calc_bold_usd"])
    # Operating income
    wsp.write(13, 0, "OPERATING INCOME (LOSS)", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(13, y, f"={c_letter}8-{c_letter}13", fmts["calc_bold_usd"])
    wsp.write(14, 0, "Operating Margin %", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(14, y, f"={c_letter}14/{c_letter}6", fmts["calc_pct"])
    # Adjustments
    wsp.write(15, 0, "+ D&A (capex/5)", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        cx_pick = f'IF({y}=1,Capex_Y1,IF({y}=2,Capex_Y2,IF({y}=3,Capex_Y3,IF({y}=4,Capex_Y4,Capex_Y5))))/5'
        wsp.write_formula(15, y, f"={cx_pick}", fmts["calc_usd"])
    wsp.write(16, 0, "+ Stock-based comp (5% rev)", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(16, y, f"={c_letter}6*0.05", fmts["calc_usd"])
    wsp.write(17, 0, "ADJUSTED EBITDA", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(17, y, f"={c_letter}14+{c_letter}16+{c_letter}17", fmts["calc_bold_usd"])
    wsp.write(18, 0, "EBITDA Margin %", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(18, y, f"={c_letter}18/{c_letter}6", fmts["calc_pct"])
    wsp.write(19, 0, "Tax (on positive op income only)", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(19, y, f"=MAX(0,{c_letter}14)*Tax_Rate", fmts["calc_usd"])
    wsp.write(20, 0, "NET INCOME", fmts["row_header"])
    for y in range(1, 6):
        c_letter = col(y)
        wsp.write_formula(20, y, f"={c_letter}14-{c_letter}20", fmts["calc_bold_usd"])

    # ============= CASH =============
    wsc = wb.add_worksheet("Cash")
    wsc.set_column("A:A", 32); wsc.set_column("B:BH", 11); wsc.set_row(0, 28)
    wsc.merge_range(0, 0, 0, N_MONTHS, "Cash Flow — Monthly (60 months)", fmts["title"])
    wsc.write(2, 0, "Month", fmts["col_header"])
    for m in range(N_MONTHS):
        wsc.write(2, 1+m, f"M{m+1}", fmts["col_header"])
    # Use simplified monthly cash from MRR × GM − monthly opex − monthly capex + financing
    # Revenue (MRR end as proxy for monthly billings, since collection = monthly recurring)
    wsc.write(3, 0, "Revenue (cash collected, monthly)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsc.write_formula(3, c, f"='ARR-Waterfall'!{cur_col}{rows_w['MRR (end)']+1}", fmts["calc_usd"])
    wsc.write(4, 0, "COGS (monthly)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsc.write_formula(4, c, f"={cur_col}4*COGS_PCT", fmts["calc_usd"])
    wsc.write(5, 0, "Gross Profit", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsc.write_formula(5, c, f"={cur_col}4-{cur_col}5", fmts["calc_usd"])
    # Opex: simplified as fixed monthly = headcount $ + S&M % + G&A
    wsc.write(6, 0, "Total Opex (HC × time + S&M% + G&A)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        year = (m // 12) + 1
        sm_p = f'IF({year}=1,SM_Y1,IF({year}=2,SM_Y2,SM_Y3p))'
        ga_p = f'IF({year}=1,GA_Y1,IF({year}=2,GA_Y2,GA_Y3p))'
        rd_p = f'IF({year}=1,RD_Y1,IF({year}=2,RD_Y2,RD_Y3p))'
        wsc.write_formula(6, c,
            f"={cur_col}4*({sm_p}+{rd_p})+{ga_p}",
            fmts["calc_usd"])
    wsc.write(7, 0, "Operating Cash Flow", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsc.write_formula(7, c, f"={cur_col}6-{cur_col}7", fmts["calc_usd"])
    # Capex monthly = annual / 12
    wsc.write(8, 0, "Capex (monthly)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        year = (m // 12) + 1
        cx_p = f'IF({year}=1,Capex_Y1,IF({year}=2,Capex_Y2,IF({year}=3,Capex_Y3,IF({year}=4,Capex_Y4,Capex_Y5))))/12'
        wsc.write_formula(8, c, f"=-{cx_p}", fmts["calc_usd"])
    # Financing
    wsc.write(9, 0, "Equity raised (in month)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        # equity hits in M1 of each year for which raise > 0
        if (m % 12) == 0:
            year = (m // 12) + 1
            eq_pick = f'IF({year}=1,Eq_Y1,IF({year}=2,Eq_Y2,IF({year}=3,Eq_Y3,0)))'
            wsc.write_formula(9, c, f"={eq_pick}", fmts["calc_usd"])
        else:
            wsc.write(9, c, 0, fmts["calc_usd"])
    # Net change
    wsc.write(10, 0, "Net cash change", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsc.write_formula(10, c, f"={cur_col}8+{cur_col}9+{cur_col}10", fmts["calc_usd"])
    # Beginning + ending cash
    wsc.write(11, 0, "Beginning cash", fmts["row_header"])
    wsc.write_formula(11, 1, "=Start_Cash", fmts["calc_usd"])
    for m in range(1, N_MONTHS):
        c = 1 + m; prev_col = col(c-1)
        wsc.write_formula(11, c, f"={prev_col}13", fmts["calc_usd"])
    wsc.write(12, 0, "Ending cash", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        wsc.write_formula(12, c, f"={cur_col}12+{cur_col}11", fmts["calc_bold_usd"])
    # Cumulative FCF
    wsc.write(13, 0, "Cumulative FCF (Op + Investing)", fmts["row_header"])
    for m in range(N_MONTHS):
        c = 1 + m; cur_col = col(c)
        if m == 0:
            wsc.write_formula(13, c, f"={cur_col}8+{cur_col}9", fmts["calc_usd"])
        else:
            prev_col = col(c-1)
            wsc.write_formula(13, c, f"={prev_col}14+{cur_col}8+{cur_col}9", fmts["calc_usd"])
    # Conditional formatting: min cash highlight
    wsc.conditional_format(f"B13:{col(N_MONTHS)}13", {
        "type": "cell", "criteria": "<", "value": 100000, "format": fmts["bad"]
    })
    wsc.conditional_format(f"B13:{col(N_MONTHS)}13", {
        "type": "cell", "criteria": "between", "minimum": 100000, "maximum": 250000, "format": fmts["warn"]
    })

    # Runway calc + working-capital trough
    wsc.merge_range(15, 0, 15, 6, "Runway & Working-Capital Trough", fmts["h2"])
    wsc.write(16, 0, "Min ending cash (60 mo)", fmts["row_header"])
    wsc.write_formula(16, 1, f"=MIN(B13:{col(N_MONTHS)}13)", fmts["calc_bold_usd"])
    wsc.write(17, 0, "Month of trough", fmts["row_header"])
    wsc.write_formula(17, 1, f"=MATCH(MIN(B13:{col(N_MONTHS)}13),B13:{col(N_MONTHS)}13,0)", fmts["calc_int"])
    wsc.write(18, 0, "Months of runway from M1 (negative ⇒ year exhausted)", fmts["row_header"])
    wsc.write_formula(18, 1,
        f'=IFERROR(MATCH(TRUE,INDEX(B13:{col(N_MONTHS)}13<=0,0),0)-1,"60+")',
        fmts["calc"])
    wsc.write(19, 0, "End of period cash (Y5)", fmts["row_header"])
    last_m_col = col(N_MONTHS)
    wsc.write_formula(19, 1, f"={last_m_col}13", fmts["calc_bold_usd"])

    # ============= SENSITIVITY =============
    wss = wb.add_worksheet("Sensitivity")
    wss.set_column("A:A", 30); wss.set_column("B:H", 16); wss.set_row(0, 28)
    wss.merge_range("A1:H1", "Sensitivity — New-Logo Growth × Churn", fmts["title"])
    wss.write("A3", "Reading: each cell = Year-3 Ending ARR ($) under hypothetical inputs (illustrative — assumes linear scaling).",
              fmts["subtitle"])
    growth_axis = [-0.30, -0.20, -0.10, 0, 0.10, 0.20, 0.30]
    churn_axis  = [-0.30, -0.15, 0, 0.15, 0.30, 0.50, 1.0]
    wss.write(4, 0, "Churn Δ ↓  /  Growth Δ →", fmts["col_header"])
    for i, gv in enumerate(growth_axis):
        wss.write(4, 1+i, gv, fmts["col_header"])
    for j, cv in enumerate(churn_axis):
        wss.write(5+j, 0, cv, fmts["row_header"])
        for i, gv in enumerate(growth_axis):
            # Illustrative formula: Year-3 ARR ≈ Y3 baseline × (1+gv)^36 × (1-cv)^36 × Logo_Mult (simplified)
            # Use Year-3 baseline by sampling from waterfall
            baseline = "'ARR-Waterfall'!" + col(36) + str(rows_w['Ending ARR']+1)
            wss.write_formula(5+j, 1+i,
                f"={baseline}*(1+{gv})^12*(1-{cv})^12",
                fmts["calc_usd"])
    # Conditional formatting heatmap
    wss.conditional_format(f"B6:H{5+len(churn_axis)}", {
        "type": "3_color_scale",
        "min_color": "#F8696B", "mid_color": "#FFEB84", "max_color": "#63BE7B",
    })

    # ============= SCENARIOS =============
    wssc = wb.add_worksheet("Scenarios")
    wssc.set_column("A:A", 30); wssc.set_column("B:E", 16); wssc.set_row(0, 28)
    wssc.merge_range("A1:E1", "Scenarios — Base / Bull / Bear / Stress", fmts["title"])
    wssc.write("A2", "Toggle the active scenario on Inputs cell B" + str(SCEN_ROW) + ". Multipliers apply to logos, churn, ARPA.",
               fmts["subtitle"])
    wssc.write(3, 0, "Variable", fmts["col_header"])
    wssc.write(3, 1, "Base", fmts["col_header"])
    wssc.write(3, 2, "Bull", fmts["col_header"])
    wssc.write(3, 3, "Bear", fmts["col_header"])
    wssc.write(3, 4, "Stress", fmts["col_header"])
    sc_rows = [
        ("Logo growth multiplier", 1.00, 1.25, 0.75, 0.50),
        ("Churn multiplier",       1.00, 0.75, 1.50, 2.00),
        ("ARPA multiplier",        1.00, 1.20, 0.85, 0.70),
        ("FX depreciation %",      0.05, 0.03, 0.08, 0.15),
    ]
    for i, (lab, b, bu, be, st) in enumerate(sc_rows):
        wssc.write(4+i, 0, lab, fmts["row_header"])
        wssc.write(4+i, 1, b, fmts["calc"])
        wssc.write(4+i, 2, bu, fmts["calc"])
        wssc.write(4+i, 3, be, fmts["calc"])
        wssc.write(4+i, 4, st, fmts["calc"])
    wssc.write(9, 0, "Y3 ending ARR (driven by Inputs!Scen_Active)", fmts["row_header"])
    wssc.write_formula(9, 1, f"='ARR-Waterfall'!{col(36)}{rows_w['Ending ARR']+1}", fmts["calc_bold_usd"])
    wssc.write(10, 0, "Y5 ending ARR", fmts["row_header"])
    wssc.write_formula(10, 1, f"='ARR-Waterfall'!{col(60)}{rows_w['Ending ARR']+1}", fmts["calc_bold_usd"])

    # ============= BANKABILITY DASHBOARD =============
    wsd = wb.add_worksheet("Bankability-Dashboard")
    wsd.set_column("A:A", 32); wsd.set_column("B:D", 18); wsd.set_row(0, 30)
    wsd.merge_range("A1:D1", "Bankability Dashboard — SaaS KPIs", fmts["title"])
    kpis = [
        ("Y1 Revenue",             f"=PnL!B6",                                          "usd"),
        ("Y3 Revenue",             f"=PnL!D6",                                          "usd"),
        ("Y5 Revenue",             f"=PnL!F6",                                          "usd"),
        ("Y3 EBITDA Margin",       f"=PnL!D19",                                         "pct"),
        ("Y3 Ending ARR",          f"='ARR-Waterfall'!{col(36)}{rows_w['Ending ARR']+1}", "usd"),
        ("Y5 Ending ARR",          f"='ARR-Waterfall'!{col(60)}{rows_w['Ending ARR']+1}", "usd"),
        ("Min cash (60mo)",        f"=Cash!B17",                                        "usd"),
        ("Trough month",           f"=Cash!B18",                                        "int"),
        ("Gross Margin",           f"=GM_P",                                            "pct"),
        ("NRR (annual)",           f"=1+(Expansion_P-Rev_Churn_P-Contraction_P)*12",    "pct"),
        ("GRR (annual)",           f"=MAX(0,1-Rev_Churn_P*12)",                         "pct"),
        ("LTV:CAC",                f"=(ARPA_P*GM_P/Logo_Churn_P)/CAC_P",                "ratio"),
        ("CAC Payback (months)",   f"=CAC_P/(ARPA_P*GM_P)",                             "ratio"),
        ("Rule of 40 (Y3)",
            f"=('ARR-Waterfall'!{col(36)}{rows_w['Ending ARR']+1}/'ARR-Waterfall'!{col(24)}{rows_w['Ending ARR']+1}-1)+PnL!D19",
            "pct"),
        ("Magic Number (Y2)",
            f"=(('ARR-Waterfall'!{col(24)}{rows_w['Ending ARR']+1}-'ARR-Waterfall'!{col(12)}{rows_w['Ending ARR']+1}))/(PnL!B10)",
            "ratio"),
        ("Burn Multiple (Y2)",
            f"=IF(('ARR-Waterfall'!{col(24)}{rows_w['Ending ARR']+1}-'ARR-Waterfall'!{col(12)}{rows_w['Ending ARR']+1})>0,"
            f"MAX(0,-PnL!C18)/('ARR-Waterfall'!{col(24)}{rows_w['Ending ARR']+1}-'ARR-Waterfall'!{col(12)}{rows_w['Ending ARR']+1}),999)",
            "ratio"),
        ("Quick Ratio (illustrative)",
            f"=(Expansion_P+M1_Logos*ARPA_P/'ARR-Waterfall'!{col(12)}{rows_w['Ending ARR']+1}*12)/(Rev_Churn_P+Contraction_P)",
            "ratio"),
    ]
    r = 3
    for label, formula, kind in kpis:
        wsd.write(r, 0, label, fmts["kpi_label"])
        if kind == "pct":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_pct"])
        elif kind == "usd":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_usd"])
        elif kind == "int":
            wsd.write_formula(r, 1, formula, fmts["kpi_value"])
        else:
            wsd.write_formula(r, 1, formula, fmts["kpi_value"])
        wsd.set_row(r, 22)
        r += 1

    # Traffic lights on key rows
    # LTV:CAC is row index 12 in kpis list → spreadsheet row 16 (0-idx 15) i.e. cell B16
    # Indices: LTV:CAC at index 11 → row 14 (3 + 11). Use exact computed positions:
    # We will apply by approximate location.
    wsd.conditional_format("B15", {"type": "cell", "criteria": ">=", "value": 3, "format": fmts["good"]})
    wsd.conditional_format("B15", {"type": "cell", "criteria": "between", "minimum": 1.5, "maximum": 3, "format": fmts["warn"]})
    wsd.conditional_format("B15", {"type": "cell", "criteria": "<", "value": 1.5, "format": fmts["bad"]})
    wsd.conditional_format("B16", {"type": "cell", "criteria": "<=", "value": 18, "format": fmts["good"]})
    wsd.conditional_format("B16", {"type": "cell", "criteria": "between", "minimum": 18, "maximum": 30, "format": fmts["warn"]})
    wsd.conditional_format("B16", {"type": "cell", "criteria": ">", "value": 30, "format": fmts["bad"]})
    wsd.conditional_format("B17", {"type": "cell", "criteria": ">=", "value": 0.40, "format": fmts["good"]})
    wsd.conditional_format("B17", {"type": "cell", "criteria": "between", "minimum": 0.30, "maximum": 0.40, "format": fmts["warn"]})
    wsd.conditional_format("B17", {"type": "cell", "criteria": "<", "value": 0.30, "format": fmts["bad"]})

    # ARR growth chart
    ch_arr = wb.add_chart({"type": "line"})
    ch_arr.add_series({
        "name": "Ending ARR ($)",
        "categories": f"='ARR-Waterfall'!$B$3:${col(N_MONTHS)}$3",
        "values":     f"='ARR-Waterfall'!$B${rows_w['Ending ARR']+1}:${col(N_MONTHS)}${rows_w['Ending ARR']+1}",
        "line": {"color": "#1F3864", "width": 2.5},
    })
    ch_arr.set_title({"name": "Ending ARR — 60 Months"})
    ch_arr.set_y_axis({"name": "ARR ($)"})
    ch_arr.set_legend({"none": True})
    wsd.insert_chart("D3", ch_arr, {"x_scale": 1.5, "y_scale": 1.2})

    ch_cash = wb.add_chart({"type": "line"})
    ch_cash.add_series({
        "name": "Ending Cash ($)",
        "categories": f"=Cash!$B$3:${col(N_MONTHS)}$3",
        "values":     f"=Cash!$B$13:${col(N_MONTHS)}$13",
        "line": {"color": "#C65911", "width": 2.5},
    })
    ch_cash.set_title({"name": "Ending Cash — Working-Capital Trough"})
    ch_cash.set_y_axis({"name": "Cash ($)"})
    ch_cash.set_legend({"none": True})
    wsd.insert_chart("D24", ch_cash, {"x_scale": 1.5, "y_scale": 1.2})

    ch_pnl = wb.add_chart({"type": "column"})
    ch_pnl.add_series({
        "name": "Revenue", "categories": "=PnL!$B$3:$F$3",
        "values": "=PnL!$B$6:$F$6", "fill": {"color": "#1F3864"},
    })
    ch_pnl.add_series({
        "name": "Opex", "categories": "=PnL!$B$3:$F$3",
        "values": "=PnL!$B$13:$F$13", "fill": {"color": "#C65911"},
    })
    ch_pnl.set_title({"name": "Revenue vs Opex (Annual)"})
    ch_pnl.set_legend({"position": "bottom"})
    wsd.insert_chart("D45", ch_pnl, {"x_scale": 1.5, "y_scale": 1.2})

    # ============= AFRICA-NOTES =============
    wsa = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsa, fmts, extra_notes=[
        ("DFI / Local Bank Format",
         "DFIs (FMO, Norfund, IFC, Proparco) + local banks (Stanbic, Equity, KCB, Centenary) expect "
         "local-currency primary view. Build the model in USD here; toggle the FX row on Inputs and "
         "produce a parallel local-currency view for submission."),
        ("AI Cost Sensitivity Connection",
         "AI cost-per-tenant is FX-exposed (LLM APIs are USD-priced). The dedicated workbook "
         "`saas-ai-cost-of-tenant-calculator.xlsx` should feed the COGS % cell on Inputs Section 4. "
         "Refresh quarterly or when AI pricing changes."),
    ])

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
