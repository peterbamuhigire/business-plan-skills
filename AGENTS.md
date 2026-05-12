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

- `skills/skill-writing/references/dual-compatible-skill-template.md`
- `skills/skill-writing/references/dual-surface-migration-rules.md`

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

- validate new skills with `python skills/skill-writing/scripts/quick_validate.py skills/<skill-name>`
- update references when the workflow changes materially
- update evaluation docs if repository capability materially changes
- prefer spot verification of modified skills and routing dependencies

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

Load `doctrine/accounting-finance-doctrine.md` whenever the user's request, the artefact being generated, or the code being edited touches **any** of:

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

1. Read `doctrine/accounting-finance-doctrine.md`.
2. Read the relevant doctrine reference file under `doctrine/references/`.
3. Read the relevant skill `SKILL.md` under `skills/finance/`.
4. Apply the **finance & accounting quality gate** from `doctrine/governance/finance-accounting-quality-gate.md`.
5. Record the gate run in the artefact manifest.

The `finance-module-audit` skill (at `skills/finance/finance-module-audit/`) auto-runs whenever the user asks to analyse, review, audit, build, propose, or replace any software system with even a slight finance element.

