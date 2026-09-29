# Repository Operating Guide

## Codex-only model setup and Kaizen review

Apply this section only when the active runner is Codex. Claude and other
runners must skip it and retain their own models and full engine capabilities.

Before substantive Codex work, resolve this engine's directory and an available
Python 3.11+ interpreter (use its absolute path if absent from PATH), then run
`python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`.
If it reports configuration drift, Peter authorises the bounded
`--runtime codex --apply` repair, followed by `--check`. The helper backs up
changes and preserves unrelated settings. If Python or configuration access is
unavailable, report the limitation; do not replace the user's config wholesale.
Read `.codex/model-policy.md` for the full contract. Use Luna (`gpt-6-luna`) with high reasoning by
default for orchestration, research, audit, review, and implementation. Use Astra (`gpt-6-astra`) only when
Peter explicitly selects it for the task; never select or fall back to GPT-5.6. Report unavailable required GPT-6
models. A running session may need restarting for root settings to apply.

Every Kaizen cycle MUST check latest official model releases and actual
runtime availability, record dated evidence and a retain/change decision,
and evaluate better candidates before recommending replacement. Preserve the
pins until Peter authorises a verified change. Missing model-currentness
evidence is `NOT_ASSESSED`. This Codex adapter must not change CLAUDE.md,
Claude configuration, domain doctrine, permission settings or skill access.

## Universal agent integration

See `.skills-engine/engine-manifest.yaml` for the declarative contract used by the optional universal coordination package. The router and domain SKILL.md files remain authoritative.

The package may read the router, discover skills, inspect Git, and run only declared checks. Missing evidence is NOT ASSESSED; writes, pulls, publication, submissions, ledger/filing changes, deployment, or control changes require explicit approval.

## Rules

Always-on cross-cutting principles live in `rules/` — see `rules/README.md`.
Load `rules/common/core.md` alongside the routed skill for any non-trivial task;
it is short and does not replace the skill, only sets the baseline the skill
operates within.

## Mandatory Digital Research currentness gate for Kaizen

Every Kaizen audit, skill edit, reference update, validator change, and
standardisation decision MUST begin with the Digital Research Engine. Resolve its
location on this device from the global engine-routing table (`~/.claude/CLAUDE.md`,
or `AGENTS.md` for Codex); never assume a path. Read its `source-evaluation` and
`source-verification` skills and its currentness gate reference
`docs/continuous-improvement/kaizen-currentness-gate.md` (a path inside that engine,
not inside this repository).

Before admitting any standard, policy, law, technology, platform capability,
software version, command, security control, benchmark, or lifecycle claim,
record source scope, publication/version date, access date, freshness class,
review date, support status, and uncertainty. Use current authoritative
primary sources; quarantine stale/ambiguous/unsupported claims and mark them
`NOT_ASSESSED`. Books are durable concept inputs only.

Shared agent, command, hook, evidence, and handoff contracts are mapped for
this engine in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md)
and governed centrally by `docs/engine-control-plane.md` in the engineering-catalog engine (resolve it through the global engine-routing table).

## Purpose

This repository is a dual-surface skills suite for generating bankable, investor-grade business plans, proposals, pitch materials, and execution frameworks.

The portable unit is the skill directory under `skills/`:

- `skills/<skill-name>/SKILL.md` is the canonical shared instruction surface for both Codex and Claude Code
- `skills/<skill-name>/references/` stores deeper frameworks, examples, checklists, and long-form material
- `AGENTS.md` stores repo-wide orchestration, routing, constraints, and verification expectations

## Current Layout

Skills live under `skills/` as skill directories such as:

- `skills/pipeline/00-client-intake`
- `skills/pipeline/01-executive-summary`
- `skills/pipeline/10-financial-projections`
- `skills/meta-strategy/meta-consulting-synthesis`
- `skills/meta-finance/meta-valuation`

Root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant. Leave `docs/`, `projects/`, `.git`, `tools/`, and other non-skill operational directories at root unless the directory itself is an actual skill with its own root `SKILL.md`.

Active skills live under `skills/<category>/<skill-name>/SKILL.md`; each skill folder is self-contained with optional `references/`.

### Skill Categories

Skills are grouped into thematic categories under `skills/`. Use `skills/<category>/<skill-name>/` when writing paths in docs; bare skill names remain valid when invoking skills by name.

- `pipeline/` — numbered plan-section skills (`00-plan-assembly` through `16-sustainability-strategy`)
- `advisory-deliverables/` — standalone organisational consulting documents that are NOT business-plan sections. Each owns its document architecture and East African context and defers substance: accounting to the finance engine, PPDA to proposal-skills, M&E methodology to the M&E skills.
  - `finance-policy-and-manual` — Financial Management Policy & Finance/Accounting Manual
  - `procurement-policy-and-manual` — Procurement Policy & Procurement/Disposal Manual (PPDA-aware)
  - `internal-controls-and-risk-framework` — Internal Control & Risk Management Framework (COSO ERM / ISO 31000, SoD, surcharge overlay)
  - `grants-management-manual` — Grants/Donor-Funds Management Manual (fund accounting, multi-currency flexing, eligibility, sub-granting)
  - `governance-and-board-charter` — Governance Framework, Board & committee charters, Delegation-of-Authority matrix
  - `hr-policy-manual` — Human Resources Policy Manual (Employment Act 2006 framing; pay/allowances/advances defer to the finance engine)
  - `me-framework-document` — standalone Monitoring, Evaluation & Learning (MEL) Framework
- `meta-finance/` — in-repo finance skills (bankability scoring, workbook audit); IFRS / IAS / accounting close, audit, reconciliation, and controls route to the external Chwezi Accounting Doctrine engine (`C:\wamp64\www\chwezi-accounting-doctrine`) per the Finance & Accounting Trigger below
- `ict/` — ICT-sector business-plan skills
- `industry-guides/` — sector reference guides (agriculture, manufacturing, hospitality, retail, etc.)
- `saas/` — SaaS GTM, unit economics, lifecycle, pricing, valuation
- `marketing-sales/` — `marketing-plan-orchestrator` for complete standalone marketing plans (20-section architecture, SMART objective builder, location and scope calibration, Bullseye channel selection, advertising and media plan, sales and account coverage, marketing economics, KPI and control plan, quality gate); `entrepreneurial-demand-generation`, `demand-forecasting`, and `digital-marketing-strategy` for their specialist layers.
- `writing-content/` — `ai-prompt-writer`, `blog-idea-generator`, `blog-writer`, `content-writing`, `premium-commercial-writing`
- `language/` — `east-african-english`, `language-standards`, `writing-quality`
- `meta-finance/` — bankability, valuation, financial stress test, revenue recognition, SLA controls
- `meta-pitch/` — `pitch-deck`, `meta-pitch-preparation`, `meta-presentation-design`
- `meta-pricing-gtm/` — pricing strategy, premium GTM, website investment planning
- `meta-reporting/` — board & investor reporting
- `meta-strategy/` — end-to-end business-plan orchestration, consulting synthesis, due diligence, optionality (including exit readiness and sale preparation), governance, statistics, and the strategy-rigour set: `meta-strategic-factor-analysis` (PESTEL key drivers, five forces, EFAS/IFAS/SFAS on one 1–5 scale, SWOT to TOWS), `meta-strategic-audit`, `meta-strategic-options-evaluation` (SAFe, strategy clock, low-cost-rival response, 35-word strategy statement gate), `meta-business-model-design` (Debelak GEL scoring, run before drafting), `meta-international-market-entry` (CAGE, institutional voids, Diamond, entry modes)
- `meta-sustainability/` — sustainability strategy references
- `meta-utility/` — `skill-writing`, `skill-safety-audit`, `proposal-architect`, `update-claude-documentation`, `anti-ai-slop`, `ai-slop-audit`

### Naming Conventions

- Core plan sections: `01-executive-summary` through `15-appendices` (numbered for reading order)
- Meta/analytical skills: `meta-` prefix (e.g., `meta-financial-stress-test`)
- Utility skills: plain names (e.g., `skill-writing`)

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

Additional authoring rules:

- Audit and review skills default to read-only; mutation, publishing, spending, destructive action, and certification require explicit authority.
- Keep `SKILL.md` at or below 500 lines and use British English.
- Route every serious full-plan engagement through `business-plan-orchestrator`; use `00-plan-assembly` only for the final packaging stage. Validate the cross-engine release bundle before external handoff.
- Use `meta-investment-committee-red-team` for blocker-first lender, DFI, VC, grant or owner-board rehearsal only after a complete pack exists; simulation is not approval.

## Default Baseline

Kaizen is mandatory across the engine. Load `skills/meta-strategy/kaizen-improvement-system/SKILL.md` for engine or product audits and book-driven improvement. Publish audits with a hard maximum of 65/100; every remediation plan targets 95/100 and must name evidence, owners, experiments, and re-audit dates. Route current external claims to Digital Research Skills Engine and finance doctrine to Chwezi.

For serious full business-plan work, start with `business-plan-orchestrator`, which controls the stage register, cross-engine handoffs, blocker precedence and release bundle. It routes to these baseline skills:

- `00-client-intake`
- `country-context/{country}` where available, otherwise Uganda defaults
- `meta-critical-thinking-business-logic`
- `meta-consulting-synthesis`
- `meta-bankability-scoring`
- `meta-due-diligence`
- `meta-operational-readiness-due-diligence` when the plan depends on local banking, tax, licensing, payroll, FX, compliance, logistics, privacy, government interface, or local partnerships

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

- Standalone marketing plan: `skills/marketing-sales/marketing-plan-orchestrator/SKILL.md` owns market choices, situation analysis, SMART and location-calibrated objectives, positioning, channels (Bullseye), advertising and media, sales plan, economics, budget reconciled to the P&L, KPIs, control and the marketing-plan quality gate. Section 07 remains the business-plan component and follows `skills/pipeline/07-marketing-sales-strategy/references/business-plan-marketing-section-standard.md`, drawing on the orchestrator's references; social-media-skills is the digital marketing and advertising engine and owns detailed media plans, creative briefs, build specifications, optimisation, attribution, channel execution briefs and content calendars, while this engine owns plan-level advertising objectives, the budget envelope and the media-mix decision reconciled to the P&L (handoff table in the orchestrator's document architecture).
- Strategy rigour: `meta-strategic-factor-analysis` (EFAS/IFAS/SFAS, TOWS), `meta-strategic-audit` (read-only audit), `meta-strategic-options-evaluation` (SAFe, strategy clock, low-cost-rival response, strategy statement gate), `meta-business-model-design` (score the model before drafting), `meta-international-market-entry` (cross-border entry), `meta-strategic-optionality` (exit readiness and sale preparation; valuation to `meta-valuation`, tax to Chwezi).
- Plan wording: `skills/language/writing-quality/references/business-plan-phrase-bank.md` and its section, marketing-plan and article files; `strategy_type` is recorded at `00-client-intake`.
- Full bankable plan: `business-plan-orchestrator` -> `00-client-intake` -> evidence design -> `meta-business-model-design` -> `meta-critical-thinking-business-logic` -> sections `02` to `16` -> `01-executive-summary` -> synthesis/model/challenge gates -> `15-appendices` -> `00-plan-assembly` -> cross-engine finalisation -> validated release bundle
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

## Plan Content Doctrine

### Key Methodologies

- Financial sections follow Rogoff's bankability criteria
- Marketing sections follow Palo Alto's On Target framework, now executed through `skills/pipeline/07-marketing-sales-strategy/references/business-plan-marketing-section-standard.md` (section versus standalone plan, required content, depth by plan type, reconciliation with sections 03–06, 10, 12 and 13). Standalone marketing plans use `marketing-plan-orchestrator` and its references; Section 07 borrows those methods rather than duplicating them.
- Every objective and target in a plan or marketing plan must pass the SMART quality test (specific, measurable, accurate and achievable, realistic, time-bound) and be applicable to the business, its location and scope — see `skills/marketing-sales/marketing-plan-orchestrator/references/smart-objectives-builder.md` and `location-and-scope-calibration.md` (Uganda/East Africa defaults, data-protection registration, consent and direct-marketing objection rules).
- Plan wording uses the section-by-section phrase bank in `skills/language/writing-quality/references/business-plan-phrase-bank.md` (index) with its section files, `marketing-plan-phrase-bank.md` and `article-and-blog-phrase-guidance.md`; record the client's `strategy_type` at intake (`00-client-intake`) and apply its emphasis row in every section.
- Before drafting sections, score the business model with `meta-business-model-design`; use `meta-strategic-factor-analysis` and `meta-strategic-options-evaluation` when strategic choices are contested.
- Every number in a plan carries its evidence class (verified fact, assumption, estimate, projection or target) with source and date — see `skills/marketing-sales/marketing-plan-orchestrator/references/evidence-discipline-for-marketing-claims.md`.
- Implementation/M&E follows Jan B. King's game plan methodology
- AI integration section is mandatory for 2026-era plans
- When digitisation or technology modernisation is a material part of the plan, run `meta-digital-transformation` before or alongside `14-ai-integration` so the plan covers customer networks, data, process redesign, business-model change, and investment logic rather than AI tooling alone.
- When a plan includes a website, ecommerce site, content/SEO engine, landing pages, customer portal, web app, website-design service line, or website startup/recurring costs, run `meta-website-investment-planning` so the plan explains website role, design philosophy, stack, content/SEO, operations, realistic costs, and cross-section consistency.
- When a plan is for retail, omnichannel commerce, supermarkets, shops, POS-enabled stores, e-commerce operations, merchandising, pricing, promotions, markdowns, loyalty, fulfilment, returns, shrink, vendor terms, private label, or retail dashboards, load `skills/industry-guides/retail/guide.md` and `skills/industry-guides/retail/references/retail-operating-model-and-engine-plan.md` before drafting operations, marketing/sales, financial projections, risk, and implementation sections.
- Pricing discipline follows Kennedy/Marrs *No B.S. Price Strategy* — use `meta-pricing-strategy` skill + `skills/meta-pricing-gtm/meta-pricing-strategy/references/price-strategy-audit-and-proposition-stack.md`. Never accept a plan with cost-plus or competitor-match pricing without running the 9 Failures audit and the 5 Propositions stack.
- Sales and go-to-market copy apply Kennedy + Brunson direct-response frameworks — see `skills/pipeline/07-marketing-sales-strategy/references/direct-response-selling-playbook.md`, `skills/pipeline/07-marketing-sales-strategy/references/long-form-sales-letter-build.md`, and `skills/pipeline/07-marketing-sales-strategy/references/funnel-and-value-ladder-design.md`.
- Attraction, conversion, retention, and referral logic should be explicit in serious go-to-market sections; use `skills/pipeline/07-marketing-sales-strategy/references/direct-response-commercial-system.md` when the plan has channels but no commercial system.
- Major systems, digitisation, expansion, or automation recommendations should survive a business-case test — problem, options, do-nothing case, incremental economics, timing, and sensitivity. Use `skills/meta-strategy/meta-critical-thinking-business-logic/references/business-case-test.md`.
- Serious plan logic must pass `skills/meta-strategy/meta-critical-thinking-business-logic/SKILL.md`: essential questions, claim-evidence-warrant mapping, mental-model checks, design-thinking validation, strategic logic, and achievability review.

### When Generating Plan Content

- Always ask for the business name, industry, and country context first
- Financial projections need explicit assumptions — never fabricate numbers
- Market data must be sourced or clearly flagged as estimates
- Each section should cross-reference related sections for consistency
- Load-bearing claims must show evidence, warrant, assumptions, countercase, and implication before they are promoted into polished prose
- Do not call a plan convincing, bankable, investor-ready, or achievable unless market, operations, financials, risk, funding ask, and implementation timing reconcile

### Currency and Localisation

- **Default context: Uganda (UGX)**. All examples, costs, and financial projections should use Ugandan Shillings (UGX) unless the user specifies a different country.
- When reference materials quote foreign currency, use a dated, named source-register rate or an explicitly labelled planning assumption with sensitivity analysis. Never present a cached rate as current. Adjust for local economic realities rather than applying a bare conversion. Account for differences in:
  - Labour costs (significantly lower in Uganda)
  - Land/rent costs (varies by location — Kampala vs rural)
  - Input costs (some imported inputs may be more expensive)
  - Market prices and consumer purchasing power
- Use local regulatory context (URA tax requirements, KCCA/district licensing, UNBS standards, NEMA environmental permits)
- Reference local institutions: Bank of Uganda, Uganda Development Bank, microfinance institutions, SACCOs

### Multi-Country Plans (Non-Uganda)

When a `country-context/{country-name}/SKILL.md` file exists in the repo, **use it as the regulatory and financial context for all plan sections**:

1. **Currency** — use the currency code and exchange rates from Section 1 (replace UGX with local currency)
2. **Tax rates** — use Section 4 (replace Uganda PAYE bands, 30% corporate tax, 18% VAT, EFRIS references)
3. **Regulatory bodies** — use Section 5 (replace KCCA, URA, UNBS, NEMA with local equivalents)
4. **Banking context** — use Section 6 (replace Centenary Bank, Stanbic, UDB with local institutions)
5. **Salary benchmarks** — use Section 7 (replace Uganda wage bands)
6. **Risk context** — use Section 9 (replace Uganda-specific risks table in Section 12 skill)

**Universal frameworks always apply regardless of country:**
- CAMPARI, DSCR ≥ 1.25×, TAM/SAM/SOM methodology
- DCF/WACC/CAPM valuation, revenue multiples, Damodaran rules
- Pyramid Principle / SCQA (Minto), MECE / issue trees (Rasiel)
- Sales methodology (Schiffman, Keenan, gap selling)
- Risk assessment (COSO ERM, Bowtie, MECE risk register)
- All marketing frameworks (AARRR, 4Ps/7Ps, Kotler, Golden Circle)

If no country file exists, Uganda defaults apply. To create a file for a new country, copy `country-context/template.md` to `country-context/{country-name}/SKILL.md`. See `country-context/INDEX.md` for available countries.

### Source Referencing

- Cite reference books where they add credibility to the business plan: financial benchmarks, regulatory frameworks, pricing methodologies, industry statistics
- Format: parenthetical (Author, Year) on first use; full bibliographic details in the appendices
- Do NOT cite for generic advice, the user's own data, or derived projections

## Anti-AI-Slop Quality Gate

Two skills keep generated output from reading as AI slop. They live at
`skills/meta-utility/anti-ai-slop/` and `skills/meta-utility/ai-slop-audit/`.

- **`anti-ai-slop` is MANDATORY and applied in REAL TIME.** It is a live constraint applied
  **continuously while generating** — to every section, paragraph, slide, and projection as it
  is written, not only as a final pre-ship pass. The moment a banned word, generic placeholder,
  unverified market size/figure, or template default appears, fix it in place. Run it on every
  generated business plan, plan section, executive summary, pitch deck, investment case, funding
  request, GTM/pricing narrative, financial narrative, grant proposal, or blog post before that
  output is delivered or called bankable/investor-ready/submission-ready. Apply it after
  `writing-quality` and the section skill, and after `meta-critical-thinking-business-logic`.
  Financial and market claims must pass its verify-before-emit rule — never invent a market
  size, growth rate, TAM/SAM/SOM figure, or benchmark.
- **`ai-slop-audit` RUNS AFTER EACH MAJOR ITERATION (not only on request).** Run it after each
  completed unit of work — each drafted plan section, each completed deck, each financial-narrative
  module, each significant revision, each milestone — logging a verdict each time; a grade **F
  blocks progression** to the next section or submission until the blocking findings are fixed.
  It also auto-runs whenever the user asks to analyse, review, evaluate, critique, audit, score,
  or de-slop a business plan, pitch deck, financial model or narrative, GTM/pricing narrative,
  proposal, plan section, or codebase for AI slop, or asks "does this look AI-generated?", and as
  the final gate before submission. It produces a graded A/B/C/F report with a 0–100 genericness
  score and a concrete fix per finding.

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


<!-- design-system-skills:trigger v2 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from the active runner's global engine-routing table or
`AGENTS.md`** — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
as primary type — hard ban: Inter, Geist, Roboto, Open Sans, Lato, Arial, Fraunces, IBM Plex (all
faces); secondary ban: Space Grotesk, Instrument Serif, Poppins, Montserrat, Nunito, Nunito Sans;
Roboto Mono and IBM Plex Mono are banned as monospace choices; Source Sans 3 only as a paired
body face; no bare system stacks alone. State the chosen typeface and reason before producing
any artifact.
<!-- /design-system-skills:trigger -->

## Book extractions and source text

Book extractions, book summaries and raw source text must never be stored in this repository. The former `book-extractions/` folder was removed on 2026-09-23 under a zero-loss capability-preservation map. Books are durable concept inputs only: fold their methods into the owning skill's `references/` as task-oriented, paraphrased procedures, checklists, templates, phrase patterns and decision rules, cite the source briefly (Author (Year) *Title*, Publisher), keep verbatim quotation to 25 words or fewer, and route volatile claims through the currentness register or the Digital Research engine. `scripts/source_ingestion_guardrail.py` fails on any `book-extractions/` path.

## Human-English editorial standard (2026-08 Kaizen)

Every business plan, pitch, proposal, report, blog post, executive summary, and client-facing message must also load [`skills/language/writing-quality/references/human-english-five-pass-standard.md`](skills/language/writing-quality/references/human-english-five-pass-standard.md). Apply its five passes in real time: reader and purpose, genre and spine, meaning and evidence, sentence/paragraph craft, and proof/read-aloud. Use it alongside `skills/language/writing-quality/`, `skills/language/language-standards/`, and `skills/meta-utility/anti-ai-slop/`; it does not replace financial, market, or reasoning gates.

The standard requires audience-fit British English, concrete nouns, exact verbs, controlled vocabulary, correct grammar and collocation, varied intentional rhythm, visible judgement, and a distinct register for plans, proposals, social copy, web copy, research, political writing, and app messages. Natural writing must never be simulated with errors, slang, fake anecdotes, or unsupported certainty.

## DOMAIN PROMPT GENERATION CONTRACT

For a prompt handoff, read the local [domain prompt contract](docs/ai-prompting/domain-prompt-compilation-contract.md). Generate a ready-to-paste prompt using decision, audience, evidence, assumptions, economics, downside case, constraints, output, and acceptance checks. Never prompt around missing market, finance, tax, or legal evidence. **Ready-to-paste prompt:** include mode, requirements, assumptions, risks, and next action. **Failure action:** repair the unsupported or unreconciled field, then re-test.

## PORTFOLIO CRAFT CONTRACT

Load `C:\wamp64\www\chwezi-engine-agents\docs\operations\portfolio-craft-standard-2026-09-04.md` when available. Build plans one decision-bearing section at a time: frame the reader and decision, inspect the evidence and model, draft the smallest useful section, test its assumptions and downside case, revise the argument, and then assemble. Every plan must make its thesis, customer logic, operating logic, financial reconciliation, funding use, counter-case, and next action concrete; delete sections that carry no decision or evidence. Do not produce a full plan as an opaque batch. Apply `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure` to kaizen itself. Missing source, model, spreadsheet, render, reviewer, or stakeholder evidence is `NOT ASSESSED`, never a pass.
