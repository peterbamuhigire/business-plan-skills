# Business Plan Skills Suite

The Business Plan Skills Suite turns a defined business, investment, nonprofit, feasibility, or operating-change question into a decision-ready plan, model, or pack through evidence, explicit assumptions, reconciled financial logic, and staged execution choices. It develops the work section by section and decision by decision, preserving the detail a founder, lender, investor, grant-maker, or delivery owner needs to challenge, fund, and operate the plan.

Founders, management teams, advisers, analysts, nonprofit leaders, investors, lenders, grant applicants, and delivery owners use it to clarify decisions, test material assumptions, reconcile commercial and financial logic, and plan execution. The workflows organise work across `skills/`, `country-context/`, examples, templates, and validation tools without treating a generic template as evidence about a particular organisation or market.

Used with project-specific evidence, the suite produces clearer choices, explicit assumptions, traceable financial and implementation logic, and a defined review and release path. It provides planning methods and validation structure, not automatic approval, professional accounting or legal sign-off, or current market facts; its agent roles, lifecycle hooks, evidence contract, and stop/recovery behaviour are documented in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md), while formal software requirements and lifecycle documentation belong with the <a href="https://github.com/peterbamuhigire/srs-skills" target="_blank" rel="noopener noreferrer">SRS Skills engine</a> when triggered.

The default planning context is Uganda and East Africa, with UGX as the default currency. The methods are portable: country, sector, currency, audience, funding instrument, and regulatory context must be changed through evidence-backed project inputs rather than assumed from this default.

## Output capability and evidence state

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

For a serious engagement, start with `skills/meta-strategy/business-plan-orchestrator/SKILL.md`. It controls intake, evidence design, stage dependencies, handoffs, model reconciliation, challenge gates, assembly, and release. Use `skills/pipeline/00-plan-assembly/SKILL.md` only for final ordering and packaging.

| Need | Primary route | Add when triggered |
|---|---|---|
| Full business plan | `skills/meta-strategy/business-plan-orchestrator/` | Country, sector, finance, valuation, sustainability, digital, website, execution, and audience routes |
| Feasibility or business case | `skills/meta-strategy/meta-critical-thinking-business-logic/` and the relevant pipeline sections | `meta-market-validation`, `meta-finance`, sector gates, and investment-case evidence |
| Market validation | `skills/meta-strategy/meta-market-validation/` | Customer research, interviews, experiments, channel evidence, and claim-level source verification |
| Build-Measure-Learn | `skills/meta-strategy/meta-market-validation/` and `skills/meta-strategy/meta-living-plan-governance/` | Small reversible tests, innovation accounting, leading indicators, counter-metrics, and pivot/stop rules |
| Nonprofit strategic planning | `skills/pipeline/` plus `skills/advisory-deliverables/me-framework-document/` | Governance, stakeholder, mission, resource, donor, safeguarding, and M&E requirements |
| Facility move or major operating change | `skills/pipeline/13-implementation-timeline/` and `skills/pipeline/08-operations-plan/` | Charter, decision rights, readiness, continuity, inventory, capacity, cutover, stabilisation, and closeout evidence |
| M&E and execution | `skills/meta-strategy/meta-monitoring-evaluation/` and `meta-quarterly-gameplan/` | Living-plan governance, KPI definitions, owners, cadence, thresholds, and decision logs |
| Financial projections | `skills/pipeline/10-financial-projections/` | <a href="https://github.com/peterbamuhigire/chwezi-accounting-doctrine" target="_blank" rel="noopener noreferrer">Chwezi Accounting Doctrine</a>, finance review, workbook audit, stress tests, tax and regulatory verification |
| SaaS or recurring revenue | `skills/saas/` and the relevant pipeline sections | Cohorts, CAC/LTV, retention, NRR, Rule of 40, ARR waterfall, COGS, pricing, and valuation |
| AI-enabled business | `skills/pipeline/14-ai-integration/` and relevant SaaS skills | Problem-first AI selection, system and data risks, evaluation, AI cost, governance, drift, and human oversight |
| Digital transformation | `skills/meta-strategy/meta-digital-transformation/` | Capability maturity, operating-model change, investment logic, sequencing, adoption, and benefits realisation |
| Pitch or presentation | `skills/meta-pitch/` | <a href="https://github.com/peterbamuhigire/design-system-skills" target="_blank" rel="noopener noreferrer">Design System Skills</a> for visual design and <a href="https://github.com/peterbamuhigire/digital-research-skills" target="_blank" rel="noopener noreferrer">Digital Research Engine</a> for current evidence |
| Proposal, tender, EOI, or RFP | Route to <a href="https://github.com/peterbamuhigire/proposal-skills" target="_blank" rel="noopener noreferrer">Proposal Skills</a> | Add this engine for the business case, commercial model, finance, or implementation content |

Use the smallest route that can answer the decision. Do not load every skill by default; add country, sector, funding, finance, design, document, website, accounting, or research overlays only when the engagement triggers them.

## The Kaizen operating contract

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

## Licence

See the individual skill folders for licence information.
