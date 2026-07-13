# Business Plan Skills Suite

## Project Structure

This is a collection of Claude Code skills for generating bankable business plans. Active skills live under `skills/<category>/<skill-name>/SKILL.md`; each skill folder is self-contained with optional `references/`.

The repository root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant. Keep `docs/`, `.git`, `tools/`, and unrelated non-skill operational directories at root.

## Skill Categories

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
- `finance/` — IFRS / IAS / accounting close, audit, reconciliation, controls
- `ict/` — ICT-sector business-plan skills
- `industry-guides/` — sector reference guides (agriculture, manufacturing, hospitality, retail, etc.)
- `saas/` — SaaS GTM, unit economics, lifecycle, pricing, valuation
- `marketing-sales/` — `demand-forecasting`, `digital-marketing-strategy`
- `writing-content/` — `ai-prompt-writer`, `blog-idea-generator`, `blog-writer`, `content-writing`, `premium-commercial-writing`
- `language/` — `east-african-english`, `language-standards`, `writing-quality`
- `meta-finance/` — bankability, valuation, financial stress test, revenue recognition, SLA controls
- `meta-pitch/` — `pitch-deck`, `meta-pitch-preparation`, `meta-presentation-design`
- `meta-pricing-gtm/` — pricing strategy, premium GTM, website investment planning
- `meta-reporting/` — board & investor reporting
- `meta-strategy/` — consulting synthesis, due diligence, optionality, governance, statistics
- `meta-sustainability/` — sustainability strategy references
- `meta-utility/` — `skill-writing`, `skill-safety-audit`, `proposal-architect`, `update-claude-documentation`, `anti-ai-slop`, `ai-slop-audit`

### Naming Conventions

- Core plan sections: `01-executive-summary` through `15-appendices` (numbered for reading order)
- Meta/analytical skills: `meta-` prefix (e.g., `meta-financial-stress-test`)
- Utility skills: plain names (e.g., `skill-writing`)

### Skill Authoring Rules

- Every active skill follows the July 2026 contract in `skills/meta-utility/skill-writing/SKILL.md` and its dual-compatible template.
- Frontmatter names the directory, uses a one-line `Use when` description of at most 350 characters, and declares portable Claude Code/Codex metadata.
- Skills declare positive and negative triggers, inputs, outputs, evidence, ordered workflow, decisions, quality, five corrected anti-patterns, permissions, degraded mode, and references.
- Audit and review skills default to read-only; mutation, publishing, spending, destructive action, and certification require explicit authority.
- Keep `SKILL.md` at or below 500 lines and use British English.
- Run the zero-debt validator and routing smoke test before release; see `CONTRIBUTING.md`.

### Key Methodologies

- Financial sections follow Rogoff's bankability criteria
- Marketing sections follow Palo Alto's On Target framework
- Implementation/M&E follows Jan B. King's game plan methodology
- AI integration section is mandatory for 2026-era plans
- When digitisation or technology modernisation is a material part of the plan, run `meta-digital-transformation` before or alongside `14-ai-integration` so the plan covers customer networks, data, process redesign, business-model change, and investment logic rather than AI tooling alone.
- When a plan includes a website, ecommerce site, content/SEO engine, landing pages, customer portal, web app, website-design service line, or website startup/recurring costs, run `meta-website-investment-planning` so the plan explains website role, design philosophy, stack, content/SEO, operations, realistic costs, and cross-section consistency.
- When a plan is for retail, omnichannel commerce, supermarkets, shops, POS-enabled stores, e-commerce operations, merchandising, pricing, promotions, markdowns, loyalty, fulfilment, returns, shrink, vendor terms, private label, or retail dashboards, load `skills/industry-guides/retail/guide.md` and `skills/industry-guides/retail/references/retail-operating-model-and-engine-plan.md` before drafting operations, marketing/sales, financial projections, risk, and implementation sections.
- Pricing discipline follows Kennedy/Marrs *No B.S. Price Strategy* — use `meta-pricing-strategy` skill + `book-extractions/kennedy-no-bs-price-strategy-extraction.md`. Never accept a plan with cost-plus or competitor-match pricing without running the 9 Failures audit and the 5 Propositions stack.
- Sales and go-to-market copy apply Kennedy + Brunson direct-response frameworks — see `book-extractions/kennedy-no-bs-sales-success-extraction.md`, `kennedy-ultimate-sales-letter-extraction.md`, and `brunson-dotcomsecrets-ignite-extraction.md`.
- Attraction, conversion, retention, and referral logic should be explicit in serious go-to-market sections; use `book-extractions/kennedy-magnetic-marketing-extraction.md` when the plan has channels but no commercial system.
- Major systems, digitisation, expansion, or automation recommendations should survive a business-case test — problem, options, do-nothing case, incremental economics, timing, and sensitivity. Use `book-extractions/haines-how-to-create-a-business-case-extraction.md`.
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
3. Read the corresponding skill `SKILL.md` in the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
4. Apply the **finance & accounting quality gate** from the finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`).
5. Record the gate run in the artefact manifest.

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
