---
name: ict-services-firm-business-plan
description: Generate or audit the business plan for an ICT services / digital-agency / systems-integrator firm — project-based revenue, utilisation, bench management, productisation roadmap, recurring-revenue evolution. Different financial profile from SaaS (lower gross margin, headcount-bound revenue, project-cycle cash flow). Use when the company is an ICT services firm, not a pure SaaS company.
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
