---
name: saas-ai-unit-economics-and-cogs
description: Decompose AI cost-of-revenue into a CFO-grade COGS waterfall (token COGS, embedding COGS, fine-tuning amortisation, eval COGS, vector-store COGS, GPU reservation, retraining cycles, hallucination-liability reserve) and produce the AI Gross Margin, AI Contribution Margin, AI margin contribution to blended GM, and AI-cost-as-%-of-ARR diagnostics that AI-aware investors expect. Use whenever AI is a material cost line in a SaaS plan — typically >2% of revenue or load-bearing to the product thesis. Sits on top of `saas-unit-economics-and-cohort-model`.
---

# SaaS AI Unit Economics & COGS Skill

## Overview

Generic SaaS unit economics treats AI as one cost line. AI-aware investors in 2026 require the AI cost line decomposed into its constituent waterfall, separately modelled, separately sensitised, and separately reported. This skill installs that discipline.

The output is a four-layer view of the AI cost-of-revenue:

1. **Direct AI COGS** — tokens, embeddings, fine-tuning amortisation, vector store, GPU reservation.
2. **Indirect AI COGS** — eval pipeline cost, observability / safety infra, model-router infra, caching infra.
3. **AI reserves** — hallucination-liability reserve, retraining-cycle reserve, model-migration reserve.
4. **AI overhead allocation** — share of AI-team payroll, share of AI tooling, share of governance.

Together these produce the AI Gross Margin, AI Contribution Margin per tier, blended-GM impact, AI-cost-as-%-of-ARR, and the diagnostics investors and DFIs look for.

## Use When

- AI is a material cost in a SaaS / ICT plan (typically >2% of ARR or load-bearing to product)
- Section 10 (Financial Projections) is being built for an AI-feature-led plan
- Investors or DFIs have asked for AI gross margin specifically
- A plan claims AI-native or AI-first and needs to defend the cost economics
- Pricing or packaging decisions need AI-cost sensitivity
- The plan must pass `meta-ai-bankability-and-investor-readiness`

## Do Not Use When

- AI is incidental (internal-efficiency only, no customer-facing AI cost) — use `14-ai-integration` plus generic `saas-unit-economics-and-cohort-model`
- The plan is pre-PMF and no real AI usage data exists — use directional inputs with explicit sensitivity ranges, and pair with `saas-mvp-and-product-market-fit-strategy`
- The business is not SaaS / subscription / recurring revenue

## Required Inputs

- AI architecture description (which models, which providers, RAG / fine-tuning / agentic / multi-model router)
- Provider pricing snapshot (per-1k-token, per-embedding, per-fine-tune-token, per-GPU-hour, per-vector-store-row)
- Per-tenant usage profile by tier (queries/month, tokens/query, embeddings/month, document volume)
- Cache-hit ratio (or assumed range)
- Model-mix policy (which queries route to which model)
- Eval pipeline cost (eval-runs/month × tokens-per-run × model-cost)
- Retraining cadence (quarterly / annual / triggered)
- Hallucination-liability exposure (high-stakes vs low-stakes feature mix)
- Currency exposure (USD-denominated AI cost vs local-currency ARPU)

## Workflow

1. **Document the AI architecture** in one paragraph + one diagram (or text-based component list). Without this, the cost model is fiction.
2. **Build the per-tenant AI cost** per `references/saas-ai-cost-of-tenant-calculator.md` — token COGS + embeddings + amortised fine-tune + eval share + reserve + overhead share.
3. **Build the AI COGS waterfall** — direct + indirect + reserves + overhead allocation, monthly Year 1, quarterly Years 2–5.
4. **Compute AI Gross Margin** = (AI-attributable revenue − AI COGS) / AI-attributable revenue. AI-attributable revenue uses the AI-TAM attribution discipline (`ai-tam-attribution.md`) — usually a fraction of total ARPU, not all of it, unless the product is AI-native.
5. **Compute AI Contribution Margin per tier** — for each tier: (tier ARPU × AI-attribution %) − tier AI cost. Identify tiers where AI is margin-eating.
6. **Compute blended-GM impact** — AI COGS as a share of total COGS; impact of AI on company-level GM trajectory over the 5-year plan.
7. **Compute AI-cost-as-%-of-ARR** — the headline diagnostic investors quote. Set targets: <5% (excellent), 5–10% (typical), 10–15% (margin-strained), >15% (alarm).
8. **Apply mitigation levers** in scenarios — cache-hit increase, model-mix downshift (route routine queries to cheaper models), usage caps, AI-as-add-on tier, prompt-token optimisation, response-token truncation, semantic compression.
9. **Sensitivity-test** — ±30% token usage, ±50% provider pricing, ±20pp cache-hit ratio, ±20% FX, model-deprecation forced migration cost.
10. **Stress-test** — provider doubles pricing; foundation model deprecates; hallucination event triggers reserve drawdown; GPU scarcity raises hosting cost 2×.
11. **Wire into living-plan governance** — assign cadence, owners, variance thresholds per the AI Living-Plan Cadence below.
12. **Diagnose the binding AI-cost constraint** — which lever (cache, model-mix, prompt design, tier design, pricing) most improves AI margin?

## Quality Bar

- AI architecture stated explicitly; no "we use GPT" wave-of-hand
- All cost components computed with formulas and assumptions
- AI Gross Margin and AI Contribution Margin separately computed and stated
- AI-cost-as-%-of-ARR reported as headline metric
- Tier-by-tier AI contribution stated; margin-eating tiers flagged
- Sensitivity covers usage, pricing, cache-hit, FX
- Stress scenarios cover cost spike, model deprecation, hallucination event, GPU scarcity
- Mitigation playbook explicit, with expected impact per lever
- Living-plan cadence assigned; eval / cost / margin owners named
- A sceptical CFO at a Series A AI fund would not laugh

## Anti-Patterns

- "AI cost ~5% of revenue" with no calculation behind it
- Token cost without prompt-token vs completion-token split (completion tokens are 2–4× pricier on most providers)
- Ignoring embedding cost when RAG is core to the product
- Ignoring eval cost — evals can equal 10–30% of production AI spend
- No cache-hit ratio modelled (semantic caching typically saves 30–60%)
- Single-model assumption when product clearly needs router logic
- USD-only modelling when ARPU is in local currency (FX is real)
- No hallucination-liability reserve in a regulated vertical
- No reserve for forced model migrations (these happen every 12–24 months)
- "We'll switch to cheaper models" stated as cost-reduction without quality-impact modelling

## Outputs

- AI architecture description (one paragraph + component list)
- AI COGS waterfall (monthly Y1, quarterly Y2–5)
- Per-tenant AI cost by tier
- AI Gross Margin (recurring)
- AI Contribution Margin per tier
- AI-cost-as-%-of-ARR diagnostic
- Sensitivity + stress analyses
- Mitigation playbook with prioritised levers
- Living-plan cadence assignment

## Living-Plan AI Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Per-tenant AI cost | monthly | CFO + Head of AI | +20% MoM |
| AI Gross Margin | monthly | CFO | -3pp MoM |
| AI-cost-as-%-of-ARR | monthly | CFO | >15% alarm |
| Token usage / tenant | weekly | Head of AI | +30% week-over-week |
| Cache-hit ratio | weekly | Head of AI | -10pp from baseline |
| Provider pricing watch | monthly | Head of AI / CTO | any provider change |
| Eval cost share | monthly | Head of AI | >30% of AI COGS |
| Hallucination reserve | quarterly | CFO + Head of AI | reserve drawdown event |
| Retraining-cost line | per-cycle + quarterly review | Head of AI | actual >150% planned |
| Model-mix policy | quarterly | Head of AI | competitor parity at cheaper cost |

## References

- `references/saas-ai-unit-economics-template.md` — formulas, worked example, AI COGS waterfall
- `references/saas-ai-cost-of-tenant-calculator.md` — calculator spec, sensitivity matrix
- `references/saas-ai-pricing-architecture.md` — pricing levers that protect AI margin
- `references/saas-ai-stress-test-scenarios.md` — stress scenarios with quantified impact
- `skills/saas-unit-economics-and-cohort-model/SKILL.md` — sister skill (standard SaaS unit economics)
- `skills/14-ai-integration/references/saas-ai-feature-roadmap-in-business-plan.md` — AI roadmap discipline
- `skills/meta-living-plan-governance/SKILL.md` — living-plan governance
- `book-extractions/mersch-hacking-saas-extraction.md` — CFO-grade SaaS discipline
- `book-extractions/tod-building-multi-tenant-saas-architectures-extraction.md` — multi-tenant cost realities

## Africa / Uganda Application Notes

- AI cost is USD-denominated; ARPU is typically local-currency. FX is a real margin risk; model the FX corridor explicitly (UGX 3,500-3,900/$, NGN 1,500-1,800/$, KES 128-145/$ as 2025/26 ranges).
- Cache-hit ratios are higher than typical US benchmarks in African vertical SaaS because user queries are more repetitive within tightly-defined verticals (cooperatives, clinics, schools) — model 40-60% cache-hit, not 20-30%.
- Local-language inference (Swahili, Hausa, Yoruba, Amharic, Luganda) is often more expensive per task because it requires more tokens or fine-tuned models — separately line-item.
- Eval cost in regulated verticals (health, finance) is higher because production sampling rates must be higher to meet sectoral expectations.
- Hallucination-liability reserve should reflect the regulatory environment — Kenya DPC, Nigeria NITDA / NDPC, Uganda NITA-U, South Africa Information Regulator all have evolving AI-incident expectations.
- GPU-reservation cost: if hosting in Cape Town (af-south-1), Johannesburg (africa-south1), or Liquid / Cassava / MainOne, expect 1.5-3× US/EU pricing; model the premium explicitly.
- Track all AI cost in USD for international investors, local currency for DFI / bank submissions.
