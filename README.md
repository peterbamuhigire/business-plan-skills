# Business Plan Skills Suite

A modular collection of Claude Code skills for generating, monitoring, and evaluating bankable business plans. Each section of a professional business plan is implemented as a standalone skill that can be invoked individually or chained to produce a complete investor-ready document.

## Purpose

These skills transform Claude into a specialised business strategist capable of:

- **Generating** complete, bankable business plans section by section
- **Validating** financial projections, market claims, and competitive positioning
- **Monitoring** plan execution through KPIs, M&E frameworks, and quarterly game plans
- **Stress-testing** assumptions to ensure plans survive investor scrutiny

## Methodology

Built on frameworks from six foundational business planning texts:

- **Bankable Business Plans** (Edward Rogoff) — investor-readiness criteria and scoring
- **On Target: The Book on Marketing Plans** (Palo Alto Software) — marketing and sales depth
- **Business Plans to Game Plans** (Jan B. King) — strategy-to-action conversion and M&E
- **Planning a Profitable Business for Dummies** — accessible financial planning
- **The Business Plan Workbook, 11th Ed.** (Colin Barrow) — structured workbook exercises
- **The Complete Book of Business Plans** (Hazelgren & Covello) — comprehensive templates

Updated for 2026 standards including mandatory AI integration planning.

## Skill Directory

### Core Plan Sections (invoke in order for a complete plan)

| # | Skill | Description |
|---|-------|-------------|
| 01 | `executive-summary` | The investor pitch — written last, presented first |
| 02 | `company-overview` | Mission, vision, legal structure, history, milestones |
| 03 | `products-services` | Value proposition, product lifecycle, IP, R&D pipeline |
| 04 | `market-analysis` | Industry analysis, TAM/SAM/SOM, trends, data sources |
| 05 | `target-market` | Customer personas, segmentation, buyer behaviour |
| 06 | `competitive-analysis` | SWOT, competitive matrix, moat and differentiation |
| 07 | `marketing-sales-strategy` | 4Ps, pricing model, channels, sales funnel |
| 08 | `operations-plan` | Supply chain, facilities, processes, technology stack |
| 09 | `management-team` | Team bios, org chart, advisory board, hiring plan |
| 10 | `financial-projections` | P&L, cash flow, balance sheet, break-even, assumptions |
| 11 | `funding-request` | The ask, use of funds, terms, exit/ROI strategy |
| 12 | `risk-analysis` | Risk matrix, mitigation strategies, contingency plans |
| 13 | `implementation-timeline` | Milestones, phased rollout, 90-day game plans |
| 14 | `ai-integration` | AI utilisation map, automation ROI, efficiency gains |
| 15 | `appendices` | Supporting documents, permits, contracts, data tables |

### Meta-Skills (analytical and operational tools)

| Skill | Description |
|-------|-------------|
| `meta-financial-stress-test` | Sensitivity analysis, scenario modelling, Monte Carlo |
| `meta-market-validation` | Validates market claims against real data, flags gaps |
| `meta-bankability-scoring` | Scores plan against investor/lender criteria |
| `meta-monitoring-evaluation` | Converts plan into KPI dashboard and M&E framework |
| `meta-quarterly-gameplan` | Converts annual strategy into 90-day action sprints |

### Utility Skills (pre-installed)

| Skill | Description |
|-------|-------------|
| `east-african-english` | Language and tone standard for East African markets |
| `skill-writing` | Guide for creating and extending skills |
| `skill-safety-audit` | Safety validation for new skills |
| `update-claude-documentation` | Documentation maintenance workflow |

## Usage

### Generate a complete business plan

Invoke skills sequentially (02 through 15, then 01 last):

```
Use the company-overview skill to generate section 2 for [Business Name]
```

### Validate an existing plan

```
Use the meta-bankability-scoring skill to evaluate this business plan
```

### Convert plan to action

```
Use the meta-quarterly-gameplan skill to create Q1 action items from this plan
```

## Installation

Copy skill folders into your Claude Code skills directory:

```
~/.claude/skills/
```

Or reference the project directory in your Claude Code configuration.

## Contributing

Each skill follows the standard Claude Code skill structure:

```
skill-name/
├── SKILL.md              # Required: skill definition and instructions
└── references/           # Optional: supporting methodology and templates
```

See the `skill-writing` skill for authoring guidelines.

## Licence

See individual skill folders for licence information.
