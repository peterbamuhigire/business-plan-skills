---
source: Walling (SaaS Playbook), Mersch, ProfitWell pricing research, OpenView pricing benchmarks, Kennedy/Marrs
frameworks: [Pricing-dimension selection; Tier ladder; Expansion mechanic; Annual prepay; PLG pricing]
skill: meta-pricing-strategy (enhancement)
cross-reference: [saas-pricing-and-packaging-strategy, saas-unit-economics-and-cohort-model]
---

# SaaS Pricing Architecture — Enhancement to meta-pricing-strategy

The engine's `meta-pricing-strategy` defends premium pricing through Kennedy/Marrs positioning (9 failures, 5 Propositions, Triangle of Preeminence). SaaS adds a second layer: the **pricing architecture** — dimension, tiers, expansion, prepay. This reference adds that layer.

## 1. The Two-Layer Pricing Discipline

| Layer | Question | Owner |
|---|---|---|
| **Positioning** (Kennedy / Marrs) | Why is this worth premium? | `meta-pricing-strategy` |
| **Architecture** (SaaS-specific) | How is the price structured to scale with value? | `saas-pricing-and-packaging-strategy` |

Both must work. Premium positioning without architecture leaks expansion revenue. Architecture without positioning competes on price and erodes margin.

## 2. The Five SaaS Pricing Decisions

(See `skills/saas-pricing-and-packaging-strategy/SKILL.md` for full workflow.)

1. **Pricing dimension** — per seat / per usage / per outcome / per record / hybrid
2. **Tier architecture** — number of tiers; what differentiates each
3. **Anchor strategy** — high-tier anchor; sticker-price anchor
4. **Expansion mechanic** — how does revenue grow over customer lifetime
5. **Discount / prepayment policy** — when, how much, what trade-in

## 3. Cross-Linking the Positioning to the Architecture

Each pricing decision should reinforce the positioning:

- **Premium positioning** + **simple flat pricing** = positioning is undermined (where's the premium?)
- **Premium positioning** + **three-tier ladder with high anchor** = positioning is reinforced (the anchor IS the premium signal)
- **Premium positioning** + **annual prepay incentive** = positioning is reinforced (signals confidence)
- **Premium positioning** + **predictable discounts** = positioning is destroyed (Cotton discount discipline)
- **Premium positioning** + **expansion mechanic that scales with value** = positioning is reinforced (price grows with customer success)

## 4. The Pricing-Dimension Decision (the architecture lever Kennedy doesn't address)

Kennedy treats price as a single number ("$X for the service"). SaaS prices are functions of usage:

```
Customer payment per month = base + (dimension unit price × dimension volume)
```

The choice of dimension is the master architecture decision:
- **Per seat**: scales with team size. Works for collaboration tools.
- **Per usage / consumption**: scales with volume. Works for infrastructure / AI / messaging.
- **Per outcome / event**: scales with value delivered. Calendly meetings; Loom views.
- **Per record / account**: scales with managed entity count. HubSpot contacts; Salesforce records.
- **Flat**: fixed regardless of usage. Simple but doesn't capture upside.
- **Hybrid base + usage**: most modern SaaS default.

## 5. Worked Example — Aligning Premium with Architecture

**Plan:** Dairy-cooperative SaaS in Uganda.

**Premium positioning (Kennedy):**
- Triangle of Preeminence: built dairy-specific expertise; high-visibility partnership with MAAIF; community service via field-officer training
- 5 Propositions: USP (Luganda-first SaaS) + UVP (recovers Y% of milk-payment leakage = 10× ROI) + Irresistible Offer (free pilot for cooperatives with extension-officer engagement) + Unique Safety Proposition (audit-trail compliance) + Unique Experience Proposition (in-language; field-team trained)
- Niche pricing: deep niche specialisation justifies 3-5× generic ERP

**Pricing architecture (SaaS layer):**
- Dimension: per-100-farmers (scales with cooperative size)
- Tiers: Starter / Growth / Professional / Enterprise (4 tiers; see `saas-pricing-and-packaging-strategy-template.md` worked example)
- Anchor: Enterprise tier at UGX 3.5M+/month
- Expansion mechanic: Tier upgrade (small → large cooperative) + module attach (basic recording → farmer scoring → payment automation)
- Annual prepay: 15% discount; 25-30% target uptake

**Result:** premium positioning IS the architecture. Each tier signals premium. Each dimension increment is value-justified.

## 6. The Pricing Page Discipline

Whether for marketing or sales-quote, the pricing page must:
- Show the three / four tiers transparently (PLG) or "from $X / Contact us for Enterprise" (sales-led)
- State the dimension explicitly (per seat, per usage, etc.)
- Show annual prepay discount prominently
- Provide FAQ / objection responses
- Include comparison table vs alternatives where it strengthens the case
- Lead with the recommended tier (anchor middle)

## 7. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Pricing dashboard (tier mix, ARPU trend) | Monthly | Head of GTM + CFO |
| Pricing experiment (one per quarter) | Quarterly | Head of GTM |
| Annual prepay uptake | Monthly | CFO + Sales |
| Discount-given trend | Monthly | CFO + VP Sales |
| Major price increase | Annually | CEO + Board |
| FX review (Africa) | Quarterly | CFO |

## 8. Africa / Uganda Application Notes

- **Premium positioning + niche pricing** can deliver 200-500% lift over generic global tools in African markets — combine `meta-pricing-strategy` + this architecture layer.
- **Local-currency pricing** for SMB / mid-market plans; USD pricing for enterprise / cross-country.
- **Mobile-money UX** for monthly billing — minimise friction; one-tap-to-pay.
- **Annual prepayment** uptake target 25-35% (aggressive vs US norms because of lower local baseline).
- **Public-sector / NGO** procurement requires quotation format with VAT line, withholding tax line, validity window — design these into the contract template.
- **Multi-currency invoicing** for cross-country sellers (UGX customer + USD enterprise + KES sub-region) requires accounting discipline.
