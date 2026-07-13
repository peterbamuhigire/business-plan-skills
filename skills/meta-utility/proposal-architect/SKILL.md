---
name: proposal-architect
description: Use when coordinating a proposal, bid, tender, EOI, or RFP response from intake through compliant draft and document handoff; route specialised procurement methodology to the external proposal-skills engine.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Proposal Architect

Coordinate the local business-plan suite's proposal workflow without replacing the canonical proposal-skills engine. Keep opportunity evidence, compliance, technical response, budget logic, review, and compilation traceable from source to final document.

<!-- dual-compat-start -->
## Use When

- Starting or resuming a proposal, bid, tender, EOI, grant-like response, or RFP submission.
- Converting solicitation documents into a compliance matrix, section plan, drafting workflow, and evidence register.
- Coordinating technical narrative, financial proposal, annexes, review, and DOCX/PDF handoff.

## Do Not Use When

- Use the external `proposal-skills` engine for specialised tender strategy, procurement response doctrine, evaluator simulation, or bid review.
- Use `11b-grant-proposal` when the task is a business-plan grant section rather than a full procurement response.
- Do not draft from an unread or incomplete solicitation when a missing instruction could create a knockout failure.

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when missing |
| --- | --- | ---: | --- |
| Solicitation, TOR, RFP, tender, or EOI documents | Issuing authority or client workspace | Yes | Stop compliance claims and request the controlling document. |
| Submission instructions, deadlines, and evaluation criteria | Solicitation and clarifications | Yes | Mark the bid blocked where the omission could cause disqualification. |
| Bidder credentials and evidence | Client evidence register | Yes | Leave unsupported claims out and assign an evidence owner. |
| Technical approach and price inputs | Subject-matter and finance owners | Conditional | Produce a gap register; do not invent methodology, rates, costs, or staffing. |

## Workflow

1. Confirm authority, proposal type, issuer, deadline, submission channel, and whether the workspace is new or continuing.
2. Inventory every source file, clarification, form, template, eligibility condition, and mandatory signature; stop on unreadable or contradictory controlling documents.
3. Produce an opportunity analysis covering deliverables, evaluation criteria, compliance requirements, budget rules, dates, themes, risks, and a section plan.
4. Build the compliance matrix, evidence register, responsibility map, and outline before drafting. Recover missing evidence by assigning an owner and due date, not by inserting an unsupported claim.
5. Draft section by section against the evaluation criteria. Apply the external proposal engine, relevant sector skills, finance doctrine, and research evidence as triggered.
6. Run compliance, red-team, finance, consistency, anti-slop, document-tooling, and rendering checks. Stop release on a knockout, unresolved contradiction, unverified price, missing form, or failed render.
7. Compile the authorised technical and financial outputs, preserve version history, and hand off the evidence pack with caveats and submission responsibility.

## Quality Standards

- Every requirement maps to an owner, response location, evidence item, and completion state.
- The response makes an evaluator-visible claim, evidence, warrant, and implication rather than generic capability statements.
- The technical method, workplan, team, budget, assumptions, and deliverables reconcile.
- Current procurement, tax, statutory, exchange-rate, or issuer facts are dated and verified.
- Document files are not claimed complete until written, opened, rendered, and checked.

## Anti-Patterns

- Drafting before extracting mandatory requirements. Correction: build the compliance matrix and knockout register first.
- Repeating the TOR as a methodology. Correction: state the bidder's sequence, roles, tools, evidence, decisions, and quality controls.
- Claiming experience without a supporting reference. Correction: link each credential to a named contract, certificate, CV, or approved evidence gap.
- Hiding an unpriced activity in technical prose. Correction: reconcile every resource and deliverable with the financial proposal.
- Treating a missing annex as a formatting issue. Correction: classify its compliance impact and block submission when mandatory.
- Compiling DOCX or PDF without rendering. Correction: open and visually verify pagination, tables, headings, signatures, and annex order.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Opportunity analysis and compliance matrix | Bid lead and section owners | Every mandatory instruction, criterion, deliverable, date, and form has a traceable response state. |
| Technical and financial proposal drafts | Evaluator and submission owner | Claims are evidenced; approach, staffing, workplan, and budget reconcile. |
| Submission evidence pack | Reviewer and authorised submitter | Includes source register, review results, render evidence, open caveats, and final responsibility. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Requirement trace | Matrix row with source location, owner, response, evidence, and status | No mandatory item is silently omitted. |
| Review record | Compliance, red-team, finance, anti-slop, and render results | Blocking findings are closed or the proposal remains blocked. |
| Compilation manifest | File list, versions, checksums or timestamps, and output checks | The handed-off files match the reviewed content. |

<!-- dual-compat-end -->
## Capability Contract

Read and search proposal sources and authorised evidence. Edit only the proposal workspace when drafting authority is explicit. Execute document conversion and validation only with approved local tooling. Network research must follow the digital-research engine. Sending, portal submission, external messaging, accepting terms, spending, signing, and certification require explicit human authority.

## Degraded Mode

Fallback: if a solicitation file, evidence source, finance input, converter, renderer, font, or network source is unavailable, return the narrowest qualified artefact and mark affected checks `not assessed`. Preserve the blocker, owner, and recovery action; never declare a proposal compliant, priced, compiled, or submission-ready without evidence.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A mandatory requirement is absent or contradicted | Stop the affected draft and seek clarification or evidence | Knockout or non-responsive bid. |
| Evaluation weighting is explicit | Allocate effort and proof in proportion to scored criteria | Polished low-value sections crowding out decisive content. |
| The proposal touches money, tax, grants, payroll, or price | Apply finance doctrine and qualified review | Unreconciled or non-compliant financial proposal. |
| Rendering or submission tooling is unavailable | Hand off source plus a blocked compilation manifest | Claiming a deliverable exists when it was not generated or checked. |

## Worked Example

An RFP requires three signed reference forms and scores methodology at 40%. Two references are evidenced and one is missing. Mark the third form as a knockout risk with an owner and deadline; do not invent a client. Draft the method against the weighted criteria, reconcile staffing days to price, render the final files, and retain the compliance and compilation records.

## References

- [Full lifecycle workflow](references/full-lifecycle-workflow.md) - load for workspace phases, folder conventions, analysis structure, drafting, review, and compilation detail.
- [High-value proposal strategy](references/high-value-proposal-strategy.md) - load for win themes, evaluator logic, evidence, and commercial differentiation.

## Read Next

- External `proposal-skills` for procurement-specific response strategy and red-team review.
- `meta-accounting-finance-review` for financial proposal reconciliation.
- `ai-slop-audit` for the independent final content gate.
