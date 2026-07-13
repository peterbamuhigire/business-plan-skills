---
name: procurement-policy-and-manual
description: Use when authoring a procurement policy or procurement and disposal manual for an East African organisation; use proposal skills for bid responses, verify current PPDA or donor rules, and defer purchasing, payables, asset, inventory, and control doctrine to Chwezi Accounting Doctrine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Procurement Policy and Manual

A consulting-deliverable skill producing a standalone organisational procurement document. It owns the document's structure, the procurement-cycle workflow, the methods-and-thresholds framework, and the East African regulatory framing — and it pulls procurement-law substance and financial controls from existing skills rather than improvising.

## Use When

- A client needs a **Procurement Policy**, **Procurement & Disposal Manual**, **Procurement Procedures Manual**, **supplier/prequalification framework**, or a **contract-management policy**.
- Responding to an RFP/EOI for "development of a procurement policy / manual."
- Reviewing or updating procurement rules against the PPDA framework or donor requirements.

## Do Not Use When

- The document is a finance manual — use `advisory-deliverables/finance-policy-and-manual` (procurement is one chapter there; this skill is the full standalone manual).
- Writing a bid/tender response — use `proposal-skills` (`sectors/ppda-uganda`, `giz-eu-local-procurement-response`, `world-bank`, `afdb`, `undp`).
- A pure HR or IT policy with no procurement content.

## Required Inputs

Entity type and regime (PPDA-regulated public body / LG; NGO-CSO; SME; donor-funded project); legal form and registration; funding sources and any binding donor procurement rules (World Bank, USAID ADS, EU/GIZ, AfDB, UN); whether asset disposal is in scope; existing procurement rules; committee/board structure; spend profile and categories; jurisdiction (default Uganda); named approver. Never invent these — ask.

## Workflow

1. **Intake & regime selection.** Determine the governing regime: **(A) PPDA-regulated** (PPDA Act 2003 as amended + the PPDA Regulations 2023, which since 5 Feb 2024 cover both central and local government) — thresholds and methods are statutory; or **(B) non-PPDA** (NGO/SME/private) — thresholds are organisation-set, with donor rules layered on. Most entities are B with one or more donor overlays.
2. **Select the blueprint.** Load `references/document-blueprint.md` for the chapter map and the methods-and-thresholds framework.
3. **Pull substance — do not improvise.** For PPDA substance (methods, evaluation, forms, committees, complaints) read `proposal-skills/skills/profiles-sectors/sectors/ppda-uganda/SKILL.md` and its references. For commitment control, payment controls, three-way match, and segregation read the finance engine: `12-public-sector-and-ipsas/government-procurement-and-fiscal-controls` and `10-controls-governance-and-fraud/internal-controls-library`, plus `doctrine/references/uganda-public-sector-pfm.md` (public) or `uganda-ngo-financial-management-patterns.md` (NGO).
4. **Draft section by section** using the procurement cycle: planning → requisition → sourcing/solicitation → evaluation → award → contracting → delivery/inspection → payment → records. Set every threshold and committee composition as a **named client parameter**.
5. **Keep statutory thresholds OUT of the body.** PPDA monetary thresholds and method bands change by regulation — put them in a dated, verified **Threshold Schedule appendix** that cites the current PPDA Regulations; the body refers to "the applicable threshold per the Threshold Schedule."
6. **Wire procurement to finance.** No commitment without an approved requisition and uncommitted budget (commitment control); three-way match (PO/GRN/invoice) before payment; procurement records feed the audit trail.
7. **Add governance, ethics, disposal, complaints, and forms.** Contracts/Procurement Committee, Evaluation Committee, and (PPDA) the user/PDU split; conflict-of-interest and anti-corruption rules; asset disposal/board of survey; bidder complaints and appeals; the forms appendix; and a review/version-control page.
8. **Run the quality gates.** `meta-utility/anti-ai-slop` (live), `meta-strategy/meta-critical-thinking-business-logic`, and the finance engine's conformance scan where finance controls appear. Record each gate run.
9. **Produce the deliverable.** Client-ready DOCX/PDF plus an adoption checklist (board approval, effective date, training, supplier-database setup).

## Quality Bar

Every rule is specific and enforceable; every threshold is a named parameter with an owner and review date; segregation between requisition, approval, procurement, receipt, and payment holds even for small teams; statutory PPDA thresholds are never hardcoded in the body; donor rules are layered explicitly with "stricter rule wins"; procurement reconciles to the entity's budget and commitment control; and the document passes anti-ai-slop. British English throughout.

## Anti-Patterns

- Stating a PPDA monetary threshold or method band as current without the dated Threshold Schedule and a citation to the regulation.
- Letting the end user select the supplier and sign the contract (committee owns award; requester cannot approve or pay; procurer cannot keep inventory).
- Shipping a generic template full of `[placeholders]` instead of regime-specific, client-parameterised rules.
- Treating donor procurement rules and the entity policy as interchangeable — layer both.
- Omitting disposal, conflict-of-interest, and complaints sections.
- Asserting PPDA procedure without reading `proposal-skills/sectors/ppda-uganda`.

## Outputs

Procurement Policy; Procurement & Disposal Manual; procurement-cycle procedures; methods-and-thresholds framework + dated Threshold Schedule; committee charters and evaluation procedures; conflict-of-interest/anti-corruption rules; contract-management and disposal procedures; complaints/appeals procedure; forms pack; adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — chapter map, methods-and-thresholds framework, procurement cycle, committees, and forms list.
- `proposal-skills` (`C:\wamp64\www\proposal-skills`): `skills/profiles-sectors/sectors/ppda-uganda/` and its references; donor packs (`world-bank`, `afdb`, `undp`, `giz-eu-local-procurement-response`).
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `skills/12-public-sector-and-ipsas/government-procurement-and-fiscal-controls/`, `skills/10-controls-governance-and-fraud/internal-controls-library/`, and `doctrine/references/uganda-public-sector-pfm.md` / `uganda-ngo-financial-management-patterns.md`.
- `country-context/uganda/SKILL.md`; `language/east-african-english`.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Existing procurement rules, plans, thresholds, forms, findings, and contracts | Client and donor records | Required | Return a gap and evidence request; do not invent thresholds |
| Entity type, funding sources, jurisdiction, delegations, categories, and systems | Client governance records and verified authorities | Required | Keep methods and approvals parameterised |
| Purchasing, payables, asset, inventory, and control doctrine | Chwezi Accounting Doctrine | Required for money-touching chapters | Stop affected chapters pending doctrine and professional review |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Procurement Policy and Procurement and Disposal Manual | Board, management, procurement, users, finance, stores, auditors, and funders | Planning, methods, competition, evaluation, award, contracting, receipt, disposal, records, and complaints are executable |
| Threshold, method, committee, and evidence schedules | Procurement owner and assurance reviewers | Each parameter has authority, effective date, owner, exception route, and required record |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Requirement-to-process traceability | Legal or donor clause-to-step-to-record matrix | Binding procurement obligations map to procedures and evidence |
| Finance integration gate | Doctrine mapping and professional-review status | Commitments, payables, receipt, assets, inventory, taxes, and controls align with current Chwezi doctrine |

## Capability Contract

Review defaults to read-only. Edit only the authorised manual. Do not run a procurement, contact bidders, alter evaluations, approve awards, sign contracts, dispose of assets, spend funds, or certify compliance without explicit delegated authority and independent legal or professional review.

## Degraded Mode

If current law, donor rules, delegation, procurement evidence, or finance doctrine is unavailable, return a provisional method framework, controlled parameter schedule, and evidence request. Mark legal and compliance conclusions `not assessed`; never treat missing rules as discretion.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Public or donor rule is stricter than internal policy | Apply the stricter binding route | Ineligible or unlawful procurement |
| Requirement can be openly specified and competed | Use the authorised competitive method | Unjustified single sourcing |
| Emergency is genuine and documented | Use the lawful emergency route with retrospective review | Abuse of urgency |
| Step affects commitments, payables, tax, receipt, assets, or inventory | Apply Chwezi doctrine and professional review | Broken financial records or custody |

## Workflow

1. Confirm entity, funding, jurisdictions, categories, systems, users, and approval route.
2. Inventory plans, thresholds, delegations, methods, committees, contracts, disputes, forms, and findings.
3. Build the source hierarchy and parameter schedule; stop where a binding threshold lacks current authority.
4. Map planning through disposal, including segregation, conflicts, evaluation, complaints, receipt, and records.
5. Draft each method with trigger, approvals, competition, evaluation, evidence, exception, and contract route.
6. Reconcile money-touching procedures with current Chwezi doctrine and qualified professional review.
7. Test a routine purchase, consultant selection, emergency, disposal, conflict, and complaint; recover by revising any ambiguous handoff.
8. Release with approval status, controlled schedules, unresolved legal questions, and review dates visible.

## Quality Standards

The manual must support fair competition, value, accountability, documented exceptions, and complete custody and finance handoffs. Current legal, donor, and accounting rules must be sourced and professionally reviewed.

## Anti-Patterns

- Hard-coding thresholds without a source date. Fix: use a controlled schedule with authority and review owner.
- Splitting purchases to avoid competition. Fix: aggregate foreseeable need and monitor related requisitions.
- Treating three quotations as universal compliance. Fix: select the method required by value, category, donor, and law.
- Letting a conflicted evaluator remain silent. Fix: require disclosure, recusal, quorum review, and recordkeeping.
- Ending the process at contract signature. Fix: include receipt, inspection, invoice match, asset or inventory record, performance, and close-out.
- Calling the manual PPDA-compliant without current legal review. Fix: state scope, verification date, and professional sign-off status.

## Worked Example

When urgent flood repairs are required, document the emergency basis, verify the authorised emergency method and delegation, preserve competition where practicable, record receipt and asset consequences, and schedule independent retrospective review.
<!-- dual-compat-end -->
