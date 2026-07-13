---
name: saas-pricing-and-packaging-strategy
description: Use when a SaaS plan has a single flat price (no tiering, no expansion mechanic). Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Pricing & Packaging Strategy Skill

## Overview

Apply SaaS-specific pricing-architecture discipline on top of Kennedy/Marrs premium positioning. Where `meta-pricing-strategy` defends the right to charge premium prices, this skill designs the package architecture that makes premium SaaS pricing operationally and commercially defensible: tiering, pricing dimension, freemium policy, expansion mechanics, annual prepay, and the experiment cadence by which pricing stays alive across the business lifetime.

## Use When

- A SaaS plan has a single flat price (no tiering, no expansion mechanic)
- Pricing dimension is unclear or doesn't scale with customer value
- The plan claims "expansion revenue" but has no architectural mechanism for it
- Freemium is being considered (or already in use without justification)
- Annual prepayment uptake is below 30% and cash flow is constrained
- The team has not run a pricing experiment in >12 months
- An African plan is using USD pricing without an FX-pass-through or local-currency strategy

## Do Not Use When

- The plan is pre-PMF — pricing experiments before PMF is theatre
- The product is being given away pre-launch as a deliberate acquisition strategy with explicit time-bound exit
- A regulatory ceiling caps the price (regulated utilities, government contracts)


- For `saas-pricing-and-packaging-strategy`, route to the corresponding cross-sector meta skill instead when recurring-revenue SaaS logic is not material.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Pricing And Packaging Strategy brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Current pricing structure (tiers, prices, dimension)
- Customer segmentation (SMB / Mid / Enterprise / B2C)
- Top-3 competitor prices and packages
- Churn and expansion data by tier
- Cost-per-customer by tier (per-tenant cost telemetry if available)
- Country / currency context

## Workflow

1. **Audit current pricing** against `references/saas-pricing-and-packaging-strategy-template.md` checklist.
2. **Select the pricing dimension** that aligns with customer value scaling:
   - Per seat / user — when value scales with team size (Slack, Notion)
   - Per usage / consumption — when value scales with volume (Twilio, Stripe, AI APIs)
   - Per outcome / event — when value is event-driven (Calendly meetings, Loom views)
   - Per record / account — when value scales with managed entity count (HubSpot contacts, Salesforce records)
   - Hybrid — most modern SaaS combines a base + usage
3. **Design the tier ladder** — good / better / best (three-tier default; sometimes four). Each tier has a clear ICP, a clear feature set, and a clear price.
4. **Anchor with a high tier** — even if 5% of customers buy it, a high tier makes the middle tier feel reasonable and creates upsell space.
5. **Build the expansion mechanic** — at what point does a customer naturally move up? (More seats; more usage; new module; tier upgrade.) Without an expansion mechanic, NRR is capped at 100%.
6. **Decide freemium policy** — only valid if (a) free tier delivers genuine value, (b) paid-tier upgrade trigger is obvious, (c) infra cost per free user is <$1/month, (d) the company has the brand reach to attract millions. Otherwise drop freemium for a free-trial.
7. **Design annual prepayment incentive** — typically 10–20% discount for annual prepay. Working-capital trough deepens without prepayment.
8. **Localise pricing for Africa** — USD for export tier, local currency for domestic tier, with explicit FX-pass-through clause for >10% currency movement.
9. **Install pricing experiment cadence** — quarterly small experiments (subject lines, tier names, anchor positioning), annual large experiments (price increase, packaging change). Decision log every experiment.
10. **Cross-reference**: pricing must reconcile with Section 04 (market), Section 06 (competitive), Section 07 (sales process — discount discipline), Section 10 (financial projections), and `meta-pricing-strategy` for the premium positioning layer.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the SaaS packaging architecture and that the decision concerns tier boundaries, price metric, limits, and expansion path.
- **Stop condition:** halt the affected conclusion if required evidence is missing (value metric, segment needs, entitlement costs, usage, and churn evidence) or if the work could lead to this identified risk: creating packages customers can game or that detach price from value.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Pricing dimension explicitly chosen and justified by customer value-scaling logic
- Tier ladder with three or four named tiers, each with distinct ICP
- High-anchor tier present
- Expansion mechanic documented (seat / usage / module / tier upgrade path)
- Annual prepayment incentive in place
- Freemium justified against the four-condition test, or replaced with free-trial
- African plans: FX strategy explicit
- Pricing experiment cadence installed (quarterly + annual)
- Pricing flows through to projections, sales materials, marketing copy, contracts

## Anti-Patterns

- Single-tier flat pricing (no tiering)
- Pricing dimension that doesn't scale with customer value (e.g. per-organisation when customer size varies 100×)
- Freemium without the four-condition justification
- Monthly-only billing in enterprise SaaS (working capital trap)
- "We'll figure out enterprise pricing later" (lost revenue)
- USD pricing in African market without FX strategy
- Pricing page hasn't changed in 18+ months (decay)
- No expansion mechanic but plan assumes NRR > 100%


- Applying the wrong neighbouring route to saas pricing and packaging strategy. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pricing And Packaging Strategy deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Pricing audit (current state vs target state)
- Tier table with ICP, feature set, price, target % of revenue
- Pricing-dimension decision document
- Expansion-mechanic specification
- Annual prepayment + discount policy
- Localisation / FX strategy (Africa)
- Pricing-experiment plan with cadence
- Pricing page copy outline
- Updates required to Section 07, 10, 11

## References

- `references/saas-pricing-and-packaging-strategy-template.md` — full architecture and worked examples
- `skills/meta-pricing-strategy/SKILL.md` — Kennedy/Marrs premium positioning (run before this for premium plans)
- `book-extractions/walling-saas-playbook-extraction.md` — SaaS pricing principles (chapter 9)
- `book-extractions/mersch-hacking-saas-extraction.md` — pricing models by SaaS segment
- `book-extractions/cotton-run-a-saas-business-extraction.md` — pricing-publication discipline

## Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Price-list review | Quarterly | CFO + Head of GTM |
| Tier-mix analysis | Monthly | Head of GTM |
| Expansion-revenue review | Monthly | Head of CS + CFO |
| Pricing experiment | Quarterly | Head of GTM |
| Major price increase | Annually | CEO + Board |
| FX review (Africa) | Quarterly | CFO |

## Africa / Uganda Application Notes

- Local-currency pricing with annual FX-escalator clause is more sustainable than USD pricing for African SaaS targeting SMB / mid-market segments.
- USD pricing acceptable for enterprise / multi-country / regional plays; couple with quarterly FX adjustment for new contracts.
- Annual prepayment uptake in Africa typically 20–40% (vs 60–80% US); design the prepayment incentive aggressively (15–20% discount) to push uptake.
- Mobile-money fees (1–2%) materially affect tier economics for low-ARPU tiers; design the lowest tier ARPU to absorb the fee with margin.
- Pricing pages should be in local language for the lowest tiers — code-switching (English + local-language emphasis) often improves conversion.
- Public-sector and NGO buyers in Africa often require quotation in local currency with VAT, withholding-tax handling, and specific tax-clearance documentation. Build this into the contracting flow.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| SaaS packaging architecture decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to creating packages customers can game or that detach price from value. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the SaaS packaging architecture; drafting package tests without changing production billing is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If value metric, segment needs, entitlement costs, usage, and churn evidence cannot be obtained, return a qualified SaaS packaging architecture covering only the checks that remain supportable. Leave this decision unresolved: tier boundaries, price metric, limits, and expansion path. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: tier boundaries, price metric, limits, and expansion path | Record the conclusion, source trail, owner, and review trigger in the SaaS packaging architecture. | Risk of creating packages customers can game or that detach price from value |
| Material evidence conflicts or remains uncertain | Prototype the competing package boundaries with the target segment and model entitlement cost, expansion, and downgrade behaviour. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: value metric, segment needs, entitlement costs, usage, and churn evidence | Mark the decision on tier boundaries, price metric, limits, and expansion path `not assessed` in the SaaS packaging architecture, and send it to the product, commercial, and finance owners. | Otherwise, the work risks creating packages customers can game or that detach price from value |

## Quality Standards


Accept the SaaS packaging architecture only when evidence is sufficient for this decision: tier boundaries, price metric, limits, and expansion path. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of creating packages customers can game or that detach price from value.

## Worked Example


Heavy users remain on the entry tier because limits do not track value. Redesign the value metric and entitlements, model gross margin and downgrade behaviour, then test the packages with the affected segment.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the SaaS packaging architecture, using the reporting basis and effective date supported by value metric, segment needs, entitlement costs, usage, and churn evidence. Reconcile the treatment to the model and narrative, and have the finance owner and commercial lead review the treatment, reconciliation, and exposure to this risk: creating packages customers can game or that detach price from value.

<!-- dual-compat-end -->
