---
name: marketing-plan-orchestrator
description: Use when creating or auditing a full standalone marketing plan with situation analysis, SMART objectives, strategy, channels, media, sales plan, budget, KPIs and control; use `07-marketing-sales-strategy` for the business-plan section and `digital-marketing-strategy` for the digital layer only.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Marketing Plan Orchestrator

Turn customer evidence and commercial constraints into a complete, standalone
marketing plan: what market to serve, what to say, where and how often to say
it, how demand becomes cash, what it costs, who does what, and how the plan is
steered. A marketing plan is a distinct deliverable; it must work without a
full business plan, and every objective must be specific, measurable, accurate,
realistic, time-bound and applicable to the business, its location and scope.

<!-- dual-compat-start -->
## Use When

- Create or substantially revise an annual, launch, product, service, market-entry, regional or campaign marketing plan.
- Audit an existing marketing plan against the document architecture and quality gate.
- Reconcile brand, demand, sales, service, channel investment and financial assumptions across a marketing programme.

## Do Not Use When

- Use `07-marketing-sales-strategy` for Section 07 of a business plan; it borrows this skill's references at section depth.
- Use `digital-marketing-strategy` for only the digital layer. Use the digital marketing and advertising engine (`social-media-skills`) for advertising strategy detail, detailed media plans, creative briefs, build specifications, optimisation and attribution; this skill keeps only the plan-level objectives, budget envelope and media-mix decision reconciled to the P&L.
- Use `meta-strategic-factor-analysis` or `meta-strategic-options-evaluation` for corporate strategy work that is not a marketing plan.
- Do not replace a full business plan, statutory review or evidence of market demand with this workflow.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when missing |
|---|---|---:|---|
| Business, offer, location and scope, audience, decision, planning horizon and strategy type | Sponsor or `00-client-intake` | Yes | Stop strategic choices; request the missing context |
| Customer, competitor and current-performance evidence (sales, CRM, research) | Research, CRM, sales and service records | Yes | Produce a research plan and bounded hypotheses; no validated demand claim |
| Price, contribution, budget, cash and capacity constraints | Finance and delivery owners | Yes | Hold scale and budget approval; use labelled scenarios |
| Brand, distribution, sales, service and delivery commitments | Accountable owners | Yes | Record dependencies and required decisions |
| Current legal, platform and market facts | Currentness register, Digital Research engine, qualified reviewers | Conditional | Mark affected claims and release gates NOT_ASSESSED |

## Workflow

1. **Frame.** Record the business outcome, decision, reader, horizon, budget authority, strategy type and scope level. Apply [location and scope calibration](references/location-and-scope-calibration.md). Open a claim register using [evidence discipline](references/evidence-discipline-for-marketing-claims.md).
2. **Outline.** Choose the depth from the scaling rules in [document architecture](references/marketing-plan-document-architecture.md). Keep all 20 section decisions; compress, do not omit.
3. **Research the customer first.** Build the customer insights report, segmentation, target-market tests, buying situations and sensitivities using [the toolkit](references/situation-and-market-toolkit.md) and [the decision workpapers](references/marketing-decision-workpapers.md). Stop creative and media work until this exists.
4. **Analyse the situation.** Reduce PESTEL to key drivers, rate five forces, and build EFAS, IFAS and SFAS on the single scale defined by `meta-strategic-factor-analysis`; convert SWOT to TOWS. Size the market top-down and bottom-up with a sanity check. Map competitors with weighted grids.
5. **Position.** Write the positioning statement, choose one or two of the five buyer-benefit answers and two or three message themes by importance × proof × distinctiveness. Route premium offers to `meta-premium-go-to-market`.
6. **Set objectives.** Build the business → marketing → communication → channel cascade with the [SMART objective builder](references/smart-objectives-builder.md). Reject any objective that fails its quality test.
7. **Choose strategy.** STP and coverage, strategy-clock position, growth route and method, push and pull balance, and the marketing mix with a decision per P; evaluate options with `meta-strategic-options-evaluation` when the choice is contested.
8. **Choose channels.** Run the [Bullseye method](references/traction-channel-bullseye.md) across all 19 channels; write three test cards; set the critical path and not-doing list.
9. **Plan advertising, digital and content.** Use the [advertising and media plan](references/advertising-and-media-plan.md) for objectives, triangulated budget, reach, frequency, flighting, the audience-cost table and the creative brief. Hand the digital, content and detailed advertising layers to `digital-marketing-strategy` and the digital marketing and advertising engine with the handoff table in the architecture; keep the envelope, mix and P&L reconciliation here.
10. **Plan sales and retention.** Apply [sales plan and account coverage](references/sales-plan-and-account-coverage.md) and the retention and CLV sections of [marketing economics](references/marketing-economics-and-budget.md).
11. **Cost and reconcile.** Build the two-phase budget, direct-response break-even lines, the maximum affordable cost per lead and the demand-to-cash bridge; reconcile the budget with the P&L marketing line under the Chwezi finance doctrine. Stop release on any mismatch.
12. **Steer.** Build the calendar, KPI dashboard (OMTM, guard-rails, lines in the sand), control table, war-room cadence and risk register with the [KPI and control plan](references/kpi-dashboard-and-control-plan.md).
13. **Write and gate.** Draft the executive summary last. Write with the [marketing-plan phrase bank](../../language/writing-quality/references/marketing-plan-phrase-bank.md), `writing-quality` and `anti-ai-slop`. Run the [quality gate](references/marketing-plan-quality-gate.md); when it fails, return to the affected step, revise, and re-run the gate. Hand the plan and evidence to named owners.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Customer research or an approved plan is missing | Hold creative and scaled media; run research and a capped test first | Spending on messages nobody has tested |
| Demand evidence is weak | Commission a bounded validation test before scaling | A persuasive forecast masks an untested market |
| An objective fails the SMART quality test or is not calibrated to the place and scope | Rewrite it or delete it | Unmeasurable or inapplicable targets |
| More leads would exceed delivery or sales capacity | Repair delivery, narrow demand or sequence investment | Marketing damages the brand promise |
| Budget below the minimum effective level | Concentrate on fewer places, segments or months | Invisible, spread-thin campaigns |
| A channel's cost per enquiry exceeds the affordable ceiling after its test | Drop or redesign it and move to the next test card | Scaling a loss-making channel |
| Premium price has no distinct buyer value or proof | Revise offer and test price acceptance | Prestige language substitutes for willingness to pay |
| Digital is not the best route for the segment | Prioritise a justified offline, partner or sales route | Channel fashion overrides customer behaviour |
| Plan budget differs from the P&L marketing line | Return to the owning section and reconcile before release | Narrative and numbers that disagree |
| Direct marketing or data collection lacks a data-protection line | Add registration, consent and objection handling per jurisdiction | Unlawful campaigns and regulator exposure |
| A material source, model or approval is missing | Hold the affected decision and name the recovery input | False release readiness |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Standalone marketing plan (20 sections plus appendices) | Sponsor and operating team | Passes the quality gate with no blockers and meets the release thresholds |
| Objectives cascade and KPI table | Owners and reviewers | Every objective passes the SMART test; every KPI has a line, owner and pre-agreed action |
| Budget, economics and demand-to-cash model | Finance and commercial owners | Budget equals the P&L line; costs, demand, margin, cash and capacity reconcile by period and scenario |
| Channel, media and sales plans | Channel, sales and service owners | Every initiative has owner, budget, dependency, measure, stop rule and review date |
| Handoff briefs | Digital marketing and advertising, website and design engines | Message, channel and compliance briefs carry the agreed definitions |
| Evidence and release record | Reviewer | Claims classed and sourced; unknowns and NOT_ASSESSED items listed |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Claim and source register | Appendix table | Every number has a class, source and date; register claim IDs cited |
| Customer insights report and research records | Workpaper | Method, sample, dates and limitations visible; no fabricated respondents |
| Options and investment decisions | Decision table and model | A reviewer can reproduce the selected option, rejected alternatives and downside case |
| Quality-gate record | Scored rubric | Score, blockers, fixes and reviewer recorded; missing review marked NOT_ASSESSED |

## Quality Standards

- Make explicit choices; a list of channels is not a strategy.
- Every objective is SMART and applicable to the place and scope; every target states the source of its line in the sand.
- Reconcile the promise with delivery quality, the forecast with cash and capacity, and the budget with the P&L.
- Separate verified facts, assumptions, estimates, projections and targets; use register or freshly verified current facts only.
- Never call the plan bankable, viable, investor-ready or compliant without the engine's evidence gates.
- Review authored prose and rendered artefacts separately. Missing market, finance, professional or render evidence remains NOT_ASSESSED.

## Anti-Patterns

- Delivering only a social calendar. Fix: cover market, offer, price, distribution, sales, economics and control.
- Treating affluent consumers or "SMEs" as one segment. Fix: apply the four target-market tests and research buying situations.
- Budgeting media alone. Fix: include production, research, testing, labour, fees, tools and contingency, triangulated and reconciled.
- Forecasting sales from impressions. Fix: model qualified demand, conversion, sales lag and fulfilment with explicit assumptions.
- Copying foreign benchmarks and channel habits into a Ugandan plan. Fix: calibrate to the place, scope and evidence.
- Calling the plan convincing because it is polished. Fix: challenge the evidence, alternatives and downside economics.
- Applying every framework. Fix: retain only methods that change a decision or expose a risk.

<!-- dual-compat-end -->
## Capability Contract

Read and search supplied evidence; calculate and draft the authorised working
plan. Analysis, planning and gate review are read-only with respect to source
systems. Network verification is required for current claims. Publishing,
outreach, spending, account changes and certification require explicit
authority.

## Degraded Mode

Without research, financial inputs or current sources, deliver a labelled
hypothesis plan with the evidence-acquisition sequence, test cards and
placeholders listed as evidence requests. Hold investment approval and affected
compliance claims. If export or render tools are unavailable, deliver Markdown
and mark final-format checks not assessed; do not claim files exist.

## Worked Example

A Kampala meal-prep business wants "a big Facebook campaign". The orchestrator
first builds a customer insights report (320 survey responses and 10
interviews in Kira and Nakawa), finds that working parents value "no cooking
after work" and weekly mobile-money payment, and that month-two reorder is the
weak point. It sets a reconciled cascade (UGX 38m to UGX 55m monthly revenue by
June 2027; 160 net new households; month-two reorder 48% to 60%), runs Bullseye
tests on click-to-WhatsApp ads, resident-association sponsorships and a
referral credit, caps each at UGX 1.5m, and makes month-two reorder the OMTM.
The budget equals the P&L marketing line; a third delivery rider is scheduled
before capacity binds. All figures illustrative.

## References

- [Document architecture](references/marketing-plan-document-architecture.md) — load first; section decisions, required tables, scaling and cross-engine handoffs.
- [Situation, market and positioning toolkit](references/situation-and-market-toolkit.md) — sections 2–8: drivers, forces, factor tables, TOWS, segmentation, target-market checks, competitor grids, buyer-benefit questions, message themes.
- [SMART objective builder](references/smart-objectives-builder.md) — any objective or target; cascade, lines in the sand, quality test, UGX examples.
- [Location and scope calibration](references/location-and-scope-calibration.md) — before objectives, channels and budgets; Uganda and East Africa defaults and data-protection rules.
- [Traction channel Bullseye](references/traction-channel-bullseye.md) — channel choice, test cards, critical path.
- [Advertising and media plan](references/advertising-and-media-plan.md) — paid media, budget triangulation, scheduling, creative brief, measurement.
- [Sales plan and account coverage](references/sales-plan-and-account-coverage.md) — sales structure, lead grading, B2B contact economics, key accounts.
- [Marketing economics and budget](references/marketing-economics-and-budget.md) — CLV, CAC ceilings, break-even response, budget and demand-to-cash reconciliation.
- [KPI dashboard and control plan](references/kpi-dashboard-and-control-plan.md) — OMTM, metric tests, control table, cadence.
- [Evidence discipline](references/evidence-discipline-for-marketing-claims.md) — every number and claim.
- [Quality gate](references/marketing-plan-quality-gate.md) — before release.
- [Marketing decision workpapers](references/marketing-decision-workpapers.md) — market-sensing methods, premium workpaper, standards applicability.
- [Marketing-plan phrase bank](../../language/writing-quality/references/marketing-plan-phrase-bank.md) — wording per section.
- [Section 07](../../pipeline/07-marketing-sales-strategy/SKILL.md), [digital marketing layer](../digital-marketing-strategy/SKILL.md), [premium go-to-market](../../meta-pricing-gtm/meta-premium-go-to-market/SKILL.md).
- Resolve Digital Research, Chwezi finance, design-system, social-media and website engines through the global engine table; load their canonical skills rather than copying their doctrine.

## Read Next

- `meta-strategic-factor-analysis` — EFAS, IFAS and SFAS tables for section 2.
- `meta-strategic-options-evaluation` — contested strategic choices in section 8.
- `demand-forecasting` — volume forecasts behind the demand-to-cash bridge.
- `ai-slop-audit` — graded review after each drafted section.
