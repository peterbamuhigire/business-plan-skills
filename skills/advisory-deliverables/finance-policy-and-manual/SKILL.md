---
name: finance-policy-and-manual
description: Author a client-ready Financial Management Policy and Finance & Accounting Manual (and related controls/governance documents) for NGOs, SMEs, SACCOs, projects, and public-bodies. Owns document architecture, consulting process, and East African context; defers all accounting substance to the Chwezi finance engine. Methodology grounded in real Ugandan finance manuals (UCOBAC, MCLD, IMAU) and the LG Regulations 2007 / MOFPED 2024 framework.
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
