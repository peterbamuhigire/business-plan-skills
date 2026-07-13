---
name: meta-financial-stress-test
description: Use when stress-testing downside revenue, margins, working capital, break-even, cash runway, or debt-service assumptions after the model is materially complete. This skill tests an existing model; it does not construct one.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Financial Stress Test Meta-Skill

## Overview

Use this meta-skill to challenge a financial model under adverse conditions. It stress-tests assumptions, scenarios, break-even resilience, and debt-service capacity so the plan can survive scrutiny and bad conditions, not just base-case optimism.

## Use When

- Use after financial projections are materially complete.
- Use when lenders, investors, or internal reviewers need downside analysis.
- Use when resilience under uncertainty matters as much as the headline forecast.

## Do Not Use When

- Do not use before the baseline model exists.
- Do not present stress cases as precision forecasts; they are decision tests.
- Do not use stress scenarios to hide a fundamentally broken base model.


- Route to `10-financial-projections` instead when the task is to construct the underlying model.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Financial Stress Test brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Baseline projections and core financial assumptions
- Funding structure, debt terms, and repayment expectations where relevant
- Key commercial drivers such as price, volume, cost, and working-capital assumptions
- Any country or sector context that shapes plausible shocks

## Workflow

1. Confirm the base case and the assumptions most likely to break.
2. Build adverse and comparative scenarios around the key financial drivers.
3. Test break-even, liquidity, margin, and DSCR resilience under stress.
4. Interpret which assumptions are fatal, manageable, or optimistic.
5. Reconcile the findings with the narrative, risk section, and funding ask.
6. Flag weaknesses that need redesign rather than explanation.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the financial stress-test pack and that the decision concerns which downside breaks liquidity, break-even, or DSCR.
- **Stop condition:** halt the affected conclusion if required evidence is missing (working model, debt schedule, and operating assumptions) or if the work could lead to this identified risk: reporting resilience from scenarios that do not alter operating drivers.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Stress scenarios are plausible and decision-relevant.
- The analysis shows which levers matter most.
- Findings translate into financing or operating implications.
- The output makes the plan more credible, not merely more complex.

## Anti-Patterns

- Performing sensitivity analysis on trivial variables while ignoring core drivers.
- Presenting only mild downside cases.
- Stress-testing numbers that are already inconsistent in the base model.
- Failing to connect stress outcomes to actual management responses.
- Treating a generic financial stress test template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta financial stress test. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Financial Stress Test deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A stress-tested financial view with scenarios and key sensitivities
- Clear resilience findings and management implications
- Any assumptions or structural weaknesses needing correction


Validate and stress-test the financial projections from section 10 to prove the business model is resilient.

## When to Use

Invoke AFTER section 10 (Financial Projections) is complete. This skill takes the projections as input and produces stress-tested outputs.

## What to Generate

### 1. Four-Scenario Model

**Every stress test must produce four scenarios  not three.** The four-scenario model gives lenders confidence that the business has been honestly tested.

| Scenario | Revenue Adjustment | Cost Adjustment |
|---|---|---|
| **Optimistic** | +20 to +30% vs. base | 5% (efficiency gains) |
| **Base case** | 0% (the projection as written) | 0% |
| **Pessimistic** | 15 to 25% | +10 to +15% |
| **Extreme / Tail risk** | 35 to 50% | +20 to +30% |

**Rule:** The pessimistic scenario must be grounded in a plausible real-world event. Use calibrated shocks from Uganda's actual economic history  see `references/stress-test-methodology.md`. A 20% shock that cites "exchange rate depreciation + fuel cost increase" is credible; an unexplained 20% is not.

For each scenario, document explicit assumptions (revenue growth, gross margin, fixed costs, exchange rate, fuel cost, interest rate, repayment start). See the Scenario Assumption Table format in `references/stress-test-methodology.md`.

For each scenario, adjust:
- Revenue growth rate (use calibrated magnitudes from reference file)
- Customer acquisition cost (+/- 25%)
- Churn rate (+/- 50%)
- Operating costs (+/- 15%)
- Time to break-even (+/- 3-6 months)

### 2. Sensitivity Analysis

Test each key variable independently:

| Variable | -20% | -10% | Base | +10% | +20% | Impact Level |
|---|---|---|---|---|---|---|
| Unit price | | | $X | | | High/Med/Low |
| Volume | | | X | | | |
| COGS | | | $X | | | |
| CAC | | | $X | | | |
| Churn | | | X% | | | |

Identify which variables have the highest impact on profitability.

### 3. Break-Even Stress Test

- Base case break-even date
- How much revenue decline before break-even is unreachable?
- What is the maximum sustainable burn rate?
- How many months of runway remain in pessimistic case?

### 4. Cash Flow Stress Test

- Can the business survive 2 months of zero revenue?
- What happens if a major customer defaults?
- Impact of 60-day vs. 30-day payment terms
- Minimum cash reserve required

### 5. Key Risk Indicators

Define early warning triggers:

~~~text
IF monthly revenue < $X for 2 consecutive months  [Action]
IF CAC exceeds $X  [Action]
IF cash reserves drop below $X  [Action]
IF churn exceeds X%  [Action]
~~~

## Generation Process

1. Take financial projections from section 10 as input
2. Build three-scenario model by adjusting key assumptions
3. Run sensitivity analysis on 5-7 key variables
4. Stress-test break-even under adverse conditions
5. Stress-test cash flow under shock scenarios
6. Define early warning triggers and response actions
7. Summarise findings and flag critical vulnerabilities

## Output Format

Produce a stress test report with:
- Executive summary of resilience assessment
- Three-scenario comparison table
- Sensitivity analysis matrix
- Cash flow stress test results
- Risk trigger dashboard
- Recommendations for strengthening financial resilience

## Quality Criteria

- Four scenarios produced (optimistic, base, pessimistic, extreme)  three is insufficient
- Pessimistic scenario cites a specific, plausible Uganda risk event (e.g., "COVID-equivalent lockdown", "UGX 4,200/$ depreciation", "fuel cost +40%")
- Sensitivity analysis identifies the 2-3 variables that matter most
- Cash flow stress tests include realistic shock scenarios
- Early warning triggers are specific (revenue amount, DSCR level, cash reserve weeks) and actionable
- DSCR stress test shows all four scenarios with pass/fail against 1.25x bank minimum
- Recommendations are practical, not just "reduce costs"

## References

- `references/stress-test-methodology.md`  Calibrated Uganda historical shock data (COVID-19 by sector, FX depreciation 202123, fuel shock 2022, LGBTQ law 2023 economic fallout, coffee price cycle, regional security disruptions), sector-specific shock factors (agriculture/hospitality/retail/manufacturing), four-scenario framework, Scenario Assumption Table, DSCR Stress Test table, Breakeven Sensitivity Analysis table, Early Warning Dashboard (Green/Amber/Red triggers with specific UGX thresholds)

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Financial stress-test pack decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to reporting resilience from scenarios that do not alter operating drivers. |

## Capability and Permission Boundaries


Default to read-only inspection while producing the financial stress-test pack. Read supplied records and run non-mutating checks; running scenarios in a copy of the supplied model is permitted only when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If working model, debt schedule, and operating assumptions cannot be obtained, return a qualified financial stress-test pack covering only the checks that remain supportable. Leave this decision unresolved: which downside breaks liquidity, break-even, or DSCR. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which downside breaks liquidity, break-even, or DSCR | Record the conclusion, source trail, owner, and review trigger in the financial stress-test pack. | Risk of reporting resilience from scenarios that do not alter operating drivers |
| Material evidence conflicts or remains uncertain | Change the operating driver that creates the downside, rerun cash and debt schedules, and compare the breach date with the base case. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: working model, debt schedule, and operating assumptions | Mark the decision on which downside breaks liquidity, break-even, or DSCR `not assessed` in the financial stress-test pack, and send it to the model owner and credit or investment reviewer. | Otherwise, the work risks reporting resilience from scenarios that do not alter operating drivers |

## Quality Standards


Accept the financial stress-test pack only when evidence is sufficient for this decision: which downside breaks liquidity, break-even, or DSCR. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of reporting resilience from scenarios that do not alter operating drivers.

## Worked Example


A base model assumes 45 collection days. Re-run cash, overdraft, and DSCR at the evidenced downside collection period and report the first covenant or liquidity breach month.

<!-- dual-compat-end -->
