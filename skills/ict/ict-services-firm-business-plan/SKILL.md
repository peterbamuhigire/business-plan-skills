---
name: ict-services-firm-business-plan
description: Use when generating or reviewing a business plan for an ICT services firm, digital agency, implementer, or systems integrator with project revenue, utilisation, bench, pipeline, and productisation decisions; use `ict-product-company-business-plan` for products and SaaS skills for subscriptions.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# ICT Services Firm Business Plan Skill

## Overview

ICT services firms (digital agencies, systems integrators, IT consultancies, dev shops) have a fundamentally different economic structure from SaaS: revenue is people-bound, gross margin is 25-45% (vs SaaS 70-85%), and scaling is linear, not platform-leveraged. This skill generates the business plan for this specific company profile, with explicit guidance on the productisation roadmap (the path from services revenue to recurring revenue).

## Use When

- The company sells custom development, integration, consulting, or managed services as primary revenue
- The company is an agency / SI / consultancy considering productising
- A hybrid firm is moving services revenue toward SaaS / recurring product revenue

## Do Not Use When

- Pure SaaS company with services as <10% of revenue (use SaaS skills)
- Pure product / hardware company

## Required Inputs

- Current service offerings (custom dev, consulting, managed services, training)
- Current revenue, headcount, utilisation
- Bench / pipeline / book-to-bill
- Capability mix (engineers, designers, PMs, BAs)
- Geographic footprint
- Productisation candidates (services repeated 5+ times)

## Workflow

1. **Map the service offerings** — discrete service lines with pricing, gross margin, demand drivers.
2. **Compute utilisation economics**:
   - Billable utilisation target (60-75% healthy)
   - Realisation rate (% of billed hours that get paid)
   - Per-hour / per-day / per-project rate by capability
   - Bench cost
3. **Build the revenue model**:
   - Project-based revenue (fixed-fee or time-and-materials)
   - Retainer revenue (monthly recurring services)
   - Managed-services revenue (recurring; high margin if multi-tenant ops)
   - Product / SaaS revenue (if productised)
4. **Plan the productisation roadmap**:
   - Identify services repeated 5+ times — these are candidates for productisation
   - Score each by automation potential, market demand, defensibility
   - Build the path from custom-build → repeated-template → semi-product → product / SaaS
5. **Design the org structure** — capability pools (Eng, Design, PM, BA, DevOps), client pods, productisation team.
6. **Compute the financial profile**:
   - Gross margin (25-45% typical for services; 60-75% for managed services)
   - S&M as % of revenue (15-25%)
   - G&A (8-12%)
   - Operating margin (10-20% healthy; 5-15% for growth-stage)
   - Cash conversion (project receivables; usually 60-90 days DSO)
7. **Plan the recurring-revenue evolution** — services → managed services → SaaS over 3-5 years.
8. **Cross-reference**: Section 03 (Products) describes services + future product; Section 04 (Market) services market; Section 10 (Financials) services P&L with productisation transition.

## Quality Bar

- Service-line P&L explicit (gross margin per service line)
- Utilisation targets named (with capacity formula)
- Productisation roadmap with named candidates and scoring
- Recurring-revenue evolution thesis
- Org structure supports both services delivery and product development
- Cash conversion (DSO) realistic

## Anti-Patterns

- "We're a services company that will become SaaS" with no productisation roadmap
- 100% utilisation target (no bench = no growth capacity)
- Hourly billing without realisation discipline
- Services-only model with no recurring-revenue thesis (linear growth ceiling)
- Productising too early (before service is profitable + repeated)

## Outputs

- Service-line P&L with gross margin per line
- Utilisation model
- Productisation roadmap (candidates, scoring, sequencing)
- Recurring-revenue evolution
- Org chart by capability pool
- Cash conversion model

## References

- `book-extractions/walling-saas-playbook-extraction.md` — stair-step method (often via services to product)
- `book-extractions/practical-small-business-guides-extraction.md` — SME services discipline
- `book-extractions/cotton-run-a-saas-business-extraction.md` — when services revenue makes sense in SaaS
- `skills/ict-product-company-business-plan/SKILL.md` — sister skill for product (non-SaaS) firms
- `skills/saas-mvp-and-product-market-fit-strategy/SKILL.md` — for productisation MVP

## Africa / Uganda Application Notes

- ICT services in Africa often operates as the on-ramp to SaaS (agency → repeatable project → product). The Stair-Step in African context.
- DSO is often longer in Africa (90-180 days for public-sector / large-corporate clients). Plan working capital accordingly.
- Public-sector procurement is a major services market but has 6-18 month cycles; requires dedicated sales motion.
- Donor-funded projects often have specific reporting and pricing structures (FAR rates, IFRS specific cost-categories).
- Multi-country services delivery (delivering Nigerian projects from Kenyan office, etc.) requires VAT, withholding-tax, transfer-pricing discipline.
- Productisation candidates often emerge from public-sector / donor-funded work: tax-platform, beneficiary-tracking, monitoring-evaluation tools.
- Labour-cost arbitrage is real for African ICT services — selling US/EU rates with local-cost delivery produces high margin.
- Hybrid model is increasingly common: services revenue funds the SaaS build; SaaS revenue eventually exceeds services. Pattern: Andela, Soft, Genesys Tech (Nigeria).

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Service catalogue, project history, pipeline, rates, contracts, staffing, time, utilisation, and delivery evidence | Founder, sales, delivery, HR, and systems | Required | Return a discovery gap list and qualified plan |
| Customer, competitor, procurement, partner, and channel evidence | Primary research and verified market sources | Required | Avoid invented demand and pipeline conversion |
| Revenue, work in progress, payroll, subcontractor, tax, FX, receivable, and cash treatment | Chwezi Accounting Doctrine and finance records | Required for projections | Stop financial conclusions pending doctrine and reconciliation |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| ICT services-firm plan input pack | Business-plan pipeline, founder, lender, or investor | Demand, sales capacity, delivery capacity, utilisation, margin, cash, growth, and risks reconcile |
| Services economics and capacity register | Sales, delivery, HR, finance, and reviewers | Rates, effort, utilisation, bench, subcontracting, collection, and hiring assumptions are sourced and testable |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Pipeline-to-capacity traceability | Opportunity, probability, timing, skills, effort, owner, and evidence table | Forecast work can be delivered by available or funded capacity |
| Finance quality-gate result | Doctrine mapping, model reconciliation, and professional-review status | Revenue, WIP, payroll, tax, FX, receivables, and cash treatment pass Chwezi doctrine |

## Capability Contract

Analysis defaults to read-only. Edit the plan only when authorised. Do not change CRM probabilities, rates, contracts, staffing, payroll, client systems, or production delivery; spending, hiring, contracting, certification, and financial claims require explicit authority and qualified review.

## Degraded Mode

Without time data, contract history, pipeline evidence, current market sources, or reconciled finance records, return a scenario-based module with ranges and validation actions. Mark utilisation, margin, or cash checks `not assessed` rather than assuming industry benchmarks are achieved.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Revenue scales mainly with billable people or project capacity | Use the services-firm model | False software scalability |
| Revenue scales mainly with product units or licences | Route to `ict-product-company-business-plan` | Hiding product lifecycle economics |
| Recurring subscriptions dominate value and revenue | Route to the SaaS stack | Wrong retention and gross-margin model |
| Financial treatment is material or disputed | Apply Chwezi doctrine and professional review | Misstated revenue or cash |

## Workflow

1. Classify service lines, contract types, clients, geography, decision, and audience; stop if product or subscription economics dominate.
2. Gather pipeline, win rate, cycle, backlog, rates, effort, utilisation, bench, skills, delivery, receivables, and client-concentration evidence.
3. Map lead-to-cash and project delivery, including scope change, acceptance, billing, collection, support, and knowledge retention.
4. Build capacity and economics under current Chwezi doctrine, separating billable delivery, overhead, subcontracting, and product investment.
5. Reconcile sales pipeline with delivery capacity, hiring lead time, working capital, and funding.
6. Stress delays, scope creep, attrition, bench, collection, client concentration, and FX.
7. Recover from evidence gaps by narrowing claims and defining dated validation or instrumentation work.
8. Release only after business-logic, finance, evidence, risk, and anti-slop gates pass.

## Quality Standards

The plan must prove how leads become collectable engagements and how delivery capacity turns into contribution and cash. It must expose bench, concentration, hiring, acceptance, and collection constraints rather than hiding them in a revenue growth rate.

## Anti-Patterns

- Forecasting revenue without delivery hours. Fix: translate backlog and pipeline into skills, effort, utilisation, and timing.
- Treating all staff cost as variable COGS. Fix: apply the documented payroll, bench, overhead, and delivery allocation policy.
- Assuming proposals equal pipeline. Fix: use stage evidence, probability, cycle, and decision dates.
- Ignoring client acceptance and receivable timing. Fix: model milestones, sign-off, invoicing, disputes, and collection.
- Funding a product from services without ring-fencing capacity. Fix: show people, cash, milestones, and stop conditions.
- Finalising project revenue without Chwezi review. Fix: map contracts and recognition evidence to doctrine and professional sign-off.

## Worked Example

A systems integrator has three likely projects but only one implementation team. Sequence the opportunities by evidence and start date, model subcontracting or hiring lead time, and cap recognised capacity rather than booking all three at once.
<!-- dual-compat-end -->
