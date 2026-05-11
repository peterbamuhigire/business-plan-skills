---
name: saas-sales-org-design-and-capacity-planning
description: Design the SaaS sales organisation and produce the sales capacity model — quota, ramp, attainment, OTE, SDR:AE:CSM ratios, pod structure, hiring sequence by ARR milestone. Forces the financial-projection bookings line to reconcile with the headcount plan. Mandatory when ARR projection exceeds $1M.
---

# SaaS Sales Org Design & Capacity Planning Skill

## Overview

Convert ARR ambition into a reconcilable sales-org plan. Most SaaS plans project $5M ARR by Year 3 with two sales hires — mathematically impossible. This skill produces the canonical formula: **Bookings = #AEs × Quota × Attainment % × (1 − Ramp Discount)** and the org evolution by ARR milestone.

## Use When

- Section 09 (Management Team) or Section 10 (Financial Projections) is being built for a SaaS plan with target ARR > $1M
- The plan's sales-bookings line doesn't reconcile with the headcount plan
- The team is hiring its first VP of Sales / Head of Revenue
- An ARR milestone is approaching and the org needs to evolve

## Required Inputs

- Target ARR by year (Year 1, 2, 3, 5)
- Average ACV
- Sales-cycle length
- GTM motion (from `saas-gtm-motion-design`)
- Country context (African OTE benchmarks differ materially from US)

## Workflow

1. **Map ACV to AE archetype** — SMB AE ($500k-$1M quota), Mid-Market AE ($1-1.5M quota), Enterprise AE ($1-2M quota). African SaaS adjust quotas down 30–50% for local-currency-priced products.
2. **Compute capacity formula** — `Bookings = #AEs × Quota × Attainment × (1 − Ramp Discount)`. Use the worked formula in references.
3. **Solve for #AEs needed** to hit target ARR. If the number is implausible (40 AEs by Year 2), the plan must change motion, ACV, or target.
4. **Add SDR/BDR ratio** — typically 1 SDR per AE (outbound-heavy) or 1 SDR per 2-3 AEs (inbound-heavy).
5. **Add CSM ratio** — high-touch 1:25 customers; mid-touch 1:75; tech-touch 1:300.
6. **Add management ratio** — 1 sales manager per 5-8 AEs; VP Sales above 10 AEs.
7. **Add ops** — RevOps lead at $5M ARR; team at $15M ARR.
8. **Sequence the hiring** by ARR milestone (not calendar). Use the milestone table in references.
9. **Compute fully-loaded cost** including OTE, benefits, payroll tax, tools, allocated overhead.
10. **Reconcile with Section 10 financials** — sales-cost line must match.

## Quality Bar

- Capacity formula explicit and arithmetically reconciled with target ARR
- AE archetype matches ACV (no $5k ACV being sold by enterprise AEs)
- Ramp discount modelled (50% months 1-3, 75% months 4-6, 100% by month 9 for enterprise)
- Attainment rate realistic (60-70% of reps making quota is healthy; 90% suggests under-quota)
- SDR:AE, CSM:Customer ratios specified
- Hiring sequenced by ARR milestone with explicit triggers
- Africa-adjusted OTE and quota

## Anti-Patterns

- "We'll hire a VP Sales and they'll figure it out"
- Bookings target with no capacity model
- 100% attainment assumption
- No ramp discount on new hires
- Enterprise AE selling SMB volume
- Single AE — Cotton's rule: never build a sales team with one rep

## Outputs

- Capacity model spreadsheet (or table for early plans)
- Org chart by ARR milestone
- Hiring sequence with triggers
- Fully-loaded cost roll-up (feeds Section 10)
- Comp plan outline (base / variable / accelerators / SPIFs)

## References

- `references/saas-sales-capacity-and-ramp-model.md` — full capacity formulas and worked examples
- `book-extractions/vanderkooij-saas-sales-method-ae-extraction.md` — methodology to ACV mapping
- `book-extractions/cotton-run-a-saas-business-extraction.md` — Rule of 3 and 10
- `book-extractions/mersch-hacking-saas-extraction.md` — S&M as % of revenue benchmarks

## Africa / Uganda Application Notes

- AE OTE in African markets: $15-30k (SMB), $25-50k (mid), $40-80k (enterprise) — vs US $80k/$150k/$300k.
- Quotas scale proportionally; capacity formulas should use African quotas.
- SDR cost is 50–70% lower than US, making outbound prospecting more economically attractive.
- CSM in Africa often doubles as field-implementation; budget for travel within country and across borders.
- Sales-cycle inflation (1.5–2× US benchmarks) means lower #deals/AE; offset by lower OTE.
