# Business Plan Skills Suite

**Business Plan Skills** (repository `business-plan-skills`) is a skills engine for writing and reviewing business plans, standalone marketing plans, strategy analyses and the policy documents that support them. It gives Claude Code and Codex a routed set of 137 active skills (134 under `skills/` and 3 country contexts) that turn a business question into a decision-ready document: a bankable or investor plan, a 12-month marketing plan, a strategic audit, a market-entry assessment, an exit-readiness programme, or a grant application. Uganda and East Africa are the default context (UGX, mobile money, local media, regulators and data-protection law), and a `country-context/` mechanism adapts the work to other markets.

The engine works the way a disciplined consulting team works. It starts with intake (including the client's strategy type and the places the business actually serves), scores the business model before drafting, builds evidence before prose, and separates verified facts from assumptions, estimates, projections and targets. Every objective must be specific, measurable, accurate, realistic, time-bound and applicable to the business, its location and its scope. Numbers must reconcile: the marketing budget equals the P&L marketing line, volumes match the financial model, and the funding ask matches the implementation plan. Plans are written with a section-by-section phrase bank and an anti-AI-slop gate so they read as specific, human, professional British English. The engine never invents market sizes, benchmarks or results, and it withholds words such as "bankable", "viable" or "investor-ready" until its evidence gates pass.

It helps founders and owner-managers who need a plan a lender or investor will take seriously; consultants and agencies who sell plans, marketing plans and strategy work and need a repeatable, premium method; NGO and programme leaders preparing grant cases and strategic plans; and lenders, investors and boards who want a structured way to test a plan. It helps by supplying the method (procedures, checklists, templates, decision rules and worked Ugandan examples), the routing between sections and sister engines (finance, research, design, social media, website, proposals), and the validators that stop a plan with unreconciled numbers, stale facts or vague objectives from being released.

## Capabilities

| Category | Skills | What it covers |
|---|---|---|
| `pipeline` | 49 | Numbered plan sections, `00-client-intake` through `16-sustainability-strategy` (with SaaS and AI sub-skills), run under `business-plan-orchestrator`; Section 07 follows the business-plan marketing section standard |
| `meta-strategy` | 22 | Plan orchestration, consulting synthesis, due diligence, critical-thinking checks, market validation (stage and model metrics), competitive analysis, governance, statistics, and the strategy-rigour set: strategic factor analysis (EFAS/IFAS/SFAS, TOWS), strategic audit, strategic options evaluation, business-model design and GEL scoring, international market entry, exit readiness |
| `meta-finance` | 12 | Bankability scoring (Rogoff criteria), valuation, financial stress testing, investment-committee red team, revenue recognition, SLA controls |
| `saas` | 11 | SaaS go-to-market, unit economics, lifecycle, pricing, valuation |
| `advisory-deliverables` | 7 | Standalone finance, procurement and HR policy manuals, internal controls and risk framework, governance charter, grants-management manual, M&E framework |
| `meta-utility` | 6 | Skill writing, skill safety audit, proposal architect, documentation updates, anti-ai-slop, ai-slop-audit |
| `writing-content` | 5 | AI prompt writer, blog idea generator, blog writer, content writing, premium commercial writing |
| `ict` | 4 | ICT-sector business plans and e-commerce diagnostics |
| `marketing-sales` | 4 | Standalone marketing plans (20-section architecture, SMART objective builder, location and scope calibration, Bullseye channel selection, advertising and media plan, sales and account coverage, marketing economics, KPI and control plan, quality gate), demand generation, demand forecasting, digital marketing strategy |
| `language` | 3 | East African English, language standards, writing quality with the business-plan, marketing-plan and article phrase banks |
| `meta-pitch` | 3 | Pitch deck, pitch preparation, presentation design |
| `meta-pricing-gtm` | 3 | Pricing strategy, premium go-to-market, website investment planning |
| `meta-reporting` | 2 | Board and investor reporting |
| `industry-guides` | 2 | Sector reference guides (agriculture, manufacturing, hospitality, retail and others as `guide.md` files, not all packaged as `SKILL.md`) |
| `meta-sustainability` | 1 | Sustainability strategy references |

Total: 134 `SKILL.md` files under `skills/` plus 3 under `country-context/` (137 active skills, as counted by `scripts/validate_skill_engine.py`).

## Installation

```
# Native Claude Code plugin
/plugin marketplace add https://github.com/peterbamuhigire/business-plan-skills
/plugin install business-plan@chwezi-business-plan

# npm-free, from a clone
git clone https://github.com/peterbamuhigire/business-plan-skills
cd business-plan-skills
./install.sh --scope project      # macOS/Linux/Git Bash
.\install.ps1 -scope project      # Windows PowerShell
```

`install.sh`/`install.ps1` delegate to the vendored `scripts/install-engine.js` (Node ≥18), which also supports `--dry-run` (prints the plan, writes nothing), `--json`, and `--scope user` (default, `~/.claude`) as an alternative to `--scope project` (`.claude` under the current directory).

This engine names its own sister engines directly in `AGENTS.md`'s Kaizen and finance-trigger rules — each is an independent, optional install, never a hard dependency. **`chwezi-accounting-doctrine`** is triggered whenever money flows, tax, payroll, grants, reconciliation, or any IFRS/IFRS-for-SMEs section arises in a plan; this repository's own `meta-finance/` skills explicitly defer accounting close, audit, and controls to it. **`digital-research-skills`** (local checkout `digital-research-engine`) is where `AGENTS.md` routes "current external claims" — the source-register verification a bankable plan's market and benchmark figures need. **`design-system-skills`** is routed to for all font/typeface, layout, colour, and visual-formatting decisions on decks, DOCX, PPTX, and XLSX deliverables, per the engine's own design-trigger block in `CLAUDE.md`.

## Content integrity

This repository contains no client names, client data, or project-specific
work product; client, project, and proposal-workspace directories are
excluded from version control by design (see `.gitignore`). Users
installing this engine should still exercise their own due diligence — you
can ask Claude Code or Codex to run a security scan of this engine, its
skills, and its reference files before relying on it in a sensitive
environment (for example: "scan this repository for hardcoded secrets,
personal paths, or unexpected network calls").

## References

- Mustafa, A. et al. *Everything Claude Code* (ECC). GitHub: affaan-m/ECC, 2026. This engine adapts several ECC skills directly: `skills/pipeline/00-client-intake/SKILL.md` states its Question 7 diagnostic and a "Golden Rule" section are "adapted from" ECC's `investor-materials` and `product-lens` skills; `skills/meta-strategy/benchmark-methodology/SKILL.md`, `skills/meta-strategy/competitive-platform-analysis/SKILL.md`, and `skills/meta-strategy/competitive-report-structure/SKILL.md` each declare `origin: ECC (skills/<name>/SKILL.md), adapted for` business-plan use in their frontmatter.
- Kennedy, Dan S. and Marrs, Jason. *No B.S. Price Strategy: The Ultimate No Holds Barred, Kick Butt, Take No Prisoners Guide to Profits, Power, and Prosperity* (Entrepreneur Press, 2011). Cited in `CLAUDE.md` as the basis for `meta-pricing-strategy` and the 9 Failures/5 Propositions pricing audit; method now at `skills/meta-pricing-gtm/meta-pricing-strategy/references/price-strategy-audit-and-proposition-stack.md`.
- Kennedy, Dan. *No B.S. Sales Success: The Ultimate No Holds Barred, Kick Butt, Take No Prisoners, Tough and Spirited Guide* (Entrepreneur Press, 3rd ed. 2004; original 1994). Method now at `skills/pipeline/07-marketing-sales-strategy/references/direct-response-selling-playbook.md`.
- Kennedy, Daniel S. *The Ultimate Sales Letter: Boost Your Sales with Powerful Sales Letters, Based on Madison Avenue Techniques* (Adams Media, 1st ed. 1991; 2nd ed. 2000; 4th ed. 2011). Method now at `skills/pipeline/07-marketing-sales-strategy/references/long-form-sales-letter-build.md`.
- Kennedy, Dan S. and Walsh-Phillips, Kim. *Magnetic Marketing: How to Attract a Flood of New Customers That Pay, Stay, and Refer* (ForbesBooks, 2018). Cited in `CLAUDE.md` for attraction/conversion/retention/referral go-to-market logic; method now at `skills/pipeline/07-marketing-sales-strategy/references/direct-response-commercial-system.md`.
- Brunson, Russell. *Proven Secrets to Double Your Traffic, Conversion & Sales for Any Product or Service Online* (SuccessEtc LLC / DotComSecrets Ignite). Method now at `skills/pipeline/07-marketing-sales-strategy/references/funnel-and-value-ladder-design.md`.
- Haines, Steven. *How to Create a Business Case* (2022). Cited in `CLAUDE.md` as the basis for the business-case test (problem, options, do-nothing case, incremental economics, timing, sensitivity) applied to major systems, digitisation, expansion, or automation recommendations; method now at `skills/meta-strategy/meta-critical-thinking-business-logic/references/business-case-test.md`.

Books added in the September 2026 marketing and strategy Kaizen (methods paraphrased into task-oriented references; no book text is stored):

- Abrams, Rhonda M. *The Successful Business Plan: Secrets & Strategies*, 2nd edn (The Oasis Press, 1993). Target-market tests and lenses, weighted competitor grids, Five F's, sales worksheets and flow-through reconciliation in `skills/marketing-sales/marketing-plan-orchestrator/references/`; executive-summary form choice in `01-executive-summary`; five-minute reader test in `meta-investment-committee-red-team`.
- Barrow, Colin. *Get Backed, Get Big, Get Bought* (Capstone, 2009). Exit readiness and sale preparation in `skills/meta-strategy/meta-strategic-optionality/references/exit-readiness-and-sale-preparation.md`; adoption and commission checks in the marketing references.
- Croll, Alistair and Yoskovitz, Benjamin. *Lean Analytics* (O'Reilly Media, 2013). One metric that matters, lines in the sand, stage and business-model metrics in `skills/meta-strategy/meta-market-validation/references/lean-analytics-stage-and-model-metrics.md` and the orchestrator's KPI and control plan.
- Debelak, Don. *Business Models Made Easy* (Entrepreneur Press, 2006). Business-model design and GEL scoring in `skills/meta-strategy/meta-business-model-design/`.
- Debelak, Don. *Perfect Phrases for Business Proposals and Business Plans* (McGraw-Hill, 2006). Section-by-section phrase banks and the `strategy_type` field in `skills/language/writing-quality/references/business-plan-phrase-bank.md` (with its section files) and `marketing-plan-phrase-bank.md`.
- Johnson, Gerry; Whittington, Richard; Scholes, Kevan; Angwin, Duncan and Regnér, Patrick. *Exploring Strategy*, 11th edn (Pearson, 2017). PESTEL key drivers, SAFe, strategy clock, low-cost-rival response, strategy statement gate, CAGE and institutional voids in `meta-strategic-factor-analysis`, `meta-strategic-options-evaluation` and `meta-international-market-entry`.
- Kelley, Larry D. and Sheehan, Kim Bartel. *Advertising Management in a Digital Environment: Text and Cases* (Routledge, c. 2021). Budget triangulation, creative brief, positioning checks and measurement architecture in the orchestrator's advertising and media plan.
- Lin, Lewis C. *Decode and Conquer*, 2nd edn (Impact Interview, 2013). Estimation driver trees in `04-market-analysis/references/estimation-trees-and-sanity-checks.md`; pricing triangle and price-change P&L in `03-products-services/references/pricing-triangle-and-price-change-pnl.md`.
- Marcos, Javier; Guesalaga, Rodrigo; Hough, Andrew and Vincent, Richard. *The High-Performing Key Account Manager* (Kogan Page, c. 2025). Research-backed key-account typology only, in the orchestrator's sales plan and account coverage reference.
- Hunter, Victor L. with Tietyen, David. *Business to Business Marketing: Creating a Community of Customers* (NTC Business Books, 1997). Account grading, contact matrix, allowable cost per lead and market-at-risk in the orchestrator's sales and economics references.
- Stockwell, John and Shaw, Henry M. *Direct Marketing Checklists* (NTC Business Books, 1994). Campaign pro-forma P&L, break-even response rate, cost per interested thousand and goal hierarchy in the orchestrator's economics, media and objectives references.
- Stutts, Phillip. *The Undefeated Marketing System* (Lioncrest/Scribe, 2021). Research → plan → creative → test → launch sequencing gate, customer insights report, message themes and war-room cadence in the orchestrator.
- Weinberg, Gabriel and Mares, Justin. *Traction: A Startup Guide to Getting Customers* (S-curves Publishing, 2014). Bullseye across 19 channels and the critical path in `traction-channel-bullseye.md`.
- Wheelen, Thomas L.; Hunger, J. David; Hoffman, Alan N. and Bamford, Charles E. *Concepts in Strategic Management and Business Policy*, 15th edn (Pearson, 2018). EFAS/IFAS/SFAS on a 1–5 scale, the strategic audit and the control-plan table in `meta-strategic-factor-analysis`, `meta-strategic-audit` and the orchestrator's KPI and control plan.
- Skimmed for business-plan relevance only: Wiebe, Joanna. *Copy Hackers: 6 Persuasion Strategies* (Copy Hackers, 2011); Maltz, Maxwell et al. *Zero-Resistance Selling* (Prentice Hall Press, 1998); Kupsh, Joyce and Graves, Pat R. *How to Create High-Impact Business Presentations* (NTC Business Books, 1993); Serling, Bob (ed.) *How to Write Million Dollar Ads, Sales Letters & Web Marketing Pieces* (The Internet Marketing Center, 2002; the source file was mislabelled as a Peng Joon title).


The former `book-extractions/` folder was removed on 2026-09-23 because storing book extractions in the repository infringes copyright. Its durable methods now live as task-oriented, paraphrased references inside the owning skills (for example Rogers, Molenaar, and e-commerce models in `skills/meta-strategy/meta-digital-transformation/references/digital-business-model-redesign-tests.md`; Godin in `skills/pipeline/07-marketing-sales-strategy/references/niche-first-positioning-test.md`; Golding on multi-tenant SaaS in `skills/pipeline/08-operations-plan/references/saas-tenancy-model-and-msp-trap-test.md`; van der Kooij on SaaS sales in `skills/saas/saas-sales-org-design-and-capacity-planning/references/saas-sales-methodology-and-conversation-craft.md`), each with a brief source citation.

## Capability map

The suite routes and validates business-plan work. The state of an output is
separate from the existence of a route or template; see the [Wave 1 evidence
report](docs/continuous-improvement/kaizen-wave-1-2026-08-11.md) for the dated
inventory and residual gaps.

| Output family | Tracked evidence | Wave 1 state |
|---|---|---|
| Business-plan narratives and decision packs | Fictional Markdown plans, evidence manifests, committee records, and release bundles under [`examples/full-plan-packages/`](examples/full-plan-packages/) | Generated and structurally validated by [`validate_exemplar_packs.py`](tools/exemplar-packs/validate_exemplar_packs.py); client or authority evidence is not implied. |
| Financial models and planning workbooks | XLSX templates under `skills/` | Generated and workbook-validated by [`verify_workbooks.py`](scripts/build-financial-models/verify_workbooks.py); production/client fitness remains not assessed. |
| Pitch and presentation material | Markdown deck outlines in the fictional exemplar packs | Generated as source text; native PPTX generation, rendering, and visual inspection are **NOT ASSESSED**. |
| DOCX and PDF deliverables | No tracked native DOCX or PDF artefact in this repository baseline | **NOT ASSESSED**; do not infer editability, accessibility, pagination, or print fidelity from Markdown. |
| External release | Release-bundle schemas and blocker-first validator | **BLOCKED** until required research, finance, spreadsheet, design, document, security, render, reviewer, and authority evidence is present. |

The engine provides decision support, not automatic approval. A plan is not
called bankable, investor-ready, achievable, compliant, or submission-ready
unless the required evidence, financial logic, professional reviews, and
release authority are present.

## How to route work

## Prompt-generation capability — 2026-09-17

This release adds evidence-first candidate testing, failure-slice review, and explicit `NOT_ASSESSED` handling for volatile prompt claims.

The engine now generates decision-ready prompts that bind objective, evidence
boundary, assumptions, financial/implementation constraints, output format,
acceptance checks, and safe refinement through the local [domain prompt
contract](docs/ai-prompting/domain-prompt-compilation-contract.md). A forked
engine retains this capability without the portfolio checkout.

For execution across phases, use the runtime-neutral [orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md), dated 2026-09-07. It defines scoped work packages, evidence checkpoints, context hygiene, least agency, and sanitized handling of external content while preserving Claude and Codex runtime capabilities.

For a serious engagement, start with `skills/meta-strategy/business-plan-orchestrator/SKILL.md`. It controls intake, evidence design, stage dependencies, handoffs, model reconciliation, challenge gates, assembly, and release. Use `skills/pipeline/00-plan-assembly/SKILL.md` only for final ordering and packaging.

| Need | Primary route | Add when triggered |
|---|---|---|
| Full business plan | `skills/meta-strategy/business-plan-orchestrator/` | Country, sector, finance, valuation, sustainability, digital, website, execution, and audience routes |
| Feasibility or business case | `skills/meta-strategy/meta-critical-thinking-business-logic/` and the relevant pipeline sections | `meta-market-validation`, `meta-finance`, sector gates, and investment-case evidence |
| Standalone marketing plan | `skills/marketing-sales/marketing-plan-orchestrator/` | SMART objective builder, location and scope calibration, Bullseye, advertising and media plan, sales plan, economics, KPI and control plan, quality gate; digital marketing and advertising engine (social-media-skills) for detailed media plans, creative briefs, build specs and attribution; Chwezi finance for budget reconciliation |
| Business-plan marketing section | `skills/pipeline/07-marketing-sales-strategy/` | Business-plan marketing section standard and the orchestrator's references |
| Strategy analysis and choice | `skills/meta-strategy/meta-strategic-factor-analysis/`, `meta-strategic-options-evaluation/`, `meta-strategic-audit/` | `meta-business-model-design` before drafting; `meta-international-market-entry` for cross-border entry; `meta-strategic-optionality` for exit readiness |
| Market validation | `skills/meta-strategy/meta-market-validation/` | Customer research, interviews, experiments, channel evidence, and claim-level source verification |
| Build-Measure-Learn | `skills/meta-strategy/meta-market-validation/` and `skills/meta-strategy/meta-living-plan-governance/` | Small reversible tests, innovation accounting, leading indicators, counter-metrics, and pivot/stop rules |
| Nonprofit strategic planning | `skills/pipeline/` plus `skills/advisory-deliverables/me-framework-document/` | Governance, stakeholder, mission, resource, donor, safeguarding, and M&E requirements |
| Facility move or major operating change | `skills/pipeline/13-implementation-timeline/` and `skills/pipeline/08-operations-plan/` | Charter, decision rights, readiness, continuity, inventory, capacity, cutover, stabilisation, and closeout evidence |
| M&E and execution | `skills/meta-strategy/meta-monitoring-evaluation/` and `meta-quarterly-gameplan/` | Living-plan governance, KPI definitions, owners, cadence, thresholds, and decision logs |
| Financial projections | `skills/pipeline/10-financial-projections/` | <a href="https://github.com/peterbamuhigire/chwezi-accounting-doctrine" target="_blank" rel="noopener noreferrer">Chwezi Accounting Doctrine</a>, finance review, workbook audit, stress tests, tax and regulatory verification |
| Local operational readiness | `skills/meta-strategy/meta-operational-readiness-due-diligence/` | Ten-point banking, tax, licensing, payroll, FX, compliance-calendar, logistics, privacy, government-interface, and partnership readiness matrix |
| SaaS or recurring revenue | `skills/saas/` and the relevant pipeline sections | Cohorts, CAC/LTV, retention, NRR, Rule of 40, ARR waterfall, COGS, pricing, and valuation |
| AI-enabled business | `skills/pipeline/14-ai-integration/` and relevant SaaS skills | Problem-first AI selection, system and data risks, evaluation, AI cost, governance, drift, and human oversight |
| Digital transformation | `skills/meta-strategy/meta-digital-transformation/` | Capability maturity, operating-model change, investment logic, sequencing, adoption, and benefits realisation |
| Pitch or presentation | `skills/meta-pitch/` | <a href="https://github.com/peterbamuhigire/design-system-skills" target="_blank" rel="noopener noreferrer">Design System Skills</a> for visual design and <a href="https://github.com/peterbamuhigire/digital-research-skills" target="_blank" rel="noopener noreferrer">Digital Research Engine</a> for current evidence |
| Proposal, tender, EOI, or RFP | Route to <a href="https://github.com/peterbamuhigire/proposal-skills" target="_blank" rel="noopener noreferrer">Proposal Skills</a> | Add this engine for the business case, commercial model, finance, or implementation content |
| Hotel, resort, lodge, inn, guest house, restaurant, bar, catering, or venue plan | `skills/industry-guides/hospitality-hotel-restaurant/SKILL.md` plus `skills/industry-guides/hospitality-tourism/` and `skills/industry-guides/restaurant/` | Add Chwezi finance, current country/regulatory research, and requirements/engineering routes where systems or statutory claims appear |

Use the smallest route that can answer the decision. Do not load every skill by default; add country, sector, funding, finance, design, document, website, accounting, or research overlays only when the engagement triggers them.

## The Kaizen operating contract

Latest local improvement evidence: [2026-09-06 Kaizen](docs/audits/2026-09-06-kaizen.md).

For a ready-to-run product or project operation, use [`prompts/full-kaizen-operation.md`](prompts/full-kaizen-operation.md).

Continuous improvement is part of the engine itself and part of every product it produces. The governing skill is `skills/meta-strategy/kaizen-improvement-system/SKILL.md`, supported by `docs/continuous-improvement/kaizen-adoption-2026-08.md` and the portfolio standard maintained by the <a href="https://github.com/peterbamuhigire/digital-research-skills" target="_blank" rel="noopener noreferrer">Digital Research Engine</a>.

Every engine or product improvement follows this cycle:

```text
Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure
```

### Engine audits

An engine audit reviews doctrine, taxonomy and routing, skill depth, applied proof, currency, output readiness, inclusion, production fidelity, hygiene, and integrity. It must identify:

- The scope, date, evidence, assumptions, and unavailable checks.
- A raw diagnostic score and the reason for each dimension result.
- The published score as `min(raw score, 65)`. **65/100 is a reporting ceiling, not a pass mark or a waiver.**
- Blockers, root causes, owners, experiments, measures, rollback conditions, and re-audit dates.
- A remediation plan whose target score is **95/100**.

### Product audits

The same contract applies to a business plan, feasibility study, market analysis, nonprofit strategy, facility-move plan, financial model, pitch, dashboard, or implementation framework. Test the product's:

- Decision thesis, audience, stakeholder or beneficiary logic, and intended use.
- Claim-and-evidence register, source freshness, assumptions, confidence, and countercases.
- Customer, market, revenue, cost, operating, capacity, funding, and implementation logic.
- Financial reconciliation, scenarios, cash implications, risk controls, and professional-review state.
- M&E indicators, owners, cadence, targets, counter-metrics, refresh triggers, and decision rules.
- Production, rendering, accessibility, design, security, spreadsheet, document, and release evidence where applicable.

An unavailable source, reviewer, tool, render, or professional check is `not assessed`; it is never silently treated as passed. Successful changes are standardised in a skill, reference, template, fixture, or operating record and then re-measured.

## Business-plan workflow

1. **Intake and decision framing** - define the decision, audience, jurisdiction, business stage, funding instrument, scope, authority, constraints, and deliverable family.
2. **Evidence design** - create a claim register and evidence plan before drafting. Separate verified facts, management assumptions, estimates, inferences, unknowns, and hypotheses.
3. **Validation and options** - test the most consequential demand, customer, channel, delivery, capability, regulatory, and financial assumptions. Compare the base case with credible alternatives and a do-nothing or downside case.
4. **Section production** - draft only the required pipeline sections, preserving shared assumptions and returning conflicts to their owning section.
5. **Integrated model** - reconcile narrative, drivers, operating plan, use of funds, milestones, cash flow, income statement, balance sheet, scenarios, and funding need.
6. **Challenge and handoffs** - run business-logic, evidence, finance, regulatory, sector, risk, valuation, design, document, spreadsheet, security, and audience-specific gates as applicable.
7. **Assembly and release** - assemble approved versions, populate the release-evidence bundle, validate it, render layout-sensitive artefacts, retain reviewer evidence, and require explicit release authority.
8. **Learning and refresh** - record what changed, what was learned, which assumptions moved, what was standardised, and when the plan or quarterly gameplan will be revisited.

## Build-Measure-Learn and living plans

Market validation is not a decorative appendix. The engine converts material assumptions into testable hypotheses:

| Element | Required treatment |
|---|---|
| Hypothesis | State the customer, problem, offer, behaviour, value, or growth assumption and the decision it controls. |
| Small test | Use the smallest ethical, reversible experiment that can produce useful evidence. |
| Measure | Define a leading indicator, lagging outcome, threshold, time window, sample or denominator, and counter-metric. |
| Learning | Classify the result as supports, weakens, mixed, or does not test the hypothesis. Do not equate activity with validation. |
| Decision | Continue, revise, pivot, pause, or stop; state the consequence for the plan and model. |
| Standardisation | Keep only evidence-backed changes, assign an owner and cadence, and record the next review trigger. |

Living-plan outputs retain a data feed, owner, cadence, decision log, variance threshold, refresh trigger, and sunset or stop condition. Monthly learning loops feed quarterly plan refreshes; quarterly refreshes do not replace annual strategic review.

## Nonprofit planning and M&E

Nonprofit routes add readiness and governance before strategy drafting. They make mission, stakeholder needs, board and management roles, beneficiary outcomes, resource constraints, donor restrictions, implementation capacity, and approval authority explicit.

M&E work defines a results chain, baseline, indicators, disaggregation where relevant, data source, collection frequency, owner, quality check, target, counter-metric, learning question, escalation threshold, and decision use. A dashboard is not evidence of impact unless definitions, data quality, denominator, timing, and interpretation are documented.

The strategic plan should include implementation ownership, review cadence, annual or event-triggered refresh rules, and a record of what was learned and changed. Publisher templates and illustrative nonprofit examples are methods, not proof about a particular organisation or community.

## Facility moves and operational change

Facility-move logic is reusable for relocations, ERP changes, infrastructure migrations, branch openings, operating-model changes, and continuity-sensitive transitions. The plan should expose:

- Charter, scope, decision rights, dependencies, success criteria, and authority.
- Current-state baseline, asset and process inventory, readiness, capacity, quality, safety, regulatory, and continuity risks.
- Future-state operating design, integrated schedule, procurement and resource needs, communications, testing, and contingency paths.
- Cutover entry criteria, go/no-go decision, rollback or fallback, stabilisation monitoring, issue ownership, and closeout.
- Lessons learned, standard work, residual risks, benefits evidence, and the next improvement cycle.

## Financial logic and accounting routing

This engine handles financial modelling and business-plan financial logic; it is not a substitute for accounting doctrine or professional sign-off.

For financial work, route to the <a href="https://github.com/peterbamuhigire/chwezi-accounting-doctrine" target="_blank" rel="noopener noreferrer">Chwezi Accounting Doctrine</a> whenever the engagement touches money flows, inventory, payroll, tax, grants, banking, mobile money, POS, fixed assets, statutory reporting, journals, reconciliations, period close, controls, audit evidence, IFRS/IAS, or finance-system integration. Read the relevant Chwezi doctrine, skill, and finance quality gate, and record the handoff.

Financial outputs should reconcile:

- Commercial drivers to revenue, volume, price, timing, churn, and collection assumptions.
- Operating drivers to headcount, capacity, productivity, procurement, inventory, quality, and delivery costs.
- Income statement, cash flow, balance sheet, working capital, funding need, and use of funds.
- Base, upside, downside, sensitivity, break-even, runway, DSCR, covenant, and liquidity cases where relevant.
- Revenue recognition, deferred revenue, refunds, SLA credits, AI COGS, grants, tax, and control implications where triggered.

Use `tools/workbook-audit/formula_map.py` for XLSX formula and reconciliation evidence. Never plug a model to force it to balance; isolate the broken schedule, identify the owner, and mark the affected conclusion unassessed until recovered.

## Evidence, research, and current claims

All current market, country, tax, regulatory, platform, legal, safety, pricing, exchange-rate, or benchmark claims must be verified through the <a href="https://github.com/peterbamuhigire/digital-research-skills" target="_blank" rel="noopener noreferrer">Digital Research Engine</a>. The engine's source register and evidence discipline distinguish:

- Source discovery from claim-level verification.
- An official portal from proof of a copied figure.
- A historical source from a current standard.
- A book's method from evidence about the client or market.
- A model assumption from an observed fact.
- An unavailable review from a passed review.

Before release, check `docs/source-registers/country-market-data.json`, apply `references/sector-regulatory-gates.json` or the linked sector gate, and retain dated claim-level evidence. Current statutory, tax, accounting, legal, and professional judgements remain subject to the relevant authority or qualified reviewer.

## What the 16-book study changed here

The book-derived upgrade is recorded in the <a href="https://github.com/peterbamuhigire/digital-research-skills/blob/main/docs/continuous-improvement/book-study-2026-08.md" target="_blank" rel="noopener noreferrer">Digital Research Engine book study</a> and this engine's `docs/continuous-improvement/kaizen-adoption-2026-08.md`.

- **LEAN: Ultimate Collection** informed Build-Measure-Learn, validated learning, innovation accounting, KPI cadence, waste and value analysis, experiments, progressive implementation, and learning-organisation practices. It is a compilation with uneven source quality; original authoritative sources govern exact definitions.
- **Applying the Kaizen in Africa** informed participatory and incremental improvement, PDCA, 5S, muda reduction, QC Story, standardisation, management commitment, on-site observation, and institutional sustainability. African cases guide adaptation; they do not guarantee results in a client setting.
- **The Nonprofit Guide to Strategic Planning** strengthened readiness, governance, stakeholder analysis, baseline, options and trade-offs, resource implications, implementation cadence, KPI review, and refresh triggers.
- **Facility Move Playbook** strengthened change charters, continuity, readiness, inventory, capacity, cutover, stabilisation, closeout, and lessons-learned patterns.
- **Paid for Your Perspective** strengthened expert positioning, buyer needs, preparation, compliance screening, evidence-bounded advisory work, follow-up, and knowledge-product routes.
- **XP 2026** contributed current Agile learning themes such as value retrospectives, experimentation, team autonomy, architecture uncertainty, UX pilots, and evidence-led adoption. Specific research findings require source-aware use.
- **Platform Enterprise** contributed platform-as-product, user and team feedback, sociotechnical capability, ownership, maintenance, and sustainable operating-model thinking. Only the available early-release chapters were admitted.
- **Designing for AI** contributed problem-first AI selection, system-centred business cases, human/AI/system layers, data and inference transparency, oversight, drift, and rollback thinking. Only the available early-release chapters were admitted and legal claims require independent verification.

The two unreadable extractions, *Kaizen and the Art of Creative Thinking* and *Anatomy for Artists*, were not used to invent business-plan guidance. Historical, partial, duplicated, or practical books are treated as method inputs, not current legal, market, technical, financial, or professional authority.

## September 2026 book-driven Kaizen wave

See [`docs/continuous-improvement/book-driven-kaizen-2026-09-01.md`](docs/continuous-improvement/book-driven-kaizen-2026-09-01.md) for the AI/data-foundation, health-trust, and NGO cyber-resilience additions.

## Repository architecture

```text
skills/
|-- pipeline/                 # Numbered plan sections and final assembly
|-- meta-strategy/            # Orchestration, validation, living plans, M&E, Kaizen
|-- meta-finance/             # Bankability, valuation, stress tests, finance review
|-- meta-pitch/               # Pitch and presentation routes
|-- meta-pricing-gtm/         # Pricing, premium GTM, website investment planning
|-- meta-reporting/           # Board and investor reporting
|-- saas/                     # SaaS, recurring revenue, cohorts, pricing, valuation
|-- ict/                      # ICT product, services, ecommerce, and cross-border routes
|-- industry-guides/          # Sector operating and business-plan guidance
|-- advisory-deliverables/    # Policies, governance, grants, controls, and M&E artefacts
|-- marketing-sales/          # Demand, channels, and digital marketing
|-- writing-content/          # Business writing and content production
|-- language/                 # East African English and writing quality
`-- meta-utility/             # Skill authoring, safety, anti-slop, and documentation
country-context/              # Country-specific overrides and evidence-linked routes
docs/                         # Quality, source registers, release, and improvement records
tools/                        # Evidence, sector, workbook, exemplar, and release gates
tests/                        # Routing and regression tests
```

Skills are portable directories under `skills/**/SKILL.md` and `country-context/**/SKILL.md`. Each active skill must meet the repository's July 2026 contract: directory-matching identity, portable metadata, positive and negative triggers, input/output/evidence contracts, ordered workflow with stop and recovery behaviour, decision rules, permission boundaries, degraded mode, quality standards, concrete anti-patterns, and directly linked references. The baseline is a regression lock, not a waiver.

## Validation commands

Run from the repository root in PowerShell:

```powershell
# Structural and contract validation
python -X utf8 scripts\validate_skill_engine.py --baseline docs\quality\skill-quality-baseline.json

# Routing precision; the repository threshold is 100% top-three precision
python -X utf8 scripts\routing_smoke_test.py --threshold 1.0

# Validate one changed skill
python -X utf8 skills\meta-utility\skill-writing\scripts\quick_validate.py <skill-directory>

# Source, country, and sector evidence
python -X utf8 scripts\source_ingestion_guardrail.py
python -X utf8 tools\evidence-register\refresh_evidence_register.py --check
python -X utf8 tools\sector-gates\validate_sector_gates.py

# Marketing objective check (vague-goal fixtures) and content-aware source guard
python -X utf8 tools\objective-check\check_objectives.py <objectives.json>
python -X utf8 scripts\source_ingestion_guardrail.py    # content warnings are report-only; add --strict-content to block

# Exemplar, workbook, release, and regression checks
python -X utf8 tools\exemplar-packs\validate_exemplar_packs.py
Get-ChildItem examples\full-plan-packages -Directory | ForEach-Object { python -X utf8 tools\release-gate\validate_release_bundle.py "$($_.FullName)\release-bundle.json" }
python -X utf8 -m unittest discover -s tests -p "test_*.py"
git diff --check
```

For financial workbooks, also run:

```powershell
python -X utf8 tools\workbook-audit\formula_map.py <workbook.xlsx> --output <formula-report.json>
```

The release gate remains blocked by missing mandatory research, finance, spreadsheet, design, document, security, render, reviewer, or authority evidence. Automated validators do not replace claim verification, professional judgement, visual review, or authorised release.

## Evidence limitations and safety boundaries

- The engine does not fabricate market size, growth, benchmark, customer, regulatory, tax, exchange-rate, or legal facts.
- A source register identifies what must be checked; it does not prove the underlying claim without claim-level verification.
- Country defaults are starting context, not current evidence.
- Fictional exemplars are structural teaching aids; replace every fact, assumption, source, and model input before client use.
- Book-derived methods are not automatically current standards, professional advice, or evidence about a particular enterprise.
- The 65/100 audit ceiling does not mean an engine or product is acceptable. It forces an honest capped baseline and a visible plan toward 95/100.
- Missing evidence, unavailable tools, unavailable reviewers, and unresolved professional judgements remain `not assessed` and narrow the conclusion.
- Finance, tax, accounting, legal, regulatory, safeguarding, and other professional conclusions require the applicable doctrine, authority, or qualified reviewer.
- Design and visual-formatting work routes to <a href="https://github.com/peterbamuhigire/design-system-skills" target="_blank" rel="noopener noreferrer">Design System Skills</a>; content and business logic remain here.
- Proposal, website, social-media, software, Linux, research, accounting, and design work routes to their canonical sibling engines when triggered. Do not copy or mirror those engines into this repository.

## Contribution and release discipline

Read `AGENTS.md` and `CONTRIBUTING.md` before changing the engine. Preserve existing skills, prefer improving an overlapping skill over creating a duplicate, keep long frameworks in directly linked references, and update the source register, fixtures, baseline, evaluation record, or release bundle when the capability changes.

Before a release:

1. Fetch and check that local `main` is not behind its remote.
2. Run the repository, routing, canonical, evidence, syntax, workbook, release, test, and diff checks applicable to the change.
3. Inspect the complete diff for unrelated files, secrets, generated caches, and accidental deletions.
4. Update the active count and evidence from machine output.
5. Stage only intended files, inspect the staged diff, commit once, and push without force.

See `AGENTS.md` for the complete routing and quality contract.

## September 2026 marketing and strategy Kaizen

The marketing-plan orchestrator now produces a full standalone marketing plan: a 20-section document architecture, a SMART objective builder with a pass-or-fail quality test and worked UGX cascades, location and scope calibration (Uganda and East Africa defaults, data-protection registration, consent and direct-marketing objection rules from the dated currentness register), Bullseye channel selection across 19 channels, an advertising and media plan with budget triangulation, a sales and account-coverage method, marketing economics (CLV, affordable cost per lead, break-even response rate, budget reconciled to the P&L), a KPI and control plan, evidence discipline and a quality gate. Section 07 follows a business-plan marketing section standard that draws on those references. Five strategy skills were added (factor analysis, strategic audit, options evaluation, business-model design, international market entry) and exit readiness was added to `meta-strategic-optionality`. A section-by-section phrase bank and a `strategy_type` intake field support human, specific plan wording. The `book-extractions/` folder was removed with a zero-loss capability map; see the change and check ledgers for this wave.

## September 2026 Kaizen execution update

The bounded first wave adds a synthetic lender trace fixture and
`tools/evidence-register/validate_plan_trace.py`. It checks that source IDs,
assumptions, model cells, decision outputs and reviewer fields remain linked;
the new tests cover valid, missing-source and broken-link cases. The full
repository test suite passes 33 tests. This proves fixture and validator
mechanics only. No lender decision, client workbook, funding outcome or
professional finance review is implied. The next step is an independently
recalculated disposable workbook before rendering or widening the audience.

## September 2026 Kaizen Phase 1 references

The bounded Phase 1 contract set adds source-status-aware references for FP&A
assumption tracing and manager financial intelligence, business-agility
readiness, strategy-map scorecards, healthcare payer volume-to-cash
reconciliation, and healthcare workforce learning and cost/capacity scenarios.
The examples use synthetic values only. Deterministic checks live in
`tests/test_phase1_kaizen_contracts.py` with
`tests/fixtures/phase1-kaizen-contracts.json`. Current payer, statutory,
clinical, salary, market, and benchmark evidence remains a separate
currentness-gated review; missing evidence is `not_assessed`.

## Licence

See the individual skill folders for licence information.
