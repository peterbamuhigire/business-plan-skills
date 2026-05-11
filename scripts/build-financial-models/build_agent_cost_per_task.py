"""Build saas-agent-cost-per-task-calculator.xlsx.

Per-tier agent cost-per-task and cost-per-resolved-task engine with multi-step
COGS waterfall (planner + worker × parallel × retries × LLM tokens + tools +
HITL + eval + reserves). Sensitivity, stress-test, dashboard, Africa-notes.

Spec: skills/10-financial-projections/saas-agent-unit-economics-and-cogs/
      references/saas-agent-cost-per-task-calculator-spec.md
      and saas-agent-unit-economics-template.md.
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
    "saas-agent-cost-per-task-calculator.xlsx"
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
        "SaaS Agent Cost-Per-Task Calculator",
        "Per-tier agent cost engine for AI-agent SaaS products. Builds the agent COGS "
        "waterfall from inputs: (planner steps + worker steps x parallel branches) x "
        "(1 + retries) x LLM tokens + tool invocations + HITL escalations + vector + "
        "observability + eval overhead + retraining amortisation + safety floor + "
        "supervision overhead. Produces cost-per-attempted-task AND cost-per-resolved-"
        "task (the true unit, since failed / abandoned tasks still consume cost and must "
        "amortise across resolved outcomes). Includes margin analysis vs per-resolution "
        "pricing, 2-D sensitivity, eight pre-coded stress scenarios, dashboard with "
        "traffic lights, and Africa-specific adjustments.",
        sheets=[
            ("Inputs",        "Yellow cells. Tier mix, per-task agent dimensions, LLM rates, tools, HITL, eval, reserves, FX."),
            ("Cost-Per-Task", "Per-tier waterfall: step inflation, LLM, tool, HITL, vector, observability, eval, retraining, safety floor, supervision. Cost per attempted vs resolved task. Sensitivity columns."),
            ("Margin-Analysis", "Agent price per resolved task × resolution rate vs cost-per-resolved-task → agent gross margin per tier; contribution margin including S&M attribution."),
            ("Sensitivity",   "Four 2-D tables: tokens/step × $/1k; intervention-rate × HITL $/min; tools/task × external-%; parallel branches × retries factor (step inflation)."),
            ("Stress-Test",   "Six pre-coded scenarios: Provider 5x; Intervention 2x; Model deprecation 2x; Tool-vendor outage 3x; Abandonment 50→25% (positive); Combined shock."),
            ("Dashboard",     "Cost-per-resolved by tier with traffic lights (>70% GM green / 50-70 amber / <50 red); stress waterfall chart; reference to AI-cost-of-tenant baseline."),
            ("Africa-Notes",  "Agent-specific FX clauses, mobile-money in tool costs, longer collection cycles for SLA-tied per-resolution pricing, USD pricing for Enterprise, sovereign-AI premium."),
        ],
        owner="CFO + Head of Agent (joint ownership); Eval Engineer for intervention rate; Tool Engineer for tool cost share",
        cadence="Weekly: cost-per-resolved-task, cost-per-task weighted, intervention rate, tool reliability. "
                "Monthly: agent gross margin, HITL share, tool-cost share, retry overhead share, provider pricing watch. "
                "Quarterly: model-migration reserve, irreversibility reserve. "
                "Variance >+15% WoW on cost-per-resolved triggers a re-plan loop per meta-living-plan-governance.",
        sources="saas-agent-cost-per-task-calculator-spec.md, saas-agent-unit-economics-template.md (this engine); "
                "book-extractions/agent-products-business-plan-audit-2026.md COGS waterfall; "
                "saas-ai-cost-of-tenant-calculator.xlsx (single-shot baseline this workbook extends to multi-step)."
    )

    # =============================================================
    # INPUTS
    # =============================================================
    ws = wb.add_worksheet("Inputs")
    ws.set_column("A:A", 48)
    ws.set_column("B:D", 14)
    ws.set_column("E:E", 4)
    ws.set_column("F:F", 60)
    ws.set_row(0, 28)
    ws.merge_range("A1:F1", "Inputs — Agent Cost-Per-Task Calculator", fmts["title"])
    ws.write("A2", "Yellow = input. White = formula. Three tiers: Free, Pro, Enterprise.", fmts["subtitle"])

    # We'll track row numbers as we go (1-indexed for cell references).
    # Section 1: Tier mix
    ws.merge_range("A4:F4", "1. Tenant Mix & Volume", fmts["h2"])
    ws.write("A5", "", fmts["row_header"])
    ws.write("B5", "Free", fmts["col_header"])
    ws.write("C5", "Pro", fmts["col_header"])
    ws.write("D5", "Enterprise", fmts["col_header"])
    ws.write("F5", "Notes", fmts["col_header"])

    # Row map starts at 6 (1-indexed)
    rows_block_1 = [
        ("Tenants (count)",                       [400, 150, 30],   "input_int",
            "Active customer count by tier."),
        ("Active tasks per tenant per month",     [50, 400, 3000],  "input_int",
            "Tasks attempted per tenant per month."),
    ]
    # Section 2 — per-task agent dimensions
    rows_block_2 = [
        ("Avg planner steps per task",            [1, 1, 2],        "input_int",
            "Plan / decompose step(s) before workers."),
        ("Avg worker steps per task",             [2, 4, 8],        "input_int",
            "Worker LLM calls per task (single branch)."),
        ("Parallel branches per task",            [1, 1, 2],        "input_int",
            "Fan-out factor for multi-agent designs. 1 = single agent."),
        ("Retries factor (% of steps retried)",   [0.10, 0.15, 0.20], "input_pct",
            "Retry-overhead multiplier on step count."),
        ("Abandonment rate",                      [0.10, 0.12, 0.15], "input_pct",
            "% of attempted tasks the user abandons. Divides into cost-per-resolved."),
        ("Intervention (HITL escalation) rate",   [0.05, 0.10, 0.15], "input_pct",
            "% of tasks needing human help."),
        ("HITL minutes per intervention",         [3, 5, 8],        "input_int",
            "Avg minutes a human spends per escalated task."),
        ("HITL fully-loaded $/min",               [0.10, 0.15, 0.50], "input_usd2",
            "Loaded HITL hourly rate / 60. Africa-low end Free; US-comparable Ent."),
    ]
    # Section 3 — LLM dimensions
    rows_block_3 = [
        ("Input tokens per step (avg)",           [400, 800, 1500], "input_int",
            "Prompt + RAG context + chat history per step."),
        ("Output tokens per step (avg)",          [150, 400, 1000], "input_int",
            "Generation tokens per step."),
        ("Cheap-router model $/1k input",         [0.0001, 0.00015, 0.00020], "input_usd2",
            "Routing / cheap step price. Llama / Haiku class."),
        ("Cheap-router model $/1k output",        [0.0002, 0.00060, 0.00080], "input_usd2",
            ""),
        ("Planner model $/1k input",              [0.00050, 0.00150, 0.00250], "input_usd2",
            "Planner LLM. GPT-4o-mini → GPT-4o / Sonnet."),
        ("Planner model $/1k output",             [0.00150, 0.00500, 0.01000], "input_usd2",
            ""),
        ("Worker model $/1k input",               [0.00015, 0.00050, 0.00150], "input_usd2",
            "Worker LLM (typically mid-tier)."),
        ("Worker model $/1k output",              [0.00060, 0.00150, 0.00500], "input_usd2",
            ""),
    ]
    # Section 4 — Tools
    rows_block_4 = [
        ("Tool calls per task",                   [2, 5, 10],       "input_int",
            "Avg invocations to external tools per task."),
        ("% of tool calls external (paid)",       [0.40, 0.60, 0.80], "input_pct",
            "Fraction that incurs vendor cost (rest internal/free)."),
        ("Avg external tool call $",              [0.005, 0.010, 0.020], "input_usd2",
            "Avg per-invocation tariff (CRM/ERP/payment/KYC/etc)."),
        ("Vector store $/task",                   [0.0005, 0.0010, 0.0025], "input_usd2",
            "Pinecone / Qdrant / pgvector per-query allocation."),
        ("Observability $/task",                  [0.0002, 0.0005, 0.0015], "input_usd2",
            "Langfuse / LangSmith / Helicone per-trace allocation."),
    ]
    # Section 5 — Overheads & reserves
    rows_block_5 = [
        ("Eval overhead (% of LLM+tool cost)",    [0.08, 0.10, 0.15], "input_pct",
            "Online + offline eval re-runs as a % of direct AI+tool."),
        ("Retraining amortisation $/task",        [0.000, 0.0005, 0.002], "input_usd2",
            "Monthly retrain cost / monthly task volume."),
        ("Supervision overhead (% of LLM)",       [0.05, 0.08, 0.12], "input_pct",
            "Critic / supervisor LLM calls overhead."),
        ("Safety floor — red-team $/task",        [0.0001, 0.0005, 0.002], "input_usd2",
            "Red-team monitoring, jailbreak detection."),
    ]
    # Section 6 — Pricing
    rows_block_6 = [
        ("Per-resolved-task price ($)",           [0.00, 0.50, 2.00], "input_usd2",
            "Headline price per resolved (Free tier may be $0 / tier-bundled)."),
        ("S&M attribution % of revenue",          [0.00, 0.25, 0.15], "input_pct",
            "Per-resolution revenue absorbed by S&M."),
        ("Target agent gross margin",             [0.50, 0.65, 0.75], "input_pct",
            "Pricing-floor target; <50 red / 50-70 amber / >70 green on Dashboard."),
        ("Internal markup (cost ceiling × price)",[1.30, 1.50, 1.50], "input",
            "If cost-per-resolved > markup × price, flag tenant as above ceiling."),
    ]

    r = 5  # spreadsheet row 6 (Tenants count) — 0-indexed 5
    block_starts = {}
    block_starts["TENANTS"] = r + 1
    for label, vals, kind, note in rows_block_1:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1 + i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1
    block_starts["TASKS_PM"] = block_starts["TENANTS"] + 1

    # Section 2 header
    ws.merge_range(r, 0, r, 5, "2. Per-Task Agent Architecture", fmts["h2"]); r += 1
    block_starts["SEC2"] = r + 1
    for label, vals, kind, note in rows_block_2:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1 + i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1
    # rows in sec2 indices
    PLAN_R   = block_starts["SEC2"]      # planner steps
    WORK_R   = PLAN_R + 1                # worker steps
    BRANCH_R = WORK_R + 1                # parallel branches
    RETRY_R  = BRANCH_R + 1              # retries factor
    ABAND_R  = RETRY_R + 1               # abandonment
    INTERV_R = ABAND_R + 1               # intervention
    HMIN_R   = INTERV_R + 1              # hitl minutes
    HRATE_R  = HMIN_R + 1                # hitl $/min

    # Section 3
    ws.merge_range(r, 0, r, 5, "3. LLM Token Dimensions (per step, three model classes)", fmts["h2"]); r += 1
    block_starts["SEC3"] = r + 1
    for label, vals, kind, note in rows_block_3:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1 + i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1
    INTOK_R    = block_starts["SEC3"]
    OUTTOK_R   = INTOK_R + 1
    CHEAP_IN_R = OUTTOK_R + 1
    CHEAP_OUT_R= CHEAP_IN_R + 1
    PLAN_IN_R  = CHEAP_OUT_R + 1
    PLAN_OUT_R = PLAN_IN_R + 1
    WORK_IN_R  = PLAN_OUT_R + 1
    WORK_OUT_R = WORK_IN_R + 1

    # Section 4
    ws.merge_range(r, 0, r, 5, "4. Tools, Vector, Observability", fmts["h2"]); r += 1
    block_starts["SEC4"] = r + 1
    for label, vals, kind, note in rows_block_4:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1 + i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1
    TOOLS_R   = block_starts["SEC4"]
    EXTPCT_R  = TOOLS_R + 1
    EXTCOST_R = EXTPCT_R + 1
    VECT_R    = EXTCOST_R + 1
    OBS_R     = VECT_R + 1

    # Section 5
    ws.merge_range(r, 0, r, 5, "5. Overheads, Retraining & Safety", fmts["h2"]); r += 1
    block_starts["SEC5"] = r + 1
    for label, vals, kind, note in rows_block_5:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1 + i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1
    EVAL_R    = block_starts["SEC5"]
    RETR_R    = EVAL_R + 1
    SUPV_R    = RETR_R + 1
    SAFE_R    = SUPV_R + 1

    # Section 6
    ws.merge_range(r, 0, r, 5, "6. Pricing & Margin Targets", fmts["h2"]); r += 1
    block_starts["SEC6"] = r + 1
    for label, vals, kind, note in rows_block_6:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1 + i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1
    PRICE_R  = block_starts["SEC6"]
    SM_R     = PRICE_R + 1
    GMTGT_R  = SM_R + 1
    MARK_R   = GMTGT_R + 1

    # Section 7 — FX & display
    ws.merge_range(r, 0, r, 5, "7. FX & Display", fmts["h2"]); r += 1
    ws.write(r, 0, "FX rate UGX per USD", fmts["row_header"]); ws.write(r, 1, 3800, fmts["input"]); FX_UGX = r + 1; r += 1
    ws.write(r, 0, "FX rate KES per USD", fmts["row_header"]); ws.write(r, 1, 130,  fmts["input"]); FX_KES = r + 1; r += 1
    ws.write(r, 0, "FX rate NGN per USD", fmts["row_header"]); ws.write(r, 1, 1600, fmts["input"]); FX_NGN = r + 1; r += 1
    ws.write(r, 0, "FX rate ZAR per USD", fmts["row_header"]); ws.write(r, 1, 18,   fmts["input"]); FX_ZAR = r + 1; r += 1
    ws.write(r, 0, "FX rate EGP per USD", fmts["row_header"]); ws.write(r, 1, 49,   fmts["input"]); FX_EGP = r + 1; r += 1
    ws.write(r, 0, "Reporting currency code", fmts["row_header"]); ws.write(r, 1, "UGX", fmts["input_text"]); r += 1

    # Named ranges (tier-by-tier where useful)
    add_named(wb, "Branch_Avg",   f"Inputs!$C${BRANCH_R}")  # use Pro tier value as representative for some displays
    add_named(wb, "Retry_Avg",    f"Inputs!$C${RETRY_R}")
    add_named(wb, "FX_UGX_A",     f"Inputs!$B${FX_UGX}")
    add_named(wb, "FX_KES_A",     f"Inputs!$B${FX_KES}")
    add_named(wb, "FX_NGN_A",     f"Inputs!$B${FX_NGN}")
    add_named(wb, "AGT_Markup_Ent", f"Inputs!$D${MARK_R}")
    add_named(wb, "AGT_GM_Target_Ent", f"Inputs!$D${GMTGT_R}")
    add_named(wb, "AGT_Tenants_Ent", f"Inputs!$D${block_starts['TENANTS']}")
    add_named(wb, "AGT_TasksPM_Ent", f"Inputs!$D${block_starts['TASKS_PM']}")

    # Helper: tier column letter (1=B, 2=C, 3=D) and ref
    def cell(tier, row):
        return f"Inputs!{chr(ord('A')+tier)}{row}"

    # =============================================================
    # COST-PER-TASK
    # =============================================================
    wsc = wb.add_worksheet("Cost-Per-Task")
    wsc.set_column("A:A", 46); wsc.set_column("B:D", 16); wsc.set_column("E:H", 14)
    wsc.set_column("I:I", 56)
    wsc.set_row(0, 28)
    wsc.merge_range("A1:I1", "Cost-Per-Task — Agent COGS Waterfall (USD / task)", fmts["title"])
    wsc.write("A2",
        "Step inflation × LLM (planner + worker + supervision) + tools + HITL + vector + obs + eval + retraining + safety.",
        fmts["subtitle"])
    wsc.write(2, 0, "Component", fmts["col_header"])
    wsc.write(2, 1, "Free",       fmts["col_header"])
    wsc.write(2, 2, "Pro",        fmts["col_header"])
    wsc.write(2, 3, "Enterprise", fmts["col_header"])
    wsc.write(2, 4, "Free ×2 steps",  fmts["col_header"])
    wsc.write(2, 5, "Pro ×2 tools",   fmts["col_header"])
    wsc.write(2, 6, "Ent ×2 interv.", fmts["col_header"])
    wsc.write(2, 7, "Ent ×2 abandon", fmts["col_header"])
    wsc.write(2, 8, "Formula",    fmts["col_header"])

    # Row pointers (1-indexed for spreadsheet)
    # The first data row is spreadsheet row 4 (0-idx 3).
    def step_count_formula(t):
        return (f"=({cell(t,PLAN_R)}+{cell(t,WORK_R)}*{cell(t,BRANCH_R)})"
                f"*(1+{cell(t,RETRY_R)})")

    def llm_cost_formula(t):
        # planner step cost + worker step costs. Approx model:
        # planner_step_count = planner_steps * (1+retries) at planner price
        # worker_step_count  = worker_steps * branches * (1+retries) at worker price
        return (
            f"=({cell(t,PLAN_R)}*(1+{cell(t,RETRY_R)})*("
            f"{cell(t,INTOK_R)}*{cell(t,PLAN_IN_R)}+{cell(t,OUTTOK_R)}*{cell(t,PLAN_OUT_R)})/1000"
            f"+{cell(t,WORK_R)}*{cell(t,BRANCH_R)}*(1+{cell(t,RETRY_R)})*("
            f"{cell(t,INTOK_R)}*{cell(t,WORK_IN_R)}+{cell(t,OUTTOK_R)}*{cell(t,WORK_OUT_R)})/1000)"
        )

    def tool_cost_formula(t):
        return (f"={cell(t,TOOLS_R)}*{cell(t,EXTPCT_R)}*{cell(t,EXTCOST_R)}")

    def hitl_cost_formula(t):
        return (f"={cell(t,INTERV_R)}*{cell(t,HMIN_R)}*{cell(t,HRATE_R)}")

    def vec_formula(t):  return f"={cell(t,VECT_R)}"
    def obs_formula(t):  return f"={cell(t,OBS_R)}"
    def eval_formula(t, llm_row, tool_row):
        return f"=({llm_row}+{tool_row})*{cell(t,EVAL_R)}"
    def retrain_formula(t): return f"={cell(t,RETR_R)}"
    def safe_formula(t):    return f"={cell(t,SAFE_R)}"
    def supv_formula(t, llm_row):
        return f"={llm_row}*{cell(t,SUPV_R)}"

    # Now write rows. row 3 (0-idx) is "Step inflation" diagnostic.
    # Spreadsheet refs use 4 for first.
    # Component layout:
    rows = []
    # 1) Step inflation
    rows.append(("Step inflation (steps per attempted task)",
                 step_count_formula, "calc"))
    # 2) LLM cost
    rows.append(("LLM cost (planner + worker × branches × retries)",
                 llm_cost_formula, "calc_usd2"))
    # 3) Tool cost
    rows.append(("Tool cost (calls × external-% × $/call)",
                 tool_cost_formula, "calc_usd2"))
    # 4) HITL cost
    rows.append(("HITL escalation cost (interv. rate × min × $/min)",
                 hitl_cost_formula, "calc_usd2"))
    # 5) Vector store
    rows.append(("Vector store / RAG per task",
                 vec_formula, "calc_usd2"))
    # 6) Observability
    rows.append(("Observability / tracing per task",
                 obs_formula, "calc_usd2"))
    # 7) Supervision overhead
    rows.append(("Supervision (% of LLM)",
                 None, "calc_usd2"))     # placeholder; uses derived LLM ref
    # 8) Eval overhead
    rows.append(("Eval overhead (% of LLM + tool)",
                 None, "calc_usd2"))
    # 9) Retraining amortisation
    rows.append(("Retraining amortisation per task",
                 retrain_formula, "calc_usd2"))
    # 10) Safety floor
    rows.append(("Safety floor (red-team monitoring)",
                 safe_formula, "calc_usd2"))

    # Write rows
    start_r = 3  # 0-idx
    for i, (label, fn, kind) in enumerate(rows):
        rr = start_r + i
        wsc.write(rr, 0, label, fmts["row_header"])
        if fn is not None:
            for t in range(3):
                wsc.write_formula(rr, 1 + t, fn(t + 1), fmts[kind])
        # sensitivity columns filled later in pass-2

    # Now we have:
    # spreadsheet row of LLM = start_r+2 (0-idx) → row number = start_r+2+1
    LLM_ROW   = start_r + 2 + 1   # 1-indexed
    TOOL_ROW  = start_r + 3 + 1
    HITL_ROW  = start_r + 4 + 1
    VEC_ROW   = start_r + 5 + 1
    OBS_ROW   = start_r + 6 + 1
    SUPV_ROW  = start_r + 7 + 1
    EVAL_ROW  = start_r + 8 + 1
    RETR_ROW  = start_r + 9 + 1
    SAFE_ROW  = start_r + 10 + 1

    # Fill supervision (row index = start_r+7)
    for t in range(3):
        col_letter = chr(ord('B')+t)
        wsc.write_formula(start_r+7-1+1, 1+t, f"={col_letter}{LLM_ROW}*{cell(t+1,SUPV_R)}", fmts["calc_usd2"])
    # Actually correct row index 0-based = start_r+7-1? Let me redo cleanly.
    # rows indices in our list 0..9. supervision is index 7. start_r+7=10 → spreadsheet row 11.
    # We wrote None earlier so let's re-do supervision and eval cleanly:
    # supervision row index = start_r+6 (because rows[6] is supervision)
    # Actually rows[6] is "Supervision" (0-indexed: 0=step,1=LLM,2=tool,3=HITL,4=vec,5=obs,6=supv,7=eval,8=retrain,9=safe)
    SUPV_ROW_IDX = start_r + 6   # 0-indexed
    EVAL_ROW_IDX = start_r + 7   # 0-indexed
    # spreadsheet row numbers
    SUPV_R_NUM = SUPV_ROW_IDX + 1
    EVAL_R_NUM = EVAL_ROW_IDX + 1
    # recompute LLM/TOOL using correct 0-indexed → spreadsheet
    LLM_ROW   = start_r + 1 + 1   # 0-idx 4 → ss row 5
    TOOL_ROW  = start_r + 2 + 1   # 0-idx 5 → ss row 6
    HITL_ROW  = start_r + 3 + 1
    VEC_ROW   = start_r + 4 + 1
    OBS_ROW   = start_r + 5 + 1
    RETR_ROW  = start_r + 8 + 1
    SAFE_ROW  = start_r + 9 + 1

    # Now write supervision and eval correctly
    for t in range(3):
        col_letter = chr(ord('B')+t)
        wsc.write_formula(SUPV_ROW_IDX, 1+t,
            f"={col_letter}{LLM_ROW}*{cell(t+1,SUPV_R)}", fmts["calc_usd2"])
        wsc.write_formula(EVAL_ROW_IDX, 1+t,
            f"=({col_letter}{LLM_ROW}+{col_letter}{TOOL_ROW})*{cell(t+1,EVAL_R)}", fmts["calc_usd2"])

    # TOTAL row
    total_idx = start_r + 10   # 0-idx
    TOTAL_R_NUM = total_idx + 1
    wsc.write(total_idx, 0, "TOTAL cost per ATTEMPTED task", fmts["row_header"])
    for t in range(3):
        col_letter = chr(ord('B')+t)
        wsc.write_formula(total_idx, 1+t,
            f"=SUM({col_letter}{LLM_ROW}:{col_letter}{SAFE_ROW})",
            fmts["calc_bold_usd"])
    # COST PER RESOLVED row
    resolved_idx = total_idx + 1
    RES_R_NUM = resolved_idx + 1
    wsc.write(resolved_idx, 0, "COST per RESOLVED task (÷ (1−abandonment))", fmts["row_header"])
    for t in range(3):
        col_letter = chr(ord('B')+t)
        wsc.write_formula(resolved_idx, 1+t,
            f"={col_letter}{TOTAL_R_NUM}/(1-{cell(t+1,ABAND_R)})",
            fmts["calc_bold_usd"])
    wsc.write(resolved_idx, 8,
        "The TRUE unit. Failed/abandoned tasks still consume cost; resolved outcomes carry that drag.",
        fmts["note_bold"])

    # Total tier monthly cost
    tt_idx = resolved_idx + 1
    wsc.write(tt_idx, 0, "× Tasks/month × Tenants → tier monthly cost", fmts["row_header"])
    for t in range(3):
        col_letter = chr(ord('B')+t)
        wsc.write_formula(tt_idx, 1+t,
            f"={col_letter}{TOTAL_R_NUM}*{cell(t+1, block_starts['TASKS_PM'])}*{cell(t+1, block_starts['TENANTS'])}",
            fmts["calc_usd"])
    annual_idx = tt_idx + 1
    wsc.write(annual_idx, 0, "Annual tier agent COGS (USD)", fmts["row_header"])
    for t in range(3):
        col_letter = chr(ord('B')+t)
        wsc.write_formula(annual_idx, 1+t, f"={col_letter}{tt_idx+1}*12", fmts["calc_usd"])
    grand_idx = annual_idx + 1
    wsc.write(grand_idx, 0, "GRAND total annual agent COGS (USD, all tiers)", fmts["row_header"])
    wsc.write_formula(grand_idx, 1, f"=SUM(B{annual_idx+1}:D{annual_idx+1})", fmts["calc_bold_usd"])

    # Sensitivity columns (E..H) for the TOTAL and RESOLVED rows
    # Free ×2 steps  — recompute LLM under doubled step counts
    # We re-derive cleanly per scenario in a couple of rows for clarity.
    sens_idx = grand_idx + 3
    wsc.merge_range(sens_idx, 0, sens_idx, 8,
        "Sensitivity columns (×2 stress vs baseline, per tier highlighted)", fmts["h2"])
    sens_idx += 1
    sens_rows = [
        ("Free — total cost-per-resolved at ×2 step count",
         lambda: (
            f"=( {cell(1,PLAN_R)}*2*(1+{cell(1,RETRY_R)})*({cell(1,INTOK_R)}*{cell(1,PLAN_IN_R)}+{cell(1,OUTTOK_R)}*{cell(1,PLAN_OUT_R)})/1000"
            f" + {cell(1,WORK_R)}*2*{cell(1,BRANCH_R)}*(1+{cell(1,RETRY_R)})*({cell(1,INTOK_R)}*{cell(1,WORK_IN_R)}+{cell(1,OUTTOK_R)}*{cell(1,WORK_OUT_R)})/1000"
            f" + {cell(1,TOOLS_R)}*{cell(1,EXTPCT_R)}*{cell(1,EXTCOST_R)}"
            f" + {cell(1,INTERV_R)}*{cell(1,HMIN_R)}*{cell(1,HRATE_R)}"
            f" + {cell(1,VECT_R)} + {cell(1,OBS_R)}"
            f" + {cell(1,RETR_R)} + {cell(1,SAFE_R)} )"
            f" * (1 + {cell(1,SUPV_R)} + {cell(1,EVAL_R)})"
            f" / (1-{cell(1,ABAND_R)})"
         )),
        ("Pro — total cost-per-resolved at ×2 tool calls",
         lambda: (
            f"=( B{LLM_ROW.__repr__().replace('repr','')}".replace("repr(","").replace(")","")  # placeholder
         )),
    ]
    # Simpler: just write Pro and Ent stress versions
    wsc.write(sens_idx, 0, "Free — cost/resolved @ ×2 steps", fmts["row_header"])
    wsc.write_formula(sens_idx, 1,
        f"=( {cell(1,PLAN_R)}*2*(1+{cell(1,RETRY_R)})*({cell(1,INTOK_R)}*{cell(1,PLAN_IN_R)}+{cell(1,OUTTOK_R)}*{cell(1,PLAN_OUT_R)})/1000"
        f"+ {cell(1,WORK_R)}*2*{cell(1,BRANCH_R)}*(1+{cell(1,RETRY_R)})*({cell(1,INTOK_R)}*{cell(1,WORK_IN_R)}+{cell(1,OUTTOK_R)}*{cell(1,WORK_OUT_R)})/1000"
        f"+ {cell(1,TOOLS_R)}*{cell(1,EXTPCT_R)}*{cell(1,EXTCOST_R)}"
        f"+ {cell(1,INTERV_R)}*{cell(1,HMIN_R)}*{cell(1,HRATE_R)}"
        f"+ {cell(1,VECT_R)} + {cell(1,OBS_R)} + {cell(1,RETR_R)} + {cell(1,SAFE_R)} )"
        f"*(1+{cell(1,SUPV_R)}+{cell(1,EVAL_R)})/(1-{cell(1,ABAND_R)})",
        fmts["calc_usd2"])
    sens_idx += 1
    wsc.write(sens_idx, 0, "Pro — cost/resolved @ ×2 tool calls", fmts["row_header"])
    wsc.write_formula(sens_idx, 1,
        f"=( {cell(2,PLAN_R)}*(1+{cell(2,RETRY_R)})*({cell(2,INTOK_R)}*{cell(2,PLAN_IN_R)}+{cell(2,OUTTOK_R)}*{cell(2,PLAN_OUT_R)})/1000"
        f"+ {cell(2,WORK_R)}*{cell(2,BRANCH_R)}*(1+{cell(2,RETRY_R)})*({cell(2,INTOK_R)}*{cell(2,WORK_IN_R)}+{cell(2,OUTTOK_R)}*{cell(2,WORK_OUT_R)})/1000"
        f"+ {cell(2,TOOLS_R)}*2*{cell(2,EXTPCT_R)}*{cell(2,EXTCOST_R)}"
        f"+ {cell(2,INTERV_R)}*{cell(2,HMIN_R)}*{cell(2,HRATE_R)}"
        f"+ {cell(2,VECT_R)} + {cell(2,OBS_R)} + {cell(2,RETR_R)} + {cell(2,SAFE_R)} )"
        f"*(1+{cell(2,SUPV_R)}+{cell(2,EVAL_R)})/(1-{cell(2,ABAND_R)})",
        fmts["calc_usd2"])
    sens_idx += 1
    wsc.write(sens_idx, 0, "Ent — cost/resolved @ ×2 intervention rate", fmts["row_header"])
    wsc.write_formula(sens_idx, 1,
        f"=( {cell(3,PLAN_R)}*(1+{cell(3,RETRY_R)})*({cell(3,INTOK_R)}*{cell(3,PLAN_IN_R)}+{cell(3,OUTTOK_R)}*{cell(3,PLAN_OUT_R)})/1000"
        f"+ {cell(3,WORK_R)}*{cell(3,BRANCH_R)}*(1+{cell(3,RETRY_R)})*({cell(3,INTOK_R)}*{cell(3,WORK_IN_R)}+{cell(3,OUTTOK_R)}*{cell(3,WORK_OUT_R)})/1000"
        f"+ {cell(3,TOOLS_R)}*{cell(3,EXTPCT_R)}*{cell(3,EXTCOST_R)}"
        f"+ {cell(3,INTERV_R)}*2*{cell(3,HMIN_R)}*{cell(3,HRATE_R)}"
        f"+ {cell(3,VECT_R)} + {cell(3,OBS_R)} + {cell(3,RETR_R)} + {cell(3,SAFE_R)} )"
        f"*(1+{cell(3,SUPV_R)}+{cell(3,EVAL_R)})/(1-{cell(3,ABAND_R)})",
        fmts["calc_usd2"])
    sens_idx += 1
    wsc.write(sens_idx, 0, "Ent — cost/resolved @ ×2 abandonment rate", fmts["row_header"])
    wsc.write_formula(sens_idx, 1,
        f"=D{TOTAL_R_NUM}/(1-{cell(3,ABAND_R)}*2)",
        fmts["calc_usd2"])

    # Conditional format on cost-per-resolved row — green when low, red when high (per-tier reading)
    wsc.conditional_format(f"B{RES_R_NUM}:D{RES_R_NUM}", {
        "type": "3_color_scale",
        "min_color": "#63BE7B", "mid_color": "#FFEB84", "max_color": "#F8696B",
    })

    # =============================================================
    # MARGIN-ANALYSIS
    # =============================================================
    wsm = wb.add_worksheet("Margin-Analysis")
    wsm.set_column("A:A", 44); wsm.set_column("B:D", 16); wsm.set_row(0, 28)
    wsm.merge_range("A1:D1", "Agent Margin Analysis — by Tier", fmts["title"])
    wsm.write(2, 0, "Line", fmts["col_header"])
    wsm.write(2, 1, "Free", fmts["col_header"])
    wsm.write(2, 2, "Pro", fmts["col_header"])
    wsm.write(2, 3, "Enterprise", fmts["col_header"])

    margin_rows = [
        ("Per-resolved-task price ($)",
            lambda t: f"={cell(t,PRICE_R)}", "calc_usd2"),
        ("Resolution rate (1 − abandonment)",
            lambda t: f"=1-{cell(t,ABAND_R)}", "calc_pct"),
        ("Agent revenue per attempted task ($)",
            lambda t: f"={cell(t,PRICE_R)}*(1-{cell(t,ABAND_R)})", "calc_usd2"),
        ("Cost per attempted task ($)",
            lambda t: f"='Cost-Per-Task'!{chr(ord('A')+t)}{TOTAL_R_NUM}", "calc_usd2"),
        ("Cost per resolved task ($)",
            lambda t: f"='Cost-Per-Task'!{chr(ord('A')+t)}{RES_R_NUM}", "calc_usd2"),
        ("Agent gross profit per resolved ($)",
            lambda t: f"={cell(t,PRICE_R)}-'Cost-Per-Task'!{chr(ord('A')+t)}{RES_R_NUM}", "calc_usd2"),
        ("Agent gross margin %",
            lambda t: f"=IF({cell(t,PRICE_R)}>0,({cell(t,PRICE_R)}-'Cost-Per-Task'!{chr(ord('A')+t)}{RES_R_NUM})/{cell(t,PRICE_R)},-1)", "calc_bold_pct"),
        ("S&M attribution per resolved ($)",
            lambda t: f"={cell(t,PRICE_R)}*{cell(t,SM_R)}", "calc_usd2"),
        ("Contribution margin per resolved ($)",
            lambda t: f"={cell(t,PRICE_R)}-'Cost-Per-Task'!{chr(ord('A')+t)}{RES_R_NUM}-{cell(t,PRICE_R)}*{cell(t,SM_R)}", "calc_bold_usd"),
        ("Contribution margin %",
            lambda t: f"=IF({cell(t,PRICE_R)}>0,({cell(t,PRICE_R)}-'Cost-Per-Task'!{chr(ord('A')+t)}{RES_R_NUM}-{cell(t,PRICE_R)}*{cell(t,SM_R)})/{cell(t,PRICE_R)},-1)", "calc_bold_pct"),
        ("Cost ceiling ($ = markup × price)",
            lambda t: f"={cell(t,PRICE_R)}*{cell(t,MARK_R)}", "calc_usd2"),
        ("Above ceiling? (cost-per-resolved > ceiling)",
            lambda t: f"=IF('Cost-Per-Task'!{chr(ord('A')+t)}{RES_R_NUM}>{cell(t,PRICE_R)}*{cell(t,MARK_R)},\"YES\",\"no\")", "calc"),
    ]
    for i, (label, fn, kind) in enumerate(margin_rows):
        wsm.write(3+i, 0, label, fmts["row_header"])
        for t in range(3):
            wsm.write_formula(3+i, 1+t, fn(t+1), fmts[kind])

    # Conditional formatting on Agent GM% (row 10, 1-indexed; 0-idx = 9 → ss row 10)
    GM_PCT_SS = 3 + 6 + 1   # 0-idx 9 → ss row 10
    wsm.conditional_format(f"B{GM_PCT_SS}:D{GM_PCT_SS}", {"type":"cell","criteria":">=","value":0.70,"format":fmts["good"]})
    wsm.conditional_format(f"B{GM_PCT_SS}:D{GM_PCT_SS}", {"type":"cell","criteria":"between","minimum":0.50,"maximum":0.70,"format":fmts["warn"]})
    wsm.conditional_format(f"B{GM_PCT_SS}:D{GM_PCT_SS}", {"type":"cell","criteria":"<","value":0.50,"format":fmts["bad"]})
    # Above ceiling row → bad
    CEIL_SS = 3 + 11 + 1
    wsm.conditional_format(f"B{CEIL_SS}:D{CEIL_SS}", {"type":"text","criteria":"containing","value":"YES","format":fmts["bad"]})

    # =============================================================
    # SENSITIVITY — four 2D tables
    # =============================================================
    wss = wb.add_worksheet("Sensitivity")
    wss.set_column("A:A", 30); wss.set_column("B:I", 12); wss.set_row(0, 28)
    wss.merge_range("A1:I1", "Sensitivity — 2-D tables (Enterprise tier focus)", fmts["title"])

    # Table 1: tokens/step × $/1k (combined input + output proxy)
    wss.merge_range("A3:I3", "1. Tokens/step (combined in+out) × Blended $/1k → LLM cost / step", fmts["h2"])
    tok_axis = [200, 500, 1000, 2000, 3000, 5000, 8000]
    price_axis = [0.0005, 0.001, 0.0025, 0.005, 0.01, 0.02, 0.05]
    wss.write(4, 0, "Tokens ↓  $/1k →", fmts["col_header"])
    for i, p in enumerate(price_axis):
        wss.write(4, 1+i, p, fmts["col_header"])
    for j, tk in enumerate(tok_axis):
        wss.write(5+j, 0, tk, fmts["row_header"])
        for i, p in enumerate(price_axis):
            wss.write_formula(5+j, 1+i, f"=({tk}*{p})/1000", fmts["calc_usd2"])
    wss.conditional_format("B6:H12", {"type":"3_color_scale",
        "min_color":"#63BE7B","mid_color":"#FFEB84","max_color":"#F8696B"})

    # Table 2: intervention rate × HITL $/min → HITL cost/task (Ent HITL minutes from Inputs)
    wss.merge_range("A15:I15", "2. Intervention rate × HITL $/min → HITL cost / task (Ent HITL min)", fmts["h2"])
    int_axis = [0.02, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50]
    rate_axis = [0.05, 0.10, 0.20, 0.50, 1.0, 1.5, 2.0]
    wss.write(16, 0, "Interv. ↓  $/min →", fmts["col_header"])
    for i, rt in enumerate(rate_axis):
        wss.write(16, 1+i, rt, fmts["col_header"])
    for j, ir in enumerate(int_axis):
        wss.write(17+j, 0, ir, fmts["row_header"])
        for i, rt in enumerate(rate_axis):
            wss.write_formula(17+j, 1+i,
                f"={ir}*{cell(3,HMIN_R)}*{rt}", fmts["calc_usd2"])
    wss.conditional_format("B18:H24", {"type":"3_color_scale",
        "min_color":"#63BE7B","mid_color":"#FFEB84","max_color":"#F8696B"})

    # Table 3: tools/task × external-% → tool cost/task (Ent avg $)
    wss.merge_range("A27:I27", "3. Tools/task × External-% → tool cost / task (Ent $/call)", fmts["h2"])
    tools_axis = [1, 3, 5, 10, 15, 25, 40]
    extpct_axis = [0.1, 0.25, 0.40, 0.60, 0.75, 0.90, 1.0]
    wss.write(28, 0, "Tools ↓  Ext% →", fmts["col_header"])
    for i, ep in enumerate(extpct_axis):
        wss.write(28, 1+i, ep, fmts["col_header"])
    for j, tc in enumerate(tools_axis):
        wss.write(29+j, 0, tc, fmts["row_header"])
        for i, ep in enumerate(extpct_axis):
            wss.write_formula(29+j, 1+i,
                f"={tc}*{ep}*{cell(3,EXTCOST_R)}", fmts["calc_usd2"])
    wss.conditional_format("B30:H36", {"type":"3_color_scale",
        "min_color":"#63BE7B","mid_color":"#FFEB84","max_color":"#F8696B"})

    # Table 4: parallel branches × retries factor → step inflation
    wss.merge_range("A39:I39", "4. Parallel branches × Retries factor → step inflation multiplier (planner=1, worker=4 ref)", fmts["h2"])
    branch_axis = [1, 2, 3, 4, 5, 8, 12]
    retry_axis  = [0.0, 0.05, 0.10, 0.20, 0.30, 0.50, 1.0]
    wss.write(40, 0, "Branches ↓  Retries →", fmts["col_header"])
    for i, rt in enumerate(retry_axis):
        wss.write(40, 1+i, rt, fmts["col_header"])
    for j, br in enumerate(branch_axis):
        wss.write(41+j, 0, br, fmts["row_header"])
        for i, rt in enumerate(retry_axis):
            # (1 + 4×br) × (1+rt)
            wss.write_formula(41+j, 1+i, f"=(1+4*{br})*(1+{rt})", fmts["calc"])
    wss.conditional_format("B42:H48", {"type":"3_color_scale",
        "min_color":"#63BE7B","mid_color":"#FFEB84","max_color":"#F8696B"})

    # =============================================================
    # STRESS-TEST
    # =============================================================
    wst = wb.add_worksheet("Stress-Test")
    wst.set_column("A:A", 44); wst.set_column("B:F", 16); wst.set_row(0, 28)
    wst.merge_range("A1:F1", "Stress-Test — Enterprise Tier Cost-Per-Resolved", fmts["title"])
    wst.write(2, 0, "Scenario", fmts["col_header"])
    wst.write(2, 1, "Cost/resolved $", fmts["col_header"])
    wst.write(2, 2, "Agent GM %", fmts["col_header"])
    wst.write(2, 3, "Above ceiling?", fmts["col_header"])
    wst.write(2, 4, "Δ vs base", fmts["col_header"])
    wst.write(2, 5, "Mitigation", fmts["col_header"])

    base_res = f"'Cost-Per-Task'!D{RES_R_NUM}"
    base_price = f"{cell(3, PRICE_R)}"
    base_markup = f"{cell(3, MARK_R)}"
    # Generic builder for an Ent-tier total cost with multiplier overrides
    def ent_cost_formula(tok_mult=1.0, tool_mult=1.0, interv_mult=1.0, aband_mult=1.0,
                        provider_mult=1.0, retry_add=0.0, fix_aband=None):
        aband_term = (f"{cell(3,ABAND_R)}*{aband_mult}" if fix_aband is None
                     else str(fix_aband))
        return (
            f"=("
            f"{cell(3,PLAN_R)}*(1+{cell(3,RETRY_R)}+{retry_add})*("
            f"{cell(3,INTOK_R)}*{tok_mult}*{cell(3,PLAN_IN_R)}*{provider_mult}+"
            f"{cell(3,OUTTOK_R)}*{tok_mult}*{cell(3,PLAN_OUT_R)}*{provider_mult})/1000"
            f"+ {cell(3,WORK_R)}*{cell(3,BRANCH_R)}*(1+{cell(3,RETRY_R)}+{retry_add})*("
            f"{cell(3,INTOK_R)}*{tok_mult}*{cell(3,WORK_IN_R)}*{provider_mult}+"
            f"{cell(3,OUTTOK_R)}*{tok_mult}*{cell(3,WORK_OUT_R)}*{provider_mult})/1000"
            f"+ {cell(3,TOOLS_R)}*{tool_mult}*{cell(3,EXTPCT_R)}*{cell(3,EXTCOST_R)}"
            f"+ {cell(3,INTERV_R)}*{interv_mult}*{cell(3,HMIN_R)}*{cell(3,HRATE_R)}"
            f"+ {cell(3,VECT_R)} + {cell(3,OBS_R)} + {cell(3,RETR_R)} + {cell(3,SAFE_R)}"
            f") * (1+{cell(3,SUPV_R)}+{cell(3,EVAL_R)})"
            f" / (1-{aband_term})"
        )

    scenarios = [
        ("Baseline",
            ent_cost_formula(),
            "n/a — reference"),
        ("Provider 5× price hike",
            ent_cost_formula(provider_mult=5.0),
            "Emergency price-pass-through; switch provider; downshift router."),
        ("Intervention rate doubles to ~30%",
            ent_cost_formula(interv_mult=2.0),
            "Re-train triage; tighten policy thresholds; eval round."),
        ("Foundation-model deprecation (2× cost forced)",
            ent_cost_formula(provider_mult=2.0),
            "Reserve drawdown; planned migration; bench OSS fallback."),
        ("Tool-vendor outage (3× calls via fallback chain)",
            ent_cost_formula(tool_mult=3.0, retry_add=0.10),
            "Multi-vendor failover; degrade gracefully; SLA credit."),
        ("Positive — abandonment 50%→25% (better triage)",
            ent_cost_formula(fix_aband=cell(3, ABAND_R) + "*0.5"),
            "Upside case if eval / triage improvements land."),
        ("Combined shock: provider 2× + interv 2× + aband +10pp",
            ent_cost_formula(provider_mult=2.0, interv_mult=2.0,
                            fix_aband=f"({cell(3,ABAND_R)}+0.10)"),
            "Multi-front response: reprice + retrain + switch + reserve."),
    ]
    for i, (name, formula, mitig) in enumerate(scenarios):
        rr = 3 + i
        wst.write(rr, 0, name, fmts["row_header"])
        wst.write_formula(rr, 1, formula, fmts["calc_usd2"])
        wst.write_formula(rr, 2,
            f"=IF({base_price}>0,({base_price}-B{rr+1})/{base_price},-1)",
            fmts["calc_pct"])
        wst.write_formula(rr, 3,
            f"=IF(B{rr+1}>{base_price}*{base_markup},\"YES\",\"no\")",
            fmts["calc"])
        wst.write_formula(rr, 4, f"=B{rr+1}-{base_res}", fmts["calc_usd2"])
        wst.write(rr, 5, mitig, fmts["note"])

    wst.conditional_format(f"C4:C{3+len(scenarios)}", {"type":"cell","criteria":"<","value":0.0,"format":fmts["bad"]})
    wst.conditional_format(f"C4:C{3+len(scenarios)}", {"type":"cell","criteria":"between","minimum":0.0,"maximum":0.50,"format":fmts["warn"]})
    wst.conditional_format(f"C4:C{3+len(scenarios)}", {"type":"cell","criteria":">=","value":0.50,"format":fmts["good"]})
    wst.conditional_format(f"D4:D{3+len(scenarios)}", {"type":"text","criteria":"containing","value":"YES","format":fmts["bad"]})

    # =============================================================
    # DASHBOARD
    # =============================================================
    wsd = wb.add_worksheet("Dashboard")
    wsd.set_column("A:A", 42); wsd.set_column("B:B", 18); wsd.set_column("C:E", 14); wsd.set_row(0, 30)
    wsd.merge_range("A1:E1", "Dashboard — Agent Cost-Per-Task", fmts["title"])
    rows_d = [
        ("Free — cost per attempted task ($)",   f"='Cost-Per-Task'!B{TOTAL_R_NUM}", "usd2"),
        ("Pro — cost per attempted task ($)",    f"='Cost-Per-Task'!C{TOTAL_R_NUM}", "usd2"),
        ("Enterprise — cost per attempted ($)",  f"='Cost-Per-Task'!D{TOTAL_R_NUM}", "usd2"),
        ("Free — cost per RESOLVED task ($)",    f"='Cost-Per-Task'!B{RES_R_NUM}",   "usd2"),
        ("Pro — cost per RESOLVED task ($)",     f"='Cost-Per-Task'!C{RES_R_NUM}",   "usd2"),
        ("Enterprise — cost per RESOLVED ($)",   f"='Cost-Per-Task'!D{RES_R_NUM}",   "usd2"),
        ("Free agent GM %",                       "='Margin-Analysis'!B10", "pct"),
        ("Pro agent GM %",                        "='Margin-Analysis'!C10", "pct"),
        ("Enterprise agent GM %",                 "='Margin-Analysis'!D10", "pct"),
        ("Pro contribution margin %",             "='Margin-Analysis'!C13", "pct"),
        ("Enterprise contribution margin %",      "='Margin-Analysis'!D13", "pct"),
        ("GRAND annual agent COGS (USD all tiers)", f"='Cost-Per-Task'!B{grand_idx+1}", "usd"),
        ("GRAND annual COGS in UGX",              f"='Cost-Per-Task'!B{grand_idx+1}*FX_UGX_A", "usd"),
        ("Baseline (AI-cost-of-tenant calc) cross-ref",
            "\"See skills/14-ai-integration/templates/saas-ai-cost-of-tenant-calculator.xlsx — agent COGS extends that single-shot model\"",
            "txt"),
    ]
    r = 3
    for label, formula, kind in rows_d:
        wsd.write(r, 0, label, fmts["kpi_label"])
        if kind == "pct":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_pct"])
        elif kind in ("usd", "usd2"):
            wsd.write_formula(r, 1, formula, fmts["kpi_value_usd"])
        elif kind == "txt":
            wsd.write(r, 1, formula.strip('"'), fmts["note"])
        else:
            wsd.write_formula(r, 1, formula, fmts["kpi_value"])
        wsd.set_row(r, 22)
        r += 1

    # Traffic lights on agent GM% rows (Dashboard rows 10-12 in 1-indexed)
    wsd.conditional_format("B10:B12", {"type":"cell","criteria":">=","value":0.70,"format":fmts["good"]})
    wsd.conditional_format("B10:B12", {"type":"cell","criteria":"between","minimum":0.50,"maximum":0.70,"format":fmts["warn"]})
    wsd.conditional_format("B10:B12", {"type":"cell","criteria":"<","value":0.50,"format":fmts["bad"]})

    # Charts
    ch1 = wb.add_chart({"type":"column"})
    ch1.add_series({
        "name": "Cost per resolved task",
        "categories": "='Cost-Per-Task'!$B$3:$D$3",
        "values":     f"='Cost-Per-Task'!$B${RES_R_NUM}:$D${RES_R_NUM}",
        "fill": {"color": "#1F3864"},
    })
    ch1.set_title({"name": "Cost per Resolved Task — by Tier"})
    ch1.set_y_axis({"name": "USD"})
    ch1.set_legend({"none": True})
    wsd.insert_chart("G3", ch1, {"x_scale": 1.2, "y_scale": 1.0})

    ch2 = wb.add_chart({"type": "bar"})
    ch2.add_series({
        "name": "Agent GM %",
        "categories": "='Margin-Analysis'!$B$3:$D$3",
        "values":     "='Margin-Analysis'!$B$10:$D$10",
        "fill": {"color": "#2E75B6"},
    })
    ch2.set_title({"name": "Agent Gross Margin % by Tier"})
    ch2.set_legend({"none": True})
    wsd.insert_chart("G22", ch2, {"x_scale": 1.2, "y_scale": 1.0})

    ch3 = wb.add_chart({"type": "column"})
    ch3.add_series({
        "name": "Cost per resolved (Ent)",
        "categories": f"='Stress-Test'!$A$4:$A${3+len(scenarios)}",
        "values":     f"='Stress-Test'!$B$4:$B${3+len(scenarios)}",
        "fill": {"color": "#C65911"},
    })
    ch3.set_title({"name": "Stress-Test Waterfall — Enterprise Cost/Resolved"})
    ch3.set_y_axis({"name": "USD"})
    ch3.set_legend({"none": True})
    wsd.insert_chart("G41", ch3, {"x_scale": 1.3, "y_scale": 1.0})

    # =============================================================
    # AFRICA-NOTES
    # =============================================================
    wsa = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsa, fmts, extra_notes=[
        ("Per-Resolution Pricing under FX",
         "Agent per-resolution prices charged in local currency face USD-denominated LLM and tool cost. "
         "Include an FX corridor in pricing (re-price quarterly if FX moves >5%); Enterprise SLAs in USD. "
         "The model must hold across +/-20% FX swing per saas-agent-pricing-strategy."),
        ("Mobile-Money in Tool Costs",
         "M-Pesa / MoMo per-transaction fees are real per-task line items when agents move money. "
         "Add 1.0-2.0% as an external-tool cost when agent flows include payment initiation, KYC re-verification, or disbursement."),
        ("Longer Collection on SLA-Tied Per-Resolution Pricing",
         "Per-resolution billing tied to outcomes (e.g. arrears recovered, KYC completed) often invoices monthly in arrears with 60-120 day DSO. "
         "Hold a 9-month opex cushion vs the US 6-month standard. AI/tool cost is paid mid-month USD; revenue lags. Model the working-capital trough."),
        ("USD Pricing for Enterprise Tier (Agent Edition)",
         "Charge Enterprise per-resolution in USD-equivalent via local entity or offshore SPV. "
         "Keep Free / Pro in local currency. This protects 60-80% of agent revenue against FX as ARR scales."),
        ("Sovereign-AI Provider Premium",
         "When local-hosting is required (NITA-U directives, KE DPC, NDPC sectoral rules, ZA Info Reg), "
         "in-region GPU inference costs 1.5-3x US/EU rates. Reflect in the planner/worker $/1k cells if required by procurement."),
        ("HITL Cost Asymmetry",
         "Africa HITL cost is materially lower (UGX 4-8k/hour fully-loaded vs USD 30-60 US). "
         "Agents in Africa must beat a much lower human cost floor — but HITL fallback is cheaper to operate. "
         "Adjust the HITL $/min cell to match local market; do not import US benchmarks blindly."),
        ("Channel Cost as Per-Task Line Item",
         "WhatsApp Business API, USSD aggregator fees, SMS, IVR — these are real per-task costs in African contexts. "
         "Roll them into the external-tool cost ($/call × calls/task) cell with documented breakdown."),
    ])

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
