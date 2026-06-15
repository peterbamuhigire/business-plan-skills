# Repository Operating Guide

## Purpose

This repository is a dual-surface skills suite for generating bankable, investor-grade business plans, proposals, pitch materials, and execution frameworks.

The portable unit is the skill directory under `skills/`:

- `skills/<skill-name>/SKILL.md` is the canonical shared instruction surface for both Codex and Claude Code
- `skills/<skill-name>/references/` stores deeper frameworks, examples, checklists, and long-form material
- `AGENTS.md` stores repo-wide orchestration, routing, constraints, and verification expectations

## Current Layout

Skills live under `skills/` as skill directories such as:

- `skills/00-client-intake`
- `skills/01-executive-summary`
- `skills/10-financial-projections`
- `skills/meta-consulting-synthesis`
- `skills/meta-valuation`

Root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant. Leave `docs/`, `projects/`, `.git`, `tools/`, and other non-skill operational directories at root unless the directory itself is an actual skill with its own root `SKILL.md`.

## Canonical Authoring Standard

When creating or updating a skill:

- Keep reusable logic inside `SKILL.md`
- Keep deep material in `references/`
- Keep repo-wide routing and rules in this `AGENTS.md`
- Prefer provider-agnostic wording inside skills
- Avoid platform-specific UI assumptions inside `SKILL.md`

Use this shared structure inside skills whenever possible:

1. Overview
2. Use when
3. Do not use when
4. Required inputs
5. Workflow
6. Quality bar
7. Anti-patterns
8. Outputs
9. References

For the canonical template and migration rules, see:

- `skills/meta-utility/skill-writing/references/dual-compatible-skill-template.md`
- `skills/meta-utility/skill-writing/references/dual-surface-migration-rules.md`

## Default Baseline

For serious business-plan work, start from these skills:

- `00-client-intake`
- `country-context/{country}` where available, otherwise Uganda defaults
- `meta-critical-thinking-business-logic`
- `meta-consulting-synthesis`
- `meta-bankability-scoring`
- `meta-due-diligence`

When funding includes equity, convertibles, strategic investors, or blended finance, also load:

- `meta-valuation`

When execution systems matter, also load:

- `meta-monitoring-evaluation`
- `meta-quarterly-gameplan`

When the plan or strategy must explain how the business should digitise, modernise its model, or use technology intelligently beyond a narrow AI section, also load:

- `meta-digital-transformation`

When a plan includes a website, ecommerce site, content/SEO engine, portal, landing pages, web app, website-design service line, or website startup/recurring costs, also load:

- `meta-website-investment-planning`

When preparing decks or presentations, also load:

- `meta-pitch-preparation`
- `meta-presentation-design`

## Task Routing

- Full bankable plan: `00-client-intake` -> `meta-critical-thinking-business-logic` -> sections `02` to `16` -> `01-executive-summary` -> `meta-critical-thinking-business-logic` review -> `meta-consulting-synthesis` -> `meta-financial-stress-test` -> `meta-bankability-scoring` -> `meta-due-diligence` -> `15-appendices` -> `00-plan-assembly`
- Equity or investor plan: baseline plan flow + `meta-valuation`
- Grant application: `11b-grant-proposal` instead of standard funding-request workflow
- Proposal work: `proposal-architect` plus any relevant sector or funding skills
- Pitch or deck work: `meta-pitch-preparation` + `meta-presentation-design`
- Execution planning: `meta-monitoring-evaluation` + `meta-quarterly-gameplan`
- Digital-first or technology-modernisation strategy: baseline flow + `meta-digital-transformation` + `14-ai-integration` where AI is materially relevant
- Website, ecommerce, or website-design-service planning: relevant section flow + `meta-website-investment-planning` + `digital-marketing-strategy` + `meta-premium-go-to-market` when premium positioning applies
- EAC e-commerce BDS company diagnostics: use `skills/ict/ecommerce-business-model-diagnostic/` when assessing operating e-commerce, marketplace, D2C, B2B, social-commerce, or dropship companies for donor-funded needs assessments, cross-border readiness, and 90-day action planning
- Cross-border e-commerce unit economics: use `skills/ict/ecommerce-unit-economics-and-cross-border-margin-model/` before recommending target markets, discounts, paid acquisition, partner channels, or export marketing budgets that depend on margin, CAC, payment, fulfilment, returns, or landed-cost assumptions
- Pre-ship quality gate (every generated plan, section, deck, narrative, or proposal): run `anti-ai-slop` last, after `writing-quality` and `meta-critical-thinking-business-logic`
- Slop audit cadence: `ai-slop-audit` runs after each major iteration (each drafted section, completed deck, financial-narrative module, or significant revision), logging a verdict each time; a grade **F blocks progression** until the blocking findings are fixed. It also auto-runs on request ("audit / review / de-slop this for AI slop", "does this look AI-generated?") and returns a graded A/B/C/F report with a 0–100 genericness score

## Core Rules

- Do not call output bankable, investor-grade, or submission-ready unless assumptions, risks, evidence, and financing logic are explicit.
- Do not call output achievable, convincing, or commercially sound unless customer, market, revenue, cost, operating, implementation, and funding logic reconcile.
- For load-bearing claims, make claim, evidence, warrant, assumption, countercase, and implication visible in notes or prose.
- Do not duplicate repo-wide standards across many skills when a baseline skill, shared reference, or this file is the right home.
- Prefer updating an existing overlapping skill over creating a near-duplicate skill.
- Keep `SKILL.md` concise. Move frameworks, examples, and long teaching content into `references/`.
- Keep skills declarative, workflow-first, and tool-agnostic.
- Use British English spelling where natural for the repo.
- Any recommendation to digitise, automate, launch a platform, or buy major systems must show customer logic, operating logic, and investment logic - not trend language alone.
- Prefer SMART, context-fit, realistically staged digitisation over all-at-once transformation promises.
- No generated output ships until it passes the `anti-ai-slop` gate: a specificity floor, verify-before-emit on every stat/market size/citation, an authored strategy, the hard parts covered, and no banned-vocabulary filler. Never invent a TAM, growth rate, or benchmark to fill a section.

## Done Means

A high-stakes output is not complete unless:

- the governing thesis is clear
- assumptions are explicit
- load-bearing claims have evidence, warrants, countercases, and implications
- financials reconcile with the narrative
- the funding ask matches the implementation plan
- risks are decision-relevant
- appendices or evidence support the major claims
- the output matches the audience mode: bank, investor, DFI, grant, or strategic partner
- the digital strategy, if included, is commercially justified, operationally realistic, and integrated with the business model rather than bolted on

## Verification

Before treating significant skill changes as complete:

- validate new skills with `python skills/meta-utility/skill-writing/scripts/quick_validate.py skills/<category>/<skill-name>`
- update references when the workflow changes materially
- update evaluation docs if repository capability materially changes
- prefer spot verification of modified skills and routing dependencies

## Document and Spreadsheet Tooling

- Before promising `.docx`, `.pdf`, `.xlsx`, financial models, application registers, scoring matrices, budgets, dashboards, or board/investor packs, verify the machine has the required document and spreadsheet tooling.
- Prefer built-in document/spreadsheet plugins where available. Otherwise use local Python libraries such as `openpyxl`, `XlsxWriter`, `pandas`, `python-docx`, `docxtpl`, `docxcompose`, `pypandoc`, `markdown`, `PyMuPDF`, `pypdf`, `pdfplumber`, and `reportlab`.
- Check binaries such as `pandoc`, LibreOffice/`soffice`, `wkhtmltopdf`, and `tesseract` when conversion or OCR is needed.
- Run a minimal DOCX/XLSX smoke test on a new machine before production export.
- Never claim a Word, PDF, Excel, or model file was generated unless it was actually written and opened or validated.

## Migration Guidance

When modernising older skills:

- remove provider-specific command syntax from `SKILL.md`
- remove chat UI assumptions from `SKILL.md`
- move duplicated repo-wide rules into `AGENTS.md` or a shared reference
- add `Use when`, `Do not use when`, `Required inputs`, `Workflow`, `Quality bar`, `Anti-patterns`, and `Outputs` where missing

## Change Strategy

Use incremental migration, not a repo-wide rewrite:

1. Preserve working skills
2. Upgrade touched skills to the shared structure
3. Add shared references where repetition is high
4. Only reorganise physical directories when the migration cost is justified


## Finance & Accounting Trigger

For finance/accounting/IFRS/IAS work, use the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine` whenever the user's request, the artefact being generated, or the code being edited touches **any** of:

- Money flows: sales, purchases, payments, refunds, credit notes, expenses
- Stock and inventory
- Payroll
- Tax (VAT, PAYE, WHT, NSSF, income tax, customs, excise, EFRIS, eTIMS)
- Grants, donations, donor restrictions
- Banking, mobile money, POS, card settlement, cash drawer
- Fixed assets
- Financial reports, management accounts, statutory returns
- Chart of Accounts, journals, ledger, posting services, period state, audit trail
- Reconciliation, close, migration, opening balances
- Internal controls, audit, evidence packs
- Any IFRS or IFRS for SMEs section

When the trigger fires:

1. For finance/accounting/IFRS/IAS work, use the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.
2. Read the relevant doctrine reference file in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
3. Read the corresponding finance skill `SKILL.md` in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
4. Apply the **finance & accounting quality gate** from the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
6. Record the gate run in the artefact manifest.

The `finance-module-audit` skill (the corresponding skill in the finance engine, `C:\wamp64\www\chwezi-accounting-doctrine`) auto-runs whenever the user asks to analyse, review, audit, build, propose, or replace any software system with even a slight finance element.

