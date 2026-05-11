"""Build saas-ai-cost-of-tenant-calculator.xlsx.

Per-tenant AI cost (token cost + eval + retraining + vector store + RAG + observability),
margin analysis vs tier prices, sensitivity (tokens-per-prompt × $/1k input), stress-test
(token-inflation, usage-shock, retraining-doubling), dashboard.

Spec: section 14 ai-integration skill. References ai-economics-framework.md.
"""
import os, sys
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _common import make_formats, write_readme, write_africa_notes, add_named  # noqa

OUT = os.path.normpath(os.path.join(
    HERE, "..", "..", "skills", "14-ai-integration",
    "templates", "saas-ai-cost-of-tenant-calculator.xlsx"
))


def build():
    wb = xlsxwriter.Workbook(OUT)
    fmts = make_formats(wb)

    # README
    ws_r = wb.add_worksheet("README")
    write_readme(ws_r, fmts,
        "SaaS AI Cost-of-Tenant Calculator",
        "Per-tenant AI cost engine for SaaS with LLM-backed features. Models token cost "
        "(input + output × model price), eval overhead, retraining amortisation, vector-store "
        "cost, RAG retrieval, and observability — across Free / Pro / Enterprise tiers. "
        "Produces AI gross margin per tier, % of customers above the cost ceiling, and a "
        "stress-test waterfall for token-inflation and usage-shock scenarios.",
        sheets=[
            ("Inputs", "Tenants by tier, users/tenant, prompts/day, tokens, model selection, fixed costs, markup, FX."),
            ("Cost-Per-Tenant", "Monthly per-tenant cost formula by tier."),
            ("Margin-Analysis", "Tier price vs AI cost → AI GM per tier, contribution margin with S&M attribution."),
            ("Sensitivity", "2-D tables: tokens-per-prompt × $/1k input;  prompts/day × users/tenant."),
            ("Stress-Test", "Waterfall: +50/+100/+200% tokens; 2× usage; retraining 2×; eval 2×; model deprecation."),
            ("Dashboard", "Cost per tier; AI GM per tier; % customers above cost ceiling; charts."),
            ("Africa-Notes", "USD AI pricing, FX hedging, local-LLM fallback, usage caps."),
        ],
        owner="Head of AI / CFO joint ownership",
        cadence="Monthly when LLM provider pricing changes; quarterly for usage assumptions; "
                "before each pricing/packaging change.",
        sources="ai-economics-framework.md (this engine); OpenAI/Anthropic/Together public pricing; "
                "tracker.ai_economics; Cotton (Run a SaaS Business) Rule of 3-and-10 cost-margin discipline."
    )

    # INPUTS
    ws = wb.add_worksheet("Inputs")
    ws.set_column("A:A", 44); ws.set_column("B:E", 14); ws.set_column("F:F", 56); ws.set_row(0, 28)
    ws.merge_range("A1:F1", "Inputs — AI Cost-of-Tenant", fmts["title"])
    ws.write("A2", "Yellow = input. White = formula. Three tiers: Free, Pro, Enterprise.", fmts["subtitle"])

    # Tier headers
    ws.merge_range("A4:F4", "1. Tenant Mix", fmts["h2"])
    ws.write("A5", "", fmts["row_header"])
    ws.write("B5", "Free", fmts["col_header"])
    ws.write("C5", "Pro", fmts["col_header"])
    ws.write("D5", "Enterprise", fmts["col_header"])
    ws.write("F5", "Notes", fmts["col_header"])

    rows = [
        ("Tenants (count)", [500, 200, 50], "input_int",
            "Active customer count by tier."),
        ("Users per tenant", [3, 8, 25], "input_int",
            "Number of seats per tenant."),
        ("Prompts per user per day", [5, 15, 30], "input_int",
            "Daily AI prompt volume per active user."),
        ("Input tokens per prompt", [400, 800, 2000], "input_int",
            "Avg input length (prompt + RAG context + chat history)."),
        ("Output tokens per prompt", [200, 500, 1200], "input_int",
            "Avg generation length."),
        ("$ per 1k input tokens", [0.0001, 0.00015, 0.0025], "input_usd2",
            "Free=Llama-class; Pro=GPT-4o-mini-class; Ent=GPT-4o/Claude-Sonnet-class."),
        ("$ per 1k output tokens", [0.0002, 0.0006, 0.010], "input_usd2",
            "Output-tier USD pricing."),
        ("Eval / guardrails overhead %", [0.10, 0.10, 0.15], "input_pct",
            "% of token cost spent on evals (re-runs, judge models)."),
        ("Retraining $/month per tenant", [0, 1, 8], "input_usd2",
            "Amortised fine-tune / embed-refresh cost."),
        ("Vector store $/month per tenant", [0, 2, 15], "input_usd2",
            "Pinecone / Qdrant / Weaviate / pgvector."),
        ("RAG retrieval $/query", [0, 0.0001, 0.0003], "input_usd2",
            "Vector search + reranker pass."),
        ("Observability $/call", [0, 0.00005, 0.0002], "input_usd2",
            "Langfuse / Helicone / Phoenix logging."),
        ("Tier MRR price ($)", [0, 79, 499], "input_usd2",
            "Subscription price per tenant per month."),
        ("S&M attribution % of price", [0, 0.25, 0.15], "input_pct",
            "% of monthly price absorbed by S&M (CAC payback)."),
        ("Other COGS % of price", [0, 0.20, 0.15], "input_pct",
            "Non-AI COGS (hosting, support, rails)."),
    ]
    r = 5
    for label, vals, kind, note in rows:
        ws.write(r, 0, label, fmts["row_header"])
        for i, v in enumerate(vals):
            ws.write(r, 1+i, v, fmts[kind])
        ws.write(r, 5, note, fmts["note"])
        r += 1

    ws.merge_range(r, 0, r, 5, "2. Pricing Markup & FX", fmts["h2"]); r += 1
    ws.write(r, 0, "Internal markup (cost-ceiling tolerance % of price)", fmts["row_header"])
    ws.write(r, 1, 0.30, fmts["input_pct"])
    MARKUP_ROW = r + 1
    ws.write(r, 5, "If AI cost > markup × price, flag tenant as above ceiling.", fmts["note"])
    r += 1
    ws.write(r, 0, "FX rate (local per USD)", fmts["row_header"])
    ws.write(r, 1, 3800, fmts["input"])
    FX_AI_ROW = r + 1
    r += 1
    ws.write(r, 0, "Reporting currency", fmts["row_header"])
    ws.write(r, 1, "UGX", fmts["input_text"])
    r += 1
    ws.write(r, 0, "Days per month for prompt count", fmts["row_header"])
    ws.write(r, 1, 22, fmts["input_int"])
    DAYS_ROW = r + 1
    ws.write(r, 5, "Working days; reduce for B2C consumer or weekend-heavy workloads.", fmts["note"])
    r += 1

    # Named ranges by tier — for clarity we use Inputs columns directly
    add_named(wb, "FX_AI", f"Inputs!$B${FX_AI_ROW}")
    add_named(wb, "Markup", f"Inputs!$B${MARKUP_ROW}")
    add_named(wb, "Days_PM", f"Inputs!$B${DAYS_ROW}")

    # COST-PER-TENANT
    wsc = wb.add_worksheet("Cost-Per-Tenant")
    wsc.set_column("A:A", 44); wsc.set_column("B:D", 14); wsc.set_column("F:F", 60); wsc.set_row(0, 28)
    wsc.merge_range("A1:F1", "Cost Per Tenant (USD / month)", fmts["title"])
    wsc.write("A2", "Formula breakdown by tier — every component pulled from Inputs.", fmts["subtitle"])
    wsc.write(2, 0, "Component", fmts["col_header"])
    wsc.write(2, 1, "Free", fmts["col_header"])
    wsc.write(2, 2, "Pro", fmts["col_header"])
    wsc.write(2, 3, "Enterprise", fmts["col_header"])
    wsc.write(2, 5, "Formula", fmts["col_header"])

    # users × prompts/day × days × (input × $/1k_in + output × $/1k_out) /1000
    # Row 6 is users/tenant; row 7 prompts; row 8 input tokens; row 9 output; row 10 $/1k_in; row 11 $/1k_out
    # In our Inputs build the labels start at row index 5; so:
    # users-per-tenant -> Inputs row 7 (1-idx), prompts row 8, input tokens row 9, output row 10, $/1k_in row 11, $/1k_out row 12
    # eval overhead row 13, retraining row 14, vector row 15, RAG row 16, observability row 17, tier MRR row 18.
    # Let's compute these dynamically: first label "Tenants (count)" is at row index 5 → spreadsheet row 6.
    TENANT_R   = 6
    USERS_R    = 7
    PROMPTS_R  = 8
    INTOK_R    = 9
    OUTTOK_R   = 10
    INPRICE_R  = 11
    OUTPRICE_R = 12
    EVAL_R     = 13
    RETRAIN_R  = 14
    VECTOR_R   = 15
    RAG_R      = 16
    OBS_R      = 17
    PRICE_R    = 18
    SM_R       = 19
    OTHCOGS_R  = 20

    # Helper: cell ref for tier (1=B,2=C,3=D) and a given row
    def cell(tier, row):  # tier 1,2,3
        return f"Inputs!{chr(ord('A')+tier)}{row}"

    components = [
        ("Token cost (input)",
            lambda t: f"=({cell(t,USERS_R)}*{cell(t,PROMPTS_R)}*Days_PM*{cell(t,INTOK_R)}*{cell(t,INPRICE_R)})/1000"),
        ("Token cost (output)",
            lambda t: f"=({cell(t,USERS_R)}*{cell(t,PROMPTS_R)}*Days_PM*{cell(t,OUTTOK_R)}*{cell(t,OUTPRICE_R)})/1000"),
        ("Eval / guardrails",
            lambda t: f"=(B{4}+B{5})*{cell(t,EVAL_R)}".replace("B{4}", "B4").replace("B{5}","B5") if False else
                      f"=({cell(t,USERS_R)}*{cell(t,PROMPTS_R)}*Days_PM*"
                      f"({cell(t,INTOK_R)}*{cell(t,INPRICE_R)}+{cell(t,OUTTOK_R)}*{cell(t,OUTPRICE_R)})/1000)*{cell(t,EVAL_R)}"),
        ("Retraining (amortised)",
            lambda t: f"={cell(t,RETRAIN_R)}"),
        ("Vector store (fixed/tenant)",
            lambda t: f"={cell(t,VECTOR_R)}"),
        ("RAG retrieval",
            lambda t: f"={cell(t,USERS_R)}*{cell(t,PROMPTS_R)}*Days_PM*{cell(t,RAG_R)}"),
        ("Observability",
            lambda t: f"={cell(t,USERS_R)}*{cell(t,PROMPTS_R)}*Days_PM*{cell(t,OBS_R)}"),
    ]
    for i, (label, fn) in enumerate(components):
        wsc.write(3+i, 0, label, fmts["row_header"])
        for t in range(3):
            wsc.write_formula(3+i, 1+t, fn(t+1), fmts["calc_usd2"])
        wsc.write(3+i, 5,
            "Tier formula derived from Inputs row × users × prompts × Days_PM, plus fixed-cost rows.",
            fmts["note"])
    # Total per tenant
    wsc.write(10, 0, "TOTAL AI cost per tenant / month", fmts["row_header"])
    for t in range(3):
        c_letter = chr(ord('B')+t)
        wsc.write_formula(10, 1+t, f"=SUM({c_letter}4:{c_letter}10)", fmts["calc_bold_usd"])
    # × tenants by tier
    wsc.write(11, 0, "× Tenants in tier", fmts["row_header"])
    for t in range(3):
        wsc.write_formula(11, 1+t, f"={cell(t+1,TENANT_R)}", fmts["calc_int"])
    wsc.write(12, 0, "Total tier AI cost / month", fmts["row_header"])
    for t in range(3):
        c_letter = chr(ord('B')+t)
        wsc.write_formula(12, 1+t, f"={c_letter}11*{c_letter}12", fmts["calc_bold_usd"])
    wsc.write(13, 0, "Total AI cost / year", fmts["row_header"])
    for t in range(3):
        c_letter = chr(ord('B')+t)
        wsc.write_formula(13, 1+t, f"={c_letter}13*12", fmts["calc_usd"])
    # Grand total
    wsc.write(14, 0, "GRAND TOTAL AI cost / year (all tiers)", fmts["row_header"])
    wsc.write_formula(14, 1, "=SUM(B14:D14)", fmts["calc_bold_usd"])

    # MARGIN ANALYSIS
    wsm = wb.add_worksheet("Margin-Analysis")
    wsm.set_column("A:A", 40); wsm.set_column("B:D", 14); wsm.set_row(0, 28)
    wsm.merge_range("A1:D1", "AI Margin Analysis — by Tier", fmts["title"])
    wsm.write(2, 0, "Line", fmts["col_header"])
    wsm.write(2, 1, "Free", fmts["col_header"])
    wsm.write(2, 2, "Pro", fmts["col_header"])
    wsm.write(2, 3, "Enterprise", fmts["col_header"])

    margin_rows = [
        ("Tier price ($/month)",            lambda t: f"={cell(t,PRICE_R)}",                "calc_usd"),
        ("AI cost per tenant ($/month)",    lambda t: f"='Cost-Per-Tenant'!{chr(ord('B')+t-1)}11", "calc_usd2"),
        ("AI GM $",                          lambda t: f"=B4-B5".replace("B", chr(ord('B')+t-1)),  "calc_usd2"),
        ("AI GM %",                          lambda t: f"=IF(B4>0,(B4-B5)/B4,-1)".replace("B", chr(ord('B')+t-1)), "calc_pct"),
        ("S&M attribution $",                lambda t: f"={cell(t,PRICE_R)}*{cell(t,SM_R)}",  "calc_usd2"),
        ("Other COGS $",                     lambda t: f"={cell(t,PRICE_R)}*{cell(t,OTHCOGS_R)}", "calc_usd2"),
        ("Contribution margin $",            lambda t: f"=B4-B5-B7-B8".replace("B", chr(ord('B')+t-1)), "calc_bold_usd"),
        ("Contribution margin %",            lambda t: f"=IF(B4>0,(B4-B5-B7-B8)/B4,-1)".replace("B", chr(ord('B')+t-1)), "calc_bold_pct"),
        ("Cost ceiling $ (Markup × price)",  lambda t: f"={cell(t,PRICE_R)}*Markup",          "calc_usd2"),
        ("Above ceiling? (AI cost > ceiling)", lambda t: f"=IF(B5>B11,\"YES\",\"no\")".replace("B", chr(ord('B')+t-1)), "calc"),
    ]
    for i, (label, fn, kind) in enumerate(margin_rows):
        wsm.write(3+i, 0, label, fmts["row_header"])
        for t in range(3):
            wsm.write_formula(3+i, 1+t, fn(t+1), fmts[kind])

    # Conditional format AI GM%
    wsm.conditional_format("B7:D7", {"type": "cell", "criteria": ">=", "value": 0.70, "format": fmts["good"]})
    wsm.conditional_format("B7:D7", {"type": "cell", "criteria": "between", "minimum": 0.40, "maximum": 0.70, "format": fmts["warn"]})
    wsm.conditional_format("B7:D7", {"type": "cell", "criteria": "<", "value": 0.40, "format": fmts["bad"]})

    # SENSITIVITY
    wss = wb.add_worksheet("Sensitivity")
    wss.set_column("A:A", 32); wss.set_column("B:H", 14); wss.set_row(0, 28)
    wss.merge_range("A1:H1", "Sensitivity — tokens-per-prompt × $/1k (Enterprise tier)", fmts["title"])
    wss.write(2, 0, "Reading: Enterprise cost/tenant/mo @ varied tokens & price.", fmts["subtitle"])
    tok_axis = [500, 1000, 1500, 2000, 3000, 4000, 6000]   # total tokens per prompt
    price_axis = [0.001, 0.0025, 0.005, 0.0075, 0.010, 0.015, 0.020]
    wss.write(4, 0, "Tokens/prompt ↓  $/1k →", fmts["col_header"])
    for i, p in enumerate(price_axis):
        wss.write(4, 1+i, p, fmts["col_header"])
    for j, tk in enumerate(tok_axis):
        wss.write(5+j, 0, tk, fmts["row_header"])
        for i, p in enumerate(price_axis):
            wss.write_formula(5+j, 1+i,
                f"=({cell(3,USERS_R)}*{cell(3,PROMPTS_R)}*Days_PM*{tk}*{p})/1000",
                fmts["calc_usd2"])
    wss.conditional_format("B6:H12", {
        "type": "3_color_scale",
        "min_color": "#63BE7B", "mid_color": "#FFEB84", "max_color": "#F8696B",
    })

    # Second 2-D: prompts/day × users/tenant
    wss.merge_range("A15:H15", "Sensitivity — prompts/day × users/tenant (Pro tier, holding tokens fixed)", fmts["h2"])
    pd_axis = [5, 10, 15, 20, 30, 50, 80]
    u_axis  = [2, 5, 8, 12, 20, 30, 50]
    wss.write(16, 0, "Prompts/day ↓  Users/tenant →", fmts["col_header"])
    for i, u in enumerate(u_axis):
        wss.write(16, 1+i, u, fmts["col_header"])
    for j, pd in enumerate(pd_axis):
        wss.write(17+j, 0, pd, fmts["row_header"])
        for i, u in enumerate(u_axis):
            # Pro tier total token cost
            wss.write_formula(17+j, 1+i,
                f"=({u}*{pd}*Days_PM*({cell(2,INTOK_R)}*{cell(2,INPRICE_R)}+{cell(2,OUTTOK_R)}*{cell(2,OUTPRICE_R)}))/1000",
                fmts["calc_usd2"])
    wss.conditional_format("B18:H24", {
        "type": "3_color_scale",
        "min_color": "#63BE7B", "mid_color": "#FFEB84", "max_color": "#F8696B",
    })

    # STRESS-TEST
    wst = wb.add_worksheet("Stress-Test")
    wst.set_column("A:A", 40); wst.set_column("B:E", 16); wst.set_row(0, 28)
    wst.merge_range("A1:E1", "Stress-Test Waterfall — Enterprise Tier", fmts["title"])
    wst.write(2, 0, "Scenario", fmts["col_header"])
    wst.write(2, 1, "AI cost / tenant", fmts["col_header"])
    wst.write(2, 2, "AI GM %", fmts["col_header"])
    wst.write(2, 3, "Above ceiling?", fmts["col_header"])
    wst.write(2, 4, "Cost Δ vs base", fmts["col_header"])
    base_ent_cost_ref = "'Cost-Per-Tenant'!D11"
    base_price = f"{cell(3, PRICE_R)}"

    scenarios = [
        ("Baseline", 1.0, 1.0, 1.0, 1.0),
        ("Tokens +50%", 1.5, 1.0, 1.0, 1.0),
        ("Tokens +100%", 2.0, 1.0, 1.0, 1.0),
        ("Tokens +200%", 3.0, 1.0, 1.0, 1.0),
        ("Usage 2× (more prompts)", 1.0, 2.0, 1.0, 1.0),
        ("Retraining 2×", 1.0, 1.0, 2.0, 1.0),
        ("Eval 2×", 1.0, 1.0, 1.0, 2.0),
        ("Model deprecation (price 1.5×)", 1.0, 1.0, 1.0, 1.0),
    ]
    # We rebuild the cost inline per scenario for transparency
    for i, (name, tok_mult, usage_mult, retrain_mult, eval_mult) in enumerate(scenarios):
        wst.write(3+i, 0, name, fmts["row_header"])
        # base components scaled
        # token cost = users × prompts × days × tokens × mult × $/1k
        if name == "Model deprecation (price 1.5×)":
            cost_formula = (
                f"=({cell(3,USERS_R)}*{cell(3,PROMPTS_R)}*Days_PM*"
                f"({cell(3,INTOK_R)}*{cell(3,INPRICE_R)}*1.5+{cell(3,OUTTOK_R)}*{cell(3,OUTPRICE_R)}*1.5))/1000*(1+{cell(3,EVAL_R)})"
                f"+{cell(3,RETRAIN_R)}+{cell(3,VECTOR_R)}"
                f"+{cell(3,USERS_R)}*{cell(3,PROMPTS_R)}*Days_PM*({cell(3,RAG_R)}+{cell(3,OBS_R)})"
            )
        else:
            cost_formula = (
                f"=({cell(3,USERS_R)}*{cell(3,PROMPTS_R)}*{usage_mult}*Days_PM*"
                f"({cell(3,INTOK_R)}*{tok_mult}*{cell(3,INPRICE_R)}+{cell(3,OUTTOK_R)}*{tok_mult}*{cell(3,OUTPRICE_R)}))/1000*(1+{cell(3,EVAL_R)}*{eval_mult})"
                f"+{cell(3,RETRAIN_R)}*{retrain_mult}+{cell(3,VECTOR_R)}"
                f"+{cell(3,USERS_R)}*{cell(3,PROMPTS_R)}*{usage_mult}*Days_PM*({cell(3,RAG_R)}+{cell(3,OBS_R)})"
            )
        wst.write_formula(3+i, 1, cost_formula, fmts["calc_usd2"])
        wst.write_formula(3+i, 2, f"=IF({base_price}>0,({base_price}-B{4+i})/{base_price},-1)", fmts["calc_pct"])
        wst.write_formula(3+i, 3, f"=IF(B{4+i}>{base_price}*Markup,\"YES\",\"no\")", fmts["calc"])
        wst.write_formula(3+i, 4, f"=B{4+i}-{base_ent_cost_ref}", fmts["calc_usd2"])

    wst.conditional_format("D4:D11", {
        "type": "text", "criteria": "containing", "value": "YES", "format": fmts["bad"]
    })
    wst.conditional_format("C4:C11", {"type": "cell", "criteria": "<", "value": 0.40, "format": fmts["bad"]})
    wst.conditional_format("C4:C11", {"type": "cell", "criteria": "between", "minimum": 0.40, "maximum": 0.70, "format": fmts["warn"]})
    wst.conditional_format("C4:C11", {"type": "cell", "criteria": ">=", "value": 0.70, "format": fmts["good"]})

    # DASHBOARD
    wsd = wb.add_worksheet("Dashboard")
    wsd.set_column("A:A", 36); wsd.set_column("B:D", 16); wsd.set_row(0, 30)
    wsd.merge_range("A1:D1", "Dashboard — AI Cost-of-Tenant", fmts["title"])
    rows_d = [
        ("Free AI cost/tenant/mo",     "='Cost-Per-Tenant'!B11", "usd"),
        ("Pro AI cost/tenant/mo",      "='Cost-Per-Tenant'!C11", "usd"),
        ("Enterprise AI cost/tenant/mo","='Cost-Per-Tenant'!D11", "usd"),
        ("Free AI GM %",               "='Margin-Analysis'!B7",  "pct"),
        ("Pro AI GM %",                "='Margin-Analysis'!C7",  "pct"),
        ("Enterprise AI GM %",         "='Margin-Analysis'!D7",  "pct"),
        ("Pro contribution margin %",  "='Margin-Analysis'!C11", "pct"),
        ("Enterprise contribution margin %", "='Margin-Analysis'!D11", "pct"),
        ("Grand total AI cost / year (USD)", "='Cost-Per-Tenant'!B15", "usd"),
        ("Grand total AI cost / year (local)", "='Cost-Per-Tenant'!B15*FX_AI", "calc_usd"),
    ]
    r = 3
    for label, formula, kind in rows_d:
        wsd.write(r, 0, label, fmts["kpi_label"])
        if kind == "pct":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_pct"])
        elif kind == "usd":
            wsd.write_formula(r, 1, formula, fmts["kpi_value_usd"])
        else:
            wsd.write_formula(r, 1, formula, fmts["kpi_value"])
        wsd.set_row(r, 22)
        r += 1

    # Cost-by-tier bar chart
    ch1 = wb.add_chart({"type": "column"})
    ch1.add_series({
        "name": "Cost / tenant",
        "categories": "='Cost-Per-Tenant'!$B$3:$D$3",
        "values":     "='Cost-Per-Tenant'!$B$11:$D$11",
        "fill": {"color": "#1F3864"},
    })
    ch1.set_title({"name": "AI Cost per Tenant by Tier"})
    ch1.set_y_axis({"name": "USD / month"})
    ch1.set_legend({"none": True})
    wsd.insert_chart("F3", ch1, {"x_scale": 1.2, "y_scale": 1.0})

    # GM% by tier
    ch2 = wb.add_chart({"type": "bar"})
    ch2.add_series({
        "name": "AI GM %",
        "categories": "='Margin-Analysis'!$B$3:$D$3",
        "values":     "='Margin-Analysis'!$B$7:$D$7",
        "fill": {"color": "#2E75B6"},
    })
    ch2.set_title({"name": "AI Gross Margin % by Tier"})
    ch2.set_legend({"none": True})
    wsd.insert_chart("F22", ch2, {"x_scale": 1.2, "y_scale": 1.0})

    # Stress-test waterfall
    ch3 = wb.add_chart({"type": "column"})
    ch3.add_series({
        "name": "Enterprise cost/tenant",
        "categories": "='Stress-Test'!$A$4:$A$11",
        "values":     "='Stress-Test'!$B$4:$B$11",
        "fill": {"color": "#C65911"},
    })
    ch3.set_title({"name": "Stress-Test — Enterprise AI Cost / Tenant"})
    ch3.set_y_axis({"name": "USD"})
    ch3.set_legend({"none": True})
    wsd.insert_chart("F41", ch3, {"x_scale": 1.3, "y_scale": 1.0})

    # AFRICA-NOTES
    wsa = wb.add_worksheet("Africa-Notes")
    write_africa_notes(wsa, fmts, extra_notes=[
        ("USD-Indexed AI Tier",
         "Because LLM pricing is USD-denominated, an FX shock instantly compresses AI margin on local-currency-priced tiers. "
         "Recommended hedge: price the Enterprise tier in USD (route via local entity or offshore SPV for invoicing) so that "
         "AI cost and price are in the same currency."),
        ("Local-LLM Fallback",
         "For African deployments with FX volatility, configure a fallback to Llama-class on Bedrock / Together / Groq with "
         "local-currency hosting. Quality is ~80–90% on most enterprise tasks; cost is 3–10× lower; FX exposure is reduced because "
         "many local providers offer regional pricing."),
        ("Usage Caps",
         "Implement per-tenant token caps and prompt throttling. Defaults to consider: Free 100k tokens/mo, Pro 2M tokens/mo, "
         "Enterprise unlimited with rate-limit. Caps protect AI margin from runaway-usage by power users."),
        ("Model-Deprecation Risk",
         "Major-version model deprecations (GPT-3.5 → GPT-4 → GPT-4o → GPT-5) move pricing 30–100%. Maintain a 3-month price-tracker; "
         "the Stress-Test sheet's 'Model deprecation' row simulates a 1.5× price step."),
    ])

    wb.close()
    print(f"OK: {OUT}")
    print(f"   size = {os.path.getsize(OUT):,} bytes")


if __name__ == "__main__":
    build()
