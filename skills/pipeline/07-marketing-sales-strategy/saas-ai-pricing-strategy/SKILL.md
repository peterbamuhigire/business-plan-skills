---
name: saas-ai-pricing-strategy
description: Design the AI pricing architecture for a SaaS plan — included-with-tier vs metered vs hybrid vs AI-as-add-on vs outcome-based, with margin-protection mechanics, allowance × overage design, model-mix-aware pricing, and African FX overlay. Use whenever AI features are customer-facing and pricing decisions need to defend AI Gross Margin. Sits on top of `saas-pricing-and-packaging-strategy`.
---

# SaaS AI Pricing Strategy Skill

## Overview

Generic SaaS pricing skills (Kennedy/Marrs premium positioning; `saas-pricing-and-packaging-strategy` for tier/freemium/usage architecture) cannot answer questions specific to AI feature pricing: how to include AI in a tier without margin disaster, when to meter, when to charge by outcome, how to design allowance × overage, how to price across FX corridors when AI cost is USD-denominated and ARPU is in UGX / KES / NGN / ZAR / GHS. This skill specifies the AI pricing architecture and the discipline behind it.

The output is a pricing architecture document with: tier × included-AI-allowance × model-mix policy × overage rate × add-on tier × FX corridor × margin-protection mechanic. It feeds Section 07 and reconciles back to `saas-ai-cost-of-tenant-calculator`.

## Use When

- AI features are customer-facing and material to value proposition
- Tier design needs to defend AI margin
- Existing pricing is causing margin compression from heavy-AI tenants
- Investor or DFI has asked "how does your pricing protect AI margin?"
- A pricing experiment is being designed
- Multi-currency / cross-border pricing requires FX-aware architecture

## Do Not Use When

- AI is internal-efficiency only (no customer-facing AI) — use `meta-pricing-strategy`
- Plan is pre-PMF and pricing is still notional — produce a hypothesis architecture but don't over-engineer
- Pricing is mandated externally (regulated, government tender, RFP-bound)

## Required Inputs

- Tier list with current pricing and AI features
- Output from `saas-ai-cost-of-tenant-calculator` (per-tenant AI cost by tier)
- Customer-willingness-to-pay evidence (interviews, win-rate data, competitor pricing)
- FX exposure (cost currency vs revenue currency)
- Competitive pricing snapshot (especially "AI included" claims)
- Buyer persona — SMB / mid-market / enterprise / public-sector / consumer

## Workflow

1. **Decide the pricing model** per `references/saas-ai-pricing-architecture.md`:
   - **Included-with-tier** (AI cost absorbed; usage capped via fair-use) — works for low-AI-cost-share products
   - **Metered (per-query / per-1k-token / per-document / per-seat)** — works for high-variance usage; commodity perception risk
   - **Hybrid (included allowance + overage rate)** — usually the right answer; predictable + margin-protected
   - **AI-as-add-on (separate AI tier or upgrade)** — works when AI is differentiated value, not table stakes
   - **Outcome-based ("pay only when AI succeeds")** — premium positioning; requires success-definition rigour
2. **Set the allowance per tier** using `saas-ai-cost-of-tenant-calculator` data — allowance should cover median tenant usage at target margin, with overage rate covering high-decile usage at cost+markup.
3. **Set the overage rate** — typical: 1.5-3× marginal AI cost. The overage rate is the margin lever; it should not feel punitive to mid-decile users (they should never hit it).
4. **Map model-mix to pricing tier** — premium tiers route to premium models (more accurate, slower-deprecated); lower tiers route to cheap models with quality SLAs. Be honest with customers about model-mix differences.
5. **Apply the FX corridor** — when ARPU is in local currency and AI cost is USD, set tier prices with FX headroom. Re-price quarterly or on >7% FX move.
6. **Apply the competitive overlay** — if competitors include AI "free," design positioning (quality, transparency, vertical-specificity, governance) rather than match price. Cost-plus + competitor-match are the two failure modes of SaaS AI pricing (Kennedy 9 Failures discipline).
7. **Apply the customer-segment lens** — SMB / mid-market / enterprise / public-sector have different AI-price-tolerance and different procurement cycles; align packaging.
8. **Design the AI-only upgrade path** — for customers without AI today, the upgrade ladder (no-AI → AI-light → AI-full) is an expansion-revenue lever.
9. **Stress-test the pricing** — what happens to margin if usage doubles? if provider doubles pricing? if FX depreciates 20%? if hallucination event forces capacity reduction?
10. **Wire to living plan** — pricing cadence (quarterly review default), AI cost-as-%-of-ARPU monthly, AI overage realisation monthly.

## Pricing Decision Matrix

| Customer profile | AI cost share of ARPU | Recommended model |
|---|---|---|
| SMB / high-volume / commodity | <5% | Included; tier-gated; fair-use cap |
| SMB / heavy AI usage | 5-15% | Hybrid (included allowance + overage) |
| Mid-market | 5-15% | Hybrid + premium-AI add-on |
| Enterprise | <5% (large ARPU absorbs) | Included; SLA-backed; custom model option |
| Public-sector / NGO | 5-25% (often heavy use, sensitive pricing) | AI-as-add-on; usage-based with floor |
| Consumer / freemium | 0-5% (free), 5-20% (paid) | Strict allowance + overage; premium AI tier |
| Outcome-priced (legal, sales, recruiting) | n/a (priced on outcome) | Outcome-based with floor |

## Quality Bar

- Pricing model decision explicit and defended
- Allowance × overage architecture defined per tier
- Model-mix mapped to tier with honest disclosure
- FX corridor and re-pricing rule defined
- Competitive overlay analysed; differentiation thesis stated
- Customer-segment alignment explicit
- Pricing stress-tested across cost, usage, FX, provider-pricing scenarios
- AI Gross Margin protected at planned utilisation
- Margin trajectory positive across 3-year plan
- Living-plan cadence assigned

## Anti-Patterns

- "AI included, no usage cap" with no margin model behind it
- Cost-plus AI pricing (this is the Kennedy Failure #1)
- Competitor-match AI pricing ("they're charging $X so we charge $X")
- Metered-only pricing for a small-ACV SMB segment (causes bill-shock churn)
- Outcome-based pricing without rigorous success-definition (becomes dispute-machine)
- Hiding model-mix from customers (eroded trust when they discover)
- One global price across currencies that ignores FX
- No mechanism to re-price when provider raises rates
- Pricing decided by Finance alone or Sales alone — must reconcile

## Outputs

- Pricing architecture document (tier × allowance × overage × add-on × model-mix × FX)
- Pricing decision rationale per tier
- Margin sensitivity analysis
- Competitive pricing overlay
- Customer-segment alignment notes
- Re-pricing trigger rules
- Pricing experiment backlog (3-5 tests)

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI cost-as-%-of-ARPU by tier | monthly | CFO + Head of GTM | >planned by 3pp |
| Overage revenue / overage events | monthly | CFO + Head of CS | overage events <5% or >25% of tenants |
| FX corridor | monthly | CFO | move >5% |
| Provider pricing | as-published + monthly | Head of AI | any change |
| Pricing experiment outcomes | per-experiment + quarterly | Head of GTM | as designed |
| Full pricing review | quarterly | CEO + CFO + Head of GTM | strategic |

## References

- `references/saas-ai-pricing-architecture.md` — full architecture spec with worked example
- `references/ai-feature-pricing-and-positioning.md` — positioning discipline (in `07-marketing-sales-strategy/references/`)
- `skills/saas-pricing-and-packaging-strategy/SKILL.md` — sister skill (generic SaaS pricing)
- `skills/meta-pricing-strategy/SKILL.md` — Kennedy/Marrs discipline (anti cost-plus, anti competitor-match)
- `skills/10-financial-projections/saas-ai-cost-of-tenant-calculator/SKILL.md` — cost input
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md` — margin output
- `book-extractions/walling-saas-playbook-extraction.md` — pricing chapters
- `book-extractions/mersch-hacking-saas-extraction.md` — pricing-as-CFO-discipline
- `book-extractions/kennedy-no-bs-price-strategy-extraction.md` — anti-cost-plus discipline

## Africa / Uganda Application Notes

- FX corridor is the binding pricing constraint. Set local-currency tier prices with 10-15% FX headroom; re-price on >7% FX move or quarterly, whichever comes first.
- Mobile-money fees (1.5-2.5%) eat margin alongside AI cost; model both.
- Public-sector and NGO customers procure on annual cycles with USD-pegged budgets — USD pricing for these segments is often easier than local.
- Donor-funded customers (NGOs, programmes) are AI-heavy users (analysis, reporting); design AI-as-add-on rather than included.
- Local-language inference is more expensive per task; charge premium for local-language AI tiers, not less.
- Sovereign-AI / data-residency requirements drive a separate enterprise tier (in-country hosting + dedicated model + governance) that supports premium pricing.
- WhatsApp-channel AI (chatbots, voice notes) is the highest-tolerance, lowest-friction AI usage profile in Africa — design pricing that captures this.
