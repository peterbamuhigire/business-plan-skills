---
name: ict-product-company-business-plan
description: Use when generating or reviewing a business plan for a non-SaaS ICT product company selling licensed software, embedded systems, hardware-software products, or on-premise systems; use `ict-services-firm-business-plan` for project-led services and SaaS skills for subscriptions.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# ICT Product Company Business Plan Skill

## Overview

Not every ICT plan is SaaS. Licensed-software, embedded-systems, hardware-plus-software, and on-premise enterprise-software companies have a fundamentally different economic model. This skill produces the plan for that company profile, with explicit guidance on the SaaS-transition path that most of these companies should plan over time.

## Use When

- Product is sold as a one-time licence (perpetual or term)
- Product has a hardware component (M-KOPA, BasiGo, Sun King, Helium)
- Product is on-premise enterprise software
- Hybrid (one-time licence + recurring maintenance + optional SaaS layer)

## Do Not Use When

- Pure SaaS (use SaaS skills)
- Pure services (use `ict-services-firm-business-plan`)

## Required Inputs

- Product description and revenue model (licence + maintenance / hardware + service)
- Unit pricing and cost
- Sales cycle and channels
- Manufacturing / supply-chain (if hardware)
- Maintenance / support cost profile

## Workflow

1. **Define the revenue model:**
   - Perpetual licence + annual maintenance (15-25% of licence fee)
   - Term licence (1-3 years)
   - Hardware-plus-software bundle (one-time + recurring service)
   - PAYG / financed (M-KOPA model)
2. **Compute the unit economics**:
   - Revenue per unit (one-time + recurring components)
   - Cost per unit (hardware BOM if applicable; software COGS; install/onboarding)
   - Gross margin (typically 40-65% for hardware-inclusive; 50-75% for pure licensed-software)
   - Maintenance attach rate (target 90%+)
   - Maintenance renewal rate
3. **Plan the SaaS-transition path** (most of these companies should plan one):
   - Phase 1: Pure perpetual + maintenance (current)
   - Phase 2: SaaS offering for new customers (some cannibalisation acceptable)
   - Phase 3: Migrate existing customers to SaaS
   - Mersch's perpetual-vs-SaaS chapter is the source
4. **Compute the financial profile**:
   - Higher one-time revenue per customer than SaaS
   - Lumpier cash flow (large up-front + smaller recurring)
   - Different working-capital pattern (no Working Capital Trough but unit costs)
   - Inventory if hardware
5. **Hardware-specific considerations**:
   - BOM (Bill of Materials) cost
   - Manufacturing partner / EMS
   - Supply-chain (Africa: shipping, customs, FX-on-import)
   - Inventory management
   - Field-service / repair operation
6. **Design the sales motion** — typically channel + direct, longer cycles, RFP-friendly.
7. **Plan the productivity moat** — how does the product avoid commoditisation?

## Quality Bar

- Unit economics computed per unit, not aggregate
- Maintenance attach + renewal rate explicit
- SaaS-transition path planned (or explicit reason not to)
- Hardware supply-chain modelled (if applicable)
- Sales cycle and channel structure designed
- Cash flow recognises lumpy nature

## Anti-Patterns

- Treating one-time licence as if it were ARR (it isn't)
- Hardware product without supply-chain plan
- No maintenance / support contract structure
- "We'll convert to SaaS later" without roadmap
- Underestimating field-service / repair cost
- Ignoring FX on imported hardware

## Outputs

- Unit-economic model per product
- Revenue model (licence + maintenance / PAYG / etc.)
- SaaS-transition roadmap (or rationale for not transitioning)
- Hardware supply-chain plan (if applicable)
- Sales motion and channel structure
- Financial profile distinct from SaaS

## References

- `book-extractions/mersch-hacking-saas-extraction.md` — perpetual vs SaaS comparison (ch. 1)
- `book-extractions/tod-building-multi-tenant-saas-architectures-extraction.md` — MSP vs SaaS clarity
- `book-extractions/haines-how-to-create-a-business-case-extraction.md` — business-case discipline for product investments
- `skills/ict-services-firm-business-plan/SKILL.md` — sister skill
- `skills/saas-unit-economics-and-cohort-model/SKILL.md` — for SaaS-transition modelling

## Africa / Uganda Application Notes

- Hardware-inclusive plans are a major African opportunity (energy access M-KOPA / Sun King / Zola; e-mobility BasiGo / Ampersand; agritech tools Hello Tractor).
- PAYG financing is a powerful African model — combines hardware + software + financing.
- Customs duty, VAT, and shipping costs are material — model explicitly.
- Local assembly often required for tax / local-content reasons — plan partner relationships.
- Field-service network is a real capability (M-KOPA built ~3,000 field agents in Kenya).
- Mobile-money integration is standard for PAYG.
- Public-sector procurement of on-premise software has specific compliance (data localisation, security certification) — plan early.
- The transition from licensed-software to SaaS is harder in African enterprise markets where data-residency concerns and unreliable connectivity favour on-premise.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Product architecture, bill of materials, licences, roadmap, support, installation, and lifecycle evidence | Founder, product, engineering, supplier, and customer records | Required | Return a discovery gap list, not a complete plan |
| Customer, competitor, procurement, channel, pricing, pipeline, and adoption evidence | Primary research and verified market sources | Required | Qualify demand and avoid invented market figures |
| Revenue, inventory, warranty, maintenance, FX, tax, and cash-flow treatment | Chwezi Accounting Doctrine and finance records | Required for projections | Stop financial conclusions until doctrine and model reconcile |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| ICT product-company plan input pack | Business-plan pipeline, founder, lender, or investor | Product, market, delivery, support, economics, funding, and risks reconcile |
| Product economics and lifecycle assumptions register | Finance, product, operations, and investor reviewers | Each price, unit cost, licence, warranty, support, replacement, and capacity assumption has evidence or a range |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Product-to-commercial traceability | Feature, customer problem, evidence, price, delivery, support, and risk matrix | Every roadmap and revenue claim links to customer and operating evidence |
| Finance quality-gate result | Doctrine mapping, reconciled model, and professional-review status | Revenue, COGS, inventory, warranty, maintenance, tax, and cash treatment pass the Chwezi gate |

## Capability Contract

Analysis defaults to read-only. Edit the plan only when authorised. Do not alter product systems, supplier orders, pricing, contracts, production, customer data, or financial records; spending, launch, certification, legal, security, and accounting claims require explicit authority and qualified review.

## Degraded Mode

Without product evidence, customer research, supplier quotes, current sources, or a reconciled finance model, return a qualified plan module and validation backlog. Mark affected checks `not assessed` and do not convert a prototype, letter of intent, or scenario into proven demand or revenue.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Value is delivered mainly by one-time software or hardware sale | Use product and lifecycle economics | Misapplying SaaS metrics |
| Delivery depends mainly on billable projects | Route to `ict-services-firm-business-plan` | Hiding utilisation constraints |
| Value and payment are recurring subscriptions | Route to the SaaS plan stack | Wrong revenue and retention model |
| Revenue or cost treatment is material | Apply Chwezi doctrine and professional review | Misstated projections |

## Workflow

1. Classify the offer as licensed software, embedded, hardware-software, on-premise, or hybrid; stop if SaaS or services dominates.
2. Gather product, customer, channel, procurement, supplier, implementation, support, roadmap, and risk evidence.
3. Map the product lifecycle from manufacture or development through installation, warranty, maintenance, upgrade, and retirement.
4. Build pricing, unit cost, capacity, working-capital, support, and replacement assumptions under current Chwezi doctrine.
5. Reconcile market, operations, staffing, funding, and financial sections with the product roadmap.
6. Stress supplier, FX, defect, warranty, adoption, procurement-cycle, certification, and obsolescence cases.
7. Recover from missing evidence by narrowing claims and adding dated validation actions.
8. Release the module only after business-logic, finance, evidence, risk, and anti-slop gates pass.

## Quality Standards

The plan must show why the product wins, how it is built or sourced and supported, how each unit contributes cash, and how funding bridges the lifecycle. Current claims and finance treatments must be verified or qualified.

## Anti-Patterns

- Treating a perpetual licence as monthly recurring revenue. Fix: separate licence, implementation, maintenance, and upgrade streams.
- Ignoring hardware replacements and warranty returns. Fix: model failure, replacement, service, and reserve assumptions.
- Calling a prototype a market-ready product. Fix: state readiness evidence, certification, backlog, and launch gates.
- Using one supplier quote as a permanent unit cost. Fix: date it, include FX, lead time, minimum order, and sensitivity.
- Forecasting sales without procurement-cycle evidence. Fix: model decision makers, trials, approvals, and payment timing.
- Finalising revenue or inventory treatment without Chwezi review. Fix: retain the doctrine map and professional sign-off status.

## Worked Example

An on-premise school-management product charges a licence plus installation and annual maintenance. Model those streams separately, include deployment capacity and support cost, and do not route it to SaaS unless recurring access is the dominant product and economic model.
<!-- dual-compat-end -->
