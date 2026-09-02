---
name: kaizen-improvement-system
description: Use when auditing or improving the business-plan engine or any business plan, strategy, model, pitch, nonprofit plan, or execution framework it produces.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Kaizen Improvement System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Auditing this engine or a plan, model, strategy, pitch, or execution framework.
- Converting assumptions, market feedback, KPI variance, or delivery lessons into a tested improvement.

## Do Not Use When

- The task is only a single-skill safety audit.
- A current market, legal, tax, platform, or finance claim has not been routed to Digital Research and Chwezi where applicable.

## Required Inputs

| Artefact | Source/provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Engine or product scope, audience, evidence pack, assumptions/model, current score, constraints, and target measures | Project and engine | yes | Set audit scope and improvement target | Stop, mark unassessed, or request the missing evidence |

## Workflow

1. Read the local adoption plan and the portfolio standard.
2. Inventory routes, plan types, references, templates, models, examples, source registers, and release gates.
3. Score doctrine, taxonomy, skill depth, applied proof, currency, output readiness, inclusivity, production fidelity, hygiene, routing, and integrity. Publish `min(raw score, 65)` and record blockers.
4. For a product, test the thesis, customer or beneficiary logic, market evidence, operating model, financial reconciliation, implementation capacity, risks, governance, and audience fit.
5. Create a P0/P1/P2 improvement backlog targeting 95/100; each action needs owner, experiment, measure, evidence, and rollback.
6. Run a small Build-Measure-Learn or PDCA experiment. If evidence fails, stop, recover the safe baseline, and revise the hypothesis.
7. Re-run model, source, anti-slop, workbook, and release gates as applicable; standardise successful learning and schedule the next review.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Capped audit, evidence gaps, blockers, 95/100 plan, experiment log, and standardisation record | Planner, reviewer, and release owner | Scores, owners, evidence, decisions, rollback, and re-audit date are explicit |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumption ledger, model/source checks, experiment result, gate results, and before/after review | Markdown, workbook, or validator output | Another reviewer can reproduce the decision and verify the change |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Audits are read-only by default; edits require explicit authority and permission. Route current facts to Digital Research and finance doctrine to Chwezi.

## Degraded Mode

If evidence, model, source, reviewer, or tool is unavailable, return the narrowest qualified result, mark the gap as not assessed, and do not certify bankability or readiness.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Material assumption has no evidence | Stop the claim and run a validation test | False certainty |
| A test improves one metric but harms cash, mission, quality, or capacity | Reject, recover, or escalate | Local optimisation |
| A change passes gates and improves the target measure | Standardise it and re-audit | Lost learning |

## Quality Standards

Never call a plan bankable or achievable without reconciled evidence, assumptions, finance, implementation, and risks. Never turn a book example into a client fact.

## Mandatory 65-to-95 gate

The first pass is an initial analysis, not a certification: calculate the raw result,
publish `min(raw_score, 65)`, and keep every unassessed dimension and blocker visible.
Only after the capped baseline is recorded may the engine run the improvement cycle.
The cycle must target 95/100 with a named root cause, one reversible change, owner,
measure, guardrail, stop/rollback rule, acceptance evidence, and re-audit date. A
polished plan or book-derived idea is not a score increase until the evidence passes.
Run it twice when scope warrants: first for engine routing, models, references,
validators, and handoffs; then for the individual plan, model, pitch, or strategy.

## Anti-Patterns

- Adding initiatives without stopping or sequencing others. Fix: expose capacity trade-offs.
- Treating a KPI as learning without a decision rule. Fix: define threshold, action, and counter-metric.
- Writing a polished plan before testing assumptions. Fix: run a small validation experiment.
- Hiding uncertainty in prose. Fix: label assumptions, gaps, confidence, and countercases.
- Closing an improvement with no evidence. Fix: require a validated artefact or test.

## Worked Example

If a market test raises enquiries but worsens fulfilment capacity, retain the result as mixed evidence, keep the capacity guardrail, revise the offer or process, and re-test before changing the plan.

## Mandatory Digital Research currentness gate

Every Kaizen cycle must begin with `digital-research-skills` source evaluation
and source verification. Record scope, dates, freshness class, support status,
uncertainty, and review date for current market, legal, policy, technology,
platform, finance, and lifecycle claims; quarantine unsupported claims as
`NOT_ASSESSED`. Apply the [portfolio Kaizen currentness gate](../../../../digital-research-skills/docs/continuous-improvement/kaizen-currentness-gate.md).

## References

- [Local adoption plan](../../../docs/continuous-improvement/kaizen-adoption-2026-08.md)
- Portfolio standard: resolve `digital-research-skills` through the global engine-routing table, then read `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`.
- `skills/meta-strategy/meta-market-validation/`
- `skills/meta-strategy/meta-living-plan-governance/`
- [Book-driven commercial system and validation](../references/book-driven-commercial-system-and-validation.md) - whole-system trade-offs, validation, replication, GTM, cash, and currentness.
- [Marketing Plan Handbook operating loop](../references/marketing-plan-handbook-operating-loop.md) - adaptive customer-first planning, segmentation, strategy-to-program alignment, forecasting, budgeting, metrics, and control.
- [Book-driven Kaizen Wave 3](../references/book-driven-kaizen-wave-3-2026-09-02.md) - hypotheses, capacity/cash guardrails, experiments, dashboards, and responsible AI economics.
