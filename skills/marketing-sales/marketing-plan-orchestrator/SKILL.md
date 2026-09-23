---
name: marketing-plan-orchestrator
description: Use when creating a standalone marketing plan covering market choices, positioning, offer, pricing, distribution, promotion, budget and execution; use 07-marketing-sales-strategy for a business-plan section and digital-marketing-strategy for its digital layer.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Marketing Plan Orchestrator

Turn customer evidence and commercial constraints into a complete marketing
investment and execution decision. A marketing plan is a distinct deliverable;
it must work without being embedded in a full business plan.

<!-- dual-compat-start -->
## Use When

- Create or substantially revise an annual, launch, service, product or market-entry marketing plan.
- Reconcile brand, demand, sales, service, channel investment and financial assumptions across a marketing programme.

## Do Not Use When

- Use `07-marketing-sales-strategy` for Section 07 alone.
- Use `digital-marketing-strategy` for only the digital layer; use the social-media engine for channel execution plans and campaign production briefs.
- Do not replace a full business plan, statutory review or evidence of market demand with this workflow.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when missing |
|---|---|---:|---|
| Business, offer, country, audience, decision and planning horizon | Sponsor/intake | Yes | Stop strategic choices; request the missing context |
| Customer, competitor and current-performance evidence | Research, CRM, sales and service records | Yes | Produce a research plan and bounded hypotheses; no validated demand claim |
| Price, contribution, budget, cash and capacity constraints | Finance and delivery owners | Yes | Hold scale/budget approval; use labelled scenarios |
| Brand, distribution, sales, service and delivery commitments | Accountable owners | Yes | Record dependencies and required decisions |
| Applicable regulation, rights and approval requirements | Current primary sources and qualified reviewers | Conditional | Mark affected release gates NOT_ASSESSED |

## Workflow

1. Frame the decision, buyer, geography, horizon, success measure and authority. Create a stage/evidence register.
2. Apply [the marketing decision workpapers](references/marketing-decision-workpapers.md). Research buying situations, unmet needs, alternatives and reasons for non-purchase; distinguish observation from inference.
3. Choose target segments and exclusions. State positioning, offer, proof and willingness-to-pay hypothesis. Compare at least one credible alternative; route premium positioning to `meta-premium-go-to-market`.
4. Design the marketing mix: product/service, pricing, distribution/access, promotion, sales and retention. Address people, process and physical/digital proof where service delivery affects the promise.
5. Choose channel roles from buyer evidence and economics. Route digital detail to `digital-marketing-strategy`, website investment to `meta-website-investment-planning`, and execution briefs to social-media-skills.
6. Build an integrated budget and demand-to-cash bridge with Chwezi finance doctrine. Reconcile funnel assumptions, sales-cycle lag, fulfilment, retention and capacity; keep scenario inputs explicit.
7. Prioritise the first experiments and execution cycle. Assign owners, effort, dependencies, spend ceiling, evidence requirement, stop rule and review date. Make later roadmap phases conditional.
8. Challenge demand, competitive response, weak conversion, delayed approvals, cost increases and delivery failure. Stop scaling when contribution, cash, trust or capacity guardrails fail; recover with a smaller test or revised offer.
9. Draft the executive decision last. Assemble strategy, implementation, budget, measurement, evidence and risk appendices in an order the reader can use.
10. Run finance/reconciliation, current-source, anti-slop and document/design gates as applicable. Correct failures and repeat affected checks. Hand off the plan and evidence to named operating owners.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Demand evidence is weak | Commission a bounded validation test before scaling | A persuasive forecast masks an untested market |
| More leads would exceed service capacity | Repair delivery, narrow demand or sequence investment | Marketing damages the brand promise |
| Premium price has no distinct buyer value/proof | Revise offer and test price acceptance | Prestige language substitutes for willingness to pay |
| Digital is not the best route | Prioritise a justified offline/partner route | Channel fashion overrides customer behaviour |
| A material source, model or approval is missing | Hold the affected decision and name the recovery input | False release readiness |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Standalone marketing plan | Sponsor and operating team | Market choices, full mix, budget, execution and control work without a separate business-plan chapter |
| Investment and assumption model | Finance and commercial owners | Costs, demand, margin, cash and capacity reconcile by period/scenario |
| Execution and learning register | Channel, sales and service owners | Every initiative has owner, resources, dependency, measure, stop rule and review |
| Evidence and release record | Reviewer | Claims, unknowns, standards applicability and required approvals are traceable |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Customer/competitor and claim register | Source-linked workpaper | Sampling, dates, scope, contradictions and confidence are visible |
| Alternatives and investment decisions | Decision table/model | A reviewer can reproduce the selected option and downside case |
| Plan rehearsal | Synthetic or real brief, clearly labelled | Handoffs and failure paths are exercised; no simulation is passed off as market proof |

## Quality Standards

- Make explicit choices; a list of channels is incomplete.
- Reconcile the promise with delivery quality and the revenue forecast with cash and capacity.
- Separate targets, assumptions, estimates, observed results and commitments.
- Use jurisdiction-specific current evidence; never claim universal compliance or guaranteed results.
- Review authored prose and rendered artefacts separately. Missing market, finance, professional or render evidence remains NOT_ASSESSED.

## Anti-Patterns

- Delivering only a social calendar. Fix: cover market, offer, price, distribution, sales, economics and control.
- Treating affluent consumers as one segment. Fix: research buying situation, value drivers and access constraints.
- Budgeting media alone. Fix: include production, labour, tools, fees, research and operating capacity.
- Forecasting sales from impressions alone. Fix: model qualified demand, conversion, lag and fulfilment with explicit assumptions.
- Calling the plan convincing because it is polished. Fix: challenge the evidence, alternatives and downside economics.
- Applying every framework. Fix: retain only methods that change a decision or expose a risk.

<!-- dual-compat-end -->
## Capability Contract

Read and search supplied evidence; calculate and draft the authorised working
plan. Analysis and planning are read-only with respect to source systems.
Network verification is required for current claims. Publishing, outreach,
spending, account changes and certification require explicit authority.

## Degraded Mode

Without research, financial inputs or current sources, deliver a labelled
hypothesis plan and evidence-acquisition sequence. Hold investment approval and
affected compliance claims. If export/render tools are unavailable, deliver
Markdown and mark final-format checks not assessed; do not claim files exist.

## Worked Example

A consultancy wants LinkedIn, Instagram, TikTok and paid search simultaneously,
but one practitioner owns delivery and sales. Compare buyer evidence and effort;
select a narrow LinkedIn-to-website pilot if justified, maintain the other
channels only where they serve an evidenced job, and test qualified enquiries
against available delivery hours before expanding.

## References

- [Marketing decision workpapers](references/marketing-decision-workpapers.md).
- [Section 07](../../pipeline/07-marketing-sales-strategy/SKILL.md).
- [Digital marketing layer](../digital-marketing-strategy/SKILL.md).
- [Premium go-to-market](../../meta-pricing-gtm/meta-premium-go-to-market/SKILL.md).
- Resolve Digital Research, Chwezi finance, design-system, social-media and website engines through the global engine table; load the relevant canonical skill rather than copying their doctrine.
