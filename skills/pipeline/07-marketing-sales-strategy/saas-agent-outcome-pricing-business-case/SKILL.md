---
name: saas-agent-outcome-pricing-business-case
description: Use when producing or reviewing the saas agent outcome pricing business case component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

Apply the ordered stages below; stop and recover when a stage lacks its required evidence.

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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| ICP, buying process, channel evidence, price tests, unit economics, and sales capacity for saas agent outcome pricing business case | Customer research, CRM records, approved financial model, and sales owner | Yes | If absent, price, margin, conversion, or capacity evidence is unavailable, return a testable commercial hypothesis and cap the recommendation at pilot scale. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pricing or packaging decision with margin and adoption guardrails | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent outcome pricing business case exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent outcome pricing business case release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Price metric rationale, willingness-to-pay evidence, margin bridge, and failure thresholds | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent outcome pricing business case decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent outcome pricing business case review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent outcome pricing business case, the controlling focus is outcome attribution, baseline agreement, counterfactual evidence, dispute rules, and value-sharing limits. This skill may analyse commercial options and draft tests; it may not launch prices, purchase media, contact prospects, alter contracts, or promise outcomes without explicit authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent outcome pricing business case, loss of evidence about outcome attribution, baseline agreement, counterfactual evidence, dispute rules, and value-sharing limits activates degraded mode. If the controlling saas agent outcome pricing business case evidence is unavailable, the same boundary applies. When price, margin, conversion, or capacity evidence is unavailable, return a testable commercial hypothesis and cap the recommendation at pilot scale. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent outcome pricing business case, a package or channel grows headline demand while weakening gross margin, trust, or delivery capacity| reject or constrain it, quantify the guardrail, and test the next credible option | Growth recommendations can consume cash or create obligations the business cannot fulfil |
| For saas agent outcome pricing business case, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent outcome pricing business case decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent outcome pricing business case, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete pricing or packaging decision with margin and adoption guardrails, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent outcome pricing business case decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect icp, buying process, channel evidence, price tests, unit economics, and sales capacity and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce pricing or packaging decision with margin and adoption guardrails with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Pricing or packaging decision with margin and adoption guardrails must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Price metric rationale, willingness-to-pay evidence, margin bridge, and failure thresholds must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent outcome pricing business case, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent outcome pricing business case, treating an unavailable icp, buying process, channel evidence, price tests, unit economics, and sales capacity as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing pricing or packaging decision with margin and adoption guardrails that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A collections agent is offered 8% of recovered debt, but the customer changes its internal collections team during the test. Reject the unadjusted success fee, agree a baseline and attribution rule, and pilot with a dispute cap.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent outcome pricing business case; no local deep-dive reference is declared.
- For saas agent outcome pricing business case claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
