---
name: funding-request
description: Generate the funding request section for Uganda/East Africa context covering bank loans, DFI funding, equity, grants, or combinations. Use for capital ask, use of funds, DSCR logic, collateral statement, CAMPARI alignment, investor terms, and valuation-linked funding strategy.
---

# Funding Request and Use of Funds Skill

## Use When

- Use when translating the business case into a specific ask to a bank, investor, DFI, or other capital provider.
- Use when the plan must show exact use of funds, repayment logic, ownership consequences, or term logic.
- Use when the funding ask needs to align tightly with implementation and financial projections.

## Do Not Use When

- Do not use before the financial model and implementation budget are stable enough to support a real ask.
- Do not use a debt-style ask for an equity case or vice versa.
- Do not use a generic funding paragraph when the audience expects a structured ask.

## Required Inputs

- Funder type and desired instrument
- Final or near-final projections, DSCR logic, and implementation budget
- Collateral, equity contribution, cap-table, or valuation information as relevant
- Milestones funded and intended next step for the capital provider

## Workflow

1. Identify the capital provider and the funding instrument.
2. Tie the ask to the implementation plan and the financial model.
3. Build the use-of-funds table at line-item level.
4. For debt, show repayment source, DSCR, and collateral logic.
5. For equity or blended capital, show valuation, dilution, milestone, and exit logic.
6. Reconcile the funding section against appendices, financials, and timelines.

## Quality Bar

- The ask is exact, not vague.
- The use of funds is traceable to real execution needs.
- Debt asks are serviceable and equity asks are valuation-defensible.
- The section reads like a real capital request, not a placeholder.

## Anti-Patterns

- Asking for a rounded headline amount with no line-item logic.
- Mixing debt and equity language without clarifying the instrument.
- Presenting valuation as negotiation posture instead of analytical output.
- Leaving the capital provider to infer how the money will be used.

## Outputs

- Funding request section
- Use-of-funds table
- Debt or equity logic tailored to the audience
- Any unresolved term, collateral, or valuation issues



Generate the section that tells lenders or investors exactly what is being requested, how it will be used, and why the request is financeable.

## Funder Type Identification

Identify the primary funder first:

| Funder Type | Primary Concern | What They Want to See |
|---|---|---|
| Ugandan commercial bank | Repayment security | DSCR >= 1.25x; collateral >= 125%; CAMPARI compliance |
| DFI | Development impact plus viability | jobs, sector fit, safeguards, DSCR |
| Microfinance / SACCO | Cash flow and character | transaction history, guarantees, repayment realism |
| Equity investor | Return on investment | growth, valuation, dilution, exit, traction |
| Development partner grant | Programme objectives | use `11b-grant-proposal` |
| Government programme | Eligibility and social criteria | beneficiary fit, sector, group status |

Default for Uganda SME plans: commercial bank or DFI.

## Bank Loan Mode

### Required Elements

1. Exact funding amount in UGX
2. Facility type: term loan, working-capital line, overdraft, asset finance, or invoice finance
3. Itemised use of funds tied exactly to Section 13 implementation budget
4. Proposed term, grace period, and repayment source
5. DSCR from Section 10 projections
6. Owner equity contribution
7. Collateral and coverage ratio
8. Security documents available
9. Compensating factors if collateral is weak

### Bank Use-of-Funds Format

| Line Item | Amount (UGX) | % of Facility | Purpose |
|---|---|---|---|
| [Asset / spend item] | [X] | [X%] | [specific use] |
| [Asset / spend item] | [X] | [X%] | [specific use] |
| Working capital | [X] | [X%] | [months covered] |
| Total facility request | [X] | 100% | |
| Owner equity contribution | [X] | - | own funds or existing assets |
| Total project cost | [X] | | |

### DSCR Statement

State:

- EBITDA or cash available for debt service
- annual debt service
- DSCR result
- whether the plan clears the 1.25x threshold
- mitigation if Year 1 is weak

### Collateral Statement

State:

- asset type
- description and ownership
- estimated value
- valuation basis
- coverage ratio
- documents available

## Equity Investor Mode

### Required Elements

1. Exact amount being raised
2. Instrument type: equity, convertible note, SAFE, or combination
3. Detailed use of funds
4. Current cap table
5. Valuation basis
6. Investment terms
7. Milestones funded
8. Runway created
9. Future funding needs
10. Exit strategy

### Mandatory Valuation Step

For every equity, convertible, SAFE, strategic-investor, acquisition, or blended-finance case, run `meta-valuation` before finalising this section.

Minimum outputs required from `meta-valuation`:

- valuation purpose and audience
- base, upside, and downside range
- method used and why it fits the stage
- implied pre-money and post-money values
- ownership / dilution consequence
- sanity-check commentary on comparables and assumptions

### Equity Use-of-Funds Format

| Category | Amount | % of Total | Purpose |
|---|---|---|---|
| Product / service build | [X] | [X%] | [deliverables] |
| Commercial growth | [X] | [X%] | [channels / hires] |
| Operations | [X] | [X%] | [equipment / systems] |
| Working capital | [X] | [X%] | [runway support] |
| Team / capability build | [X] | [X%] | [roles / training] |

## Generation Process

1. Identify the funder type
2. For debt: gather amount, purpose, term, collateral, and owner contribution
3. For equity: gather amount, instrument, current cap table, and milestone target
4. Build the detailed use-of-funds table and tie it to Section 13
5. For debt: calculate DSCR and collateral coverage
6. For equity: calculate runway, define terms, and state exit logic
7. For equity or blended capital: integrate `meta-valuation` output into the ask and terms
8. Verify consistency against `meta-bankability-scoring/references/consistency-audit.md`
9. Where material technology, systems, or expansion spend is requested, include a short business-case rationale: problem solved, option chosen, expected benefit, timing, and downside controls

## Quality Criteria

- Ask is specific and single-point, not a range
- Use of funds is line-item based and totals correctly
- Use of funds aligns with implementation timing
- For bank loans: DSCR >= 1.25x, collateral >= 125%, repayment source identified
- For bank loans: run `meta-bankability-scoring` before submission
- For equity: runway reaches the next major milestone and exit logic is realistic
- For equity: valuation comes from `meta-valuation`, not unsupported negotiation positioning
- Material technology and expansion line items are justified by execution logic and incremental benefit, not by vague modernisation language

## References

- `../meta-valuation/SKILL.md` - required for all equity, convertible, SAFE, strategic-investor, and blended-finance asks
- `references/business-valuation-methods.md` - repo-specific valuation methods and East Africa adjustments
- `references/equity-term-sheets.md` - term-sheet mechanics and cap-table implications
- `references/credit-assessment-frameworks.md` - 5 Cs and CAMPARI
- `references/women-financing-uganda.md` - collateral constraints and alternative pathways
- `references/esmp-template.md` - safeguards and ESMP requirements for DFI cases
- `references/uganda-banking-sector-2025.md` - lending context and pricing benchmarks
- `references/uganda-banking-loan-framework.md` - Uganda bank underwriting practice
- `references/uganda-financial-sector-regulatory.md` - financing-channel selection and compliance
- `references/msme-financing-options-ea.md` - financing fit by stage and business maturity
- `references/africa-infrastructure-financing.md` - relevant for infrastructure, PPP, and blended-finance cases
- `../book-extractions/haines-how-to-create-a-business-case-extraction.md` - use when the ask includes a major system, automation, capacity, or market-entry investment that needs clearer option logic and incremental benefits
- `meta-bankability-scoring/SKILL.md` - bank readiness scoring and consistency checks
- `meta-due-diligence/SKILL.md` - DD readiness before investor or DFI outreach
- `meta-presentation-design/SKILL.md` - ask-slide and use-of-funds presentation standards
