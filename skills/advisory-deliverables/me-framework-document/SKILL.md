---
name: me-framework-document
description: Use when authoring a standalone monitoring, evaluation and learning framework for an East African organisation or programme; use `meta-monitoring-evaluation` for a plan section, and defer budget variance, burn rate, and financial-monitoring doctrine to Chwezi Accounting Doctrine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
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

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Programme design, theory of change, results commitments, budget, and stakeholder needs | Client, funder, and programme records | Required | Produce an evidence request and provisional results chain |
| Baselines, targets, data systems, definitions, disaggregation, and reporting calendar | Programme owners and data providers | Required | Mark the affected indicator unbaselined or unassessed |
| Financial-monitoring definitions and data | Chwezi Accounting Doctrine and finance system owners | Conditional | Keep budget, burn-rate, and variance indicators draft-only |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Standalone MEL Framework | Programme team, management, funder, partners, evaluators, and data stewards | Results chain, indicators, methods, roles, learning, reporting, ethics, and evaluation are coherent |
| Indicator reference sheets and MEL plan | Data collectors and decision owners | Each indicator defines formula, source, frequency, disaggregation, owner, quality checks, target, and use |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Results and indicator traceability | Outcome-to-indicator-to-source-to-decision matrix | Every indicator supports a named result and management decision |
| Financial-monitoring gate | Definition and doctrine review log | Budget, variance, and burn-rate measures reconcile to Chwezi doctrine and finance-system definitions |

## Capability Contract

Assessment defaults to read-only access and minimises personal or sensitive data. Edit only the authorised framework. Do not fabricate baselines, alter source records, promise impact attribution, approve budgets, or certify evaluation findings without explicit authority and appropriate methodological and finance review.

## Degraded Mode

If baseline data, respondent access, tools, finance definitions, or source verification is unavailable, return a qualified framework, indicator gaps, and a data-acquisition plan. Mark the affected measure `not assessed` or `baseline pending`; never convert absence of evidence into zero performance.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Result can be directly measured with reliable routine data | Use a direct indicator | Unnecessary proxy error |
| Direct measurement is infeasible | Use a justified proxy and state its limitation | False precision |
| Evaluation question needs causal attribution | Specify a credible design or limit claim to contribution | Unsupported impact claim |
| Indicator is financial | Reconcile definition and source to Chwezi doctrine | Conflicting programme and finance figures |

## Workflow

1. Confirm purpose, audience, decisions, evaluation questions, ethics, and approval route.
2. Review programme logic, commitments, stakeholder information needs, budgets, and existing data.
3. Test the results chain and stop where a load-bearing causal link has no plausible warrant.
4. Define indicators, baselines, targets, methods, disaggregation, sources, frequency, and owners.
5. Design collection, quality assurance, safeguarding, storage, reporting, learning, and evaluation processes.
6. Reconcile financial measures to current Chwezi doctrine and finance-system definitions.
7. Pilot representative indicator calculations and failure paths; recover by revising definitions or data plans.
8. Release with assumptions, missing baselines, limitations, resource needs, and review status visible.

## Quality Standards

The framework must connect results to decisions, use measurable definitions, protect participants, and expose data limitations. Financial indicators must reconcile with accounting definitions and pass finance review.

## Anti-Patterns

- Counting activities as outcomes. Fix: separate delivery, uptake, behaviour, and outcome measures.
- Inventing a baseline to complete a logframe. Fix: label it pending and specify collection method and date.
- Using an indicator without a decision owner. Fix: name who acts, when, and on what threshold.
- Collecting sensitive data by default. Fix: justify necessity, consent, access, retention, and protection.
- Mixing programme burn rate with accounting figures. Fix: define and reconcile it under Chwezi doctrine.
- Claiming attribution from a before-and-after observation. Fix: specify a valid design or qualify the claim as contribution.

## Worked Example

If a programme promises improved household income but has no baseline, retain the outcome, mark the baseline pending, define the sampling and timing, add an interim leading indicator, and prohibit impact claims until comparable data exist.
<!-- dual-compat-end -->
