---
name: 00-plan-assembly
description: Use when producing or reviewing the 00 plan assembly component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Plan Assembly and Submission Skill

## Use When

- Use after the core sections and the main meta checks are complete.
- Use when the work needs to become a submission-ready package rather than a set of draft sections.
- Use when the final deliverable must be tailored to a specific funder or audience.

## Do Not Use When

- Do not use before synthesis, financial stress testing, and due-diligence review are complete.
- Do not use before critical thinking and business-logic gaps have been resolved or explicitly waived.
- Do not use as a substitute for fixing weak sections.
- Do not assemble a final package while major numerical contradictions remain unresolved.

## Required Inputs

- Completed or near-complete plan sections
- Funder type and submission mode
- Final funding ask, financials, and appendix evidence set
- Results from synthesis, bankability, DD, stress-test, and valuation workflows where relevant
- Results from `meta-critical-thinking-business-logic` where relevant

## Workflow

1. Confirm the plan has passed the required prerequisite skills.
2. Identify the primary recipient and submission context.
3. Assemble the document in the correct order for that audience.
4. Generate the covering letter, attachment checklist, and final TOC.
5. Apply `premium-commercial-writing` to the final client-facing package, especially the cover letter, executive summary, funding ask, and decision summaries.
6. Reconcile the final package against the funding ask, appendices, and page references.
7. Produce the final pre-submission issue list if anything still blocks handover.

## Quality Bar

- The assembled package reads like one submission, not stitched drafts.
- The covering letter, plan, and appendices all point to the same funding story.
- The package is tailored to the reader's decision criteria.
- Final checks catch numerical, structural, and documentary errors before submission.

## Anti-Patterns

- Assembling a pack before the numbers have stabilised.
- Using one generic package for bank, investor, DFI, and grant audiences.
- Leaving appendix evidence disconnected from the claims in the main body.
- Treating formatting as assembly while ignoring submission logic.

## Outputs

- Submission-ready package structure
- Covering letter
- Attachment checklist
- Final TOC and packaging order
- Final pre-submission issue list if needed



Convert a completed set of business-plan sections into a submission-ready document package. This skill is the last step before presenting to any funder.

## When to Use

Invoke AFTER:
- all 16 sections are drafted
- `meta-critical-thinking-business-logic` has been run and fatal logic, achievability, evidence, or assumption gaps are fixed
- `meta-consulting-synthesis` has been run and the plan has one governing thesis
- `meta-sustainability` Mode C audit has been run
- `meta-bankability-scoring` has been run and passes the required threshold
- financial projections have been stress-tested via `meta-financial-stress-test`
- accounting and financial consistency has been reviewed via `meta-accounting-finance-review` where projections, funding, tax, controls, inventory, payroll, valuation, or investor/lender readiness are material
- `meta-due-diligence` Mode C has been run
- `meta-valuation` has been run where the plan includes equity, convertible, SAFE, acquisition, strategic-partner, or blended-finance logic

After plan assembly, also prepare:
- deck using `meta-presentation-design`
- live pitch preparation using `meta-pitch-preparation`

## Step 1: Identify the Funder Type

Ask: who is the primary recipient of this business plan?

| Funder Type | Orientation | Key Difference |
|---|---|---|
| Commercial bank | Debt | DSCR and collateral front and centre |
| DFI | Long-term debt or blended capital | impact, safeguards, feasibility, governance |
| Grant body | Grant | redirect to `11b-grant-proposal` |
| Impact investor | Equity plus impact | cap table, valuation, scale story |
| Microfinance / SACCO | Small debt | simplified format, character references |

## Step 2: Generate the Covering Letter

Every submission requires a formal covering letter that states:

- exact amount requested
- facility or instrument type
- purpose of the funding
- legal identity of the business
- repayment source or value-creation logic
- key attachments enclosed

For bank submissions, state DSCR and collateral clearly.
For DFI submissions, state impact and safeguard readiness clearly.
For grants, use the separate grant-proposal workflow.

## Step 3: Package Order

Default order:

1. Covering letter
2. Executive summary
3. Core plan sections 02-14 in logical order
4. Funding request
5. Appendices
6. Sustainability strategy where required

For investor or DFI submissions, ensure the appendices include the evidence matrix and data-room index.

## Step 4: Required Attachments Checklist

Always verify:

- registration documents
- tax identifiers and licences
- director IDs and CVs
- financial statements or reconstructed records
- bank statements where relevant
- collateral documents where debt is sought
- sector licences and compliance certificates
- ESMP or safeguard materials where relevant

## Step 5: Table of Contents

Generate a table of contents with page numbers and confirm that all section references inside the plan point to the correct final pages.

## Step 6: Final Pre-Submission Check

Before handover, verify:

- all numbers reconcile across sections
- dates are internally consistent
- executive summary reflects final financials and final ask
- funding request matches implementation timing and appendix evidence
- valuation outputs are reflected correctly where equity or blended capital is involved
- appendices contain proof for every high-stakes claim

## References

- `meta-consulting-synthesis/SKILL.md` - run before assembly to force one thesis and resolve contradictions
- `meta-critical-thinking-business-logic/SKILL.md` - run before synthesis and assembly to test claims, assumptions, countercases, business logic, feasibility, and achievability
- `meta-valuation/SKILL.md` - required where valuation or investor-term logic appears
- `meta-accounting-finance-review/SKILL.md` - required where accounting consistency, finance controls, tax, inventory, payroll, valuation, or funder-ready numbers are material
- `meta-sustainability/SKILL.md` - sustainability audit before assembly
- `meta-due-diligence/SKILL.md` - due-diligence readiness and data-room structure
- `15-appendices/SKILL.md` - appendix architecture and evidence-matrix requirements
- `meta-presentation-design/SKILL.md` - deck design after assembly
- `meta-pitch-preparation/SKILL.md` - live delivery preparation after assembly
- `premium-commercial-writing/SKILL.md` - final premium commercial writing pass for cover letters, executive summaries, funding asks, proposal language, and investor/lender decision summaries

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Approved section set, model outputs, evidence register, and audience brief for 00 plan assembly | Pipeline section owners and release reviewer | Yes | If absent, any mandatory section, model output, or approval is unavailable, produce an assembly gap map and stop release rather than inserting filler. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Assembled business plan with cross-reference and release manifest | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 00 plan assembly exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 00 plan assembly release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Section-version register, reconciliation log, and unresolved-release finding list | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 00 plan assembly decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 00 plan assembly review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 00 plan assembly, the controlling focus is approved section versions, narrative-model reconciliation, cross-references, evidence completeness, audience requirements, and release gates. This skill may read and assemble approved sections and correct assembly defects; it may not rewrite an owner's financial assumption, suppress a failed gate, or publish the plan without release authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 00 plan assembly, loss of evidence about 00 plan assembly evidence, decisions, failure thresholds, ownership, and downstream handoffs activates degraded mode. If the controlling 00 plan assembly evidence is unavailable, the same boundary applies. When any mandatory section, model output, or approval is unavailable, produce an assembly gap map and stop release rather than inserting filler. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 00 plan assembly, two sections state different figures or strategic positions| identify the owning skill, return the conflict for reconciliation, and retain only the approved value supported by evidence | A polished document can conceal internal contradictions and an unsupported funding ask |
| For 00 plan assembly, A current legal, regulatory, tax, accounting, market, or platform claim controls the 00 plan assembly decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 00 plan assembly, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete assembled business plan with cross-reference and release manifest, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 00 plan assembly decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect approved section set, model outputs, evidence register, and audience brief and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce assembled business plan with cross-reference and release manifest with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Assembled business plan with cross-reference and release manifest must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Section-version register, reconciliation log, and unresolved-release finding list must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 00 plan assembly, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 00 plan assembly, treating an unavailable approved section set, model outputs, evidence register, and audience brief as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing assembled business plan with cross-reference and release manifest that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

The funding request asks for UGX 800 million while the implementation schedule allocates UGX 650 million. Block assembly and resume only after the use-of-funds schedule reconciles.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 00 plan assembly; no local deep-dive reference is declared.
- For 00 plan assembly claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
