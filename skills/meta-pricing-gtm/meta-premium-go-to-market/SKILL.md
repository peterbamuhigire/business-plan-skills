---
name: meta-premium-go-to-market
description: Use when a plan targets affluent consumers, executives, enterprise clients, premium SMEs, luxury/lifestyle buyers, investors, or high-ticket service customers. Use the SaaS pricing skill for recurring-revenue tier architecture.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Premium Go-To-Market Meta-Skill

## Use When

- A plan targets affluent consumers, executives, enterprise clients, premium SMEs, luxury/lifestyle buyers, investors, or high-ticket service customers.
- The plan needs premium positioning, premium product design, value-based pricing, lead generation, sales process, or launch strategy.
- The revenue model depends on higher margins, fewer better customers, consultative selling, relationship trust, or enterprise buying committees.

## Do Not Use When

- Do not use to make a weak or commodity offer sound expensive without improving the product, proof, service, or economics.
- Do not use when the user explicitly wants a low-cost, mass-market, discount-led strategy and accepts the margin trade-off.
- Do not use before the target customer and core offer are at least directionally defined.


- Route to `saas-pricing-and-packaging-strategy` instead for recurring-revenue tier architecture.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Premium Go To Market brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Product/service definition, target customer, price point, gross margin, sales model, and proof assets.
- Current or planned marketing channels, sales process, follow-up capacity, and customer success/service model.
- Competitive alternatives, buyer objections, and any evidence of willingness to pay.

## Workflow

1. Define the premium segment narrowly: buyer profile, buying context, status/risk drivers, channels, proof expectations, and alternatives.
2. Position the offer around expensive outcomes: revenue, profit, time, status, confidence, risk reduction, access, transformation, or strategic control.
3. Build the premium offer: tiers, inclusions, exclusions, guarantees/assurances, onboarding, service cadence, evidence, and delivery quality.
4. Price for value: anchor to outcomes and consequences, show trade-offs, avoid reflex discounts, and connect pricing to financial projections.
5. Design acquisition: account lists, referrals, executive outreach, social proof, authority content, lead magnets, email nurture, contact campaigns, and qualification.
6. Design sales execution: discovery questions, implication/value logic, stakeholder map, business case, proposal, objections, next-step commitments, and follow-up.
7. Design retention and expansion: VIP treatment, reviews, success metrics, referral loops, upsells, renewals, and customer advocacy.
8. Run the premium GTM gate before bankability scoring, pricing review, launch planning, or final assembly.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the premium go-to-market plan and that the decision concerns which segment, promise, proof, and sales motion can sustain premium rates.
- **Stop condition:** halt the affected conclusion if required evidence is missing (premium buyer evidence, offer economics, and sales capacity) or if the work could lead to this identified risk: confusing expensive positioning with a deliverable premium offer.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Premium claims are supported by product quality, proof, service design, and pricing logic.
- The plan explains how high-value leads are found, warmed, qualified, converted, retained, and expanded.
- The sales process respects executive time and committee risk.
- The financial model reflects lower volume, higher conversion cost, longer sales cycles, higher service expectations, and better margins where relevant.

## Anti-Patterns

- Premium pricing with ordinary delivery, weak onboarding, or no proof.
- Luxury language with discount-heavy campaigns.
- Enterprise sales assumptions without named-account research, stakeholder mapping, or business-case logic.
- Lead generation that optimises for volume while attracting low-fit buyers.
- Sales projections that ignore longer premium sales cycles and higher service cost.


- Applying the wrong neighbouring route to meta premium go to market. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Premium Go To Market deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Premium positioning and GTM review.
- Premium marketing and sales strategy section guidance.
- Pricing and offer architecture recommendations.
- Lead generation, outreach, nurture, and sales execution plan.
- Fix list for weak claims, proof gaps, and margin risks.

## References

- `references/premium-gtm-quality-gate.md` - detailed gate for premium positioning, luxury/affluent marketing, enterprise selling, pricing, and launch execution.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Premium go-to-market plan decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to confusing expensive positioning with a deliverable premium offer. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the premium go-to-market plan; drafting the approved channel and sales plan is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If premium buyer evidence, offer economics, and sales capacity cannot be obtained, return a qualified premium go-to-market plan covering only the checks that remain supportable. Leave this decision unresolved: which segment, promise, proof, and sales motion can sustain premium rates. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which segment, promise, proof, and sales motion can sustain premium rates | Record the conclusion, source trail, owner, and review trigger in the premium go-to-market plan. | Risk of confusing expensive positioning with a deliverable premium offer |
| Material evidence conflicts or remains uncertain | Compare the premium segment and offer against a narrower entry segment using contribution, sales-cycle, and proof requirements. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: premium buyer evidence, offer economics, and sales capacity | Mark the decision on which segment, promise, proof, and sales motion can sustain premium rates `not assessed` in the premium go-to-market plan, and send it to the finance owner and commercial lead. | Otherwise, the work risks confusing expensive positioning with a deliverable premium offer |

## Quality Standards


Accept the premium go-to-market plan only when evidence is sufficient for this decision: which segment, promise, proof, and sales motion can sustain premium rates. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of confusing expensive positioning with a deliverable premium offer.

## Worked Example


A consultancy raises price but still targets every SME with the same generic offer. Narrow the segment, name the high-cost problem and proof, and accept the premium motion only when delivery margin and sales capacity support it.

<!-- dual-compat-end -->
