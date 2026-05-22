---
source: Golding ch. 11 (multi-tenant SaaS architectures); 2024-2026 AI-ops practice; engine synthesis
frameworks: [Multi-model vendor strategy; Model-router design; Eval pipeline operational discipline; Cost-engineering rituals; Model-deprecation calendar; AI-incident runbook]
section: 08-operations-plan
cross-reference: [saas-ai-product-strategy-and-roadmap, saas-ai-risk-and-stress-test, saas-ai-cost-of-tenant-calculator, saas-ai-unit-economics-and-cogs]
---

# AI Cost & Vendor Management Ops — Reference

The operational discipline that turns AI-as-a-feature into AI-as-a-managed-cost-line. Sits in Section 08 (Operations Plan) for AI-feature-led SaaS plans.

## 1. Multi-model vendor strategy

A single-foundation-model-provider strategy is now a known platform risk. Operating practice:

| Component | Primary | Secondary | Local fallback |
|---|---|---|---|
| Premium LLM | Anthropic Claude Sonnet 4 / OpenAI GPT-4o | OpenAI / Anthropic (the other one) | Llama 3.1 70B self-hosted |
| Cheap LLM | OpenAI GPT-4o-mini / Anthropic Haiku 4 | Google Gemini 1.5 Flash | Llama 3.1 8B self-hosted; Mistral Small |
| Local-language LLM | Cohere Command R+ (multilingual) | Lelapa / Awarri / fine-tuned local | Distilled local model |
| Embeddings | OpenAI text-embedding-3-large | Cohere embed-multilingual-v3 | BGE / E5 self-hosted |
| Vector DB | Pinecone / Qdrant cloud | Weaviate | Qdrant self-hosted |
| Eval pipeline | Langfuse | Helicone / Arize | Custom |
| Observability | Langfuse + Helicone | Arize | Custom |

Operating discipline: every primary has at least one tested secondary; every premium has a tested local fallback.

## 2. Model-router design

The router is the operational asset that protects margin and provides multi-provider resilience.

**Router policy elements:**
- **Query classification** — route by query type (factual / generative / reasoning / classification / local-language / high-stakes)
- **Cost gating** — premium model only when query value justifies
- **Cache lookup before model call** — semantic + exact-match
- **Fallback chain** — primary → secondary → tertiary on provider failure
- **Quality SLA** — per-tier model-mix policy (Pro tier guaranteed premium; Standard tier mostly cheap)
- **Eval gating** — new model variants validated against eval suite before promotion to production routing

**Router operations:**
- Routing decisions logged for analysis
- A/B test new routing policies on 5-10% traffic before full rollout
- Quarterly router policy review

## 3. Eval pipeline operational discipline

Eval is not a one-time task; it's a continuous process.

**Eval coverage build-out:**
- **Phase 1** (pre-PMF): evals on 1-3 critical user flows
- **Phase 2** ($0-$1M ARR): evals on top 5 user flows; 40% coverage of production AI behaviour
- **Phase 3** ($1-$5M ARR): evals on all material flows; 60% coverage
- **Phase 4** ($5-$20M ARR): full eval suite + production sampling; 75-85% coverage
- **Phase 5** ($20M+): institutional-grade with external audit / ISO 42001 path

**Eval cadence:**
- **Weekly**: eval suite runs on production-similar traffic; scores reported
- **Pre-deploy**: every model / prompt change must pass eval
- **Production sampling**: 0.5-5% of production calls sampled for human review (rate depends on stakes)
- **Customer-impact eval**: ad-hoc when customer reports issue
- **External / red-team eval**: quarterly for high-stakes products

**Eval ownership:**
- Head of AI + QA lead
- Domain-expert reviewers (for local-language, regulated-vertical evals)
- Customer-success team feeds production-incident eval gaps

## 4. Cost-engineering rituals (the routine that protects margin)

| Ritual | Cadence | Owner | Output |
|---|---|---|---|
| Provider price review | weekly | Head of AI | rate change ack + sensitivity rerun |
| Cache-hit ratio review | weekly | Head of AI | trend + intervention if drop |
| Token usage per tenant (median + top decile) | weekly | Head of AI | outlier list for investigation |
| Model-mix share review | monthly | Head of AI | router policy adjustment |
| Per-tenant AI cost report | monthly | CFO + Head of AI | margin trajectory + alerts |
| Prompt-token audit | quarterly | Head of AI | compression opportunities |
| Cache-strategy review | quarterly | Head of AI / Eng | semantic / exact / TTL tuning |
| Self-hosted vs API cost benchmark | quarterly | Head of AI / CFO | build vs buy decisions |
| Distillation candidate review | semi-annual | Head of AI | model-replacement opportunities |
| Annual AI cost-engineering plan | annual | CTO + CFO + Head of AI | year's cost-engineering roadmap |

## 5. Model-deprecation calendar (operational artefact)

Maintain a model-deprecation calendar showing:
- Each foundation model in use
- Provider's announced deprecation date (if any)
- Provider's typical deprecation cadence (~12-24 months for major models)
- Migration playbook readiness (eval comparison ready, alternative model identified)
- Estimated migration cost
- Last review date

Review monthly. Trigger migration sprint when deprecation announced or when alternative model demonstrates eval-better-or-equal at significantly lower cost.

## 6. AI-incident runbook (operational SOP)

| Stage | Action | Owner | Timeline |
|---|---|---|---|
| 1. Detect | Eval alert / customer report / sampling flag / monitoring alarm | Head of AI / On-call | within 15 min of trigger |
| 2. Triage | Severity classify (sev-1/2/3); impact scope; affected-customer list | Incident commander | within 30 min |
| 3. Contain | Disable feature / route to human / rollback model / restrict access | Eng on-call | within 1 hour |
| 4. Communicate | Customer comms; regulator notification per jurisdiction | CEO + Head of Comms + Head of Legal | within 4 hours (sev-1) / 24 hours (sev-2) |
| 5. Diagnose | Root cause: model / data / prompt / integration / provider / human | Head of AI + Eng | within 24-48 hours |
| 6. Remediate | Fix root cause; deploy with canary; verify with extended eval | Head of AI + Eng | as required |
| 7. Reserve drawdown | If liability event, reserve allocation triggered | CFO | per incident |
| 8. Learn | Eval-suite extension; document in decision log | Head of AI + AI committee | within 7 days |
| 9. Report | Post-mortem in monthly investor update; sev-1 in immediate board comms | CEO + CFO | per cadence |

## 7. Vendor-management operational tasks

- **EULA review** quarterly per provider + on any change notice
- **Cost reconciliation** monthly per provider
- **Outage tracking** per incident; SLA-credit collection
- **Contract renewals** with negotiation prep (volume discounts, rate locks)
- **Roadmap intelligence** — what new models / features are providers releasing; how does it affect router policy / cost / quality

## 8. Living-plan cadence

| Element | Cadence | Owner |
|---|---|---|
| Eval suite runs | weekly | Head of AI / QA |
| Production sampling review | weekly | Head of AI / QA |
| Cache-hit ratio | weekly | Head of AI |
| Token usage per tenant | weekly | Head of AI |
| Provider price watch | weekly + per-change | Head of AI |
| Model-deprecation calendar | monthly | Head of AI / CTO |
| Per-tenant AI cost report | monthly | CFO + Head of AI |
| Router policy A/B tests | per-experiment | Head of AI |
| Cost-engineering plan | annual | CTO + CFO + Head of AI |
| AI-incident log | continuous + monthly review | Head of AI |

## 9. Africa context

- Multi-region routing is operationally complex when in-region GPU capacity is constrained; plan for hybrid (US/EU training; in-region inference for residency-sensitive data)
- Provider contracts with in-country billing entities (where available) ease tax + FX management
- Local-provider partnerships (Liquid, Cassava, Africa Data Centres, MainOne) for sovereign-AI / data-residency contracts
- Outage tracking — African connectivity issues can be misclassified as AI provider outages; instrument carefully
- Mobile-money payment failures on AI-metered billing are payment-rail issues, not AI issues; separately track
