---
name: meta-website-investment-planning
description: Use when a business plan includes a website, online store, booking site, content hub, landing pages, portal, web app, or SEO-driven customer acquisition. Use the SaaS pricing skill for recurring-revenue tier architecture.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Website Investment Planning
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Overview

Use this skill to treat a website as a business investment, not a generic online presence. It helps business plans explain what the website will do, why the chosen approach fits the business, how it will be built and operated, and what costs must be included in financial projections.

## Use When

- A business plan includes a website, online store, booking site, content hub, landing pages, portal, web app, or SEO-driven customer acquisition.
- The plan needs to explain website design philosophy, tech stack, website operations, content/SEO, launch, maintenance, or realistic costing.
- The business sells website design/development services and needs productised service tiers, pricing logic, delivery capacity, and margins.
- Website spend appears in startup costs, capex, marketing budget, software subscriptions, or implementation roadmap.

## Do Not Use When

- The business has no material website, digital presence, ecommerce, online marketing, or technology investment.
- A one-line "we will have a website" statement is enough for a very small, non-digital plan.


- Route to `saas-pricing-and-packaging-strategy` instead for recurring-revenue tier architecture.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Website Investment Planning brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Business model, target customers, channels, geography, languages, sales process, and website role.
- Expected pages/features, content ownership, SEO goals, integrations, payment/booking needs, and support requirements.
- Budget constraints, implementation timeline, launch priorities, and country/currency context.
- If planning a website-design service business: team capacity, offer tiers, quality standard, delivery process, and fee policy.

## Workflow

1. Define the website's business role: credibility, local discovery, lead generation, ecommerce, bookings, content authority, recruitment, investor trust, customer support, or software delivery.
2. Choose the correct website type and scope: foundation presence, growth website, premium authority system, ecommerce, web app/portal, landing-page funnel, or content hub.
3. Explain the design philosophy in business-plan language: strategy before design, content/SEO before decoration, mobile-first UX, accessibility, performance, security, analytics, and handover.
4. Select the tech stack based on operating logic: static-first, CMS, WordPress, ecommerce platform, custom application, CRM/payment/booking integrations, hosting, analytics, and content workflow.
5. Build a website investment budget with one-time and recurring costs, including content, SEO, UX, development, QA, launch, hosting, licences, maintenance, analytics, and optimisation.
6. Reconcile the website plan across products/services, marketing, operations, implementation, risk, and financial projections.
7. Run the website investment and costing gate before calling the plan realistic, bankable, investor-ready, or premium.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the website investment case and that the decision concerns what to build now, defer, and budget as recurring operations.
- **Stop condition:** halt the affected conclusion if required evidence is missing (website role, customer journey, scope, and lifecycle costs) or if the work could lead to this identified risk: buying a showcase site that cannot support the acquisition or service model.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The plan explains how the website helps the business make money, reduce risk, support operations, or build trust.
- Website costs are visible and realistic; they are not hidden inside a vague "marketing" line.
- Content, SEO, analytics, maintenance, and post-launch improvement are budgeted where they drive growth.
- The stack choice matches business stage, staff capability, cash flow, risk, and customer expectations.
- For website-design service businesses, the pricing model protects premium delivery standards and avoids sub-premium work.

## Anti-Patterns

- Listing "website and social media" as a marketing tactic with no funnel, content, SEO, or budget.
- Budgeting a one-time build but ignoring hosting, domain, SSL, maintenance, security, backups, content updates, SEO, analytics, or support.
- Assuming a website will generate sales without traffic, proof, conversion paths, and follow-up.
- Recommending ecommerce without operations for catalogue, inventory, delivery, returns, customer support, payments, fraud, and accounting.
- Using cheap website costs in projections while claiming premium brand positioning.


- Applying the wrong neighbouring route to meta website investment planning. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Website Investment Planning deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Website strategy paragraph for a business plan.
- Website operating model and stack explanation.
- Website startup and recurring cost assumptions.
- Website-design service pricing guidance.
- Cross-section reconciliation notes for marketing, operations, finance, risk, and implementation.

## References

- `references/website-investment-costing-gate.md` - website role, design philosophy, stack, cost schedule, service pricing, and cross-section checks.
- `../07-marketing-sales-strategy/SKILL.md` - marketing and sales strategy owner.
- `../08-operations-plan/SKILL.md` - operating model owner.
- `../10-financial-projections/SKILL.md` - financial model owner.
- `../meta-premium-go-to-market/SKILL.md` - use when the website or website service is premium/high-ticket.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Website investment case decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to buying a showcase site that cannot support the acquisition or service model. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the website investment case; drafting scope and cost assumptions without purchasing services is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If website role, customer journey, scope, and lifecycle costs cannot be obtained, return a qualified website investment case covering only the checks that remain supportable. Leave this decision unresolved: what to build now, defer, and budget as recurring operations. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: what to build now, defer, and budget as recurring operations | Record the conclusion, source trail, owner, and review trigger in the website investment case. | Risk of buying a showcase site that cannot support the acquisition or service model |
| Material evidence conflicts or remains uncertain | Cost the minimum conversion path separately from deferred features and approve only the phase tied to a named customer or operating need. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: website role, customer journey, scope, and lifecycle costs | Mark the decision on what to build now, defer, and budget as recurring operations `not assessed` in the website investment case, and send it to the plan owner and website delivery lead. | Otherwise, the work risks buying a showcase site that cannot support the acquisition or service model |

## Quality Standards


Accept the website investment case only when evidence is sufficient for this decision: what to build now, defer, and budget as recurring operations. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of buying a showcase site that cannot support the acquisition or service model.

## Worked Example


A service business budgets a complex portal before validating online enquiries. Fund the measurable lead and booking path first, state recurring content and maintenance costs, and defer the portal behind an adoption trigger.

<!-- dual-compat-end -->
