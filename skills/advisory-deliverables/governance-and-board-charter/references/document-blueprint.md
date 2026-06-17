# Governance Framework & Board Charter — Document Blueprint

The reusable architecture for a standalone governance deliverable, synthesised from real Ugandan NGO governance manuals (General Assembly → Board of Directors/Trustees → Secretariat/Management) and the LG (Financial & Accounting) Regulations 2007 accounting-officer / surcharge framework. Use the chapter→source map so oversight substance always comes from the finance engine, never improvised.

Finance-engine root: `C:\wamp64\www\chwezi-accounting-doctrine` (paths below are relative to it).

## The document set, one source

A governance engagement produces a linked set, not a single file:

- **Governance Framework** — the apex document: principles, governance tiers, structure, and how the bodies relate. 15–30 pages.
- **Board Charter** — the constitution of the top governing body (Board of Directors / Trustees / Council).
- **Committee charters** — one per standing committee (Finance, Audit, Procurement/Contracts, Budget, Accounts, and optionally Risk).
- **Delegation-of-Authority (DoA) matrix** — authority limits keyed to amount, mirroring the finance-manual authorisation matrix.
- **Conduct & integrity policies** — conflict-of-interest register and declarations, code-of-conduct attestation, whistleblowing policy.

The Framework is the apex; the charters operationalise it; the DoA matrix makes authority concrete. Draft the Framework first, then expand each tier into its charter.

## Governance tiers (the standard structure)

The tier most Ugandan manuals use:

**General Assembly / Members** (supreme organ; elects the board, receives audited accounts) → **Board of Directors / Trustees / Council** (top authority between assemblies) → **Secretariat / Management** (day-to-day execution under the Chief Executive / Accounting Officer).

The Board is the top authority: it approves the budget, the audited accounts, the manual(s), the appointment of the external auditor (tenure commonly ~3 years, a parameter), and changes to the bank-signatory mandate.

## Standard charter contents (every charter follows this shape)

| Element | What it states |
|---|---|
| Purpose / mandate | Why the body exists; its scope of authority |
| Composition | Number of members, chair, ex-officio, member/management mix; independence requirements |
| Quorum | Minimum present to transact (a parameter) |
| Term | Length of appointment, rotation, term limits, vacancy rules (a parameter) |
| Duties | The specific, enumerated responsibilities — pulled from the mapped finance-engine skill |
| Reporting line | To whom the body reports (Board → General Assembly; committees → Board; Accounts Committee → General Assembly) |
| Meeting cadence | How often it meets (a parameter); notice, agenda, minutes, decision log |

## Charter map (and where the substance comes from)

| Body | Mandate focus | Substance from finance-engine skill / reference |
|---|---|---|
| **Board of Directors / Trustees / Council** | Approves budget, audited accounts, manuals, auditor appointment, bank-signatory changes; sets strategy and risk appetite | `10-controls-governance-and-fraud/internal-controls-library`; `engagement-quality-and-plain-language-output`; `meta-strategy/meta-living-plan-governance` (business-plan-skills); `meta-reporting` board & investor reporting |
| **Finance Committee** | Legal / strategic / fiduciary / oversight roles over finances; reviews budget and management accounts | `internal-controls-library` (authorisation/segregation); `uganda-ngo-financial-management-patterns.md` |
| **Audit Committee** | Internal & external audit interface, auditor tenure, follow-up on findings | `06-close-consolidation-and-reporting/audit-ready-reporting-pack`, `audit-pbc-and-evidence-management` |
| **Procurement / Contracts Committee** | Award oversight, thresholds, contract approval | `internal-controls-library`; cross-reference `advisory-deliverables/procurement-policy-and-manual` |
| **Budget Committee** | Budget preparation, virement rules, monitoring | `internal-controls-library`; `uganda-ngo-financial-management-patterns.md` |
| **Accounts Committee** | Scrutinises audited accounts; reports to the General Assembly | `audit-ready-reporting-pack`; `uganda-ngo-financial-management-patterns.md` |
| **Risk Committee** (optional) | Enterprise risk register, risk appetite, mitigation oversight | `internal-controls-library`; `forensic-accounting-and-anti-fraud` |
| **Conduct & integrity** | Conflict-of-interest register, code of conduct, whistleblowing (Whistleblowers Protection Act 2010) | `10-controls-governance-and-fraud/whistleblowing-and-finance-ethics` |

For governance principles and structure overall, anchor on `meta-strategy/meta-living-plan-governance` (business-plan-skills) and `engagement-quality-and-plain-language-output` (finance engine).

## Delegation-of-Authority (DoA) matrix

The DoA matrix makes authority concrete by keying decisions to amount, mirroring the authorisation matrix in the finance manual (operational → management → board). Render it as a table; the figures are client/board-set parameters.

| Decision / transaction type | Operational (officer) | Management (CEO / Accounting Officer) | Board / Committee |
|---|---|---|---|
| Expenditure / payment up to | UGX [____] | above operational up to UGX [____] | above management threshold |
| Procurement award up to | UGX [____] | UGX [____] | above management threshold (Contracts Committee) |
| Budget virement | not delegated | within line up to [____] | between votes / above [____] |
| Bank-signatory mandate change | — | recommend | approve |
| Auditor appointment / removal | — | recommend | approve (tenure ~[3] years) |
| Asset disposal / write-off above | — | up to UGX [____] | above UGX [____] |
| Engaging staff / contracts of service | — | up to grade/value [____] | senior appointments |

The matrix must reconcile to the entity's finance-manual authorisation tiers; where they differ, the stricter applies and the discrepancy is flagged for board resolution.

## NGO-vs-public-body switch

Distinguish three governance models — never mix them:

- **Not-for-profit board (members / trustees).** General Assembly / Members is the supreme organ; the Board of Directors or Board of Trustees holds top authority between assemblies; the Accounts Committee reports audited accounts to the General Assembly. Fiduciary, not proprietary — no shareholders.
- **Company board.** A board of directors accountable to shareholders or (for a company limited by guarantee) members; governed by the company's articles and the Companies Act; directors owe statutory duties to the company.
- **Public-body / accounting-officer model.** Under the LG (Financial & Accounting) Regulations 2007: the **Accounting Officer** (Chief Executive / Chief Administrative Officer) is personally accountable; an **Executive Committee** runs the council; the **Local Government Public Accounts Committee** scrutinises; **surcharge / pecuniary-liability powers** apply to officers for loss; **internal audit reports direct to council**. Layer this from `uganda-public-sector-pfm.md`.

Select the model at intake; the Framework, charters, and DoA matrix all follow from it.

## Parameterisation rule

Everything the entity must choose is a **parameter with an owner and a review date**, presented as a default-to-be-approved, not a hardcoded fact:

> "Board quorum: **[____]** members (recommended default: half the members plus one) — set by the General Assembly, reviewed every [____]." 
> "External auditor tenure: **[____] years** (recommended default: 3 years, then rotation) — Board-approved, reviewed at reappointment."

Statutory items are NOT parameters — accounting-officer duties, surcharge/pecuniary-liability powers under the LG Regulations 2007, and Whistleblowers Protection Act 2010 obligations live in the dated **Statutory Schedule** appendix and are verified against the source at issue (see `uganda-compliance-caveats.md`). The body references "the statutory duty per the Statutory Schedule", never a paraphrase that can drift.

## Chapter → source map (summary)

- Governance principles & structure → `meta-strategy/meta-living-plan-governance` (business-plan-skills); `10-controls-governance-and-fraud/engagement-quality-and-plain-language-output` (finance engine).
- Board charter, committee charters, delegation of authority → `10-controls-governance-and-fraud/internal-controls-library` (authorisation/segregation); `meta-reporting` board & investor reporting (business-plan-skills).
- Conflict of interest, code of conduct, whistleblowing → `10-controls-governance-and-fraud/whistleblowing-and-finance-ethics`.
- Audit committee & external/internal audit interface → `06-close-consolidation-and-reporting/audit-ready-reporting-pack`, `audit-pbc-and-evidence-management`.
- Public-sector governance roles & surcharge → `doctrine/references/uganda-public-sector-pfm.md`.
- NGO governance bodies (Finance / Procurement / Accounts Committees) → `doctrine/references/uganda-ngo-financial-management-patterns.md`.
- Country context and style → `country-context/uganda` and `language/east-african-english`.
