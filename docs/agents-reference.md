# Reference sections moved out of AGENTS.md

Moved verbatim on 2026-11-10 to keep the always-loaded file small (token economy; Codex reads at most 32 KiB of AGENTS.md). Open the section you need.

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
- `meta-finance/` — in-repo finance skills (bankability scoring, workbook audit); IFRS / IAS / accounting close, audit, reconciliation, and controls route to the external Chwezi Accounting Doctrine engine (resolve its location through the global engine-routing table) per the Finance & Accounting Trigger below
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

- Core plan sections: `01-executive-summary` through `16-sustainability-strategy` (numbered for reading order; `11b-grant-proposal` is the grant variant of `11-funding-request`)
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

