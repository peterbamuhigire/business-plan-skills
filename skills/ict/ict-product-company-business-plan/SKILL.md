---
name: ict-product-company-business-plan
description: Generate or audit the business plan for an ICT product company (non-SaaS) — licensed software, embedded systems, hardware-plus-software, on-premise enterprise software. Different unit economics from SaaS (one-time fee + maintenance vs recurring subscription). Use when the product is sold under perpetual licence, as a unit, or with a hardware component.
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
