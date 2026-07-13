---
name: meta-valuation
description: Use when valuing a company through DCF, market multiples, venture methods, sensitivity ranges, dilution, or transaction terms. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Valuation Meta-Skill

## Use When

- Use when a business case needs a defensible view of value rather than a hand-waved number.
- Use for equity raises, acquisitions, strategic partnerships, or blended-finance structuring.
- Use when Section 11 needs valuation-backed ownership or term logic.

## Do Not Use When

- Do not use before the financial model is stable enough to support valuation inputs.
- Do not use a single-point valuation when scenario thinking is required.
- Do not confuse valuation with pricing the deal politically; start with economics first.


- Route to `10-financial-projections` instead when the task is to construct the underlying model.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Valuation brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Financial projections and key assumptions
- Business stage, sector, and transaction context
- Country and capital-market context where relevant
- Any existing comparables, cap-table, or prior valuation expectations

## Workflow

1. Define the valuation question and deal context.
2. Select the primary method and a sanity-check method.
3. Translate the operating model into value drivers.
4. Run downside, base, and upside cases.
5. Convert value into ownership, dilution, or funding-structure implications.
6. Flag the assumptions that matter most and where more evidence is needed.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the valuation range and term analysis and that the decision concerns the method, range, and dilution implication.
- **Stop condition:** halt the affected conclusion if required evidence is missing (stable projections, transaction context, and comparables) or if the work could lead to this identified risk: presenting point-estimate theatre as transaction value.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The method fits the business stage and transaction type.
- The valuation is scenario-based, not fake precision.
- Value is tied to operating economics and risk.
- The result is usable in funding negotiations and the plan narrative.

## Anti-Patterns

- Using TAM as if it were value.
- Presenting a valuation with no method logic or scenario range.
- Using comparables with no adjustment for growth, quality, or context.
- Ignoring dilution and milestone implications.
- Treating a generic valuation template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta valuation. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Valuation deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Valuation summary
- Assumptions table
- Downside, base, and upside range
- Term or dilution implications
- Caveats and evidence gaps


Use this skill when Section 10 and Section 11 need a valuation conclusion instead of a generic funding ask.

## Objective

Translate business economics into a defensible view of value, expected returns, and funding terms.

## What to Produce

1. Valuation purpose and audience
2. Appropriate valuation method selection
3. Key assumptions table
4. Base, upside, and downside valuation range
5. Implied investor terms and dilution
6. Sanity checks against market reality

## Method Selection

Choose the primary method by business stage:

| Situation | Primary Method | Secondary Check |
|---|---|---|
| Stable cash-generating business | DCF / enterprise DCF | EV/EBITDA, P/E |
| Growth SME with limited comparables | DCF with scenario range | EV/Revenue or transaction multiples |
| Early-stage or pre-profit venture | Revenue multiples / VC method | Milestone-based dilution check |
| Asset-heavy business | DCF plus asset backing | Book value / replacement cost |
| Distressed or turnaround | Scenario DCF | asset floor |

Use at least one primary method and one cross-check. Never present a single-point valuation without sensitivity.

## Required Workflow

### 1. Define the valuation question

Clarify:

- equity raise, acquisition, buyout, joint venture, or strategic partnership
- minority or control context
- pre-money or post-money framing
- local or international investor lens

### 2. Anchor in operating reality

Valuation must reconcile with:

- Section 04 market size and growth
- Section 07 acquisition assumptions
- Section 08 operating capacity
- Section 10 free cash flow drivers
- Section 11 funding structure

If the model does not reconcile, fix the model before valuing it.

### 3. Build the value drivers

Explicitly state:

- revenue growth
- operating margin
- reinvestment needs
- working capital intensity
- tax rate
- cost of capital
- terminal growth or exit multiple

### 4. Run scenarios

Produce:

- downside case
- base case
- upside case

Change the business assumptions, not just the discount rate.

### 5. Convert value into deal logic

For equity:

- pre-money valuation
- investment amount
- post-money valuation
- investor ownership
- founder dilution

For blended or structured finance:

- amount best raised as debt
- amount best raised as equity
- conditions required for each source

## Mandatory Sanity Checks

- Does the implied multiple look credible for the sector and geography?
- Does the valuation imply a growth rate the market analysis can support?
- Does the ownership being offered make sense for the milestone funded?
- Does the exit or repayment logic remain credible under downside conditions?

## Output Format

### A. Valuation Summary

One paragraph with purpose, method, and conclusion.

### B. Assumptions Table

List the core value drivers and sources.

### C. Valuation Range

Show downside, base, upside values and explain the differences.

### D. Term Implications

State the likely equity stake, dilution, or funding-structure consequence.

### E. Sanity Checks and Caveats

Name the assumptions that matter most and the evidence still needed.

## Quality Criteria

- Method fits the stage and deal context
- Value range is scenario-based, not point-estimate theatre
- Assumptions are explicit and tied to operating drivers
- Investor terms are a consequence of value, not guesswork
- Final answer is usable in Section 11 and the pitch deck

## References

- `references/valuation-frameworks.md` - practical DCF, multiples, cost-of-capital, terminal-value, and dilution guidance distilled from *Valuation* and *The Little Book of Valuation*
- `../11-funding-request/references/business-valuation-methods.md` - repo-specific valuation methods and Uganda / East Africa adjustments
- `../10-financial-projections/SKILL.md` - required financial-model linkage

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Valuation range and term analysis decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to presenting point-estimate theatre as transaction value. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the valuation range and term analysis; building scenarios in the supplied valuation workbook is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If stable projections, transaction context, and comparables cannot be obtained, return a qualified valuation range and term analysis covering only the checks that remain supportable. Leave this decision unresolved: the method, range, and dilution implication. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: the method, range, and dilution implication | Record the conclusion, source trail, owner, and review trigger in the valuation range and term analysis. | Risk of presenting point-estimate theatre as transaction value |
| Material evidence conflicts or remains uncertain | Triangulate DCF, adjusted multiples, and a dilution check; widen the range when the methods diverge instead of averaging them mechanically. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: stable projections, transaction context, and comparables | Mark the decision on the method, range, and dilution implication `not assessed` in the valuation range and term analysis, and send it to the valuation lead and transaction adviser. | Otherwise, the work risks presenting point-estimate theatre as transaction value |

## Quality Standards


Accept the valuation range and term analysis only when evidence is sufficient for this decision: the method, range, and dilution implication. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of presenting point-estimate theatre as transaction value.

## Worked Example


A profitable SME has a stable forecast but weak local comparables. Use DCF as the primary method, show an adjusted-multiple cross-check, and widen the range where the two methods disagree; derive dilution from that range.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the valuation range and term analysis, using the reporting basis and effective date supported by stable projections, transaction context, and comparables. Reconcile the treatment to the model and narrative, and have the valuation lead and transaction adviser review the treatment, reconciliation, and exposure to this risk: presenting point-estimate theatre as transaction value.

<!-- dual-compat-end -->
