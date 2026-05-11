---
name: saas-agent-outcome-pricing-business-case
description: Adjudicate when outcome pricing wins commercially (high TCV; narrow success definition; low-variance outcomes; regulated/measurable; customer prefers risk-transfer) vs when it loses (high variance; attribution ambiguity; long verification lag; low TCV not worth measurement overhead). Margin-volatility model. When to refuse outcome pricing. Sits alongside `saas-agent-pricing-strategy` which adopts outcome pricing as a primitive.
---

# SaaS Agent Outcome Pricing Business Case Skill

## Overview

Outcome pricing is a popular pricing primitive for agent products in 2025-2026 because it aligns vendor and customer incentives at the surface and signals confidence. But outcome pricing wins commercially only when specific conditions hold. When those conditions do not hold, outcome pricing creates:

- Wild margin volatility (the vendor absorbs outcome variance)
- Disputes (counter-party rejects outcomes; vendor cannot collect)
- Long cash-conversion cycles (revenue recognised only on outcome verification; cash arrives much later)
- Variable-consideration constraints that hold back revenue recognition
- Investor confusion about ARR vs realised revenue
- Reserve pressure (refund + dispute reserves balloon)

This skill is the **business-case adjudicator** for outcome pricing. It does not assume outcome pricing is right; it tests whether it is right for the specific agent product and customer context.

## Use When

- A pricing decision involves outcome pricing as a primitive (alone or in hybrid)
- The board / investor narrative claims "we charge only when we succeed"
- A customer-procurement team is requesting outcome pricing
- A regulated sector (insurance, healthcare, legal, public-sector) is expecting outcome pricing
- The 3yr / 5yr plan models outcome pricing revenue and the variance assumption must be tested
- Cross-loaded with `saas-agent-pricing-strategy`, `saas-agent-revenue-recognition`, and `saas-agent-deferred-revenue-and-credit-reserves`

## Do Not Use When

- Outcome pricing is not on the table — use `saas-agent-pricing-strategy`
- The product is internal-efficiency only

## Required Inputs

- Customer value-anchor (what does outcome replace?)
- Outcome variance data (historical or modelled)
- Counter-party verification mechanism (who verifies the outcome and how)
- Verification lag (time from action to verification)
- Cost per attempt (cost-per-task, not just cost-per-resolved-task)
- TCV per customer
- Disputes-history (where available)
- Refund / credit policy
- Competitive context (what competitors charge for similar outcomes)

## Workflow

### 1. Apply the "outcome pricing wins" test

Outcome pricing wins when **all** of the following hold:

- [ ] **High TCV per customer** — outcome measurement overhead is justified (typically $10k+ ACV)
- [ ] **Narrow, objectively measurable success definition** — both parties can agree on what counts; outcome is observable not subjective
- [ ] **Low outcome variance** — outcome rate is predictable within tight bands; std dev < 20% of mean
- [ ] **Short verification lag** — outcome verified within days, not months
- [ ] **Clean attribution** — counter-party process attributes the outcome to your action unambiguously
- [ ] **Customer prefers risk-transfer** — customer wants to pay only on success and is willing to accept higher per-outcome price for that
- [ ] **Vendor cost-per-attempt is low relative to per-outcome price** — failed attempts do not destroy unit economics

If 5+ of 7 hold: outcome pricing is commercially viable.
If 3-4 hold: hybrid pricing (subscription + success fee).
If 0-2 hold: refuse outcome pricing. Choose per-resolution or subscription.

### 2. Apply the "outcome pricing loses" red flags

Outcome pricing loses when **any** of the following are present:

- High outcome variance (recovery rates 15-60% across portfolios; accuracy rates 70-95%)
- Attribution ambiguity (customer can claim the outcome would have happened without you)
- Long verification lag (90+ days)
- Counter-party can refuse to verify (e.g. payer denial in medical coding; court rejection in legal)
- Customer-side gaming risk (customer marks outcomes as failed to avoid paying)
- TCV per customer is low; per-outcome price is too small to cover variance
- Cost per attempt is high relative to per-outcome price
- No reserve capacity to absorb refund / dispute volatility

If any 2+ red flags: hybrid or refuse outcome pricing.

### 3. Build the margin-volatility model

For an outcome-priced agent, model:

- Expected outcome rate (e.g. 35%)
- Outcome rate std dev (e.g. 8pp)
- Outcome rate range (e.g. 20-50%)
- Cost per attempt (e.g. $40)
- Per-outcome price (e.g. $200)
- Attempts per customer per month (e.g. 100)

Compute:
- Best case (50% outcome rate): 50 outcomes × $200 - 100 × $40 = $10,000 - $4,000 = $6,000 contribution
- Expected (35%): 35 × $200 - 100 × $40 = $7,000 - $4,000 = $3,000 contribution
- Worst case (20%): 20 × $200 - 100 × $40 = $4,000 - $4,000 = $0 contribution (breakeven)
- Stress (-1 std dev, 27%): 27 × $200 - 100 × $40 = $1,400 contribution
- Catastrophic (-2 std dev, 19%): -$200 (loss)

**Volatility ratio:** (best case - worst case) / expected = ($6,000 - $0) / $3,000 = 200%

Margin volatility this high is investor-unfriendly. Mitigations:
- Floor + variable structure: minimum monthly fee + per-outcome top-up
- Volume guarantee with success kicker
- Hybrid: subscription + reduced per-outcome rate

### 4. Compute the constrained-revenue impact

Under ASC 606 / IFRS 15, outcome-pricing revenue is variable consideration subject to the constraint. The constraint reduces recognised revenue below expected:

- Expected revenue (outcome rate 35%): $7,000/month
- Constraint applied (probable not to reverse): include only $5,000 (worst plausible)
- Recognised revenue: $5,000/month
- Reserved upside: $2,000/month recognised as outcomes verify

For investor reporting:
- ARR (booked annual): $84,000 expected
- ARR (recognised): $60,000 constrained
- Gap: $24,000 reserved upside

This gap is investor-confusing. Tell the story explicitly.

### 5. Decision matrix

| Customer / context | Recommendation |
|---|---|
| Enterprise insurer; claim-payment outcomes; clean attribution; 35% success ±5pp | Outcome pricing fits |
| SMB collections; per-debt; recovery 15-50%; attribution ambiguous | Hybrid: floor + success |
| Public-sector citizen-service; outcome subjective; verification lag 60+ days | Per-resolution; not outcome |
| Legal-filing agent; outcome = document accepted; binary; verified in days | Outcome pricing fits |
| Medical coding; outcome = code accepted by payer; payer denial rate 8% with variance | Hybrid with refund reserve |
| Agri-advisory; outcome = yield improvement; verification 6 months; ambiguous | Per-task subscription; not outcome |
| CX resolution; outcome = ticket resolved + customer accepts; binary; verified hours | Outcome pricing fits if cost per attempt low |

### 6. Build the refund/dispute reserve (cross-load)

If outcome pricing is adopted, refund reserve is large. Cross-load `saas-agent-refund-reserve-methodology.md`.

### 7. Plan the dispute-resolution mechanism

Outcome pricing requires:
- Clear definition of success (in contract)
- Verification mechanism agreed (counter-party process / external evidence / both)
- Dispute-escalation path (timeline, owner, evidence)
- Reserve for legal cost of disputes
- Reserve for refund cost where disputes resolve against vendor

Cross-load with `meta-agent-sla-financial-controls`.

### 8. Wire to investor narrative

In the funding deck:
- State the outcome-pricing decision and the reasoning
- Show the volatility model
- Show the constraint impact on recognised revenue
- Show the reserve / dispute mitigation
- Cross-reference to risk register

### 9. Wire to living-plan governance

Per cadence below.

## Quality Bar

- "Wins" test applied explicitly; outcome pricing chosen only if 5+ of 7 conditions hold
- "Loses" red flags scanned; outcome pricing avoided if 2+ flags
- Margin-volatility model built with std dev / range
- Constrained-revenue impact computed and disclosed
- Refund / dispute reserve sized
- Dispute-resolution mechanism designed
- Investor narrative integrates the volatility story honestly
- Cross-references consistent

## Anti-Patterns

- "Outcome pricing aligns incentives so it's always right" — wrong
- No margin-volatility model — overstates predictability
- Adopting outcome pricing when verification lag exceeds cash-conversion tolerance
- No dispute mechanism — first dispute creates legal cost and churn
- Recognising outcome revenue at billing rather than at verification — overstates
- No constraint applied to variable consideration — overstates
- "Customer wants outcome pricing" without testing whether the customer can verify outcomes cleanly
- Outcome pricing on subjective outcomes (e.g. "improve productivity") — destined for dispute
- Hybrid pricing presented as outcome pricing in investor narrative — misleading

## Outputs

- Outcome pricing wins / loses test
- Margin-volatility model
- Constrained-revenue impact
- Refund / dispute reserve cross-load
- Dispute-resolution mechanism
- Decision matrix vs alternative primitives
- Investor narrative draft
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Outcome rate (actual vs projected) | weekly | Head of Agent + CFO | -3pp from plan |
| Per-outcome margin contribution | monthly | CFO | -10% from plan |
| Constraint adjustment (variable consideration) | quarterly | Controller + CFO | adjustment >10% |
| Dispute count / aging | weekly | Head of CS + Legal | >5 disputes >7 days |
| Refund-reserve adequacy | monthly | CFO | reserve <plan |
| Outcome-pricing business-case revalidation | annually + on trigger | CFO + Head of GTM + CEO | trigger |

## References

- `references/saas-agent-outcome-pricing-business-case-template.md` — worked decision-tree and volatility model
- `skills/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md` — pricing primitives parent
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — variable-consideration treatment
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — refund reserve
- `skills/meta-agent-sla-financial-controls/SKILL.md` — dispute controls
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit
- `book-extractions/kennedy-no-bs-price-strategy-extraction.md` — pricing discipline

## Africa / Uganda Application Notes

- **Collections agents in Africa** — outcome pricing fits (per-debt recovery is binary; mobile-money settlement is the verification trigger; lag is short); but recovery-rate variance is wide; hybrid recommended (small per-account fee + success kicker)
- **Insurance / microinsurance** — outcome-pricing fits where claim payment is the outcome; payer (insurer) verification is the trigger; works for KE / NG / ZA microinsurance pilots
- **Public-sector outcome pricing** — KE / NG / RW tenders sometimes propose outcome pricing but verification lag is 90-180 days; mostly avoid; choose per-resolution or fixed-fee
- **DFI / multilateral milestone-pricing** — looks like outcome pricing but is closer to milestone-deliverable pricing; treat as performance-obligation-per-milestone in rev-rec
- **Agri-advisory** — outcome pricing on yield improvement does not work (long verification, attribution ambiguity, seasonal variance); per-task subscription is the right model
- **Legal-filing agents** — outcome pricing on document filed and accepted works in KE / NG / ZA / RW where filing systems verify
- **Medical-coding agents in regulated payer systems** — outcome pricing fits but payer denial rates 5-15%; refund reserve essential
- **Mobile-money settlement as verification** — for collections / recovery outcomes, MoMo / M-Pesa settlement notification is the verification event; document the chain
- **FX corridor on outcome pricing** — USD cost vs local-currency outcome value; +/-20% FX swing changes the breakeven outcome rate; model the corridor
