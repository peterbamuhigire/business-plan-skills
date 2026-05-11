"""Build saas-cohort-and-retention-model.xlsx.

36-month logo + revenue cohort matrices with optional tenure decay, NRR/GRR
trend, and separate involuntary-churn cohort by African payment rail.

Spec: skills/10-financial-projections/references/saas-cohort-and-retention-model-template.md
"""
import os, sys
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _common import make_formats, write_readme, write_africa_notes, add_named  # noqa

OUT = os.path.normpath(os.path.join(
    HERE, "..", "..", "skills", "saas-unit-economics-and-cohort-model",
    "templates", "saas-cohort-and-retention-model.xlsx"
))

N_COHORTS = 12          # 12 monthly cohorts modeled
N_MONTHS  = 36          # 36 months of horizon per cohort


def build():
    wb = xlsxwriter.Workbook(OUT)
    fmts = make_formats(wb)

    # ----- README -----
    ws_readme = wb.add_worksheet("README")
    write_readme(ws_readme, fmts,
        "SaaS Cohort & Retention Model",
        "36-month logo and revenue cohort retention matrix with optional tenure-decay "
        "(churn falls as cohorts mature), NRR / GRR trend, and separate involuntary-churn "
        "tracking by African payment rail (M-Pesa, MoMo, card). Surfaces the 'smile curve' "
        "test that distinguishes net-negative-churn SaaS from acquisition-treadmill SaaS.",
        sheets=[
            ("Inputs", "New logos by channel (12 mo), ARPA, base churn, tenure decay factor, expansion, involuntary churn by rail."),
            ("Logo-Cohort", "36-month logo retention matrix, formula-driven, with cohort heatmap."),
            ("Revenue-Cohort", "Revenue-weighted retention with expansion compounding; smile-curve test."),
            ("NRR-GRR", "Aggregate NRR and GRR trended monthly; trigger thresholds."),
            ("Involuntary-Churn", "Dunning-recoverable vs hard-lost across M-Pesa / MoMo / Card rails."),
            ("Dashboard", "Cohort heatmap, NRR trend, churn curve, smile-curve test."),
            ("Africa-Notes", "Payment-rail mechanics, public-sector cohort split, regional split discipline."),
        ],
        owner="CFO / Head of Customer Success",
        cadence="Monthly cohort refresh from billing system. Quarterly QBR slide.",
        sources="Mersch (Hacking SaaS) ch. 11; Skok forentrepreneurs.com; ChartMogul SaaS Benchmarks; Garbugli.",
    )

    # ----- Inputs -----
    ws = wb.add_worksheet("Inputs")
    ws.set_column("A:A", 40); ws.set_column("B:M", 10); ws.set_row(0, 28)
    ws.merge_range("A1:M1", "Inputs — Cohort & Retention Model", fmts["title"])

    ws.merge_range("A3:M3", "1. New Logos Acquired per Month (12 cohorts)", fmts["h2"])
    ws.write("A4", "Month / Cohort", fmts["col_header"])
    months = [f"M{i:02d}" for i in range(1, N_COHORTS+1)]
    for i, m in enumerate(months):
        ws.write(3, 1+i, m, fmts["col_header"])
    ws.write("A5", "Paid channel", fmts["row_header"])
    ws.write("A6", "Inbound channel", fmts["row_header"])
    ws.write("A7", "Outbound channel", fmts["row_header"])
    ws.write("A8", "Partner channel", fmts["row_header"])
    defaults = {
        4: [3,4,5,6,8,10,12,12,15,15,18,20],
        5: [5,6,7,9,12,15,18,20,22,25,28,32],
        6: [2,2,3,4,5,6,8,10,12,12,14,16],
        7: [1,1,2,2,3,4,5,5,6,7,8,10],
    }
    for r_idx, vals in defaults.items():
        for c_idx, v in enumerate(vals):
            ws.write(r_idx, 1+c_idx, v, fmts["input_int"])
    ws.write("A9", "Total new logos (calc)", fmts["row_header"])
    for c in range(N_COHORTS):
        col = chr(ord('B')+c)
        ws.write_formula(8, 1+c, f"=SUM({col}5:{col}8)", fmts["calc_bold"])

    ws.merge_range("A11:M11", "2. Pricing & Expansion", fmts["h2"])
    ws.write("A12", "ARPA ($/month)", fmts["row_header"]); ws.write("B12", 79, fmts["input_usd2"])
    ws.write("A13", "Monthly expansion rate (existing customers)", fmts["row_header"]); ws.write("B13", 0.012, fmts["input_pct"])
    ws.write("A14", "Monthly contraction rate", fmts["row_header"]); ws.write("B14", 0.004, fmts["input_pct"])

    ws.merge_range("A16:M16", "3. Churn — Base + Tenure Decay", fmts["h2"])
    ws.write("A17", "Base monthly logo churn (M1)", fmts["row_header"]); ws.write("B17", 0.040, fmts["input_pct"])
    ws.write("A18", "Tenure decay factor (per month, applied multiplicatively)", fmts["row_header"]); ws.write("B18", 0.97, fmts["input"])
    ws.write("D17", "Rationale: cohorts mature → churn falls. 0.97 means each month's churn is 97% of the prior month's.", fmts["note"])
    ws.write("A19", "Floor monthly logo churn (long-run)", fmts["row_header"]); ws.write("B19", 0.010, fmts["input_pct"])
    ws.write("A20", "Monthly revenue (gross) churn (base)", fmts["row_header"]); ws.write("B20", 0.030, fmts["input_pct"])

    ws.merge_range("A22:M22", "4. Involuntary Churn by Payment Rail", fmts["h2"])
    ws.write("A23", "% revenue collected via M-Pesa", fmts["row_header"]); ws.write("B23", 0.35, fmts["input_pct"])
    ws.write("A24", "% revenue collected via MoMo (MTN/Airtel)", fmts["row_header"]); ws.write("B24", 0.30, fmts["input_pct"])
    ws.write("A25", "% revenue collected via card / Stripe / Flutterwave", fmts["row_header"]); ws.write("B25", 0.25, fmts["input_pct"])
    ws.write("A26", "% revenue collected via bank-transfer / invoice", fmts["row_header"]); ws.write("B26", 0.10, fmts["input_pct"])
    ws.write("A27", "M-Pesa monthly involuntary churn", fmts["row_header"]); ws.write("B27", 0.005, fmts["input_pct"])
    ws.write("A28", "MoMo monthly involuntary churn", fmts["row_header"]); ws.write("B28", 0.008, fmts["input_pct"])
    ws.write("A29", "Card monthly involuntary churn", fmts["row_header"]); ws.write("B29", 0.006, fmts["input_pct"])
    ws.write("A30", "Bank-transfer monthly involuntary churn", fmts["row_header"]); ws.write("B30", 0.001, fmts["input_pct"])
    ws.write("A31", "Dunning recovery rate", fmts["row_header"]); ws.write("B31", 0.40, fmts["input_pct"])
    ws.write("D31", "% of failed payments recovered via 3-retry dunning over 7 days.", fmts["note"])

    ws.merge_range("A33:M33", "5. FX", fmts["h2"])
    ws.write("A34", "Reporting currency", fmts["row_header"]); ws.write("B34", "UGX", fmts["input_text"])
    ws.write("A35", "FX (local per 1 USD)", fmts["row_header"]); ws.write("B35", 3800, fmts["input"])

    # Named ranges
    add_named(wb, "ARPA_C", "Inputs!$B$12")
    add_named(wb, "Expansion_C", "Inputs!$B$13")
    add_named(wb, "Contraction_C", "Inputs!$B$14")
    add_named(wb, "Base_Logo_Churn", "Inputs!$B$17")
    add_named(wb, "Decay_Factor", "Inputs!$B$18")
    add_named(wb, "Churn_Floor", "Inputs!$B$19")
    add_named(wb, "Base_Rev_Churn", "Inputs!$B$20")
    add_named(wb, "MPesa_Mix", "Inputs!$B$23")
    add_named(wb, "MoMo_Mix", "Inputs!$B$24")
    add_named(wb, "Card_Mix", "Inputs!$B$25")
    add_named(wb, "Bank_Mix", "Inputs!$B$26")
    add_named(wb, "MPesa_Invol", "Inputs!$B$27")
    add_named(wb, "MoMo_Invol", "Inputs!$B$28")
    add_named(wb, "Card_Invol", "Inputs!$B$29")
    add_named(wb, "Bank_Invol", "Inputs!$B$30")
    add_named(wb, "Dunning_Recovery", "Inputs!$B$31")
    add_named(wb, "FX_C", "Inputs!$B$35")

    # ----- Logo-Cohort -----
    wsl = wb.add_worksheet("Logo-Cohort")
    wsl.set_column("A:A", 14); wsl.set_column("B:AN", 7); wsl.set_row(0, 26)
    wsl.merge_range(0, 0, 0, N_MONTHS, "Logo Cohort Retention (% of original cohort still active)", fmts["title"])
    wsl.write(2, 0, "Retention(t) = retention(t-1) × (1 - churn_t), churn_t = MAX(floor, base × decay^t)", fmts["subtitle"])
    wsl.write(4, 0, "Cohort", fmts["col_header"])
    for t in range(N_MONTHS+1):
        wsl.write(4, 1+t, f"M{t}", fmts["col_header"])
    # Each cohort row
    for i in range(N_COHORTS):
        wsl.write(5+i, 0, f"Cohort {i+1:02d}", fmts["row_header"])
        for t in range(N_MONTHS+1):
            col = chr(ord('B')+t) if t < 25 else None  # we use letter only for readability
            if t == 0:
                wsl.write(5+i, 1+t, 1.0, fmts["calc_pct"])
            else:
                # Reference previous month; churn_t formula
                prev_col_idx = t  # column B is t=0 (col index 1)
                # build A1 column letters dynamically
                def col_letter(idx):
                    s = ""
                    n = idx
                    while True:
                        s = chr(ord('A') + n % 26) + s
                        n = n // 26 - 1
                        if n < 0: break
                    return s
                prev_cell = f"{col_letter(t)}{6+i}"   # row 6+i (1-idx) = row index 5+i + 1
                # Churn for this month: MAX(Churn_Floor, Base_Logo_Churn * Decay_Factor^t)
                wsl.write_formula(5+i, 1+t,
                    f"={prev_cell}*(1-MAX(Churn_Floor, Base_Logo_Churn*Decay_Factor^{t-1}))",
                    fmts["calc_pct"])
    # Heatmap
    last_col_letter = "AN"  # safe range
    wsl.conditional_format(f"B6:{last_col_letter}{5+N_COHORTS}", {
        "type": "3_color_scale",
        "min_color": "#F8696B", "mid_color": "#FFEB84", "max_color": "#63BE7B",
        "min_type": "num", "min_value": 0.2,
        "mid_type": "num", "mid_value": 0.6,
        "max_type": "num", "max_value": 1.0,
    })

    # ----- Revenue-Cohort -----
    wsr = wb.add_worksheet("Revenue-Cohort")
    wsr.set_column("A:A", 14); wsr.set_column("B:AN", 7); wsr.set_row(0, 26)
    wsr.merge_range(0, 0, 0, N_MONTHS, "Revenue Cohort Retention (NRR per cohort)", fmts["title"])
    wsr.write(2, 0, "Rev(t) = Rev(t-1) × Logo_Retention_growth × (1 + Expansion - Contraction). Includes expansion compounding.", fmts["subtitle"])
    wsr.write(4, 0, "Cohort", fmts["col_header"])
    for t in range(N_MONTHS+1):
        wsr.write(4, 1+t, f"M{t}", fmts["col_header"])
    for i in range(N_COHORTS):
        wsr.write(5+i, 0, f"Cohort {i+1:02d}", fmts["row_header"])
        for t in range(N_MONTHS+1):
            if t == 0:
                wsr.write(5+i, 1+t, 1.0, fmts["calc_pct"])
            else:
                def col_letter(idx):
                    s = ""; n = idx
                    while True:
                        s = chr(ord('A') + n % 26) + s
                        n = n // 26 - 1
                        if n < 0: break
                    return s
                # Revenue retention = logo retention × cumulative expansion factor
                # = Logo-Cohort!Bt × (1+Expansion-Contraction)^t / (1+0)^0
                logo_ref = f"'Logo-Cohort'!{col_letter(t+1)}{6+i}"
                wsr.write_formula(5+i, 1+t,
                    f"={logo_ref}*(1+Expansion_C-Contraction_C)^{t}",
                    fmts["calc_pct"])
    wsr.conditional_format(f"B6:AN{5+N_COHORTS}", {
        "type": "3_color_scale",
        "min_color": "#F8696B", "mid_color": "#FFEB84", "max_color": "#63BE7B",
        "min_type": "num", "min_value": 0.5,
        "mid_type": "num", "mid_value": 1.0,
        "max_type": "num", "max_value": 1.5,
    })

    # ----- NRR-GRR -----
    wsn = wb.add_worksheet("NRR-GRR")
    wsn.set_column("A:A", 32); wsn.set_column("B:AN", 9); wsn.set_row(0, 28)
    wsn.merge_range(0, 0, 0, 12, "NRR / GRR Aggregate Trend (annualised)", fmts["title"])
    wsn.write(2, 0, "Period", fmts["col_header"])
    for q in range(1, 13):
        wsn.write(2, q, f"M{q*3}", fmts["col_header"])
    wsn.write(3, 0, "GRR (annual, modeled flat from inputs)", fmts["row_header"])
    for q in range(1, 13):
        wsn.write_formula(3, q, f"=MAX(0, 1-Base_Rev_Churn*12)", fmts["calc_pct"])
    wsn.write(4, 0, "NRR (annual, modeled flat from inputs)", fmts["row_header"])
    for q in range(1, 13):
        wsn.write_formula(4, q, f"=1+(Expansion_C-Base_Rev_Churn-Contraction_C)*12", fmts["calc_pct"])
    wsn.write(5, 0, "Target NRR (>=110% best)", fmts["row_header"])
    for q in range(1, 13):
        wsn.write(5, q, 1.10, fmts["calc_pct"])
    wsn.write(6, 0, "Target GRR (>=85% Mid)", fmts["row_header"])
    for q in range(1, 13):
        wsn.write(6, q, 0.85, fmts["calc_pct"])

    # ----- Involuntary-Churn -----
    wsi = wb.add_worksheet("Involuntary-Churn")
    wsi.set_column("A:A", 36); wsi.set_column("B:F", 16); wsi.set_row(0, 28)
    wsi.merge_range("A1:F1", "Involuntary Churn — by Payment Rail", fmts["title"])
    wsi.write(2, 0, "Rail", fmts["col_header"]); wsi.write(2, 1, "Revenue mix", fmts["col_header"])
    wsi.write(2, 2, "Monthly invol. churn", fmts["col_header"])
    wsi.write(2, 3, "Annualised", fmts["col_header"])
    wsi.write(2, 4, "Dunning-recovered", fmts["col_header"])
    wsi.write(2, 5, "Hard-lost (annual)", fmts["col_header"])
    rails = [
        ("M-Pesa", "MPesa_Mix", "MPesa_Invol"),
        ("MoMo (MTN/Airtel)", "MoMo_Mix", "MoMo_Invol"),
        ("Card", "Card_Mix", "Card_Invol"),
        ("Bank-transfer / invoice", "Bank_Mix", "Bank_Invol"),
    ]
    for i, (name, mix, invol) in enumerate(rails):
        r = 3 + i
        wsi.write(r, 0, name, fmts["row_header"])
        wsi.write_formula(r, 1, f"={mix}", fmts["calc_pct"])
        wsi.write_formula(r, 2, f"={invol}", fmts["calc_pct"])
        wsi.write_formula(r, 3, f"={invol}*12", fmts["calc_pct"])
        wsi.write_formula(r, 4, f"={invol}*12*Dunning_Recovery", fmts["calc_pct"])
        wsi.write_formula(r, 5, f"={invol}*12*(1-Dunning_Recovery)", fmts["calc_pct"])
    # Blended involuntary churn
    wsi.write(7, 0, "BLENDED (rev-mix-weighted)", fmts["row_header"])
    wsi.write_formula(7, 2,
        "=MPesa_Mix*MPesa_Invol+MoMo_Mix*MoMo_Invol+Card_Mix*Card_Invol+Bank_Mix*Bank_Invol",
        fmts["calc_bold_pct"])
    wsi.write_formula(7, 3, "=C8*12", fmts["calc_bold_pct"])
    wsi.write_formula(7, 4, "=D8*Dunning_Recovery", fmts["calc_bold_pct"])
    wsi.write_formula(7, 5, "=D8*(1-Dunning_Recovery)", fmts["calc_bold_pct"])

    wsi.merge_range("A11:F11", "Operating implications", fmts["h2"])
    wsi.merge_range("A12:F12",
        "Hard-lost annual % is the real customer-attrition consequence of payment-rail friction. "
        "Reduce it via (1) STK-Push retry sequencing on M-Pesa, (2) PIN-failure SMS guidance on MoMo, "
        "(3) Account-Updater on card. Best-in-class target hard-lost <1% — Africa typical 3-6%.",
        fmts["note"])

    # ----- Dashboard -----
    wsd = wb.add_worksheet("Dashboard")
    wsd.set_column("A:A", 32); wsd.set_column("B:E", 18); wsd.set_row(0, 30)
    wsd.merge_range("A1:E1", "Dashboard — Cohort & Retention", fmts["title"])

    kpis = [
        ("Annualised GRR",        "=MAX(0, 1-Base_Rev_Churn*12)",                          "pct"),
        ("Annualised NRR",        "=1+(Expansion_C-Base_Rev_Churn-Contraction_C)*12",      "pct"),
        ("Blended Involuntary Churn (annual)",
                                  "='Involuntary-Churn'!D8",                               "pct"),
        ("Hard-lost annual %",    "='Involuntary-Churn'!F8",                               "pct"),
        ("12-month Logo Retention (cohort 01)",   "='Logo-Cohort'!N6",                     "pct"),
        ("24-month Logo Retention (cohort 01)",   "='Logo-Cohort'!Z6",                     "pct"),
        ("12-month Revenue Retention (cohort 01)","='Revenue-Cohort'!N6",                  "pct"),
        ("24-month Revenue Retention (cohort 01)","='Revenue-Cohort'!Z6",                  "pct"),
    ]
    r = 3
    for label, formula, kind in kpis:
        wsd.write(r, 0, label, fmts["kpi_label"])
        wsd.write_formula(r, 1, formula, fmts["kpi_value_pct"] if kind == "pct" else fmts["kpi_value"])
        wsd.set_row(r, 22); r += 1

    # Conditional format on Dashboard NRR (row 4 = index 4)
    wsd.conditional_format("B5", {"type": "cell", "criteria": ">=", "value": 1.10, "format": fmts["good"]})
    wsd.conditional_format("B5", {"type": "cell", "criteria": "between", "minimum": 1.00, "maximum": 1.10, "format": fmts["warn"]})
    wsd.conditional_format("B5", {"type": "cell", "criteria": "<", "value": 1.00, "format": fmts["bad"]})

    # Charts
    # Smile curve from cohort 01
    ch1 = wb.add_chart({"type": "line"})
    ch1.add_series({
        "name": "Cohort 01 Revenue Retention",
        "categories": f"='Revenue-Cohort'!$B$5:$AN$5",
        "values":     f"='Revenue-Cohort'!$B$6:$AN$6",
        "line": {"color": "#1F3864", "width": 2.5},
    })
    ch1.add_series({
        "name": "Cohort 06 Revenue Retention",
        "categories": f"='Revenue-Cohort'!$B$5:$AN$5",
        "values":     f"='Revenue-Cohort'!$B$11:$AN$11",
        "line": {"color": "#2E75B6", "width": 2.0, "dash_type": "dash"},
    })
    ch1.set_title({"name": "Smile-Curve Test — Revenue Cohort"})
    ch1.set_y_axis({"name": "% of M0 revenue", "num_format": "0%"})
    ch1.set_x_axis({"name": "Months since acquisition"})
    ch1.set_legend({"position": "bottom"})
    wsd.insert_chart("F3", ch1, {"x_scale": 1.4, "y_scale": 1.2})

    ch2 = wb.add_chart({"type": "line"})
    ch2.add_series({
        "name": "Cohort 01 Logo Retention",
        "categories": f"='Logo-Cohort'!$B$5:$AN$5",
        "values":     f"='Logo-Cohort'!$B$6:$AN$6",
        "line": {"color": "#C65911", "width": 2.5},
    })
    ch2.set_title({"name": "Logo Retention — Cohort 01"})
    ch2.set_y_axis({"name": "% retained", "num_format": "0%"})
    ch2.set_legend({"position": "bottom"})
    wsd.insert_chart("F25", ch2, {"x_scale": 1.4, "y_scale": 1.2})

    ch3 = wb.add_chart({"type": "column"})
    ch3.add_series({
        "name": "Hard-lost annual %",
        "categories": "='Involuntary-Churn'!$A$4:$A$7",
        "values":     "='Involuntary-Churn'!$F$4:$F$7",
        "fill": {"color": "#C65911"},
    })
    ch3.set_title({"name": "Hard-lost Annual % by Payment Rail"})
    ch3.set_y_axis({"name": "% revenue", "num_format": "0.0%"})
    ch3.set_legend({"none": True})
    wsd.insert_chart("F48", ch3, {"x_scale": 1.4, "y_scale": 1.0})

    # ----- Africa-Notes -----
    wsa = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsa, fmts, extra_notes=[
        ("Regional Cohort Splits",
         "For multi-region SaaS, split cohorts by region (Nairobi/Mombasa/Kisumu; Lagos/Abuja/Port Harcourt; "
         "Kampala/Mbarara/Gulu). Regional economic conditions drive different churn dynamics — "
         "a single national curve hides actionable variance."),
        ("Public-Sector vs Private-Sector Cohorts",
         "Public-sector / NGO cohorts in Africa churn by funding cycle (renewal lapse at end of grant period, "
         "not value dissatisfaction). Separate from private-sector cohorts or the curve will mislead investors."),
    ])

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
