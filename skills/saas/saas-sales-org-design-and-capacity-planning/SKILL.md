---
name: saas-sales-org-design-and-capacity-planning
description: Use when Section 09 or Section 10 is being built for a SaaS plan with target ARR above $1M. Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Sales Org Design & Capacity Planning Skill

## Overview

Convert ARR ambition into a reconcilable sales-org plan. Most SaaS plans project $5M ARR by Year 3 with two sales hires — mathematically impossible. This skill produces the canonical formula: **Bookings = #AEs × Quota × Attainment % × (1 − Ramp Discount)** and the org evolution by ARR milestone.

## Use When

- Section 09 (Management Team) or Section 10 (Financial Projections) is being built for a SaaS plan with target ARR > $1M
- The plan's sales-bookings line doesn't reconcile with the headcount plan
- The team is hiring its first VP of Sales / Head of Revenue
- An ARR milestone is approaching and the org needs to evolve

## Do Not Use When

- The request belongs to the neighbouring route. Use the cross-sector meta skill when the decision is not specific to recurring-revenue SaaS economics or operations.
- The available evidence cannot support a responsible sales org design and capacity planning conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Sales Org Design And Capacity Planning brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
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

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the sales capacity model and that the decision concerns the hiring sequence and productive capacity that can support bookings.
- **Stop condition:** halt the affected conclusion if required evidence is missing (ARR target, quota, ramp, attainment, OTE, sales cycle, and hiring lead time) or if the work could lead to this identified risk: forecasting ARR that the planned sales team cannot produce.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

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


- Applying the wrong neighbouring route to saas sales org design and capacity planning. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Sales Org Design And Capacity Planning deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
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

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Sales capacity model decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to forecasting ARR that the planned sales team cannot produce. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the sales capacity model; modelling headcount without opening requisitions is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If ARR target, quota, ramp, attainment, OTE, sales cycle, and hiring lead time cannot be obtained, return a qualified sales capacity model covering only the checks that remain supportable. Leave this decision unresolved: the hiring sequence and productive capacity that can support bookings. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: the hiring sequence and productive capacity that can support bookings | Record the conclusion, source trail, owner, and review trigger in the sales capacity model. | Risk of forecasting ARR that the planned sales team cannot produce |
| Material evidence conflicts or remains uncertain | Rebuild bookings from productive representatives, ramp, attainment, and sales cycle under each hiring sequence before approving headcount. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: ARR target, quota, ramp, attainment, OTE, sales cycle, and hiring lead time | Mark the decision on the hiring sequence and productive capacity that can support bookings `not assessed` in the sales capacity model, and send it to the sales leader and finance owner. | Otherwise, the work risks forecasting ARR that the planned sales team cannot produce |

## Quality Standards


Accept the sales capacity model only when evidence is sufficient for this decision: the hiring sequence and productive capacity that can support bookings. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of forecasting ARR that the planned sales team cannot produce.

## Worked Example


The bookings forecast assumes four fully productive representatives from their first month. Apply hiring lead time, ramp, attainment, and sales cycle; either stage the hires or revise ARR.

<!-- dual-compat-end -->
