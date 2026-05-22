---
source: Walling moats chapter; 2024-2026 AI-investor diligence practice; Wardley Mapping
frameworks: [7-question AI moat test; False-moat catalogue; Wardley placement for AI; Defensibility scorecard 0-21]
skill: saas-ai-moat-and-defensibility
cross-reference: [meta-ai-valuation-adjustments, saas-ai-product-strategy-and-roadmap, saas-ai-risk-and-stress-test]
---

# SaaS AI Moat & Defensibility Checklist

## 1. The 7-question AI moat test

Score each 0-3 (0 = absent / aspirational; 1 = early signal; 2 = real but improvable; 3 = strong + compounding). Max = 21.

### Q1 — Data moat

- Do you have proprietary training / fine-tuning data that competitors cannot acquire?
- Is the data accruing (each customer / each interaction adds to the moat)?
- Can the data be replicated by scraping, licensing, or partnering with the same sources?
- Is the data licensed for AI training (or are you exposed to a future lawsuit)?

Score:
- 0: Generic / public data only
- 1: Some proprietary data, not yet at scale
- 2: Proprietary + accruing, with clear competitive advantage
- 3: Proprietary, accruing, exclusive (e.g. via institutional partnership), with provable accuracy lift in evals

### Q2 — Workflow moat

- Is the AI embedded in a multi-step workflow that's hard to replicate?
- Does the workflow integrate proprietary data, regulatory steps, multi-stakeholder approval, or domain knowledge?
- Could a competitor build a similar workflow in <6 months?

Score:
- 0: AI feature bolted on
- 1: Workflow integration begun
- 2: Deep workflow integration; hard to replicate quickly
- 3: Vertical-specific workflow with regulatory or institutional embedding

### Q3 — Distribution moat

- Do you reach customers in a way competitors can't easily match (channel partnership, embedded in a larger platform, exclusive distributor)?
- How many customers / users have you reached, and what would it cost a competitor to match?

Score:
- 0: No distribution advantage
- 1: Building distribution but not yet meaningful
- 2: Real distribution advantage in target vertical
- 3: Dominant distribution channel; competitors must build from scratch

### Q4 — Cost moat

- Are you running AI cheaper than competitors per equivalent quality output?
- Is your cost engineering (cache, model-mix, fine-tuning, local model) defensible?
- Could a well-funded competitor match your cost in <6 months?

Score:
- 0: Same provider, same models, no engineering edge
- 1: Some cost engineering; not differentiating
- 2: Clear cost advantage (e.g. distilled models, aggressive cache)
- 3: Structural cost advantage (e.g. proprietary fine-tuned models; in-region GPU reservation; local-language model trained in-house)

### Q5 — Brand / trust moat

- Are you the trusted AI expert in your vertical?
- Do customers ask for you by name when they think "AI for [vertical]"?
- Is your brand defensible across model changes (when you switch underlying model, do customers still trust the output)?

Score:
- 0: Generic brand
- 1: Building reputation
- 2: Recognised in vertical
- 3: Category-defining brand

### Q6 — Regulatory moat

- Do you have compliance, certification, or data-residency that competitors lack?
- Is the regulatory burden a barrier to new entrants?
- Are you the only AI provider for a regulated vertical (health, finance, legal, public-sector)?

Score:
- 0: No regulatory edge
- 1: Compliance posture exists; not yet differentiating
- 2: Regulatory advantage in target market
- 3: Regulatory near-monopoly (sole certified AI in vertical; sovereign-AI status)

### Q7 — Switching-cost moat

- Is the AI tied to data, integrations, training data, customer config that locks customer in?
- What does it cost a customer to switch to a competitor's AI?
- Does the lock-in compound over time (more usage → more data → more value)?

Score:
- 0: Easy to switch
- 1: Some friction
- 2: Real switching cost (data + integration + training)
- 3: Deep lock-in (years of accrued workflow / data / muscle memory)

## 2. Scoring interpretation

| Total score | Verdict | Valuation implication |
|---|---|---|
| 0-7 | Weak; "AI moat" claim should be retracted | -0.5x to -1.5x ARR multiple discount |
| 8-14 | Real moat in development; not yet unique | Neutral; small premium possible |
| 15-21 | Strong; defensible | +0.5x to +3x ARR multiple premium |

## 3. The false-moat catalogue

Common claims that are NOT moats:

| Claim | Why it's not a moat |
|---|---|
| "We use GPT-4 / Claude" | Everyone has API access |
| "We partner with OpenAI" | A partnership is a customer relationship, not a moat |
| "We fine-tuned a model" | A one-time fine-tune with no ongoing data accrual is reproducible |
| "We use RAG" | RAG is a technique, not a moat. The moat is the data fed to RAG and the workflow around it |
| "We have prompt-engineering" | Prompts are easily copied (literally screenshot) |
| "We're AI-native" | Marketing language without architectural specificity |
| "We're working on AI" | Roadmap is not a moat until shipped + adopted |
| "Our team has ex-Google ML talent" | Talent is mobile; team is a moat only if it produces non-team assets |
| "We have AI in our product" | A feature is not a moat |
| "We have proprietary algorithms" | Proprietary algorithms in the LLM era are rarely defensible vs foundation-model providers |

## 4. The foundation-model platform-risk test

For each foundation-model provider (OpenAI, Anthropic, Google, Meta, Amazon, Mistral, Cohere) that you depend on, answer:

1. What if they release a competing product in your category? (Most pressing for horizontal SaaS; less so for vertical SaaS with workflow + data moat)
2. What if they deprecate the model you depend on? (Migration cost + eval re-run + quality risk)
3. What if they raise prices 100%? (Margin shock)
4. What if their EULA changes to allow them to train on your customer data? (Compliance + competitive exposure)
5. What if they restrict your country / region? (Operational risk)
6. What if they suffer outage > 24 hours? (Service-availability risk)

For each: state probability × impact × mitigation × current readiness. A plan that depends on one provider with no mitigation is not investable for AI-aware investors.

## 5. Wardley-map placement for AI components

Wardley evolution axis: Genesis → Custom → Product → Commodity

Place each AI component:

| Component | 2026 typical placement | Moat implication |
|---|---|---|
| Foundation model (GPT, Claude, Gemini) | Product → Commodity | Cannot be your moat |
| Embedding model | Product → Commodity | Cannot be your moat |
| Vector database | Product | Not a moat |
| RAG orchestration | Custom → Product | Implementation can be moat if vertical-specific |
| Fine-tuning pipeline | Custom → Product | Moat only with proprietary data |
| Eval suite | Custom | Domain-specific evals can be moat |
| Model router | Custom | Vertical-tuned router can be moat |
| Cache layer | Product | Not a moat |
| Domain data pipeline | Custom → Genesis (for proprietary) | Real moat candidate |
| Local-language model (e.g. Lelapa Vulavula, Awarri, Masakhane) | Genesis → Custom | Strong moat in African contexts |
| Workflow integration | Custom | Real moat candidate |
| Distribution / customer relationships | Custom | Real moat candidate |

**Rule**: your moat must be in Genesis or Custom layer. Components in Commodity or moving to Commodity cannot be your moat. State this honestly in the plan.

## 6. The moat-thesis paragraph (the output)

After scoring, produce a one-paragraph moat thesis that an experienced operator would not call marketing language. Template:

> Our AI moat is principally [data / workflow / distribution / cost / brand / regulatory / switching-cost], specifically [evidence: what data is accruing / what workflow is embedded / what distribution is locked / what cost is structural / etc.]. The foundation-model platform risk is mitigated by [multi-provider strategy / vertical depth / workflow integration / local-language coverage]. Competitors could match our [generic AI capability] in [time] but would need [specific resource / data / partnership / time] to match our [moat dimensions]. Wardley placement: our moat components sit in [Custom / Genesis] layers; we deliberately do not build moats in [Commodity] layers.

## 7. Living-Plan Cadence

(Replicated from `saas-ai-moat-and-defensibility/SKILL.md`.)

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Competitor AI claim scan | monthly | Head of Strategy | new entrant with similar moat claim |
| Foundation-model commoditisation watch | monthly | Head of AI / CTO | provider releases competing capability |
| Data accrual evidence | monthly | Head of Product | accrual rate <plan |
| Moat score reassessment | quarterly | CEO + Head of Strategy | -3 points on any dimension |
| Wardley-map refresh | annual | Head of Strategy | structural shift |

## 8. African / Uganda Application Notes

- **Local-language data moat** is the most under-utilised real moat in African AI; very high Q1 score available
- **Sovereign-AI / data-residency moat** in regulated African verticals is very real; can score 3 on Q6
- **Distribution moat in vertical SaaS** (200 cooperatives, 50 clinics) is realistic Q3 = 2-3
- **Workflow moat** in mobile-money / WhatsApp / USSD-channel workflows is genuine and underappreciated
- **Brand moat** in regulated African verticals where local trust matters more than global brand recognition
- **Cost moat** via local model deployment (Llama 3 on Liquid / Cassava infra) can be real and defensible
- For African AI plans, a 15+ moat score is achievable when local-language + workflow + distribution combine
