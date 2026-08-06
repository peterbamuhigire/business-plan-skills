# Repository Operating Guide

Shared agent, command, hook, evidence, and handoff contracts are mapped for
this engine in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md)
and governed centrally by `C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`.

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

The July 2026 contract is mandatory for every active skill. Require directory-matching identity; a one-line, neighbour-aware `Use when` description of at most 350 characters; portable metadata; positive and negative triggers; input, output, and evidence tables; an ordered workflow with stop and recovery behaviour; quality standards; five concrete anti-patterns with fixes; capability and permission boundaries; degraded mode; a domain decision table; and directly linked references. Audit and review skills default to read-only. Keep each `SKILL.md` at or below 500 lines.

For the canonical template and migration rules, see:

- `skills/meta-utility/skill-writing/references/dual-compatible-skill-template.md`
- `skills/meta-utility/skill-writing/references/dual-surface-migration-rules.md`

## Default Baseline

Kaizen is mandatory across the engine. Load `skills/meta-strategy/kaizen-improvement-system/SKILL.md` for engine or product audits and book-driven improvement. Publish audits with a hard maximum of 65/100; every remediation plan targets 95/100 and must name evidence, owners, experiments, and re-audit dates. Route current external claims to Digital Research Skills Engine and finance doctrine to Chwezi.

For serious full business-plan work, start with `business-plan-orchestrator`, which controls the stage register, cross-engine handoffs, blocker precedence and release bundle. It routes to these baseline skills:

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

Before a country or market fact is released, check `docs/source-registers/country-market-data.json`; an overdue entry or missing claim-level citation blocks the affected conclusion. Before sector assumptions enter operations, risk, implementation or finance, apply `references/sector-regulatory-gates.md`. Run `tools/workbook-audit/formula_map.py` on delivered XLSX models. Use `meta-investment-committee-red-team` only after a complete plan, model audit and evidence pack exist.

Before external release of a complete plan, apply `references/cross-engine-delivery-contract.md`, populate `templates/release-evidence-bundle.json`, and run `tools/release-gate/validate_release_bundle.py`. Missing mandatory research, finance, spreadsheet, design, document, security, render, reviewer or authority evidence remains blocking.

## Task Routing

- Full bankable plan: `business-plan-orchestrator` -> `00-client-intake` -> evidence design -> `meta-critical-thinking-business-logic` -> sections `02` to `16` -> `01-executive-summary` -> synthesis/model/challenge gates -> `15-appendices` -> `00-plan-assembly` -> cross-engine finalisation -> validated release bundle
- Equity or investor plan: baseline plan flow + `meta-valuation`
- Grant application: `11b-grant-proposal` instead of standard funding-request workflow
- Proposal work: `proposal-architect` plus any relevant sector or funding skills
- Pitch or deck work: `meta-pitch-preparation` + `meta-presentation-design`
- Execution planning: `meta-monitoring-evaluation` + `meta-quarterly-gameplan`
- Digital-first or technology-modernisation strategy: baseline flow + `meta-digital-transformation` + `14-ai-integration` where AI is materially relevant
- Website, ecommerce, or website-design-service planning: relevant section flow + `meta-website-investment-planning` + `digital-marketing-strategy` + `meta-premium-go-to-market` when premium positioning applies
- EAC e-commerce BDS company diagnostics: use `skills/ict/ecommerce-business-model-diagnostic/` when assessing operating e-commerce, marketplace, D2C, B2B, social-commerce, or dropship companies for donor-funded needs assessments, cross-border readiness, and 90-day action planning
- Cross-border e-commerce unit economics: use `skills/ict/ecommerce-unit-economics-and-cross-border-margin-model/` before recommending target markets, discounts, paid acquisition, partner channels, or export marketing budgets that depend on margin, CAC, payment, fulfilment, returns, or landed-cost assumptions
- Retail operating-model plans: use `skills/industry-guides/retail/guide.md` plus `skills/industry-guides/retail/references/retail-operating-model-and-engine-plan.md` when the plan includes retail, omnichannel commerce, POS-enabled stores, merchandising, pricing, promotions, markdowns, loyalty, fulfilment, returns, shrink, vendor terms, private label, planograms, or retail KPI/WBR cadence
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

- run `python -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json`
- run `python -X utf8 scripts/routing_smoke_test.py --threshold 1.0`
- validate each changed skill with `python -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <skill-directory>`
- on Peter's development machine, run the canonical scanner for both `skills/` and `country-context/` plus the canonical quick validator for every active skill directory
- keep `docs/quality/skill-quality-baseline.json` at zero debt; a baseline is never a waiver
- update references when the workflow changes materially
- update evaluation docs if repository capability materially changes
- prefer spot verification of modified skills and routing dependencies
- run the evidence-register, sector-gate, exemplar-pack, workbook and unit-test gates documented in `CONTRIBUTING.md` when those capabilities are touched

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
- add every contract named in the Canonical Authoring Standard; do not fill missing domain decisions, examples, evidence, or acceptance criteria with generic boilerplate

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


<!-- design-system-skills:trigger v1 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from your global engine-routing table** (`~/.claude/CLAUDE.md`,
or `AGENTS.md` for Codex) — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
(Inter, Geist, Roboto, Arial, Open Sans, Lato, Space Grotesk, bare system stacks) as primary
type — state the chosen typeface and reason before producing any artifact.
<!-- /design-system-skills:trigger -->
