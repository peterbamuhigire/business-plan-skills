# SaaS Financial Models — Master README

This engine ships **five working Excel financial models** for ICT/SaaS startups operating in Africa (Uganda primary, Kenya/Nigeria/South Africa/Egypt/Rwanda extendable). They are usable today for investor conversations, lender presentations, grant applications, and quarterly board packs.

All workbooks share design conventions:
- **Yellow cells** = user-editable inputs.
- **White cells** = formulas — do not overwrite.
- **Green/Yellow/Red traffic lights** = conditional formatting on bankability metrics.
- **Named ranges** for all major inputs (`ARPA_P`, `Logo_Churn`, `GM_P`, `Net_New_ARR`, `Blended_CAC`, ...).
- **USD as base currency**, with an `FX` row on Inputs for local-currency display (UGX / KES / NGN / ZAR / EGP).
- **Africa-Notes sheet** in every workbook — FX, M-Pesa, MoMo, USD-Enterprise tier, longer collection cycles.
- **README sheet** in every workbook — purpose, sheets, owner, cadence.

Regenerate any workbook from `scripts/build-financial-models/` (xlsxwriter 3.2.9).

---

## 1. Unit Economics Model
**Path:** `skills/saas-unit-economics-and-cohort-model/templates/saas-unit-economics-model.xlsx`
**Build script:** `scripts/build-financial-models/build_unit_economics.py`
**Sheets (6):** README · Inputs · Calc · Cohort · Dashboard · Africa-Notes

The canonical 12-metric SaaS unit-economics dashboard for a single steady-state period. Computes:
- Blended ARPA, ACV, Gross Margin
- LTV in three formulations (simple, GM-adjusted, expansion-adjusted with NRR cap)
- Blended CAC across paid / inbound / outbound / partner channels
- CAC Payback, LTV:CAC, GRR, NRR, Magic Number, Rule of 40, Burn Multiple, Quick Ratio
- 24-month logo + revenue cohort matrices for 6 illustrative cohorts (heat-mapped)

**Living-plan cadence:** Monthly refresh of Inputs from billing system. Quarterly benchmark review.

---

## 2. Cohort & Retention Model
**Path:** `skills/saas-unit-economics-and-cohort-model/templates/saas-cohort-and-retention-model.xlsx`
**Build script:** `scripts/build-financial-models/build_cohort_retention.py`
**Sheets (8):** README · Inputs · Logo-Cohort · Revenue-Cohort · NRR-GRR · Involuntary-Churn · Dashboard · Africa-Notes

36-month formula-driven cohort matrices for 12 monthly cohorts:
- Tenure-decay churn: `churn(t) = MAX(floor, base × decay^t)`
- Revenue cohorts include expansion compounding (smile-curve test)
- Separate **Involuntary-Churn** sheet by African payment rail (M-Pesa / MoMo / Card / Bank-transfer) with dunning-recoverable vs hard-lost split

**Living-plan cadence:** Monthly cohort refresh from billing system; quarterly QBR slide.

---

## 3. Financial Projection (3-yr / 5-yr, 60 months)
**Path:** `skills/10-financial-projections/templates/saas-financial-projection-3yr-5yr.xlsx`
**Build script:** `scripts/build-financial-models/build_financial_projection.py`
**Sheets (11):** README · Inputs · ARR-Waterfall · MRR-Detail · Headcount · PnL · Cash · Sensitivity · Scenarios · Bankability-Dashboard · Africa-Notes

Implements:
- **60-month ARR Waterfall** (opening + new + expansion − contraction − churn = closing)
- **MRR-Detail** by tier with reconciliation to ARR (Δ check row)
- **Quarterly Headcount** by role with loaded-cost rollup
- **Multi-Step P&L** in Mersch format (Rev → COGS → GP → S&M → R&D → G&A → Op Inc → +D&A +SBC → EBITDA → Tax → NI)
- **Cash** with 60-month running balance and **working-capital trough** flagging
- **2-D Sensitivity**: new-logo growth × churn → Year-3 ending ARR
- **Scenario toggle** on Inputs cell — Base / Bull / Bear / Stress drive `Scen_Active` multipliers (logos × churn × ARPA × FX)
- **Bankability-Dashboard**: Rule of 40, LTV:CAC, CAC Payback, NRR, Burn Multiple, Magic Number, Quick Ratio with traffic lights + ARR / Cash / Revenue-vs-Opex charts

**Living-plan cadence:** Monthly actuals against plan; quarterly re-forecast next 4 quarters; annual roll-forward.

---

## 4. AI Cost-of-Tenant Calculator
**Path:** `skills/14-ai-integration/templates/saas-ai-cost-of-tenant-calculator.xlsx`
**Build script:** `scripts/build-financial-models/build_ai_cost_tenant.py`
**Sheets (8):** README · Inputs · Cost-Per-Tenant · Margin-Analysis · Sensitivity · Stress-Test · Dashboard · Africa-Notes

Per-tenant LLM economics across three tiers:
- **Free**: Llama-class default ($0.0001/k input)
- **Pro**: GPT-4o-mini-class ($0.00015/k input)
- **Enterprise**: GPT-4o / Claude-Sonnet class ($0.0025/k input)

Components: token cost (input + output), eval overhead, retraining (amortised), vector store, RAG retrieval, observability, S&M attribution, other COGS, markup ceiling.

- **Cost-Per-Tenant** computes monthly cost by tier with full component decomposition.
- **Margin-Analysis** produces AI GM%, contribution margin, "above cost ceiling" flag.
- **Sensitivity** has two 2-D tables: tokens-per-prompt × $/1k; prompts/day × users/tenant.
- **Stress-Test** waterfall: +50/+100/+200% tokens; 2× usage; retraining 2×; eval 2×; model deprecation (price 1.5×).

**Living-plan cadence:** Monthly when LLM pricing changes; quarterly for usage assumptions; before each pricing/packaging change.

---

## 5. Living-Plan KPI Dashboard (Monthly)
**Path:** `skills/meta-living-plan-governance/templates/saas-living-plan-kpi-dashboard.xlsx`
**Build script:** `scripts/build-financial-models/build_living_plan_dashboard.py`
**Sheets (5):** README · Monthly-Inputs · KPI-Dashboard · Variance-Tracker · Africa-Notes

24-month rolling dashboard. Paste actuals into Monthly-Inputs; the workbook computes:
- MRR / ARR / MoM / YoY
- Logo churn rate, Expansion rate
- NRR (annual rolling), GRR (annual rolling)
- Magic Number (3-mo trailing), CAC Payback, LTV:CAC, Quick Ratio
- Burn Multiple (3-mo), Rule of 40 (trailing 12-mo)

**Variance-Tracker** computes plan-vs-actual % deviation across 6 metrics; any deviation > variance-threshold (default 10%) raises a **REPLAN** flag — links back to `skills/meta-living-plan-governance` variance protocol.

**Living-plan cadence:** Monthly close + 5 working days. Variance review same day as close.

---

## How the Five Workbooks Interlink

```
   ┌──────────────────────┐
   │ Unit Economics Model │ ─── feeds ───┐
   └──────────────────────┘              │
                                         ▼
   ┌──────────────────────┐    ┌────────────────────────────────┐
   │ Cohort & Retention    │ →  │ Financial Projection 3yr/5yr  │
   │   Model              │    │  (60-month master model)       │
   └──────────────────────┘    └────────────────────────────────┘
                                         ▲
   ┌──────────────────────┐              │
   │ AI Cost-of-Tenant     │ ─── feeds ──┘
   │   Calculator         │      (COGS %, Enterprise pricing)
   └──────────────────────┘

   ┌─────────────────────────────────────┐
   │ Living-Plan KPI Dashboard (monthly) │
   │ ingests actuals → flags variance    │
   │ → triggers replan loop              │
   └─────────────────────────────────────┘
```

Specifically:
- **Unit Economics** outputs (ARPA, GM, Logo Churn, NRR, CAC) → paste into **Projection Inputs** sections 1–4 and 8.
- **Cohort & Retention** outputs (involuntary churn by rail, dunning recovery) → paste into **Projection Inputs** section 3 (use blended logo + involuntary).
- **AI Cost-of-Tenant** outputs (AI cost % of revenue for Enterprise tier) → paste into **Projection Inputs** section 4 (COGS %).
- **Living-Plan KPI Dashboard** ingests monthly actuals; >10% variance vs plan flags REPLAN, which triggers updating the Projection inputs and re-running.

---

## Adoption Sequence by Funding Stage

| Stage | Workbooks needed | Notes |
|---|---|---|
| **Pre-seed / Friends & Family** | 1 (Unit Economics) + 3 (Projection at 3-yr depth) | Enough for SAFE / convertible-note conversation |
| **Seed** | 1 + 2 (Cohort once 6+ months of data) + 3 (5-yr) + 5 (Living-Plan) | Investor data room baseline |
| **Series A** | All 5 | AI-cost calculator becomes mandatory if LLM-backed product |
| **DFI / Bank lending** | 3 + 5 with parallel local-currency view | DFIs (FMO, Norfund, IFC, Proparco) expect this |
| **Grant proposals (Ugandan / DFI)** | 3 (M&E-augmented) + 5 | Pair with `skills/meta-monitoring-evaluation` |
| **Quarterly board pack** | 5 (Living-Plan) primary; 3 secondary | Variance-Tracker REPLAN flags drive agenda |

---

## Regenerating the Workbooks

```bash
cd C:/wamp64/www/business-plan-skills
python scripts/build-financial-models/build_unit_economics.py
python scripts/build-financial-models/build_cohort_retention.py
python scripts/build-financial-models/build_financial_projection.py
python scripts/build-financial-models/build_ai_cost_tenant.py
python scripts/build-financial-models/build_living_plan_dashboard.py
python scripts/build-financial-models/verify_workbooks.py
```

Each script is self-contained and idempotent — re-running overwrites the existing `.xlsx`.

---

## Verification

```
OK: skills/saas-unit-economics-and-cohort-model/templates/saas-unit-economics-model.xlsx       sheets=6
OK: skills/saas-unit-economics-and-cohort-model/templates/saas-cohort-and-retention-model.xlsx  sheets=8
OK: skills/10-financial-projections/templates/saas-financial-projection-3yr-5yr.xlsx           sheets=11
OK: skills/14-ai-integration/templates/saas-ai-cost-of-tenant-calculator.xlsx                  sheets=8
OK: skills/meta-living-plan-governance/templates/saas-living-plan-kpi-dashboard.xlsx           sheets=5
```

All workbooks: valid OOXML zip, expected sheet count, README + Inputs + Africa-Notes present.
