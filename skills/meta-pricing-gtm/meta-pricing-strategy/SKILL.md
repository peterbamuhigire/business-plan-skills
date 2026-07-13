---
name: meta-pricing-strategy
description: Use when a business plan's projected prices match or undercut competitors without a defensible reason. Use the SaaS pricing skill for recurring-revenue tier architecture.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Premium Pricing Strategy Skill (Kennedy/Marrs + Lycka)

## Overview

Audit and upgrade the pricing strategy inside any business plan section — specifically Section 07 (Marketing & Sales Strategy), Section 10 (Financial Projections), and Section 11 (Funding Request / business model). Applies the Kennedy/Marrs *No B.S. Price Strategy* framework plus Dr. Barry Lycka's Triangle of Preeminence to move the plan from cost-plus or competitor-match pricing to defensible premium positioning.

## Use When

- A business plan's projected prices match or undercut competitors without a defensible reason
- Pricing is set by cost-plus, industry norm, client-dictated, or wild guess (four of Kennedy's five "bad" methods)
- The plan competes against free/subsidised alternatives (government services, open-source, public-sector)
- The plan enters a commoditised category (groceries, fuel, basic services, generic professional services)
- The founder is reluctant to charge what the value supports — common in first-generation entrepreneurs and mission-driven founders
- A recession, currency depreciation, or margin squeeze is prompting a price cut decision

## Do Not Use When

- The business is deliberately a penetration-pricing play (e.g. a platform seeking share for network effects) and investors have explicitly approved that strategy
- The legal / regulatory environment caps the price (taxi meters, utility tariffs, government-regulated fees) — in which case apply the upstream/downstream value levers instead
- Pricing is not the binding constraint; if unit economics fail at any reasonable price, the business model itself needs redesign first

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Pricing Strategy brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Product / service definition, target customer segments, and channel mix
- Current or proposed price points with rationale
- Competitor prices and the business's current differentiation
- Unit economics (cost, margin, CAC, LTV where known)
- Country context (UGX + EA market norms, any regulatory price constraints)

## Workflow

1. **Audit against the 9 Price Failures** — identify which of Kennedy's nine failure modes the current pricing exhibits (see `references/kennedy-9-price-failures.md` or the extraction file).
2. **Classify the current pricing method** — WAG / Industry Norm / Client-Dictated / Cost-Plus / Target Return. Only Target Return survives as a valid *starting* method.
3. **Identify the niche** — move the offer from "generic" to "specifically for [sub-niche or subculture]." Calculate the price lift this unlocks (typically 100–500%).
4. **Build the Triangle of Preeminence** — name the three sides the business will build: (a) expertise/excellence, (b) high-visibility marketing, (c) community/industry contribution.
5. **Design the 5-Proposition stack** — USP + UVP + Irresistible Offer + Unique Safety Proposition + Unique Experience Proposition. Lead with the strongest; hook the others.
6. **Destroy apples-to-apples comparisons** — bundle, proprietise the method, change one little thing about delivery/packaging/speed so direct competitor comparison becomes impossible.
7. **Design discount discipline** — every discount must have (a) a reason and (b) a quid pro quo. Never predictable. Never for prestige offerings.
8. **Surface hidden costs of cheaper/free alternatives** — red tape, wait time, quality variance, privacy loss, etc. This is essential where the plan competes with free or subsidised services.
9. **Stress-test the price against recession/depreciation** — in most categories, the right recession move is to raise prices and upgrade service, not cut.
10. **Reconcile with financial projections** — updated price flows through to Section 10 (projections) and must match the marketing mix in Section 07.
11. **Test packaging experiments** — for digital, service, and subscription businesses, test monthly versus annual, bundle versus single, premium tier versus entry tier, and onboarding/support inclusions before treating the price architecture as final.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the pricing decision record and that the decision concerns the price architecture and concessions the business can defend.
- **Stop condition:** halt the affected conclusion if required evidence is missing (unit economics, willingness-to-pay evidence, and discount rules) or if the work could lead to this identified risk: setting price by imitation while eroding margin and positioning.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Framework Applied — The 9 Price Failures (audit checklist)

| # | Failure | How to spot it in a plan |
|---|---|---|
| 1 | Pricing by textbook formula / industry norm | "Our prices are in line with industry standards" |
| 2 | Excess concern about competitors' lower prices | Competitor price table drives the plan's price anchor |
| 3 | Attracting customers who buy by price | Target segment described by budget, not by problem or aspiration |
| 4 | Pre-determined belief about "what they'll pay" | Founder asserts a ceiling without test data |
| 5 | Permitting apples-to-apples comparison | The offer is packaged identically to competitors |
| 6 | Insufficient differentiation | No proprietary method, name, process, or brand ritual |
| 7 | Not offering premium price options | Only one price; no good/better/best tier |
| 8 | Ignorance about business math | CAC, LTV, gross margin not calculated |
| 9 | Poor business-esteem | "We don't want to overcharge" framing |

Mark each failure Yes / Partial / No. Every Yes is a revenue leak.

## Framework Applied — The 5 Propositions

Every revised pricing page/section must demonstrate all five:

1. **Unique Selling Proposition (USP)** — Why choose this business over every alternative, *including the status quo*?
2. **Unique Value Proposition (UVP)** — Why is this worth far more than the price? (bundle, ROI, intangibles, hidden benefit)
3. **Irresistible Offer** — Discount + premiums + fast-action bonus + deadline penalty
4. **Unique Safety Proposition (USP)** — Guarantees, warranties, risk-reversal-plus, proof
5. **Unique Experience Proposition (UEP)** — Theme, ritual, celebrity, events, surprise-and-delight

## Framework Applied — The Triangle of Preeminence (Dr. Barry Lycka)

| Side | What to build | Evidence in the plan |
|---|---|---|
| **Expertise & Excellence** | Proprietary method, best technology, trained team, advanced credentials | Section 03 product description, Section 09 team bios |
| **High-Visibility Marketing** | Saturation media, event marketing, PR, publicity | Section 07 marketing budget and channel mix |
| **Community & Industry Contribution** | Charity, non-profit, activist/thought-leader roles, speaking, writing | Section 09 management, Section 16 sustainability, Section 01 summary |

All three must be visible in the plan for "preeminence pricing" to be defensible to an investor.

## Framework Applied — The Hawaiian Fisherman Method (lead-flow diversification)

Premium pricing is sustainable only when the business is never desperate for the next sale. The plan must show **at least 5 live lead sources** (referral / paid / content / partnerships / events / PR / outbound / inbound) — not 1 or 2.

## Framework Applied — Niche/Subculture Pricing Lift

Audit the product's position on this ladder:

~~~text
Generic (baseline price)
    → Niche (2-5× baseline)
        → Sub-niche (2× niche)
            → Subculture (price becomes almost irrelevant)
~~~

For every offer, specify: which niche/sub-niche/subculture, what the customer identity-signal looks like ("for [specific role/hobby/community]"), and where in the plan this shows up (positioning, packaging, branding).

## Framework Applied — Competing with Free

When the plan faces free or heavily subsidised alternatives (government healthcare, public education, open-source, development-partner-funded services):

1. **Surface the hidden cost of free** — red tape, wait time, quality variance, lost control, privacy loss. Make this explicit in marketing copy and sales collateral.
2. **Don't give away prestige offerings** — protect premium tiers from free samples, demos, or discounts.
3. **Edu-marketing** — give away *information* that educates buyers (free reports, checklists, webinars); charge premium for *delivery and results*.
4. **Deliberately repel price-sensitive prospects** via your messaging — "this is for clients who value X over price."

## Discount Discipline — 5 Rules

1. Every discount has a reason (volume / prepay / early / charitable / behaviour modification).
2. Every discount includes quid pro quo (referrals / deadline compliance / multi-purchase / information exchange).
3. Discounts are never predictable (don't train buyers to wait).
4. Prestige offerings are never discounted or given free — add value via warranties, bonuses, events, financing.
5. Staff cannot discount unilaterally — pricing authority is a founder-level decision.

## Integration With Other Plan Sections

| Plan Section | Integration |
|---|---|
| 01 Executive Summary | The one-liner must telegraph premium positioning and target customer |
| 02 Company Overview | Mission/vision supports preeminence; values consistent with premium brand |
| 03 Products/Services | Product design shows proprietary method, naming, bundling, good/better/best tiers |
| 05 Target Market | Customer described by identity / aspiration, not by budget tier |
| 06 Competitive Analysis | Apples-to-oranges comparisons, category-of-one positioning |
| 07 Marketing & Sales | 5 Propositions visible; Triangle of Preeminence activated; 5+ lead sources |
| 10 Financial Projections | Target-return pricing; gross margin ≥ 50% for services / 30% for physical goods where feasible |
| 12 Risk Analysis | Pricing risks: staff sabotage, competitor dumping, recession response — all with mitigation |
| 16 Sustainability | ESG story supports premium positioning (Leleux/van der Kaaij) |

## Quality Bar

- None of the 9 Price Failures remain unaddressed
- All 5 Propositions are visible in the plan's positioning and marketing sections
- The Triangle of Preeminence is visible across product, marketing, and management sections
- At least 5 lead-flow sources are planned (Hawaiian Fisherman)
- Discount discipline is codified in written pricing rules
- Hidden cost of cheaper/free alternatives is explicitly surfaced in marketing copy
- Niche/sub-niche/subculture positioning is specific and defensible
- Financial projections use the upgraded prices and gross margin targets match

## Anti-Patterns

- "We're priced in line with competitors" as a justification
- A single monolithic price with no tier structure
- Copy that leads with features rather than the five propositions
- Discounts buried as "standard practice" with no reason and no quid pro quo
- Premium offerings given away free "for marketing"
- Plans that cut prices as the recession response
- Founder language about "not overcharging" or "being fair"


- Applying the wrong neighbouring route to meta pricing strategy. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pricing Strategy deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Annotated critique of the current pricing section (9 Failures scorecard)
- Revised pricing architecture (tiers, propositions, niche placement)
- Triangle-of-Preeminence implementation plan (expertise / visibility / community)
- Discount rulebook (the 5 rules with business-specific examples)
- Hidden-cost-of-free messaging block (where applicable)
- Updated Section 07 pricing narrative and Section 10 projections
- Pricing risk block for Section 12
- Pricing experiment plan covering hypothesis, segment, test period, decision metric, and expected margin effect

## References

- **Kennedy & Marrs primary source**: See `../book-extractions/kennedy-no-bs-price-strategy-extraction.md` for the full 248-page extraction — 9 failures, Triangle of Preeminence, Hawaiian Fisherman, 5 Propositions, niche pricing, association principle, 5 price-setting methods, staff sabotage, recession strategy, Uganda/EA application notes.
- **Kennedy sales success companion**: See `../book-extractions/kennedy-no-bs-sales-success-extraction.md` for how pricing shows up in the selling conversation (Takeaway Selling, Beating Price, Apples-to-Oranges).
- **Ultimate Sales Letter**: See `../book-extractions/kennedy-ultimate-sales-letter-extraction.md` Step 7 "Beat the Price Bugaboo" for specific price-handling copy techniques.
- **Brunson funnel economics**: See `../book-extractions/brunson-dotcomsecrets-ignite-extraction.md` for the Value Ladder, SLO-sustained continuity, and reverse-engineered revenue planning — all of which support premium pricing.
- **Related skills in this repo**: `07-marketing-sales-strategy`, `10-financial-projections`, `06-competitive-analysis`, `03-products-services`, `meta-bankability-scoring`, `meta-valuation`.
- **Profit and growth-system companion**: See `../../book-extractions/growth-profit-disruption-systems-extraction.md` for offer-mix improvement, 15 percent compounding levers, retention economics, package testing, and profit-led growth logic.

## Premium GTM Companion

Run `../meta-premium-go-to-market/SKILL.md` when premium pricing depends on affluent, executive, enterprise, luxury, high-ticket, or premium-service positioning. Pricing power must be supported by offer design, proof, sales execution, and retention economics.

## Uganda / East Africa Notes

- **UGX pricing** — the "reassuringly expensive" effect is amplified in EA where very-low prices signal counterfeit or fraud risk.
- **Growing affluent middle class** — Kampala, Entebbe, Mbarara, Jinja (and the diaspora market) support premium tiers in healthcare, education, hospitality, financial services, fashion, specialty food, and personal services.
- **Compete-with-free maps to** — private schools vs government, private clinics vs Ministry of Health, private SACCOs/MFIs vs subsidised programmes, paid training vs NGO-funded programmes. The hidden-cost-of-free playbook applies directly.
- **Principle of Association** — partner logos from banks (DFCU, Stanbic, Equity), listed companies (Umeme, MTN), universities (Makerere, Strathmore), hospitals (IHK, Nakasero) unlock premium perception.
- **Recession / FX response** — shilling depreciation increases imported-input costs; the default Ugandan SME response is to absorb margin; the right Kennedy response is to raise prices and trim wrong-fit customers.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Pricing decision record decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to setting price by imitation while eroding margin and positioning. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the pricing decision record; updating a working pricing schedule, not live prices is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If unit economics, willingness-to-pay evidence, and discount rules cannot be obtained, return a qualified pricing decision record covering only the checks that remain supportable. Leave this decision unresolved: the price architecture and concessions the business can defend. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: the price architecture and concessions the business can defend | Record the conclusion, source trail, owner, and review trigger in the pricing decision record. | Risk of setting price by imitation while eroding margin and positioning |
| Material evidence conflicts or remains uncertain | Model the competing price structures against contribution margin, willingness-to-pay evidence, and discount leakage before choosing one. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: unit economics, willingness-to-pay evidence, and discount rules | Mark the decision on the price architecture and concessions the business can defend `not assessed` in the pricing decision record, and send it to the finance owner and commercial lead. | Otherwise, the work risks setting price by imitation while eroding margin and positioning |

## Quality Standards


Accept the pricing decision record only when evidence is sufficient for this decision: the price architecture and concessions the business can defend. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of setting price by imitation while eroding margin and positioning.

## Worked Example


A manufacturer matches a competitor's discount without knowing contribution after distribution. Recalculate the floor, define the concession received in return, and reject any discount that breaches the approved margin.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the pricing decision record, using the reporting basis and effective date supported by unit economics, willingness-to-pay evidence, and discount rules. Reconcile the treatment to the model and narrative, and have the finance owner and commercial lead review the treatment, reconciliation, and exposure to this risk: setting price by imitation while eroding margin and positioning.

<!-- dual-compat-end -->
