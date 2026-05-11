---
source: Walling pp. 67–106; Mersch ch. 10; Cotton essay 6; Kennedy / Marrs anti-cost-plus discipline; 2024-2026 AI-SaaS pricing practice
frameworks: [Tier × Model × Allowance × Overage × FX; Pricing-model decision; Margin-protection mechanics; African pricing realities]
skill: saas-ai-pricing-strategy
cross-reference: [saas-pricing-and-packaging-strategy, saas-ai-cost-of-tenant-calculator, saas-ai-unit-economics-and-cogs, meta-pricing-strategy]
---

# SaaS AI Pricing Architecture — Reference

## 1. The five pricing models

| Model | Mechanism | Best when | Risk |
|---|---|---|---|
| **Included-with-tier** | AI absorbed in tier price; cap via fair-use | Low AI cost share (<5% ARPU); commoditised AI features | Heavy-AI users destroy tier margin |
| **Metered** | Per-query / per-1k-token / per-document / per-seat | High-variance usage; sophisticated buyers; AI is core utility | Bill shock; commoditisation perception; revenue volatility |
| **Hybrid (allowance + overage)** | Tier includes X queries/tokens/seats; overage at $Y/unit | The right answer for most SaaS-with-AI | Allowance design is a tier-redesign exercise |
| **AI-as-add-on** | Separate AI tier or upgrade ($X/seat/mo extra) | AI is differentiated value, not table stakes; or initial customers don't all want AI | Sales cycle complexity; risk of two-tier value perception |
| **Outcome-based** | Pay only when AI succeeds (e.g. per closed lead, per resolved ticket) | Sales / recruiting / legal AI with clear success definition | Success-definition disputes; requires sophisticated tracking |

## 2. The pricing decision flow

```
1. Compute per-tier per-tenant AI cost (saas-ai-cost-of-tenant-calculator)
2. Compute AI-cost-as-%-of-ARPU per tier
3. If AI cost / ARPU < 5% → included-with-tier (simplest)
4. If 5-15% → hybrid (allowance covers median; overage covers high decile)
5. If >15% → AI-as-add-on (separate tier) OR move feature to higher tier
6. If product IS AI → outcome-based or premium AI-native pricing
7. Apply FX overlay
8. Apply competitive overlay (don't match; differentiate)
9. Stress-test for cost spike + FX move + usage growth
```

## 3. Tier × Model × Allowance × Overage × FX architecture

The architecture has five dimensions. Each tier specifies all five.

### Dimension 1: Tier

The pricing tier name and target customer (Starter / Growth / Pro / Enterprise; or named-vertical tiers).

### Dimension 2: Model-mix per tier

Each tier specifies which AI models the customer's queries route to:

| Tier | Model-mix policy | Quality SLA |
|---|---|---|
| Starter | 80% cheap model (GPT-4o-mini / Haiku 4) + 20% premium for complex | Best-effort |
| Growth | 50% cheap + 50% premium | "Premium model for complex queries" |
| Pro | 30% cheap + 70% premium | "Premium model by default" |
| Enterprise | Customer-selectable + custom routing | Negotiated SLA |

This is a real customer-facing tier dimension that protects margin. Be honest about it.

### Dimension 3: Allowance per tier

What is included before overage kicks in:

| Tier | Allowance | Reasoning |
|---|---|---|
| Starter | 50 queries / month per seat | Covers median Starter usage; overage rare |
| Growth | 200 queries / month per seat | Covers median Growth; overage occasional |
| Pro | 1,000 queries / month per seat | Covers median Pro; overage rare |
| Enterprise | Negotiated (often unlimited) | Per contract |

Set allowance to cover the median tenant at target margin; let overage cover the high decile at cost+markup. Goal: <20% of tenants hit overage in a typical month; <5% hit it consistently.

### Dimension 4: Overage rate per tier

The overage rate is the margin lever. Typical structure:

```
Overage rate = blended per-query cost × markup
```

Markup typically:
- 1.5× cost for AI commodity (matching customer expectation of "cost-plus-a-bit")
- 2-3× cost for differentiated AI ("our AI is worth more")
- 4-5× cost for outcome-bearing AI (legal, recruiting, sales-closing)

Overage rate must be: explicit, predictable, not punitive, with usage transparency in customer's portal.

### Dimension 5: FX overlay

For local-currency pricing where AI cost is USD-denominated:

```
local-currency tier price = USD tier price × FX corridor rate
local-currency allowance value = same calculation (allowance is unit-based, not price-based)
local-currency overage rate = USD overage rate × FX corridor rate
```

Set re-pricing trigger at FX move >7% or quarterly, whichever comes first. Communicate re-pricing in advance; never surprise customers.

## 4. Pricing-decision matrix by customer segment

| Customer profile | AI cost share of ARPU | Recommended model | Mechanism |
|---|---|---|---|
| SMB / high-volume / commodity | <5% | Included | Tier price absorbs; fair-use cap |
| SMB / heavy AI | 5-15% | Hybrid | Allowance + overage |
| Mid-market | 5-15% | Hybrid + AI-premium tier | Allowance + overage; AI-Pro tier upgrade |
| Enterprise | <5% (large ARPU absorbs) | Included with SLA | Custom model option; AI-governance add-ons |
| Public-sector / NGO | 5-25% | AI-as-add-on | Separate AI tier; usage-based with floor |
| Consumer / freemium | 0% free / 5-20% paid | Strict allowance + overage | Premium AI tier; cost-control fundamental |
| Outcome-priced (legal, sales, recruiting) | n/a (priced on outcome) | Outcome-based with floor | Per-success rate + minimum |

## 5. Margin-protection mechanics (the engine of profitable AI pricing)

1. **Allowance design** — covers the median, lets high-decile pay overage
2. **Model-mix tiering** — premium models for premium tiers
3. **Cache and prompt-engineering** — done by Eng, but pricing-aware
4. **Per-tier cost-engineering targets** — Growth must reach AI cost <8% of ARPU by Q4
5. **AI-as-add-on for high-cost features** — segregate AI revenue and cost
6. **FX corridor and re-pricing** — protect margin against currency shock
7. **Overage rate set above cost** — every overage event must be margin-accretive
8. **Pricing experimentation cadence** — A/B test pricing quarterly; the price is a variable, not a constant

## 6. Competitive pricing — the three failure modes

### Failure mode 1: Cost-plus AI pricing (Kennedy Failure #1)

"Our AI costs $0.02 per query so we charge $0.05 per query." This is the cheapest way to capture none of the value AI creates and to be undercut by anyone with cheaper cost.

Anti-mode: **value-based pricing** — what is the AI worth to the customer? Charge a fraction of that.

### Failure mode 2: Competitor-match AI pricing

"Competitor X bundles AI for free; we must too." This forces you into the competitor's margin structure without their scale.

Anti-mode: **differentiated positioning** — quality, vertical depth, governance, local-language, transparency, support. Don't compete on AI-feature-included; compete on AI-quality-delivered.

### Failure mode 3: "Free AI to drive adoption"

This works only if AI cost-per-tenant is genuinely low or if AI directly drives expansion revenue elsewhere. Many plans destroy themselves on this.

Anti-mode: **carefully designed freemium** with strict allowance, model-mix routing to cheap models, prompt-token discipline, and upgrade path to AI-paid tier.

## 7. Worked example — East-African Vertical SaaS

(Drawn from `saas-ai-cost-of-tenant-calculator.md` Section 6 worked example.)

Plan: dairy-cooperative AI platform, three tiers.

**Pricing architecture decision:**

| Tier | Mechanism | ARPU local / USD | Model-mix | Allowance | Overage | FX trigger |
|---|---|---|---|---|---|---|
| Basic | Included | UGX 250,000 / $67 | 100% GPT-4o-mini (cheap) | 50 summary queries / month | Soft-cap; require upgrade | re-price quarterly |
| Standard | Hybrid | UGX 750,000 / $200 | 60% cheap + 40% Claude/Cohere | 200 queries / month total | UGX 600 / $0.16 per extra summary; UGX 1,500 / $0.40 per Luganda chat overage | FX >7% triggers review |
| Pro | Included with high allowance | UGX 2,000,000 / $540 | Premium-by-default + Cohere Luganda always | 2,000 queries / month + custom anomaly thresholds | Negotiated for >2,000 | annual contract; FX in T&Cs |

**Margin protection:**
- Standard tier overage rate is 3× marginal cost — every overage event covers the tier's contribution margin gap if usage exceeds plan
- Basic tier deliberately cheap-model-only — keeps cost predictable; upgrade path to Standard is the freemium → paid hand-off
- Pro tier locks customer into annual contract (better cash; lower churn); FX adjustment clause in contract
- AI-as-add-on **not** chosen here because AI is core value of all tiers — instead, AI-Pro is just the Pro tier

**Competitive overlay:**
- Competitors offering "AI included free" are using GPT-3.5-level quality with no Luganda support
- This plan's positioning is "the Luganda-first dairy AI" — quality, language, vertical depth are the differentiation; matching the "AI free" model would compromise quality
- Pricing premium of 25-40% vs commodity competitor is defensible on this differentiation

**FX overlay:**
- USD reference prices set; UGX corridor at 3,700/$
- Re-price trigger: 7% move (UGX moves outside 3,440-3,960 corridor)
- Pro tier annual contracts include FX-adjustment clause beyond 10% move

## 8. Pricing experimentation backlog (engine for living pricing)

Every plan should propose 3-5 pricing experiments to run within 12 months:

| Experiment | Hypothesis | Measure | Decision |
|---|---|---|---|
| Move Basic allowance from 50 to 30 queries | Will reduce free-rider users; nudge to Standard | Conversion from Basic to Standard +X% | Lower if conversion + revenue net positive |
| Add AI-Pro upgrade ($25/seat/mo extra on Standard) | Captures additional WTP without disturbing core pricing | Take-rate of upgrade | Permanent if take-rate >12% |
| A/B test Pro at UGX 2.0M vs 2.5M | Pro buyers are price-insensitive | Conversion rate change | Higher price if conversion drop <30% |
| Outcome-based pilot for premium customers | Customers willing to pay on success | Pilot signups; success rate | Decide post-pilot |
| Overage rate down to 1.5× cost (more generous) | Reduces customer friction; expands usage | Overage event rate + retention | Revert if margin impact >2pp |

## 9. Living-Plan Cadence

(Replicated from `saas-ai-pricing-strategy/SKILL.md` for convenience.)

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI cost-as-%-of-ARPU by tier | monthly | CFO + Head of GTM | >planned by 3pp |
| Overage revenue / overage events | monthly | CFO + Head of CS | overage events <5% or >25% of tenants |
| FX corridor | monthly | CFO | move >5% |
| Provider pricing | monthly | Head of AI | any change |
| Pricing experiment outcomes | per-experiment + quarterly | Head of GTM | as designed |
| Full pricing review | quarterly | CEO + CFO + Head of GTM | strategic |

## 10. Anti-patterns reminder

- Cost-plus AI pricing
- Competitor-match AI pricing
- "Free AI to drive adoption" with no cost model
- One global tier price across currencies (no FX overlay)
- Allowance set to "unlimited" — destroys margin
- Overage rate set below or near cost — overage events become losses
- Hiding model-mix from customers — eroded trust
- Pricing decided by Sales alone or Finance alone (must reconcile both)
