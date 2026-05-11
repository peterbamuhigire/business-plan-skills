---
source: Agent-products business-plan audit (2026); Briter Bridges African AI talent; African AI ecosystem actors; engine synthesis
frameworks: [Agent role specs; Comp benchmark bands; Hiring stages; Retention levers]
skill: saas-agent-talent-strategy
cross-reference: [saas-agent-unit-economics-and-cogs, meta-agent-bankability-and-investor-readiness, saas-ai-talent-strategy]
---

# Agent Talent & Org-Design Template

## 1. Role Specifications

### Agent Architect (mandatory)
- Designs the multi-step decomposition (planner / worker / critic)
- Defines the autonomy ladder (assist -> suggest -> supervise -> agentic) per action class
- Designs the tool-registry strategy and tool-call schema
- Owns the agent runtime architecture
- Seniority: Staff / Principal Engineer or Lead with 3-5+ years systems experience and 1-2+ years agent / LLM-pipeline experience
- Reports to: CTO

### Tool Engineer (mandatory)
- Builds and maintains the proprietary tool registry
- Owns integration adapters to customer systems-of-record
- Reliability engineering for tools (retries, timeouts, idempotency, signed envelopes)
- Multi-vendor abstraction
- Seniority: Senior Engineer with API integration depth; 3-5+ years
- Reports to: CTO or Agent Architect

### Eval Engineer (mandatory)
- Builds offline + online eval suites
- Production sampling and human-correction signal capture
- Regression detection on model version changes
- Eval-set proprietary build on customer data (with rights)
- Cross-functional with AI Safety Lead on Class C/D eval coverage
- Seniority: Senior Engineer with ML / data infra background
- Reports to: Head of AI or CTO

### AI Safety Lead (mandatory if Class C/D actions live)
- Irreversibility-class policy
- Red-team and drill cadence
- Audit-log design and review
- Regulator engagement (KE ODPC / NG NDPC / UG NITA-U / ZA Info Reg / sectoral)
- Incident response and postmortem
- Kill-switch design
- Sign-off on autonomy expansions
- Seniority: Lead / Director-level with safety, security, or governance background
- Reports to: CTO or CEO directly (some plans put on Board safety committee)

### HITL Designer (mandatory if HITL is live)
- HITL UX (reviewer workbench)
- Escalation policy by action class
- Reviewer training and quality discipline
- Intervention-cost optimisation
- Cross-functional with Eval (reviewer signal feeds eval)
- Seniority: Senior UX designer with operations / workflow background; or product manager with UX
- Reports to: Head of Product or COO

### MLOps / Agent Infra Engineer
- Runtime, observability, tracing, deployment
- Sandbox / staging environments
- Cost engineering at infra layer
- Multi-region, residency-compliant routing where needed
- Seniority: Senior DevOps / SRE with ML systems exposure
- Reports to: CTO

### Forward Deployed Engineer (FDE) - required when vertical depth is part of the moat
- Customer-specific agent shipping
- Vertical integration work
- On-site / hybrid customer engagement
- Feedback loop into product
- Seniority: Senior engineer who can talk to customers; 4-6+ years
- Reports to: Head of CS or VP Engineering

### Agent Product Manager
- Agent roadmap
- Autonomy ladder rollout
- Customer outcomes
- Pricing input
- Cross-functional with Architect, Safety, HITL, FDE
- Seniority: Senior PM with technical depth
- Reports to: VP Product or CPO

### Domain Expert / Trainer (vertical-specific)
- Domain knowledge encoded into eval-set and prompt design
- Quality review on high-stakes outputs
- Regulator and certification engagement in sector
- Examples: paralegal / lawyer (legal); RN / clinician (health); CFA / accountant (finance); agronomist (agri); customer-service operations manager (CX)
- Seniority: Mid-senior with 5-10+ years domain experience
- Reports to: Head of Product or Domain Lead

## 2. Hiring Plan by Stage

### Pre-seed (pre-PMF, <USD 0.2M ARR or no revenue)
- Founders cover: Agent Architect (CTO) + Tool Engineer (eng founder) + Eval Engineer (early hire)
- Fractional / advisory AI Safety Lead (acceptable if no Class C/D actions live yet)
- 1 FDE if vertical commitment
- Team: 3-5 people

### Seed (USD 0.2-1M ARR)
- Agent Architect (full-time)
- Tool Engineer (full-time)
- Eval Engineer (full-time)
- AI Safety Lead (full-time mandatory if Class C/D actions live; fractional otherwise)
- HITL Designer (full-time if HITL workflow live; fractional otherwise)
- 1-2 FDE
- 1 Agent PM
- MLOps (full-time or fractional)
- Domain Expert (fractional / part-time)
- Team: 8-15 people

### Series A (USD 1-5M ARR)
- All above full-time + scale
- 2-3 FDE
- Domain Expert (full-time)
- MLOps (full-time)
- AI Safety Lead (full-time with at least one safety engineer)
- Eval Engineer team of 2-3
- Tool Engineer team of 2-4
- Agent PM team of 2
- Customer-AI-Ops team forming
- Team: 25-50 people

### Series B (USD 5-20M ARR)
- Above + team scaling
- Multiple FDEs (5-10)
- Domain Expert team
- AI Safety team (Lead + 2-3 safety engineers)
- Eval team (3-5)
- Tool Engineer team (5-10)
- Regional safety leads for multi-country deployments
- Vertical PM team
- AI Policy / Compliance team forming
- Team: 60-150 people

### Growth (USD 20M+ ARR)
- Scale all above
- Multiple regional hubs
- Sovereign-AI compliance team
- Agent-platform team if platform play
- M&A integration for vertical acquisitions
- Team: 150+

## 3. Compensation Benchmarks (loaded monthly USD; African market 2026)

| Role | Junior | Mid | Senior | Lead / Principal |
|---|---|---|---|---|
| Agent Architect | n/a (senior+) | n/a | 4,000-6,000 | 6,000-9,500 |
| Tool Engineer | 1,500-2,500 | 2,500-4,000 | 4,000-6,500 | 6,000-8,500 |
| Eval Engineer | 2,000-3,000 | 3,500-5,500 | 5,500-7,500 | 7,000-9,500 |
| AI Safety Lead | n/a | n/a | 5,500-7,500 | 7,500-12,000 |
| HITL Designer | 1,200-2,000 | 2,000-3,500 | 3,500-5,500 | 5,000-7,500 |
| MLOps | 1,800-2,800 | 3,000-4,500 | 4,500-6,500 | 6,000-8,500 |
| FDE | 2,000-3,200 | 3,200-5,000 | 5,000-7,000 | 6,500-9,000 |
| Agent PM | 1,800-2,800 | 3,000-4,500 | 4,500-7,000 | 6,500-9,500 |
| Domain Expert | 1,000-2,000 | 2,000-3,500 | 3,500-5,500 | 5,500-8,000 |

Notes:
- Lagos / Nairobi / Cape Town / Johannesburg trend 1.1-1.3x; Kigali / Kampala / Accra trend 0.9-1.1x; smaller cities lower
- Remote-USA / EU competition pulls senior comp 1.5-3x these levels; retention matters more than initial hire
- Loaded comp includes employer taxes, statutory contributions, benefits, ~25-35% on top of gross
- Equity refresh annually; AI Safety Lead and Eval Engineer should get above-grade equity given scarcity

## 4. Retention Levers (in priority order)

1. **Compensation at or above band** (review every 6 months; adjust for market drift)
2. **Equity refresh** (annual; meaningful for scarce roles)
3. **AI-specific learning budget** (USD 2-5k/year per engineer; conferences, courses, books, compute for personal projects)
4. **Public visibility** (talks, papers, open-source contributions) where compatible with IP
5. **Mission alignment** (especially for AI Safety roles; people leave when leadership is glib about risk)
6. **Career path** (Senior -> Staff -> Principal; Lead -> Director -> VP)
7. **Tooling** (provide top-tier dev / LLM / observability tools; saving USD 200/month on tools costs you a USD 8,000/month engineer)
8. **Geographic / hybrid flexibility**
9. **Onboarding investment** (90-day plan with safety drill participation, eval-loop walkthrough, customer shadow)
10. **Internal mobility** (allow rotation between Tool, Eval, Agent Architect tracks for engineers who want growth)

## 5. Build-vs-Buy Posture

| Capability | Buy | Build proprietary on top |
|---|---|---|
| Orchestration framework | LangChain / LangGraph / CrewAI / Semantic Kernel / AutoGen | Your planner / worker / critic logic |
| Eval platform | LangSmith / LangFuse / Arize / Weights & Biases / Helicone | Proprietary eval sets on customer data; vertical-specific judges |
| Observability / tracing | LangSmith / LangFuse / Helicone / Datadog APM with LLM | Custom dashboards + alerts on agent-specific anomalies |
| HITL workbench | (mostly build; some buy from Scale / Snorkel / Surge for labelling) | Yours is moat territory if HITL is core |
| Tool registry | (build) | All proprietary; this is moat |
| Sandbox / staging | (build on top of cloud) | Yes; specific to your tools |
| Vector DB / retrieval | Pinecone / Weaviate / pgvector / Chroma / Qdrant | Your indexing strategy |
| Foundation model | OpenAI / Anthropic / Google / Mistral / Meta / Cohere / local | Your model router |
| Specialist models | Hugging Face / Together / Fireworks / Replicate / providers | Your fine-tunes |

## 6. African Talent Sourcing Channels

- Carnegie Mellon Africa (Kigali)
- ALU AI track (Mauritius / Rwanda)
- Andela AI pool (pan-Africa)
- Deep Learning Indaba alumni network (pan-Africa)
- AIMS network (SA / Cameroon / Senegal / Tanzania / Ghana / Rwanda)
- Lelapa AI partners (South Africa)
- Masakhane network (pan-Africa; especially NLP for African languages)
- Awarri (Nigeria)
- EqualyzAI (pan-Africa)
- InstaDeep alumni (Tunisia / UK / BioNTech)
- University CS programmes: Lagos, Covenant, Ashesi, UCT, Stellenbosch, Strathmore, Makerere, KIST, AAU
- Black in AI Africa chapters
- Women in AI Africa
- BPO operations talent (CCI Kenya, Webhelp / Concentrix Africa, Genesys partners) for HITL Designer roles

## 7. Diversity Goals

- Gender ratio target 40%+ in technical roles by Series A
- Local-language fluency criterion for vertical agents
- Country-distribution target to align with customer geography
- Inclusion practices: structured interviews, blinded screening for senior roles, paid pre-hire trial work, candidate-friendly remote-onsite hybrid

## 8. Outsource / Buy Posture for Scarce Roles

- AI Safety Lead: fractional / advisory at pre-seed and seed; full-time at A
- Eval Engineer: contract-to-hire from senior backend / SRE with structured ML training
- Domain Expert: part-time / fractional from industry practitioners at pre-seed and seed; full-time at A for vertical depth
- AI Policy / Compliance: fractional / external counsel at seed; in-house team at B

## 9. Cross-References

- Section 10 OpEx: comp feeds Section 10 (use payroll allocation in `saas-agent-unit-economics-and-cogs`)
- Bankability: `meta-agent-bankability-and-investor-readiness` checks AI Safety Lead in seat
- Africa context: `country-context/africa-regional/africa-agent-context-extension.md`
