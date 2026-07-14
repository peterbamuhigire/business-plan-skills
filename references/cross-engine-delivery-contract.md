# Cross-engine delivery contract

This contract governs handoffs from the business-plan engine. A named engine remains the source of truth for its domain; this repository records inputs, outputs, acceptance evidence, caveats, and receiver state without copying that engine's doctrine.

## Common handoff envelope

Every applicable handoff records:

| Field | Requirement |
|---|---|
| `engine` | Canonical engine or specialist capability receiving the work |
| `applicable` | `true` or `false`, with a reason when false |
| `input_versions` | Exact source artefacts or commit/version identifiers |
| `requested_decision` | The decision the receiving engine must answer |
| `state` | `pass`, `pass-with-caveats`, `fail`, `not-assessed`, or `not-applicable` |
| `evidence` | Existing paths or source records supporting the state |
| `caveats` | Unresolved limits, professional review, or current-source checks |
| `receiver` | Named role responsible for acceptance |

`fail` blocks release. `not-assessed` blocks release whenever the handoff is mandatory. `pass-with-caveats` is permitted only when the final audience and governing domain gate permit it; caveats remain visible.

## Domain handoffs

| Domain | Send | Receive | Acceptance condition | Mandatory when |
|---|---|---|---|---|
| Digital research engine | Decision brief, claim register, jurisdictions, dates, gaps | Source evaluation, verification trail, evidence pack, contradiction log, confidence | Load-bearing claims are claim-linked, current where volatile, and gaps are explicit | Any external factual claim controls a conclusion |
| Chwezi accounting doctrine | Model, assumptions, funding ask, reporting basis, money-flow scope | Doctrine gate, formula/reconciliation evidence, framework and professional-review state | No blocker; narrative-model-funding logic reconciles; current rates are verified or blocked | Money, inventory, payroll, grants, tax, banking, valuation, or statements appear |
| Spreadsheet capability | Workbook, required scenarios/checks, named inputs and outputs | Opened/validated workbook, formula map, error/link report, reconciliation and scenario evidence | No broken/missing/external links, cached formula errors, missing required scenario, or failed reconciliation | XLSX or spreadsheet model is delivered or relied upon |
| Design-system engine | Audience, brand constraints, content hierarchy, charts/tables, accessibility and print needs | Typeface and rationale, layout system, visual QA record, accessible and print-safe artefact | Visual system follows the canonical design doctrine and rendered pages/slides are inspected | Appearance, typography, deck, dashboard, DOCX, PDF, or XLSX presentation matters |
| Document/presentation capability | Approved content, style contract, output format, annex order | Written file, open/readback proof, render output, pagination/table/link QA | Native file exists, opens, renders, and matches approved content | DOCX, PDF, PPTX, or equivalent is promised |
| `skills-web-dev` security route | Data inventory, sharing route, recipients, hosting or SaaS scope | Confidentiality classification, redaction/access decision, security/privacy findings | Sensitive data is minimised and authorised; material technology risks have disposition | Personal/confidential data, data room, web app, SaaS, AI, portal, or external sharing is involved |

## Evidence rules

- A portal URL is a verification route, not proof of the copied claim.
- A source citation does not prove a workbook formula, and a formula audit does not prove the commercial assumption.
- A successful file write is not render evidence; retain a visual or renderer QA record.
- Automated validation is not professional certification or release authority.
- `not-applicable` requires a reason tied to scope. It must not hide unavailable tooling or review.

## Rejection and recovery

The receiver rejects a handoff when inputs are version-ambiguous, evidence paths are missing, the decision is unclear, or the requested conclusion exceeds the engine's authority. The sender corrects the envelope, invalidates dependent outputs where needed, and resubmits. Handoff history is append-only in the audit log.
