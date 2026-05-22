---
name: saas-unit-economics-and-cohort-model
description: Build the SaaS-specific unit economics and cohort retention model for a business plan — LTV, CAC, CAC payback, LTV:CAC, gross margin, NRR/GRR, Rule of 40, magic number, burn multiple, quick ratio, ARR waterfall, and cohort retention curves. Use whenever a SaaS / ICT plan requires Section 10 (Financial Projections) to be bankable and investor-grade. Replaces the generic financial-projections workflow for SaaS plans.
---

# SaaS Unit Economics & Cohort Model Skill

## Overview

Produce the SaaS-specific unit economics and cohort exhibits that turn a generic financial model into a bankable, investor-grade SaaS plan. This skill is the operating discipline behind Section 10 for any SaaS plan; it should always be run together with `10-financial-projections` and the SaaS financial-projection template.

## Use When

- Section 10 of a SaaS / ICT plan is being built or reviewed
- An investor or DFI has asked for the unit economics, LTV:CAC, NRR, Rule of 40, or burn multiple
- A plan claims SaaS but does not yet have the canonical SaaS metrics
- A founder is making a pricing / packaging / growth decision and needs the unit-economic impact
- The plan needs to pass `meta-bankability-scoring` for SaaS investors

## Do Not Use When

- The business is not SaaS / subscription / recurring revenue (use `10-financial-projections` generic flow)
- The plan is pre-PMF and there's no meaningful customer data to model (run `saas-mvp-and-product-market-fit-strategy` first; this skill needs at least directional inputs)
- The plan is for a one-off services or grant deliverable (use `proposal-architect`)

## Required Inputs

- ARR / MRR (current or projected)
- ARPU by tier / segment
- New customer acquisition rate
- Monthly logo churn (gross)
- Monthly expansion rate
- S&M cost (fully loaded, including sales team + marketing + tools + allocated overhead)
- Hosting / infrastructure / customer-support / third-party-fee cost per customer
- Country context (FX, payment-rail fees, AI cost in USD)

## Workflow

1. **Compute the twelve core metrics** per `references/saas-unit-economics-model-template.md`: MRR, ARR, Net New ARR, Gross Margin (recurring), CAC, CAC Payback, LTV (three formulations), LTV:CAC, GRR, NRR, Magic Number, Rule of 40, Burn Multiple, Quick Ratio.
2. **Build the ARR waterfall** monthly for Year 1, quarterly for Years 2–5.
3. **Build the cohort retention matrix** — both logo cohort and revenue cohort. Compute the smile curve where data permits.
4. **Separate the involuntary-churn cohort** (Africa-specific discipline) so payment-rail issues are not conflated with product-fit issues.
5. **Compute cohort-driven LTV** per `references/saas-cohort-and-retention-model-template.md`.
6. **Benchmark against published SaaS benchmarks** (OpenView, KeyBanc, ChartMogul, ProfitWell). Adjust African benchmarks per the template's notes.
7. **Sensitivity-test** the unit economics: ±20% on churn, ±20% on ARPU, ±20% on CAC, ±20% on win-rate, +20% FX depreciation.
8. **Scenario-test** Base / Bear / Bull / Stress.
9. **Diagnose the binding constraint** — which lever (acquisition, retention, expansion, pricing) most improves the plan? This is the most useful output.
10. **Wire into living-plan governance** — assign cadence, owner, variance threshold, decision-log expectations per `meta-living-plan-governance`.

## Quality Bar

- All twelve metrics computed with explicit formulas and assumptions
- ARR waterfall mandatory and arithmetically consistent with customer-build tab
- Cohort retention matrix produced (or projected if pre-revenue)
- Smile curve test applied; if curve never turns upward, expansion strategy or LTV cap is disclosed
- Involuntary churn separated from voluntary churn
- Benchmarks cited; deviations explained
- Sensitivity and scenario analyses cover the binding constraints
- Plan-vs-actual variance protocol installed
- The CFO of a sceptical Series A investor would not laugh

## Anti-Patterns

- Aggregate churn rate without cohort breakdown
- LTV computed without gross-margin adjustment
- CAC computed from marketing spend only (no sales-team comp)
- Using US benchmarks without African adjustment
- Conflating voluntary and involuntary churn
- "We'll achieve 120% NRR by year 3" without expansion mechanic specified
- Magic Number > 2 in a market with no proven channel — fantasy

## Outputs

- Unit economics dashboard (Mersch format)
- ARR waterfall (monthly Y1, quarterly Y2–5)
- Cohort retention matrix (logo + revenue)
- Involuntary-churn cohort (Africa contexts)
- Sensitivity + scenario analyses
- Diagnosis of binding constraint
- Living-plan cadence assignment

## References

- `references/saas-unit-economics-model-template.md` — formulas, benchmarks, worked example (lives in `10-financial-projections/references/`)
- `references/saas-cohort-and-retention-model-template.md` — cohort matrix discipline
- `book-extractions/mersch-hacking-saas-extraction.md` — CFO-grade discipline
- `book-extractions/cotton-run-a-saas-business-extraction.md` — Rule of 40, churn, LTV:CAC rules
- `book-extractions/walling-saas-playbook-extraction.md` — 80/20 metrics chapter

## Living-Plan Cadence Defaults

| Metric | Cadence | Owner | Variance threshold |
|---|---|---|---|
| ARR / MRR | weekly | CFO / Founder | ±15% triggers replan |
| Net New ARR | weekly | CFO | ±20% |
| Gross Margin | monthly | CFO | ±5pp |
| CAC | monthly | CFO + Head of GTM | ±20% |
| CAC Payback | monthly | CFO | >18 months alarm |
| LTV | quarterly | CFO | ±15% |
| Churn (gross) | weekly | Head of CS | ±0.5pp |
| NRR / GRR | monthly | Head of CS + CFO | ±10pp NRR |
| Magic Number | quarterly | CFO + Head of GTM | <0.75 alarm |
| Rule of 40 | quarterly | CFO | <30 alarm |
| Burn Multiple | monthly | CFO | >2.5 alarm |
| Cohort retention | monthly | CFO + Head of CS | new cohort >5pp worse |

## Africa / Uganda Application Notes

- Adjust African benchmarks: gross margin -5 to -10pp, CAC payback +50–100%, Rule of 40 target 30 in years 1–3 acceptable.
- Always separate involuntary churn; African payment rails fail 3–6% annually.
- Track all metrics in **local currency for DFI/bank presentations** and USD for international investors.
- AI cost per tenant is a real cost line and is FX-exposed; model explicitly.
