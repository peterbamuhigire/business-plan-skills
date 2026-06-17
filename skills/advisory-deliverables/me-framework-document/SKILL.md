---
name: me-framework-document
description: Author a client-ready, standalone Monitoring, Evaluation & Learning (MEL) Framework document for NGOs, CSOs, SMEs, donor-funded projects, and public-bodies in Uganda/East Africa. Owns document architecture, the consulting workflow, parameterisation, and East African context; defers M&E methodology (theory of change, results framework, indicators, OECD-DAC evaluation) to existing M&E skills and defers financial-monitoring substance (budget-vs-actual, variance, burn rate) to the Chwezi finance engine. Distinct from the business-plan M&E section: this produces the full standalone framework deliverable.
---

# M&E Framework Document

A consulting-deliverable skill: it produces a standalone organisational document — a Monitoring, Evaluation & Learning (MEL) Framework — not a business-plan section. It owns the document's structure, the consulting workflow, the parameter-setting, and the East African framing — and it pulls M&E methodology from the existing M&E skills and every financial-monitoring treatment from the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.

## Use When

- A client needs a **Monitoring, Evaluation & Learning (MEL) Framework**, **M&E Framework / Plan**, **Results Framework / LogFrame**, **performance-measurement framework**, or a **theory of change** deliverable as a standalone document.
- Responding to an RFP/EOI/ToR for "development of an M&E / MEL framework" or "design of a results and learning system."
- Reviewing, gap-auditing, or updating an existing M&E framework against current practice and donor requirements.

## Do Not Use When

- Writing the M&E **section inside a business plan** — use `meta-strategy/meta-monitoring-evaluation` (that produces an M&E section in a plan; this skill produces the full standalone framework).
- Drafting an M&E **section of a bid/proposal** — use `proposal-skills` (`domain-delivery/monitoring-and-evaluation`).
- Answering a single methodology question — go straight to the relevant M&E skill.
- Producing the financial-monitoring substance itself (variance, burn rate) — that comes from the finance engine; this skill links to it.

## Required Inputs

Entity type (NGO/CSO, SME, donor-funded project, public/LG-adjacent body); the programme/project being measured, its goal and objectives, and its theory of change if one exists; funding model and any binding donor M&E rules and result frameworks (USAID, EU/GIZ, FCDO, UN, World Bank, AfDB); existing M&E framework, indicators, or logframe; data systems and capacity in place; reporting obligations and audiences (board, donor, regulator); the approved budget so programmatic results can be tied to financial absorption; jurisdiction (default Uganda); named approver/owner. Never fabricate these — ask.

## Workflow

1. **Intake & scope.** Fix entity type, the programme to be measured, the document(s) wanted, donors and their result frameworks, audiences, and jurisdiction. If a framework exists, run a gap audit against the blueprint before drafting.
2. **Select the blueprint.** Load `references/document-blueprint.md` for the MEL-framework chapter map, indicator-matrix template, parameterisation rule, and tools list.
3. **Pull M&E methodology from the existing skills — do not improvise.** For theory of change, results framework, indicators, and evaluation design read `business-plan-skills/skills/meta-strategy/meta-monitoring-evaluation` and `proposal-skills/skills/domain-delivery/monitoring-and-evaluation`; for stakeholder/beneficiary engagement read `proposal-skills/skills/domain-delivery/stakeholder-engagement`; for review gates and living-plan governance read `meta-strategy/meta-living-plan-governance`. The blueprint carries the chapter→source map.
4. **Build the results logic.** Theory of change first, then the results framework / logframe (inputs → activities → outputs → outcomes → impact), then SMART indicators with baseline, target, means of verification, frequency, and responsibility. Render indicators as the matrix table from the blueprint.
5. **Pull financial-monitoring substance from the finance engine — do not improvise.** For budget-vs-actual, variance with narrative, and KPI cascade read `09-budgeting-fpa-and-costing/variance-analysis-and-kpi-reporting` and `budgeting-and-rolling-forecasts`; for donor flexed-budget (exchange-rate-adjusted) variance read `doctrine/references/uganda-ngo-financial-management-patterns.md`. Tie programmatic results to financial absorption / burn rate.
6. **Set every target, baseline, and cadence as a named client parameter.** Indicator targets and baselines, data-collection frequency, and reporting cadences are defaults-to-be-approved, each with an owner and a review date — never asserted as fixed facts.
7. **Design the evaluation plan on OECD-DAC criteria** — relevance, coherence, effectiveness, efficiency, impact, sustainability — with an evaluation calendar and a ToR template; add the data management plan (collection tools, data-quality assurance) and the M&E calendar.
8. **Add roles, learning, and utilisation-focused reporting.** M&E roles & responsibilities; adaptive-management / learning loop with review gates; board and donor reporting templates (quarterly performance report tying results to financial absorption); version control.
9. **Run the quality gates.** `meta-utility/anti-ai-slop` (live) and `meta-strategy/meta-critical-thinking-business-logic`; where financial monitoring appears, the finance engine's conformance scan. Record each gate run in the artefact manifest.
10. **Produce the deliverable.** Client-ready DOCX/PDF (use the document engines), plus an adoption checklist: board/donor approval, effective date, and an M&E capacity / data-systems plan.

## Quality Bar

Every indicator is SMART with a stated baseline, target, means of verification, frequency, and a named responsible person; every target and cadence is a parameter with an owner and a review date, not a hardcoded fact; the results framework chains cleanly inputs → activities → outputs → outcomes → impact with no orphan indicators; the theory of change states assumptions explicitly; the evaluation plan covers all six OECD-DAC criteria; programmatic results are tied to financial absorption/burn rate via the finance engine (with flexed-budget variance for donor-funded work); reporting is utilisation-focused for its actual audiences; and it passes anti-ai-slop. British English throughout.

## Anti-Patterns

- Copying one programme's indicators, baselines, or targets verbatim into another.
- Indicators with no baseline, no means of verification, or no responsible person.
- A logframe whose outputs do not connect to the stated outcomes and impact (orphan results).
- Asserting an indicator target or reporting cadence as fixed instead of a default-to-be-approved parameter with an owner and review date.
- Improvising variance / budget-vs-actual logic instead of pulling it from the finance engine; omitting the flexed-budget variance on donor-funded work.
- Treating donor result frameworks and the entity's framework as interchangeable — layer both, stricter wins.
- Dropping the learning/adaptive-management loop so the framework only reports backwards.
- Shipping a generic template full of `[bracketed placeholders]` instead of a client-parameterised framework.

## Outputs

MEL Framework document; theory of change; results framework / logframe; indicator matrix (with baselines, targets, MoV, frequency, responsibility); data management plan and data-collection tools; M&E calendar; roles & responsibilities; evaluation plan (OECD-DAC) with ToR template; reporting & learning plan with board/donor and quarterly performance report templates; financial-monitoring linkage (budget-vs-actual / absorption); adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — MEL-framework chapter map, chapter→source mapping, indicator-matrix table template, parameterisation rule, and tools list.
- M&E methodology: `business-plan-skills/skills/meta-strategy/meta-monitoring-evaluation`; `proposal-skills` (`C:\wamp64\www\proposal-skills`) `skills/domain-delivery/monitoring-and-evaluation` and `skills/domain-delivery/stakeholder-engagement`; `meta-strategy/meta-living-plan-governance`.
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `skills/09-budgeting-fpa-and-costing/variance-analysis-and-kpi-reporting/`, `skills/09-budgeting-fpa-and-costing/budgeting-and-rolling-forecasts/`, and `doctrine/references/uganda-ngo-financial-management-patterns.md` (donor flexed-budget variance).
- `country-context/uganda/SKILL.md` for institutions/regulatory bodies; `language/east-african-english` for style.
