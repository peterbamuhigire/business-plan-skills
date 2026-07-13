---
name: 11-funding-request
description: Use when producing or reviewing the 11 funding request component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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
- `saas-agent-funding-stage-playbook/SKILL.md` - agent-business funding playbook by stage (pre-seed → growth); agent-specialist / vertical AI / sovereign-AI / DFI investor archetypes; agent-specific use-of-proceeds shape and milestone breakpoints
- `saas-agent-investor-narrative-on-sla/SKILL.md` - SLA narrative for fundraising (confidence-builder vs liability question); peer benchmarks; SLA-as-moat positioning; pitch-deck slide; data-room SLA section; quarterly investor-update SLA block; FAQ rebuttal library

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria for 11 funding request | Financial model, implementation plan, client records, and target-financier materials | Yes | If absent, the funding gap, uses, repayment capacity, dilution effect, or stage evidence is unavailable, return a financing-readiness gap note and withhold the amount or instrument recommendation. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Audience-specific funding request with instrument, uses, milestones, and repayment or return logic | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 11 funding request exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 11 funding request release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Ask-to-use reconciliation, financing-option decision record, milestone release logic, and caveat register | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 11 funding request decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 11 funding request review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 11 funding request, the controlling focus is funding quantum, instrument fit, use of funds, repayment or return logic, and financing conditions. This skill may analyse financing options and draft the ask; it may not solicit investors, submit applications, negotiate terms, value securities, or bind the client without explicit authority and professional review. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 11 funding request, loss of evidence about funding quantum, instrument fit, use of funds, repayment or return logic, and financing conditions activates degraded mode. If the controlling 11 funding request evidence is unavailable, the same boundary applies. When the funding gap, uses, repayment capacity, dilution effect, or stage evidence is unavailable, return a financing-readiness gap note and withhold the amount or instrument recommendation. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 11 funding request, the preferred instrument does not match cash-flow capacity, stage, security, or investor-return evidence| reject it, compare the viable alternatives, and state the milestone needed to reopen the option | A mismatched ask can create unaffordable debt, avoidable dilution, or failed diligence |
| For 11 funding request, A current legal, regulatory, tax, accounting, market, or platform claim controls the 11 funding request decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 11 funding request, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete audience-specific funding request with instrument, uses, milestones, and repayment or return logic, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 11 funding request decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce audience-specific funding request with instrument, uses, milestones, and repayment or return logic with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Audience-specific funding request with instrument, uses, milestones, and repayment or return logic must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Ask-to-use reconciliation, financing-option decision record, milestone release logic, and caveat register must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 11 funding request, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 11 funding request, treating an unavailable reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing audience-specific funding request with instrument, uses, milestones, and repayment or return logic that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A profitable business requests equipment debt but allocates part of the loan to speculative product research. Separate financeable assets from uncertain R&D and match each use to an affordable instrument.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 11 funding request; no local deep-dive reference is declared.
- For 11 funding request claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
