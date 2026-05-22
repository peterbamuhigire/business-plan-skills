---
source: Golding (Multi-Tenant SaaS Architectures) ch. 11; 2024-2026 AI-platform decision practice; engine synthesis
frameworks: [Build / Buy / Host / Orchestrate decision per AI component; Cost / control / time trade-offs; Model-router architecture]
skill: saas-ai-product-strategy-and-roadmap
cross-reference: [saas-ai-feature-roadmap-in-business-plan, saas-ai-cost-of-tenant-calculator]
---

# AI Build / Buy / Host / Orchestrate Matrix

## 1. The matrix

For each AI component, the four options:

- **Build** — write from scratch (rare; reserved for proprietary-data moat)
- **Buy** — commercial managed service (default for most components)
- **Host** — self-host open-source (cost / control trade-off)
- **Orchestrate** — use as library / framework but build product around it

| Component | Default for most SaaS | When to depart from default |
|---|---|---|
| Foundation model | Buy (OpenAI, Anthropic, Google, AWS Bedrock, Cohere, Mistral) | Build only for proprietary-data moat at >$100M ARR. Host (self-deploy Llama 3, Mistral, Gemma) at >$500k AI cost / year for high-volume routine queries with quality-tolerant use cases |
| Embedding model | Buy (OpenAI, Cohere, Voyage) | Host (BGE, E5) at >$200k embedding cost / year |
| Vector database | Buy (Pinecone, Weaviate cloud, Qdrant cloud) | Host (Qdrant self-hosted, pgvector, Weaviate self-hosted) at >$50k vector DB cost / year |
| RAG orchestration | Orchestrate (LangChain, LlamaIndex are libraries) — build the product around them | Always — this is your product |
| Fine-tuning pipeline | Buy / hybrid (OpenAI fine-tuning, Together AI, HuggingFace AutoTrain) | Build only for proprietary-data competitive moat at scale |
| Eval / observability | Buy (Langfuse, Helicone, Arize, Weights & Biases) | Always buy; the alternative is building eval infra that distracts from product |
| Model router | Build / Orchestrate (build on top of LangChain / custom) | Always — this is a strategic asset |
| Cache layer | Build / Orchestrate (Redis + semantic cache library) | Always |
| Safety / moderation | Buy (provider-native + Lakera / Patronus) | Always buy where possible |
| Voice / speech | Buy (Deepgram, AssemblyAI, ElevenLabs, OpenAI Whisper API; or Whisper self-hosted for cost) | Host Whisper at >$30k voice cost / year |
| OCR / document understanding | Buy (Mistral OCR, AWS Textract, Google Document AI, Reducto) | Host (PaddleOCR) at very high volume |
| Local-language LLM | Buy (Cohere multilingual; Mistral; Llama-3-Multilingual) + Lelapa / Masakhane partnership where vertical-specific | Host fine-tuned local model if local-language is a moat |

## 2. The trade-off triangle

For each component, three dimensions:

- **Cost** (monthly recurring + variable)
- **Control** (ability to customise; data residency; quality control)
- **Time-to-market**

Buy maximises time-to-market and minimises cost-of-engineering. Build maximises control. Host is the middle path.

## 3. When does departure from default make sense?

### Departure to Host (self-deploy)

- Volume is high enough to amortise infra cost
- Use case is quality-tolerant (routine queries; classification)
- Data residency / compliance requires it (sovereign-AI)
- Cost engineering is a real moat
- You have the MLOps capability

### Departure to Build

- Genuine proprietary-data moat
- Domain-specific quality requirement that off-shelf models cannot meet
- Scale (>$100M ARR typical threshold)
- Research / publication is part of brand / talent strategy

## 4. Multi-provider router (recommended for almost all plans)

The router is the single most impactful architecture decision. Operating policy:

```
For each query:
  1. Classify (cost / quality requirements)
  2. Cache lookup (semantic + exact)
  3. Route to provider:
     - If quality-critical: premium model (primary; fallback to secondary)
     - If routine: cheap model (primary; fallback to local-hosted if down)
     - If local-language: language-specialist provider (primary; fallback to multilingual)
  4. On provider failure: fallback chain
  5. Log routing decision for analysis
```

## 5. Architecture archetype examples

**SMB vertical SaaS (e.g. dairy cooperative platform):**
- Foundation model: Buy (Claude Haiku 4 primary; GPT-4o-mini secondary)
- Local-language: Buy (Cohere Command R+ primary; Lelapa partnership for Luganda)
- Embeddings: Buy (Cohere multilingual)
- Vector DB: Buy (Qdrant cloud)
- RAG: Orchestrate (custom on LangChain)
- Eval: Buy (Langfuse)
- Router: Build (vertical-specific)
- Cache: Build (Redis + semantic)

**Enterprise / regulated vertical (e.g. health AI):**
- Foundation model: Buy with private deployment (Azure OpenAI; AWS Bedrock private)
- Embeddings: Buy private (Azure / AWS)
- Vector DB: Host (Qdrant self-deployed in customer's tenant)
- RAG: Build (deeply customised; regulatory traceability)
- Eval: Buy + Build (regulatory-specific evals)
- Router: Build (compliance-aware routing)
- Cache: Build (audit-trail-enabled)

**AI-platform / AI-as-infrastructure:**
- Foundation model: Multi-provider buy + selective host
- Embeddings: Multi-provider buy
- Vector DB: Host (own infrastructure to differentiate)
- RAG: Build (your product)
- Eval: Build (your product feature)
- Router: Build (your product core asset)
- Cache: Build (your product)

## 6. Investment trajectory

| ARR | Build investment | Host investment | Buy / Orchestrate spend |
|---|---|---|---|
| Pre-PMF | RAG orchestration only | None | Foundation model, embedding, vector DB, eval, observability |
| $0-$1M | + Router (basic) + Cache (basic) | None | Same |
| $1-$5M | + Router (sophisticated) + Cache (semantic) + Eval coverage build | Possibly vector DB self-host | Same; multi-provider |
| $5-$20M | + Distillation; + Local-language fine-tune | Selective LLM self-host for routine | Premium foundation models; specialist evals |
| $20M+ | + Possibly proprietary models | Significant self-host portfolio | Strategic provider partnerships |

## 7. Anti-patterns

- Building foundation models pre-$100M ARR
- Self-hosting everything to "save money" before usage justifies infra investment
- Single-provider buy with no router
- Using LangChain / LlamaIndex as the product itself (they're libraries, not products)
- "We built our own vector DB" without performance / cost / scale evidence
- Buying eval / observability is rarely a mistake; building is rarely worth it
- Cache layer assumed but not implemented

## 8. Living-plan cadence

| Element | Cadence | Owner |
|---|---|---|
| Build vs buy reassessment per component | annual | CTO + CFO |
| Host vs buy reassessment | quarterly | Head of AI + CFO |
| Multi-provider router policy | quarterly | Head of AI |
| Provider price tracking | weekly | Head of AI |
| Self-host cost benchmark | quarterly | Head of AI + CFO |
| Distillation candidate review | semi-annual | Head of AI |

## 9. Africa context

- Self-host on Liquid / Cassava / Africa Data Centres can be cost-effective for routine queries with data-residency requirements
- Multi-region routing complex when in-region capacity constrained; design hybrid (US/EU training + in-region inference for sensitive data)
- Local-language model partnerships (Lelapa, Masakhane, Awarri) — buy or co-develop — under-utilised
- Sovereign-AI tenders often require self-host or in-country hosting; plan investment accordingly
- AI infra build-out is fundable via DFI / AI-for-good capital, not just commercial — explore blended finance
