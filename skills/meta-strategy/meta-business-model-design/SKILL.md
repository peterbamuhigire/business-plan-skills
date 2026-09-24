---
name: meta-business-model-design
description: Use when designing, comparing and scoring alternative business models with Debelak's six elements and GEL factors (great customers, easy sales, long life) before any plan section is drafted; distinguishes `idea-testing`, which designs validation experiments for a chosen model.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Business Model Design and Scoring

Choose how the business will acquire customers, deliver value, earn margin, satisfy customers after the sale, hold its position and fund itself, then score that model before any plan prose is written. Method: Debelak, D. (2006) *Business Models Made Easy*, Entrepreneur Press. The governing judgement: a plan written around an unscored model spends its budget compensating for weaknesses that a model change would remove.

<!-- dual-compat-start -->
## Use When

- A new venture, new product line or restructured business needs its business model chosen and scored before sections 01 to 16 are drafted.
- Two or more alternative models (for example direct sales against distributors, product against service, one-off sale against subscription) must be compared on the same evidence.
- A funder or banker has said "I don't like the model", or margins, customer acquisition cost or after-sales support are straining an existing business.
- The orchestrator's model-first gate requires a scored model choice to feed `03-products-services`, `07-marketing-sales-strategy` and `10-financial-projections`.

## Do Not Use When

- Use `idea-testing` instead to design experiments that prove or disprove the chosen model's riskiest assumptions.
- Use `meta-critical-thinking-business-logic` instead to review the reasoning of an already drafted plan.
- Use `ecommerce-business-model-diagnostic` instead for a donor-funded diagnostic of an operating e-commerce company.
- Use `meta-strategic-options-evaluation` instead when the model is settled and the question is strategic direction or competitive position.
- Do not use as a substitute for demand evidence; GEL scores are structured judgement that must cite evidence.

## Required Inputs

| Input artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Concept brief: offer, target customer, geography, founder capabilities | `00-client-intake` | Yes | Stop and return the intake questions; a model cannot be scored without a customer. |
| Customer evidence (interviews, sales history, ranking tests) | Client, `meta-market-validation`, Digital research engine | Yes | Score customer factors as hypotheses, flag `VERIFY`, and route the gaps to `idea-testing`. |
| Competitor and channel evidence | `06-competitive-analysis`, channel interviews | Yes | Score relative factors (advantage, entry points) as provisional. |
| Cost, price and margin outline per model | Founder, `10-financial-projections`, finance owner | Yes | Score long-life factors `not assessed` and block the final evaluation. |
| Funding position and constraints | Owner, `11-funding-request` | Conditional | Treat the funding element as a red light until sources are named. |

## Workflow

1. Write the three-sentence story (who we target, what we give them, why they need it) and the concept line of 40 words or fewer. Test both on someone outside the business; revise until they are understood.
2. Draft the model on the six-element canvas and, for each element, a chosen strategy plus two alternatives (Options B and C). Use [the canvas and readjustment reference](references/business-model-canvas-and-readjustment.md).
3. Check the green lights (acquire high-value customers cheaply, significant value, high-margin delivery) and red lights (after-sales burden, unholdable position, excessive funding). Stop and redesign if a green light is missing.
4. Score the eighteen GEL checks (questions R, B, P and S) Strong, Middling or Weak against the desired state and relative to named competitors, citing evidence for each. Use [the GEL checklist and scoring rules](references/gel-factor-checklist-and-scoring.md).
5. For each Middling or Weak check, brainstorm compensating tactics, rate their effectiveness 1 to 3, and keep no more than three tactics in total.
6. Run the verdict labels (Advantage, Par, Repaired, Open concern) and the three gates. The model fails unless R2, B3 and P1 are advantages, none of R3, R6 and S2 is an open concern, and advantages outnumber open concerns by at least 3 to 1.
7. If the model fails, readjust with the fewest levers (customers, value, sales and distribution, production), re-score, and repeat. Compare alternative models side by side on the same evidence.
8. Record the chosen model, the scored table, the rejected models and the open assumptions. Hand the assumptions to `idea-testing`, the model to `03`, channels and tactics to `07`, and margin and investment assumptions to `10`. Block section drafting until the final evaluation passes or the owner accepts a documented exception.

## Quality Standards

- Every GEL score cites evidence and is relative to named competitors; no factor is scored on enthusiasm alone.
- The final evaluation rules are applied exactly and the result is recorded as pass or fail, not averaged.
- Compensating tactics are three or fewer, each with an effectiveness rating and a cost.
- At least one alternative model or Option B per weak element is documented before the choice is made.
- Margin, investment and funding factors reconcile with the financial outline and are reviewed under the Chwezi finance doctrine.

## Anti-Patterns

- Writing the plan before scoring the model. Fix: run the GEL evaluation first and block drafting until it passes.
- Taking "people like the idea" as evidence of importance. Fix: ask whether the purchase is a top-three priority and look for money or effort customers already spend.
- Stacking five or six compensating tactics onto a weak model. Fix: keep three at most and change the model instead; tactics are at best about half as effective as a model fix.
- Chasing the biggest customer group with a give-away price. Fix: compute the price each sale must earn and find the group willing to pay it.
- Ignoring after-sales support cost. Fix: ask industry practitioners, charge for the support customers want, or push it to service-capable partners.
- Assuming distributors will push the product unaided. Fix: name the distributors, their requirements and the training and margin they need.

## Outputs

| Output artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Three-sentence story and concept line (40 words or fewer) | `01-executive-summary`, `02-company-overview` | Tested on an outsider and understood. |
| Six-element canvas with Options B and C | `03-products-services`, owner | Every element has a chosen strategy and two alternatives. |
| GEL scored table, compensating-tactic register and final evaluation | `business-plan-orchestrator`, funders | Rules applied; pass or fail recorded with evidence. |
| Model comparison and choice record | Owner, `03`, `07`, `10` | Alternatives scored on the same evidence; rejected models and reasons listed. |
| Open-assumption list | `idea-testing` | Each assumption has the evidence that would confirm or kill it. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Factor evidence log | Table: factor, score, evidence, source, competitor comparison | Every score traces to evidence or a labelled judgement. |
| Final evaluation record | Three gates: must-be-advantages, no open concerns, 3:1 balance | A reviewer can reproduce the pass or fail. |
| Readjustment history | Versions with lever changed and re-score | Model iterations are visible, not overwritten. |

<!-- dual-compat-end -->
## Capability Contract

Permission boundary: analysis and drafting only unless the engagement owner has authorised more. Read and search the intake, customer, competitor and financial evidence; draft the canvas, scores and choice record. The owner chooses the model. Margin conventions, investment returns and funding structure follow the Chwezi finance doctrine; current market or channel facts come from the Digital research engine. Do not contact customers, distributors or funders, or publish, without explicit authority.

## Degraded Mode

Without customer evidence or a margin outline, score only the factors with evidence, mark the rest `not assessed`, record the final evaluation as incomplete rather than passed, and return the evidence list that would complete it. A qualified model sketch may guide `idea-testing`, but it does not unblock plan drafting.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A green-light element is missing | Redesign the model before scoring | Scoring detail on a model that cannot work. |
| Customers are hard to find or need heavy support | Change the sales and distribution route (distributors, dealers, a bigger solution) | Acquisition and support costs that consume margin. |
| Customers do not value the offer enough | Change the customer group or the value, not the promotion budget | Buying attention for a product nobody prioritises. |
| More than three compensating tactics are needed | Rework the model | Spending that rises steeply as the model moves away from ideal. |
| Annual market sales potential is under about ten times the entry investment (Debelak's heuristic) | Reduce investment, pre-sell contracts, or reject | An investment the market cannot repay. |
| Final evaluation fails and the owner still wants to proceed | Record a documented exception and route to `idea-testing` | A plan presented as sound on a failed model. |

## Worked Example

A Kampala founder proposes a pharmacy stock-management app sold to single-branch pharmacies at a monthly fee. GEL scoring: ease of finding (R2) is Weak (thousands of scattered shops, no list), after-sale support (R6) is an open concern (owners need on-site set-up), margins are Middling. The gates fail: one must-be-advantage check is not an advantage and one must-not-be-concern check is a concern. Readjustment changes the target customers to pharmacies with two to five branches, reachable through the pharmacists' association and a wholesaler partner who installs the app with stock deliveries. Re-scored, ease of finding becomes an advantage, support is Repaired through the wholesaler, and advantages outnumber open concerns 4 to 1. The model passes; the wholesaler partnership assumption goes to `idea-testing`. Illustrative only.

## References

- [GEL factor checklist and scoring rules](references/gel-factor-checklist-and-scoring.md) - read at steps 4 to 6 for the eighteen factors, key-concern triggers, compensating tactics and evaluation rules.
- [Six-element canvas and readjustment levers](references/business-model-canvas-and-readjustment.md) - read at steps 1 to 3 and 7 for the canvas with options, green and red lights, the four levers and East African adaptations.

## Read Next

- `idea-testing` - when the chosen model's riskiest assumptions need experiments.
- `03-products-services` - when the scored model becomes the products and business-model section.
- `meta-strategic-options-evaluation` - when the model is settled and strategic direction must be chosen.
- `meta-pricing-strategy` - when the margin factor depends on a pricing decision.
