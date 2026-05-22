---
source: Walling moats chapter; 2024-2026 AI-investor diligence practice; Wardley Mapping
frameworks: [Real-moat checklist; False-moat catalogue with rebuttals; Wardley placement for AI components]
section: 06-competitive-analysis
cross-reference: [saas-ai-moat-and-defensibility, saas-ai-moats-and-defensibility-checklist, meta-ai-valuation-adjustments]
---

# AI Moats vs False Moats — Reference

Pointer reference for Section 06 competitive-analysis enhancement. The full discipline lives in `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/references/saas-ai-moats-and-defensibility-checklist.md`. This file is the section-04 cross-reference + the false-moat-detection table extracted for quick use.

## 1. Real-moat 7-question summary

For each AI moat claim, score 0-3 on:
1. **Data moat** — proprietary + accruing data
2. **Workflow moat** — AI embedded in hard-to-replicate workflow
3. **Distribution moat** — customer reach hard to replicate
4. **Cost moat** — running AI cheaper than competitors (structurally)
5. **Brand / trust moat** — category-defining AI brand in vertical
6. **Regulatory moat** — compliance / data residency competitors lack
7. **Switching-cost moat** — AI tied to data + integrations + training that locks customer

Score interpretation: 0-7 weak / 8-14 real-but-not-unique / 15-21 strong.

## 2. False-moat catalogue (10 most common false claims + rebuttals)

| Claim | Why it's not a moat | What would make it a moat |
|---|---|---|
| "We use GPT / Claude / Gemini" | API access is universal | The data, workflow, distribution around the model |
| "We partner with OpenAI / Anthropic / Google" | A partnership is a customer relationship | An exclusive distribution or data partnership might be |
| "We fine-tuned a model" | One-time fine-tune is reproducible | Continuous fine-tuning on accruing proprietary data |
| "We use RAG" | RAG is a technique | The data fed to RAG + the workflow around it |
| "We have prompt engineering" | Prompts are easily copied | The eval discipline + iteration pace might be |
| "We're AI-native" | Marketing language | Demonstrable architecture choices + product behaviour |
| "We're working on AI" | Roadmap is not a moat | Shipped + adopted AI with measured impact |
| "Our team has ex-Google / OpenAI ML talent" | Talent is mobile | Team + accruing data + workflow asset |
| "We have AI in our product" | A feature is not a moat | Workflow integration + switching cost |
| "We have proprietary algorithms" | Rare to defend in LLM era | Proprietary data + proprietary fine-tunes + proprietary distribution combined |

## 3. Wardley placement (where AI components sit)

| Component | Layer | Moat implication |
|---|---|---|
| Foundation model | Product → Commodity | Cannot be your moat |
| Embedding model | Product → Commodity | Cannot be your moat |
| Vector database | Product | Not a moat |
| RAG orchestration | Custom → Product | Implementation can be moat if vertical-specific |
| Fine-tuning pipeline | Custom → Product | Moat only with proprietary data |
| Eval suite | Custom | Domain-specific evals can be moat |
| Model router | Custom | Vertical-tuned router can be moat |
| Cache layer | Product | Not a moat |
| Domain data pipeline | Custom → Genesis (if proprietary) | Real moat candidate |
| Local-language model | Genesis → Custom | Strong moat in African contexts |
| Workflow integration | Custom | Real moat candidate |
| Distribution / customer relationships | Custom | Real moat candidate |

**Rule**: your moat must be in Genesis or Custom layer. Components in Commodity or moving to Commodity cannot be your moat. State this honestly in the plan.

## 4. Foundation-model platform-risk test (the dominant lens in 2026)

For each foundation-model provider you depend on, answer with evidence:

1. What if they release a competing product in your category?
2. What if they deprecate the model you depend on?
3. What if they raise prices 100%?
4. What if their EULA changes to allow training on your customer data?
5. What if they restrict your country / region?
6. What if they suffer outage > 24h?

A plan that depends on one provider with no mitigation is not investable for AI-aware investors.

## 5. Anti-patterns the section 06 enhancement guards against

- "AI moat" without specifying which of the 7 dimensions
- One-time fine-tune as the moat (without ongoing data accrual)
- API access as the moat
- Foundation-model platform risk omitted
- Wardley-map placing the moat in Commodity layer
- "AI moat" applied to LLM-wrapper products

## 6. Africa context

- Local-language data moat (Swahili / Hausa / Yoruba / Amharic / Luganda etc.) is the most under-utilised real moat available to African AI startups
- Sovereign-AI / data-residency moat in regulated African verticals is genuine
- Distribution moat in vertical SaaS (200 cooperatives, 50 clinics) is real and not replicable quickly by offshore competitors
- Workflow moat in mobile-money / WhatsApp / USSD-channel workflows is real
- Cost moat via local model deployment (Llama 3 / Mistral on Liquid / Cassava / Africa Data Centres infra) can be structural

For African plans, a 15+ moat score is achievable when local-language + workflow + distribution combine.
