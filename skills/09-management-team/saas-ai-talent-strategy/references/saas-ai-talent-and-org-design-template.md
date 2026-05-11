---
source: Cotton SaaS team-design discipline; 2024-2026 AI-talent market data; Briter Bridges African AI talent reports; engine synthesis
frameworks: [AI org chart by ARR milestone; Role × seniority × source × comp; Africa talent map; Outsource-to-build-to-buy decision; Retention strategy]
skill: saas-ai-talent-strategy
cross-reference: [africa-ai-context-extension, saas-ai-product-strategy-and-roadmap, saas-ai-risk-and-stress-test]
---

# SaaS AI Talent & Org-Design Template

## 1. AI roles by ARR milestone

| ARR | AI roles |
|---|---|
| Pre-PMF | Founder / co-founder as Head of AI; 0-1 ML engineers |
| $0-$1M | + 1-2 RAG / applied-ML engineers; + AI-aware product manager |
| $1-$5M | + MLOps / AI infra engineer; + eval / QA lead; + 1 domain-expert-as-AI-trainer |
| $5-$20M | + AI safety / governance lead; + AI policy / compliance specialist; + 2-4 additional ML engineers; + research-engineering capacity if proprietary models |
| $20M+ | Head of AI / VP AI as full role; research engineering function; multi-region AI ops |

## 2. Role definitions

| Role | Core responsibilities | Skills | Typical seniority |
|---|---|---|---|
| **Head of AI / VP AI** | AI strategy, roadmap, hiring, governance | ML + product + operating leadership | Senior |
| **Applied ML / RAG engineer** | Build & maintain AI features; eval; cost engineering | Python, ML, LLM integration, vector DBs, RAG patterns | Mid-Senior |
| **AI product manager** | Define AI feature roadmap; eval criteria; customer feedback loop | Product + AI literacy + customer empathy | Mid-Senior |
| **MLOps / AI infra** | Model deployment, monitoring, cost engineering, multi-provider router, cache, scaling | Kubernetes, observability, model serving | Mid-Senior |
| **Eval / QA lead** | Build & maintain eval suite; production sampling; human-review process | ML evaluation, domain knowledge, statistics | Mid |
| **AI safety / governance lead** | AI policy, governance committee, bias audits, ethics review | Ethics, policy, AI safety, regulatory | Senior |
| **AI policy / compliance** | Regulatory tracking, jurisdiction compliance, data residency | Legal / regulatory / policy + AI literacy | Senior |
| **Domain expert (AI-trainer)** | Curate training data, design eval cases, validate AI outputs in domain context | Deep domain + AI literacy | Mid-Senior |
| **Research engineer** (if proprietary models) | Train / fine-tune proprietary models; publish | ML research, distributed training, paper / open-source | Senior |

## 3. Outsource → Build → Buy decision

| Function | Pre-seed | Seed | Series A | Series B+ |
|---|---|---|---|---|
| AI strategy / Head of AI | Founder + fractional CTO/AI | Founder transitioning; possibly fractional Head of AI | Hire Head of AI (buy senior) | Buy VP AI |
| Applied ML / RAG | Founder + 1 hire | 1-2 hires | 3-4 hires + 1 senior | Team of 5-10 |
| AI product | Founder | 1 dedicated AI PM | 1-2 AI PMs | 2-4 AI PMs |
| MLOps / infra | Outsourced / on top of platform | 1 hire | 1-2 hires | Team of 3-5 |
| Eval / QA | Founder + freelance reviewers | 1 hire + reviewers | 1-2 + reviewer pool | Team |
| Governance | CEO / informal | Committee starting | Committee operating + compliance hire | External advisor + internal team |
| Research engineering | n/a | n/a | n/a unless proprietary models | Build only if proprietary-data moat |

## 4. African talent pool map

### Top-tier sources

| Source | Geography | Strengths |
|---|---|---|
| **Carnegie Mellon Africa** | Kigali | Top-tier ML / AI Master's; small annual cohort; recruited heavily |
| **AIMS** network (SA, Senegal, Cameroon, Ghana, Tanzania, Rwanda) | Pan-African | Mathematical sciences with AI specialisation; rigorous |
| **African Master's in Machine Intelligence (AMMI)** (AIMS partnership) | Rwanda, Ghana | Continental flagship; highly selective |
| **Deep Learning Indaba** alumni | Continental | Conference-mediated network; annual continental gathering |
| **Black in AI Africa** chapters | Continental | Community + mentorship network |
| **Lelapa AI** research / startup | South Africa | African-language NLP frontier |
| **InstaDeep** alumni (now BioNTech subsidiary) | NG / Tunisia roots, global | Premier African AI engineering precedent |
| **Andela AI talent pool** | Continental | Distributed-team trained; remote-ready |
| **Local CS departments (top)** | Makerere, Nairobi, Wits, UCT, UP, Cairo, Lagos, ABU Zaria, Addis Ababa, Khartoum, Stellenbosch | Strong undergraduates; ML postgrad programmes |
| **Awarri** + Naijaminds | Nigeria | Local-language + applied AI |
| **EqualyzAI** | South Africa | Inclusion-focused; local-language |
| **Masakhane** network (open-source) | Continental | Research collaborators |

### Sourcing approach

- **Carnegie Mellon Africa / AMMI / AIMS**: build relationships 12-24 months before hiring; sponsor projects, hackathons, scholarships
- **Deep Learning Indaba**: annual presence; sponsor; co-author papers
- **Lelapa / Masakhane**: partner on local-language work; hire from / collaborate with
- **Andela**: remote-distributed-team hiring; vetted
- **University CS departments**: internship-to-hire pipelines

### Comp benchmarks (mid-2025 indicative monthly USD)

| Role | In-country (Uganda / Tanzania / Ethiopia) | In-country (KE / GH / RW) | In-country (NG / EG) | In-country (SA) | Remote-international |
|---|---|---|---|---|---|
| Junior ML engineer | $1,200-2,500 | $1,500-3,000 | $1,500-3,500 | $2,500-4,500 | $4,000-6,500 |
| Mid ML engineer | $2,500-4,500 | $3,000-5,000 | $3,000-5,500 | $4,500-7,500 | $6,500-10,000 |
| Senior ML engineer | $4,000-7,500 | $5,000-8,500 | $5,000-9,000 | $7,500-12,000 | $9,000-15,000 |
| Head of AI / VP AI | $7,000-12,000 + equity | $8,000-13,000 + equity | $8,000-15,000 + equity | $12,000-20,000 + equity | $15,000-25,000 + equity |

## 5. Retention strategy

Top African AI talent is recruited by US/EU companies at international comp. Retention levers:

1. **Equity ladder** that vests meaningfully — equity is the most underused lever
2. **Technical leadership track** alongside management track — engineers shouldn't have to manage to grow
3. **Research / publishing time** — 10-20% of time for conferences, papers, open-source contributions
4. **Conference + publishing budget** — Deep Learning Indaba, NeurIPS, ICML, KDD attendance + sponsorship
5. **Sabbatical policy** — 6-12 weeks per 3-4 years
6. **Sponsored partnerships** — university affiliations, AIMS visiting, Masakhane involvement
7. **Mission + impact** — DFI / AI-for-good narrative resonates with talent who chose African deployment over US/EU offers
8. **Distributed team** — talent doesn't need to relocate; pick the city that fits their life
9. **Local-context as career value** — building AI that understands cooperatives, mobile money, USSD is a non-replicable career arc

## 6. Training / upskilling plan

| Programme | Frequency | Budget per head |
|---|---|---|
| Internal AI literacy (non-AI roles) | Quarterly workshops | $0 (internal) |
| External AI courses (DeepLearning.AI, fast.ai, Hugging Face) | As applicable | $500-1,500 / year |
| Conferences (Indaba, IndabaX, NeurIPS, ICML) | 1-2 / year per AI engineer | $2,000-5,000 / event |
| University partnerships (AIMS visiting, AMMI affiliate) | Annual cohort | $5,000-20,000 / year |
| External advisor / coach | Quarterly check-ins | $1,000-3,000 / quarter |

## 7. Diversity / inclusion targets

DFI-grade plans should set explicit, measurable targets:

- **Gender ratio** in AI team — typical target: 40%+ women in AI engineering
- **Country diversity** — at least 3 African countries represented in AI team for pan-African plans
- **Language coverage** of AI team — internal representation of operating-country languages
- **Age / experience mix** — junior-to-senior ratio appropriate for stage
- **Disability inclusion** — accessibility hiring practice

Targets reported quarterly; trajectory shared with DFIs / grant funders.

## 8. Key-person contingency

For each AI lead:
- Documentation discipline (architecture, decisions, evals all documented; no tribal knowledge)
- Backup ownership — a second person can run the function for 2-4 weeks
- IP assignment + NDA in employment contract
- Notice period appropriate for criticality (3-6 months for Head of AI)
- Departure scenario in `meta-living-plan-governance` trigger-replan list

## 9. Living-plan cadence

| Element | Cadence | Owner |
|---|---|---|
| Hiring plan status | monthly | Head of People + CTO |
| AI team attrition | quarterly | Head of People |
| Comp benchmark review | semi-annual | Head of People + CFO |
| Retention plan effectiveness | quarterly | Head of People |
| Training spend | quarterly | Head of People |
| AI talent landscape | semi-annual | CTO |
| Diversity targets | quarterly | Head of People |

## 10. Anti-patterns

- "We'll hire AI talent" without role specification
- LinkedIn-only sourcing assumption when most senior African AI talent isn't on public market
- Comp pegged to local SMB benchmarks (AI talent is international-tier)
- No retention plan when international competition is intense
- Diversity stated as aspiration without target
- Founder-as-permanent-Head-of-AI past Series A
- No documentation discipline; tribal knowledge concentration
