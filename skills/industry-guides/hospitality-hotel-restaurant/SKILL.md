---
name: hospitality-hotel-restaurant
description: Use when preparing a bankable business plan, feasibility study, investment case, or operating plan for a hotel, resort, lodge, inn, guest house, restaurant, bar, catering, or food-service business.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Hospitality Hotel And Restaurant Business Planning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- A bankable plan, feasibility study, investment case or operating plan concerns hospitality or food service.

## Do Not Use When

- The deliverable is only a generic plan with no hospitality-specific decision; route to `skills/meta-strategy/business-plan-orchestrator/` instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Format, location, capacity, ownership, stage, market and operating model | Client intake and sector guide | Yes | Stop classification and request the missing context. |
| Funding audience, financial model, country evidence and reviewer route | Client, finance and research engines | Conditional | Return a qualified plan and mark the affected decision `NOT_ASSESSED`. |

## Workflow

1. Classify the format and revenue centres.
2. Build evidence and assumptions before narrative or model drafting.
3. Model operations, capacity, revenue, cost, cash, funding and scenarios.
4. Reconcile finance, country/regulatory, implementation and reviewer gates.
5. Release only with explicit uncertainties, decisions and owner sign-offs; stop and recover by narrowing the plan when evidence is incomplete.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Hospitality sector brief, integrated plan/model, risk and implementation pack | Owner, lender, investor and delivery team | Revenue centres, assumptions, evidence, scenarios, funding and operations reconcile. |

## Evidence Produced

| Evidence | Format | Consumer | Acceptance condition |
|---|---|---|---|
| Source-to-assumption trace, formula/reconciliation checks and sensitivity cases | Register, workpaper and review record | Reviewer and finance owner | Each material assumption has source/date/status/owner and unresolved gaps are visible. |

## Capability Contract

Read/search, calculation, modelling and document production may be required.
Client data, external publication, funding commitments and professional sign-off
remain within the stated authority boundary.

## Degraded Mode

Return a qualified partial plan with an evidence and model-gap register when
market, finance, country, permit or management evidence is unavailable.

## Decision Rules

| Condition | Action | Risk avoided |
|---|---|---|
| Two material revenue centres exist | Model them separately and reconcile interfaces | Hidden cross-subsidy |
| A benchmark is old or foreign | Treat it as a hypothesis pending verification | False local precision |
| Debt or investor funding is requested | Include downside, cash and debt-service evidence | Overstated bankability |

## Quality Standards

The plan is decision-ready only when the narrative, operating model, financial
model, evidence, risks, implementation and review route agree.

This overlay sits on the business-plan pipeline and the hospitality-tourism and
restaurant guides. It converts hospitality concepts into a bankable, auditable
plan without treating old book benchmarks or generic templates as local facts.

## Classification before modelling

Classify the format before selecting assumptions: hotel/resort, lodge/eco-lodge,
inn/guest house, serviced apartment, restaurant, bar, cafe, catering,
banqueting/event venue, or a mixed property. Record location, keys, seats,
outlets, event capacity, service periods, seasonality, ownership, lease/debt,
management model, and construction/opening stage.

## Bankable plan architecture

1. **Investment thesis and use of funds:** concept, site, guest/customer,
   problem, differentiation, development phases, sources and uses, contingency,
   working-capital runway, and decision gates.
2. **Market and demand proof:** trade area, tourism/business/domestic demand,
   competitor set, access, seasonality, channel mix, event demand, customer
   interviews or primary counts, and downside case. Old market claims are
   context only until current country evidence verifies them.
3. **Product and service model:** room types and packages; restaurant/bar
   concept, menu and beverage architecture; events, meetings, catering,
   experiences, and ancillary services. State what is deliberately excluded.
4. **Operating model:** organisation, service standards, front office,
   reservations, housekeeping, kitchen, service, procurement, receiving,
   inventory, maintenance, food safety, security, complaints, events, training,
   technology, and management cadence.
5. **Revenue model:** model each centre separately: occupied room nights and
   ADR; food/beverage covers, average check, meal periods and table turns;
   events by space, date and package; and ancillary services. Reconcile gross
   revenue, discounts, commissions, taxes, deposits, refunds and net revenue.
6. **Financial model:** monthly opening ramp and at least a five-year annual
   view when appropriate; profit and loss, cash flow, balance sheet or opening
   position, capex schedule, depreciation, working capital, debt service,
   break-even, downside/upside sensitivities, and sources/uses. Use UGX or the
   requested functional currency consistently and route accounting judgement to
   Chwezi doctrine.
7. **Implementation and governance:** critical path, permits, design/procurement,
   recruitment/training, soft opening, systems, launch, KPI cadence, risks,
   mitigations, owners, and lender/investor reporting.

## Hospitality modelling rules

- Hotel capacity is keys x available nights; separate out-of-order rooms,
  complimentary rooms, group blocks, cancellations, no-shows, deposits and
  channel commissions. Forecast demand and revenue separately.
- Restaurant volume is seats x turns x covers x average check by meal period,
  reconciled to opening hours, capacity, delivery, catering and events. Use
  recipe cost, yield, waste, spoilage, labour and payment leakage controls.
- Show room revenue, F&B revenue, events, ancillary revenue, direct/channel cost,
  departmental costs, undistributed costs, capex and cash separately.
- Use ranges only when a dated, geography- and format-matched source supports
  them. A book or internal guide can supply a hypothesis; it cannot establish a
  current Uganda rate, licence, tax, wage, demand, margin or failure statistic.
- Include scenario sensitivities for occupancy/covers, price, seasonality,
  food cost, labour, utilities, FX, opening delay, capex overrun and interest
  where material. Do not make a lender claim from a single optimistic case.

## Required outputs for a bankable plan

- Assumption register with source, date, status, owner and validation trigger.
- Market evidence and competitor/price observation log.
- Five-year or approved-horizon integrated model with monthly ramp.
- Sources and uses, capex procurement schedule, working capital and debt case.
- Departmental operating plan and staffing/training plan.
- Risk register with financial impact and mitigation owner.
- KPI pack: occupancy, ADR, RevPAR, rooms revenue, covers, average check,
  table turns, food/beverage cost, labour, prime cost, event pipeline, cash
  variance, receivables, guest satisfaction, complaints and repeat/direct share.
- Sensitivity table, lender/investor questions, and a no-go/phase-gate decision.

## Anti-bloat rule

Do not add a spa, channel manager, loyalty scheme, AI pricing, delivery fleet,
large menu, event venue, or second outlet to improve the story unless demand,
capacity, economics, owner capability and implementation evidence support it.
Phase the concept and show the cash consequence of each optional component.

## Release gate

The plan is not “bankable” merely because it is polished. Release only when
material assumptions, market evidence, model formulas, taxes, permits, debt
service, operating capacity, management capability, downside case, sources and
uses, and reviewer approvals are traceable. Missing evidence remains
`NOT_ASSESSED`.

<!-- dual-compat-end -->

## Anti-patterns

- A single annual revenue figure. Fix: replace it with monthly ramp and revenue-centre drivers.
- Imported foreign ratios presented as Uganda facts. Fix: cite scope or convert to a labelled hypothesis.
- A hotel plan that ignores housekeeping, maintenance, food safety or working capital. Fix: add the operating constraints.
- Adding outlets or amenities to make returns look better. Fix: model them as phased options with evidence.
- Calling a plan bankable without debt service, downside, sources/uses and reviewer evidence. Fix: withhold that label.

## Worked example

For a 40-key guest house with a breakfast outlet, model available room nights,
out-of-order/closed inventory, occupancy and ADR by month; model breakfast
covers and average check separately; then reconcile staffing, utilities,
supplies, taxes, commissions, capex, working capital and debt service. Present
the base, downside and stop/phase gates rather than a single optimistic return.

## References

- [Hospitality and Tourism Guide](../hospitality-tourism/guide.md)
- [Restaurant Guide](../restaurant/guide.md)
- [Chwezi Accounting Doctrine](C:/wamp64/www/chwezi-accounting-doctrine/README.md)
