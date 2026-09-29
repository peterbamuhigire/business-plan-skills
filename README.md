# Business Plan Skills

Business Plan Skills is a routed engine of 137 skills for writing, testing and releasing business plans, bankable and investor-grade plans, standalone marketing plans, and the strategy, finance and advisory documents that sit around them. The [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md) runs an engagement from client intake and evidence design through sixteen numbered plan sections (with a grant-proposal variant), the financial model, investment-committee challenge, assembly and release; specialist skills cover business-model design, market validation, competitive intelligence, pricing, valuation, bankability scoring, stress testing, due diligence, SaaS, AI and agent-product economics, ICT and e-commerce businesses, hospitality, pitch preparation and organisational policy manuals. Country context for Uganda (the default), Kenya and Tanzania supplies currency, tax, regulatory, labour and banking facts, each of which must be verified at the time of writing. The engine keeps assumptions and evidence apart, requires the narrative and the model to reconcile, and limits every release claim to the evidence actually reviewed.

The engine works to standards it cites directly: IFRS 15, IAS 20, IAS 21, IFRS 13 and IFRS for SMEs for revenue, grants, foreign currency and fair value in projections (with accounting doctrine deferred to the Chwezi Accounting Doctrine engine); COSO and ISO 31000 for internal control and risk; the IFC Performance Standards (2012) for environmental and social management in development-finance submissions; ISO/IEC 27001 and ISO/IEC 42001 for security and AI governance in SaaS due diligence; the ICC/ESOMAR International Code for market research; and the PPDA framework for public procurement in Uganda. Its products are complete business plans and plan sections, bankable plans for banks and development-finance institutions, investor memoranda and pitch decks, Excel financial models built by the scripts in [`scripts/build-financial-models/`](scripts/build-financial-models/), bankability scores, stress tests, valuations, marketing plans, competitive-intelligence reports, grant proposals, quarterly execution plans, and finance, procurement, HR, governance, grants, controls and M&E manuals. It serves founders and owner-managers, consultants and programme teams, boards, lenders, development-finance institutions and investors, principally in East and Central Africa.

## Installation

Prerequisites: [Claude Code](https://claude.com/claude-code) or Codex; Node.js 18 or later for the installer scripts; Python 3.11 or later for the validators and model builders (CI uses Python 3.12 with `PyYAML==6.0.2`; the workbook builders need `xlsxwriter`, and the tools in [`tools/`](tools/) list their packages in [`tools/requirements.txt`](tools/requirements.txt)).

**Claude Code plugin.** The repository ships a marketplace in [`.claude-plugin/`](.claude-plugin/marketplace.json):

```text
/plugin marketplace add https://github.com/peterbamuhigire/business-plan-skills
/plugin install business-plan@chwezi-business-plan
```

**Installer scripts.** [`install.sh`](install.sh) and [`install.ps1`](install.ps1) call `scripts/install-engine.js`, which copies the engine into `~/.claude` (`--scope user`, the default) or into `.claude` under the current directory (`--scope project`). Add `--dry-run` to see the plan without writing anything, or `--json` for machine-readable output.

```sh
git clone https://github.com/peterbamuhigire/business-plan-skills
cd business-plan-skills
./install.sh --scope project --dry-run
./install.sh --scope project
```

On Windows PowerShell: `.\install.ps1 --scope project`.

**Codex.** Codex reads [`AGENTS.md`](AGENTS.md) as the router. Before substantive work, run the model-policy check described in [`.codex/README.md`](.codex/README.md): `python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`. Claude skips that section.

**Manual use.** Clone the repository, read [`CLAUDE.md`](CLAUDE.md) (Claude Code) or [`AGENTS.md`](AGENTS.md) (any runner), then open the `SKILL.md` that the router names. Skills are read directly from disk; no registration is required.

**Checks.** From the repository root:

```sh
python -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py --threshold 1.0
python -X utf8 scripts/routing_link_check.py
python -X utf8 -m unittest discover -s tests -p "test_*.py"
```

## Capabilities

137 active skills: 134 under [`skills/`](skills/) and 3 under [`country-context/`](country-context/). Templates in [`templates/`](templates/) and sector guide files that are references rather than skills are not counted.

| Category | Folder | Skills |
|---|---|---:|
| Plan pipeline | [`skills/pipeline/`](skills/pipeline/) | 49 |
| Strategy and validation | [`skills/meta-strategy/`](skills/meta-strategy/) | 22 |
| Finance and investor readiness | [`skills/meta-finance/`](skills/meta-finance/) | 12 |
| SaaS | [`skills/saas/`](skills/saas/) | 11 |
| ICT and e-commerce | [`skills/ict/`](skills/ict/) | 4 |
| Marketing and sales | [`skills/marketing-sales/`](skills/marketing-sales/) | 4 |
| Pricing and go-to-market | [`skills/meta-pricing-gtm/`](skills/meta-pricing-gtm/) | 3 |
| Pitch | [`skills/meta-pitch/`](skills/meta-pitch/) | 3 |
| Advisory deliverables | [`skills/advisory-deliverables/`](skills/advisory-deliverables/) | 7 |
| Board and investor reporting | [`skills/meta-reporting/`](skills/meta-reporting/) | 2 |
| Language | [`skills/language/`](skills/language/) | 3 |
| Writing and content | [`skills/writing-content/`](skills/writing-content/) | 5 |
| Utility and quality | [`skills/meta-utility/`](skills/meta-utility/) | 6 |
| Sustainability | [`skills/meta-sustainability/`](skills/meta-sustainability/) | 1 |
| Industry guides | [`skills/industry-guides/`](skills/industry-guides/) | 2 |
| Country context | [`country-context/`](country-context/) | 3 |
| **Total** | | **137** |

| Category | Skill | What it does |
|---|---|---|
| Plan pipeline | [`00-client-intake`](skills/pipeline/00-client-intake/SKILL.md) | Client intake: scope, facts, evidence gaps and assumptions register. |
| Plan pipeline | [`00-plan-assembly`](skills/pipeline/00-plan-assembly/SKILL.md) | Assembles, reconciles and renders the finished plan, including plan figures. |
| Plan pipeline | [`01-executive-summary`](skills/pipeline/01-executive-summary/SKILL.md) | Executive summary written last from reconciled sections. |
| Plan pipeline | [`02-company-overview`](skills/pipeline/02-company-overview/SKILL.md) | Company overview: legal form, ownership, history, mission and structure. |
| Plan pipeline | [`saas-agent-product-strategy-and-roadmap`](skills/pipeline/03-products-services/saas-agent-product-strategy-and-roadmap/SKILL.md) | Product strategy and roadmap overlay for agent products. |
| Plan pipeline | [`saas-ai-product-strategy-and-roadmap`](skills/pipeline/03-products-services/saas-ai-product-strategy-and-roadmap/SKILL.md) | Product strategy and roadmap overlay for AI-led SaaS. |
| Plan pipeline | [`03-products-services`](skills/pipeline/03-products-services/SKILL.md) | Products and services section. |
| Plan pipeline | [`saas-ai-market-and-tam`](skills/pipeline/04-market-analysis/saas-ai-market-and-tam/SKILL.md) | Market and TAM overlay for AI-led SaaS. |
| Plan pipeline | [`04-market-analysis`](skills/pipeline/04-market-analysis/SKILL.md) | Market analysis and sizing section. |
| Plan pipeline | [`05-target-market`](skills/pipeline/05-target-market/SKILL.md) | Target market and customer segmentation section. |
| Plan pipeline | [`saas-agent-moat-and-wrapper-risk`](skills/pipeline/06-competitive-analysis/saas-agent-moat-and-wrapper-risk/SKILL.md) | Moat and wrapper-risk overlay for agent products. |
| Plan pipeline | [`saas-ai-moat-and-defensibility`](skills/pipeline/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md) | Moat and defensibility overlay for AI-led SaaS. |
| Plan pipeline | [`06-competitive-analysis`](skills/pipeline/06-competitive-analysis/SKILL.md) | Competitive analysis section. |
| Plan pipeline | [`saas-agent-commercial-packaging-economics`](skills/pipeline/07-marketing-sales-strategy/saas-agent-commercial-packaging-economics/SKILL.md) | Commercial packaging economics for agent products. |
| Plan pipeline | [`saas-agent-outcome-pricing-business-case`](skills/pipeline/07-marketing-sales-strategy/saas-agent-outcome-pricing-business-case/SKILL.md) | Business case for outcome-based pricing of agent products. |
| Plan pipeline | [`saas-agent-pricing-strategy`](skills/pipeline/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md) | Pricing strategy overlay for agent products. |
| Plan pipeline | [`saas-ai-pricing-strategy`](skills/pipeline/07-marketing-sales-strategy/saas-ai-pricing-strategy/SKILL.md) | Pricing strategy overlay for AI-led SaaS. |
| Plan pipeline | [`07-marketing-sales-strategy`](skills/pipeline/07-marketing-sales-strategy/SKILL.md) | Marketing and sales section with SMART objectives, channels and a budget reconciled to the P&L. |
| Plan pipeline | [`08-operations-plan`](skills/pipeline/08-operations-plan/SKILL.md) | Operations plan: processes, facilities, suppliers and controls. |
| Plan pipeline | [`coaching-performance-management`](skills/pipeline/09-management-team/coaching-performance-management/SKILL.md) | Coaching and performance-management design for the team section. |
| Plan pipeline | [`saas-agent-talent-strategy`](skills/pipeline/09-management-team/saas-agent-talent-strategy/SKILL.md) | Talent strategy overlay for agent businesses. |
| Plan pipeline | [`saas-ai-talent-strategy`](skills/pipeline/09-management-team/saas-ai-talent-strategy/SKILL.md) | Talent strategy overlay for AI-led SaaS. |
| Plan pipeline | [`09-management-team`](skills/pipeline/09-management-team/SKILL.md) | Management team, governance and staffing section. |
| Plan pipeline | [`saas-agent-deferred-revenue-and-credit-reserves`](skills/pipeline/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md) | Deferred revenue and credit-reserve treatment for agent businesses. |
| Plan pipeline | [`saas-agent-revenue-recognition`](skills/pipeline/10-financial-projections/saas-agent-revenue-recognition/SKILL.md) | Revenue-recognition treatment in agent-business projections. |
| Plan pipeline | [`saas-agent-sla-cogs-treatment`](skills/pipeline/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md) | SLA cost-of-revenue treatment for agent businesses. |
| Plan pipeline | [`saas-agent-sla-economics-in-projection`](skills/pipeline/10-financial-projections/saas-agent-sla-economics-in-projection/SKILL.md) | SLA economics carried into the projection model. |
| Plan pipeline | [`saas-agent-unit-economics-and-cogs`](skills/pipeline/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md) | Unit economics and cost of revenue for agent products. |
| Plan pipeline | [`saas-ai-cost-of-tenant-calculator`](skills/pipeline/10-financial-projections/saas-ai-cost-of-tenant-calculator/SKILL.md) | Per-tenant AI cost calculator for SaaS projections. |
| Plan pipeline | [`saas-ai-unit-economics-and-cogs`](skills/pipeline/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md) | Unit economics and cost of revenue for AI-led SaaS. |
| Plan pipeline | [`10-financial-projections`](skills/pipeline/10-financial-projections/SKILL.md) | Financial projections: three statements, assumptions and workbook model. |
| Plan pipeline | [`saas-agent-funding-stage-playbook`](skills/pipeline/11-funding-request/saas-agent-funding-stage-playbook/SKILL.md) | Funding-stage playbook for agent businesses. |
| Plan pipeline | [`saas-agent-investor-narrative-on-sla`](skills/pipeline/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md) | Investor narrative for SLA commitments in agent businesses. |
| Plan pipeline | [`saas-ai-funding-stage-playbook`](skills/pipeline/11-funding-request/saas-ai-funding-stage-playbook/SKILL.md) | Funding-stage playbook for AI-led SaaS. |
| Plan pipeline | [`11-funding-request`](skills/pipeline/11-funding-request/SKILL.md) | Funding request: amount, use of funds, instrument and terms. |
| Plan pipeline | [`saas-ai-for-good-grant-proposal`](skills/pipeline/11b-grant-proposal/saas-ai-for-good-grant-proposal/SKILL.md) | AI-for-good grant proposal overlay. |
| Plan pipeline | [`11b-grant-proposal`](skills/pipeline/11b-grant-proposal/SKILL.md) | Grant proposal variant of the funding section. |
| Plan pipeline | [`saas-agent-risk-and-stress-test`](skills/pipeline/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md) | Risk and stress-test overlay for agent businesses. |
| Plan pipeline | [`saas-agent-sla-risk`](skills/pipeline/12-risk-analysis/saas-agent-sla-risk/SKILL.md) | SLA risk overlay for agent businesses. |
| Plan pipeline | [`saas-ai-risk-and-stress-test`](skills/pipeline/12-risk-analysis/saas-ai-risk-and-stress-test/SKILL.md) | Risk and stress-test overlay for AI-led SaaS. |
| Plan pipeline | [`12-risk-analysis`](skills/pipeline/12-risk-analysis/SKILL.md) | Risk analysis: register, mitigation and scenario links. |
| Plan pipeline | [`saas-agent-implementation-timeline`](skills/pipeline/13-implementation-timeline/saas-agent-implementation-timeline/SKILL.md) | Implementation timeline overlay for agent products. |
| Plan pipeline | [`13-implementation-timeline`](skills/pipeline/13-implementation-timeline/SKILL.md) | Implementation timeline with approval gates, critical path and Gantt. |
| Plan pipeline | [`saas-agent-integration-deep`](skills/pipeline/14-ai-integration/saas-agent-integration-deep/SKILL.md) | Deep integration overlay for agent products. |
| Plan pipeline | [`14-ai-integration`](skills/pipeline/14-ai-integration/SKILL.md) | AI integration section, including staged data-foundation investment cases. |
| Plan pipeline | [`15-appendices`](skills/pipeline/15-appendices/SKILL.md) | Appendices: evidence, workings and supporting documents. |
| Plan pipeline | [`saas-agent-sustainability-and-ethics`](skills/pipeline/16-sustainability-strategy/saas-agent-sustainability-and-ethics/SKILL.md) | Sustainability and ethics overlay for agent products. |
| Plan pipeline | [`saas-ai-sustainability-and-ethics`](skills/pipeline/16-sustainability-strategy/saas-ai-sustainability-and-ethics/SKILL.md) | Sustainability and ethics overlay for AI-led SaaS. |
| Plan pipeline | [`16-sustainability-strategy`](skills/pipeline/16-sustainability-strategy/SKILL.md) | Sustainability strategy section. |
| Strategy and validation | [`benchmark-methodology`](skills/meta-strategy/benchmark-methodology/SKILL.md) | Scores a tiered competitor set against a defined benchmark method. |
| Strategy and validation | [`business-plan-orchestrator`](skills/meta-strategy/business-plan-orchestrator/SKILL.md) | Runs a full business-plan engagement from intake and evidence design to assembly and release. |
| Strategy and validation | [`competitive-platform-analysis`](skills/meta-strategy/competitive-platform-analysis/SKILL.md) | Scopes a sourced, tiered competitor set for a competitive-intelligence report. |
| Strategy and validation | [`competitive-report-structure`](skills/meta-strategy/competitive-report-structure/SKILL.md) | Assembles scored competitor profiles into a competitive-intelligence report. |
| Strategy and validation | [`idea-testing`](skills/meta-strategy/idea-testing/SKILL.md) | Tests a business idea, offer or market hypothesis before commitment. |
| Strategy and validation | [`kaizen-improvement-system`](skills/meta-strategy/kaizen-improvement-system/SKILL.md) | Audits and improves this engine or any plan, model or pitch it produces. |
| Strategy and validation | [`meta-business-model-design`](skills/meta-strategy/meta-business-model-design/SKILL.md) | Designs and scores alternative business models before sections are drafted. |
| Strategy and validation | [`meta-consulting-synthesis`](skills/meta-strategy/meta-consulting-synthesis/SKILL.md) | Synthesises analytical sections into a consulting-grade storyline before assembly. |
| Strategy and validation | [`meta-critical-thinking-business-logic`](skills/meta-strategy/meta-critical-thinking-business-logic/SKILL.md) | Tests the business logic of model, market, operations, financials and funding ask. |
| Strategy and validation | [`meta-digital-transformation`](skills/meta-strategy/meta-digital-transformation/SKILL.md) | Digitally enabled growth strategy, operating model or business-model redesign. |
| Strategy and validation | [`meta-due-diligence`](skills/meta-strategy/meta-due-diligence/SKILL.md) | Commercial, operational, legal and financial due diligence. |
| Strategy and validation | [`meta-international-market-entry`](skills/meta-strategy/meta-international-market-entry/SKILL.md) | Chooses a foreign or regional market and entry mode (Porter's Diamond, CAGE, institutional voids). |
| Strategy and validation | [`meta-living-plan-governance`](skills/meta-strategy/meta-living-plan-governance/SKILL.md) | Specifies how a finished plan is maintained, reviewed and updated. |
| Strategy and validation | [`meta-market-validation`](skills/meta-strategy/meta-market-validation/SKILL.md) | Field validation of market assumptions before writing. |
| Strategy and validation | [`meta-monitoring-evaluation`](skills/meta-strategy/meta-monitoring-evaluation/SKILL.md) | Translates a completed plan into execution monitoring. |
| Strategy and validation | [`meta-operational-readiness-due-diligence`](skills/meta-strategy/meta-operational-readiness-due-diligence/SKILL.md) | Tests local executability: banking, tax, licensing, payroll, FX, logistics and compliance. |
| Strategy and validation | [`meta-quarterly-gameplan`](skills/meta-strategy/meta-quarterly-gameplan/SKILL.md) | Converts a completed plan into quarterly execution sprints. |
| Strategy and validation | [`meta-statistics`](skills/meta-strategy/meta-statistics/SKILL.md) | Statistical rigour for market sizing, surveys, forecasts and comparative metrics. |
| Strategy and validation | [`meta-strategic-audit`](skills/meta-strategy/meta-strategic-audit/SKILL.md) | Read-only strategic audit of an existing SME, NGO or growth firm. |
| Strategy and validation | [`meta-strategic-factor-analysis`](skills/meta-strategy/meta-strategic-factor-analysis/SKILL.md) | Turns PESTEL and five-forces scans into EFAS, IFAS, SFAS tables and a TOWS matrix. |
| Strategy and validation | [`meta-strategic-optionality`](skills/meta-strategy/meta-strategic-optionality/SKILL.md) | Exit thesis, exit readiness, sale memorandum and succession options. |
| Strategy and validation | [`meta-strategic-options-evaluation`](skills/meta-strategy/meta-strategic-options-evaluation/SKILL.md) | Generates and chooses strategic options (TOWS, Ansoff, strategy clock, SAFe tests). |
| Finance and investor readiness | [`meta-accounting-finance-review`](skills/meta-finance/meta-accounting-finance-review/SKILL.md) | Reviews projections, funding requests, valuation, budgets and controls in a plan. |
| Finance and investor readiness | [`meta-agent-bankability-and-investor-readiness`](skills/meta-finance/meta-agent-bankability-and-investor-readiness/SKILL.md) | Bankability and investor-readiness gate for agent-product plans. |
| Finance and investor readiness | [`meta-agent-revenue-recognition-policy`](skills/meta-finance/meta-agent-revenue-recognition-policy/SKILL.md) | Revenue-recognition policy for agent businesses facing audit or institutional due diligence. |
| Finance and investor readiness | [`meta-agent-sla-financial-controls`](skills/meta-finance/meta-agent-sla-financial-controls/SKILL.md) | Financial controls for SLA credits, refunds, prepaid credits and outcome pricing. |
| Finance and investor readiness | [`meta-agent-valuation-adjustments`](skills/meta-finance/meta-agent-valuation-adjustments/SKILL.md) | Valuation adjustments specific to agent-product businesses. |
| Finance and investor readiness | [`meta-agent-valuation-overlay-for-sla`](skills/meta-finance/meta-agent-valuation-overlay-for-sla/SKILL.md) | Valuation overlay for agent businesses carrying SLA commitments. |
| Finance and investor readiness | [`meta-ai-bankability-and-investor-readiness`](skills/meta-finance/meta-ai-bankability-and-investor-readiness/SKILL.md) | Readiness gate for AI-led SaaS plans going to fundraise, DFI or grant review. |
| Finance and investor readiness | [`meta-ai-valuation-adjustments`](skills/meta-finance/meta-ai-valuation-adjustments/SKILL.md) | Valuation adjustments for AI-led SaaS in priced rounds, secondaries or acquisitions. |
| Finance and investor readiness | [`meta-bankability-scoring`](skills/meta-finance/meta-bankability-scoring/SKILL.md) | Scores debt-service capacity, security, repayment logic and bankability blockers. |
| Finance and investor readiness | [`meta-financial-stress-test`](skills/meta-finance/meta-financial-stress-test/SKILL.md) | Stress-tests revenue, margins, working capital, break-even, runway and debt service. |
| Finance and investor readiness | [`meta-investment-committee-red-team`](skills/meta-finance/meta-investment-committee-red-team/SKILL.md) | Simulates a lender, DFI, VC, grant or board investment committee against the full plan. |
| Finance and investor readiness | [`meta-valuation`](skills/meta-finance/meta-valuation/SKILL.md) | Values a company by DCF, multiples and venture methods, with sensitivity and dilution. |
| SaaS | [`saas-bankability-and-investor-readiness`](skills/saas/saas-bankability-and-investor-readiness/SKILL.md) | Readiness gate for SaaS equity rounds from pre-seed to growth and DFI equity. |
| SaaS | [`saas-customer-success-operating-model`](skills/saas/saas-customer-success-operating-model/SKILL.md) | Customer-success operating model for SaaS operations and sales sections. |
| SaaS | [`saas-gtm-motion-design`](skills/saas/saas-gtm-motion-design/SKILL.md) | Chooses the SaaS go-to-market motion before the sales section is detailed. |
| SaaS | [`saas-lifecycle-email-and-retention`](skills/saas/saas-lifecycle-email-and-retention/SKILL.md) | Lifecycle email and retention programme for SaaS. |
| SaaS | [`saas-marketing-channel-economics`](skills/saas/saas-marketing-channel-economics/SKILL.md) | Channel economics for SaaS marketing. |
| SaaS | [`saas-mvp-and-product-market-fit-strategy`](skills/saas/saas-mvp-and-product-market-fit-strategy/SKILL.md) | MVP and product-market-fit strategy for pre-PMF SaaS or ICT plans. |
| SaaS | [`saas-pricing-and-packaging-strategy`](skills/saas/saas-pricing-and-packaging-strategy/SKILL.md) | Tiering, packaging and expansion pricing for SaaS. |
| SaaS | [`saas-sales-org-design-and-capacity-planning`](skills/saas/saas-sales-org-design-and-capacity-planning/SKILL.md) | Sales organisation design and capacity planning for SaaS above $1M ARR. |
| SaaS | [`saas-unit-economics-and-cohort-model`](skills/saas/saas-unit-economics-and-cohort-model/SKILL.md) | SaaS unit economics and cohort model for the projections section. |
| SaaS | [`saas-valuation-and-fundraising-strategy`](skills/saas/saas-valuation-and-fundraising-strategy/SKILL.md) | SaaS valuation and fundraising strategy. |
| SaaS | [`saas-vertical-niche-selection`](skills/saas/saas-vertical-niche-selection/SKILL.md) | Selects a vertical niche before a new SaaS or ICT plan is drafted. |
| ICT and e-commerce | [`ecommerce-business-model-diagnostic`](skills/ict/ecommerce-business-model-diagnostic/SKILL.md) | Scores an operating e-commerce business for viability and cross-border readiness, with a 90-day improvement plan. |
| ICT and e-commerce | [`ecommerce-unit-economics-and-cross-border-margin-model`](skills/ict/ecommerce-unit-economics-and-cross-border-margin-model/SKILL.md) | Models landed cost, contribution margin, CAC, LTV and cross-border viability for e-commerce. |
| ICT and e-commerce | [`ict-product-company-business-plan`](skills/ict/ict-product-company-business-plan/SKILL.md) | Business plan for a non-SaaS ICT product company (licensed, embedded or on-premise software). |
| ICT and e-commerce | [`ict-services-firm-business-plan`](skills/ict/ict-services-firm-business-plan/SKILL.md) | Business plan for an ICT services firm, agency or integrator: utilisation, bench, pipeline and productisation. |
| Marketing and sales | [`demand-forecasting`](skills/marketing-sales/demand-forecasting/SKILL.md) | Demand forecasts, stock-out timing, reorder logic and branch or product sales aggregation. |
| Marketing and sales | [`digital-marketing-strategy`](skills/marketing-sales/digital-marketing-strategy/SKILL.md) | Evidence-based digital marketing section: channels, content, campaigns, measurement and budget. |
| Marketing and sales | [`entrepreneurial-demand-generation`](skills/marketing-sales/entrepreneurial-demand-generation/SKILL.md) | Shows how customers move from awareness to conversion, retention and referral. |
| Marketing and sales | [`marketing-plan-orchestrator`](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md) | Builds or audits a standalone marketing plan from situation analysis to budget, KPIs and control. |
| Pricing and go-to-market | [`meta-premium-go-to-market`](skills/meta-pricing-gtm/meta-premium-go-to-market/SKILL.md) | Go-to-market for premium, executive, enterprise and high-ticket buyers. |
| Pricing and go-to-market | [`meta-pricing-strategy`](skills/meta-pricing-gtm/meta-pricing-strategy/SKILL.md) | Tests and defends pricing that matches or undercuts competitors. |
| Pricing and go-to-market | [`meta-website-investment-planning`](skills/meta-pricing-gtm/meta-website-investment-planning/SKILL.md) | Plans and justifies website, online store, portal or SEO investment within a plan. |
| Pitch | [`meta-pitch-preparation`](skills/meta-pitch/meta-pitch-preparation/SKILL.md) | Prepares founders for investor, lender, donor, client or board pitches. |
| Pitch | [`meta-presentation-design`](skills/meta-pitch/meta-presentation-design/SKILL.md) | Designs or audits a presentation deck tied to a plan or proposal. |
| Pitch | [`pitch-deck`](skills/meta-pitch/pitch-deck/SKILL.md) | Builds investor, bank or proposal pitch decks. |
| Advisory deliverables | [`finance-policy-and-manual`](skills/advisory-deliverables/finance-policy-and-manual/SKILL.md) | Drafts a financial management policy or finance and accounting manual. |
| Advisory deliverables | [`governance-and-board-charter`](skills/advisory-deliverables/governance-and-board-charter/SKILL.md) | Drafts a governance framework, board or committee charter and delegation-of-authority matrix. |
| Advisory deliverables | [`grants-management-manual`](skills/advisory-deliverables/grants-management-manual/SKILL.md) | Drafts a grants or donor-funds management manual for a grant recipient. |
| Advisory deliverables | [`hr-policy-manual`](skills/advisory-deliverables/hr-policy-manual/SKILL.md) | Drafts an HR policy manual for an NGO, SME, SACCO, project or public-adjacent body. |
| Advisory deliverables | [`internal-controls-and-risk-framework`](skills/advisory-deliverables/internal-controls-and-risk-framework/SKILL.md) | Drafts an internal-control policy, risk framework, control matrix and risk register. |
| Advisory deliverables | [`me-framework-document`](skills/advisory-deliverables/me-framework-document/SKILL.md) | Drafts a standalone monitoring, evaluation and learning framework. |
| Advisory deliverables | [`procurement-policy-and-manual`](skills/advisory-deliverables/procurement-policy-and-manual/SKILL.md) | Drafts a procurement policy or procurement and disposal manual. |
| Board and investor reporting | [`meta-agent-board-and-investor-reporting`](skills/meta-reporting/meta-agent-board-and-investor-reporting/SKILL.md) | Monthly investor updates for agent businesses. |
| Board and investor reporting | [`meta-board-and-investor-reporting`](skills/meta-reporting/meta-board-and-investor-reporting/SKILL.md) | Board and investor reporting for SaaS companies with external investors. |
| Language | [`east-african-english`](skills/language/east-african-english/SKILL.md) | Professional English for Uganda, Kenya and Tanzania: British spelling, register, courtesy and country tone. |
| Language | [`language-standards`](skills/language/language-standards/SKILL.md) | Grammar, register, terminology and localisation controls for English, French and Kiswahili content. |
| Language | [`writing-quality`](skills/language/writing-quality/SKILL.md) | Edits plans, proposals and pitches for clarity, argument, persuasion and a human voice. |
| Writing and content | [`ai-prompt-writer`](skills/writing-content/ai-prompt-writer/SKILL.md) | Writes prompts for external AI tools (text, image and video). |
| Writing and content | [`blog-idea-generator`](skills/writing-content/blog-idea-generator/SKILL.md) | Generates blog topics, editorial angles and content pipelines. |
| Writing and content | [`blog-writer`](skills/writing-content/blog-writer/SKILL.md) | Writes blog articles and long-form website content. |
| Writing and content | [`content-writing`](skills/writing-content/content-writing/SKILL.md) | Drafts and edits website copy. |
| Writing and content | [`premium-commercial-writing`](skills/writing-content/premium-commercial-writing/SKILL.md) | Persuasive writing for buyers, lenders, investors, boards and grant committees. |
| Utility and quality | [`ai-slop-audit`](skills/meta-utility/ai-slop-audit/SKILL.md) | Audits a finished artefact for AI-generated filler before release. |
| Utility and quality | [`anti-ai-slop`](skills/meta-utility/anti-ai-slop/SKILL.md) | Prevents AI-generated filler while drafting any human-facing artefact. |
| Utility and quality | [`proposal-architect`](skills/meta-utility/proposal-architect/SKILL.md) | Coordinates a proposal, bid, tender, EOI or RFP response to a compliant draft. |
| Utility and quality | [`skill-safety-audit`](skills/meta-utility/skill-safety-audit/SKILL.md) | Read-only safety review of new or changed skills. |
| Utility and quality | [`skill-writing`](skills/meta-utility/skill-writing/SKILL.md) | Creates and reviews skills under the canonical chwezi-dev-engine standard. |
| Utility and quality | [`update-claude-documentation`](skills/meta-utility/update-claude-documentation/SKILL.md) | Synchronises README, AGENTS, CLAUDE and status documents after authorised changes. |
| Sustainability | [`meta-sustainability`](skills/meta-sustainability/SKILL.md) | Identifies sustainability design requirements at the start of an engagement. |
| Industry guides | [`hospitality-hotel-restaurant`](skills/industry-guides/hospitality-hotel-restaurant/SKILL.md) | Bankable plans, feasibility studies and operating plans for hotels, lodges, restaurants and food service. |
| Industry guides | [`industry-guides`](skills/industry-guides/SKILL.md) | Entry point to the sector guide catalogue: operating models, benchmarks, regulation, costs and risks. |
| Country context | [`kenya`](country-context/kenya/SKILL.md) | Kenya currency, tax, regulatory, labour, banking, market and risk context for plans and investment cases. |
| Country context | [`tanzania`](country-context/tanzania/SKILL.md) | Tanzania currency, tax, regulatory, labour, banking, development-plan and risk context. |
| Country context | [`uganda`](country-context/uganda/SKILL.md) | Uganda context (the repository default): currency, tax, regulation, labour, banking, market and risk. |

## Operating contracts

- [`AGENTS.md`](AGENTS.md) is the runner-agnostic router; [`CLAUDE.md`](CLAUDE.md) imports it for Claude Code. Always-on principles live in [`rules/`](rules/).
- Multi-phase work follows the [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md): scoped work packages, evidence checkpoints, context hygiene, least agency, and sanitised handling of external content.
- Full plans start at the [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md); standalone marketing plans start at the [marketing-plan orchestrator](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md).
- Sister engines are consulted alongside, never instead: Chwezi Accounting Doctrine for IFRS/IAS, tax and controls; chwezi-design-engine for the look of any deliverable; digital-research-engine for current facts; proposal-skills for tenders and PPDA submissions.

## References

Sources the repository itself cites as the basis for its skills. Books that appear only in reading or wish lists (for example [`05-reading-list.md`](docs/engine-upgrade-july-2026/05-reading-list.md)), and titles supplied without content, are not listed. Citations only; no book content is reproduced here.

### Books

- Abrams, R. M. (1993) *The Successful Business Plan: Secrets & Strategies*, 2nd edn, The Oasis Press
- Agrawal, A., Gans, J. and Goldfarb, A. (2018; updated 2022) *Prediction Machines: The Simple Economics of Artificial Intelligence*, Harvard Business Review Press
- Alam, M. M. *Transforming an Idea Into a Business with Design Thinking*, Springer
- Alonzo, R. S. (2007) *The Upstart Guide to Owning and Managing a Restaurant*, 2nd edn, Kaplan
- Amitabh, U. (2022) *Passion Economy and the Side Hustle Revolution*, SAGE
- Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D. and Cochran, J. J. (2013) *Essentials of Statistics for Business and Economics*, 7th edn, Cengage
- Anthony, R. and Boyd, B. (2014) *Innovative Presentations For Dummies*, Wiley
- ASCM (2022) *Certified in Logistics, Transportation and Distribution (CLTD) Learning System*
- Ashley, A. (2003) *Oxford Handbook of Commercial Correspondence*, Oxford University Press
- Atkinson, C. (2008) *Beyond Bullet Points*, Microsoft Press
- Barnard, F., Akridge, J., Dooley, F. and Foltz, J. (2012) *Agribusiness Management*, 4th edn, Routledge
- Barrow, C. (2009) *Get Backed, Get Big, Get Bought*, Capstone
- Bates (2024) *Valuepreneurs*
- Berger, L. and Berger, D. (eds) (2004) *The Talent Management Handbook*, McGraw-Hill
- Berkman, J. W. (2013) *Due Diligence and the Business Transaction: Getting a Deal Done*, Apress
- Berlin, I. (1953) *The Hedgehog and the Fox*
- Berman, B. and Evans, J. (2013) *Retail Management*
- Berns, G. (2005) *Satisfaction*
- Beveridge, A. and Oberschall, A. (1979) *African Businessmen and Development in Zambia*, Princeton University Press
- Bland, D. and Osterwalder, A. (2020) *Testing Business Ideas*, Wiley
- Blank, S. and Dorf, B. (2012) *The Startup Owner's Manual*, K&S Ranch
- Bly, R. *How to Write and Sell Simple Information*
- Bodnar, K. and Cohen, J. L. (2012) *The B2B Social Media Book*, Wiley
- Bragg, S. (2003) *Essentials of Payroll: Management and Accounting*, Wiley
- Brandenburger, A. and Nalebuff, B. (1996) *Co-opetition*
- Brito, M. (2013) *Your Brand, The Next Media Company*, Que Biz-Tech/Pearson
- Brunson, R. (n.d.) *Proven Secrets to Double Your Traffic, Conversion & Sales for Any Product or Service Online*, SuccessEtc LLC
- Bush, W. *ProductLed Growth*
- Byczynski, L. (2013) *Market Farming Success*, rev. edn, Chelsea Green
- Cadle, J., Paul, D. and Turner, P. (2010) *Business Analysis Techniques: 72 Essential Tools for Success*, BCS
- Cassani, A. *Code Revealed*
- Chaffey, D. and Ellis-Chadwick, F. (2022) *Digital Marketing*, 8th edn
- Cialdini, R. (2021) *Influence*, Harper Business
- Collins, J. (2001) *Good to Great*
- Cooper, B. and Vlaskovits, P. (2010) *The Entrepreneur's Guide to Customer Development*, Cooper-Vlaskovits
- Cotton, B. / FLG Partners (2019) *How to Run a SaaS Business*
- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly Media
- Cunningham, L. (2014) *Berkshire Beyond Buffett: The Enduring Value of Values*
- Damerow, G. (2010) *Storey's Guide to Raising Chickens*, 3rd edn, Storey Publishing
- Damodaran, A. (2011) *The Little Book of Valuation*, Wiley
- Dardick, E. (2011) *Get Catering and Grow Sales!*
- Debelak, D. (2006) *Business Models Made Easy*, Entrepreneur Press
- Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*, McGraw-Hill
- Dennis, A., Wixom, B. H. and Tegarden, D. (2021) *Systems Analysis and Design: An Object-Oriented Approach with UML*, 6th edn, Wiley
- Dietz, T. (2023) *Decisions for Sustainability*, Cambridge University Press
- Digital Business Academy (2021) *Social Media Marketing 2021-22: Beginners Guide to Making Money Online*, self-published
- Dittmer, P. R. and Keefe, J. D. (2009) *Principles of Food, Beverage, and Labor Cost Controls*, 9th edn
- Donnelly and Foley (2003) *Budgeting for Better Performance*, 4th edn, ILM/Elsevier/Pergamon
- Duarte, N. (2010) *Resonate*, Wiley
- Duarte, N. (2012) *HBR Guide to Persuasive Presentations*, Harvard Business Review Press
- Duguin, S. *Cybersecurity for NGOs: Attack Prevention and Threat Response*
- Dumas, M., La Rosa, M., Mendling, J. and Reijers, H. A. (2013) *Fundamentals of Business Process Management*, Springer
- Edwards, J. (ed.) (2007) *Presentation Skill*, Global Media
- Edwards, P., Edwards, S. and Douglas, L. C. (1991) *Getting Business to Come to You*, Jeremy P. Tarcher/Perigee
- Entrepreneur Press (2012) *Start Your Own Restaurant and More*, 4th edn
- Evans, V. (2018) *Strategy Plain and Simple*, Pearson
- Fahey, L. and Randall, R. (eds) (2000) *The Portable MBA in Strategy*, 2nd edn, Wiley
- Feld, B. and Mendelson, J. (2019) *Venture Deals*, 4th edn, Wiley
- Fisher, R. and Ury, W. *Getting to Yes*
- Fleisher, C. and Bensoussan, B. (2007) *Business and Competitive Analysis*, FT Press
- Fortier, J.-M. (2014) *The Market Gardener*, New Society Publishers
- Gallo, C. (2010) *The Presentation Secrets of Steve Jobs*, McGraw-Hill
- Garbugli, É. (2020) *The SaaS Email Marketing Playbook*
- Geddes, B. (2014) *Advanced Google AdWords*, 3rd edn, Wiley/Sybex
- Geffner, A. (1998) *Business English*, 3rd edn, Barron's
- Gerber, M. E. (1995) *The E-Myth Revisited*
- Gerber, M. E. (2008) *Awakening the Entrepreneur Within*, HarperCollins
- Godin, S. (2012) *Startup School* (audio programme)
- Goh, F. (2025) *Innovate to Elevate!*
- Goldratt, E. *The Goal*
- Golding, T. (2024) *Building Multi-Tenant SaaS Architectures*, O'Reilly Media
- Goliger (2023) *The Zero to 100 Million Sales Blueprint*
- Graves *Writing for Profit*
- Grove, A. (1983) *High Output Management*
- Guillebeau, C. (2017) *Side Hustle: From Idea to Income in 27 Days*, Crown Business
- Gupta, N. (2019) *Black Book of English Vocabulary*
- Hahn, F. and Mangun, K. (2003) *Do It Yourself Advertising and Promotion*, 3rd edn
- Haines, S. (2022) *How to Create a Business Case*
- Hair, J. F. Jr., Ortinau, D. J. and Harrison, D. E. (2023) *Essentials of Marketing Research*, 6th edn, McGraw-Hill Education
- Hak, T., Moldan, B. and Dahl, A. L. (eds) (2007) *Sustainability Indicators: A Scientific Assessment*, SCOPE Report 67, Island Press
- Hammer, M. and Champy, J. (1993) *Reengineering the Corporation*
- Hansen *Deploy Empathy*
- Hargis, G. et al. *Developing Quality Technical Information*
- Harris and Lenox (2013) *The Strategist's Toolkit*, Darden
- Harvard Business Review (2014) *Presentations* (20-Minute Manager series), Harvard Business Review Press
- Harvard Business Review (2020) *10 Must Reads on Managing People*, Vol. 2
- Hattori, S. *The McKinsey Edge*
- Hetherington, C. (2024) *OSINT: The Authoritative Guide to Due Diligence*, 3rd edn, Hetherington Group
- Hill, R. (2013) *Pricing for Profit*, Kogan Page
- Holmes, C. *The Ultimate Sales Machine*
- Holt, J. and Farenga, P. (2003) *Teach Your Own*
- Hood (2013) *Words at Work*, WordCraft Global
- Horowitz, B. (2014) *The Hard Thing About Hard Things*, HarperBusiness
- Howson, P. (2003) *Due Diligence: The Critical Stage in Mergers and Acquisitions*, Gower
- Hunter, V. L. with Tietyen, D. (1997) *Business to Business Marketing*, NTC Business Books
- ILM/Elsevier (2003) *Finance for Non-Financial Managers*
- Jia, R. (2025) *Growth Marketing Strategy*
- John, I. (2023) *The Art of Asking ChatGPT for High-Quality Answers*
- Johnson, G., Whittington, R., Scholes, K., Angwin, D. and Regnér, P. (2017) *Exploring Strategy*, 11th edn, Pearson
- Kagan, N. (2024) *Million Dollar Weekend*, Portfolio/Penguin
- Kane, A. (2021) *Social Media Marketing and Online Business 2021*, self-published
- Kawasaki, G. (1989) *The Macintosh Way*
- Kawasaki, G. (2004) *The Art of the Start*
- Kaza, S. (2025) *Unconvention: A Small Business Strategy Guide*, Ideapress Publishing
- Kazanjy, P. (2020) *Founding Sales*
- Keeley, L. et al. (2013) *Ten Types of Innovation*
- Keenan, J. (2019) *Gap Selling*
- Keegan, B. P. (2024) *Dare to Disrupt*
- Keller, G. (2011) *Statistics for Management and Economics, Abbreviated*, 9th edn, Cengage
- Kelley, L. D. and Sheehan, K. B. (c. 2021) *Advertising Management in a Digital Environment*, Routledge
- Kennedy, D. S. (2000) *The Ultimate Sales Letter*, 2nd edn, Adams Media
- Kennedy, D. S. (2004) *No B.S. Sales Success*, 3rd edn, Entrepreneur Press
- Kennedy, D. S. and Marrs, J. (2011) *No B.S. Price Strategy*, Entrepreneur Press
- Kennedy, D. S. and Walsh-Phillips, K. (2018) *Magnetic Marketing*, ForbesBooks
- Keshwani, A. (2023) *55 Digital Marketing Masterpieces*
- Kim, G. et al. *The DevOps Handbook*, 2nd edn, IT Revolution
- Kim, W. C. and Mauborgne, R. (2005) *Blue Ocean Strategy*
- King, J. B. *Business Plans to Game Plans*
- Klaff, O. (2011) *Pitch Anything*, McGraw-Hill
- Knaflic, C. N. *Storytelling with Data*
- Kotler, P., Kartajaya, H. and Setiawan, I. (2023) *Marketing 6.0: The Future Is Immersive*, Wiley
- Kumar, R. et al. (2025) *Technopreneurship and Sustainability*, CRC Press
- Kupsh, J. and Graves, P. R. (1993) *How to Create High-Impact Business Presentations*, NTC Business Books
- Lafley, A. G. and Martin, R. (2013) *Playing to Win: How Strategy Really Works*, Harvard Business Review Press
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn, Mercury Learning and Information
- Leleux, B. and van der Kaaij, J. (2019) *Winning Sustainability Strategies*, Palgrave Macmillan
- Levinson, J. C. *Guerrilla Marketing*
- Lima *Fundamentals of Writing*
- Lin, L. C. (2013) *Decode and Conquer*, 2nd edn, Impact Interview
- Maister, D., Green, C. and Galford, R. *The Trusted Advisor*
- Marcos, J., Guesalaga, R., Hough, A. and Vincent, R. (c. 2025) *The High-Performing Key Account Manager*, Kogan Page
- Marshall, P. and Yu, D. (2022) *The Definitive Guide to TikTok Advertising*, Perry Marshall & Associates
- Mathew, J. (2021) *YouTube Marketing 2021*, self-published
- Maxwell *7 Steps to Better Writing*
- Mayer, R. (2009) *Multimedia Learning*, Cambridge University Press
- McDonald, M., Wilson, H. and Chaffey, D. (2024) *Marketing Plans: Profitable Strategies in the Digital Age*, 9th edn, Wiley
- McGowan, B. (2014) *Pitch Perfect*, HarperBusiness
- McNeill, J. (2026) *The Algorithm*
- Mersch, E. (2023) *Hacking SaaS*
- Miller, D. (2017) *Building a StoryBrand*, HarperCollins
- Minto, B. (1987; 2002; Minto International 2010) *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*
- Mirieri, T. (c. 2015-2016) *SACCO and Chama Business Explained*, self-published
- Mohan, S. *Designing the AI-Driven Data Foundations: Architecture, Principles, and Practice*
- Molenaar, C. *Demand-Driven Business Strategy: Digital Transformation and Business Model Innovation*
- Moore, G. (1991/1999) *Crossing the Chasm*
- Morlidge, S. and Player, S. (2010) *Future Ready: How to Master Business Forecasting*, Wiley
- Murray-Webster, R. and Pullan, P. *Making Risk Management Work*, 2nd edn, Routledge
- Nager, M. et al. (2011) *Startup Weekend*
- National Restaurant Association (1996) *Uniform System of Accounts for Restaurants*, 7th edn
- Ohmae, K. (1982) *The Mind of the Strategist*, McGraw-Hill
- Olson, D. and Wu, D. (2017) *Enterprise Risk Management Models*, 2nd edn, Springer
- Orlicky, J. *Material Requirements Planning*, McGraw-Hill
- Page, S. (2015) *The Power of Business Process Improvement*, 2nd edn, AMACOM
- Palfreyman, J. (2020) *Digital Transformation Handbook: An Agile Approach to Maximise Value*
- Penrith, D. (2009) *Start and Run a Shop*, How To Books
- Pinskey, R. (1997) *101 Ways to Promote Yourself*, Avon Books
- Porter, M. E. (1980) *Competitive Strategy: Techniques for Analyzing Industries and Competitors*, Free Press
- Porter, M. E. (1985) *Competitive Advantage: Creating and Sustaining Superior Performance*, Free Press
- Rasiel, E. (1999) *The McKinsey Way*, McGraw-Hill
- Rasiel, E. and Friga, P. *The McKinsey Mind*
- Raydugin, Y. (2013) *Project Risk Management: Essential Methods for Project Teams and Decision Makers*, Wiley
- Reynolds, G. (2008) *Presentation Zen*, New Riders
- Robinson, D. (2023) *The Digital Marketing Playbook for 2023*, self-published
- Rogers, D. L. (2016) *The Digital Transformation Playbook*, Columbia University Press
- Rogers, E. (1962) *Diffusion of Innovations*
- Rogoff, E. *Bankable Business Plans*
- Rouhiainen, L. (2021) *101 Facebook Marketing Tips and Strategies for Small Businesses*
- Rowse, D. *ProBlogger*
- Rubie, P. and Provost, G. (1997) *How to Tell a Story*, Writer's Digest Books
- Rubinelli, S. *Institutional Health Communication in the Information Age*
- Rumelt, R. (2011) *Good Strategy/Bad Strategy*
- Sardanis, A. (2007) *A Venture in Africa*, I.B. Tauris
- Scharfman, J. (2012) *Private Equity Operational Due Diligence*, Wiley
- Schmidgall, R. S., Hayes, D. K. and Ninemeier, J. D. (2002) *Restaurant Financial Basics*, Wiley
- Shiach, D. (2009) *How to Write Essays*, How To Books
- Silberman, M. (ed.) (2003) *The Active Manager's Tool Kit*, McGraw-Hill
- Simon, A. R. (2022) *Side Hustles For Dummies*, Wiley
- Sinek, S. (2009) *Start With Why*, Portfolio/Penguin
- Smith, S. and Mazin, R. (2004) *The HR Answer Book*, AMACOM
- Stephenson, G. (2019) *Whole Farm Management*, Storey Publishing
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*, NTC Business Books
- Stutts, P. (2021) *The Undefeated Marketing System*
- Thankaraju (2018) *Startup 500 Business Ideas*
- Tidd, J. and Bessant, J. (2013) *Managing Innovation*, 5th edn, Wiley
- Tiwari, R. (2008) *Retailing*
- Tracy, B. and Partridge, H. (2026) *Make Phenomenal Profits*
- Upadhyay (2024) *Generative AI for Marketing*
- van der Kooij, J. et al. (2018) *The SaaS Sales Method for Account Executives* and *The SaaS Sales Method Fundamentals*, Winning by Design
- Vandeput, N. (2023) *Demand Forecasting Best Practices*, Manning
- Verwijs, C., Overeem, B. and Lennartz, R. (2023) *Practical Product Management for Product Owners*, Scrum.org
- Waite, M. (2023) *Sustainability at Work*, 2nd edn, Routledge
- Walling, R. (2023) *The SaaS Playbook*
- Webb *What Customers Crave*
- Weinberg, G. and Mares, J. (2014) *Traction*, S-curves Publishing
- Wheelen, T. L., Hunger, J. D., Hoffman, A. N. and Bamford, C. E. (2018) *Concepts in Strategic Management and Business Policy*, 15th edn, Pearson
- Whitmell *Business Writing Essentials*
- Willis, T. (2024) *Social Media Marketing in 2024*, self-published
- Wiswall, R. (2009) *The Organic Farmer's Business Handbook*, Chelsea Green
- Wood, M. B. (2003) *The Marketing Plan Handbook*
- *The Chicago Manual of Style*, 17th edn
- Cited by title only in the repository: *Valuation*; *Master Data Storytelling*; *Strategic Storytelling*; *The Bezos Letters*; *Yes!*; *Buyology*; *The Adweek Copywriting Handbook*; *Digital Business Strategy* (2024); *Business Models for E-Commerce*; *Growth Engineering*; *Remarkable Business Growth*; *Think Deeper*; *Small Business 911*; *Strategic DevOps*; *DevOps for PHP Developers*; *Modern DevOps Practices*; *Mastering Project Management Integration and Scope*; *Mathematical Foundations of Big Data Analytics*; *AI-Based Data Analytics: Applications for Business Management*; *The Data Analytics Advantage*; *Data Analytics using Python*; *Introduction to Data Analytics*; *The Nonprofit Guide to Strategic Planning*; *Facility Move Playbook*; *Paid for Your Perspective*

### Repositories

- Archify — https://github.com/tt-a1i/archify — MIT — diagram IR and render-evidence pattern for plan figures (Gantt, process flow, pitch diagrams), paraphrased at commit `0e4949f910a8e390bd3b4933883a4dcabad571be` via the chwezi-sdlc-documentation renderer ([`plan-figures.md`](skills/pipeline/00-plan-assembly/references/plan-figures.md))
- ECC (affaan-m) — https://github.com/affaan-m/ECC — shortform, longform and security guides behind the [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md); the Git Bash path fix in `install.sh`
- codex-astra-luna-orchestrator — https://github.com/donvito/codex-astra-luna-orchestrator — concept reference for the Codex model-policy helper, inspected at commit `21f4561656a1b8f2813828520357e3cd1785d50f`; independently implemented ([`.codex/README.md`](.codex/README.md))
- chwezi-dev-engine — https://github.com/peterbamuhigire/chwezi-dev-engine — canonical `skill-writing` standard and byte-mirrored validator scripts
- Business Plan Skills — https://github.com/peterbamuhigire/business-plan-skills — this repository

Repositories studied in the 29 September 2026 ten-repository Kaizen from which this engine adopted something:

- Archify — https://github.com/tt-a1i/archify — MIT — plan-figure pipeline (M10-13, above)
- Impeccable — https://github.com/pbakaus/impeccable — Apache-2.0 — project-context contract: the router reads a `PROJECT.md` with `project_schema: 1` before planning (M10-12, IM-11)
- Ponytail — https://github.com/DietrichGebert/ponytail — MIT — host-file single source and drift control: thin `CLAUDE.md` bridge over `AGENTS.md` (M10-02)
- Superpowers — https://github.com/obra/superpowers — MIT — skill-authoring convergence that turned local `skill-writing` into a pointer to the canonical standard (M10-04)
- Addy Osmani agent-skills — https://github.com/addyosmani/agent-skills — MIT — routing-evaluation work that re-mirrored the canonical `quick_validate.py` (M10-03)
- Graphify — https://github.com/Graphify-Labs/graphify — Apache-2.0 — skill-graph pass that found 151 dangling numbered-skill paths, repointed on 29 September (M10-12)

### Standards and official sources

- Accounting and assurance: IFRS 15 (with ASC 606); IAS 21 (with ASC 830); IAS 20; IFRS 9; IFRS 13; IFRS for SMEs; IPSAS; IPEV Valuation Guidelines; COSO Internal Control and COSO ERM (2017); ISO 31000
- Environmental, social and development finance: IFC (2012) *Performance Standards on Environmental and Social Sustainability*; AfDB Operational Safeguards; Uganda Development Bank (2021) *Environmental and Social Policy*; IIRC (2021) *International Integrated Reporting Framework*; GRI Standards; TCFD; UN Sustainable Development Goals; EU Deforestation Regulation 2023/1115; published ESMPs of AfDB (Zambia Grid Resilience, 2025), FAO/World Bank (Yemen FSRRP, 2025), UNDP (Vietnam Climate Smart Coastal Communities, 2025) and World Bank (Rail Logistics Improvement Project, P170532)
- Security, AI and data protection: ISO/IEC 27001; SOC 2; ISO/IEC 42001; NIST AI RMF; OWASP; GDPR
- Trade, quality and research codes: ISO 9001; ISO 4217; Incoterms (2000/2020); HACCP; ICC/ESOMAR International Code 2025 (https://standards.esomar.org/assets/documents/icc-esomar-code-2025.pdf); FATF; UNBS specifications US 107, US 191, US 386, US 792 and US/IEC 60227
- Donor and procurement rules: EU PRAG Annex III; USAID ADS 303; GIZ procurement standards; Government of Uganda IPPS rates; UNDP Uganda procurement guidelines; PPDA Act 2003 and PPDA Regulations 2023
- Uganda statutes: Income Tax Act Cap. 340; Value Added Tax Act Cap. 349; Excise Duty Act 2014; Stamp Duty Act 2014; Income Tax (Transfer Pricing) Regulations 2011; Employment Act 2006; NSSF Act; Workers' Compensation Act; Occupational Safety and Health Act; Whistleblowers Protection Act 2010; Local Governments (Financial and Accounting) Regulations 2007; Trade Licensing Act Cap. 101; Companies Act 2012; Industrial Property Act Cap. 224 and Regulations 2017; Trademarks Act Cap. 225 and Regulations 2023; Children Act Cap. 59; NEMA Act Cap. 153; Data Protection and Privacy Act 2019 (https://media.ulii.org/files/legislation/akn-ug-act-2019-9-eng-2019-05-03.pdf) and Regulations 2021; Tier 4 Microfinance Institutions and Money Lenders Act 2016; Financial Institutions (Revision of Minimum Capital Requirements) Instrument 2022
- Uganda regulators and official publications: KPMG (2025) *Tax (Amendment) Bills, 2025*; Ministry of Justice and Constitutional Affairs / WIPO (2019) *National Intellectual Property Policy*; URSB (2025) *Intellectual Property Examination Guidelines*; UMRA (2024) *Tier 4 Digital Lending Guidelines*; CMA Uganda (2020) *Handbook*; USE (2021) *Listing Rules*; TASLAF Advocates (2023) *A Legal Guide to Uganda's Financial Sector*; Uganda Bankers' Association *Banking Sector Report 2023*; Norfund / DFCU Bank (2017) *Increasing Access to Finance in Uganda*; Stanbic Bank Uganda (2019) loan terms; Uganda Development Bank lending guidelines; Uganda Credit Guarantee Scheme manual; PSFU SME lending data 2024; BoU CBR data 2025; MSME Financing Gateway for East Africa; UNCDF; aBi Trust; MoICT&NG (2025) *Uganda ICT IP Guidelines*; NRC et al. (2025) *Self-Employment and Small Business Guide for Uganda*; RSM Eastern Africa (2026) *Doing Business in Uganda 2025/26*; Baker Tilly Hem *Business in Uganda*; Uganda Green Growth Development Strategy; NEMA Environmental Sensitivity Atlas
- Uganda statistics: UBOS *Key Economic Indicators* (139th issue), CPI (February 2026), UNHS 2023/24, National Labour Force Survey 2021, Annual Agricultural Survey 2021/22, NPHC 2024, National Livestock Census 2021 (https://www.ubos.org/publications/statistical/)
- Uganda agriculture: MAAIF dairy-farm planning guidelines; MAAIF/UNDP (2014) *NAMA on Climate-Smart Dairy Livestock Value Chains*; MAAIF (2020) goat and sheep guidance; NAGRC&DB guidance; NARO/MAAIF (2015) *Cassava Seed Business Training Manual*; NAARI/MAAIF *Cassava Development in Uganda*; AgriTT/DFID/MAAIF *Building Uganda's Cassava Production Base*; ASHC/IITA/CABI (2014) *Cassava System Cropping Guide*; TAAT/IITA (2022) *Cassava Processing Technology Toolkit Catalogue*; IITA (2005) *Cassava Production, Processing and Marketing in Nigeria*; Abass et al. (2014) *Quality Assurance Manual for Cassava Processing*, ASERECA; UCDA guidance
- Regional and multilateral: UNDP Uganda *Compendium of Investment & Business Opportunities*, Vol. 2; World Bank *Uganda Economic Update* (21st edn, 2023; 26th edn, 2025); World Bank / Government of Uganda (2025) *Uganda Human Capital Development and Growth Review*; IFC/World Bank (2022) *Creating Markets in Uganda*; World Bank/IFC (2022) *Unlocking the Potential of Women Entrepreneurs in Uganda*; World Bank (2019) *Profiting from Parity*; World Bank Worldwide Governance Indicators and *Doing Business 2020*; World Bank World Development Indicators (https://databank.worldbank.org/source/world-development-indicators); AfDB (2025) *African Economic Outlook*; Afreximbank (2025) *African Trade and Economic Outlook* and *African Trade Report*; EAA (2025) *East Africa Macroeconomic Outlook*; AUC/OECD (2025) *Africa's Development Dynamics*; AFRODAD (2021) *Mineral Resource Governance in East Africa*; UNCTAD *Economic Development in Africa Report* (2020) and AfCFTA assessment (2023); EAC (2009) *Common Market Protocol*; IOM/BRMM (2022) labour-mobility report; UNECA (2025) *Eastern Africa's Trade Performance in 2024–2025*; Majune, S. K. (2024) *Export Trade Potential of the EAC under AfCFTA*, EAC/TradeMark Africa; WTO *Global Trade Report 2025*
- Kenya: KNBS *Kenya Facts and Figures 2025*, *Economic Survey 2025* and *2025 Statistical Abstract* (https://www.knbs.or.ke/reports/2025-statistical-abstract/); US Department of State *2025 Kenya Investment Climate Statement*; SECO *Economic Report 2025 — Kenya*; CBK *Monthly Economic Indicators*, average interest rates (2025) and *Revised Risk-Based Credit Pricing Model* (2025); IMF *Article IV Kenya 2024*; Ministry of Mining *Kenya Mining Investment Handbook*; Data Protection Act 2019 (https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2022-12-31); Data Protection (General) Regulations 2021 (https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf); Consumer Protection Act 2012 (https://www.parliament.go.ke/sites/default/files/2017-05/ConsumerProtectionActNo46of2012.pdf); Media Council Code 2025 (https://new.kenyalaw.org/akn/ke/act/ln/2025/88/eng@2025-08-01); Companies (Amendment) Act 2017; Pharmacy and Poisons Act; portals https://itax.kra.go.ke/, https://eprocedures.investkenya.go.ke/, https://lands.go.ke/, http://www.nema.go.ke/
- Tanzania: *FYDP III 2021/22–2025/26*; Tanzania Investment Act No. 10 of 2022; Ministry of Finance *Budget Execution Report FY2025-26 Q1*; Afreximbank *Tanzania Country Brief* (2025); AfDB *Tanzania CSP 2021–2025 Completion Report*; IMF Country Report No. 25/164; Norad (2025); TIC *Quarterly Bulletin* (2025); NBS *Statistical Abstract* (https://www.nbs.go.tz/index.php/statistics/topic/statistical-abstract?page=1); TCRA Online Content Regulations 2020; Fair Competition Act 2003 (https://www.viwanda.go.tz/uploads/documents/sw-1618818548-fca_no_8-2003.pdf); Personal Data Protection Act 2022
- Other African data-protection law: Nigeria NDPR 2019 and DPA 2023; Rwanda Data Protection Law 2021; Ghana DPA 2012; Egypt Data Protection Law 2020
- Uganda regulator portals: https://ura.go.ug/en/dt-faqs/, https://ursb.go.ug/services/business-registration, https://obrs.ursb.go.ug, https://ubiz.go.ug, https://bou.or.ug/supervision, https://www.nema.go.ug/en/regulations/, https://www.unbs.go.ug/content.php?pg=content&src=information-resource-center, https://www.ucc.co.ug/telecommunication-licensing/, UCC QoS report (https://www.ucc.co.ug/wp-content/uploads/2024/12/QOS-August-to-September-2024.pdf), and the NSSF, NGO Bureau, business licensing, NIRA, KCCA, UMRA, UIA, UTB, UNCHE, NDA, NARO, ERB, ERA, Ministry of Education and MAAIF sites listed in [`regulatory-compliance-matrix.md`](skills/pipeline/02-company-overview/references/regulatory-compliance-matrix.md)

### Websites and articles

- Teece, D. (2007) "Explicating dynamic capabilities", *Strategic Management Journal*; Teece, D. (2010) "Business models, business strategy and innovation", *Long Range Planning* 43(2-3)
- Mangematin, V., Ravarini, A. and Sharkey Scott, P. (eds) (2017) special issue on business model innovation, *Journal of Business Strategy* 38(2), Emerald
- Zajonc, R. (1980) "Feeling and thinking", *American Psychologist*; Miller, G. (1956) "The magical number seven", *Psychological Review*; Rogers, T. and Norton, M. (2011), Harvard Business School research on topic changes and trust
- HBR articles cited in the HBR presentations guide: Denning (2004), Guber (2007), Tannen (1995), Morgan (2008)
- Barney (1991) on VRIO; Prahalad and Hamel (1990) on core competence; McClelland (1973) on competencies; Redlich (1955); Reichheld (1994)
- Gabriel, A. I. and Sheya, N. (2023) "Regulatory Framework of the Capital Market in Uganda", *KIULJ* 5(I), https://doi.org/10.59568/KIULJ-2023-5-1-08; Seijjaaka, S. (n.d.) "Challenges to the Growth of Capital Markets in Underdeveloped Economies", TrustAfrica
- Okello, T. J. O. (2011) Centenary Bank loan-recovery research report; Area, A. (2016) UDB loan-performance EMBA proposal; Alton and Hazen (2001); Nsereko (1995)
- Staal, S. and Kaguongo, W. (2003) *The Ugandan Dairy Sub-Sector*, ILRI/IFPRI/USAID; Baltenweck, I. et al. (2007) *Dairy Farming in Uganda*, ILRI Research Report 1; Kabirizi, J. M. et al. (2025) climate-smart dairy study; Balikowa (2011)
- de Melo, J. and Twum, A. (2020) *Supply Chain Trade in East Africa*, FERDI WP 263; Borin and Mancini (2019); Daly, Abdulsam and Gereffi (2016) *Regional Value Chains in East Africa*, IGC; Fritz et al. (2018)
- Infrastructure-finance studies: Dappe and Lebrand (2021); Rozenberg and Fay (2019); Fontagné et al. (2022); Collins et al. (2025); Mensah (2024); Amendolagine, Presbitero and Rabellotti (2024); CRDI (2023)
- *Sustainability Today* (Summer 2022); World Business Journal (2025), WBJAC International
- Crack A Business Kenya sector guides (2012–2018), about forty titles cited across the industry guides
- Umbrex Consulting (2025) *Market Sizing Playbook* and *Customer Retention Playbook*; McKinsey writing on the seven degrees of growth
- SaaS benchmarks: Bessemer Cloud Index and *State of the Cloud*; OpenView SaaS Benchmarks; KeyBanc SaaS Survey; ICONIQ Growth; SaaS Capital Index; NVCA Yearbook; Briter Bridges; ProfitWell pricing research; Tomasz Tunguz; David Skok (forentrepreneurs.com)
- Africa technology markets: GSMA *Mobile Economy*; Disrupt Africa; Partech Africa funding reports; GSMA Intelligence terms of use (https://www.gsmaintelligence.com/gsma-intelligence-terms-of-use/)
- Dave Chaffey, Smart Insights (RACE framework)
- Bivatec blog (beekeeping articles), bivatec.com
- DataReportal *Digital 2026: Uganda* — https://datareportal.com/reports/digital-2026-uganda
- Pew Research Center (22 March 2024) on WhatsApp and Facebook in middle-income nations — https://www.pewresearch.org/short-reads/2024/03/22/whatsapp-and-facebook-dominate-the-social-media-landscape-in-middle-income-nations/
- StatRanker mobile download speeds 2025 — https://statranker.org/digital-innovation/top-100-countries-by-mobile-internet-download-speed-median-2025/
- US Small Business Administration planning guidance — https://www.sba.gov/counseling/plan-your-business/
- Bain strategy practice — https://www.bain.com/consulting-services/strategy/; McKinsey growth, marketing and sales practice — https://www.mckinsey.com/capabilities/growth-marketing-and-sales/how-we-help-clients
- McKinsey and The Business of Fashion (2025) *State of Luxury 2025* — https://www.mckinsey.com/industries/retail/our-insights/state-of-luxury-2025
- Eleken articles on product-idea validation, UX ideas, SaaS launch, startup scaling, design-system checklists and mobile onboarding — https://www.eleken.co/blog-posts/how-to-validate-product-ideas and sibling pages
- GOV.UK Service Manual, *Plan user research for your service* — https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service
- OpenAI image prompting and image generation guides — https://developers.openai.com/api/docs/guides/image-prompting, https://developers.openai.com/api/docs/guides/image-generation
