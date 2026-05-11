---
name: saas-agent-talent-strategy
description: Hiring and org plan for agent / multi-agent products. Mandatory roles (Agent Architect, Tool Engineer, Eval Engineer, AI Safety Lead, HITL Designer, MLOps, Forward Deployed Engineer); African talent map; comp benchmarks; retention; build-vs-buy of supervision infrastructure. Sits on top of `saas-ai-talent-strategy` and makes the AI Safety Lead a mandatory rather than optional role.
---

# SaaS Agent Talent Strategy Skill

## Overview

AI-feature SaaS hiring (handled by `saas-ai-talent-strategy`) covers ML Engineer / Applied-ML / AI PM / Prompt Engineer / MLOps / AI Safety Lead (optional). **Agent talent strategy** makes the AI Safety Lead **mandatory** (because of irreversibility risk) and adds agent-specific roles: Agent Architect (designs planner / worker / critic), Tool Engineer (builds + maintains the tool registry and integrations), Eval Engineer (builds + runs the eval-loop on production data), HITL Designer (designs the human-in-the-loop UX and policy), Forward Deployed Engineer (customer-specific agent shipping where vertical depth is the moat).

This skill installs the agent team composition discipline.

## Use When

- A SaaS plan ships an agent or multi-agent product
- Section 09 is being built for an agent-product plan
- The plan claims agent autonomy in Class C / Class D actions (must show AI Safety Lead in seat)
- Investor / DFI diligence on team capacity is upcoming
- Talent-cost projections for Section 10 need agent-specific roles
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- AI is internal-efficiency only — use generic `09-management-team` + `saas-ai-talent-strategy`
- The plan is too early (pre-PMF) for full team specification — use directional roles and milestones

## Required Inputs

- Agent archetype (single-agent / multi-agent / vertical / platform)
- Action class taxonomy (A/B/C/D)
- Customer count and trajectory
- ARR trajectory
- Geography (where you hire, what compensation market, talent pool reality)
- Build-vs-buy posture for orchestration framework, eval platform, observability
- Customer-deployment model (self-serve / forward-deployed / hybrid)
- Existing team and skills audit

## Workflow

1. **Map the mandatory agent roles** per `references/saas-agent-talent-and-org-design-template.md`:
   - **Agent Architect** — designs the multi-step decomposition; planner / worker / critic; tool registry strategy; autonomy ladder
   - **Tool Engineer** — builds and maintains the tool registry; integrations; vendor abstraction; reliability engineering for tools
   - **Eval Engineer** — builds and runs the eval-loop; offline + online; human-correction signal capture; regression detection
   - **AI Safety Lead** — **mandatory** — irreversibility-class policy; red-team / drill cadence; audit-log; regulator engagement; incident response; kill-switch design
   - **HITL Designer** — human-in-the-loop UX; escalation policy; HITL reviewer training; intervention-cost optimisation
   - **MLOps / Agent Infra** — runtime; observability; tracing; deployment; sandbox / staging; cost engineering at infra layer
   - **Forward Deployed Engineer** (FDE) — customer-specific agent shipping; vertical depth; integration work; required when vertical moat is part of thesis
   - **Agent Product Manager** — agent roadmap; autonomy ladder; customer outcomes; pricing input
   - **Domain Expert as Trainer** — vertical knowledge encoded into eval-set and prompt design (legal, medical, financial, agronomic, etc.)

2. **Stage the hiring plan** by ARR / autonomy milestone:
   - **Pre-seed / pre-PMF:** founders cover most; fractional AI Safety Lead acceptable; one FDE
   - **Seed (USD 0-1M ARR):** Agent Architect + Tool Engineer + Eval Engineer + AI Safety Lead (full-time mandatory if Class C/D actions live) + 1 FDE
   - **Series A (USD 1-5M ARR):** above + HITL Designer + Agent PM + MLOps + 2-3 FDEs
   - **Series B (USD 5-20M ARR):** above + Domain Expert team + multiple FDEs + Customer-AI-Ops team
   - **Growth (USD 20M+ ARR):** above + regional safety leads + vertical PM team + AI policy / compliance team

3. **Compensation benchmarks** — set salary bands using `references/saas-agent-talent-and-org-design-template.md`. African market reality: AI Safety Lead and Eval Engineer are scarce and command premium (often 1.5-2.5x equivalent ML Engineer comp); Agent Architect 1.3-1.8x; Tool Engineer 1.0-1.2x typical senior engineer; FDE 1.1-1.3x senior engineer.

4. **Build-vs-buy decisions:**
   - Orchestration framework: typically buy (LangChain / LangGraph / CrewAI / Semantic Kernel / AutoGen) and build proprietary layer on top
   - Eval platform: buy + customise (LangSmith / LangFuse / Arize / Weights & Biases) for general; build proprietary eval sets on customer data
   - Observability: typically buy (Helicone / LangSmith / LangFuse)
   - Tool registry: build proprietary (this is moat territory)
   - HITL workbench: buy or build; depends on vertical depth
   - Sandbox / staging environment: build (specific to your tool set)

5. **Retention plan** — agent talent is scarce; retention is more important than initial hire:
   - Comp at or above market band; review every 6 months
   - Equity refresh annually
   - AI-specific learning budget (conferences, courses, compute for personal projects)
   - Public visibility (talks, papers, open-source contributions) where compatible with IP
   - Mission alignment for AI Safety roles
   - Avoid "we'll figure it out" leadership; safety / eval people leave fast when leadership is glib about risk

6. **African talent map** — where to recruit and the constraints:
   - **Carnegie Mellon Africa (Kigali)** — AI / ML graduates; small cohort
   - **African Leadership University AI track (Mauritius / Rwanda)** — graduates
   - **Andela AI pool** — pan-African; mid-senior
   - **Deep Learning Indaba alumni network** — pan-African
   - **AIMS network (SA / Cameroon / Senegal / Tanzania / Ghana / Rwanda)** — strong fundamentals
   - **Lelapa AI (SA) / Masakhane (pan-Africa) / Awarri (Nigeria) / EqualyzAI** — African AI research community
   - **InstaDeep alumni** (Tunisia/UK; BioNTech acquisition precedent)
   - **University of Lagos / UNILAG, Covenant University, Ashesi, UCT, Stellenbosch, Strathmore, Makerere, KIST, Addis Ababa University, AAU** — CS / ML talent pipelines
   - **Remote-first or remote-fractional for AI Safety Lead** — given scarcity, fractional / advisory / cross-border arrangement often realistic
   - **South Africa is the densest agent-engineering market in SSA** — consider hub model with SA core + distributed engineering

7. **Diversity and inclusion** — gender ratio in AI talent in Africa is improving but still skewed; deliberate sourcing matters. Local-language fluency is often a hiring criterion for vertical agents.

8. **Outsource-build-buy posture** — fractional AI Safety Lead from external advisors (e.g. Africa AI Safety Consortium, external lawyers with AI specialism) is acceptable at seed; must convert to full-time by A.

9. **Wire to Section 10** — compensation projections feed Section 10 OpEx. Agent team payroll allocates partly to COGS (`saas-agent-unit-economics-and-cogs` overhead allocation, default 60% to COGS).

10. **Wire to bankability** — `meta-agent-bankability-and-investor-readiness` checks "AI Safety Lead in seat" as a scorecard item.

## Quality Bar

- All mandatory roles listed with seniority and full-time / fractional status
- AI Safety Lead role filled (or fractional path explicit if pre-seed)
- Hiring plan staged by ARR / autonomy milestone
- Compensation bands set against market benchmarks
- Build-vs-buy decisions explicit per category
- Retention plan with comp, equity, learning, mission components
- African talent map referenced; sourcing channels named
- Diversity and local-language hiring criteria stated where relevant
- Outsource-build-buy posture for AI Safety + Eval explicit
- Cross-references to Section 10 (compensation costs) and bankability

## Anti-Patterns

- AI Safety Lead role optional or "we'll add later" when Class C/D actions are live — bankability impossible
- Single ML Engineer expected to cover Agent Architect + Tool + Eval + Safety
- No HITL Designer despite an active HITL workflow — UX and policy decay
- No Forward Deployed Engineer when vertical depth is the moat — moat does not materialise
- Compensation set at generic-engineer benchmark for scarce AI talent — recruitment fails
- "We'll outsource AI Safety" without specifying provider and cadence
- "We don't need an Eval Engineer because the model is good" — production agents need continuous eval
- All-remote AI Safety with no in-region presence in regulated markets — regulator engagement weakens
- Treating Domain Expert as a side-quest rather than a productised role for vertical agents

## Outputs

- Org chart for current stage + next stage
- Mandatory roles inventory with seniority + full-time / fractional / advisor
- Hiring plan by ARR / autonomy milestone
- Compensation bands by role and seniority
- Build-vs-buy posture per category
- Retention plan with concrete levers
- African talent sourcing map (where applicable)
- Outsource-build-buy posture for AI Safety + Eval
- Cross-reference to Section 10 costs and to bankability scorecard

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI Safety Lead retention signal | monthly | Head of People + CEO | flight risk signal |
| Agent team attrition | quarterly | Head of People | >15% |
| Hiring plan vs ARR | quarterly | CEO + Head of People | <80% on plan |
| Compensation market scan | semi-annual | Head of People | band drift >10% |
| Build-vs-buy posture review | annual | CTO | structural shift in vendor landscape |
| Domain expert recruitment | quarterly | Head of Product + Head of AI | vertical move |
| Diversity metrics | quarterly | Head of People | structural skew |

## References

- `references/saas-agent-talent-and-org-design-template.md` — role specs, comp bands, hiring stages
- `skills/09-management-team/saas-ai-talent-strategy/SKILL.md` — AI talent parent
- `skills/09-management-team/SKILL.md` — generic management team section
- `skills/saas-sales-org-design-and-capacity-planning/SKILL.md` — sales org pairing
- `book-extractions/cotton-run-a-saas-business-extraction.md` — hiring discipline
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit
- `country-context/africa-regional/africa-ai-context-extension.md` — African AI talent context
- `country-context/africa-regional/africa-agent-context-extension.md` — African agent context

## Africa / Uganda Application Notes

- **AI Safety Lead scarcity** in Africa is severe; consider fractional / remote-first / advisory at seed; full-time by A is mandatory for any plan with Class C/D agent actions and regulated-sector customers.
- **Eval Engineer scarcity** — second-scarcest role. Consider rotation from senior backend / SRE talent with focused training; ALU AI track + Deep Learning Indaba alumni are sourcing channels.
- **Agent Architect** can often be sourced from senior ML / backend engineers with 6-12 months of agent-product exposure; Andela AI pool is a sourcing channel.
- **Tool Engineer** is the most-available role; senior backend engineers with API integration experience adapt readily; UG / KE / NG have strong pools.
- **HITL Designer** — combine product / UX with operations knowledge; African operations-savvy designers can be sourced from BPO / call-centre operations backgrounds (CCI Kenya, Genesys partners, Webhelp / Concentrix Africa).
- **Forward Deployed Engineer** — vertical-specific; pair domain knowledge with engineering; CMU-Africa graduates are a strong source.
- **Compensation realities** — AI Safety Lead in Nairobi / Lagos / Cape Town / Kigali commands USD 4,500-9,500 / month loaded; Eval Engineer USD 3,500-7,000; Agent Architect USD 4,000-8,500; FDE USD 3,500-6,500; Tool Engineer USD 2,500-5,000. Remote-USA roles compete at 1.5-3x these levels — retention strategy must address.
- **Local-language fluency** as a hiring criterion is genuine for vertical agents (Swahili / Hausa / Yoruba / Amharic / Luganda / Lingala / Zulu / Xhosa / Wolof / Tigrinya).
- **Sovereign-AI procurement** may require local-citizen / local-resident headcount minima; plan for this when targeting public-sector customers.
- **Outsource-build-buy posture** — initial AI Safety advisory can be from external consultancies (Africa AI Safety Consortium, Lelapa AI partners, EqualyzAI partners) with quarterly engagement; convert to full-time by A.
- **Talent-flight risk** — pan-African AI talent is heavily recruited by US / EU / UAE remote roles; retention plan must combine comp + mission + equity + learning + visibility.
