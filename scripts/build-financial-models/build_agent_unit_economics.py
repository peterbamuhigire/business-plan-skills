"""Build saas-agent-unit-economics-model.xlsx.

Full agent unit-economics workbook: cohort + LTV/CAC + Rule-of-40 + moat scorecard
+ AI-vs-Agent comparison + stress test + dashboard. Sits on top of the
cost-per-task workbook (which produces the cost-per-resolved input) and the
existing saas-unit-economics-model.xlsx (SaaS baseline).

Spec sources:
  - skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md
  - skills/10-financial-projections/saas-agent-unit-economics-and-cogs/references/saas-agent-unit-economics-template.md
  - skills/06-competitive-analysis/saas-agent-moat-and-wrapper-risk/references/saas-agent-moats-and-wrapper-risk-checklist.md (8-Q moat rubric)
"""
import os
import sys
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _common import make_formats, write_readme, write_africa_notes, add_named  # noqa: E402

OUT = os.path.normpath(os.path.join(
    HERE, "..", "..", "skills", "10-financial-projections",
    "saas-agent-unit-economics-and-cogs", "templates",
    "saas-agent-unit-economics-model.xlsx"
))


def build():
    wb = xlsxwriter.Workbook(OUT)
    fmts = make_formats(wb)

    # =============================================================
    # README
    # =============================================================
    ws_r = wb.add_worksheet("README")
    write_readme(
        ws_r, fmts,
        "SaaS Agent Unit Economics Model",
        "End-to-end agent-business unit economics. Cohort retention with supervised-vs-agentic "
        "phase split (first 3 months heavy HITL, then autonomy ramp). Multi-LTV formulations "
        "(simple, with churn, with expansion, GM-adjusted, with HITL-cost-ramp). Agent LTV:CAC, "
        "CAC payback, NRR, GRR, Rule of 40, Magic Number, Burn Multiple, Quick Ratio. "
        "Cost-per-resolved-task trend across 24 months (autonomy progression hypothesis). "
        "Wrapper-vs-Moat scorecard (the 8-question rubric, each 0-3) drives a valuation-"
        "multiplier modifier. AI-vs-Agent comparison on identical tenant base shows why "
        "agent economics are materially different from SaaS + AI overlay. Stress-test sheet "
        "applies the same shock set as the cost-per-task workbook to full unit economics "
        "and reports runway impact.",
        sheets=[
            ("Inputs",                     "Yellow cells. Agent ARR by tier, ACV, GM baseline, churn, CAC by channel, HITL-cost ratio, retention multipliers, expansion mechanics, autonomy progression."),
            ("Cohort",                     "24-month logo+revenue cohort. Supervised period (M0-M2, intervention heavy) → Agentic period (M3-M24, autonomy ramp drives expansion). Resolution-per-tenant grows with autonomy tier."),
            ("Unit-Economics",             "Five LTV formulations; CAC payback; LTV:CAC; NRR/GRR; Magic Number; Rule of 40; Burn Multiple; Quick Ratio. Plus cost-per-resolved-task trend + HITL ratio trend."),
            ("Wrapper-vs-Moat-Scoring",    "Eight 0-3 scored cells per the rubric (proprietary tools, action data, integration depth, eval-loop, trust, regulatory, switching, distribution). Score / 24 → valuation modifier."),
            ("AI-vs-Agent-Comparison",     "Side-by-side: SaaS baseline vs AI overlay vs Agent — on identical tenant base. Highlights cost structure, expansion mechanics, and LTV:CAC delta."),
            ("Dashboard",                  "Traffic lights for: LTV:CAC, CAC payback, Rule of 40, agent GM, NRR, wrapper score, HITL ratio trend. Charts: cohort retention, cost/resolved trend, agent revenue mix."),
            ("Stress-Test",                "Six pre-coded shocks applied to the full unit economics (not just cost): Provider 5x, Intervention 2x, Model deprecation 2x, Tool outage 3x, Abandonment improvement, Combined. Runway impact in months."),
            ("Africa-Notes",               "FX, mobile-money fee impact, longer collections on SLA-tied per-resolution, USD enterprise tier, sovereign-AI premium, low HITL floor."),
        ],
        owner="CFO + Head of Agent (joint). Wrapper-vs-Moat sheet co-owned with CEO + Head of Product. "
              "Cohort sheet co-owned with Eval Engineer (resolution rate trend).",
        cadence="Monthly: full unit-economics refresh; agent gross margin; HITL share; cost-per-resolved trend. "
                "Quarterly: cohort re-fit; Wrapper-vs-Moat rescoring; AI-vs-Agent comparison re-run; stress-test refresh. "
                "Variance >+15% on cost-per-resolved or <-3pp on agent GM MoM triggers a re-plan loop.",
        sources="saas-agent-unit-economics-template.md, saas-agent-moats-and-wrapper-risk-checklist.md, "
                "saas-agent-cost-per-task-calculator.xlsx (this engine's cost feed), "
                "saas-unit-economics-model.xlsx (SaaS baseline for AI-vs-Agent comparison). "
                "Mersch CFO discipline; Cotton SaaS rule-of-3-and-10; Skok LTV:CAC."
    )

    # =============================================================
    # INPUTS
    # =============================================================
    ws = wb.add_worksheet("Inputs")
    ws.set_column("A:A", 50); ws.set_column("B:B", 16); ws.set_column("C:C", 16)
    ws.set_column("D:D", 60); ws.set_row(0, 28)
    ws.merge_range("A1:D1", "Inputs — Agent Unit Economics", fmts["title"])
    ws.write("A2", "Yellow = input. White = formula. Agent business = subscription + per-resolution hybrid.", fmts["subtitle"])

    # Section 1: ARR / pricing
    ws.merge_range("A4:D4", "1. Agent ARR by Tier", fmts["h2"])
    rows = [
        ("Free tier MRR ($)",                0,    "input_usd2", "Self-serve, may be $0; bundled with per-resolution metering only."),
        ("Pro tier MRR ($)",                 149,  "input_usd2", "Subscription + per-resolution bundle. Higher than non-agent Pro ($79)."),
        ("Enterprise tier MRR ($)",          1500, "input_usd2", "Enterprise agent — typically 2-3x non-agent Ent because per-outcome value."),
        ("Per-resolved-task price avg ($)",  0.50, "input_usd2", "Blended across tiers for cohort-driven per-resolution revenue."),
        ("Resolutions/tenant/month (M0)",    20,   "input_int",  "Supervised period start. Low autonomy = lower volume."),
        ("Resolutions/tenant/month (M12)",   200,  "input_int",  "Full agentic period. Autonomy progression drives expansion."),
        ("Resolutions/tenant/month (M24)",   400,  "input_int",  "Mature; tier-upgrade pushes deeper agent use."),
        ("% customers Free",                 0.30, "input_pct",  ""),
        ("% customers Pro",                  0.55, "input_pct",  ""),
        ("% customers Enterprise",           0.15, "input_pct",  ""),
    ]
    r = 4
    for label, val, kind, note in rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        ws.write(r, 3, note, fmts["note"])
        r += 1
    FREE_MRR_R = 5; PRO_MRR_R = 6; ENT_MRR_R = 7
    PRICE_RES_R = 8
    RES_M0_R = 9; RES_M12_R = 10; RES_M24_R = 11
    PCT_FREE_R = 12; PCT_PRO_R = 13; PCT_ENT_R = 14

    # Calc — Blended subscription ARPA & ACV
    ws.write(r, 0, "Blended subscription MRR ($) [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{FREE_MRR_R}*B{PCT_FREE_R}+B{PRO_MRR_R}*B{PCT_PRO_R}+B{ENT_MRR_R}*B{PCT_ENT_R}",
                     fmts["calc_usd2"])
    ws.write(r, 3, "Σ tier MRR × tier mix.", fmts["note"])
    BLENDED_ARPA_R = r + 1
    r += 1
    ws.write(r, 0, "Blended ACV (subscription only) ($) [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{BLENDED_ARPA_R}*12", fmts["calc_usd"])
    ACV_R = r + 1
    r += 1
    ws.write(r, 0, "Blended monthly per-resolution rev (M12 anchor) [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{RES_M12_R}*B{PRICE_RES_R}", fmts["calc_usd2"])
    RES_REV_R = r + 1
    r += 1
    ws.write(r, 0, "Total blended ARPA (subscription + per-resolution) [calc]", fmts["row_header"])
    ws.write_formula(r, 1, f"=B{BLENDED_ARPA_R}+B{RES_REV_R}", fmts["calc_bold_usd"])
    TOT_ARPA_R = r + 1
    r += 2

    # Section 2: agent gross-margin baseline (from cost-per-task workbook reference)
    ws.merge_range(r, 0, r, 3, "2. Agent GM Baseline (cross-ref cost-per-task workbook)", fmts["h2"]); r += 1
    gm_rows = [
        ("Cost per resolved task — Enterprise tier ($)", 0.20, "input_usd2",
            "Paste from saas-agent-cost-per-task-calculator.xlsx → Dashboard."),
        ("Cost per resolved task — Pro tier ($)",         0.10, "input_usd2", ""),
        ("Cost per resolved task — Free tier ($)",        0.05, "input_usd2", ""),
        ("HITL-cost ratio (% of agent COGS)",             0.18, "input_pct",
            "Headline HITL share — declining trend is a strong signal."),
        ("Other COGS % of subscription rev (hosting + support + payment)", 0.15, "input_pct", ""),
        ("Agent baseline gross margin (target)",          0.65, "input_pct",
            "Target benchmark; computed actuals reported below."),
    ]
    for label, val, kind, note in gm_rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        ws.write(r, 3, note, fmts["note"])
        r += 1
    CPR_ENT_R = r - 5
    CPR_PRO_R = r - 4
    CPR_FREE_R = r - 3
    HITL_RAT_R = r - 2
    OTH_COGS_R = r - 1
    GM_TGT_R   = r
    # Blended cost per resolved
    ws.write(r, 0, "Blended cost per resolved ($) [calc]", fmts["row_header"])
    ws.write_formula(r, 1,
        f"=B{CPR_FREE_R}*B{PCT_FREE_R}+B{CPR_PRO_R}*B{PCT_PRO_R}+B{CPR_ENT_R}*B{PCT_ENT_R}",
        fmts["calc_usd2"])
    BLEND_CPR_R = r + 1
    r += 1
    # GM% calc
    ws.write(r, 0, "Agent GM% (actual) [calc]", fmts["row_header"])
    ws.write_formula(r, 1,
        f"=IF(B{TOT_ARPA_R}>0, (B{TOT_ARPA_R}-B{BLEND_CPR_R}*B{RES_M12_R}-B{BLENDED_ARPA_R}*B{OTH_COGS_R})/B{TOT_ARPA_R}, -1)",
        fmts["calc_bold_pct"])
    GM_ACT_R = r + 1
    r += 2

    # Section 3: Churn & expansion (with retention multipliers from autonomy)
    ws.merge_range(r, 0, r, 3, "3. Churn / Expansion / Autonomy-Retention Coupling", fmts["h2"]); r += 1
    ce_rows = [
        ("Monthly logo churn — baseline",         0.020, "input_pct",
            "Agent businesses tend toward lower churn due to deep integration."),
        ("Monthly revenue churn — baseline",      0.015, "input_pct", ""),
        ("Retention multiplier from better resolution (per +10pp)",
            0.85, "input",
            "If resolution rate rises +10pp, monthly churn × 0.85. Strong signal."),
        ("Monthly expansion (per-resolution growth)", 0.035, "input_pct",
            "Net growth in per-resolution volume by tenant per month (autonomy-progression-driven)."),
        ("Monthly contraction",                    0.005, "input_pct", ""),
        ("Involuntary churn (payment fail)",       0.005, "input_pct", ""),
        ("Tier-upgrade rate (Pro→Ent per month)",  0.010, "input_pct",
            "Autonomy-tier upgrade — drives expansion ARR."),
    ]
    sec3_start = r + 1
    for label, val, kind, note in ce_rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        ws.write(r, 3, note, fmts["note"])
        r += 1
    LOGO_CHURN_R = sec3_start
    REV_CHURN_R  = sec3_start + 1
    RET_MULT_R   = sec3_start + 2
    EXP_R        = sec3_start + 3
    CONTR_R      = sec3_start + 4
    INVOL_R      = sec3_start + 5
    UPGR_R       = sec3_start + 6
    r += 1

    # Section 4: CAC by channel (PLG vs sales-led)
    ws.merge_range(r, 0, r, 3, "4. CAC by Channel — PLG vs Sales-Led", fmts["h2"]); r += 1
    cac_rows = [
        ("PLG / self-serve CAC ($)",       250,  "input_usd"),
        ("Inbound / content CAC ($)",      800,  "input_usd"),
        ("Outbound / sales-led CAC ($)",   4500, "input_usd"),
        ("Partner / channel CAC ($)",      900,  "input_usd"),
        ("% logos via PLG",                0.30, "input_pct"),
        ("% logos via inbound",            0.30, "input_pct"),
        ("% logos via outbound",           0.30, "input_pct"),
        ("% logos via partner",            0.10, "input_pct"),
    ]
    sec4_start = r + 1
    for label, val, kind in cac_rows:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind])
        r += 1
    # Blended CAC
    ws.write(r, 0, "Blended agent CAC ($) [calc]", fmts["row_header"])
    ws.write_formula(r, 1,
        f"=B{sec4_start}*B{sec4_start+4}+B{sec4_start+1}*B{sec4_start+5}+B{sec4_start+2}*B{sec4_start+6}+B{sec4_start+3}*B{sec4_start+7}",
        fmts["calc_bold_usd"])
    BLEND_CAC_R = r + 1
    r += 1
    # Period inputs
    ws.write(r, 0, "New logos in quarter (count)", fmts["row_header"]); ws.write(r, 1, 40, fmts["input_int"]); NEW_LOG_R = r+1; r+=1
    ws.write(r, 0, "S&M spend in quarter ($)",  fmts["row_header"]); ws.write(r, 1, 200000, fmts["input_usd"]); SM_R = r+1; r+=1
    ws.write(r, 0, "Prior-quarter S&M spend ($)", fmts["row_header"]); ws.write(r, 1, 180000, fmts["input_usd"]); PR_SM_R = r+1; r+=1
    ws.write(r, 0, "Net new ARR added in quarter ($)", fmts["row_header"]); ws.write(r, 1, 320000, fmts["input_usd"]); NEW_ARR_R = r+1; r+=1
    ws.write(r, 0, "Net cash burn in quarter ($)", fmts["row_header"]); ws.write(r, 1, 220000, fmts["input_usd"]); BURN_R = r+1; r+=1
    ws.write(r, 0, "YoY revenue growth %", fmts["row_header"]); ws.write(r, 1, 1.50, fmts["input_pct"]); GROWTH_R = r+1; r+=1
    ws.write(r, 0, "FCF margin %", fmts["row_header"]); ws.write(r, 1, -0.30, fmts["input_pct"]); FCF_R = r+1; r+=1
    ws.write(r, 0, "Cash on hand ($)", fmts["row_header"]); ws.write(r, 1, 1500000, fmts["input_usd"]); CASH_R = r+1; r+=2

    # Section 5: HITL cost ramp (supervised → agentic)
    ws.merge_range(r, 0, r, 3, "5. Supervised-vs-Agentic HITL Ramp", fmts["h2"]); r += 1
    ws.write(r, 0, "Supervised-period HITL intervention rate (M0-M2)", fmts["row_header"])
    ws.write(r, 1, 0.40, fmts["input_pct"]); SUP_INT_R = r+1
    ws.write(r, 3, "First 3 months — heavy supervision; high cost per task.", fmts["note"]); r += 1
    ws.write(r, 0, "Agentic-period HITL intervention rate (M3-M24)", fmts["row_header"])
    ws.write(r, 1, 0.10, fmts["input_pct"]); AG_INT_R = r+1
    ws.write(r, 3, "Autonomy ramp brings intervention rate down materially.", fmts["note"]); r += 1
    ws.write(r, 0, "HITL minutes per intervention", fmts["row_header"])
    ws.write(r, 1, 5, fmts["input_int"]); HMIN_R = r+1; r += 1
    ws.write(r, 0, "HITL fully-loaded $/min", fmts["row_header"])
    ws.write(r, 1, 0.30, fmts["input_usd2"]); HRATE_R = r+1; r += 1
    ws.write(r, 0, "Resolution rate — supervised period", fmts["row_header"])
    ws.write(r, 1, 0.65, fmts["input_pct"]); RES_SUP_R = r+1; r += 1
    ws.write(r, 0, "Resolution rate — agentic period", fmts["row_header"])
    ws.write(r, 1, 0.85, fmts["input_pct"]); RES_AG_R = r+1; r += 2

    # Section 6: Targets & FX
    ws.merge_range(r, 0, r, 3, "6. Targets, Benchmarks & FX", fmts["h2"]); r += 1
    targets = [
        ("Agent LTV:CAC target (>=3 healthy)",         3.0,   "input"),
        ("Agent CAC payback target (months)",          18,    "input_int"),
        ("Rule of 40 target",                          0.30,  "input_pct"),
        ("Agent NRR target",                           1.20,  "input_pct"),
        ("Agent GM target",                            0.65,  "input_pct"),
        ("Wrapper-score min for non-discount (15/24)", 15,    "input_int"),
        ("FX rate UGX per USD",                        3800,  "input"),
    ]
    sec6_start = r + 1
    for label, val, kind in targets:
        ws.write(r, 0, label, fmts["row_header"])
        ws.write(r, 1, val, fmts[kind]); r += 1
    TGT_LTV_CAC_R = sec6_start
    TGT_PAY_R     = sec6_start + 1
    TGT_R40_R     = sec6_start + 2
    TGT_NRR_R     = sec6_start + 3
    TGT_GM_R      = sec6_start + 4
    WRAP_MIN_R    = sec6_start + 5
    FX_UGX_R      = sec6_start + 6

    # Named ranges
    add_named(wb, "AG_ARPA",      f"Inputs!$B${TOT_ARPA_R}")
    add_named(wb, "AG_SubARPA",   f"Inputs!$B${BLENDED_ARPA_R}")
    add_named(wb, "AG_ACV",       f"Inputs!$B${ACV_R}")
    add_named(wb, "AG_GM",        f"Inputs!$B${GM_ACT_R}")
    add_named(wb, "AG_LogoChurn", f"Inputs!$B${LOGO_CHURN_R}")
    add_named(wb, "AG_RevChurn",  f"Inputs!$B${REV_CHURN_R}")
    add_named(wb, "AG_Exp",       f"Inputs!$B${EXP_R}")
    add_named(wb, "AG_Contr",     f"Inputs!$B${CONTR_R}")
    add_named(wb, "AG_Invol",     f"Inputs!$B${INVOL_R}")
    add_named(wb, "AG_CAC",       f"Inputs!$B${BLEND_CAC_R}")
    add_named(wb, "AG_NewLogos",  f"Inputs!$B${NEW_LOG_R}")
    add_named(wb, "AG_SM",        f"Inputs!$B${SM_R}")
    add_named(wb, "AG_PriorSM",   f"Inputs!$B${PR_SM_R}")
    add_named(wb, "AG_NewARR",    f"Inputs!$B${NEW_ARR_R}")
    add_named(wb, "AG_Burn",      f"Inputs!$B${BURN_R}")
    add_named(wb, "AG_Growth",    f"Inputs!$B${GROWTH_R}")
    add_named(wb, "AG_FCF",       f"Inputs!$B${FCF_R}")
    add_named(wb, "AG_Cash",      f"Inputs!$B${CASH_R}")
    add_named(wb, "AG_SupInt",    f"Inputs!$B${SUP_INT_R}")
    add_named(wb, "AG_AgInt",     f"Inputs!$B${AG_INT_R}")
    add_named(wb, "AG_HMin",      f"Inputs!$B${HMIN_R}")
    add_named(wb, "AG_HRate",     f"Inputs!$B${HRATE_R}")
    add_named(wb, "AG_ResSup",    f"Inputs!$B${RES_SUP_R}")
    add_named(wb, "AG_ResAg",     f"Inputs!$B${RES_AG_R}")
    add_named(wb, "AG_Blend_CPR", f"Inputs!$B${BLEND_CPR_R}")
    add_named(wb, "AG_RetMult",   f"Inputs!$B${RET_MULT_R}")
    add_named(wb, "AG_Upgrade",   f"Inputs!$B${UPGR_R}")
    add_named(wb, "AG_FX_UGX",    f"Inputs!$B${FX_UGX_R}")
    add_named(wb, "Tgt_NRR",      f"Inputs!$B${TGT_NRR_R}")
    add_named(wb, "Tgt_R40",      f"Inputs!$B${TGT_R40_R}")
    add_named(wb, "Tgt_Pay",      f"Inputs!$B${TGT_PAY_R}")
    add_named(wb, "Tgt_LTV_CAC",  f"Inputs!$B${TGT_LTV_CAC_R}")
    add_named(wb, "Tgt_GM",       f"Inputs!$B${TGT_GM_R}")
    add_named(wb, "Wrap_Min",     f"Inputs!$B${WRAP_MIN_R}")
    add_named(wb, "AG_M0_Res",    f"Inputs!$B${RES_M0_R}")
    add_named(wb, "AG_M12_Res",   f"Inputs!$B${RES_M12_R}")
    add_named(wb, "AG_M24_Res",   f"Inputs!$B${RES_M24_R}")
    add_named(wb, "AG_PriceRes",  f"Inputs!$B${PRICE_RES_R}")

    # =============================================================
    # COHORT — 24-month with supervised → agentic
    # =============================================================
    wsh = wb.add_worksheet("Cohort")
    wsh.set_column("A:A", 24)
    wsh.set_column("B:Z", 9)
    wsh.set_row(0, 28)
    wsh.merge_range("A1:Z1", "Cohort — 24-Month Logo + Revenue + Resolution Per Tenant", fmts["title"])
    wsh.write("A2", "Supervised period M0-M2: intervention 40%, resolution 65%. Agentic period M3-M24: intervention 10%, resolution 85%, expansion compounds.", fmts["subtitle"])

    # Month axis row
    wsh.write(3, 0, "Month from acquisition", fmts["col_header"])
    for m in range(25):
        wsh.write(3, 1+m, f"M{m}", fmts["col_header"])

    # Block A — Logo retention
    wsh.write(5, 0, "Logo retention (%)", fmts["h2"])
    wsh.write(6, 0, "Single illustrative cohort", fmts["row_header"])
    for m in range(25):
        wsh.write_formula(6, 1+m, f"=(1-AG_LogoChurn)^{m}", fmts["calc_pct"])
    wsh.conditional_format("B7:Z7", {
        "type":"3_color_scale","min_color":"#F8696B","mid_color":"#FFEB84","max_color":"#63BE7B",
        "min_type":"num","min_value":0.4,"mid_type":"num","mid_value":0.7,"max_type":"num","max_value":1.0})

    # Block B — Revenue retention (NRR per cohort)
    wsh.write(8, 0, "Revenue retention (NRR, smile curve)", fmts["h2"])
    wsh.write(9, 0, "Single illustrative cohort", fmts["row_header"])
    for m in range(25):
        wsh.write_formula(9, 1+m,
            f"=(1+AG_Exp-AG_RevChurn-AG_Contr)^{m}", fmts["calc_pct"])
    wsh.conditional_format("B10:Z10", {
        "type":"3_color_scale","min_color":"#F8696B","mid_color":"#FFEB84","max_color":"#63BE7B",
        "min_type":"num","min_value":0.6,"mid_type":"num","mid_value":1.0,"max_type":"num","max_value":1.6})

    # Block C — Resolutions per tenant (autonomy progression)
    # M0-M2 use M0 input, M3-M11 interpolate to M12, M13-M23 interpolate to M24
    wsh.write(11, 0, "Resolutions per tenant / month", fmts["h2"])
    wsh.write(12, 0, "Autonomy-driven volume", fmts["row_header"])
    for m in range(25):
        if m <= 2:
            f = "=AG_M0_Res"
        elif m <= 12:
            f = f"=AG_M0_Res+(AG_M12_Res-AG_M0_Res)*({m}-2)/10"
        else:
            f = f"=AG_M12_Res+(AG_M24_Res-AG_M12_Res)*({m}-12)/12"
        wsh.write_formula(12, 1+m, f, fmts["calc_int"])
    wsh.conditional_format("B13:Z13", {
        "type":"3_color_scale","min_color":"#FFFFFF","mid_color":"#FFEB84","max_color":"#1F3864"})

    # Block D — HITL intervention rate by month (supervised → agentic)
    wsh.write(14, 0, "HITL intervention rate %", fmts["h2"])
    wsh.write(15, 0, "Supervised → agentic ramp", fmts["row_header"])
    for m in range(25):
        if m <= 2:
            f = "=AG_SupInt"
        else:
            # linear ramp from sup to ag over next 6 months, then flat
            f = f"=MAX(AG_AgInt, AG_SupInt-(AG_SupInt-AG_AgInt)*MIN(1,({m}-2)/6))"
        wsh.write_formula(15, 1+m, f, fmts["calc_pct"])
    wsh.conditional_format("B16:Z16", {
        "type":"3_color_scale","min_color":"#63BE7B","mid_color":"#FFEB84","max_color":"#F8696B",
        "min_type":"num","min_value":0.05,"mid_type":"num","mid_value":0.20,"max_type":"num","max_value":0.50})

    # Block E — Revenue per tenant per month (subscription + per-resolution)
    wsh.write(17, 0, "Revenue per tenant / month ($)", fmts["h2"])
    wsh.write(18, 0, "Sub + per-resolution", fmts["row_header"])
    for m in range(25):
        # subscription with NRR compounding × monthly resolutions × price-per-resolved
        # use revenue retention block row 10 → cohort revenue retention
        f = f"=AG_SubARPA*(1+AG_Exp-AG_RevChurn-AG_Contr)^{m}+INDEX($B$13:$Z$13,1,{m+1})*AG_PriceRes"
        wsh.write_formula(18, 1+m, f, fmts["calc_usd2"])

    # Block F — Cost per tenant per month
    wsh.write(20, 0, "Cost per tenant / month ($)", fmts["h2"])
    wsh.write(21, 0, "Cost-per-resolved × resolutions/month", fmts["row_header"])
    for m in range(25):
        f = f"=AG_Blend_CPR*INDEX($B$13:$Z$13,1,{m+1})"
        wsh.write_formula(21, 1+m, f, fmts["calc_usd2"])

    # Block G — GM per tenant per month
    wsh.write(23, 0, "GM per tenant / month ($)", fmts["h2"])
    wsh.write(24, 0, "Rev − cost", fmts["row_header"])
    for m in range(25):
        f = f"=INDEX($B$19:$Z$19,1,{m+1})-INDEX($B$22:$Z$22,1,{m+1})"
        wsh.write_formula(24, 1+m, f, fmts["calc_usd2"])
    wsh.conditional_format("B25:Z25", {
        "type":"3_color_scale","min_color":"#F8696B","mid_color":"#FFEB84","max_color":"#63BE7B"})

    # =============================================================
    # UNIT-ECONOMICS
    # =============================================================
    wsu = wb.add_worksheet("Unit-Economics")
    wsu.set_column("A:A", 46); wsu.set_column("B:B", 18); wsu.set_column("C:C", 14)
    wsu.set_column("D:D", 22); wsu.set_column("E:E", 60); wsu.set_row(0, 28)
    wsu.merge_range("A1:E1", "Agent Unit Economics — Five LTV Methods + Full Metric Stack", fmts["title"])
    wsu.write("A2", "All formulas reference named ranges on Inputs.", fmts["subtitle"])
    wsu.write("A3", "Metric", fmts["col_header"])
    wsu.write("B3", "Value", fmts["col_header"])
    wsu.write("C3", "Unit", fmts["col_header"])
    wsu.write("D3", "Target", fmts["col_header"])
    wsu.write("E3", "Method / interpretation", fmts["col_header"])

    metrics = [
        ("Agent LTV — simple",
            "=AG_ARPA/AG_LogoChurn",
            "$","n/a","ARPA / monthly logo churn"),
        ("Agent LTV — with churn (revenue)",
            "=AG_ARPA/AG_RevChurn",
            "$","n/a","ARPA / monthly revenue churn"),
        ("Agent LTV — with expansion (NRR)",
            "=IF(AG_RevChurn+AG_Contr-AG_Exp>0,AG_ARPA/(AG_RevChurn+AG_Contr-AG_Exp),AG_ARPA*60)",
            "$","cap at 60mo","NRR>100% → cap horizon"),
        ("Agent LTV — GM-adjusted",
            "=AG_ARPA*AG_GM/AG_LogoChurn",
            "$","n/a","ARPA × GM% / churn (Skok/Mersch standard)"),
        ("Agent LTV — with HITL-cost ramp (agentic period)",
            "=AG_ARPA*AG_GM/AG_LogoChurn*((1-AG_AgInt)/(1-AG_SupInt)+0.5)",
            "$","headline","Adjusts GM by autonomy ramp: agentic intervention vs supervised baseline"),
        ("Agent CAC",
            "=AG_CAC",
            "$","n/a","Σ channel CAC × channel mix"),
        ("Agent CAC payback (months)",
            "=AG_CAC/(AG_ARPA*AG_GM)",
            "months","<=Tgt_Pay","CAC / (ARPA × GM%)"),
        ("Agent LTV:CAC",
            "=(AG_ARPA*AG_GM/AG_LogoChurn)/AG_CAC",
            "ratio",">=3","GM-adjusted LTV / CAC"),
        ("Agent NRR (annual)",
            "=1+(AG_Exp-AG_RevChurn-AG_Contr)*12",
            "%",">=Tgt_NRR","1 + 12×(exp − rev_churn − contraction)"),
        ("Agent GRR (annual)",
            "=MAX(0,1-AG_RevChurn*12)",
            "%",">=85%","1 − annualised revenue churn"),
        ("Agent Magic Number",
            "=AG_NewARR*4/AG_PriorSM",
            "ratio",">=1 invest","Net New ARR × 4 / prior-quarter S&M"),
        ("Rule of 40 (growth + FCF margin)",
            "=AG_Growth+AG_FCF",
            "%",">=Tgt_R40","YoY growth + FCF margin"),
        ("Burn Multiple",
            "=IF(AG_NewARR>0,AG_Burn/AG_NewARR,999)",
            "ratio","<2 healthy","Net burn / Net new ARR"),
        ("Quick Ratio",
            "=((AG_NewARR/3)+AG_Exp*AG_ARPA*AG_NewLogos)/((AG_RevChurn+AG_Contr)*AG_ARPA*AG_NewLogos+0.0001)",
            "ratio",">=2","(new MRR + expansion) / (churn + contraction)"),
        ("Runway (months at current burn)",
            "=IF(AG_Burn/3>0,AG_Cash/(AG_Burn/3),999)",
            "months",">=18","Cash / (quarterly burn / 3)"),
        ("Cost-per-resolved-task trend M0 → M12",
            "=AG_Blend_CPR-AG_Blend_CPR*((1-AG_AgInt)/(1-AG_SupInt))",
            "$","declining","Should decline as autonomy increases and HITL share falls"),
        ("HITL ratio trend M0 → M12 (Δ)",
            "=AG_SupInt-AG_AgInt",
            "%","positive","Supervised − Agentic; bigger = better trajectory"),
        ("Subscription % of total ARR",
            "=AG_SubARPA/AG_ARPA",
            "%","n/a","Higher = closer to classic SaaS"),
        ("Per-resolution % of total ARR",
            "=1-AG_SubARPA/AG_ARPA",
            "%","n/a","Mix tilt toward outcome-based pricing"),
    ]
    r = 3
    for label, formula, unit, target, descr in metrics:
        wsu.write(r, 0, label, fmts["row_header"])
        if unit == "%":
            wsu.write_formula(r, 1, formula, fmts["calc_pct"])
        elif unit == "$":
            wsu.write_formula(r, 1, formula, fmts["calc_usd"])
        elif unit == "months":
            wsu.write_formula(r, 1, formula, fmts["calc"])
        else:
            wsu.write_formula(r, 1, formula, fmts["calc"])
        wsu.write(r, 2, unit, fmts["calc"])
        wsu.write(r, 3, target, fmts["calc"])
        wsu.write(r, 4, descr, fmts["note"])
        r += 1

    # Conditional formats on LTV:CAC (row 12, 1-idx), Payback (row 11), Rule of 40 (row 15), Burn Multiple (row 16)
    # 0-idx for metrics: 0=simple, 1=with_churn_rev, 2=with_exp, 3=gm_adj, 4=hitl_ramp,
    # 5=CAC, 6=Payback, 7=LTV:CAC, 8=NRR, 9=GRR, 10=Magic, 11=Rule40, 12=Burn, 13=Quick, 14=Runway
    # Spreadsheet rows: header at 4, metric 0 at row 4 (0-idx 3) → ss row 4. Metric i at ss row 4+i.
    LTV_CAC_SS = 4 + 7   # ss row 11
    PAY_SS     = 4 + 6   # ss row 10
    NRR_SS     = 4 + 8   # ss row 12
    R40_SS     = 4 + 11  # ss row 15
    BURN_SS    = 4 + 12  # ss row 16
    RUN_SS     = 4 + 14  # ss row 18
    wsu.conditional_format(f"B{LTV_CAC_SS}", {"type":"cell","criteria":">=","value":3,"format":fmts["good"]})
    wsu.conditional_format(f"B{LTV_CAC_SS}", {"type":"cell","criteria":"between","minimum":1.5,"maximum":3,"format":fmts["warn"]})
    wsu.conditional_format(f"B{LTV_CAC_SS}", {"type":"cell","criteria":"<","value":1.5,"format":fmts["bad"]})
    wsu.conditional_format(f"B{PAY_SS}", {"type":"cell","criteria":"<=","value":18,"format":fmts["good"]})
    wsu.conditional_format(f"B{PAY_SS}", {"type":"cell","criteria":"between","minimum":18,"maximum":30,"format":fmts["warn"]})
    wsu.conditional_format(f"B{PAY_SS}", {"type":"cell","criteria":">","value":30,"format":fmts["bad"]})
    wsu.conditional_format(f"B{NRR_SS}", {"type":"cell","criteria":">=","value":1.20,"format":fmts["good"]})
    wsu.conditional_format(f"B{NRR_SS}", {"type":"cell","criteria":"between","minimum":1.0,"maximum":1.20,"format":fmts["warn"]})
    wsu.conditional_format(f"B{NRR_SS}", {"type":"cell","criteria":"<","value":1.0,"format":fmts["bad"]})
    wsu.conditional_format(f"B{R40_SS}", {"type":"cell","criteria":">=","value":0.40,"format":fmts["good"]})
    wsu.conditional_format(f"B{R40_SS}", {"type":"cell","criteria":"between","minimum":0.30,"maximum":0.40,"format":fmts["warn"]})
    wsu.conditional_format(f"B{R40_SS}", {"type":"cell","criteria":"<","value":0.30,"format":fmts["bad"]})
    wsu.conditional_format(f"B{BURN_SS}", {"type":"cell","criteria":"<=","value":1.0,"format":fmts["good"]})
    wsu.conditional_format(f"B{BURN_SS}", {"type":"cell","criteria":"between","minimum":1.0,"maximum":2.0,"format":fmts["warn"]})
    wsu.conditional_format(f"B{BURN_SS}", {"type":"cell","criteria":">","value":2.0,"format":fmts["bad"]})
    wsu.conditional_format(f"B{RUN_SS}", {"type":"cell","criteria":">=","value":18,"format":fmts["good"]})
    wsu.conditional_format(f"B{RUN_SS}", {"type":"cell","criteria":"between","minimum":9,"maximum":18,"format":fmts["warn"]})
    wsu.conditional_format(f"B{RUN_SS}", {"type":"cell","criteria":"<","value":9,"format":fmts["bad"]})

    # =============================================================
    # WRAPPER-VS-MOAT-SCORING (8-Q rubric)
    # =============================================================
    wsw = wb.add_worksheet("Wrapper-vs-Moat-Scoring")
    wsw.set_column("A:A", 6); wsw.set_column("B:B", 30); wsw.set_column("C:C", 12)
    wsw.set_column("D:D", 70); wsw.set_row(0, 28)
    wsw.merge_range("A1:D1", "Wrapper-vs-Moat Scorecard — 8 Questions × (0-3)", fmts["title"])
    wsw.write("A2", "Score 0=absent / 1=early / 2=real-improvable / 3=strong-compounding. Total / 24 drives valuation modifier.", fmts["subtitle"])
    wsw.write(3, 0, "#",       fmts["col_header"])
    wsw.write(3, 1, "Question", fmts["col_header"])
    wsw.write(3, 2, "Score",   fmts["col_header"])
    wsw.write(3, 3, "Anchor (3 = strong compounding moat)", fmts["col_header"])

    qs = [
        ("Q1", "Proprietary tools",  2,
            "Multiple proprietary tools; quarters/years to build; embodies regulatory/vertical knowledge."),
        ("Q2", "Proprietary action data flywheel", 2,
            "Action data accrues per customer/interaction; flywheel improves YOUR agent; data exclusive."),
        ("Q3", "Integration depth",  2,
            "Deep integration across multiple systems-of-record with audit + identity + billing."),
        ("Q4", "Eval-loop (proprietary)", 2,
            "Proprietary eval suite on customer data; demonstrable improvement; eval is itself a moat."),
        ("Q5", "Customer trust / brand", 2,
            "Marquee/lighthouse references; public-sector / regulator references."),
        ("Q6", "Regulatory clearance", 1,
            "Multiple regulator engagements; accepted audit log; sectoral approval."),
        ("Q7", "Switching cost",     2,
            "Years of accrued data, deep integration, regulator-attached audit, vertical config."),
        ("Q8", "Distribution",       1,
            "Embedded in larger platform; dominant distribution; competitors must build from scratch."),
    ]
    for i, (qid, q, default, anchor) in enumerate(qs):
        wsw.write(4+i, 0, qid, fmts["row_header"])
        wsw.write(4+i, 1, q,   fmts["row_header"])
        wsw.write(4+i, 2, default, fmts["input_int"])
        wsw.write(4+i, 3, anchor, fmts["note"])
    SCORE_START = 5  # ss rows 5..12
    SCORE_END   = 12
    wsw.conditional_format(f"C{SCORE_START}:C{SCORE_END}", {"type":"cell","criteria":"=","value":3,"format":fmts["good"]})
    wsw.conditional_format(f"C{SCORE_START}:C{SCORE_END}", {"type":"cell","criteria":"=","value":2,"format":fmts["warn"]})
    wsw.conditional_format(f"C{SCORE_START}:C{SCORE_END}", {"type":"cell","criteria":"<=","value":1,"format":fmts["bad"]})

    # Total + category + valuation modifier
    wsw.write(13, 1, "TOTAL / 24", fmts["row_header"])
    wsw.write_formula(13, 2, f"=SUM(C{SCORE_START}:C{SCORE_END})", fmts["calc_bold"])
    TOTAL_SS = 14
    wsw.write(14, 1, "Category", fmts["row_header"])
    wsw.write_formula(14, 2,
        f"=IF(C{TOTAL_SS}<=8,\"Wrapper\",IF(C{TOTAL_SS}<=14,\"Incomplete\",IF(C{TOTAL_SS}<=19,\"Strong moat\",\"Rare strong\")))",
        fmts["calc_bold"])
    wsw.write(15, 1, "Valuation multiplier modifier", fmts["row_header"])
    wsw.write_formula(15, 2,
        f"=IF(C{TOTAL_SS}<=8,0.6,IF(C{TOTAL_SS}<=14,0.85,IF(C{TOTAL_SS}<=19,1.10,1.35)))",
        fmts["calc_bold_pct"])
    wsw.write(15, 3,
        "Applied to baseline revenue multiple in valuation model. Wrapper = 0.6x; "
        "Incomplete = 0.85x; Strong = 1.10x; Rare = 1.35x.",
        fmts["note"])
    VAL_MOD_SS = 16

    # Named range for valuation modifier (used by Dashboard / external)
    add_named(wb, "Wrap_Score", f"'Wrapper-vs-Moat-Scoring'!$C${TOTAL_SS}")
    add_named(wb, "Wrap_Modifier", f"'Wrapper-vs-Moat-Scoring'!$C${VAL_MOD_SS}")

    # =============================================================
    # AI-vs-AGENT COMPARISON
    # =============================================================
    wsa_c = wb.add_worksheet("AI-vs-Agent-Comparison")
    wsa_c.set_column("A:A", 42); wsa_c.set_column("B:D", 16); wsa_c.set_column("E:E", 50)
    wsa_c.set_row(0, 28)
    wsa_c.merge_range("A1:E1", "AI-vs-Agent Comparison — Same Tenant Base, Three Models", fmts["title"])
    wsa_c.write("A2", "Yellow cells are illustrative baselines. Agent column references this workbook live.", fmts["subtitle"])
    wsa_c.write(2, 0, "Line", fmts["col_header"])
    wsa_c.write(2, 1, "Classic SaaS", fmts["col_header"])
    wsa_c.write(2, 2, "AI overlay", fmts["col_header"])
    wsa_c.write(2, 3, "Agent", fmts["col_header"])
    wsa_c.write(2, 4, "Why it's different", fmts["col_header"])

    comp_rows = [
        ("ARPA $/mo",            [79, 99, "=AG_ARPA"], ["input_usd2","input_usd2","calc_usd2"],
            "Agent: subscription + per-resolution can multiply ARPA 5-10x for power tenants."),
        ("Gross margin %",       [0.80, 0.70, "=AG_GM"], ["input_pct","input_pct","calc_pct"],
            "Agent GM is compressed by tokens + HITL; well-tuned 65-75%."),
        ("Monthly logo churn %", [0.020, 0.025, "=AG_LogoChurn"], ["input_pct","input_pct","calc_pct"],
            "Agent churn lower due to integration depth + switching cost."),
        ("Monthly expansion %",  [0.010, 0.012, "=AG_Exp"], ["input_pct","input_pct","calc_pct"],
            "Agent expansion mechanic is per-resolution growth × autonomy progression."),
        ("CAC $",                [1200, 1500, "=AG_CAC"], ["input_usd","input_usd","calc_usd"],
            "Agent CAC higher (longer sales cycle, more proof needed)."),
        ("LTV (GM-adjusted) $",
            ["=B4*B5/B6", "=C4*C5/C6", "=AG_ARPA*AG_GM/AG_LogoChurn"],
            ["calc_usd","calc_usd","calc_usd"],
            "Three-way LTV comparison on identical formula."),
        ("LTV:CAC",
            ["=B9/B8", "=C9/C8", "=(AG_ARPA*AG_GM/AG_LogoChurn)/AG_CAC"],
            ["calc","calc","calc"],
            "Headline efficiency — agent should beat SaaS if moat real."),
        ("CAC payback (months)",
            ["=B8/(B4*B5)", "=C8/(C4*C5)", "=AG_CAC/(AG_ARPA*AG_GM)"],
            ["calc","calc","calc"],
            "Higher payback acceptable if LTV:CAC strong."),
        ("Cost-per-customer-action ($)",
            [0.001, 0.05, "=AG_Blend_CPR"],
            ["input_usd2","input_usd2","calc_usd2"],
            "Classic SaaS: storage/compute. AI: per-prompt. Agent: per-resolved-task — the headline."),
        ("HITL or human-overhead share %",
            [0.05, 0.10, "=AG_AgInt"],
            ["input_pct","input_pct","calc_pct"],
            "Agent surfaces HITL as explicit cost line; SaaS hides it in CS overhead."),
        ("Defensibility moat type",
            ["Network effects / data", "Embedded AI features", "Action-data + integration + regulatory"],
            ["input_text","input_text","input_text"],
            "Agent moat must include action-data flywheel + integration depth, not just AI features."),
    ]
    for i, (label, vals, kinds, why) in enumerate(comp_rows):
        rr = 3 + i
        wsa_c.write(rr, 0, label, fmts["row_header"])
        for t in range(3):
            v, k = vals[t], kinds[t]
            if isinstance(v, str) and v.startswith("="):
                wsa_c.write_formula(rr, 1+t, v, fmts[k])
            else:
                wsa_c.write(rr, 1+t, v, fmts[k])
        wsa_c.write(rr, 4, why, fmts["note"])

    # =============================================================
    # DASHBOARD
    # =============================================================
    wsd = wb.add_worksheet("Dashboard")
    wsd.set_column("A:A", 42); wsd.set_column("B:B", 18); wsd.set_column("C:G", 14)
    wsd.set_row(0, 30)
    wsd.merge_range("A1:G1", "Dashboard — Agent Unit Economics", fmts["title"])

    kpis = [
        ("Agent LTV:CAC",                "=(AG_ARPA*AG_GM/AG_LogoChurn)/AG_CAC", "ratio"),
        ("Agent CAC payback (months)",   "=AG_CAC/(AG_ARPA*AG_GM)",              "ratio"),
        ("Agent GM %",                    "=AG_GM",                              "pct"),
        ("Agent NRR (annual)",            "=1+(AG_Exp-AG_RevChurn-AG_Contr)*12", "pct"),
        ("Agent GRR (annual)",            "=MAX(0,1-AG_RevChurn*12)",            "pct"),
        ("Rule of 40",                    "=AG_Growth+AG_FCF",                   "pct"),
        ("Magic Number",                  "=AG_NewARR*4/AG_PriorSM",             "ratio"),
        ("Burn Multiple",                 "=IF(AG_NewARR>0,AG_Burn/AG_NewARR,999)", "ratio"),
        ("Runway (months)",               "=IF(AG_Burn/3>0,AG_Cash/(AG_Burn/3),999)", "ratio"),
        ("Wrapper-Moat Score / 24",       "=Wrap_Score",                         "ratio"),
        ("Valuation modifier (×)",        "=Wrap_Modifier",                      "pct"),
        ("HITL ratio trend (Δ supervised→agentic)", "=AG_SupInt-AG_AgInt",       "pct"),
        ("Cost per resolved (blended)",   "=AG_Blend_CPR",                       "usd"),
        ("Agent ACV ($)",                 "=AG_ACV",                             "usd"),
        ("Annual revenue UGX (per tenant proxy)", "=AG_ARPA*12*AG_FX_UGX",       "ratio"),
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

    # Traffic lights on key KPIs (rows 4=LTV:CAC, 5=Payback, 6=GM, 7=NRR, 9=R40, 11=Burn, 12=Runway)
    wsd.conditional_format("B4", {"type":"cell","criteria":">=","value":3,"format":fmts["good"]})
    wsd.conditional_format("B4", {"type":"cell","criteria":"between","minimum":1.5,"maximum":3,"format":fmts["warn"]})
    wsd.conditional_format("B4", {"type":"cell","criteria":"<","value":1.5,"format":fmts["bad"]})
    wsd.conditional_format("B5", {"type":"cell","criteria":"<=","value":18,"format":fmts["good"]})
    wsd.conditional_format("B5", {"type":"cell","criteria":"between","minimum":18,"maximum":30,"format":fmts["warn"]})
    wsd.conditional_format("B5", {"type":"cell","criteria":">","value":30,"format":fmts["bad"]})
    wsd.conditional_format("B6", {"type":"cell","criteria":">=","value":0.70,"format":fmts["good"]})
    wsd.conditional_format("B6", {"type":"cell","criteria":"between","minimum":0.50,"maximum":0.70,"format":fmts["warn"]})
    wsd.conditional_format("B6", {"type":"cell","criteria":"<","value":0.50,"format":fmts["bad"]})
    wsd.conditional_format("B7", {"type":"cell","criteria":">=","value":1.20,"format":fmts["good"]})
    wsd.conditional_format("B7", {"type":"cell","criteria":"between","minimum":1.0,"maximum":1.20,"format":fmts["warn"]})
    wsd.conditional_format("B7", {"type":"cell","criteria":"<","value":1.0,"format":fmts["bad"]})
    wsd.conditional_format("B9", {"type":"cell","criteria":">=","value":0.40,"format":fmts["good"]})
    wsd.conditional_format("B9", {"type":"cell","criteria":"between","minimum":0.30,"maximum":0.40,"format":fmts["warn"]})
    wsd.conditional_format("B9", {"type":"cell","criteria":"<","value":0.30,"format":fmts["bad"]})
    wsd.conditional_format("B11", {"type":"cell","criteria":"<=","value":1.0,"format":fmts["good"]})
    wsd.conditional_format("B11", {"type":"cell","criteria":"between","minimum":1.0,"maximum":2.0,"format":fmts["warn"]})
    wsd.conditional_format("B11", {"type":"cell","criteria":">","value":2.0,"format":fmts["bad"]})
    wsd.conditional_format("B12", {"type":"cell","criteria":">=","value":18,"format":fmts["good"]})
    wsd.conditional_format("B12", {"type":"cell","criteria":"between","minimum":9,"maximum":18,"format":fmts["warn"]})
    wsd.conditional_format("B12", {"type":"cell","criteria":"<","value":9,"format":fmts["bad"]})
    # Wrapper score
    wsd.conditional_format("B13", {"type":"cell","criteria":">=","value":15,"format":fmts["good"]})
    wsd.conditional_format("B13", {"type":"cell","criteria":"between","minimum":9,"maximum":14,"format":fmts["warn"]})
    wsd.conditional_format("B13", {"type":"cell","criteria":"<=","value":8,"format":fmts["bad"]})

    # Charts: cohort retention, cost-per-resolved trend (computed from cohort), agent revenue mix
    ch1 = wb.add_chart({"type":"line"})
    ch1.add_series({
        "name": "Logo retention",
        "categories": "='Cohort'!$B$4:$Z$4",
        "values":     "='Cohort'!$B$7:$Z$7",
        "line": {"color":"#1F3864","width":2.5},
    })
    ch1.add_series({
        "name": "Revenue retention",
        "categories": "='Cohort'!$B$4:$Z$4",
        "values":     "='Cohort'!$B$10:$Z$10",
        "line": {"color":"#C65911","width":2.5},
    })
    ch1.set_title({"name":"Cohort Retention — Logo vs Revenue"})
    ch1.set_y_axis({"name":"% retained","num_format":"0%"})
    ch1.set_legend({"position":"bottom"})
    wsd.insert_chart("D3", ch1, {"x_scale":1.4,"y_scale":1.0})

    ch2 = wb.add_chart({"type":"line"})
    ch2.add_series({
        "name": "HITL intervention rate",
        "categories": "='Cohort'!$B$4:$Z$4",
        "values":     "='Cohort'!$B$16:$Z$16",
        "line": {"color":"#2E75B6","width":2.5},
    })
    ch2.set_title({"name":"HITL Intervention Trend — Supervised→Agentic"})
    ch2.set_y_axis({"name":"%","num_format":"0%"})
    ch2.set_legend({"none":True})
    wsd.insert_chart("D22", ch2, {"x_scale":1.4,"y_scale":1.0})

    ch3 = wb.add_chart({"type":"column"})
    ch3.add_series({
        "name":"GM per tenant per month",
        "categories": "='Cohort'!$B$4:$Z$4",
        "values":     "='Cohort'!$B$25:$Z$25",
        "fill":{"color":"#7CB342"},
    })
    ch3.set_title({"name":"GM per Tenant — 24-Month Trajectory"})
    ch3.set_y_axis({"name":"USD"})
    ch3.set_legend({"none":True})
    wsd.insert_chart("D41", ch3, {"x_scale":1.4,"y_scale":1.0})

    # =============================================================
    # STRESS-TEST — applied to unit economics
    # =============================================================
    wss = wb.add_worksheet("Stress-Test")
    wss.set_column("A:A", 44); wss.set_column("B:G", 16); wss.set_row(0, 28)
    wss.merge_range("A1:G1", "Stress-Test — Full Unit Economics Impact", fmts["title"])
    wss.write(2, 0, "Scenario",         fmts["col_header"])
    wss.write(2, 1, "Cost/resolved $",  fmts["col_header"])
    wss.write(2, 2, "Agent GM %",       fmts["col_header"])
    wss.write(2, 3, "LTV:CAC",          fmts["col_header"])
    wss.write(2, 4, "Rule of 40",       fmts["col_header"])
    wss.write(2, 5, "Runway (months)",  fmts["col_header"])
    wss.write(2, 6, "Mitigation / time-to-mitigate", fmts["col_header"])

    def gm_under_shock(cpr_mult=1.0, exp_mult=1.0, churn_mult=1.0, burn_mult=1.0):
        # GM = (ARPA - cpr_blend*resolutions - other_cogs%*subARPA) / ARPA
        # We approximate ARPA fixed; cost-per-resolved scaled
        return (
            f"=(AG_ARPA-AG_Blend_CPR*{cpr_mult}*AG_M12_Res-AG_SubARPA*{1.0})/AG_ARPA"
        )

    def ltv_cac_shock(cpr_mult=1.0, churn_mult=1.0):
        # GM-adj LTV / CAC = (ARPA*GM_under_shock)/(churn*churn_mult) / CAC
        return (
            f"=(AG_ARPA*((AG_ARPA-AG_Blend_CPR*{cpr_mult}*AG_M12_Res-AG_SubARPA*0.15)/AG_ARPA)"
            f"/(AG_LogoChurn*{churn_mult}))/AG_CAC"
        )

    def runway_shock(burn_mult=1.0):
        return f"=IF(AG_Burn*{burn_mult}/3>0,AG_Cash/(AG_Burn*{burn_mult}/3),999)"

    def r40_shock(growth_delta=0, fcf_delta=0):
        return f"=(AG_Growth+{growth_delta})+(AG_FCF+{fcf_delta})"

    scenarios = [
        ("Baseline",
            "=AG_Blend_CPR",                                  gm_under_shock(),                  ltv_cac_shock(),         r40_shock(),                runway_shock(),
            "Reference."),
        ("Provider 5× price hike",
            "=AG_Blend_CPR*3.5",                              gm_under_shock(cpr_mult=3.5),      ltv_cac_shock(cpr_mult=3.5), r40_shock(fcf_delta=-0.20), runway_shock(burn_mult=1.5),
            "Reprice + provider switch + router downshift. 2-4 weeks."),
        ("Intervention rate doubles",
            "=AG_Blend_CPR*1.4",                              gm_under_shock(cpr_mult=1.4),      ltv_cac_shock(cpr_mult=1.4), r40_shock(fcf_delta=-0.10), runway_shock(burn_mult=1.2),
            "Retrain triage; tighten thresholds; eval round. 4-8 weeks."),
        ("Foundation model deprecation (2× cost)",
            "=AG_Blend_CPR*1.8",                              gm_under_shock(cpr_mult=1.8),      ltv_cac_shock(cpr_mult=1.8), r40_shock(fcf_delta=-0.12), runway_shock(burn_mult=1.3),
            "Reserve drawdown; planned migration; bench OSS. 6-12 weeks."),
        ("Tool-vendor outage (3× tool cost during outage)",
            "=AG_Blend_CPR*1.5",                              gm_under_shock(cpr_mult=1.5),      ltv_cac_shock(cpr_mult=1.5), r40_shock(fcf_delta=-0.05), runway_shock(burn_mult=1.1),
            "Multi-vendor failover; SLA credits. 1-3 weeks."),
        ("Abandonment 50%→25% (POSITIVE)",
            "=AG_Blend_CPR*0.7",                              gm_under_shock(cpr_mult=0.7),      ltv_cac_shock(cpr_mult=0.7,churn_mult=0.85), r40_shock(growth_delta=0.10), runway_shock(burn_mult=0.85),
            "Upside case — better triage + eval. 8-12 weeks."),
        ("Combined: provider 2× + interv 2× + aband +10pp",
            "=AG_Blend_CPR*3.0",                              gm_under_shock(cpr_mult=3.0),      ltv_cac_shock(cpr_mult=3.0,churn_mult=1.20), r40_shock(fcf_delta=-0.25), runway_shock(burn_mult=1.8),
            "Multi-front: reprice + retrain + provider switch + reserves. 8-16 weeks."),
    ]
    for i, (name, cpr, gm, lc, r40, run, mit) in enumerate(scenarios):
        rr = 3 + i
        wss.write(rr, 0, name, fmts["row_header"])
        wss.write_formula(rr, 1, cpr, fmts["calc_usd2"])
        wss.write_formula(rr, 2, gm,  fmts["calc_pct"])
        wss.write_formula(rr, 3, lc,  fmts["calc"])
        wss.write_formula(rr, 4, r40, fmts["calc_pct"])
        wss.write_formula(rr, 5, run, fmts["calc"])
        wss.write(rr, 6, mit, fmts["note"])
    wss.conditional_format(f"C4:C{3+len(scenarios)}", {"type":"cell","criteria":">=","value":0.65,"format":fmts["good"]})
    wss.conditional_format(f"C4:C{3+len(scenarios)}", {"type":"cell","criteria":"between","minimum":0.40,"maximum":0.65,"format":fmts["warn"]})
    wss.conditional_format(f"C4:C{3+len(scenarios)}", {"type":"cell","criteria":"<","value":0.40,"format":fmts["bad"]})
    wss.conditional_format(f"D4:D{3+len(scenarios)}", {"type":"cell","criteria":">=","value":3,"format":fmts["good"]})
    wss.conditional_format(f"D4:D{3+len(scenarios)}", {"type":"cell","criteria":"between","minimum":1.5,"maximum":3,"format":fmts["warn"]})
    wss.conditional_format(f"D4:D{3+len(scenarios)}", {"type":"cell","criteria":"<","value":1.5,"format":fmts["bad"]})
    wss.conditional_format(f"F4:F{3+len(scenarios)}", {"type":"cell","criteria":">=","value":18,"format":fmts["good"]})
    wss.conditional_format(f"F4:F{3+len(scenarios)}", {"type":"cell","criteria":"between","minimum":9,"maximum":18,"format":fmts["warn"]})
    wss.conditional_format(f"F4:F{3+len(scenarios)}", {"type":"cell","criteria":"<","value":9,"format":fmts["bad"]})

    # =============================================================
    # AFRICA-NOTES
    # =============================================================
    wsaf = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsaf, fmts, extra_notes=[
        ("Agent NRR Lever — Autonomy Progression in Local Context",
         "Per-resolution growth (M0→M24 in Cohort sheet) is the headline NRR mechanic. "
         "In African verticals, autonomy progression is gated by: (a) regulator audit-log acceptance, "
         "(b) customer trust in agent decisions over a 3-6 month proving period, "
         "(c) integration depth with local cores (M-Pesa, MoMo, KCB/Equity/Stanbic core banking)."),
        ("USD Per-Resolution Pricing for Enterprise",
         "Enterprise per-resolution pricing in USD-equivalent (invoiced via local entity or offshore SPV) "
         "is the single most effective FX hedge. 60-80% of agent ARR should sit in USD by Year 3."),
        ("HITL Cost Floor Asymmetry",
         "Loaded HITL cost in Uganda/Kenya/Nigeria/Rwanda is USD 0.07-0.13/min vs USD 0.50-1.00 in US. "
         "Agents in Africa beat a much lower human cost floor — but HITL fallback is also cheaper to run. "
         "Model both directions; the cost calculator's HITL $/min cell drives this."),
        ("Sovereign-AI Procurement",
         "KE Talanta / RW innovation / NG NITDA / ZA Presidential 4IR / EG infra programmes may "
         "require local hosting that raises per-task cost 30-80%. Reflect in cost-per-resolved input."),
        ("Agent Wrapper Score in African Markets",
         "Wrapper score Q5/Q6 (Trust, Regulatory) score relatively HIGHER for African agents — "
         "regulator engagement (KE ODPC, UG NITA-U, NG NDPC, ZA Info Reg) provides genuine "
         "competitive moat. Score honestly: regulator-engagement-without-acceptance = 1, "
         "regulator-acceptance = 2-3."),
    ])

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
