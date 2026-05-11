---
source: Mersch CFO discipline; Golding multi-tenant economics; 2024-2026 AI-SaaS investor practice
frameworks: [AI COGS waterfall; AI Gross Margin; AI Contribution Margin; Blended GM impact; AI-cost-as-%-of-ARR; AI tier contribution]
skill: saas-ai-unit-economics-and-cogs
cross-reference: [saas-ai-cost-of-tenant-calculator, saas-unit-economics-and-cohort-model, saas-ai-pricing-strategy, meta-ai-bankability-and-investor-readiness]
---

# SaaS AI Unit Economics — Template

## 1. The AI COGS Waterfall (the centrepiece exhibit)

The exhibit AI-aware investors will want first. Replaces "AI ~5% of revenue" with a structured decomposition.

### 1.1 Waterfall structure

```
AI-attributable revenue                                                  [A]
  − Direct AI COGS
      − Token COGS                       [tokens × rate × (1-cache) × mix]
      − Embedding COGS                   [embeddings × rate]
      − Fine-tune amortisation           [fine-tune cost / amortisation period / tenant cohort]
      − Vector-store COGS                [vector DB cost allocated]
      − GPU reservation cost             [if dedicated GPUs]
  − Indirect AI COGS
      − Eval pipeline cost               [eval-runs × tokens × model cost]
      − Observability / safety infra     [Langfuse / Helicone / Arize / WandB]
      − Model-router infra               [routing layer]
      − Cache infra                      [Redis / vector cache]
  − AI Reserves
      − Hallucination-liability reserve  [% of AI revenue]
      − Retraining cycle reserve         [annual cycle cost / 12]
      − Model-migration reserve          [forced-migration provision]
  − AI Overhead allocation
      − AI team payroll allocation       [Head of AI, ML engineers, eval lead]
      − AI tooling allocation
      − AI governance allocation         [committee admin, audit]
= AI Gross Margin (recurring)                                            [B]
  − Adjustments for blended product (allocate fairly to non-AI features)
= AI Contribution Margin                                                 [C]
```

### 1.2 Headline metrics

| Metric | Formula | Target |
|---|---|---|
| AI Gross Margin | (A − Direct AI COGS − Indirect AI COGS − Reserves) / A | >65% (typical good); >75% (excellent) |
| AI Contribution Margin | (A − all AI COGS − overhead) / A | >40% |
| AI-cost-as-%-of-ARR | All AI COGS / Total ARR | <10% (excellent); 10-15% (typical); >15% (alarm) |
| Blended GM impact | (Generic GM − Generic GM with AI) | <5pp drag |

## 2. AI Gross Margin trajectory

AI GM should improve over plan period — cost optimisation should outpace usage growth. A typical 3-year trajectory:

| Year | AI GM | AI-cost-as-%-of-ARR | Why |
|---|---|---|---|
| Year 1 (PMF / early scale) | 50-60% | 12-18% | Overhead dominates at low tenant counts; cache + model-mix not yet optimised |
| Year 2 | 65-72% | 8-12% | Tenant scale dilutes overhead; cache + router optimisation done |
| Year 3 | 70-80% | 5-10% | Cost engineering mature; model-mix optimised; some fine-tuning displacing premium calls |

If your plan shows AI GM declining over time, the plan has a structural issue — usage growing faster than cost engineering, or product moving up-stack to more expensive models without margin protection.

## 3. AI Contribution Margin per tier

For each tier in the plan, compute the AI contribution margin as a separate exhibit. A tier with negative AI contribution margin should be redesigned or sunsetted.

| Tier | ARPU | AI-attribution % | AI-attributable ARPU | Per-tenant AI cost | AI contribution per tenant | AI contribution margin % |
|---|---|---|---|---|---|---|
| Free | $0 | n/a | $0 | $X | -$X | n/a (acquisition cost) |
| Starter | $50/mo | 30% | $15 | $5 | $10 | 67% |
| Growth | $200/mo | 50% | $100 | $25 | $75 | 75% |
| Pro | $500/mo | 60% | $300 | $50 | $250 | 83% |
| Enterprise | $5,000/mo | 40% | $2,000 | $150 | $1,850 | 93% |

Note: AI-attribution % is the share of ARPU genuinely driven by AI value (see `ai-tam-attribution.md` discipline); it is rarely 100%.

## 4. Blended GM impact

AI Gross Margin is below SaaS Gross Margin. Therefore AI introduction creates a blended-GM drag. Quantify it:

```
Blended GM = (Non-AI revenue × Non-AI GM + AI-attributable revenue × AI GM) / Total revenue
```

Worked example:
- Non-AI revenue: $4M ARR at 82% GM = $3.28M GP
- AI-attributable revenue: $1M ARR at 70% GM = $0.70M GP
- Total: $5M ARR at $3.98M GP = **79.6% blended GM**
- Drag: 82% (would-be SaaS) − 79.6% (blended) = **2.4pp**

Investors will tolerate 2-5pp blended drag if AI is driving net new growth. Beyond 5pp, the AI thesis needs to clearly explain why.

## 5. AI-cost-as-%-of-ARR: the headline diagnostic

```
AI-cost-as-%-of-ARR = (Direct AI COGS + Indirect AI COGS + Reserves + AI overhead) / Total ARR
```

| Band | What it signals | Action |
|---|---|---|
| <5% | AI is incidental cost; no margin issue | Maintain |
| 5-10% | AI is material but well-managed | Maintain + monitor |
| 10-15% | AI is meaningful margin draw; mitigation in progress | Active cost engineering |
| 15-20% | Margin-strained; pricing or cost change required | Pricing review + cost-engineering sprint |
| >20% | Alarm; AI economics broken | Re-architect or re-price |

## 6. Sensitivity exhibits

Three sensitivity matrices investors will ask for:

**Matrix A — Usage sensitivity:**

| Usage | AI cost | AI GM | AI-cost-as-%-of-ARR | Verdict |
|---|---|---|---|---|
| 0.5× plan | | | | |
| 1.0× plan (base) | | | | |
| 2× plan | | | | |
| 4× plan (power user) | | | | |

**Matrix B — Provider pricing sensitivity:**

| Provider price change | AI cost | AI GM | Verdict |
|---|---|---|---|
| -50% (price war) | | | |
| Base | | | |
| +50% (rate hike) | | | |
| +100% (provider doubles) | | | |
| +200% (provider triples; rare but happens for premium models) | | | |

**Matrix C — FX sensitivity (local-currency ARPU vs USD AI cost):**

| FX move | AI cost in local | AI GM | Verdict |
|---|---|---|---|
| -20% (currency appreciates) | | | |
| Base | | | |
| +10% (mild depreciation) | | | |
| +20% (significant depreciation) | | | |
| +40% (NGN-style shock) | | | |

## 7. Stress scenarios (feed `saas-ai-stress-test-scenarios.md`)

For each:
- Probability (high / med / low)
- Impact (AI GM change; AI-cost-as-%-of-ARR change; cash impact)
- Mitigation
- Trigger

| Scenario | Likely impact |
|---|---|
| Provider doubles pricing (Anthropic / OpenAI premium rate hike) | AI GM -10-20pp; mitigation: model-mix downshift + cache + fine-tuned alternative |
| Foundation model deprecated; forced migration | One-time $50-200k migration + eval re-run; AI GM dips 5pp for 1-2 quarters |
| Hallucination event in regulated vertical | Reserve drawdown; potential customer-churn; potential regulatory action |
| GPU scarcity raises hosting cost 2× | GPU-reserved component up 100%; mitigation: cloud-failover + multi-region |
| FX shock (local currency -20%) | AI-cost-as-%-of-ARR up by FX % × USD-share of cost |
| Single-provider vendor concentration → outage | Service degradation; eval drop; emergency router |

## 8. Mitigation playbook (priority order)

1. **Semantic + exact-match cache** — biggest typical win (-30 to -60%)
2. **Model-mix routing** — cheap model for routine; premium for complex (-30 to -50%)
3. **Prompt-token compression** — system-prompt minimisation, schema prompting (-10 to -25%)
4. **Completion-token truncation / structured outputs** — (-15 to -30%)
5. **Distillation** — fine-tune small model on big model outputs (-60 to -85% on routed share)
6. **Local model fallback** (Llama 3 / Mistral / Gemma self-hosted) — (-50 to -90% on routed share)
7. **Batch processing** for non-real-time — (-30 to -50% on batched share)
8. **Per-tier usage caps with overage** — (-20 to -40% on variance)
9. **AI-as-add-on tier** — segregate AI cost into separate revenue
10. **RAG over fine-tuning** when data freshness matters — (-50 to -80% vs fine-tuning)

## 9. Living-Plan Cadence Defaults

(Replicated from `saas-ai-unit-economics-and-cogs/SKILL.md` for convenience.)

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Per-tenant AI cost | monthly | CFO + Head of AI | +20% MoM |
| AI Gross Margin | monthly | CFO | -3pp MoM |
| AI-cost-as-%-of-ARR | monthly | CFO | >15% alarm |
| Token usage / tenant | weekly | Head of AI | +30% WoW |
| Cache-hit ratio | weekly | Head of AI | -10pp from baseline |
| Provider pricing | monthly + as-published | Head of AI | any change |
| Eval cost share | monthly | Head of AI | >30% of AI COGS |
| Hallucination reserve | quarterly | CFO + Head of AI | drawdown event |
| Retraining-cost line | per-cycle + quarterly | Head of AI | actual >150% planned |
| Model-mix policy | quarterly | Head of AI | competitor parity at cheaper cost |

## 10. Africa / Uganda Worked-Example Header

(Full worked example sits in `saas-ai-cost-of-tenant-calculator.md` Section 6.)

Key Africa-adjusted defaults:
- Cache-hit assumption: 40-60% (higher than US 20-30% for vertical SaaS)
- Local-language inference: 1.5-2.5× more tokens per equivalent English content
- GPU reservation cost: 1.5-3× US/EU when hosted in af-south-1 / africa-south1 / local providers
- FX buffer: 10-15% NGN/GHS/EGP/ZMW; 5-10% UGX/KES/TZS; 3-5% RWF/XOF
- Eval costs in regulated verticals: 1.5-2× generic (higher sampling rate)
