# Business Plan Skills Suite

A modular collection of Claude Code skills for generating, validating, and delivering bankable business plans. Each section of a professional business plan is a standalone skill — invoke individually or chain to produce a complete investor-ready document.

**51 skills.** Default context: Uganda / East Africa (UGX). All frameworks are universally applicable; country-specific data swaps via the `country-context/` system.

---

## SaaS + AI-on-SaaS + Agent Business-Plan Stack (May 2026)

Major living-plan layer added for ICT/SaaS startups across all sections plus meta-skills. Every new and enhanced skill conforms to the **living-plan governance pattern** (data feed · cadence · owner · decision-log · variance-threshold · sunset).

**SaaS plans (16 skills + 15 enhancements + 29 references):** unit economics & cohort model, pricing & packaging strategy, living-plan governance meta, GTM motion design, sales org & capacity planning, customer success operating model, bankability & investor readiness, valuation & fundraising strategy, MVP-to-PMF strategy, vertical niche selection, marketing channel economics, lifecycle email & retention, board & investor reporting meta, strategic optionality meta, ICT services firm plan, ICT product company plan.

**AI-on-SaaS plans (13 skills + 17 enhancements + 26 references):** AI unit economics & COGS, AI cost-of-tenant calculator, AI pricing strategy, AI market & TAM (with attribution discipline), AI moat & defensibility (7-question rubric), AI product strategy & roadmap, AI talent strategy (African map: CMU-Africa, ALU, Andela AI, Deep Learning Indaba, AIMS, Lelapa, Masakhane, Awarri), AI risk & stress test, AI bankability meta, AI valuation adjustments meta, AI funding stage playbook, AI-for-good grant proposal, AI sustainability & ethics.

**Agent plans (13 skills + 17 enhancements + 25 references):** agent unit economics & COGS (cost-per-resolved-task), agent pricing strategy (per-resolution / per-outcome / per-step / per-agent / hybrid), agent product strategy & roadmap, agent moat & wrapper-risk (8-question rubric: 40–70% valuation discount when wrapper), agent risk & stress test (action taxonomy A/B/C/D + 12-category register), agent talent strategy (Agent Architect, Tool, Eval, AI Safety Lead, HITL Designer, MLOps, FDE, Agent PM, Domain Expert), agent funding stage playbook, agent implementation timeline (shadow → supervised → agentic gates), agent integration deep, agent sustainability & ethics, agent bankability meta (7-dimension 0–100 scorecard), agent valuation adjustments meta, agent board & investor reporting meta.

**Agent SLA + commercial (11 skills + many enhancements + 13 references):** ASC 606 / IFRS 15 revenue recognition for agents, deferred revenue + credit reserves, refund reserve methodology, SLA-COGS treatment policy, SLA economics in projection, commercial packaging economics, outcome pricing business case, SLA risk + stress test, investor narrative on SLA, SLA financial controls meta, valuation overlay for SLA meta.

**Africa context:** `country-context/africa-regional/africa-ict-saas-market-context.md` with Section 14 (Africa-AI) and Section 15 (Africa-Agent) covering compute scarcity (af-south-1, Liquid, Cassava, MTN AI Factories, MainOne, Raxio, Teraco, Ethiopian AI Institute), sovereign-AI demand, local-language model opportunity, national AI policies (KE/NG/ZA/RW/EG/UG/GH/MU/AU), African AI funding ecosystem, talent map, vertical opportunities, mobile-money realities, FX corridor, sector regulators.

**Working financial models (7 Excel workbooks, 2,400+ formulas):** under `skills/.../templates/`:
- `saas-unit-economics-model.xlsx`, `saas-cohort-and-retention-model.xlsx`, `saas-financial-projection-3yr-5yr.xlsx` (Multi-Step P&L + 60-month ARR waterfall + Bull/Base/Bear scenarios), `saas-ai-cost-of-tenant-calculator.xlsx`, `saas-living-plan-kpi-dashboard.xlsx` (auto-REPLAN flag at >10% variance), `saas-agent-cost-per-task-calculator.xlsx`, `saas-agent-unit-economics-model.xlsx` (Wrapper-vs-Moat scoring → valuation multiplier {0.6, 0.85, 1.10, 1.35}).
- Idempotent build scripts under `scripts/build-financial-models/`.
- Master README at `templates/README-financial-models.md`.

**Book extractions** (in `book-extractions/`): 7 SaaS books distilled through the business-plan lens, plus 5 audit documents.

---

## What This Suite Does

| Need | Skills to Use |
|---|---|
| Write a complete business plan | `01` through `15` (in order) |
| Write a specific section | Invoke the numbered skill directly |
| Test whether a plan makes logical and business sense | `meta-critical-thinking-business-logic` |
| Stop a plan, deck, or narrative reading as AI slop (pre-ship gate) | `anti-ai-slop` |
| Audit a plan, deck, model, or section for AI slop and score it | `ai-slop-audit` |
| Validate an existing plan | `meta-bankability-scoring` |
| Upgrade pricing / defend premium positioning | `meta-pricing-strategy` |
| Stress-test the financials | `meta-financial-stress-test` |
| Build a digitisation / digital-transformation roadmap | `meta-digital-transformation` |
| Validate the market claims | `meta-market-validation` |
| Convert the plan to action | `meta-quarterly-gameplan` |
| Create a pitch deck | `pitch-deck` (orchestrates `meta-pitch-preparation` + `meta-presentation-design`) |
| Prepare for live pitch / investor Q&A | `meta-pitch-preparation` |
| Design slides and coach delivery | `meta-presentation-design` |
| Write a grant proposal (LogFrame / Theory of Change) | `11b-grant-proposal` |
| Prepare for investor due diligence | `meta-due-diligence` |
| Build a monitoring and evaluation framework | `meta-monitoring-evaluation` |
| Generate industry-specific context | `industry-guides` |
| Write a business article or blog post | `blog-writer` + `blog-idea-generator` |
| Test a business idea before writing the plan | `idea-testing` |
| Write a client proposal | `proposal-architect` |

### Anti-AI-slop quality gate

Two paired skills keep generated output from reading as AI slop:

- **`anti-ai-slop` is the real-time guardrail.** It is a live constraint applied while you write — every section, paragraph, slide, and projection is checked as it is drafted, not only in a final pass. Banned-vocabulary filler, generic placeholders, and unverified figures are fixed in place. Financial and market claims must pass its verify-before-emit rule: never invent a TAM/SAM/SOM figure, growth rate, or benchmark.
- **`ai-slop-audit` runs after each major iteration** — each drafted section, completed deck, financial-narrative module, or significant revision — and auto-runs whenever a request asks to analyse, review, or audit an artefact for slop. It returns a graded report (A/B/C/F) with a 0–100 genericness score; a grade **F blocks progression** to the next section or to submission until the blocking findings are fixed.

---

## Methodology

Built on 30+ primary sources across strategy, finance, marketing, and management:

**Foundational business planning:**
- Rogoff — *Bankable Business Plans* (investor-readiness criteria, CAMPARI)
- Palo Alto Software — *On Target* (marketing planning depth)
- Jan B. King — *Business Plans to Game Plans* (strategy-to-action, M&E)

**Strategy and competitive analysis:**
- Porter (1980, 1985) — Five Forces, Value Chain, Generic Strategies
- Ohmae (1982) — 3C Strategic Triangle, Key Factors for Success
- Fahey & Randall (2000) — Portable MBA: onstage/backstage model, Value Net

**Finance and valuation:**
- Damodaran (2011) — DCF, WACC, CAPM, revenue multiples
- Feld & Mendelson (2019) — Equity term sheets, cap tables, liquidation preference
- Agrawal, Gans & Goldfarb (2022) — AI economics, prediction machines

**Marketing, pricing, and pitch:**
- Klaff (2011) — *Pitch Anything* (STRONG method, frame control)
- McGowan (2014) — *Pitch Perfect* (Hook-Meat-Payoff, delivery)
- Gallo (2010), Duarte (2012) — presentation design standards
- Kennedy & Marrs (2011) — *No B.S. Price Strategy* (9 price failures, 5 Propositions, Triangle of Preeminence, niche pricing, competing with free)
- Kennedy (2004) — *No B.S. Sales Success* (23 strategies, 6-step process, takeaway selling, positioning-not-prospecting)
- Kennedy (2000) — *The Ultimate Sales Letter* (28-step system, Power of a Sequence, Creative P.S.)
- Brunson (2013) — *DotComSecrets Ignite* (Secret Formula, Value Ladder, 3 traffic types, 7 phases of a lead, Star-Story-Solution, Perfect Webinar)

**Strategy and innovation:**
- Teece (2010) — Business model vs strategy, dynamic capabilities
- Mangematin et al. (2017) — 4V business model framework
- Digital Business Strategy (2024) — 6D model, Three Horizons, Doblin 10 types
- Cunningham (2014) — *Berkshire Beyond Buffett* (culture as moat)
- Rogers (2016) — five domains of digital transformation: customers, competition, data, innovation, value
- Molenaar (2022) — demand-driven strategy, value networks, product-as-a-service, digital leadership
- *Business Models for E-Commerce* — demand-side, supply-side, collaborative, and transaction-model design
- Haines (2022) — business-case discipline for major investments, options, incremental economics, and benefits audit
- Kennedy and Walsh-Phillips (2018) — attraction, conversion, retention, lead magnets, and referral systems

**Critical thinking, reasoning, and achievability:**
- Critical-thinking and logic references — claim-evidence-warrant mapping, assumptions, countercases, fallacy checks, and structured problem-solving
- Essential-question and Socratic-questioning references — purpose, concepts, evidence, implications, ethical questions, and writing discipline
- Mental-model references — first principles, map versus territory, base rates, incentives, second-order effects, inversion, margin of safety, and circle of competence
- Design-thinking and strategic-thinking references — user-centred problem definition, prototyping, pattern recognition, systems analysis, mental agility, structured problem-solving, visioning, and political savvy

**Uganda / East Africa context:**
- IFC/World Bank: CPSD Uganda (2022), Human Capital Review (2025)
- UBOS: CPI, KEI, NPHC data
- RSM/Baker Tilly (2025): Uganda doing business guide
- UDB Environmental and Social Policy; NEMA Act; Employment Act 2006

---

## Skill Directory

Skills live under `skills/<skill-name>/SKILL.md`. Tables below list skill names; the filesystem path is always `skills/<skill-name>/`.

### Core Plan Sections

Invoke in order (02 → 15, then 01 last) to produce a complete plan.

| # | Skill Directory | What It Generates |
|---|---|---|
| 00 | `00-plan-assembly` | Cover letter, binding order, attachments checklist, funder type identification |
| 01 | `01-executive-summary` | The investor pitch — written last, presented first |
| 02 | `02-company-overview` | Mission, vision (Golden Circle), legal structure, NIN/BRN, milestones |
| 03 | `03-products-services` | Value proposition, product lifecycle, IP protection, R&D pipeline |
| 04 | `04-market-analysis` | Industry analysis, TAM/SAM/SOM, strategic groups, data sources |
| 05 | `05-target-market` | Customer personas, segmentation, buyer behaviour |
| 06 | `06-competitive-analysis` | SWOT, competitive matrix, Five Forces, moat and differentiation |
| 07 | `07-marketing-sales-strategy` | 4Ps/7Ps, pricing, channels, sales funnel, digital strategy |
| 08 | `08-operations-plan` | BPM lifecycle, supply chain, facilities, value chain, capacity |
| 09 | `09-management-team` | Team bios, org chart, advisory board, succession, hiring plan |
| 10 | `10-financial-projections` | P&L, cash flow, balance sheet, break-even, DSCR, assumptions |
| 11 | `11-funding-request` | The ask, use of funds, CAMPARI, collateral, DSCR, terms |
| 11b | `11b-grant-proposal` | LogFrame, Theory of Change, budget narrative, grant sources |
| 12 | `12-risk-analysis` | Risk matrix, COSO ERM, Bowtie, Uganda-specific risks, mitigation |
| 13 | `13-implementation-timeline` | Gantt, milestones, Pre-Phase 0 regulatory gate, 90-day sprints |
| 14 | `14-ai-integration` | AI utilisation map, 6D model, Three Horizons, automation ROI |
| 15 | `15-appendices` | Supporting documents, Uganda bank submission checklist, templates |
| 16 | `16-sustainability-strategy` | Mandatory from 2026: sustainability vision, SDGs, climate adaptation, circular economy, social impact KPIs |

### Pitch and Presentation Skills

| Skill Directory | What It Does |
|---|---|
| `pitch-deck` | **Start here for any pitch.** Unified workflow: sequencing `meta-pitch-preparation` → `meta-presentation-design` → delivery coaching. Produces a presentation-ready deck for any audience type. |
| `meta-pitch-preparation` | Pitch strategy, frame control (Klaff STRONG method), McGowan Hook-Meat-Payoff, Q&A preparation, rehearsal protocol. Use directly for self-prep or client coaching. |
| `meta-presentation-design` | Slide design (Duarte Sparkline, assertion-evidence standard), 13-slide master template, delivery coaching, deck audit. |

### Analytical Meta-Skills

| Skill Directory | What It Does |
|---|---|
| `meta-critical-thinking-business-logic` | Tests claims, assumptions, evidence, business logic, feasibility, mental models, strategic fit, and achievability before synthesis or final review |
| `meta-accounting-finance-review` | IFRS-aware accounting, management accounting, financial-model, controls, and projection integrity review before bankability, valuation, due diligence, or final assembly |
| `meta-sustainability` | Mandatory sustainability pre-screen (Mode A) and audit (Mode C); Sustainability Readiness Score (5 dimensions); sector materialities; SDG alignment; IFC Performance Standards compliance for DFI applications |
| `meta-bankability-scoring` | CAMPARI 28-item checklist; bank loan readiness scoring; 12-point cross-section consistency audit |
| `meta-financial-stress-test` | 4-scenario stress model, Uganda historical shocks, DSCR stress test, Early Warning Dashboard |
| `meta-market-validation` | Validates market claims against real data; MECE issue trees; flags unsupported assumptions |
| `meta-digital-transformation` | Diagnoses digital maturity, prioritises digitisation and business-model modernisation, and links technology choices to customer value, operations, data, and business-case logic |
| `meta-monitoring-evaluation` | Converts plan into KPI dashboard, M&E framework, funder reporting obligations |
| `meta-quarterly-gameplan` | Converts annual strategy into 90-day action sprints |
| `meta-due-diligence` | DD readiness, outbound OSINT competitor intelligence, plan DD audit; data room structure |
| `meta-pricing-strategy` | Audit and upgrade pricing strategy using Kennedy/Marrs *No B.S. Price Strategy*: 9 price failures, 5 Propositions, Triangle of Preeminence (Lycka), niche pricing lift, quid pro quo discounting, competing with free |

### Content and Marketing Skills

| Skill Directory | What It Does |
|---|---|
| `blog-idea-generator` | Generates business plan blog post ideas derived from the reference book library |
| `blog-writer` | Writes structured, SEO-ready blog posts on business planning topics |
| `content-writing` | General business content writing with East Africa voice and standards |
| `digital-marketing-strategy` | Digital channel strategy, social media, SEO, paid acquisition |
| `proposal-architect` | Client-facing proposals: structure, persuasion, pricing, follow-up |

### Supporting and Utility Skills

| Skill Directory | What It Does |
|---|---|
| `east-african-english` | Language and tone standard — British spelling, East African idiom, plain English |
| `language-standards` | Cross-language writing quality standards |
| `idea-testing` | Rapid validation of a business idea before writing the full plan |
| `industry-guides` | Industry-specific reference guides for 13+ sectors (agri, retail, hospitality, health…) |
| `skill-writing` | Guide for authoring and extending skills in this suite |
| `skill-safety-audit` | Safety validation for new or modified skills |
| `anti-ai-slop` | Mandatory pre-ship guardrail — every generated plan, section, deck, or narrative passes it before delivery so output cannot read as AI slop |
| `ai-slop-audit` | Auto-runs on any request to analyse, review, audit, or score a plan, deck, model, or section for AI slop; returns a graded A/B/C/F report |
| `update-claude-documentation` | Documentation maintenance workflow |

### Book Extractions

Primary-source reference material stored in `book-extractions/`. Read these when a skill references them; they carry the detailed frameworks, scripts, and Uganda/EA adaptation notes.

| File | What It Contains |
|---|---|
| `kennedy-no-bs-price-strategy-extraction.md` | Kennedy/Marrs 9 Failures, 5 Propositions, Triangle of Preeminence, Hawaiian Fisherman, niche pricing, association principle, discount discipline, competing with free |
| `kennedy-no-bs-sales-success-extraction.md` | Kennedy 23 Strategies, Positioning-Not-Prospecting, 6-Step Sales Process, Takeaway Selling, Proof hierarchy |
| `kennedy-ultimate-sales-letter-extraction.md` | 28-step long-form system, Power of a Sequence, Hidden Benefit, Damaging Admission, Creative P.S. |
| `brunson-dotcomsecrets-ignite-extraction.md` | Secret Formula, Value Ladder, 3 traffic types, 7 phases of a lead, Star-Story-Solution (35 beats), OTO Bump, Perfect Webinar, Soap Opera + Seinfeld |
| `kennedy-magnetic-marketing-extraction.md` | Message-Market-Media triangle, attraction-conversion-retention system, lead magnets, follow-up sequencing, retention and referral discipline |
| `godin-startup-school-extraction.md` | Narrow-market focus, remarkability, tribe logic, anti-generic positioning |
| `business-models-ecommerce-extraction.md` | Digital transaction models, supply-side and collaborative commerce, revenue and cost logic for e-commerce |
| `rogers-digital-transformation-playbook-extraction.md` | Five domains of digital transformation, customer networks, platforms, data assets, rapid experimentation, value adaptation |
| `molenaar-demand-driven-business-strategy-extraction.md` | Demand-driven redesign, outside-in logic, value networks, network effects, product-as-a-service |
| `haines-how-to-create-a-business-case-extraction.md` | Business-case framing, option analysis, do-nothing case, incremental economics, sensitivity, benefits audit |
| `practical-small-business-guides-extraction.md` | Practical SME controls, owner bottlenecks, customer experience, branding basics, proportionate digital adoption |
| `project-management-integration-scope-extraction.md` | Objective/scope/deliverable discipline, project charter logic, WBS, change control, scope-creep prevention |

### Country Context

| Directory | What It Contains |
|---|---|
| `country-context/` | Country-specific data files that override Uganda defaults. Contains `template.md` for adding new countries (currency, tax rates, regulatory bodies, salary benchmarks, risk context). |

---

## Usage Examples

### Write a complete business plan

Invoke skills sequentially, sections 02–15, then 01 last:

```
Use the company-overview skill to generate section 02 for [Business Name], a [sector] business in [location]
```

### Write a single section

```
Use the market-analysis skill to size the Ugandan dairy processing market
```

### Validate an existing plan

```
Use the meta-bankability-scoring skill to score this business plan against UDB's CAMPARI criteria
```

### Create a pitch deck from a completed plan

```
Use the pitch-deck skill to build an investor pitch deck from this business plan
```

### Apply for a DFI loan — preparation checklist

1. Run `11-funding-request` → generates the funding request section with DSCR and collateral
2. Run `meta-bankability-scoring` → confirms CAMPARI compliance
3. Run `12-risk-analysis` → includes ESMP (use `11-funding-request/references/esmp-template.md`)
4. Run `meta-due-diligence` Mode A → builds the data room
5. Run `pitch-deck` → prepares the loan committee presentation

### Test a new business idea

```
Use the idea-testing skill to evaluate whether this business idea is worth developing into a full plan
```

### Build a digitisation roadmap for an existing business

```
Use the meta-digital-transformation skill to identify the most practical ways this business should digitise its sales, operations, and customer experience over the next 12 months
```

---

## Project Structure

```
business-plan-skills/
|-- README.md                  # Project overview and usage
|-- AGENTS.md                  # Agent operating guide
|-- CLAUDE.md                  # Claude Code project instructions
|-- docs/                      # Project documentation and historical analysis
|-- projects/                  # Optional project workspaces, if present
|-- skills/                    # Active skill repository (organised into thematic categories)
|   |-- pipeline/              # Numbered plan-section skills (00-plan-assembly ... 16-sustainability-strategy)
|   |   |-- 00-plan-assembly/
|   |   |-- 01-executive-summary/
|   |   `-- ...
|   |-- finance/               # IFRS / IAS / accounting & finance skills
|   |-- ict/                   # ICT-sector business-plan skills
|   |-- industry-guides/       # Sector reference guides (agriculture, manufacturing, etc.)
|   |-- saas/                  # SaaS-vertical skills (GTM, unit economics, lifecycle)
|   |-- marketing-sales/       # Demand forecasting, digital marketing strategy
|   |-- writing-content/       # Blog, content, copy & prompt-writing skills
|   |-- language/              # East-African English, language standards, writing quality
|   |-- meta-finance/          # Bankability, valuation, financial stress test, rev-rec
|   |-- meta-pitch/            # Pitch-deck orchestration, presentation design
|   |-- meta-pricing-gtm/      # Pricing strategy, premium GTM, website investment
|   |-- meta-reporting/        # Board & investor reporting
|   |-- meta-strategy/         # Consulting synthesis, due diligence, optionality, governance
|   |-- meta-sustainability/   # Sustainability strategy references
|   `-- meta-utility/          # skill-writing, skill-safety-audit, proposal-architect, update-claude-documentation
|-- country-context/           # Country data overrides and country-specific skills
|-- book-extractions/          # Primary-source reference material
|-- blog-posts/                # Draft and published blog content
|-- proposals/                 # Proposal outputs or working material
`-- tools/                     # Operational tooling, not a skill directory
```

Root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant. Active skills should not live at the repository root or directly under `skills/`; each active skill belongs at `skills/<category>/<skill-name>/SKILL.md`. The category directories are listed in the tree above and described in the "Skill Categories" section below.

---

## Skill Categories

Skills are grouped into thematic categories under `skills/`. When invoking a skill by name, the AI auto-resolves the path; when referencing one in documentation, use `skills/<category>/<skill-name>/`.

| Category | Purpose |
|----------|---------|
| `pipeline/` | Numbered plan-section skills (`00-plan-assembly` through `16-sustainability-strategy`) — the core business-plan generation flow |
| `finance/` | IFRS / IAS / accounting close, audit, controls, reconciliation, UI patterns |
| `ict/` | ICT-sector business-plan skills (product company, services firm) |
| `industry-guides/` | Sector reference material (agriculture, manufacturing, hospitality, retail, etc.) |
| `saas/` | SaaS-vertical skills (GTM, unit economics, lifecycle, pricing, valuation) |
| `marketing-sales/` | `demand-forecasting`, `digital-marketing-strategy` |
| `writing-content/` | `ai-prompt-writer`, `blog-idea-generator`, `blog-writer`, `content-writing`, `premium-commercial-writing` |
| `language/` | `east-african-english`, `language-standards`, `writing-quality` |
| `meta-finance/` | Bankability, valuation, financial stress test, revenue recognition, SLA controls |
| `meta-pitch/` | `pitch-deck`, `meta-pitch-preparation`, `meta-presentation-design` |
| `meta-pricing-gtm/` | Pricing strategy, premium GTM, website investment planning |
| `meta-reporting/` | Board & investor reporting (human + agent variants) |
| `meta-strategy/` | Consulting synthesis, due diligence, optionality, living-plan governance, statistics |
| `meta-sustainability/` | Sustainability strategy references |
| `meta-utility/` | `skill-writing`, `skill-safety-audit`, `proposal-architect`, `update-claude-documentation`, `anti-ai-slop`, `ai-slop-audit` |

---
## Authoring Standards

Every skill follows this structure:

```
skills/skill-name/
|-- SKILL.md              # Required: YAML frontmatter (name, description) + skill content
`-- references/           # Optional: supporting methodology, data tables, templates
    |-- framework-name.md # Each reference file covers one source or framework
    `-- ...
```

**SKILL.md rules:**
- Maximum 500 lines
- YAML frontmatter: `name`, `description` (single line, comprehensive)
- British English throughout
- References section at the bottom wires in all reference files with one-line summaries
- Uganda/UGX as default; universal frameworks always apply

**Reference file rules:**
- No line limit (reference files can be long)
- YAML frontmatter: `source`, `frameworks` (array), `skill`, `cross-reference` (array)
- Uganda/East Africa application section at the end of every file
- Generic names — no source prefix (e.g., `beef-butchery.md`, not `kenya-beef-butchery.md`)
- Before writing a new file, check whether an existing file covers the same source

See `skills/meta-utility/skill-writing/SKILL.md` for full authoring guidelines.

---

## Licence

See individual skill folders under `skills/` for licence information.
