---
name: ecommerce-unit-economics-and-cross-border-margin-model
description: Use when modelling e-commerce landed cost, contribution margin, CAC, LTV, payment, fulfilment, return, commission, pricing, or cross-border market viability; use `ecommerce-business-model-diagnostic` for the wider operating-model assessment.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# E-Commerce Unit Economics and Cross-Border Margin Model
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Overview

Use this skill to answer the hard question in cross-border e-commerce: does the route make money after all variable costs? It builds a per-market and per-channel model for landed cost, shipping, returns, payment fees, FX, commissions, CAC, gross margin, contribution margin, payback, LTV, and working-capital impact.

The skill is deliberately company-data-led. EAC-specific benchmarks for CAC, AOV, return rates, de-minimis thresholds, and category commissions are often unavailable or unreliable. Do not invent them.

## Use When

- Testing the financial viability of a cross-border route or target market.
- Setting pricing, discount, CAC, or channel guardrails for an e-commerce company.
- Preparing a TA plan, business plan, export plan, or investor/partner discussion that depends on margin reality.

## Do Not Use When

- The company cannot provide any cost, order, shipping, payment, or marketing data.
- You only need a high-level market narrative with no financial decision.
- You are tempted to use global proxies without labelling them.

## Required Inputs

- Product/category, AOV, COGS, order volumes, gross margin, payment fees, fulfilment costs, returns/refunds, platform commissions, marketing spend, customer counts, and repeat purchase data.
- Target market, channel, currency, delivery route, payment rail, and return policy.
- Any duties, taxes, customs, or logistics quotes from named sources.

## Workflow

1. Build the assumptions register first. Tag every input as company data, supplier quote, official source, global proxy, indicative source, or inference.
2. Model base unit economics: AOV, COGS, gross margin, variable fulfilment, payment/FX, platform commission, returns, CAC, contribution margin, payback, and LTV.
3. Model landed cost by route: origin cost, freight, duties/taxes where confirmed, last mile, failed delivery, returns, and payment settlement.
4. Split results by country, channel, and product/category where data allows.
5. Run sensitivity tests on returns, freight, FX, payment fees, platform commission, AOV, discount, conversion, and CAC.
6. Set pricing and discount guardrails that preserve positive contribution margin.
7. Produce a go, conditional, or no-go verdict with assumptions that would change the verdict.

## Quality Bar

- No local benchmark is asserted without a named source or company data.
- Global proxies are labelled and never hidden in the model.
- Every material assumption has a source, owner, date, and confidence level.
- The model includes sensitivity tests, not just a single-point answer.
- The verdict names the assumptions that would flip it.

## Anti-Patterns

- Inventing CAC, AOV, return-rate, commission, or de-minimis figures.
- Treating gross margin as contribution margin.
- Ignoring payment, FX, failed delivery, returns, or working capital.
- Recommending a campaign budget that the CAC guardrail cannot support.
- Producing a workbook with hard-coded unexplained numbers.

## Outputs

- Unit-economics workbook specification.
- Landed-cost and cost-to-serve model.
- Assumptions register.
- Scenario and sensitivity tests.
- Pricing, discount, and CAC guardrails.
- Financial-viability summary by market/channel.

## References

- [references/unit-economics-workbook-spec.md](references/unit-economics-workbook-spec.md): Workbook tabs, formulas, checks, and outputs.
- [references/assumptions-register-and-verdict.md](references/assumptions-register-and-verdict.md): Assumption tags, confidence scoring, and go/conditional/no-go rules.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| SKU prices, costs, discounts, taxes, duties, fees, fulfilment, returns, and currency assumptions | Company records and verified service-provider or authority sources | Required | Use an explicit range, lower confidence, and block a firm verdict |
| Orders, customers, cohorts, acquisition spend, refunds, and settlement data | Commerce, advertising, payment, logistics, and finance systems | Required for observed economics | Separate scenario economics from observed performance |
| Revenue, inventory, refund, FX, tax, and settlement treatment | Chwezi Accounting Doctrine | Required | Stop finance conclusions pending doctrine and reconciliation |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Unit-economics workbook | Founder, finance lead, adviser, or investor | Formulae are transparent, inputs trace to sources, currencies reconcile, and error checks pass |
| Market and pricing verdict | Commercial and operations owners | Go, conditional, or no-go follows stated contribution-margin and confidence rules |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumptions and source register | Input, value or range, source, date, confidence, and owner | Every load-bearing input is verified, bounded, or visibly missing |
| Reconciliation and sensitivity evidence | Check sheet and scenario table | Order, refund, settlement, inventory, and currency totals reconcile; key sensitivities are shown |

## Capability Contract

Read or search access is required; editing or mutation is allowed only with authorised permission.

Read and calculation access are required. Do not change live prices, discounts, ads, shipping rules, tax settings, or payments. Spending, production mutation, market launch, tax conclusions, and certification require explicit authority and relevant finance, tax, legal, and operational review.

## Degraded Mode

Fallback:

If transaction data, provider quotes, exchange rates, or execution tools are unavailable, produce a qualified scenario-only model with ranges and checks marked `not assessed`. Do not issue a firm go verdict where a load-bearing cost or reconciliation is missing.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Contribution after variable costs is negative in the base case | No-go or redesign price, basket, sourcing, or fulfilment | Scaling negative margin |
| Margin is positive only under weak assumptions | Conditional verdict with validation tasks | False confidence |
| Cohort retention is unavailable | Do not annualise LTV from guesswork | Inflated acquisition budget |
| Accounting or tax treatment changes the result | Apply Chwezi doctrine and professional review | Incorrect margin or revenue |

## Workflow

1. Confirm decision, market, channel, customer, fulfilment route, currency, tax basis, and model grain.
2. Gather SKU, order, cohort, acquisition, payment, logistics, return, tax, and settlement evidence.
3. Map revenue, inventory, refund, FX, tax, and settlement treatment to current Chwezi doctrine.
4. Build the workbook from the linked specification and register every input with source and confidence.
5. Reconcile orders to refunds and settlements, then calculate contribution by SKU, order, cohort, channel, and market.
6. Stress price, basket, CAC, return rate, duty, delivery, and FX; stop if a missing load-bearing input prevents a bounded result.
7. Apply the linked verdict rules and define validation actions for conditional cases.
8. Release with formula checks, unassessed items, source dates, and professional-review status visible.

## Quality Standards

The model must avoid blended averages that hide loss-making segments, use reconciled finance definitions, and expose source, confidence, sensitivity, and downside. A verdict is only as strong as its weakest load-bearing input.

## Anti-Patterns

- Calling revenue less product cost gross margin while ignoring payment and fulfilment. Fix: calculate contribution after all order-variable costs.
- Using platform GMV as company revenue. Fix: apply principal-agent doctrine and the actual take rate.
- Annualising one repeat purchase into LTV. Fix: use observed cohorts or a bounded scenario.
- Omitting returns because cash arrives first. Fix: model return probability, reverse logistics, refund, and write-off.
- Mixing currencies at one spot rate. Fix: state rate source, timing, spread, settlement, and stress range.
- Issuing a go verdict with missing duty or delivery quotes. Fix: mark it conditional and obtain verified inputs.

## Worked Example

A Ugandan seller appears profitable at product margin but loses money after cross-border delivery, payment fees, returns, and FX spread. The model should show the loss per order, test a higher basket threshold, and return conditional or no-go rather than recommending more acquisition spend.
<!-- dual-compat-end -->
