---
name: meta-financial-stress-test
description: Analytical meta-skill that stress-tests financial projections through sensitivity analysis, four-scenario modelling (optimistic/base/pessimistic/extreme), break-even stress testing, DSCR stress test, and early warning dashboard. Calibrated to Uganda's actual economic history. Ensures the financial plan survives adversity and investor scrutiny.
---

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

## Required Inputs

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

## Outputs

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
- How much revenue decline before break-even is unreachableSection 
- What is the maximum sustainable burn rateSection 
- How many months of runway remain in pessimistic caseSection 

### 4. Cash Flow Stress Test

- Can the business survive 2 months of zero revenueSection 
- What happens if a major customer defaultsSection 
- Impact of 60-day vs. 30-day payment terms
- Minimum cash reserve required

### 5. Key Risk Indicators

Define early warning triggers:

```
IF monthly revenue < $X for 2 consecutive months  [Action]
IF CAC exceeds $X  [Action]
IF cash reserves drop below $X  [Action]
IF churn exceeds X%  [Action]
```

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
