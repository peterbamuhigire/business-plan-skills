---
name: 11b-grant-proposal
description: Use when producing or reviewing the 11b grant proposal component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Grant Proposal Skill

## Overview

Generate the grant proposal workflow and grant-specific funding narrative. Use this skill when the business case must be framed around beneficiaries, outcomes, accountability, and post-grant sustainability rather than lender repayment or investor returns.

## Use When

- Use when preparing a grant application, concept note, or donor-facing funding request.
- Use when the reader's primary concern is impact, beneficiary value, compliance, and accountability.
- Use when a business or social enterprise needs Theory of Change, LogFrame, impact logic, or budget narrative support.

## Do Not Use When

- Do not use for standard bank-loan or investor-funding narratives unless there is a genuine grant component.
- Do not treat a grant proposal as a softened business plan with impact language added on top.
- Do not invent beneficiaries, outcomes, or monitoring capability that the organisation cannot substantiate.

## Required Inputs

- Grant funder type, programme objectives, geography, and eligibility context
- Problem statement, beneficiary profile, delivery model, and implementation capacity
- Budget logic, co-funding assumptions, and post-grant sustainability plan
- Any evidence or adjacent drafts needed to support impact, safeguards, and accountability claims

## Workflow

1. Identify the grant type, evaluation logic, and non-negotiable donor requirements.
2. Reframe the case around beneficiaries, outcomes, and funder priorities.
3. Build the narrative, budget logic, Theory of Change, and implementation accountability.
4. Check that outputs, outcomes, indicators, and reporting commitments are internally consistent.
5. Reconcile the grant narrative with any underlying business-plan sections.
6. Flag missing evidence, partnerships, or compliance risks that weaken eligibility.

## Quality Bar

- The proposal answers the funder's mission, not just the applicant's needs.
- Beneficiaries, outcomes, and delivery logic are specific and measurable.
- Budget, activities, and impact claims reconcile cleanly.
- Sustainability after the grant period is credible.

## Anti-Patterns

- Reusing loan-language around repayment, collateral, or investor ROI as the core pitch.
- Writing impact claims with no measurement, baseline, or accountability plan.
- Treating beneficiaries as a vague audience rather than a defined target group.
- Hiding delivery, procurement, or reporting constraints.

## Outputs

- A grant-specific narrative, structure, and supporting grant artefacts
- Clear assumptions, eligibility questions, and evidence gaps
- Cross-skill notes for implementation, monitoring, risk, and budgeting



Write a compelling, compliant grant application for a Ugandan business or social enterprise. Grant funding requires a fundamentally different narrative from a bank loan  funders want to know about social impact, beneficiaries, sustainability, and accountability, not just financial returns.

## When to Use

Invoke when the business is applying to:
- **Government grants:** Youth Livelihood Programme (YLP), Women Enterprise Programme (WEP), Parish Development Model (PDM), Emyooga/GROW programme, National Agricultural Advisory Services (NAADS)
- **Development partner grants:** USAID, EU, GIZ, DFID/FCDO, UN Women, FAO, UNDP, WFP, UNICEF
- **Impact funds:** Mastercard Foundation, Ford Foundation, Tony Elumelu Foundation, African Development Foundation
- **Research/innovation grants:** NARO, MTIC innovation fund, UNCST
- **Climate finance:** GCF (Green Climate Fund), GEF small grants, African Development Bank climate facility

## Core Difference from a Bank Loan Application

| Element | Bank Loan Plan | Grant Proposal |
|---|---|---|
| Primary question | "Can you repay?" | "What impact will this have?" |
| Financial focus | DSCR, collateral, profit | Budget narrative, cost-effectiveness |
| Beneficiary focus | Not required | Central  disaggregated by gender, age, income |
| Theory of Change | Not required | Required  how inputs lead to outcomes and impact |
| LogFrame | Not required | Required or strongly preferred |
| Sustainability plan | Implicit (profitable business) | Explicit  what happens after grant ends? |
| Procurement | Not mentioned | Competitive procurement plan required |
| Reporting | Annual accounts | Quarterly narrative + financial reports |
| Audit | By accountant | Often by independent auditor approved by funder |

## Step 1: Project Summary (Executive Summary for Grant)

Write a concise project summary (max 1 page / 400 words):

```text
PROJECT SUMMARY

Project Title: [Specific, descriptive  not generic]
Implementing Organisation: [Legal name, registration number]
Project Location: [Specific districts/sub-counties]
Project Duration: [Start date] to [End date] ([X months])
Total Budget Requested: UGX [X] / USD [X]
Co-Financing (if any): UGX [X] from [source]

Problem Statement:
[23 sentences: what specific problem does this project address?
Use data  e.g., "In Luwero District, 68% of youth aged 18-30 are
unemployed (UBOS 2024), and less than 12% of smallholder farmers
access formal markets for their produce."]

Project Objective:
[12 sentences: the specific, measurable change this project will
achieve  e.g., "To establish a certified mango processing facility
employing 45 youth (60% women) and connecting 200 smallholder
farmers to formal export markets within 24 months."]

Key Outputs:
1. [Specific output  e.g., "Mango processing facility operational,
   capacity 2 tonnes/day"]
2. [Specific output]
3. [Specific output]

Expected Impact:
[Key impact figure  jobs created, incomes improved, people reached]
```

## Step 2: Problem Analysis and Context

Provide evidence-based problem diagnosis:

1. **Statistical evidence:** UBOS data, sector surveys, UNDP reports, World Bank indicators
2. **Geographic specificity:** Which districts, sub-counties, communities?
3. **Target group analysis:** Who is affected? Age, gender, income level, vulnerability characteristics
4. **Root cause analysis:** Why does this problem persist? (Use 5 Whys or fishbone analysis from `12-risk-analysis`)
5. **Gap analysis:** What existing interventions exist and why are they insufficient?
6. **Opportunity framing:** Why is now the right time to address this problem?

## Step 3: Theory of Change

The Theory of Change (ToC) is the logical argument that connects your activities to long-term impact. It is required by most international development funders.

### ToC Structure

```text
IF we [do these activities]...
THEN we will produce [these outputs]...
WHICH WILL LEAD TO [these outcomes] for [these beneficiaries]...
BECAUSE [state the assumptions]...
WHICH WILL CONTRIBUTE TO [this long-term impact].
```

### ToC Template

```text
THEORY OF CHANGE

INPUTS  ACTIVITIES  OUTPUTS  OUTCOMES  IMPACT

INPUTS:
- Grant funding: UGX [X]
- Co-financing: UGX [X]
- Implementing org capacity: [staff, expertise, facilities]
- Partner organisations: [names and roles]

ACTIVITIES:
1. [Activity 1  e.g., "Procure and install mango processing equipment"]
2. [Activity 2  e.g., "Train 45 youth operators in food safety and
   equipment operation (20 days)"]
3. [Activity 3  e.g., "Establish farmer linkages with 200 smallholders
   in 5 sub-counties"]
4. [Activity 4  e.g., "Obtain UNBS certification and export market access"]

OUTPUTS (direct, measurable products of activities):
1. Processing facility operational  capacity [X] tonnes/day
2. [X] youth trained and certified in [skill]
3. [X] farmers contracted with minimum price guarantee
4. UNBS certification obtained; [X] export contracts signed

OUTCOMES (changes in behaviour, knowledge, or conditions):
Short-term (012 months):
- [X] youth employed at living wage of  UGX [X]/month
- Farmer incomes increase by [X]% due to price premium

Medium-term (1236 months):
- [X] youth achieve financial independence and savings targets
- Smallholder farmers access formal markets independently

LONG-TERM IMPACT:
Reduced youth unemployment and increased rural household incomes
in [target area], contributing to Uganda's NDP III objective of
[relevant NDP III target].

KEY ASSUMPTIONS:
- Stable electricity supply (risk mitigation: generator installed)
- Continued mango supply from partner farmers
- Export market demand maintains [X] price level
- Regulatory approvals obtained within [X] months
```

## Step 4: Logical Framework (LogFrame)

The LogFrame (Logical Framework Matrix) is a mandatory tool for EU, USAID, UN, and most bilateral funders.

### LogFrame Template

| Level | Description | Objectively Verifiable Indicators (OVIs) | Means of Verification (MoV) | Assumptions / Risks |
|---|---|---|---|---|
| **Goal (Impact)** | The long-term development goal this project contributes to | [Indicator at national/sector level] | [UBOS surveys, national statistics] | [External factors needed for impact to hold] |
| **Purpose (Outcome)** | The specific change this project will achieve in the target group | [SMART indicator  who, what, how much, by when] | [Project survey, monitoring data] | [What must hold for outputs to achieve purpose] |
| **Output 1** | [First deliverable] | [Quantity, quality, time] | [Activity reports, receipts] | [Input/activity assumptions] |
| **Output 2** | [Second deliverable] | [Quantity, quality, time] | [Inspection reports] | |
| **Output 3** | [Third deliverable] | [Quantity, quality, time] | [Training records] | |
| **Activities** | What the project does to produce each output | Budget and timeline | Financial reports | Resources available as planned |

**Example row (Purpose level):**
| **Purpose** | 45 youth employed in mango processing with incomes  UGX 300,000/month | By Month 18: 45 youth employed, 60% female, average wage UGX 350,000/month | Payroll records, employment contracts, spot checks | Mango processing facility operational; UNBS certification obtained |

## Step 5: Beneficiary Analysis

Grant funders require detailed beneficiary analysis, disaggregated by:

```text
DIRECT BENEFICIARIES (directly receive project services):
- Total: [X] individuals
- Women: [X] ([X]%)
- Youth (1835): [X] ([X]%)
- Persons with disabilities: [X] ([X]%)
- District: [Name], Sub-counties: [List]
- Current income level: Average UGX [X]/month before project

INDIRECT BENEFICIARIES (benefit from project outcomes):
- Smallholder farmer households: [X] (approx. [X] household members)
- Community members benefiting from local employment: [X]
- Local suppliers and service providers: [X] businesses

GENDER MAINSTREAMING:
[How does the project specifically address gender equality?]
- Minimum 60% women in employment targets
- Women-specific training on [skills]
- Flexible working arrangements for mothers
- Equal pay policy

MOST VULNERABLE:
[How does the project reach the most marginalised?]
```

## Step 6: Implementation Plan and Work Plan

```text
WORK PLAN

Phase 1: Inception (Months 13)
- Month 1: Sign contracts, open project account, hire project staff
- Month 2: Procure equipment (competitive tender)
- Month 3: Site preparation, baseline survey, farmer registration

Phase 2: Implementation (Months 418)
- Months 46: Equipment installation, staff training
- Months 712: Facility operational, first processing cycle
- Months 1318: Scale up, certification, export market entry

Phase 3: Sustainability (Months 1924)
- Month 1922: Transition to commercial operations
- Month 2324: Final evaluation, knowledge sharing, exit plan
```

## Step 7: Budget Narrative

Every budget line must be justified. Funders look for:
- **Reasonable unit costs:** Compare to market rates; justify any above-average costs
- **Proportionality:** Personnel costs typically max 3040% of total budget for infrastructure projects
- **No double-funding:** Items funded by other sources must be identified
- **Allowable costs:** Check funder guidelines  some do not fund overhead, land purchase, or contingency above 5%

### Budget Narrative Format

```text
BUDGET NARRATIVE

1. EQUIPMENT AND CAPITAL ITEMS: UGX [X]
   1.1 Mango processing line (grader + slicer + dryer): UGX [X]
       Justification: Sourced from [supplier], proforma invoice attached.
       Capacity: [X] tonnes/day. Competitive bids obtained from 3 suppliers.
   1.2 Generator (50 kVA): UGX [X]
       Justification: Required for power backup  UMEME grid unreliable in
       [location]; average 4 outages/week. Generator protects [X] hours of
       daily production.

2. PERSONNEL: UGX [X] ([X]% of budget)
   2.1 Project Manager (1 FTE  24 months  UGX [X]/month): UGX [X]
       Role: Overall project coordination and reporting
   2.2 Technical Trainer (0.5 FTE  6 months  UGX [X]/month): UGX [X]
       Role: Equipment operation training for 45 youth employees

3. TRAINING AND CAPACITY BUILDING: UGX [X]
   3.1 Youth operator training (45 persons  20 days  UGX [X]/day): UGX [X]
       Includes: Training materials, venue hire, refreshments, trainee
       subsistence allowance

4. MONITORING AND EVALUATION: UGX [X]
   Includes: Baseline survey, midterm review, final evaluation,
   data management system

5. ADMINISTRATIVE AND OVERHEAD: UGX [X] ([X]% of total  within [funder] limit)
   Office running costs, communications, bank charges

TOTAL PROJECT COST: UGX [X]
Grant requested: UGX [X] ([X]%)
Co-financing (promoter equity): UGX [X] ([X]%)
```

## Step 8: Sustainability Plan

Grant funders require convincing evidence the project continues after funding ends:

```text
SUSTAINABILITY PLAN

Financial sustainability:
After Month 24, [Business Name] will operate as a commercial entity,
generating revenue from [revenue streams]. Projected Year 3 revenue:
UGX [X]. Projected Year 3 net surplus: UGX [X]. The business will
self-finance operations and reinvest in expansion.

Institutional sustainability:
The implementing organisation [Name] will continue to operate the
facility under commercial management. Key staff will be retained
as permanent employees funded from processing revenues.

Environmental sustainability:
[How does the project avoid negative environmental impacts long-term?
Waste management plan, NEMA compliance, organic waste composting, etc.]

Social sustainability:
Farmer contracts are renewable annually. Community ownership model
ensures local stakeholders have vested interest in project success.
Women's savings group established to maintain female employee
financial inclusion after project close.

Exit strategy:
The project intends to transition to [independent commercial operation /
cooperative ownership / franchise model]. The grant funder's exit is
planned for [Month 24] following final evaluation and handover.
```

## Step 9: Monitoring and Evaluation Framework

Cross-reference `meta-monitoring-evaluation/SKILL.md` for the full M&E framework. For grants, add:

- Baseline data collection (before project starts)
- Quarterly narrative reports to funder (format per funder template)
- Quarterly financial reports (actual vs. budget with variance explanation)
- Mid-term review (Month 12)  often funder-led
- Final evaluation (Month 2224)  independent evaluator recommended
- Data disaggregation by gender, age, disability for all beneficiary indicators

## Step 10: Government Grant Specifics (Uganda)

### Youth Livelihood Programme (YLP)  Ministry of Gender
- Groups of 1530 youth applying collectively
- Revolving fund model: grant is repaid to fund new groups
- Application through Parish/Sub-county Chief
- Required: Business plan, group constitution, meeting minutes, NIN for all members
- Maximum: UGX 25M per group (verify current limits with Ministry)

### Parish Development Model (PDM)  MFPED
- Village Savings and Loan Associations (VSLAs) as delivery mechanism
- Focus on subsistence households transitioning to commercial farming
- Application through Parish Development Committee
- Maximum: UGX 1M per household per funding cycle (verify current limits)

### Women Enterprise Programme (WEP) / Emyooga
- Women-only or women-majority groups
- Application through UWEP/Emyooga SACCOs
- Financial literacy and business skills training required before disbursement

### NAADS / OWC (Operation Wealth Creation)
- Agricultural inputs focus (seeds, livestock, equipment)
- Application through District Production Office
- Must have: land, water source, group membership

## References

- `references/logframe-templates.md`  Full LogFrame templates by funder type
- `references/theory-of-change.md`  Detailed ToC construction with Uganda examples
- `references/budget-narrative-templates.md`  Line-by-line budget justification templates
- `meta-monitoring-evaluation/references/funder-reporting-requirements.md`  Quarterly report formats
- [`04-market-analysis/references/uganda-human-capital-2025.md`](../04-market-analysis/references/uganda-human-capital-2025.md)  World Bank (2025) human capital evidence base for grant problem statements: HCI 0.39 (Uganda harnesses only 39% of potential); NEET youth 5.25M; Vision 2040 GDP targets; education spending gaps (2.7% vs 4.2% EA average); health outcomes table (life expectancy 68.5 years, maternal mortality 189, under-5 mortality 52); social protection coverage only 3%; NUSAF 3 impact evidence (savings rate 54.6%70%, NUSAF 3 saved GoU 51% of emergency fund = UGX 19B); WASH gap (12M without basic water, 38M without safe sanitation); multidimensional poverty 41.2%. **Read when writing the problem statement and contextual evidence section of any Uganda grant proposal  especially for youth employment, education, health, agriculture, and WASH-sector applications.**
- [`05-target-market/references/uganda-consumer-demographics-2025.md`](../05-target-market/references/uganda-consumer-demographics-2025.md)  Beneficiary profiling data: population disaggregation by age, gender, region, income quintile, education level, and urban/rural location; NEET breakdown (women 52%, men 28%); regional market characteristics (Karamoja, Northern, Eastern, Western, Central); social protection transfer recipient segments; literacy gaps (57% of P6 below minimum). **Read when disaggregating beneficiaries by gender, age, income, and vulnerability for LogFrame indicators and funder reporting.**

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Funder call, eligibility rules, problem evidence, theory of change, work plan, budget, safeguards, and applicant credentials for 11b grant proposal | Official funder documents, client evidence, implementing partners, and finance model | Yes | If absent, the official call, eligibility rule, beneficiary baseline, partner commitment, or budget basis is unavailable, mark the proposal blocked at that requirement and return the exact evidence request. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Compliant grant proposal with theory of change, logframe, work plan, budget narrative, and sustainability case | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 11b grant proposal exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 11b grant proposal release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Requirement matrix, claim-source register, results-chain test, budget-to-activity reconciliation, and partner proof | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 11b grant proposal decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 11b grant proposal review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 11b grant proposal, the controlling focus is funder eligibility, problem evidence, results chain, beneficiary safeguards, work plan, budget, additionality, and sustainability. This skill may analyse the call and draft application material; it may not submit, sign declarations, invent beneficiaries or co-funding, contact the funder, or commit partners without explicit authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 11b grant proposal, loss of evidence about funder eligibility, problem evidence, results chain, beneficiary safeguards, work plan, budget, additionality, and sustainability activates degraded mode. If the controlling 11b grant proposal evidence is unavailable, the same boundary applies. When the official call, eligibility rule, beneficiary baseline, partner commitment, or budget basis is unavailable, mark the proposal blocked at that requirement and return the exact evidence request. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 11b grant proposal, a desirable activity does not contribute to a stated outcome or cannot be measured within the grant period| remove or redesign it and repair the results chain and budget | A fluent application can still fail eligibility, credibility, safeguarding, or value-for-money review |
| For 11b grant proposal, A current legal, regulatory, tax, accounting, market, or platform claim controls the 11b grant proposal decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 11b grant proposal, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete compliant grant proposal with theory of change, logframe, work plan, budget narrative, and sustainability case, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 11b grant proposal decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect funder call, eligibility rules, problem evidence, theory of change, work plan, budget, safeguards, and applicant credentials and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce compliant grant proposal with theory of change, logframe, work plan, budget narrative, and sustainability case with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Compliant grant proposal with theory of change, logframe, work plan, budget narrative, and sustainability case must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Requirement matrix, claim-source register, results-chain test, budget-to-activity reconciliation, and partner proof must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 11b grant proposal, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 11b grant proposal, treating an unavailable funder call, eligibility rules, problem evidence, theory of change, work plan, budget, safeguards, and applicant credentials as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing compliant grant proposal with theory of change, logframe, work plan, budget narrative, and sustainability case that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

The proposal promises 5,000 trained beneficiaries, but venue and facilitator capacity supports 1,200. Reduce or phase the target, reconcile the work plan and budget, and preserve 5,000 only as a longer-term ambition.

## References

- [Load this skill's primary method or template](../04-market-analysis/references/uganda-human-capital-2025.md) before applying the 11b grant proposal decision rules.
- For 11b grant proposal claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
