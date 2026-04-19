# Business Plan Skills Suite

A modular collection of Claude Code skills for generating, validating, and delivering bankable business plans. Each section of a professional business plan is a standalone skill — invoke individually or chain to produce a complete investor-ready document.

**40 skills.** Default context: Uganda / East Africa (UGX). All frameworks are universally applicable; country-specific data swaps via the `country-context/` system.

---

## What This Suite Does

| Need | Skills to Use |
|---|---|
| Write a complete business plan | `01` through `15` (in order) |
| Write a specific section | Invoke the numbered skill directly |
| Validate an existing plan | `meta-bankability-scoring` |
| Upgrade pricing / defend premium positioning | `meta-pricing-strategy` |
| Stress-test the financials | `meta-financial-stress-test` |
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

**Uganda / East Africa context:**
- IFC/World Bank: CPSD Uganda (2022), Human Capital Review (2025)
- UBOS: CPI, KEI, NPHC data
- RSM/Baker Tilly (2025): Uganda doing business guide
- UDB Environmental and Social Policy; NEMA Act; Employment Act 2006

---

## Skill Directory

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
| `meta-sustainability` | Mandatory sustainability pre-screen (Mode A) and audit (Mode C); Sustainability Readiness Score (5 dimensions); sector materialities; SDG alignment; IFC Performance Standards compliance for DFI applications |
| `meta-bankability-scoring` | CAMPARI 28-item checklist; bank loan readiness scoring; 12-point cross-section consistency audit |
| `meta-financial-stress-test` | 4-scenario stress model, Uganda historical shocks, DSCR stress test, Early Warning Dashboard |
| `meta-market-validation` | Validates market claims against real data; MECE issue trees; flags unsupported assumptions |
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
| `update-claude-documentation` | Documentation maintenance workflow |

### Book Extractions

Primary-source reference material stored in `book-extractions/`. Read these when a skill references them; they carry the detailed frameworks, scripts, and Uganda/EA adaptation notes.

| File | What It Contains |
|---|---|
| `kennedy-no-bs-price-strategy-extraction.md` | Kennedy/Marrs 9 Failures, 5 Propositions, Triangle of Preeminence, Hawaiian Fisherman, niche pricing, association principle, discount discipline, competing with free |
| `kennedy-no-bs-sales-success-extraction.md` | Kennedy 23 Strategies, Positioning-Not-Prospecting, 6-Step Sales Process, Takeaway Selling, Proof hierarchy |
| `kennedy-ultimate-sales-letter-extraction.md` | 28-step long-form system, Power of a Sequence, Hidden Benefit, Damaging Admission, Creative P.S. |
| `brunson-dotcomsecrets-ignite-extraction.md` | Secret Formula, Value Ladder, 3 traffic types, 7 phases of a lead, Star-Story-Solution (35 beats), OTO Bump, Perfect Webinar, Soap Opera + Seinfeld |

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

---

## Project Structure

```
business-plan-skills/
├── 00-plan-assembly/          # Plan assembly and funder identification
├── 01-executive-summary/      # Section 01 — Executive Summary
├── 02-company-overview/       # Section 02 — Company Overview
│   └── references/            # Mission/vision, legal structures, Uganda doing business
├── 03-products-services/      # Section 03 — Products & Services
│   └── references/            # Business models, pricing strategy, product lifecycle
├── 04-market-analysis/        # Section 04 — Market Analysis
│   └── references/            # Uganda macro, IFC/World Bank data, trade frameworks
├── 05-target-market/          # Section 05 — Target Market
│   └── references/            # Consumer demographics, segmentation
├── 06-competitive-analysis/   # Section 06 — Competitive Analysis
│   └── references/            # Porter, Ohmae, Teece, competitive metrics
├── 07-marketing-sales-strategy/  # Section 07 — Marketing & Sales
│   └── references/            # Kotler 6.0, social media, small business strategy
├── 08-operations-plan/        # Section 08 — Operations Plan
│   └── references/            # BPM lifecycle, value chain, Uganda operations
├── 09-management-team/        # Section 09 — Management Team
│   └── references/            # Leadership, Berkshire culture, Uganda labour market
├── 10-financial-projections/  # Section 10 — Financial Projections
│   └── references/            # Uganda tax, financial templates, IP framework
├── 11-funding-request/        # Section 11 — Funding Request
│   └── references/            # Valuation, term sheets, ESMP template
├── 11b-grant-proposal/        # Grant proposals (LogFrame, Theory of Change)
├── 12-risk-analysis/          # Section 12 — Risk Analysis
│   └── references/            # Uganda risk context, global trade risks, COSO
├── 13-implementation-timeline/ # Section 13 — Implementation Timeline
├── 14-ai-integration/         # Section 14 — AI Integration
│   └── references/            # AI economics, digital innovation strategy
├── 15-appendices/             # Section 15 — Appendices
│   └── references/            # Document templates, bank submission checklist
├── pitch-deck/                # Unified pitch deck skill (deck + delivery)
├── meta-pitch-preparation/    # Pitch strategy and frame control
│   └── references/            # Klaff STRONG method, McGowan Pitch Perfect
├── meta-presentation-design/  # Slide design and delivery coaching
│   └── references/            # Duarte, Gallo, Edwards, HBR presentation standards
├── meta-bankability-scoring/  # CAMPARI scoring and consistency audit
├── meta-due-diligence/        # DD readiness and OSINT competitor intelligence
├── meta-financial-stress-test/ # Scenario modelling and stress testing
├── meta-market-validation/    # Market claim validation and MECE analysis
├── meta-monitoring-evaluation/ # KPI dashboard and M&E frameworks
├── meta-quarterly-gameplan/   # 90-day action sprint planning
├── industry-guides/           # 13+ sector-specific reference guides
├── blog-idea-generator/       # Blog post idea generation
├── blog-writer/               # Blog post writing
├── content-writing/           # Business content writing
├── digital-marketing-strategy/ # Digital channel strategy
├── idea-testing/              # Business idea rapid validation
├── proposal-architect/        # Client proposal writing
├── east-african-english/      # Language and tone standards
├── language-standards/        # Cross-language writing quality
├── country-context/           # Country data overrides (template + country files)
├── skill-writing/             # Guide for authoring skills
├── skill-safety-audit/        # Safety validation for skills
├── update-claude-documentation/ # Documentation maintenance
└── CLAUDE.md                  # Project-wide authoring instructions
```

---

## Authoring Standards

Every skill follows this structure:

```
skill-name/
├── SKILL.md              # Required: YAML frontmatter (name, description) + skill content
└── references/           # Optional: supporting methodology, data tables, templates
    ├── framework-name.md # Each reference file covers one source or framework
    └── ...
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

See `skill-writing/SKILL.md` for full authoring guidelines.

---

## Licence

See individual skill folders for licence information.
