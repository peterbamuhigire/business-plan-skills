# Completion Blueprint — McKinsey/Bain Readiness Enhancements
**Date:** 18 March 2026

This blueprint converts every gap identified across Pillars 1–6 into a prioritised, dependency-ordered enhancement roadmap. Items are grouped by phase and rated by: Impact (H/M/L) × Effort (S=hours, M=1 day, L=2-3 days, XL=week+).

---

## Scoring Summary

| Phase | Items | Combined Impact | Effort |
|-------|-------|----------------|--------|
| Phase 1 — Critical Gaps | 4 | HIGH | M-L each |
| Phase 2 — Important Gaps | 8 | MEDIUM-HIGH | S-M each |
| Phase 3 — Quality Refinements | 9 | MEDIUM | S each |
| Phase 4 — Specialist Additions | 6 | LOW-MEDIUM | M each |

---

## Phase 1 — Critical Gaps (Do These First)

These four items have the highest impact on plan quality relative to McKinsey/Bain standards. Each can be implemented independently.

### P1-A: Primary Research Protocol (HIGHEST PRIORITY)

**Impact:** HIGH — affects every market-facing section (04, 05, 06, 07)
**Effort:** L (2-3 days — substantive content to write)
**Creates:** `meta-market-validation/references/primary-research-protocol.md`

Contents to write:
1. When primary research is mandatory (decision tree): TAM validation, SOM feasibility, pricing, competitor intelligence
2. Expert interview protocol — 15-question structured discussion guide template
3. Customer discovery interview guide — 20 questions (Blank & Dorf + Alam)
4. Survey design standards — Likert, NPS, Van Westendorp Price Sensitivity Meter
5. Sample size guidelines (qualitative: 10-20 interviews for saturation; quantitative: 100+ for significance)
6. Mystery shopping / price survey template
7. Supplier quotation checklist (for COGS validation)
8. Triangulation protocol — reconciling conflicting sources
9. Data Confidence Assessment table template
10. LOI/MOU process for converting customer intent to evidence

**Skills to update:** `meta-market-validation/SKILL.md` — add mandatory Step 0 referencing this protocol

---

### P1-B: Working Capital Cycle Modelling (HIGH PRIORITY)

**Impact:** HIGH — the primary failure mode for profitable-but-cash-strapped SMEs
**Effort:** M (1 day)
**Creates:** `10-financial-projections/references/working-capital-modelling.md`

Contents to write:
1. DSO/DIO/DPO definitions and Cash Conversion Cycle formula
2. Uganda/EA industry benchmarks for DSO by customer type (government: 90-180 days; corporate: 30-60; retail: 0)
3. Working capital requirement formula: (CCC/365) × Annual Revenue
4. Inventory financing options in Uganda (Bank of Uganda, invoice discounting, supply chain finance)
5. CCC sensitivity analysis table — impact of DSO change on working capital requirement
6. Cash adequacy gate: base case cash flow must never go negative

**Skills to update:** `10-financial-projections/SKILL.md` — add working capital model as mandatory step before finalising cash flow projections

---

### P1-C: Issue Tree Construction as Mandatory Pre-Draft Step (HIGH PRIORITY)

**Impact:** HIGH — changes the analytical discipline of plan drafting
**Effort:** S (half day — protocol addition to existing skill)
**Updates:** `meta-market-validation/SKILL.md` and `06-competitive-analysis/SKILL.md`

Additions:
1. Step 0 in `meta-market-validation` — Issue Tree Protocol before any analysis begins
2. Competitive Hypothesis Statement template in `06-competitive-analysis` (must draft before describing competitors)
3. Four questions: (1) Central funder question? (2) 3-5 MECE sub-questions? (3) Hypothesis per sub-question? (4) Evidence available?

---

### P1-D: Sensitivity Analysis Enhancement (HIGH PRIORITY)

**Impact:** HIGH — without this, financial projections lack credibility with sophisticated funders
**Effort:** M (1 day — enhance existing reference file)
**Updates:** `meta-financial-stress-test/references/stress-test-methodology.md`

Additions:
1. Tornado chart construction protocol (rank key drivers by NPV/DSCR sensitivity)
2. Two-way sensitivity table templates (price × volume; revenue × cost)
3. Standardised scenario definitions with explicit % deviations (pessimistic = -20% revenue, +15% COGS, +10% opex)
4. DSCR sensitivity corridor (state explicitly: revenue can fall X% before DSCR breaches 1.25x)
5. Break-even sensitivity: minimum revenue required at given cost structure

---

## Phase 2 — Important Gaps (Do These Second)

### P2-A: Customer Analytics Reference File

**Impact:** MEDIUM-HIGH — critical for retail, subscription, services businesses
**Effort:** L (2-3 days)
**Creates:** `05-target-market/references/customer-analytics.md`

Contents: RFM segmentation, cohort retention curves, churn rate modelling, Van Westendorp PSM, NPS methodology, CAC by channel, customer concentration risk, customer lifetime stages

**Skills to update:** `05-target-market/SKILL.md`, `07-marketing-sales-strategy/SKILL.md`, `10-financial-projections/SKILL.md`

---

### P2-B: Competitive Data Gathering Protocol

**Impact:** MEDIUM-HIGH — transforms competitive analysis from framework application to evidence-based assessment
**Effort:** M (1 day)
**Creates:** `06-competitive-analysis/references/competitive-data-gathering.md`

Contents: Mystery shopping protocol (food/retail/services variants), competitive price survey template, Uganda/EA public intelligence sources (URSB, KCCA, UMA, UEPB, NEMA), Five Forces quantification scoring, competitor vulnerability map, competitive response war-gaming

**Skills to update:** `06-competitive-analysis/SKILL.md` — add references and cross-link to OSINT framework in meta-due-diligence

---

### P2-C: Strategic Narrative and Plan Assembly Enhancement

**Impact:** MEDIUM-HIGH — improves plan coherence for sophisticated funders
**Effort:** M (1 day)
**Updates:** `00-plan-assembly/SKILL.md`

Additions:
1. One-page strategy statement template (Problem → Solution → Why Us → How → Proof → Ask)
2. Extended logical coherence checklist (market size ↔ revenue; competitive advantage ↔ marketing; team skills ↔ operations; risk mitigations ↔ implementation timeline)
3. Mandatory Quality Gate Checklist referencing all meta-skills with go/no-go criteria
4. Optional Lafley & Martin Strategy Cascade framing for PE/DFI audiences

---

### P2-D: Quality of Earnings Protocol

**Impact:** MEDIUM-HIGH — required for any business with historical financials
**Effort:** M (1 day)
**Creates:** `meta-due-diligence/references/quality-of-earnings.md` (or enhance Howson reference)

Contents: QoE normalisation steps, EBITDA bridge (reported → normalised), non-recurring revenue identification, off-balance-sheet liabilities, owner perks adjustment, working capital normalisation

**Skills to update:** `10-financial-projections/SKILL.md` — add QoE normalisation as mandatory step for businesses with >2 years history

---

### P2-E: Ansoff Growth Matrix Integration

**Impact:** MEDIUM-HIGH — standard tool in every growth strategy discussion; simple to add
**Effort:** S (2-3 hours)
**Updates:** `03-products-services/SKILL.md` or `07-marketing-sales-strategy/SKILL.md`

Addition: Ansoff 2×2 (existing/new products × existing/new markets) with strategic implications table, risk profile of each quadrant, EA applicability examples

---

### P2-F: Devil's Advocate Protocol

**Impact:** MEDIUM — distinguishes consulting-grade analysis from advocacy
**Effort:** S (half day)
**Updates:** `meta-market-validation/SKILL.md`

Addition: Three-step competing hypotheses protocol — state three strongest arguments against the business, test each with evidence, resolve in plan

---

### P2-G: Cohort Unit Economics Module

**Impact:** MEDIUM — critical for investor-grade revenue analysis
**Effort:** M (1 day)
**Creates:** `10-financial-projections/references/cohort-unit-economics.md`

Contents: Cohort retention table template, LTV from cohort curves methodology, payback period per cohort, EA industry benchmark retention rates, Magic Number (expansion revenue efficiency), churn rate modelling

**Skills to update:** `10-financial-projections/SKILL.md`

---

### P2-H: UNDP Profile Age Adjustment Methodology

**Impact:** MEDIUM — some profiles are 2013-2018 vintage; significant cost changes since
**Effort:** S (half day)
**Updates:** Add note to each major industry guide (food-processing, livestock, manufacturing)

Contents: Standardised 2018→2026 escalation factors: construction ×1.35, equipment ×1.20, wages ×1.25 for Kampala. Methodology: apply Consumer Price Index from UBOS; construction cost index from Bank of Uganda.

---

## Phase 3 — Quality Refinements (Do These Third)

These are lower-effort improvements that meaningfully raise quality but are less critical than Phase 1-2 items.

| # | Action | File to Update | Effort |
|---|--------|----------------|--------|
| P3-A | Add So-What Test to Quality Criteria in all 15 core SKILL.md files | 15 SKILL.md files | S (systematic) |
| P3-B | Add Data Confidence Assessment table to 04, 05, 06 SKILL.md | 3 files | S |
| P3-C | Add Five Forces quantification scoring to 06-competitive-analysis | 06-competitive-analysis/SKILL.md | S |
| P3-D | Add competitive response protocol (war-gaming) to 12-risk-analysis | 12-risk-analysis/SKILL.md | S |
| P3-E | Add NPS framework to 05-target-market | 05-target-market/SKILL.md | S |
| P3-F | Cross-reference OSINT framework into 06-competitive-analysis | 06-competitive-analysis/SKILL.md | S |
| P3-G | Add capital structure optimisation to 11-funding-request | 11-funding-request/SKILL.md | S |
| P3-H | Add market penetration sanity check to 04-market-analysis | 04-market-analysis/SKILL.md | S |
| P3-I | Add competitor vulnerability map protocol to 06-competitive-analysis | 06-competitive-analysis/SKILL.md | S |

---

## Phase 4 — Specialist Additions (Do These When Demand Warrants)

Lower priority — these add sophistication for specific use cases (PE, DFI, manufacturing, tech) rather than all-business improvements.

| # | Enhancement | Creates | Target Audience |
|---|------------|---------|----------------|
| P4-A | McKinsey 7-S Framework for organisational alignment | `09-management-team/references/` | DFI governance, large organisations |
| P4-B | Real Options Analysis for stage-gate investments | `11-funding-request/references/` | Manufacturing, mining, infrastructure |
| P4-C | EVA (Economic Value Added) framework | `10-financial-projections/references/` | PE investors, DFI capital deployment |
| P4-D | Jobs-to-Be-Done framework (Christensen) | `05-target-market/references/` | Innovation-led businesses |
| P4-E | Financial benchmarks by EA industry (EBITDA margins, ROCE, working capital ratios) | Each major industry guide | All plan types |
| P4-F | Digital Maturity Assessment framework | `14-ai-integration/references/` | Digital transformation businesses |

---

## Implementation Sequence

```
Week 1: P1-A (primary research protocol) + P1-B (working capital)
Week 2: P1-C (issue tree) + P1-D (sensitivity analysis) + P2-E (Ansoff)
Week 3: P2-A (customer analytics) + P2-B (competitive data gathering)
Week 4: P2-C (plan assembly) + P2-D (QoE) + P2-F (devil's advocate)
Week 5: P2-G (cohort unit economics) + P2-H (UNDP age adjustment)
Week 6: All Phase 3 refinements (systematic pass through all SKILL.md files)
Later:  Phase 4 specialist additions as demand warrants
```

---

## Expected Score After Full Implementation

| Pillar | Current | Post-Phase 1-2 | Post-Phase 3-4 |
|--------|---------|----------------|----------------|
| Framework coverage | 8.5/10 | 9.0/10 | 9.5/10 |
| Data and evidence | 6.5/10 | 8.5/10 | 9.0/10 |
| Financial modelling | 7.0/10 | 8.5/10 | 9.0/10 |
| Strategic synthesis | 7.5/10 | 8.5/10 | 9.0/10 |
| Customer analytics | 6.0/10 | 8.0/10 | 8.5/10 |
| Competitive intelligence | 7.0/10 | 8.5/10 | 9.0/10 |
| **Overall** | **7.4/10** | **8.7/10** | **9.2/10** |

Post-Phase 1-2 implementation would represent a system that is **genuinely McKinsey/Bain comparable** for East African business plan contexts — with the significant advantage of superior local regulatory depth, industry benchmarks, and bankability standards.

---

## What Will Always Remain Different from McKinsey

It is worth being honest about a structural difference that no amount of skill enhancement can fully bridge:

**McKinsey/Bain have:**
- Proprietary industry databases (Consumer Industry Surveys, B2B pulse data, etc.)
- Analyst teams that can spend 200 hours gathering primary data for a single engagement
- Client relationships that give access to competitor financial data through industry associations
- AI tools trained on thousands of prior engagement analyses

**This system's structural advantage in return:**
- Superior EA local context (no McKinsey toolkit has Uganda EFRIS or NIN/BRN gate built in)
- Speed: a skilled practitioner can produce a 95th-percentile plan in days rather than weeks
- Cost: accessible to SMEs and development partners, not only to entities that can pay McKinsey fees
- Bankability focus: Rogoff/CAMPARI/DSCR framing is more practically useful for commercial bank lending than McKinsey's equity-optimised framework

The system does not need to replace McKinsey. It needs to be credible enough that a plan generated by it would not be embarrassed in a McKinsey audit. Post-Phase 1-2, it will be.
