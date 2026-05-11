"""Shared helpers for SaaS financial-model workbook builders.

All workbook builders use xlsxwriter (write-only). This module returns
a dict of named formats so all workbooks share visual identity.
"""

def make_formats(wb):
    """Return a dict of common cell formats."""
    return {
        # Headers / titles
        "title": wb.add_format({
            "bold": True, "font_size": 16, "font_color": "#FFFFFF",
            "bg_color": "#1F3864", "align": "left", "valign": "vcenter",
            "border": 1, "border_color": "#1F3864",
        }),
        "subtitle": wb.add_format({
            "italic": True, "font_size": 11, "font_color": "#1F3864",
            "align": "left",
        }),
        "h1": wb.add_format({
            "bold": True, "font_size": 14, "font_color": "#FFFFFF",
            "bg_color": "#1F3864", "align": "left", "valign": "vcenter",
            "border": 1,
        }),
        "h2": wb.add_format({
            "bold": True, "font_size": 12, "font_color": "#FFFFFF",
            "bg_color": "#2E75B6", "align": "left", "valign": "vcenter",
            "border": 1,
        }),
        "col_header": wb.add_format({
            "bold": True, "font_color": "#FFFFFF", "bg_color": "#2E75B6",
            "align": "center", "valign": "vcenter", "border": 1,
            "text_wrap": True,
        }),
        "row_header": wb.add_format({
            "bold": True, "bg_color": "#D9E1F2", "align": "left",
            "valign": "vcenter", "border": 1,
        }),
        "section": wb.add_format({
            "bold": True, "bg_color": "#FFE699", "border": 1, "italic": True,
        }),
        # Input cells (user-editable)
        "input": wb.add_format({
            "bg_color": "#FFF2CC", "border": 1, "border_color": "#BFBFBF",
            "num_format": "#,##0.00", "locked": False,
        }),
        "input_int": wb.add_format({
            "bg_color": "#FFF2CC", "border": 1, "border_color": "#BFBFBF",
            "num_format": "#,##0", "locked": False,
        }),
        "input_pct": wb.add_format({
            "bg_color": "#FFF2CC", "border": 1, "border_color": "#BFBFBF",
            "num_format": "0.0%", "locked": False,
        }),
        "input_usd": wb.add_format({
            "bg_color": "#FFF2CC", "border": 1, "border_color": "#BFBFBF",
            "num_format": "$#,##0", "locked": False,
        }),
        "input_usd2": wb.add_format({
            "bg_color": "#FFF2CC", "border": 1, "border_color": "#BFBFBF",
            "num_format": "$#,##0.00", "locked": False,
        }),
        "input_text": wb.add_format({
            "bg_color": "#FFF2CC", "border": 1, "border_color": "#BFBFBF",
            "locked": False,
        }),
        # Calculated cells (formula, locked)
        "calc": wb.add_format({
            "bg_color": "#FFFFFF", "border": 1, "border_color": "#BFBFBF",
            "num_format": "#,##0.00",
        }),
        "calc_int": wb.add_format({
            "bg_color": "#FFFFFF", "border": 1, "border_color": "#BFBFBF",
            "num_format": "#,##0",
        }),
        "calc_pct": wb.add_format({
            "bg_color": "#FFFFFF", "border": 1, "border_color": "#BFBFBF",
            "num_format": "0.0%",
        }),
        "calc_usd": wb.add_format({
            "bg_color": "#FFFFFF", "border": 1, "border_color": "#BFBFBF",
            "num_format": "$#,##0",
        }),
        "calc_usd2": wb.add_format({
            "bg_color": "#FFFFFF", "border": 1, "border_color": "#BFBFBF",
            "num_format": "$#,##0.00",
        }),
        "calc_bold": wb.add_format({
            "bg_color": "#E2EFDA", "border": 1, "bold": True,
            "num_format": "#,##0",
        }),
        "calc_bold_usd": wb.add_format({
            "bg_color": "#E2EFDA", "border": 1, "bold": True,
            "num_format": "$#,##0",
        }),
        "calc_bold_pct": wb.add_format({
            "bg_color": "#E2EFDA", "border": 1, "bold": True,
            "num_format": "0.0%",
        }),
        # Note text
        "note": wb.add_format({
            "italic": True, "font_color": "#595959", "text_wrap": True,
            "valign": "top",
        }),
        "note_bold": wb.add_format({
            "italic": True, "bold": True, "font_color": "#1F3864",
            "text_wrap": True, "valign": "top",
        }),
        "africa_note": wb.add_format({
            "text_wrap": True, "valign": "top", "bg_color": "#FFF2CC",
            "border": 1, "font_color": "#7F6000",
        }),
        "africa_header": wb.add_format({
            "bold": True, "font_size": 13, "font_color": "#FFFFFF",
            "bg_color": "#C65911", "align": "left", "valign": "vcenter",
            "border": 1,
        }),
        # Dashboard / KPI traffic-light style targets (the conditional
        # formats use these by reference when needed)
        "good": wb.add_format({"bg_color": "#C6EFCE", "font_color": "#006100", "border": 1, "num_format": "0.00"}),
        "warn": wb.add_format({"bg_color": "#FFEB9C", "font_color": "#9C5700", "border": 1, "num_format": "0.00"}),
        "bad":  wb.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006", "border": 1, "num_format": "0.00"}),
        "kpi_label": wb.add_format({
            "bold": True, "bg_color": "#1F3864", "font_color": "#FFFFFF",
            "border": 1, "align": "left", "valign": "vcenter",
        }),
        "kpi_value": wb.add_format({
            "bold": True, "font_size": 14, "bg_color": "#FFFFFF",
            "border": 1, "align": "center", "num_format": "#,##0.00",
        }),
        "kpi_value_pct": wb.add_format({
            "bold": True, "font_size": 14, "bg_color": "#FFFFFF",
            "border": 1, "align": "center", "num_format": "0.0%",
        }),
        "kpi_value_usd": wb.add_format({
            "bold": True, "font_size": 14, "bg_color": "#FFFFFF",
            "border": 1, "align": "center", "num_format": "$#,##0",
        }),
    }


def write_readme(ws, fmts, workbook_name, purpose, sheets, owner, cadence, sources):
    """Standard README sheet structure."""
    ws.set_column("A:A", 28)
    ws.set_column("B:B", 90)
    ws.set_row(0, 30)
    ws.merge_range("A1:B1", workbook_name, fmts["title"])
    row = 2
    ws.write(row, 0, "Purpose", fmts["row_header"])
    ws.write(row, 1, purpose, fmts["note"])
    row += 2
    ws.write(row, 0, "Sheets in this workbook", fmts["h2"])
    row += 1
    for name, desc in sheets:
        ws.write(row, 0, name, fmts["row_header"])
        ws.write(row, 1, desc, fmts["note"])
        row += 1
    row += 1
    ws.write(row, 0, "Owner", fmts["row_header"])
    ws.write(row, 1, owner, fmts["note"])
    row += 1
    ws.write(row, 0, "Update cadence", fmts["row_header"])
    ws.write(row, 1, cadence, fmts["note"])
    row += 1
    ws.write(row, 0, "Living-plan discipline", fmts["row_header"])
    ws.write(row, 1,
        "All yellow cells are user-editable inputs. White cells are formulas — do not overwrite. "
        "Refresh inputs on the cadence above. Any variance >10% versus plan triggers a re-plan "
        "loop per skills/meta-living-plan-governance.",
        fmts["note"])
    row += 1
    ws.write(row, 0, "Sources / methodology", fmts["row_header"])
    ws.write(row, 1, sources, fmts["note"])
    row += 2
    ws.write(row, 0, "Currency convention", fmts["row_header"])
    ws.write(row, 1,
        "All inputs in USD. Use FX cell on Inputs sheet to display local-currency equivalents "
        "(UGX, KES, NGN, ZAR, EGP). Mobile-money (M-Pesa / MoMo) and card-rail fees enter as % of revenue.",
        fmts["note"])


def write_africa_notes(ws, fmts, extra_notes=None):
    """Standard Africa-Notes sheet content. `extra_notes` is a list of (heading, body) tuples."""
    ws.set_column("A:A", 32)
    ws.set_column("B:B", 95)
    ws.set_row(0, 30)
    ws.merge_range("A1:B1", "Africa-Specific Adjustments & Notes", fmts["africa_header"])
    notes = [
        ("FX Pass-Through",
         "USD-denominated cloud (AWS/Azure/GCP), AI APIs, and SaaS tooling sit against UGX/KES/NGN/ZAR/EGP "
         "revenue. Adjust gross-margin benchmarks 5–10pp downward vs US comps. Hold an FX rate on Inputs and "
         "stress it ±15% in the sensitivity tab."),
        ("M-Pesa Payment Rail (Kenya, Tanzania)",
         "Typical fee 1.0–1.5% per transaction. STK-Push timeout failures generate involuntary churn — model "
         "3-retry dunning over 7 days; recovery typically 30–50%. Track separately from voluntary churn."),
        ("MoMo (MTN / Airtel — Uganda, Ghana, Rwanda, Nigeria)",
         "Fee band 1.5–2.0% per transaction. PIN-failure and float-shortage produce 4–6% annual involuntary churn "
         "vs <1% US card rails. Best-practice: integrate two rails (MoMo + card) and route based on tier."),
        ("Card Rails (Flutterwave / Paystack / Stripe)",
         "Card fees 2.9–3.8% + fixed. Card-decline rate 8–15% on first attempt for African issuing banks. "
         "Use Account-Updater services where available."),
        ("USD-Enterprise Tier",
         "Charge Enterprise customers (>$1k MRR) in USD invoiced via local entity or offshore SPV to hedge FX. "
         "Carries through to the Multi-Step P&L as a separate revenue stream. Recommended for 30–60% of total ARR by Y3."),
        ("Longer Collection Cycles",
         "Enterprise/public-sector DSO in Africa: 60–120 days (vs 30–45 US). Working-capital trough is deeper. "
         "Buffer trough at 9 months of opex vs the US 6-month standard."),
        ("Annual Prepayment Uptake",
         "African SaaS: 20–40% of new contracts pay annually (vs 60–80% US enterprise). Discount typically 10–15%. "
         "Model deferred revenue accordingly — do not assume US prepayment economics."),
        ("Sales-Cycle Length",
         "African mid-market sales cycle: 90–180 days. Enterprise: 6–18 months including procurement / public-sector "
         "RFP loops. CAC-payback benchmarks: relax US targets by 50–100%: <18 (SMB), <24 (Mid), <36 (Ent)."),
        ("AI Cost Hedging",
         "LLM APIs are USD-priced. Hedge via (a) USD-priced AI premium tier, (b) per-tenant usage caps, "
         "(c) open-source model fallback (Llama-class on Bedrock/Together). The AI-cost calculator workbook models all three."),
        ("DFI / Local-Bank Reporting",
         "Banks (Stanbic, Equity, KCB, Centenary) and DFIs (FMO, Norfund, Proparco, IFC) require local-currency "
         "primary view + USD parallel view. Build the model in USD here; toggle the FX row on Inputs for local presentation."),
        ("Rule-of-40 Calibration",
         "Adjust to target 30 for years 1–3 of African SaaS (vs US 40). Aim for 40 by Year 4 once vertical S&M is unlocked."),
    ]
    if extra_notes:
        notes.extend(extra_notes)
    row = 2
    for heading, body in notes:
        ws.write(row, 0, heading, fmts["row_header"])
        ws.write(row, 1, body, fmts["africa_note"])
        ws.set_row(row, 60)
        row += 1


def add_named(wb, name, ref):
    """Define a workbook-level named range. ref like 'Inputs!$B$5'."""
    wb.define_name(name, "=" + ref)
