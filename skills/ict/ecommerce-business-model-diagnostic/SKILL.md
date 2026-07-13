---
name: ecommerce-business-model-diagnostic
description: Use when assessing an operating e-commerce, marketplace, D2C, B2B, social-commerce, or dropship company for business-model viability, cross-border readiness, diagnostic scoring, and a 90-day improvement plan.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# E-Commerce Business Model Diagnostic
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Overview

Use this skill to produce evidence-based needs assessments for operating e-commerce companies. It replaces generic SWOT analysis with a structured diagnostic across business model, digital operations, customer trust, logistics, payments, governance, financial management, compliance, and cross-border readiness.

The diagnostic is designed for donor-funded BDS programmes where several companies must be assessed consistently and the findings must feed technical assistance, unit-economics modelling, export marketing, and action planning.

## Use When

- Assessing an e-commerce company for needs, investment readiness, export readiness, or technical assistance.
- Creating a company diagnostic report, maturity scorecard, or 90-day improvement plan.
- Comparing several selected companies using a consistent diagnostic protocol.

## Do Not Use When

- Use `ecommerce-unit-economics-and-cross-border-margin-model` instead when the task is only a quantitative margin, pricing, CAC, LTV, or market verdict.
- The company has no operating commerce activity or evidence to assess.
- You only need a full bankable business plan; use the broader plan workflow and load this as a diagnostic input.
- You lack permission to use confidential company data.

## Required Inputs

- Founder/manager interview notes and company goals.
- Storefront/app/social-commerce channels and customer journey evidence.
- Available analytics, orders, complaints, returns, payment, logistics, marketing, and finance data.
- Target cross-border markets and current operating countries.
- Confidentiality, consent, and data-minimisation constraints.

## Workflow

1. Map the business model on a one-page canvas and classify the revenue model.
2. Score the eight core domains: digital operations, data sharing, governance, marketing, logistics and fulfilment, customer management, financial management, and regulatory compliance.
3. Test cross-border customer fit: language, trust, payment, delivery, returns, proof, support, and localisation.
4. Identify the binding constraint. Name the single constraint most limiting cross-border growth, then list secondary constraints.
5. Handoff margin and working-capital questions to the unit-economics skill. Do not assert margin quality without a model.
6. Convert findings into three to five ranked moves with owner, evidence, cost level, effort, dependency, and 90-day milestone.
7. Produce a founder-readable diagnostic report and a donor-safe summary.

## Quality Bar

- Every score has evidence, not opinion.
- The binding constraint is explicit and defensible.
- Recommendations are ranked and sequenced.
- Financial claims reconcile with the unit-economics model.
- Confidential data is protected and donor reports aggregate or anonymise sensitive details.
- Benchmarks are sourced, dated, and labelled as local, company, global proxy, or indicative.

## Anti-Patterns

- A generic SWOT with no domain scores or evidence.
- Listing many weaknesses without naming the binding constraint.
- Using global e-commerce benchmarks as if they were EAC facts.
- Producing recommendations that do not become an owned action plan.
- Exposing confidential company data in donor-facing synthesis.

## Outputs

- Business-model canvas and revenue-stream map.
- Domain maturity scorecard with evidence notes.
- Cross-border fit test.
- Binding-constraint analysis.
- Unit-economics handoff notes.
- 90-day priority improvement plan.
- Company diagnostic report template.

## References

- [references/diagnostic-scorecard.md](references/diagnostic-scorecard.md): Domains, maturity scoring, evidence rules, and binding-constraint logic.
- [references/company-report-template.md](references/company-report-template.md): Needs-assessment report structure and donor-safe summary format.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Business-model, channel, customer, order, fulfilment, return, payment, and operating data | Company systems, interviews, and records | Required | Score the missing domain `not assessed` and request evidence |
| Market and cross-border requirements | Verified marketplace, logistics, payment, tax, and regulatory sources | Conditional | Limit the finding to domestic readiness and flag verification gaps |
| Finance definitions and reconciled sales, refund, inventory, settlement, and margin data | Chwezi Accounting Doctrine and finance records | Required for financial conclusions | Withhold the financial score pending doctrine and reconciliation |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Evidence-backed diagnostic scorecard | Company leadership, adviser, or programme manager | Each domain score cites evidence, confidence, and a material gap |
| 90-day action plan and cross-border verdict | Owners and delivery partners | Actions target the binding constraint, name owner, timing, dependency, measure, and stop condition |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Diagnostic evidence register | Source, observation, score, confidence, and gap table | No score is based only on management assertion where system evidence should exist |
| Finance quality-gate result | Reconciliation and doctrine-review log | Sales, refunds, inventory, settlements, and margin findings use current Chwezi doctrine |

## Capability Contract

Read or search access is required; editing or mutation is allowed only with authorised permission.

Diagnosis defaults to read-only access. Do not change storefronts, prices, advertisements, integrations, marketplace settings, stock, payments, or customer data. Any production mutation, spending, or compliance claim requires explicit authority and the appropriate finance, legal, privacy, and security review.

## Degraded Mode

If systems, files, network sources, or financial evidence are unavailable, score the affected domain `not assessed`, lower confidence, and return the narrowest useful evidence request and conditional action. Never convert missing evidence into maturity.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| One weak domain constrains several others | Prioritise the binding constraint first | A scattered 90-day plan |
| Domestic economics and operations are unproven | Defer cross-border expansion | Scaling losses and service failures |
| Evidence conflicts with interview claims | Use verified records and flag the discrepancy | Optimism-biased scoring |
| Financial records do not reconcile | Route to Chwezi doctrine and mark finance unassessed | False viability verdict |

## Workflow

1. Confirm business model, stage, geography, decision, audience, and access boundary.
2. Collect operating evidence across customer, channel, merchandising, fulfilment, returns, payment, data, team, and finance.
3. Reconcile sales, refunds, inventory, settlements, and margin definitions under Chwezi doctrine; stop financial scoring if they do not reconcile.
4. Score each domain using the linked scorecard, attaching source and confidence.
5. Identify the binding constraint and test domestic and cross-border readiness separately.
6. Build a sequenced 90-day plan with owners, dependencies, measures, and stop conditions.
7. Challenge the verdict against downside cases and inaccessible evidence; recover by narrowing the conclusion.
8. Release the report using the linked template with unassessed domains and assumptions visible.

## Quality Standards

The diagnosis must distinguish fact, assertion, inference, and missing evidence. Scores must drive the recommended sequence; financial conclusions must pass reconciliation and Chwezi doctrine review.

## Anti-Patterns

- Scoring from an interview alone. Fix: seek transaction, platform, fulfilment, and finance evidence.
- Averaging away a critical failure. Fix: identify the binding constraint and apply gating logic.
- Recommending export before domestic margin is known. Fix: complete the unit-economics model first.
- Treating gross merchandise value as revenue. Fix: apply the correct principal-agent and revenue doctrine.
- Listing tools as the action plan. Fix: name the operating change, owner, measure, and dependency.
- Passing an inaccessible domain. Fix: mark it `not assessed` and qualify the verdict.

## Worked Example

A social-commerce seller has strong demand but cannot reconcile mobile-money receipts to orders and returns. Score customer demand separately, leave finance unassessed, prioritise order-to-settlement reconciliation, and defer cross-border marketing until contribution margin can be trusted.
<!-- dual-compat-end -->
