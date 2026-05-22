---
name: meta-ai-valuation-adjustments
description: AI premium / discount overlay on top of standard SaaS valuation (`meta-valuation` + `saas-valuation-and-fundraising-strategy`). Produces explicit multiple adjustments by archetype, by moat evidence, by margin trajectory, by governance maturity, and by foundation-model platform risk. Use when an AI-feature-led SaaS plan is being valued for a priced round, a secondary, or strategic-acquisition negotiation.
---

# Meta — AI Valuation Adjustments Skill

## Overview

Standard SaaS valuation methods (ARR multiple, Rule-of-40-adjusted multiple, DCF, venture method, Berkus / Scorecard at early stage) give the SaaS base case. AI changes the multiple — sometimes up, sometimes down — and the engine should model both directions explicitly rather than assuming "AI premium." This skill installs the adjustment logic.

The output is a valuation range with: SaaS base multiple → AI premium / discount → adjusted multiple → adjusted enterprise value, with explicit reasoning for each adjustment.

## Use When

- AI-feature-led SaaS plan is being valued for a priced round, secondary, or strategic acquisition
- A term sheet is being negotiated and AI thesis affects the valuation
- A board-level discussion of valuation strategy needs an AI overlay
- A comparison set (precedent multiples) needs AI-adjustment to be applicable
- Strategic-buyer modelling needs AI-attribution discipline

## Do Not Use When

- AI is internal-efficiency only — use `meta-valuation` + `saas-valuation-and-fundraising-strategy`
- Plan is bank-loan only (asset / DSCR-based valuation; AI is incidental)
- Valuation is fixed by tender / regulatory mechanism

## Required Inputs

- Standard SaaS valuation output (`saas-valuation-and-fundraising-strategy` + `meta-valuation`)
- AI bankability scorecard (`meta-ai-bankability-and-investor-readiness`)
- AI moat score (`saas-ai-moat-and-defensibility`)
- AI economics (`saas-ai-unit-economics-and-cogs`)
- Foundation-model platform-risk statement
- Comparable transactions and trading multiples (with AI-attribution)

## Workflow

1. **Establish the SaaS base multiple** from `saas-valuation-and-fundraising-strategy`. This is the starting point. AI premium/discount adjusts from here, not from a hypothetical "AI multiple."
2. **Declare the archetype** per Part 1 of `book-extractions/ai-on-saas-business-plan-audit-2026.md` (AI-native vertical SaaS / SaaS-with-AI-features / AI-platform / AI-services productising). Multiples differ by archetype.
3. **Apply the AI-premium drivers** — each adjustment with reasoning and magnitude:
   - **Real data moat** (proprietary data accruing, not buyable) → +0.5x to +2x
   - **Real workflow moat** (AI embedded in workflow with switching cost) → +0.25x to +1x
   - **AI-native product** (the product IS AI, not augmented) → +0.5x to +1.5x
   - **Demonstrated AI gross margin >70%** in regulated vertical → +0.25x to +0.75x
   - **Eval discipline + governance maturity** (reduces incident risk) → +0.1x to +0.5x
   - **Local-language / sovereign-AI moat** in regulated jurisdiction → +0.25x to +1x
   - **AI-revenue >40% of total ARR + growing** → +0.25x to +0.75x
4. **Apply the AI-discount drivers** — each adjustment with reasoning and magnitude:
   - **LLM-wrapper / commodity-feature exposure** → -0.5x to -1.5x
   - **Foundation-model platform risk** (provider could enter category) → -0.25x to -1.5x
   - **AI-cost-as-%-of-ARR >15%** → -0.25x to -0.75x
   - **Declining AI Gross Margin trajectory** → -0.25x to -1x
   - **Hallucination-liability exposure unreserved** in regulated vertical → -0.5x to -2x
   - **Eval coverage <30%** → -0.25x to -0.75x
   - **Vendor concentration >80% single provider** → -0.25x to -0.5x
   - **Training-data provenance gap** (lawsuit risk) → -0.5x to -2x
   - **No AI governance committee + AI policy** → -0.1x to -0.5x
5. **Apply the foundation-model platform-risk adjustment** explicitly. This is the most-asked diligence question in 2026 AI valuation. Magnitude scales with how vertical / how moated the company is — vertical specialists with workflow moat have less platform risk than horizontal LLM-wrappers.
6. **Apply the comparable-transaction overlay** — adjust the multiple toward observed AI premiums / discounts in recent transactions in the same vertical / stage.
7. **Run the sensitivity** — show valuation range across plausible adjustment combinations (Bull / Base / Bear).
8. **Apply the strategic-buyer overlay** — if the plan contemplates strategic acquisition, model how a buyer with foundation-model exposure (Microsoft, Google, Amazon) values you vs a buyer without (Salesforce, Oracle, ServiceNow, vertical incumbents).
9. **State the valuation thesis** in one paragraph that survives an experienced investor's first push-back.
10. **Wire to living plan** — adjustment factors are dynamic; reassess on major comparable transaction, major foundation-model release, regulatory shift.

## Archetype-Adjusted Multiple Bands (2026 indicative)

| Archetype | SaaS base | AI premium range | AI discount range | Net plausible band |
|---|---|---|---|---|
| **AI-native vertical SaaS (Rule-of-40 ≥40, ARR growth >50%)** | 10-15x ARR | +1x to +3x | -0.5x to -1.5x | 10x to 17x |
| **SaaS-with-AI-features (Rule-of-40 ≥30)** | 6-10x ARR | +0.25x to +1x | -0.5x to -1x | 6x to 11x |
| **AI-platform (Rule-of-40 ≥30, GM ≥50%)** | 8-12x ARR | +1x to +3x | -1x to -3x | 7x to 14x |
| **AI-services productising (mixed)** | 1.5-4x revenue | +0.5x to +1x | -0.5x to -1x | 1.5x to 5x |

(These bands are indicative; specific transactions and stage adjust them materially.)

## Quality Bar

- Archetype declared
- Each premium / discount adjustment named, sourced, and quantified
- Foundation-model platform-risk adjustment explicit
- Comparable-transaction overlay applied
- Bull / Base / Bear range produced
- Strategic-buyer overlay applied where relevant
- Thesis paragraph defensible against pushback
- Living-plan cadence on adjustment factors

## Anti-Patterns

- "AI is hot, multiply by 1.5x" without specifying which drivers
- AI premium claimed without moat evidence
- Foundation-model platform risk omitted
- Only premiums applied; discounts ignored
- No comparable-transaction reference
- No strategic-buyer overlay when exit-strategy contemplates strategic acquisition

## Outputs

- Adjusted valuation range (Bull / Base / Bear)
- Per-adjustment table (driver × magnitude × reasoning)
- Foundation-model platform-risk statement and adjustment
- Comparable-transaction overlay
- Strategic-buyer overlay (if relevant)
- Valuation thesis paragraph
- Cross-references to bankability scorecard, moat score, AI economics

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Adjustment-factor reassessment | quarterly | CFO + CEO | drift in any driver |
| Comparable-transaction watch | quarterly | CFO | major precedent |
| Foundation-model commoditisation watch | monthly | CTO / Head of AI | provider releases compete |
| Regulatory shift watch | quarterly | Head of Legal | enforcement / new rule |
| Strategic-buyer landscape | semi-annual | CEO | new acquirer emerges |

## References

- `references/saas-ai-valuation-adjustments.md` — full adjustment table + worked examples
- `skills/meta-valuation/SKILL.md` — base valuation discipline
- `skills/saas-valuation-and-fundraising-strategy/SKILL.md` — SaaS valuation
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — feeds adjustments
- `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md` — moat feeds adjustments
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md`
- `book-extractions/mersch-hacking-saas-extraction.md` — SaaS valuation discipline
- `book-extractions/walling-saas-playbook-extraction.md` — exit discussion

## Africa / Uganda Application Notes

- **African AI startups carry geography discount** in generalist investor portfolios — net 10-30% multiple haircut typical. AI premium drivers must outweigh this baseline geography discount to net positive.
- **DFI / impact-buyer valuations** weight IRR-floor + impact KPIs alongside multiples; the AI adjustment logic also applies but the weights shift.
- **Strategic-buyer landscape in Africa** is thinner; few local strategic acquirers can pay tech-multiples; international acquirers (Visa-Network, Stripe / Paystack, SAP, Microsoft, Google, regional telcos like MTN, Safaricom, Vodacom, Liquid) are the realistic exit buyers.
- **Local-language and sovereign-AI moats** translate to real valuation premium with regional strategic buyers and DFIs but less so with US-based generalist VCs.
- **Currency convention** — most international valuations USD-denominated; track both USD and local-currency valuations and explain FX impact.
