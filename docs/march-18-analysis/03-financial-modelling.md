# Pillar 3 — Financial Modelling Rigour
**Score: 7.0 / 10**

The foundation is solid — Rogoff bankability standards, CAMPARI, Damodaran valuation, financial model templates for Uganda. The gap to McKinsey/Bain level is in three specific areas: working capital cycle modelling, sensitivity/scenario analysis methodology, and unit economics at cohort granularity. These are not conceptually hard to add — they require methodology files, not framework redesign.

---

## 3.1 Current Financial Modelling Strengths

### What Is Already Consulting-Grade

| Component | Location | Assessment |
|-----------|----------|------------|
| **DSCR ≥1.25x** | 10-financial-projections, 11-funding-request | Correctly specified; correctly applied to bank loan mode |
| **Collateral coverage ≥125%** | meta-bankability-scoring, 11-funding-request | Integrated into CAMPARI checklist |
| **CAMPARI 28-item checklist** | meta-bankability-scoring | Excellent — more rigorous than most bank templates themselves |
| **Damodaran DCF/WACC/CAPM** | 11-funding-request/business-valuation-methods.md | Full treatment including CRP 4-6% for Uganda, illiquidity discount 25-35% |
| **Revenue multiples** | business-valuation-methods.md | P/E, EV/EBITDA, EV/Revenue, PEG, P/Book — Valuation Method Selector table |
| **Morlidge forecast/budget distinction** | 10-financial-projections | Critical distinction: forecast ≠ target ≠ plan |
| **Startup metrics** | 10-financial-projections | Burn rate, runway, LTV:CAC >3:1 |
| **Driver-based modelling principle** | 10-financial-projections | Correct — financial projections derive from business drivers not from "excel feels" |
| **Uganda tax framework** | uganda-tax-framework.md | ITA Cap.340 with 2025 amendments, all PAYE bands, WHT, EFRIS |
| **Financial model templates** | financial-model-templates.md | Monthly P&L, cash flow, balance sheet — Uganda-compliant |
| **4-scenario stress test** | meta-financial-stress-test | Base/Optimistic/Pessimistic/Extreme + DSCR stress + Early Warning Dashboard |
| **Informal business record reconstruction** | informal-business-records.md | Mobile money reconstruction, lender acceptance table — genuinely innovative |
| **Pre-revenue valuation methods** | business-valuation-methods.md | VC method, angel scoring method (Berkus) |

---

## 3.2 Critical Gaps in Financial Modelling

### Gap 1 — Working Capital Cycle Modelling (HIGH IMPACT)

**What McKinsey does:** Every financial model starts with an explicit working capital model:
- Days Sales Outstanding (DSO): how many days before customers pay
- Days Inventory Outstanding (DIO): how many days of stock held
- Days Payable Outstanding (DPO): how many days before suppliers are paid
- Cash Conversion Cycle (CCC) = DSO + DIO − DPO

This drives the **cash flow funding requirement** which is typically the primary cause of SME failure in Uganda (profitable but cash-strapped).

**What the suite currently has:** Monthly cash flow template exists in `financial-model-templates.md`. Working capital is included as a line item but the CCC decomposition methodology is absent.

**Impact of gap:** Plans built without CCC analysis systematically underestimate the working capital funding requirement. A manufacturing business buying inputs on 30-day credit and selling to institutional buyers on 90-day terms has a 60-day CCC gap — this is frequently the difference between a viable and an unviable bank loan application.

**Recommendation:** Add `10-financial-projections/references/working-capital-modelling.md` covering:
- DSO/DIO/DPO definitions and Uganda industry benchmarks
- CCC calculation formula and interpretation
- Working capital requirement formula: (CCC/365) × Revenue
- Uganda-specific benchmarks: government tenders typically 90-180 days; supermarkets 30-60 days; cash retail 0 days
- Bank of Uganda guidance on trade finance instruments (invoice discounting, supply chain finance)

### Gap 2 — Sensitivity Analysis Methodology (HIGH IMPACT)

**What McKinsey does:** Consulting-grade financial models always include:
1. **One-way sensitivity tables** (tornado chart): which single driver has the largest impact on NPV/DSCR?
2. **Two-way sensitivity tables**: interaction between two key drivers (e.g., price × volume)
3. **Scenario analysis**: structured, named scenarios with narrative justification for each assumption set
4. **Monte Carlo** (for DFI proposals): probability distribution of outcomes

**What the suite currently has:** `meta-financial-stress-test` has 4 named scenarios (base/optimistic/pessimistic/extreme) with Uganda historical shock scenarios. This is good. What is absent:
- Tornado chart methodology (ranking drivers by sensitivity impact)
- Two-way sensitivity table template
- Explicit % change thresholds for each scenario (what does "pessimistic" mean numerically?)
- DSCR sensitivity corridor (at what revenue decline does DSCR breach 1.25x?)

**Recommendation:** Enhance `meta-financial-stress-test/references/stress-test-methodology.md` with:
- Tornado chart construction protocol
- Two-way sensitivity table template (price × volume, revenue × cost)
- Standardised scenario definitions with explicit % deviations (pessimistic = -20% revenue, +15% COGS, etc.)
- Break-even sensitivity: minimum revenue required to maintain DSCR ≥1.25x

### Gap 3 — Unit Economics at Cohort Level (MEDIUM IMPACT)

**What McKinsey does:** For subscription, retail, and services businesses, the critical question is not aggregate LTV:CAC but cohort-level economics:
- Monthly cohort acquisition (e.g., 50 customers in Month 1)
- Cohort retention curve (Month 1: 100%, Month 2: 65%, Month 3: 52%…)
- Cohort revenue over time
- Break-even month per cohort
- Blended LTV across all cohorts

**What the suite currently has:** LTV:CAC >3:1 benchmark cited. No cohort modelling framework.

**Impact:** Aggregate LTV:CAC can look healthy while unit economics are deteriorating (early cohorts retained, recent cohorts churning fast). VCs and DFIs in growth-stage investments look specifically at cohort data.

**Recommendation:** Add a cohort economics section to `10-financial-projections/SKILL.md` with:
- Cohort retention table template
- LTV calculation from cohort curves (not from average revenue × average life)
- Payback period per cohort
- Magic Number (expansion revenue efficiency)

### Gap 4 — Quality of Earnings Analysis (MEDIUM IMPACT)

**What McKinsey/Howson M&A DD does:** For any business presenting historical financials, QoE analysis asks:
- Are revenues recurring or one-time?
- Are costs normalised (removing owner perks, one-time items)?
- What is the EBITDA bridge from reported to normalised?
- Are there off-balance-sheet liabilities (operating leases, contingent liabilities)?

**What the suite has:** `meta-due-diligence/references/due-diligence-ma-howson.md` covers QoE in M&A context. But the *plan generation skills* do not require presenters to normalise their historical financials before projections.

**Recommendation:** Add a QoE normalisation protocol to `10-financial-projections/SKILL.md` — a mandatory step for any business with >2 years of historical data before projections are built.

### Gap 5 — Capital Structure Optimisation (LOW-MEDIUM IMPACT)

**What McKinsey does:** The funding request section should demonstrate that the capital structure (debt/equity split) is optimal given:
- Cost of equity vs. cost of debt (WACC minimisation)
- Debt capacity (DSCR-constrained maximum debt)
- Tax shield value (interest deductibility — 30% Uganda corporate tax)
- Optimal leverage ratio by industry and growth stage

**What the suite has:** DSCR-constrained debt sizing in `11-funding-request`. Use-of-funds alignment. But no explicit WACC optimisation framework for the specific business.

**Recommendation:** Add a capital structure optimisation section to `11-funding-request/SKILL.md` — a 5-step decision tree: (1) calculate DSCR-constrained max debt, (2) estimate cost of equity (CAPM), (3) calculate WACC at different debt/equity ratios, (4) identify WACC-minimising leverage, (5) reconcile with funder preference.

---

## 3.3 Financial Modelling Quality Gates

### Current Gates (What Exists)
- CAMPARI 28-item checklist (meta-bankability-scoring) — applied post-completion
- Consistency audit (12-point) — cross-section checks
- DSCR ≥1.25x — explicit threshold enforced
- 4-scenario stress test — invocable but not mandatory

### Missing Gates (What McKinsey Would Require)

| Gate | Description | When Applied |
|------|-------------|--------------|
| **Cash adequacy gate** | Cash balance never goes negative in base case cash flow | Before any projection is submitted |
| **CCC reasonableness gate** | Working capital assumption benchmarked against industry | After projections drafted |
| **Sensitivity corridor gate** | Revenue can decline X% before DSCR breaches 1.25x; X must be documented | Before bank submission |
| **Tax reconciliation gate** | Tax charge in P&L reconciles to Uganda ITA rates (PAYE, corporate, VAT) | Before finalisation |
| **Assumptions transparency gate** | Every projection line has a named driver with a stated assumption | Before any funder sees the model |

---

## 3.4 Industry-Specific Financial Benchmarking

### What Is Present

The industry guides contain financial benchmarks — startup costs, revenue estimates, cost structures — from UNDP profiles. This is genuinely valuable and better than anything most consultants have for East Africa.

### What Is Missing: Margin and Return Benchmarks

McKinsey analysts benchmark EBITDA margins, ROCE, and working capital ratios against comparables. The current suite provides:
- Startup cost ranges (UNDP profiles) ✅
- Revenue estimates (ranges) ✅
- Employee counts (ranges) ✅

But is missing:
- **EBITDA margins by industry** (e.g., food processing typically 8-15%; retail 4-8%; services 15-35%)
- **ROCE benchmarks** (return on capital employed)
- **Inventory turnover by sector** (linked to CCC modelling)
- **Receivables days by customer type** (government vs. corporate vs. retail)

**Recommendation:** Add a `financial-benchmarks-ea.md` reference to each major industry guide with:
- EBITDA margin range (source: Damodaran industry data, regional DFI reports)
- ROCE benchmark
- Working capital benchmarks (DSO, DIO, DPO by customer type)
- Growth rate benchmarks for EA comparable businesses

---

## 3.5 Recommended New Reference Files

| File | Location | Priority |
|------|----------|---------|
| `working-capital-modelling.md` | `10-financial-projections/references/` | **HIGH** |
| Enhanced sensitivity table templates | `meta-financial-stress-test/references/stress-test-methodology.md` (update) | **HIGH** |
| `cohort-unit-economics.md` | `10-financial-projections/references/` | MEDIUM |
| `quality-of-earnings.md` | `meta-due-diligence/references/` | MEDIUM |
| `capital-structure-optimisation.md` | `11-funding-request/references/` | MEDIUM |
| `financial-benchmarks-ea.md` per industry | Each major industry guide | MEDIUM |
