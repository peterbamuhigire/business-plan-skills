---
name: saas-gtm-motion-design
description: Design the go-to-market motion for a SaaS / ICT plan — PLG (product-led growth), sales-led, hybrid, marketplace, channel-partner. Maps motion to ACV, sales-cycle, customer state, methodology (transactional / solution / consultative / provocative), and team composition. The master decision that determines marketing budget, sales hiring, pricing architecture, and unit economics.
---

# SaaS GTM Motion Design Skill

## Overview

The GTM motion is the master upstream decision in any SaaS plan. It determines pricing structure, sales-team design, marketing channel mix, customer-success operating model, and the entire financial profile. This skill forces an explicit, defended GTM-motion choice — not the lazy default of "we'll do sales and marketing."

## Use When

- A new SaaS plan is being built — run this before Section 07 detailing
- The current GTM is producing inconsistent results (suggests motion-mismatch)
- The plan combines incompatible motions (e.g. $50k ACV with 30-day cycle)
- Considering a motion expansion (PLG → enterprise; or sales-led → channel)

## Do Not Use When

- The plan has already secured PMF and a working channel, and the motion is established and producing healthy economics

## Required Inputs

- Target ICP and ACV range
- Customer state (do they know they have the problem? do they know solutions exist?)
- Product self-serve capability (can a customer use it without onboarding help?)
- Sales-cycle assumption
- Team composition / capability
- Geography (African enterprise sales cycles are 50–100% longer than US benchmarks)

## Workflow

1. **Map customer state** to one of the five WBD methodologies (DIY / Transactional / Solution / Consultative / Provocative).
2. **Map ACV** to compatible motions (see decision matrix in references).
3. **Match cycle length** — methodologies have characteristic cycle lengths; the plan's projection must reconcile.
4. **Decide PLG vs sales-led vs hybrid:**
   - PLG: high-volume, low-touch, self-serve, low ACV. Atlassian, Slack, Calendly, Notion path.
   - Sales-led: high-touch, low-volume, high ACV, complex deal. Salesforce, Workday, ServiceNow path.
   - Hybrid: PLG generates leads, sales-led converts to enterprise. HubSpot, Slack, Atlassian dual funnel.
   - Marketplace: facilitating buyers and sellers; different economics (Shopify, Stripe).
   - Channel-partner: VARs, SIs, distributors carry the sale. Common for vertical SaaS in fragmented markets.
5. **Design the funnel** for the chosen motion: top (Educate), middle (Prospect / Visit), bottom (Win), retention (Grow).
6. **Specify the named sales plays** that operate in the motion.
7. **Compute the team composition** from `saas-sales-org-design-and-capacity-planning`.
8. **Reconcile with pricing** — PLG needs simple, transparent pricing; enterprise needs custom pricing.
9. **Africa-test** — does the motion work given African sales-cycle / channel realities?

## Quality Bar

- Single GTM motion declared (or hybrid with explicit boundaries)
- Motion reconciles with ACV, sales-cycle, customer state
- Named sales plays (not generic "outbound")
- Team composition computed from motion
- Pricing architecture compatible with motion
- Africa-adjusted cycle and motion if relevant

## Anti-Patterns

- "We'll do both PLG and enterprise" without explicit boundaries
- $50k ACV with 30-day projected cycle (impossible)
- Provocative methodology in markets with no incumbent budget (no money to be unlocked)
- PLG without a product that delivers value in <10 minutes
- Channel-partner motion without channel-partner economics modelled

## Outputs

- Declared GTM motion with justification
- Funnel design (Educate / Prospect / Win / Grow stages with conversion benchmarks)
- Named sales plays
- Team composition specification (feeds into Section 09)
- Pricing-architecture compatibility check
- Africa-adjustment commentary

## References

- `references/saas-gtm-motion-decision-template.md` — full decision matrix and worked examples
- `book-extractions/vanderkooij-saas-sales-method-ae-extraction.md` — five methodologies
- `book-extractions/walling-saas-playbook-extraction.md` — dual-funnel cheat code
- `book-extractions/cotton-run-a-saas-business-extraction.md` — sales engine essay
- `skills/saas-sales-org-design-and-capacity-planning/SKILL.md` — sister skill

## Africa / Uganda Application Notes

- Enterprise sales cycles in African markets run 12–24 months for $50k+ deals; plan accordingly.
- Outbound sales is more cost-effective than US benchmarks because SDR labour is cheaper; African SaaS often runs outbound-first.
- Channel-partner motion via local resellers, SI partners (TechnoBrain, IPMC, Computech), or industry consortia is underused in African B2B SaaS; consider seriously for vertical plays.
- PLG works for products with global appeal and English-language UX; harder for vertically focused African plays where in-language onboarding matters.
- WhatsApp Business is a primary B2B sales channel; design the motion with WhatsApp at every stage.
