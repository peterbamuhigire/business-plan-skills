---
name: ecommerce-unit-economics-and-cross-border-margin-model
description: Use when modelling e-commerce unit economics, landed cost, cross-border contribution margin, CAC, LTV, payment fees, shipping, returns, platform commissions, pricing guardrails, or market go/no-go viability.
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
