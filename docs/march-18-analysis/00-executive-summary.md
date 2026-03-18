# McKinsey/Bain Readiness Audit — Executive Summary
**Project:** Business Plan Skills Suite
**Date:** 18 March 2026
**Auditor:** Claude (Implementation Status Auditor — adapted for content/methodology suite)
**Prior audits:** `docs/implementation/review-12-Mar-2026/`, `docs/march-12-analysis/`

---

## Overall Readiness Score: 7.4 / 10

This is a genuinely strong system — far above the standard of any off-the-shelf business plan template. The infrastructure, localisation depth, and methodology breadth are legitimately consulting-grade. The gap to true McKinsey/Bain level is concentrated in four areas: **primary research rigour**, **quantitative depth of financial modelling**, **strategic synthesis discipline**, and **customer analytics sophistication**.

---

## Pillar Scores

| Pillar | Score | Assessment |
|--------|-------|------------|
| **1. Framework coverage and depth** | 8.5/10 | 50+ cited frameworks; Minto, Porter, Damodaran, COSO all present with full treatment |
| **2. Data quality and evidence standards** | 6.5/10 | Strong secondary sources; primary research protocol largely absent |
| **3. Financial modelling rigour** | 7.0/10 | Rogoff/CAMPARI/DSCR solid; unit economics and sensitivity analysis underdeveloped |
| **4. Strategic synthesis and narrative** | 7.5/10 | Pyramid Principle embedded; cross-section consistency audit exists; issue-tree practice thin |
| **5. Customer and market analytics** | 6.0/10 | TAM/SAM/SOM dual methodology strong; RFM, cohort, churn, price elasticity absent |
| **6. Competitive intelligence depth** | 7.0/10 | Porter Five Forces + Ohmae + differentiation strong; quantified benchmarking weak |
| **7. Operational and supply chain rigour** | 6.5/10 | BPM lifecycle solid; supply chain risk quantification and digital maturity assessment missing |
| **8. Local context and regulatory depth** | 9.5/10 | Best-in-class for EA; Uganda/Kenya/Tanzania complete; live metrics scraper; real regulations |
| **9. Communication and presentation** | 9.0/10 | Duarte Sparkline, Minto Pyramid, Klaff STRONG, McGowan Hook-Meat-Payoff — all fully implemented |
| **10. Quality gates and validation** | 7.5/10 | CAMPARI 28-item, consistency audit, stress-test, DD readiness scoring — good but not automated |

---

## Top 5 Critical Findings

### Finding 1 — Primary Research Protocol: Absent (High Impact)
The system assumes all market sizing comes from secondary sources. McKinsey/Bain always supplement with primary research — structured interviews, surveys, mystery shopping, price testing. No skill currently guides the analyst through designing and executing primary research. This is the single largest gap between the current system and consulting-grade output.

**Affected skills:** 04-market-analysis, 05-target-market, meta-market-validation

### Finding 2 — Quantitative Financial Modelling: Templates Exist, Methodology Thin (High Impact)
The `financial-model-templates.md` reference provides structure. But McKinsey-grade financial analysis requires explicit working capital cycle modelling (DSO/DIO/DPO → cash conversion cycle), Monte Carlo or structured sensitivity tables, and unit economics modelled at cohort level — not just aggregate LTV:CAC ratios. These are referenced but not operationalised as methodology the skill actively enforces.

**Affected skills:** 10-financial-projections, meta-financial-stress-test

### Finding 3 — Issue Tree Construction: Referenced but Not Practiced (Medium Impact)
McKinsey/Bain analysts build MECE issue trees before writing a single slide. The `mckinsey-problem-solving.md` reference covers this but the skill invocation flow does not require analysts to produce and validate an issue tree before drafting any plan section. This is a process gap, not a content gap.

**Affected skills:** meta-market-validation, 01-executive-summary, 06-competitive-analysis

### Finding 4 — Customer Analytics Depth: Surface-Level (Medium Impact)
AARRR funnel exists. CLV:CAC >3:1 benchmark exists. But RFM segmentation, cohort retention curves, churn modelling, customer acquisition cost by channel, and price elasticity testing are absent. These are standard tools in any Bain revenue growth study and are essential for subscription, retail, and services businesses.

**Affected skills:** 05-target-market, 07-marketing-sales-strategy

### Finding 5 — Competitive Benchmarking with Data: Framework Without Numbers (Medium Impact)
Porter Five Forces is fully implemented. Ohmae, differentiation, moats all present. But the competitive analysis skill does not guide the analyst through *gathering* competitor data — no protocol for revenue benchmarking from public sources, no mystery shopping template, no price survey methodology, no competitor financial ratio benchmarking (EBITDA margins by sector, ROCE benchmarks). The frameworks are applied but the data-gathering discipline that fills them is missing.

**Affected skills:** 06-competitive-analysis, meta-market-validation

---

## Top 3 Quick Wins (Highest ROI in <1 Week)

| # | Action | Affected Skills | Complexity |
|---|--------|----------------|-----------|
| 1 | Add primary research design protocol to meta-market-validation | meta-market-validation, 04, 05 | M |
| 2 | Add cash conversion cycle and working capital cycle to 10-financial-projections | 10-financial-projections | M |
| 3 | Add issue-tree construction checkpoint to meta-market-validation and 06-competitive-analysis | meta-market-validation, 06 | S |

---

## What Is Already World-Class

1. **Local regulatory depth** — EFRIS, NIN/BRN, EUDR, NEMA, Uganda tax framework; Kenya EU-EPA; Tanzania SGR — this is genuinely superior to what any consulting firm's generic toolkit contains. **No gap.**

2. **Bankability standards** — Rogoff DSCR ≥1.25x, CAMPARI 28-item, collateral ≥125%, DFI ESMP template. A Stanbic or Equity Bank credit committee would find the output professionally structured. **No gap.**

3. **Communication standards** — Minto Pyramid Principle (SCQA, three logical orders, 7 structural errors), Duarte Sparkline, Klaff STRONG, McGowan Hook-Meat-Payoff. The presentation layer is genuinely McKinsey-grade. **No gap.**

4. **Risk analysis** — COSO ERM, Bowtie, Raydugin 3-part uncertainty naming, Murray-Webster behavioural biases, Uganda regulatory risk table. Structured and sourced. **No gap.**

5. **Industry depth** — 200+ UNDP profiles, food/restaurant/retail/dairy/livestock all with cost structures and financial benchmarks. For EA, this is best-in-class. **No gap.**

---

## Files in This Analysis

| File | Contents |
|------|----------|
| `00-executive-summary.md` | This file — overall score, top findings, quick wins |
| `01-framework-depth.md` | Pillar 1 — methodology coverage vs. consulting benchmark |
| `02-data-and-evidence.md` | Pillar 2 — primary research gaps, secondary source quality |
| `03-financial-modelling.md` | Pillar 3 — financial rigour gaps and enhancement roadmap |
| `04-strategic-synthesis.md` | Pillar 4 — cross-section coherence, issue trees, narrative discipline |
| `05-customer-analytics.md` | Pillar 5 — RFM, cohort, churn, price elasticity gaps |
| `06-competitive-intelligence.md` | Pillar 6 — data-gathering protocols, benchmarking standards |
| `07-completion-blueprint.md` | Prioritised enhancement roadmap with complexity ratings |
