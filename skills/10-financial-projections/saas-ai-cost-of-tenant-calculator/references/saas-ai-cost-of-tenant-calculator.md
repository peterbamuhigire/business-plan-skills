---
source: Mersch CFO discipline; Golding multi-tenant economics; 2025 provider pricing; engine synthesis
frameworks: [Per-query cost formula; Per-tenant monthly AI cost; Sensitivity matrix on usage / model-mix / cache / FX; Break-even tenant; Top-decile tenant; Mitigation lever library]
skill: saas-ai-cost-of-tenant-calculator
cross-reference: [saas-ai-unit-economics-and-cogs, saas-ai-pricing-strategy, saas-ai-feature-roadmap-in-business-plan]
---

# SaaS AI Cost-of-Tenant Calculator — Reference Spec

## 1. Why this calculator exists

A SaaS tier design that does not compute per-tenant AI cost will produce a margin disaster: a heavy-AI tenant on a flat-priced tier can destroy the tier's contribution margin, and the founder discovers this only when revenue scales. This calculator forces the discipline at plan time.

The calculator answers:

1. Median tenant monthly AI cost (the planning number)
2. Top-decile tenant monthly AI cost (the tail-risk number)
3. Break-even tenant (the tier-design constraint)
4. Cost-as-%-of-ARPU per tier (the pricing-decision input)
5. Sensitivity to usage, model-mix, cache, FX, and provider pricing

## 2. Formula stack

### 2.1 Per-query cost

```
per-query cost (USD)
  =  prompt_tokens × input_rate_per_1k / 1000
   + completion_tokens × output_rate_per_1k / 1000
```

Apply cache:

```
effective per-query cost
  = per-query cost × (1 − cache_hit_ratio)
```

Apply model-mix (when a router is used):

```
blended per-query cost
  = Σ (model_share × per-query cost of that model)
```

### 2.2 Per-tenant monthly cost

```
per-tenant monthly AI cost (USD)
  =  queries_per_month × blended per-query cost  [token COGS]
   + embeddings_per_month × embedding_rate       [embedding COGS]
   + fine_tune_amortisation_share                [fine-tune amortisation]
   + eval_pipeline_share                          [eval allocation]
   + vector_store_share                           [vector-store COGS]
   + gpu_reservation_share                        [GPU reservation, if dedicated]
   + retraining_share                             [retraining cycle amortisation]
   + hallucination_reserve_share                  [reserve allocation]
   + ai_overhead_share                            [AI-team payroll + tooling share]
```

### 2.3 Per-tier roll-up

```
tier AI cost = per-tenant monthly AI cost × tenant_count_in_tier
tier AI cost as % of tier ARPU = per-tenant monthly AI cost / tier ARPU
tier AI contribution = (tier ARPU − per-tenant AI cost) × tenant_count_in_tier
```

### 2.4 Break-even tenant

```
break-even queries (at a tier) =
  ( tier_ARPU − fixed_per_tenant_costs ) / blended per-query cost
```

If the median tenant's queries-per-month is within 30% of break-even, the tier is margin-fragile and should be redesigned.

### 2.5 FX overlay

```
local-currency AI cost = USD AI cost × FX_corridor_rate
FX-headroom price = local-currency price × (1 + FX_buffer)
```

Set FX_buffer to 10-15% in volatile-currency markets (NGN, GHS, EGP, ZMW); 5-10% in moderate-volatility (UGX, KES, TZS); 3-5% in stable (RWF).

## 3. Worksheet structure

A spreadsheet implementation needs 8 tabs:

1. **Architecture** — the model / embedding / vector / router stack; provider list
2. **Provider rates** — input rate, output rate, embedding rate, fine-tune rate, GPU rate (per provider)
3. **Tier definitions** — tier name, ARPU (local + USD), AI features included, allowance, overage rate
4. **Usage profile per tier** — queries, prompt tokens, completion tokens, embeddings, document indexes, cache-hit assumption, model-mix share
5. **Reserves and overhead** — fine-tune cost, fine-tune cohort size, eval pipeline cost, eval allocation base, vector-store cost, GPU reservation cost, hallucination reserve %, AI overhead pool, allocation base
6. **Per-tenant cost calculation** — applies the formula stack per tier
7. **Sensitivity matrix** — usage (×0.5, ×1, ×2, ×4) × model-mix downshift × cache-hit (20/40/60/80%) × FX (-20% / base / +20%)
8. **Mitigation scenarios** — apply mitigation levers and recompute

## 4. Provider rates (2025/26 indicative; verify before use)

| Provider / model | Input per 1k | Output per 1k | Notes |
|---|---|---|---|
| OpenAI GPT-4o | $2.50 | $10.00 | Premium accuracy |
| OpenAI GPT-4o-mini | $0.15 | $0.60 | Cost-effective routine |
| OpenAI o3-mini | $1.10 | $4.40 | Reasoning-tuned |
| Anthropic Claude Sonnet 4 | $3.00 | $15.00 | Premium accuracy |
| Anthropic Claude Haiku 4 | $0.80 | $4.00 | Cost-effective premium |
| Google Gemini 1.5 Pro | $1.25 | $5.00 | Long context |
| Google Gemini 1.5 Flash | $0.075 | $0.30 | Cheapest premium-provider |
| Meta Llama 3.1 70B (self-hosted) | ~$0.20-0.50 | ~$0.20-0.50 | Hosting infra cost separate |
| Mistral Large 2 | $2.00 | $6.00 | EU-resident option |
| Cohere Command R+ | $2.50 | $10.00 | Strong RAG |
| Embeddings — OpenAI text-embedding-3-large | $0.13 / 1M tokens | n/a | |
| Embeddings — Cohere embed-multilingual-v3 | $0.10 / 1M tokens | n/a | Strong on African languages |
| Embeddings — Voyage AI | $0.12 / 1M tokens | n/a | |
| Fine-tune — OpenAI GPT-4o-mini | ~$3 / 1M training tokens | ~$3 / 1M inference tokens | |
| GPU reservation — AWS af-south-1 (Cape Town) | ~$3.50 / hour H100 spot; ~$8 / hour on-demand | n/a | 1.5-2× US/EU; reservation availability constrained |
| GPU reservation — Liquid / Cassava / Africa Data Centres | ~$2.50-4 / hour H100 (where available) | n/a | Long-term reservations limited |

Verify rates monthly — provider pricing has been moving 25-60% downward year-over-year for premium models but with structural rises in reasoning-tuned models.

## 5. Sensitivity matrix template

| Scenario | Usage | Model-mix | Cache-hit | FX | Per-tenant cost | % of ARPU | Tier contribution |
|---|---|---|---|---|---|---|---|
| Base | 1.0× | as planned | 40% | base | $X | Y% | $Z |
| Heavy use | 2.0× | as planned | 40% | base | | | |
| Power user | 4.0× | premium-heavy | 30% | base | | | |
| Cost-engineered | 1.0× | 70% cheap model | 60% | base | | | |
| Provider shock | 1.0× | as planned | 40% | base + 2× provider price | | | |
| FX shock | 1.0× | as planned | 40% | +20% local depreciation | | | |
| Combined stress | 1.5× | premium-heavy | 30% | provider +50% + FX -15% | | | |

## 6. Worked Example — Ugandan Vertical SaaS (Dairy Cooperative AI Platform)

**Product:** AI-enabled cooperative management platform; three AI features (summarisation of meeting notes; anomaly detection on milk collection; Luganda chatbot for farmer queries).

**Architecture:**
- Foundation models: Claude Haiku 4 for summarisation; GPT-4o-mini for anomaly classification; Cohere Command R for Luganda chatbot (better local-language support)
- Embeddings: Cohere multilingual-v3
- Vector store: Qdrant cloud
- Eval: Langfuse + custom Luganda eval pack
- Cache: Redis semantic cache; 45% hit rate measured

**Tiers (UGX, USD at 3,700/$):**
- Tier 1 Basic: UGX 250,000/mo (~$67) — summarisation only, 50 queries/month
- Tier 2 Standard: UGX 750,000/mo (~$200) — all three features, 200 queries/month included
- Tier 3 Pro: UGX 2,000,000/mo (~$540) — unlimited + custom thresholds

**Tier 2 per-tenant cost computation (Standard, base scenario):**
- Summarisation: 80 queries/mo × avg 800 prompt tokens + 400 completion tokens at Claude Haiku 4 rates × 0.55 (cache miss)
  - = 80 × (0.0008 × 0.80 + 0.0004 × 4.00) × 0.55 = 80 × ($0.00064 + $0.00160) × 0.55 = 80 × $0.00224 × 0.55 = $0.099
- Anomaly classification: 30 batch runs/mo × avg 2,000 prompt tokens + 200 completion at GPT-4o-mini × 0.4 cache miss
  - = 30 × (0.002 × 0.15 + 0.0002 × 0.60) × 0.40 = 30 × ($0.00030 + $0.00012) × 0.40 = 30 × $0.00042 × 0.40 = $0.005
- Luganda chatbot: 90 queries/mo × avg 600 prompt + 350 completion at Cohere Command R+ × 0.55 cache miss
  - = 90 × (0.0006 × 2.50 + 0.00035 × 10.00) × 0.55 = 90 × ($0.0015 + $0.0035) × 0.55 = 90 × $0.005 × 0.55 = $0.248
- Embeddings: 500/mo at Cohere multilingual × $0.10/1M tokens × avg 200 tokens = 500 × 200 × $0.0000001 = $0.010
- Vector store: $0.30 / tenant / month (Qdrant cloud allocation)
- Eval allocation: $200/mo eval pipeline / 100 active tenants = $2.00 / tenant
- Fine-tune amortisation: $0 in year 1 (no fine-tune yet)
- Reserve: 5% of direct cost = $0.03
- AI overhead: $4,000/mo AI team comp + tools allocated / 100 active tenants = $40.00 / tenant
- **Total Tier 2 AI cost per tenant: $0.099 + $0.005 + $0.248 + $0.010 + $0.30 + $2.00 + $0 + $0.03 + $40.00 = $42.69/month**

Wait — this looks wrong at first glance because overhead dominates. That is the correct finding: at 100 active tenants, the AI-team overhead is the dominant AI cost line. The implication: AI overhead per tenant decreases with scale. At 1,000 active tenants, overhead allocation drops to $4 / tenant and total AI cost drops to ~$7 / tenant — well within healthy margin.

**This is the value of this calculator: it forces the founder to see the scale dependency, the overhead crossover point, and the tier-design constraint at every scale.**

**Tier 2 break-even table:**

| Active tenants | AI overhead per tenant | Total AI cost per tenant | AI cost as % of $200 ARPU | Verdict |
|---|---|---|---|---|
| 50 | $80 | $82.69 | 41% | Margin-disaster |
| 100 | $40 | $42.69 | 21% | Margin-strained |
| 250 | $16 | $18.69 | 9% | Acceptable |
| 500 | $8 | $10.69 | 5% | Healthy |
| 1,000 | $4 | $6.69 | 3% | Excellent |
| 2,000 | $2 | $4.69 | 2% | Mature |

**Insight:** the plan needs to reach ~250 active tenants before AI margin is acceptable; sub-250-tenant burn is a known cost, not a surprise. The plan should make this scale-dependency visible to investors.

**Top-decile tenant (3× usage):**
- Direct AI cost (queries × 3): $0.099 × 3 + $0.005 × 3 + $0.248 × 3 + small embed/vector growth = ~$1.05
- + overhead share: at 250 tenants = $16
- Total: $17 / month — still acceptable at 250-tenant scale

**Mitigation lever scenarios (at 250 tenants):**

| Lever | Per-tenant cost | Saving |
|---|---|---|
| Base (45% cache) | $18.69 | — |
| Cache to 65% | $17.85 | $0.84 (4%) |
| Move Luganda chatbot to fine-tuned Mistral Small self-hosted | $16.20 | $2.49 (13%) |
| Combined (cache 65% + Mistral chatbot) | $15.50 | $3.19 (17%) |
| Eval pipeline reduce to $100/mo | $17.69 | $1.00 (5%) |
| All combined | $14.50 | $4.19 (22%) |

**Pricing decision** (feeding `saas-ai-pricing-strategy`):
- Tier 2 ARPU UGX 750,000 = $200; AI cost target <10% = $20
- At 250 tenants, base scenario is $18.69 / tenant = 9.3% — within target
- Tier 2 launch viable from ~250-tenant scale
- Below 250 tenants, AI is a known investment cost, not a margin issue
- Overage rate: 200 queries included; $0.04 per additional summarisation / chatbot query (covers cost at ~3× margin)

This is the calculator output that goes into the plan.

## 7. Pre-PMF version (when usage data doesn't exist)

When there is no real usage data:
- Use directional benchmarks (vertical-SaaS AI queries / tenant / month typically 100-500 for SMB; 500-3,000 for mid-market)
- Apply wide sensitivity (×0.5 to ×4)
- Use the **expected** model-mix and cache-hit (40% cache typical for vertical SaaS)
- Declare directional explicitly; do not pretend to precision
- Plan instrumentation to capture the real data within 90 days of paid customer #1

## 8. Wire-out to other skills

- **`saas-ai-unit-economics-and-cogs`** — per-tenant cost rolls up into the AI COGS waterfall and the AI Gross Margin
- **`saas-ai-pricing-strategy`** — per-tier cost is the input to allowance × overage design
- **`saas-ai-product-strategy-and-roadmap`** — cost gates feature roadmap; expensive features wait
- **`saas-ai-risk-and-stress-test`** — sensitivity scenarios become stress scenarios
- **`meta-ai-bankability-and-investor-readiness`** — cost-as-%-of-ARR is a scorecard input
- **`meta-living-plan-governance`** — per-tenant cost becomes a monthly KPI

## 9. Living-Plan Cadence

- **Weekly**: token usage per tenant; cache-hit ratio
- **Monthly**: per-tenant AI cost (median + top decile); model-mix share; provider pricing
- **Per provider change**: rate update + sensitivity rerun
- **Per architecture change**: full re-build
- **Quarterly**: full calculator review with stakeholders
