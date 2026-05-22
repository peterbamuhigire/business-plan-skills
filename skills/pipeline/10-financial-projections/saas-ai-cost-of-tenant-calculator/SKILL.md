---
name: saas-ai-cost-of-tenant-calculator
description: Build a tenant-level AI cost calculator for a SaaS business plan — per-tenant tokens × rate × model-mix × cache-hit × FX, plus embeddings, fine-tuning amortisation, eval share, retraining contribution, and hallucination-liability reserve. Produces tier-by-tier AI cost, sensitivity matrix, and worked example. Use whenever a SaaS plan has customer-facing AI features and the engine must defend per-tier tier-design and packaging against cost reality.
---

# SaaS AI Cost-of-Tenant Calculator Skill

## Overview

A tier design that ignores per-tenant AI cost will produce a margin disaster. This skill installs the calculator: a tenant-level computation of monthly AI cost from first principles, with sensitivity, scenarios, and a worked African vertical-SaaS example. It is the operating tool behind `saas-ai-unit-economics-and-cogs` and the input to `saas-ai-pricing-strategy`.

The calculator answers four questions an AI-aware investor will ask within the first 30 minutes:

1. What does the median tenant cost you in AI per month?
2. What does the top-decile tenant cost you?
3. Where does the model break — what tier × usage profile turns negative-margin?
4. What levers protect margin without degrading the customer's experience?

## Use When

- A SaaS plan has customer-facing AI features (chat, summarisation, classification, generation, RAG, agentic flows)
- Tier design or packaging decisions are being made
- A tier's margin is suspicious and needs verification
- Pricing changes are being modelled
- An investor asks "what is your AI cost per tenant?" — this skill produces the answer in a defensible format
- Plan must pass `meta-ai-bankability-and-investor-readiness`

## Do Not Use When

- AI is internal-efficiency only (no per-tenant cost) — use `14-ai-integration` cost-benefit framework instead
- Product is in pre-design stage with no architecture decisions — return after architecture is set
- Tenant cost is dominated by non-AI infra (hosting, storage, payment fees) — use `saas-unit-economics-and-cohort-model` first; this is a supplement

## Required Inputs

- Tier list with ARPU and AI-feature inclusion per tier
- Architecture: foundation model(s) used, embedding model, vector store, eval pipeline, model-router policy
- Provider pricing snapshot (per-1k input tokens, per-1k output tokens, per embedding, per fine-tune token, per GPU-hour, per vector-store row)
- Per-tenant usage assumptions (queries/month, prompt tokens/query, completion tokens/query, embeddings/month, documents indexed)
- Cache-hit ratio (semantic + exact-match)
- Fine-tune amortisation policy (e.g. $5,000 fine-tune / 1,000 active tenants / 12 months)
- Eval pipeline cost / month and active-tenant count for allocation
- Reserve policies (hallucination, retraining)
- Currency exposure (USD AI cost vs local-currency ARPU)

## Workflow

1. **Capture the architecture stack** — one paragraph + component list (model, embedding, vector DB, router, eval, observability, cache).
2. **Build the per-query cost formula** per `references/saas-ai-cost-of-tenant-calculator.md`:
   ```
   per-query cost = (prompt tokens × input rate + completion tokens × output rate) × (1 − cache-hit) × model-mix-weighted-rate
   ```
3. **Build the per-tenant monthly cost formula**:
   ```
   per-tenant monthly AI cost =
       queries × per-query cost (after cache + model mix)
     + embeddings × embedding rate
     + fine-tune amortisation share
     + eval pipeline allocation share
     + GPU reservation share (if dedicated)
     + retraining contribution share
     + hallucination reserve allocation
     + AI overhead allocation
   ```
4. **Build the per-tier roll-up** — apply the per-tenant formula for each tier's usage profile. Output: tier × cost-per-tenant × cost-as-%-of-ARPU.
5. **Build the sensitivity matrix** — three axes minimum:
   - usage (×0.5, ×1, ×2, ×4)
   - model-mix downshift (cheaper-model share 25% / 50% / 75%)
   - cache-hit ratio (20% / 40% / 60% / 80%)
   - and a fourth: FX (UGX or NGN ±20%)
6. **Identify the break-even tenant** — at what usage × pricing does the tier go negative-contribution? This is the design-of-the-tier constraint.
7. **Identify the top-decile tenant cost** — the long-tail tenant is the margin killer; usage caps or fair-use policy are tier-design outputs.
8. **Apply mitigation levers** in scenarios — list 6-8 levers with expected impact (see Mitigation Lever Library below).
9. **Produce the worked example** — at least one realistic African vertical SaaS worked through end-to-end.
10. **Wire to pricing decision** — outputs feed `saas-ai-pricing-strategy`.
11. **Wire to living plan** — cost-per-tenant becomes a monthly KPI; provider pricing watch monthly; cache-hit ratio weekly.

## Mitigation Lever Library

| Lever | Typical impact | Cost / risk |
|---|---|---|
| Semantic + exact-match cache | -30 to -60% | Cache infra + freshness risk |
| Prompt-token compression (system-prompt minimisation, schema prompting) | -10 to -25% | Engineering time |
| Completion-token truncation / structured output | -15 to -30% | Quality risk if poorly designed |
| Model-mix routing (cheap model for routine; premium for complex) | -30 to -50% | Router + eval to detect drift |
| Per-tier usage caps with overage | -20 to -40% on cost variance | Customer-experience friction |
| Local model fallback (Llama 3, Mistral, Gemma) | -50 to -90% on routed share | Hosting infra + quality risk |
| Distillation (fine-tune a small model on a big model's outputs) | -60 to -85% on routed share | Eval rigour mandatory |
| Batch processing for non-real-time | -30 to -50% on batched share | Latency change |
| RAG over fine-tuning when data freshness matters | -50 to -80% vs fine-tuning | RAG infra complexity |
| AI-as-add-on tier (separate tier, separate price) | Margin-protective | Sales-cycle complexity |

## Quality Bar

- Per-tenant cost has explicit formula, not a vibe
- Prompt tokens vs completion tokens separately treated
- Cache-hit ratio explicit and defensible
- Model-mix policy stated
- Embeddings line-itemed when RAG is used
- Eval cost allocated
- Reserves modelled when product is high-stakes
- Sensitivity covers the four core axes
- Break-even tenant identified
- Top-decile tenant identified
- Mitigation levers prioritised with expected impact
- Worked example shown end-to-end
- FX modelled if cost-currency ≠ revenue-currency
- Living-plan cadence assigned

## Anti-Patterns

- "We estimate AI cost at 5%" with no calculation
- One token rate (no input/output split)
- 20% cache-hit assumed without instrumentation
- Single-model assumption when product needs routing
- Embeddings ignored when RAG is described in product section
- No long-tail / power-user accounting
- "We'll switch to cheaper models" without quality evaluation
- Mitigation levers stated as line items without quantified impact
- Reserves omitted in regulated verticals (health, finance, legal)
- USD-only modelling when ARPU is local currency

## Outputs

- Architecture stack description
- Per-query and per-tenant cost formulas with assumptions
- Tier roll-up table (tier × ARPU × AI cost × % of ARPU × contribution)
- Sensitivity matrix on usage / model-mix / cache / FX
- Break-even tenant and top-decile tenant analysis
- Mitigation lever playbook with prioritisation
- Worked African vertical-SaaS example
- Hand-off to `saas-ai-pricing-strategy` and `saas-ai-unit-economics-and-cogs`

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Per-tenant AI cost (median) | monthly | CFO + Head of AI | +20% MoM |
| Per-tenant AI cost (top decile) | monthly | Head of AI | >2.5× median |
| Cache-hit ratio | weekly | Head of AI | -10pp from baseline |
| Token usage per query | weekly | Head of AI | +25% week-over-week |
| Model-mix share | monthly | Head of AI | shift >15pp |
| Provider pricing | as-published + monthly | Head of AI / CTO | any provider change |
| FX corridor | monthly | CFO | move >5% from plan |

## References

- `references/saas-ai-cost-of-tenant-calculator.md` — full formula spec, worksheet structure, sensitivity matrix, worked example
- `references/saas-ai-pricing-architecture.md` — how cost links to pricing
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md` — sister skill
- `skills/14-ai-integration/references/saas-ai-feature-roadmap-in-business-plan.md` — roadmap discipline
- `book-extractions/tod-building-multi-tenant-saas-architectures-extraction.md` — multi-tenant cost realities

## Africa / Uganda Application Notes

- FX overlay is mandatory; tier ARPU is local currency, AI cost is USD-denominated.
- Cache-hit ratios are typically higher in vertical-SaaS African contexts (40-60% vs US 20-30%) because query patterns repeat within tight vertical contexts.
- Local-language tokens are typically 1.5-2.5× more tokens per equivalent English content because African languages are under-represented in tokenisers; line-item this if local-language inference is core.
- If hosting in af-south-1, africa-south1, or local providers (Liquid, Cassava, Raxio, MainOne), GPU pricing is typically 1.5-3× US/EU.
- Public-sector / NGO tenants are typically high-touch / high-doc-volume → top-decile AI cost; separately analyse.
- Mobile-first customers using WhatsApp interfaces produce different token profiles (shorter prompts, more turns) than browser-using customers; model both.
