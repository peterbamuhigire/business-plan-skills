---
source: Mersch ch. 11; Cotton MSPOT; 2024-2026 AI-investor update practice
frameworks: [Monthly investor-update AI block; KPI snapshot; AI wins / losses / asks; AI risk update]
section: 11-funding-request (also used by meta-board-and-investor-reporting)
cross-reference: [meta-board-and-investor-reporting, saas-ai-unit-economics-and-cogs, saas-ai-risk-and-stress-test, meta-living-plan-governance]
---

# SaaS AI Investor Update Block

The AI section that should appear in every monthly investor update for an AI-feature-led SaaS company. ~120-250 words. Sits between the financial KPI snapshot and the strategic discussion.

## 1. Required elements

1. **AI KPI snapshot** (numbers, no narrative):
   - AI-attributable ARR (with MoM trend)
   - AI Gross Margin
   - AI-cost-as-%-of-ARR
   - Eval coverage %
   - Hallucination rate (production sampling)
   - Cache-hit ratio
   - Median + top-decile per-tenant AI cost

2. **AI wins** (1-2 bullets) — feature shipped, model deployed, cost engineered, eval coverage milestone, governance milestone

3. **AI losses / risks** (1-2 bullets, honest) — provider price shift, eval gap discovered, hallucination incident, model deprecation announced, regulatory update

4. **AI asks** (0-1 bullets) — where investor / board can help (introduction to talent, customer reference, regulatory expertise, AI specialist advisor)

5. **AI model-mix change** (if any) — router policy update, new provider added, model deprecated

## 2. Template

> **AI section.**
> **KPIs**: AI-ARR $[X] ([+/-]Y% MoM); AI GM [A]%; AI-cost-%-of-ARR [B]%; eval coverage [C]%; hallucination [D]%; cache-hit [E]%; per-tenant cost median $[F] / top-decile $[G].
> **Wins**: [(1) what shipped or improved; (2) what milestone hit]
> **Losses / risks**: [(1) honest issue; (2) emerging risk]
> **Asks**: [if applicable — specific request]
> **Model-mix update**: [if applicable — what changed in routing, providers, costs]

## 3. Worked example (Month 14 update — dairy AI platform)

> **AI section.**
> **KPIs**: AI-ARR $912k (+8% MoM); AI GM 71%; AI-cost-%-of-ARR 10.4%; eval coverage 58% (Luganda flows: 72%); hallucination 0.4%; cache-hit 47%; per-tenant cost median $7.2 / top-decile $19.1.
> **Wins**: (1) Luganda eval suite expanded to 240 test cases including 30 vet-clinic disambiguation cases; eval score 0.83 (target 0.85). (2) Anomaly-detection model migrated from Claude Haiku to GPT-4o-mini saving $1,800 / month with no eval regression.
> **Losses / risks**: (1) Cohere announced 30-day notice on Command R+ retirement; migration to Command R-latest required; eval comparison in flight; expect 2 weeks of dual-routing then full cutover. (2) Discovered eval gap on extension-officer summarisation flow when prompts exceed 4,000 tokens; coverage expanding.
> **Asks**: introduction to Lelapa AI commercial team — we'd like to discuss embedding their Vulavula model for Luganda routine queries as a cost-engineered local fallback.
> **Model-mix update**: 65% routine queries now on cheap-models (was 50%); cache-hit improved 5pp QoQ.

## 4. Anti-patterns

- "AI is going well" with no numbers
- Cherry-picked metrics (different KPIs each month)
- Hidden hallucination data
- No model-mix transparency
- Asks vague
- Risks omitted

## 5. Living-plan link

Update delivered within 7 business days of month-close. KPIs pulled from `saas-ai-unit-economics-and-cogs`, `saas-ai-cost-of-tenant-calculator`, `saas-ai-risk-and-stress-test`. Owner: CEO drafts narrative; CFO + Head of AI provide KPIs.
