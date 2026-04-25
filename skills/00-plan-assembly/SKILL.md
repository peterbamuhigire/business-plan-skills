---
name: plan-assembly
description: Final assembly skill that converts completed business-plan sections into a submission-ready package. Generates the covering letter, table of contents, required attachments checklist, and submission format guidance calibrated to the specific funder type.
---

# Plan Assembly and Submission Skill

## Use When

- Use after the core sections and the main meta checks are complete.
- Use when the work needs to become a submission-ready package rather than a set of draft sections.
- Use when the final deliverable must be tailored to a specific funder or audience.

## Do Not Use When

- Do not use before synthesis, financial stress testing, and due-diligence review are complete.
- Do not use as a substitute for fixing weak sections.
- Do not assemble a final package while major numerical contradictions remain unresolved.

## Required Inputs

- Completed or near-complete plan sections
- Funder type and submission mode
- Final funding ask, financials, and appendix evidence set
- Results from synthesis, bankability, DD, stress-test, and valuation workflows where relevant

## Workflow

1. Confirm the plan has passed the required prerequisite skills.
2. Identify the primary recipient and submission context.
3. Assemble the document in the correct order for that audience.
4. Generate the covering letter, attachment checklist, and final TOC.
5. Reconcile the final package against the funding ask, appendices, and page references.
6. Produce the final pre-submission issue list if anything still blocks handover.

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
- `meta-consulting-synthesis` has been run and the plan has one governing thesis
- `meta-sustainability` Mode C audit has been run
- `meta-bankability-scoring` has been run and passes the required threshold
- financial projections have been stress-tested via `meta-financial-stress-test`
- `meta-due-diligence` Mode C has been run
- `meta-valuation` has been run where the plan includes equity, convertible, SAFE, acquisition, strategic-partner, or blended-finance logic

After plan assembly, also prepare:
- deck using `meta-presentation-design`
- live pitch preparation using `meta-pitch-preparation`

## Step 1: Identify the Funder Type

Ask: who is the primary recipient of this business planSection 

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
- `meta-valuation/SKILL.md` - required where valuation or investor-term logic appears
- `meta-sustainability/SKILL.md` - sustainability audit before assembly
- `meta-due-diligence/SKILL.md` - due-diligence readiness and data-room structure
- `15-appendices/SKILL.md` - appendix architecture and evidence-matrix requirements
- `meta-presentation-design/SKILL.md` - deck design after assembly
- `meta-pitch-preparation/SKILL.md` - live delivery preparation after assembly
