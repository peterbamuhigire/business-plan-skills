---
name: governance-and-board-charter
description: Author a client-ready Governance Framework with Board & Committee Charters and a Delegation-of-Authority matrix for NGOs/CSOs, companies, SACCOs, donor-funded projects, and public/local-government bodies in Uganda/East Africa. Owns document architecture, the consulting workflow, parameterisation, and East African context; defers all finance-control and oversight substance to the Chwezi finance engine. Grounded in real Ugandan NGO governance manuals (General Assembly → Board → Secretariat) and the LG (Financial & Accounting) Regulations 2007 accounting-officer / surcharge framework.
---

# Governance and Board Charter

A consulting-deliverable skill: it produces a standalone Governance Framework, a set of Board and committee charters, and a Delegation-of-Authority matrix — not a business-plan section. It owns the document's structure, the consulting workflow, the parameter-setting, and the East African governance framing — and it pulls every control, fiduciary, and oversight treatment from the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.

## Use When

- A client needs a **Governance Framework / Manual**, **Board Charter**, **committee charters** (Finance, Audit, Procurement/Contracts, Budget, Accounts, Risk), a **Delegation-of-Authority matrix**, a **conflict-of-interest / code-of-conduct policy**, or a **whistleblowing policy**.
- Responding to an RFP/EOI for "development of a governance framework / board charter / delegation of authority."
- Reviewing, gap-auditing, or updating an existing governance instrument against current practice and the statutory framework.

## Do Not Use When

- Writing a business-plan governance or management section — use `pipeline` and `meta-strategy/meta-living-plan-governance`.
- Authoring the finance or procurement manual — governance is a chapter there; use `advisory-deliverables/finance-policy-and-manual` or `procurement-policy-and-manual` (this skill is the full standalone charter set).
- Answering a single fiduciary-control question — go straight to the relevant finance-engine `SKILL.md`.

## Required Inputs

Entity type and governance model (NGO/CSO with members or trustees; company limited by guarantee/shares with a board of directors; SACCO/cooperative; donor-funded project; public/local-government body with an accounting officer); legal form and registration (URSB / NGO Bureau / cooperative registrar); the governance tiers in place (General Assembly/Members, Board/Trustees, Secretariat/Management); existing committees and their mandates; any binding donor governance conditions; the entity's authorisation/approval matrix from its finance manual (for alignment); meeting cadence and quorum practice; jurisdiction (default Uganda); named approver/owner. Never fabricate these — ask.

## Workflow

1. **Intake & model selection.** Fix the governance model: **(A) not-for-profit** (members/trustees board, General Assembly as supreme organ), **(B) company** (board of directors accountable to shareholders/members), or **(C) public body** (accounting-officer model under the LG Financial & Accounting Regulations 2007, council/executive committee, LG Public Accounts Committee). Most NGOs are A with a donor overlay; local governments and public entities are C.
2. **Select the blueprint.** Load `references/document-blueprint.md` for the document set, the charter contents, and the chapter→source map.
3. **Pull oversight substance from the doctrine — do not improvise.** For each charter and policy, read the mapped finance-engine `SKILL.md` plus `doctrine/references/uganda-ngo-financial-management-patterns.md` (NGO bodies: Finance/Procurement/Accounts committees) or `uganda-public-sector-pfm.md` (accounting officer, surcharge, internal audit to council). The blueprint carries the chapter→skill map.
4. **Draft the framework, then each charter.** Author the Governance Framework (principles, structure, tiers) first; expand each tier into a charter (Board, then committees). Give every charter the standard contents: purpose, composition, quorum, term, duties, reporting line, meeting cadence.
5. **Align Delegation of Authority to the finance manual.** Build the DoA matrix with authority limits keyed to amount (operational → management → board), mirroring the entity's authorisation matrix from `internal-controls-library`. Where no finance manual exists, propose defaults flagged "to be board-approved" — never copied verbatim.
6. **Set governance figures as named parameters.** Authority limits, quorum, term length, auditor tenure (commonly ~3 years), meeting cadence, and signatory thresholds are **named client parameters** (default-to-be-approved) with an owner and review date — never hardcoded facts.
7. **Keep statutory items in a dated schedule.** Statutory governance duties and powers (e.g. accounting-officer responsibilities, surcharge/pecuniary-liability powers under the LG Regulations 2007, Whistleblowers Protection Act 2010 obligations) go into a dated, verified **Statutory Schedule appendix** that cites the source — so the framework does not go stale.
8. **Add conduct, integrity, and meeting governance.** Conflict-of-interest register and declarations; code-of-conduct attestation; whistleblowing per the Whistleblowers Protection Act 2010; meeting cadence, quorum, minutes, and decision logs.
9. **Run the quality gates.** `meta-utility/anti-ai-slop` (live), `meta-strategy/meta-critical-thinking-business-logic`, and the finance engine's conformance scan where finance controls appear. Record each gate run in the artefact manifest.
10. **Produce the deliverable.** Client-ready DOCX/PDF (use the document engines), plus an adoption checklist: board/General Assembly resolution, effective date, declaration sign-off, and induction plan.

## Quality Bar

Every governance rule is specific and enforceable (no "the board shall provide oversight" with nothing behind it); every figure — authority limit, quorum, term, cadence — is a named parameter with an owner and a review date; the DoA matrix reconciles to the entity's actual authorisation matrix and chart of accounts; the model is not mixed (members/trustees board vs company board vs accounting-officer public body); statutory powers are never invented or hardcoded in the body; conflict-of-interest, code-of-conduct, and whistleblowing are always present; and it passes anti-ai-slop and the doctrine conformance scan. British English throughout.

## Anti-Patterns

- Copying one organisation's authority limits, quorum, or committee mandates verbatim into another.
- Embedding statutory duties or surcharge powers in the body instead of the dated Statutory Schedule with a citation.
- Shipping a generic charter full of `[bracketed placeholders]` instead of a client-parameterised framework.
- Asserting an accounting-officer duty or committee mandate without reading the mapped finance-engine reference.
- Mixing governance models — giving a not-for-profit a shareholder board, or a public body a trustee structure.
- A Delegation-of-Authority matrix that contradicts the entity's finance-manual authorisation tiers.
- Dropping conflict-of-interest, code-of-conduct, or whistleblowing because the entity is "small" or "trusted".

## Outputs

Governance Framework; Board Charter; per-committee charters (Finance, Audit, Procurement/Contracts, Budget, Accounts, and optionally Risk); Delegation-of-Authority matrix; conflict-of-interest register and declaration forms; code-of-conduct attestation; whistleblowing policy; meeting-governance rules (cadence, quorum, minutes, decision log); dated Statutory Schedule appendix; adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — document set, per-charter standard contents, Delegation-of-Authority matrix, parameterisation rule, NGO-vs-public-body switch, and chapter→source map.
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `skills/10-controls-governance-and-fraud/internal-controls-library/`, `engagement-quality-and-plain-language-output/`, `whistleblowing-and-finance-ethics/`; `skills/06-close-consolidation-and-reporting/audit-ready-reporting-pack/`, `audit-pbc-and-evidence-management/`; `doctrine/references/uganda-public-sector-pfm.md`, `uganda-ngo-financial-management-patterns.md`.
- `business-plan-skills`: `skills/meta-strategy/meta-living-plan-governance/`; `meta-reporting` (board & investor reporting).
- `country-context/uganda/SKILL.md` for institutions/regulatory bodies; `language/east-african-english` for style.
