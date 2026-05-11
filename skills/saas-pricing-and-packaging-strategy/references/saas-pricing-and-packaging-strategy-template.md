---
source: Walling (SaaS Playbook), Mersch (Hacking SaaS), Cotton, Patrick Campbell (ProfitWell pricing research)
frameworks: [Tier ladder, Pricing dimension selection, Freemium 4-test, Expansion mechanic, Pricing experiment cadence]
skill: saas-pricing-and-packaging-strategy
cross-reference: [meta-pricing-strategy, saas-unit-economics-and-cohort-model, saas-gtm-motion-design]
---

# SaaS Pricing & Packaging Strategy — Reference Template

## 1. The Five SaaS Pricing Decisions

Every SaaS plan must explicitly decide:

1. **Pricing dimension** — what does the price scale on?
2. **Tier architecture** — how many tiers? what differentiates them?
3. **Anchor strategy** — high tier as anchor? sticker price as anchor?
4. **Expansion mechanic** — how does revenue from existing customers grow over time?
5. **Discount / prepayment policy** — when, how much, with what trade-in?

## 2. Pricing Dimension Decision Matrix

| Dimension | When it works | Examples | African considerations |
|---|---|---|---|
| Per seat / user | Value scales with team size; collaboration | Slack, Notion, Asana | Works; specify team-size bounds for SMB tier |
| Per usage / consumption | Value scales with volume | Twilio, Stripe, AWS, OpenAI | Mobile-money / SMS / AI costs are usage costs; pass through carefully |
| Per outcome / event | Value is event-driven | Calendly meetings, Loom views | Works for B2C / freelancer market |
| Per record / account | Value scales with managed entities | HubSpot contacts, Salesforce records | Common in CRM; African SMB segments often have low record counts |
| Flat per-tier | Value is feature-based not scale-based | Basecamp (famous), early-stage products | Simple; under-monetises power users |
| Hybrid (base + usage) | Modern SaaS default | OpenAI tier + tokens, Salesforce seat + add-on | Best balance of predictability + scale |

## 3. The Three-Tier Ladder (default architecture)

```
                                     TIER 1            TIER 2            TIER 3
                                     (entry)           (recommended)     (anchor)
ICP                                  ___               ___               ___
Pricing dimension                    ___               ___               ___
Price (UGX/mo)                       ___               ___               ___
Price (USD/mo)                       ___               ___               ___
Annual prepay (-15%)                 ___               ___               ___
Feature differentiator               ___               ___               ___
Target % of customers                70%               25%               5%
Target % of revenue                  30%               45%               25%
Expansion path                       → Tier 2 via      → Tier 3 via      → custom enterprise
                                      team growth        compliance/SLA
Sales motion                         self-serve        sales-assisted    enterprise sales
```

The anchor tier (Tier 3) is not expected to sell to most customers — its job is to make Tier 2 feel reasonable.

## 4. Four Tiers (when justified)

Adds a "free" tier (freemium) or a "lite" tier below entry.

```
                                FREE              LITE              PRO               ENTERPRISE
Price                           $0                $50-100/mo        $200-500/mo       custom
Goal                            acquisition       conversion        primary revenue   anchor + custom revenue
Constraint                      feature-gated     usage-gated       full features     SLA + custom
```

## 5. The Freemium Four-Condition Test

Adopt freemium ONLY if all four pass:

1. **The free tier delivers genuine value** — not crippled to the point of pain. The customer must be able to do real work for free.
2. **The paid-tier upgrade trigger is obvious** — at some natural moment (more users, more usage, need for integration), upgrade is the path of least resistance.
3. **Infrastructure cost per free user is <$1/month** — or you'll burn cash on freeloaders.
4. **The company has the brand / distribution reach to attract millions of free users** — freemium only works at scale.

If any fail, use **free trial** (time-bounded, credit card required at signup or before trial expires) instead.

## 6. The Expansion Mechanic (mandatory for NRR > 100%)

Three types of expansion:

**Seat / user expansion** — customer grows their team; new users on the same account.
- Implementation: per-user pricing, easy to add seats, billing automation.
- Realistic NRR contribution: +5–15% per year.

**Usage expansion** — customer's volume grows.
- Implementation: usage-based pricing, transparent usage dashboard, predictable overage.
- Realistic NRR contribution: +10–30% per year for usage-based products.

**Module / tier expansion (cross-sell, upsell)** — customer adds a new capability or moves to a higher tier.
- Implementation: separate paid modules; tier-upgrade prompts at usage limits.
- Realistic NRR contribution: +5–15% per year.

A healthy SaaS often combines two of these. Best-in-class (Snowflake, Datadog) achieve 150%+ NRR via usage expansion.

## 7. Annual Prepayment Policy

**Standard policy:**
- Monthly billing: list price
- Annual prepayment: 10–20% discount (15% typical)
- Two-year prepayment: 20–25% discount
- Three-year prepayment: 25–30% discount (rare; for strategic enterprise)

**Why it matters:**
- Reduces involuntary churn (no monthly card declines)
- Reduces voluntary churn (annual decision moment, not monthly)
- Improves cash conversion (working-capital trough fills in)
- Provides forward visibility on revenue

**African specific:** uptake is lower than US; design more aggressive incentive (15–20% rather than 10%).

## 8. Pricing Experiment Cadence

**Quarterly small experiments:**
- A/B test of tier names ("Pro" vs "Business" vs "Growth")
- Anchor experiments (showing/hiding the highest tier)
- Discount-banner experiments
- Annual-prepay discount level tests
- Trial-length experiments

**Annual large experiments:**
- Price increase (typically +5–10% for new customers, grandfather existing)
- Repackaging (move features between tiers)
- New tier introduction (add a higher anchor or a lower entry)
- Discount-policy overhaul

**Decision log:** every experiment hypothesis, design, result, decision recorded.

## 9. Discount Discipline (Cotton + WBD)

- Never discount predictably (no "always 20% off in November")
- Every discount has a reason AND a quid pro quo (longer term, prepay, case study, reference, expanded scope)
- Authorisation matrix: rep 5%, manager 10%, director 10%+, CEO/board for >20% or strategic deals
- No discount discussion until: customer agrees problem is urgent, customer agrees solution fits, customer shares procurement timeline, decision-maker is in the room (Cotton 4-gate)

## 10. Worked Example — Ugandan Vertical SaaS (Dairy Cooperatives)

```
                              STARTER          GROWTH           PROFESSIONAL     ENTERPRISE
ICP                           Sub-50 farmer    50-300 farmer    300-1000 farmer  1000+ farmer / multi-coop
                              cooperative      cooperative      cooperative      union
Pricing dimension             Flat             Per-100-farmers  Per-100-farmers  Custom + per-100
Price (UGX/mo)                250,000          750,000          2,000,000        Custom (>3.5M)
Price (USD/mo)                ~67              ~200             ~540             Custom
Annual prepay (-15%)          UGX 2.55M        UGX 7.65M        UGX 20.4M        ___
Mobile-money supported        Yes (M-Pesa,     Yes              Yes              Yes
                              MTN MoMo)
Feature differentiator        Basic milk       + payment        + farmer scoring + multi-coop + API
                              recording        automation       + extension officers
Target % of customers         50%              35%              13%              2%
Target % of revenue           18%              42%              30%              10%
Expansion path                → Growth via     → Professional   → Enterprise     → custom
                              farmer count     via modules      via federation
```

## 11. Living-Plan Cadence (specific to pricing)

- **Weekly**: tier-mix dashboard (which tier are new customers landing on?)
- **Monthly**: ARPU trend; annual-prepay uptake; discount-given trend
- **Quarterly**: pricing experiment retrospective; one experiment shipped
- **Annually**: full pricing review; price increase decision; repackaging decision

## 12. Africa / Uganda Application Notes

- **Local-currency pricing** for SMB / mid-market African plans is more sustainable than USD pricing. Build FX-escalator clause for >10% currency move into contracts.
- **USD pricing** for enterprise / multi-country plans; couple with quarterly FX adjustment for new contracts.
- **Tax / VAT** in pricing display: African buyers expect price-inclusive-of-VAT in B2B contexts (different from US norms). Display both lines (price ex VAT, price inc VAT).
- **Withholding tax**: government / NGO buyers in Africa typically withhold 5–10% tax at source. Build this into your contracts and AR planning.
- **Pricing in two currencies on the website**: USD + local currency. Best-in-class African SaaS show both.
- **Mobile-money pricing tier**: design a tier where the customer pays via mobile-money daily / weekly to suit cash-flow patterns of micro-SME segments.
- **Public-sector buyers**: have specific procurement processes (tender, eCAT, eGP) that require fixed-price quotes valid for 90–180 days. Build longer quote validity into your sales process.
- **Annual price escalation**: 5–8% per year is standard in African SaaS to absorb inflation + FX depreciation.
