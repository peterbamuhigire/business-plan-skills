Parent: [AI Integration & Efficiency Skill](../SKILL.md)

When to read: at the start of any plan for a SaaS, AI-enabled, agent-based, or SLA-bearing product, to declare the archetype on page one, choose the specialist skills that apply, and set the handoffs to engineering and contract work.

# AI, Agent, and SLA Layer Archetypes and Handoffs

This reference records the engine's own layered design for technology plans, established by internal capability audits in 2026 (SaaS/ICT, AI-on-SaaS, agent products, and agent SLA and commercial layers). It is engine doctrine, not a book summary. Percentage ranges that appeared in the audits are not carried over; use current, sourced benchmarks.

## 1. Layers compose; none replaces another

| Layer | Adds | Must still pass |
|---|---|---|
| SaaS operating discipline | Unit economics, ARR waterfall, cohorts, pricing and packaging, GTM motion, sales capacity, customer success, bankability, valuation, living-plan cadence | Core business-plan gates |
| AI-on-SaaS | AI cost waterfall, AI pricing architecture, AI moat against false moat, AI risk and stress tests, AI valuation premium or discount, AI bankability, AI board and investor reporting, AI talent, AI ethics, African AI context | SaaS layer |
| Agent products | Cost per resolved task (steps × tools × branches × retries), agent pricing primitives (per resolution, per outcome, per step, hybrid, intervention credits), moat against wrapper risk, autonomy and irreversibility risk, mandatory AI safety lead, agent valuation, agent KPIs, autonomy ladder | SaaS and AI layers |
| Agent SLA and commercial | Revenue recognition by pricing primitive, deferred revenue and credit reserves, SLA-credit and refund reserves, COGS against contra-revenue policy, packaging economics, outcome-pricing business case, SLA risk, SLA investor narrative, SLA valuation overlay, SLA financial controls | All three layers above |

## 2. Declare the archetype on page one

Unit economics, pricing, moat thesis, risk register, talent plan, valuation, and (for SLA plans) revenue-recognition policy and reserve method must all align with the declared archetype.

**AI archetypes**

| Archetype | Moat profile | Main risk | Investor lens |
|---|---|---|---|
| AI-native vertical SaaS | Data and workflow moat if domain data accrues | Liability for wrong outputs in regulated sectors; data-rights conflicts | Premium only if data and workflow defensibility is evidenced |
| SaaS with AI features | Weak feature moat; the product carries the business | Cost spikes forcing repricing; feature parity | AI treated as expected, not a multiplier |
| AI platform or infrastructure | Cost and integration moat | Foundation-model providers moving down the stack; price compression | Premium with developer adoption and retention; discount on thin margins |
| AI services moving to product | Distribution and domain moat | Founder dependence; product never crystallises | Discount until product margin is shown |

**Agent archetypes**

| Archetype | Primary measure | Cost driver | Main risk |
|---|---|---|---|
| Customer-service resolution agent | Resolutions per month; intervention rate | Model steps and tools per ticket | Wrong customer answers; vendor switching |
| Back-office operations agent | Tasks per month; straight-through-processing rate | Steps, system calls, retries | Irreversible errors in ledgers or stock; audit exposure |
| Multi-agent orchestrated workflow | Outcomes per month; cost per outcome | Planner, workers, critic; branches and retries | Cost runaway; loops or collusion between agents |
| Vertical agentic SaaS | Domain outcomes (cases, codes, claims) | Steps, domain tools, supervised review | Sector regulator action; misuse |
| Agent platform or infrastructure | Active agents; runtime hours; tool calls | Compute, tool gateway, observability | Foundation providers absorbing orchestration; wrapper discount |

**SLA commercial archetypes**

| Archetype | Revenue-recognition trigger | Reserve type |
|---|---|---|
| Per resolution under uptime and accuracy SLA | Point in time at successful resolution | SLA-credit accrual |
| Per outcome under a definition-of-done SLA | Point in time when the counter-party verifies the outcome | Refund reserve plus SLA credit |
| Subscription plus success fee | Two performance obligations: subscription over time, success fee at a point in time | SLA credit on subscription; refund on success fee |
| Prepaid task credits | As credits are consumed; breakage policy required | Deferred revenue plus breakage estimate |
| Multi-tier SLA (bronze, silver, gold) | Per tier over time; SLA credit per tier | Tier-specific credit reserve; watch cannibalisation |

Accounting treatment must be confirmed through the finance engine (`chwezi-accounting-doctrine`) against the current IFRS 15 or ASC 606 text.

## 3. Which skill owns each item

| Need | Skill or reference |
|---|---|
| AI cost waterfall and per-tenant AI cost | `skills/pipeline/10-financial-projections/saas-ai-unit-economics-and-cogs/`, `saas-ai-cost-of-tenant-calculator/` |
| Agent cost per resolved task | `skills/pipeline/10-financial-projections/saas-agent-unit-economics-and-cogs/` |
| AI and agent pricing | `skills/pipeline/07-marketing-sales-strategy/saas-ai-pricing-strategy/`, `saas-agent-pricing-strategy/` |
| Packaging and outcome pricing | `saas-agent-commercial-packaging-economics/`, `saas-agent-outcome-pricing-business-case/` (Section 07) |
| AI market sizing | `skills/pipeline/04-market-analysis/saas-ai-market-and-tam/` |
| Moats | `skills/pipeline/06-competitive-analysis/saas-ai-moat-and-defensibility/`, `saas-agent-moat-and-wrapper-risk/` |
| Product strategy and autonomy ladder | `skills/pipeline/03-products-services/saas-ai-product-strategy-and-roadmap/`, `saas-agent-product-strategy-and-roadmap/` |
| Talent | `skills/pipeline/09-management-team/saas-ai-talent-strategy/`, `saas-agent-talent-strategy/` |
| Risk and stress tests | `skills/pipeline/12-risk-analysis/saas-ai-risk-and-stress-test/`, `saas-agent-risk-and-stress-test/`, `saas-agent-sla-risk/` |
| Funding and grants | `skills/pipeline/11-funding-request/saas-ai-funding-stage-playbook/`, `saas-agent-funding-stage-playbook/`, `saas-agent-investor-narrative-on-sla/`; `skills/pipeline/11b-grant-proposal/saas-ai-for-good-grant-proposal/` |
| Revenue recognition, reserves, COGS policy, SLA economics | `skills/pipeline/10-financial-projections/saas-agent-revenue-recognition/`, `saas-agent-deferred-revenue-and-credit-reserves/`, `saas-agent-sla-cogs-treatment/`, `saas-agent-sla-economics-in-projection/` |
| Bankability, valuation, controls, reporting | `skills/meta-finance/meta-ai-bankability-and-investor-readiness/`, `meta-agent-bankability-and-investor-readiness/`, `meta-ai-valuation-adjustments/`, `meta-agent-valuation-adjustments/`, `meta-agent-valuation-overlay-for-sla/`, `meta-agent-revenue-recognition-policy/`, `meta-agent-sla-financial-controls/`; `skills/meta-reporting/meta-agent-board-and-investor-reporting/` |
| Implementation gates (shadow, supervised, autonomous) | `skills/pipeline/13-implementation-timeline/saas-agent-implementation-timeline/` |
| Ethics and sustainability | `skills/pipeline/16-sustainability-strategy/saas-ai-sustainability-and-ethics/`, `saas-agent-sustainability-and-ethics/` |
| Agent layer inside Section 14 | `skills/pipeline/14-ai-integration/saas-agent-integration-deep/` |
| Living-plan cadence (AI, agent, SLA) | `skills/meta-strategy/meta-living-plan-governance/SKILL.md` (AI cadence) and `references/agent-cadence-table.md` |
| African context | `country-context/africa-regional/africa-ict-saas-market-context.md`, `africa-ai-context-extension.md`, `africa-agent-context-extension.md` — dated facts; re-verify before use |

## 4. Living-document fields

Every section of a technology plan states its data feed, cadence, owner, decision-log location, variance threshold, and sunset policy, following `skills/meta-strategy/meta-living-plan-governance/references/living-business-plan-operating-model.md`.

## 5. Cross-engine handoffs for SLA-bearing products

| Work | Owner | Artefact handed over |
|---|---|---|
| Financial discipline and plan treatment (revenue recognition, reserves, cost floor, projections) | This engine | Revenue-recognition policy memo, reserve method, SLA economics in the model |
| SLA telemetry, uptime, response-time and accuracy measurement, breach detection and alerting, automated credit calculation, kill-switch wiring, evaluation coverage | Engineering (`chwezi-dev-engine`) | Telemetry specification and measured SLA history |
| SLA clauses, credit clauses, dispute resolution, force majeure, vendor-cost pass-through, foreign-exchange corridor, outcome definition, counter-party verification, insurance and indemnity | Proposals and contracts (`proposal-skills`) | Contract language set |

Revenue-recognition policy depends on contract language; reserve methods depend on telemetry quality; the cost floor depends on engineering choices. Record each dependency in the release bundle.

## 6. Known gaps to check before claiming completeness

Sector-specific SLA benchmark libraries (customer service, collections, legal, medical, agriculture); auditor acceptance of revenue-recognition memos and reserve methods; integration of SLA performance into customer health scores; SLA as a marketing differentiator; insurance and indemnity for SLA-bearing agents; vertical agent playbooks; public-sector AI procurement; multi-agent governance and agent-to-agent trust; agent-incident post-mortem library; country-by-country regulator engagement. Mark these `NOT ASSESSED` when a plan depends on them.
