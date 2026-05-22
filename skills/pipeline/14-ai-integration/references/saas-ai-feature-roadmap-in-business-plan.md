---
source: Golding (Multi-Tenant SaaS Architectures) ch. 11; Walling; Mersch; engine synthesis
frameworks: [AI as feature / cost / moat / risk; per-tenant AI cost; AI roadmap by ARR milestone]
skill: 14-ai-integration (and saas-ai-strategy-in-business-plan enhancement)
cross-reference: [saas-unit-economics-and-cohort-model, saas-pricing-and-packaging-strategy, meta-digital-transformation]
---

# SaaS AI Feature Roadmap in Business Plan

## 1. The Four Lenses on AI in a SaaS Plan

AI in a SaaS business plan must be examined through four lenses:

| Lens | Question | Plan section impact |
|---|---|---|
| **AI as feature** | What does AI do for the customer? | Section 03 (Products) |
| **AI as cost** | What does the AI capability cost per tenant per month? | Section 10 (Financials) |
| **AI as moat** | Does the AI capability create defensibility, or is it a commodity API call? | Section 06 (Competitive) |
| **AI as risk** | What happens if AI cost spikes, AI model deprecates, or AI regulation changes? | Section 12 (Risk) |

A plan that only addresses "AI as feature" is incomplete.

## 2. AI as Feature — the Honest Categorisation

Be honest about which type of AI feature the plan is using:

| Type | Examples | Differentiation | Cost |
|---|---|---|---|
| **Generic LLM wrapper** | "Ask AI about your data"; chatbot on docs | Low (everyone has this) | Low ($0.001-$0.10 per query) |
| **Domain-tuned RAG** | "Answer questions using your customer's specific data" | Medium (data + prompt-engineering moat) | Medium ($0.05-$0.50 per query) |
| **Fine-tuned model** | Custom model for vertical-specific tasks | High (data + training-cost moat) | High ($1-$100 per training; per-inference cheaper) |
| **Proprietary model** | Trained from scratch on proprietary data | Very high (data + capital moat) | Very high (millions to train; ongoing infra) |
| **AI-native workflow** | The product IS AI-orchestrated (Devin, Cognition, agent products) | Highest (the whole product is the moat) | Variable but typically high |

A plan claiming "AI moat" while using a generic LLM wrapper will lose credibility with technical investors.

## 3. AI as Cost — Per-Tenant Cost Modelling

LLM and embedding costs flow directly to a tenant. Without modelling, a heavy-AI-usage tenant can destroy unit economics for the entire tier.

```
Per-tenant AI cost (monthly) = Σ (queries × cost-per-query) + (embeddings × cost-per-embedding) + (fine-tuning amortised)

Example for a vertical SaaS with AI features:
- 500 queries/month × $0.05/query (GPT-4 class) = $25
- 1,000 embeddings/month × $0.0001 = $0.10
- Total: $25.10 per tenant per month

Plan implication:
- Tier 1 ARPU: $200/month → $25 AI cost = 12.5% of revenue → margin-eating
- Tier 2 ARPU: $500/month → $25 AI cost = 5% → acceptable
- Enterprise tier: $5,000+/month → $25-100 AI cost = 0.5-2% → invisible
```

Mitigations for the margin problem:
- **Usage caps** per tier (Tier 1 gets 100 queries/month; Pro gets unlimited)
- **AI-as-add-on** rather than included (separate AI tier)
- **Pass-through pricing** ("AI usage costs are billed at cost + 20%")
- **Cheaper models** for lower-margin tiers (GPT-4 for Enterprise; Mixtral or Llama for SMB)
- **Caching** common queries (semantic cache reduces 30-60% of LLM costs)
- **Local-model fallback** for non-mission-critical features

## 4. AI as Moat — the Honest Defensibility Test

Five questions for whether AI creates real defensibility:

1. **Data moat**: Do you have proprietary training data competitors can't get? (E.g., 10 years of cooperative-management data; African-language clinical notes)
2. **Workflow moat**: Is the AI deeply integrated into a workflow that's hard to recreate? (E.g., the AI lives inside a multi-step approval process specific to your vertical)
3. **Distribution moat**: Do you reach customers in a way that's hard to replicate? (E.g., 200 cooperatives already deployed)
4. **Cost moat**: Are you running AI cheaply enough that price-undercutting is hard? (E.g., local model deployment instead of API)
5. **Brand moat**: Are you the trusted AI expert in your vertical? (E.g., "the AI dairy expert")

A plan claiming AI moat without at least 2 of these is making a marketing claim, not a strategic claim.

## 5. AI as Risk — the Risk Register Additions

Add these to Section 12 (Risk Analysis) if AI is material:

- **Cost spike** — LLM pricing changes (rare but happens; OpenAI cuts prices but anomalous spikes also occur)
- **Model deprecation** — provider deprecates the model your product depends on (GPT-3.5 → GPT-4 forced migration)
- **Performance degradation** — model behaviour changes between versions, breaking workflows
- **Regulatory** — AI regulations (EU AI Act, sector-specific rules in Kenya / Nigeria) may restrict use cases
- **Hallucination liability** — AI gives wrong answer in high-stakes context; legal liability
- **Data sovereignty** — AI provider stores customer data in a non-compliant jurisdiction
- **Vendor concentration** — depending on a single AI provider (OpenAI, Anthropic, Google) creates platform risk
- **Local-language coverage** — major LLMs have weaker Swahili, Luganda, Hausa, Amharic, Yoruba performance; quality risk

## 6. AI Roadmap by ARR Milestone

| ARR | AI maturity | Typical AI features |
|---|---|---|
| Pre-PMF | Generic LLM wrapper (1-2 use cases) | Chatbot on docs; AI summarisation; AI writing assist |
| $0-$1M | Domain-tuned RAG (3-5 use cases); AI gets a real position in the product | RAG on customer data; domain-specific workflows |
| $1-$5M | Fine-tuning starts (1-2 high-leverage models); per-tenant cost modelling installed | Vertical-specific named-entity recognition; domain summarisation; classification |
| $5-$20M | Multi-model orchestration; AI-native workflows; cost engineering | Specialised models routed by query type; semantic cache; local-model fallback |
| $20M+ | Proprietary model option; AI as competitive moat; enterprise AI compliance | Custom-trained models; on-premise AI options for enterprise |

## 7. The Build-vs-Buy Decision for AI Capability

| Component | Default (most SaaS) | When to build |
|---|---|---|
| Foundation model | Buy (OpenAI, Anthropic, Google, AWS Bedrock) | Almost never for pre-$100M ARR |
| Embedding model | Buy (OpenAI, Voyage, Cohere) | Rarely |
| Vector database | Buy (Pinecone, Weaviate, Qdrant cloud) | Build / self-host above $500k AI-cost / year |
| RAG orchestration | Build (LangChain, LlamaIndex are libraries, not products) | Always (this is your product) |
| Fine-tuning pipeline | Buy / hybrid (OpenAI fine-tuning, Together AI, HuggingFace AutoTrain) | Build only for proprietary-data competitive moat |
| Evaluation / monitoring | Buy (Langfuse, Helicone, Arize, Weights & Biases) | Always buy |

## 8. African / Multi-Language Considerations

- LLM performance on African languages varies dramatically:
  - **Swahili / Hausa / Yoruba / Amharic** are partially supported by major LLMs (GPT-4, Claude, Gemini) but with notable quality gaps for nuanced tasks
  - **Luganda / Lingala / Wolof / Tigrinya** are weakly supported
  - **Local-language fine-tuning** is an under-utilised moat (Lelapa AI, Masakhane, AfriBERT)
- Cost is USD-denominated; FX exposure is real
- Sovereign-AI / on-premise options: Cohere (Embed on-prem), Mistral local, Llama 3 self-hosted, NVIDIA NIM
- Mobile bandwidth: design for low-bandwidth AI features (no real-time streaming of long contexts; pre-process on server)
- Public-sector / regulated sectors increasingly require data-residency for AI — Cloudera / IBM watsonx / Azure OpenAI Service in-country deployment

## 9. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Per-tenant AI cost | Monthly | CFO + Head of AI |
| AI feature roadmap | Quarterly | Head of Product |
| Model deprecation watch | Monthly | Head of AI / CTO |
| AI cost-of-revenue review | Monthly | CFO |
| AI moat reassessment | Quarterly | CEO / Head of Strategy |
| Regulatory AI watch | Quarterly | Head of Legal / Compliance |

## 10. Worked Example — Ugandan AI-Enabled Vertical SaaS

**Plan:** dairy-cooperative SaaS with AI features (record-keeping summarisation, anomaly detection on milk-collection patterns, in-Luganda customer-service bot).

**AI cost modelling:**
- Summarisation: 200 queries/month × $0.02 = $4/tenant
- Anomaly detection: batch processing daily, $5/tenant/month amortised
- Luganda chatbot: 100 queries/month × $0.05 (premium for quality) = $5/tenant
- Total AI cost: $14/tenant/month

**Tier impact (UGX 750k = $200 ARPU at Tier 2):**
- AI cost as % of revenue: 7% — acceptable but margin-eating
- Mitigation: Tier 1 (UGX 250k = $67) gets summarisation only (cap 50 queries) → $1/tenant
- Tier 2 (UGX 750k = $200) gets all three features → $14/tenant
- Tier 3 (UGX 2M = $540) gets unlimited + custom anomaly thresholds → up to $30/tenant

**AI moat assessment:**
- Data moat: ✓ (proprietary cooperative-management data over time)
- Workflow moat: ✓ (AI embedded in milk-payment + extension-officer workflows)
- Distribution moat: building (200 cooperatives target)
- Cost moat: partial (using GPT-4-mini for routine; Anthropic for complex)
- Brand moat: building (Luganda-first AI dairy assistant)
- **Verdict**: 3 of 5 — real moat in development

**AI risks (added to Section 12):**
- Luganda quality degradation if model changes
- OpenAI / Anthropic pricing change
- Data-localisation (Uganda DPPA) — sensitive cooperative data must reside locally; using OpenAI is currently a compliance question
- Hallucination liability in payment calculations (mitigated: AI doesn't compute payments, only summarises)
