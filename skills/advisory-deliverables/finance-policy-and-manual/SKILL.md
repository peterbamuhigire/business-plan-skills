---
name: finance-policy-and-manual
description: Use when authoring a Financial Management Policy or Finance and Accounting Manual for an East African organisation; use `internal-controls-and-risk-framework` for an enterprise control framework, and defer accounting, tax, treasury, and reporting doctrine to Chwezi Accounting Doctrine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Finance Policy and Manual

A consulting-deliverable skill: it produces a standalone organisational document, not a business-plan section. It owns the document's structure, the consulting workflow, the parameter-setting, and the East African regulatory framing — and it pulls every accounting treatment, control, and statutory touchpoint from the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.

## Use When

- A client needs a **Financial Management Policy**, **Finance & Accounting Manual**, **Accounting Policies & Procedures Manual**, **internal-controls / segregation-of-duties framework**, **grants / fund-management manual**, or a finance-adjacent **procurement policy**.
- Responding to an RFP/EOI for "development of a financial management policy / accounting manual."
- Reviewing, gap-auditing, or updating an existing manual against current practice and standards.

## Do Not Use When

- Writing a business-plan financial section — use `pipeline/10-financial-projections`.
- Answering a single accounting-treatment question — go straight to the relevant finance-engine `SKILL.md`.
- Producing a pure HR, IT, or legal manual with no finance content.

## Required Inputs

Entity type (NGO/CSO, SME, SACCO/cooperative, donor-funded project, public/LG-adjacent body); legal form, registration (URSB/NGO Bureau), and funding model (donor-restricted, own revenue, mixed); reporting framework (IFRS, IFRS for SMEs, or modified-accrual public-sector); any existing manual/policies; board and committee structure; accounting software and chart of accounts in use; jurisdiction (default Uganda); named approver/owner. Never fabricate these — ask.

## Workflow

1. **Intake & scope.** Fix entity type, the document(s) wanted, jurisdiction, framework, and software. If a manual exists, run a gap audit against the blueprint before drafting.
2. **Select the blueprint and basis.** Load `references/document-blueprint.md`. Default framework is IFRS for SMEs (ICPAU). For a public/LG body, switch the basis and framing to `doctrine/references/uganda-public-sector-pfm.md`.
3. **Pull accounting substance from the doctrine — do not improvise.** For each manual chapter, read the mapped finance-engine `SKILL.md` plus `doctrine/references/uganda-ngo-financial-management-patterns.md` (NGO) or `uganda-public-sector-pfm.md` (public). The blueprint carries the chapter→skill map.
4. **Draft section by section.** Set every threshold, float, approval tier, and signatory rule as a **named client parameter**. Propose defaults from the Uganda NGO patterns (clearly flagged "to be board-approved"), never copied verbatim from another entity.
5. **Keep statutory rates OUT of the body.** PAYE/NSSF/VAT/WHT/income-tax rates go into a dated, verified **Statutory Schedule appendix** that points to the live source register — so the manual does not go stale.
6. **Build the control set.** Segregation-of-duties matrix, authorisation/approval matrix, bank-signatory mandate, reconciliation & close calendar, and procurement thresholds — from `internal-controls-library` plus the NGO/public patterns.
7. **Add governance, forms, and version control.** Finance/Procurement/Audit committee roles; the standard forms/templates appendix; and a review-and-amendment page with effective date and approver.
8. **Run the quality gates.** `meta-utility/anti-ai-slop` (live), `meta-strategy/meta-critical-thinking-business-logic`, and the finance engine's `finance-doctrine-conformance-scanner` / `finance-module-audit`. Record each gate run in the artefact manifest.
9. **Produce the deliverable.** Client-ready DOCX/PDF (use the document engines), plus an adoption checklist: board resolution, effective date, and staff training plan.

## Quality Bar

Every policy statement is specific and enforceable (no "adequate controls"); every number is a named parameter with an owner and a review date; segregation of duties holds even for a three-person team; statutory rates are never hardcoded in the body; the manual reconciles to the entity's actual chart of accounts and software; bases are not mixed (NGO accrual vs public modified-accrual); and it passes anti-ai-slop and the doctrine conformance scan. British English throughout.

## Anti-Patterns

- Copying one organisation's thresholds, floats, or depreciation rates verbatim into another.
- Embedding tax/payroll rates in the manual body instead of the live-verified Statutory Schedule.
- Shipping a generic template full of `[bracketed placeholders]` instead of client-parameterised policy.
- Asserting an IFRS/IPSAS treatment without reading the mapped finance-engine skill.
- Dropping the SoD matrix because the entity is "too small".
- Treating a donor's financial rules and the entity's manual as interchangeable — layer both, stricter wins.

## Outputs

Financial Management Policy; Finance & Accounting Manual; SoD and authorisation matrices; reconciliation/close calendar; forms-and-templates pack; dated Statutory Schedule appendix; adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — chapter map, chapter→doctrine-skill mapping, control set, and standard forms list.
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `doctrine/references/uganda-ngo-financial-management-patterns.md`, `doctrine/references/uganda-public-sector-pfm.md`, `doctrine/references/uganda-compliance-caveats.md`, and the skills named in the blueprint map.
- `country-context/uganda/SKILL.md` for institutions/regulatory bodies; `language/east-african-english` for style.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Existing policies, chart of accounts, workflows, forms, and audit findings | Client records and interviews | Required | Stop at a gap-led outline; do not invent current practice |
| Entity type, funding terms, approval limits, systems, and jurisdictions | Client governance documents and contracts | Required | Record open parameters and omit false thresholds |
| Current accounting, tax, treasury, and reporting rules | Chwezi Accounting Doctrine and verified authorities | Required for substantive chapters | Mark the chapter draft-only until doctrine and current-source review is complete |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Financial Management Policy and Finance and Accounting Manual | Board, management, finance staff, auditors, and funders | Roles, approvals, processes, records, exceptions, forms, and review ownership are explicit and mutually consistent |
| Parameter and evidence register | Document owner and reviewer | Every threshold and legal or accounting claim has an owner, source, effective date, and verification status |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Doctrine mapping and professional-review record | Chapter-to-source matrix plus sign-off status | All money-touching chapters map to current Chwezi doctrine and unresolved professional review is visible |
| Control traceability | Control-to-risk-to-evidence table | Each key finance risk has an owner, preventive or detective control, retained evidence, and escalation route |

## Capability Contract

Read and search access to client records and doctrine are required. Drafting may edit only the authorised deliverable. Do not approve policy, set production permissions, post transactions, certify compliance, or replace accountant, auditor, tax, treasury, or legal review without explicit authority.

## Degraded Mode

Fallback:

If client evidence, current sources, doctrine, or professional review is unavailable, return the narrowest useful outline, parameter register, and evidence request. Label affected chapters `not assessed`; never convert an unverified control or accounting conclusion into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Existing policy is evidenced and internally consistent | Retain it and document only the needed amendment | Disrupting a working control environment |
| Current practice conflicts with doctrine, law, or funding terms | Escalate the conflict and draft the compliant target state | Encoding an unlawful or misstated process |
| A threshold lacks delegated authority or source evidence | Leave it as an owned parameter, not a fabricated value | False approval authority |
| A chapter changes recognition, tax, treasury, payroll, inventory, close, or reporting | Require Chwezi doctrine and qualified professional review | Accounting misstatement or compliance failure |

## Workflow

1. Confirm audience, entity type, jurisdictions, mandate, systems, and document authority.
2. Inventory existing policies, workflows, forms, approval limits, audit findings, and funding restrictions.
3. Map every money-touching chapter to the current Chwezi doctrine skill and authoritative source; stop if a load-bearing rule cannot be verified.
4. Agree the policy architecture and parameter register before drafting detailed procedures.
5. Draft roles, controls, process steps, records, exceptions, escalation, and forms together so each procedure is operable.
6. Reconcile delegation limits, chart-of-accounts references, reporting duties, and document retention across chapters.
7. Run finance quality, legal/current-source, traceability, and anti-slop gates; recover from a failed gate by returning to the affected chapter and evidence request.
8. Release only with unresolved assumptions, professional-review items, and approval status visible.

## Quality Standards

The manual must be organisation-specific, executable by named roles, consistent with verified current requirements, and traceable to retained evidence. No accounting treatment is final without the applicable Chwezi doctrine gate and qualified professional review.

## Anti-Patterns

- Copying a donor or NGO manual unchanged. Fix: map each clause to this entity's authority, workflow, system, and evidence.
- Inventing approval thresholds to fill a table. Fix: use an owned parameter register pending formal delegation.
- Describing a control without its evidence. Fix: name the record, custodian, retention rule, and review cadence.
- Treating an accounting policy as administrative prose. Fix: route recognition, measurement, posting, close, and reporting to Chwezi doctrine.
- Freezing tax or statutory values into evergreen text. Fix: put dated values in a controlled schedule and verify before issue.
- Calling the draft compliant or approved. Fix: state review and approval status and retain professional sign-off.

## Worked Example

An NGO has a donor rule requiring two approvals but no board-approved monetary limits. Preserve the two-person control, place the amounts in the parameter register, ask the board to approve the delegation schedule, and keep the payments chapter draft-only until the finance doctrine and professional review gates pass.
<!-- dual-compat-end -->
