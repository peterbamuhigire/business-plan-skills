---
name: meta-strategic-options-evaluation
description: Use when generating and choosing between strategic options with TOWS, Ansoff, the strategy clock and SAFe (suitability, acceptability, feasibility), responding to a low-cost entrant, or gating a 35-word strategy statement; distinguishes `meta-critical-thinking-business-logic`, which reviews plan reasoning.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Strategic Options Evaluation

Generate a small set of genuinely different strategic options, screen them for suitability, acceptability and feasibility, and commit to one, stated in a strategy statement of 35 words or fewer. The governing judgement: a plan with one option has not made a choice, and a strategy that cannot be stated briefly with an objective, a scope and an advantage is not yet a strategy.

<!-- dual-compat-start -->
## Use When

- A business plan, marketing plan or board paper must show the options considered, the one chosen and why the others were rejected.
- Candidate strategies from a TOWS matrix, strategic audit or founder brainstorm need SAFe screening: suitability, acceptability (risk, return, stakeholder reactions) and feasibility (funds, people, capabilities).
- The competitive position must be placed on the strategy clock with a three-year path, or the firm must decide how to respond to a low-cost entrant.
- The plan's strategy statement must pass the 35-word gate before sections 01, 02 and 07 are drafted.

## Do Not Use When

- Use `meta-strategic-factor-analysis` instead when the weighted factor tables and TOWS candidates do not yet exist.
- Use `meta-critical-thinking-business-logic` instead to review claim, evidence and warrant quality across a draft plan.
- Use `meta-business-model-design` instead when the question is how the business makes money, not which strategic direction to take.
- Use `meta-international-market-entry` instead when the options are countries and entry modes.
- Use `meta-valuation` or `10-financial-projections` for the financial models; this skill consumes their outputs.

## Required Inputs

| Input artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Decision brief, objective and decision-maker | `00-client-intake`, owner or board | Yes | Stop; options cannot be screened against an unstated objective. |
| SFAS and TOWS candidates, or equivalent key factors | `meta-strategic-factor-analysis`, `meta-strategic-audit` | Yes | Build a short key-factor list with the owner, mark it provisional, and cap confidence. |
| Price and perceived-benefit evidence for the firm and rivals | Customer survey, `06-competitive-analysis`, `meta-pricing-strategy` | Conditional | Place the strategy clock on management judgement and flag it `VERIFY`. |
| Financial outline per option (investment, margin, cash timing, break-even) | `10-financial-projections`, finance owner | Yes for acceptability | Screen suitability only; mark acceptability and feasibility `not assessed`. |
| Stakeholder map (owners, lenders, regulators, staff, key customers) | Engagement owner, `12-risk-analysis` | Yes | List stakeholders from interviews and flag reactions as assumptions. |

## Workflow

1. Restate the objective and the performance gap: desired result minus the projection of the current strategy. The gap sets how ambitious the options must be.
2. Generate options from four sources: TOWS cells, Ansoff directions (penetration, product development, market development, diversification), strategy-clock positions, and methods (organic, alliance, acquisition). Keep three to five mutually exclusive options, always including "improve execution of the current strategy". Use [the option-generation and SAFe procedure](references/option-generation-and-safe-screens.md).
3. Suitability: score each option against the SFAS factors in a ranking matrix, run a scenario screen and a VRIO screen. Drop options graded C.
4. Acceptability: for survivors, test risk (sensitivity, break-even market share, liquidity), return (payback, NPV or economic profit from the finance owner) and stakeholder reactions. Route all valuation, tax and accounting treatment to `meta-valuation` and the Chwezi finance doctrine.
5. Feasibility: test funds (source and timing by life-cycle stage), people and skills, and resource integration including suppliers and partners. Stop an option that fails feasibility unless a funded fix is named.
6. Place the chosen option on the strategy clock and, where a low-cost rival exists, walk the response tree in [the clock and low-cost-rival reference](references/strategy-clock-and-low-cost-rival-response.md).
7. Write the strategy statement and apply [the 35-word gate](references/strategy-statement-gate.md). Block drafting of sections 01, 02 and 07 until it passes; revise and retest on failure.
8. Record the choice, the rejected options with reasons, the conditions and the review triggers; hand off to the orchestrator and section owners.

## Quality Standards

- At least three genuinely different options, including the current strategy improved, are screened; rejected options carry a stated reason.
- Each SAFe verdict cites evidence: SFAS factor IDs for suitability, named numbers or ranges for acceptability, named funds and people for feasibility.
- The chosen strategy's clock position matches its cost base and price evidence; a hybrid claim names the mechanism that lowers cost while raising benefit.
- The strategy statement has 35 words or fewer and contains an objective, a scope (customer, geography, activities done in-house) and an advantage that is not a threshold quality.
- Financial figures come from the model owner and are labelled base or downside; this skill does not invent returns.

## Anti-Patterns

- Presenting one recommended strategy with no alternatives. Fix: screen at least three mutually exclusive options and show why the others lost.
- Starting a price war against a low-cost entrant. Fix: walk the response tree; differentiate, launch a fighter brand only where it shares costs, or accept a smaller business.
- Claiming "cheapest and best" without a mechanism. Fix: name the scale, technology or process change that lowers cost and raises benefit, or pick one position on the clock.
- Judging acceptability by return alone. Fix: test risk, return and stakeholder reactions (lender, owner-family, regulator, staff, key customers) together.
- A 60-word strategy statement listing values. Fix: cut to objective, scope and advantage in 35 words or fewer; move values to section 02.
- Treating a positive NPV as proof of feasibility. Fix: check the cash timing, people and supplier readiness separately.

## Outputs

| Output artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Options register (source, description, method) | Decision-maker, `business-plan-orchestrator` | Three to five mutually exclusive options, each traced to TOWS, Ansoff, clock or method. |
| SAFe screening matrix with verdicts | Board, lender or investor reader; `12-risk-analysis` | Each option graded with evidence per criterion; rejections explained. |
| Strategy-clock position and three-year path; low-cost-rival response | `06-competitive-analysis`, `meta-pricing-strategy`, `07` | Position and path consistent with cost and price evidence. |
| Strategy statement (35 words or fewer) with gate result | `01`, `02`, `07`, marketing-plan orchestrator | Gate passes on length, objective, scope and advantage. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Screening trace | Ranking matrix plus acceptability and feasibility notes with sources | A reviewer can see why each option passed or failed each screen. |
| Rejected-options log | Table: option, failed screen, reason | Every rejected option is visible with its reason. |
| Strategy-statement gate record | Word count, three-element check, reviewer | The statement and its checks are reproducible. |

<!-- dual-compat-end -->
## Capability Contract

Permission boundary: analysis and drafting only unless the engagement owner has authorised more. Read and search the SFAS, audit, model and market evidence; draft options, screens and the strategy statement. The choice belongs to the owner or board; this skill recommends. Do not state valuation, tax or accounting treatment as fact: route to `meta-valuation` and the Chwezi finance doctrine. Current market or country facts come from the Digital research engine. Do not contact stakeholders, publish or commit funds without explicit authority.

## Degraded Mode

Without a financial model, customer price evidence or a stakeholder map, screen suitability only, mark acceptability and feasibility `not assessed`, and return a narrowed shortlist with the evidence each option needs. A strategy statement drafted without an agreed objective is labelled draft and does not unblock section drafting.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| The performance gap is small and the SFAS still fits | Prefer improved execution of the current strategy | Costly change for a problem that execution could solve. |
| Options are not mutually exclusive | Merge or re-cut them until choosing one precludes another | A false choice that hides the real trade-off. |
| An option passes suitability but fails lender acceptability (gearing, cover, security) | Stage it, change the funding mix, or reject it | A plan the bank will not finance. |
| A low-cost entrant targets current customers | Apply the response tree; do not cut price by default | A price war the incumbent can afford and the entrant cannot. |
| The chosen position is hybrid on the clock | Require a named cost-lowering mechanism | "Stuck in the middle" economics. |
| Strategy statement exceeds 35 words or lacks objective, scope or advantage | Fail the gate and block sections 01, 02 and 07 | Diffuse strategy that every section interprets differently. |

## Worked Example

The Mbarara dairy's factor analysis passed three alternatives. Suitability: A (focused Kampala growth) scores five ticks on seven SFAS factors, B (regional expansion) three, C (retrench) four. Acceptability: B needs certification spend before revenue and raises gearing beyond the bank's stated comfort, so it is staged to year three; A's break-even requires about 4% of the defined Kampala packaged-yoghurt market (illustrative). Feasibility: A needs a second chilling centre and a sales lead, both fundable. Clock position: differentiation without premium (about 12 o'clock) moving to a modest premium once freshness is proven. Statement (30 words, passes): "By 2028, lift gross margin to 26% selling fresh yoghurt to Kampala supermarket shoppers, collecting and processing milk ourselves, winning through the only daily chilled farm-to-shelf network in western Uganda." All figures illustrative.

## References

- [Option generation and SAFe screens](references/option-generation-and-safe-screens.md) - read at steps 1 to 5 for option sources, the ranking matrix, acceptability and feasibility tests and templates.
- [Strategy clock and low-cost-rival response](references/strategy-clock-and-low-cost-rival-response.md) - read at step 6 for clock zones, the plotting procedure and the response tree.
- [Strategy-statement gate](references/strategy-statement-gate.md) - read at step 7 for the 35-word rule, element checks and pass/fail examples.
- [Competitive strategy tools](../../pipeline/06-competitive-analysis/references/competitive-strategy-tools.md) - read for the competitive position rating and generic strategies this skill builds on.

## Read Next

- `meta-strategic-factor-analysis` - when options lack weighted factors to be screened against.
- `meta-strategic-optionality` - when the choice also shapes the owners' exit or sale path.
- `meta-investment-committee-red-team` - when the chosen strategy must survive an adversarial funder rehearsal.
