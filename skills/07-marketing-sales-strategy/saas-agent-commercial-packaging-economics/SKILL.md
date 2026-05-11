---
name: saas-agent-commercial-packaging-economics
description: Economics of Agent Included vs Agent Add-on vs Agent Standalone packaging. ARPU lift, ACV expansion, attach rate, cannibalisation of base-tier, base-tier price erosion risk, free-trial discipline, packaging migration discipline, multi-product NRR composition. Sits alongside `saas-agent-pricing-strategy` which handles the pricing primitive; packaging is a distinct commercial decision with its own economics.
---

# SaaS Agent Commercial Packaging Economics Skill

## Overview

Pricing primitives (per-resolution, per-outcome, per-step, subscription, hybrid) are handled by `saas-agent-pricing-strategy`. **Packaging** is a separate commercial decision: how does the agent product appear in the customer's commercial relationship with the company?

Three packaging archetypes dominate:

1. **Agent Included** — the agent is part of an existing platform tier; no separate purchase decision; bundled
2. **Agent Add-on** — the agent is an optional add-on on top of the platform; separate purchase decision; priced incrementally
3. **Agent Standalone** — the agent is a standalone product with its own contract; separate sales motion

Each archetype has fundamentally different economics:

| Dimension | Included | Add-on | Standalone |
|---|---|---|---|
| ARPU lift on existing base | Low / hidden in tier price | Medium / explicit incremental | N/A (separate logo) |
| Attach rate | 100% (bundled) | 20-60% typical | N/A |
| Base-tier price erosion risk | High (must raise base price to absorb cost) | Low | None |
| Cannibalisation risk | Low (no choice) | Medium (existing tier may downgrade) | Low |
| Discount visibility | Hidden | Explicit | Explicit |
| Investor revenue attribution | Hard | Easy | Easy |
| Customer expectation control | Hard | Medium | Easy |
| SLA tier discipline | Hard (one SLA for everything) | Easy (separate SLA for add-on) | Easy |
| Margin transparency to customer | Hard | Easy | Easy |

Getting the packaging decision wrong destroys economics in ways the pricing primitive cannot fix. This skill installs the discipline.

## Use When

- An agent product is being launched into an existing SaaS commercial portfolio
- An existing agent add-on is being repackaged or migrated to a different archetype
- The board / GTM team is debating attach-rate assumptions
- The 3yr / 5yr plan needs to model packaging-driven revenue carefully
- A bundle-vs-add-on decision must be made before pricing is set
- Cross-loaded with `saas-agent-pricing-strategy` and `saas-pricing-and-packaging-strategy`

## Do Not Use When

- The plan has only the agent product (no existing platform / no packaging decision)
- The plan is pre-PMF and packaging is premature (use `saas-mvp-and-product-market-fit-strategy` first)
- The agent product is internal-efficiency only

## Required Inputs

- Existing platform / SaaS pricing and tier structure
- Existing platform ARPU and ACV
- Agent product unit economics (cost per resolved task; see `saas-agent-unit-economics-and-cogs`)
- Customer-segment willingness-to-pay (from value-anchor analysis)
- Competitive packaging in the category (how competitors bundle)
- Sales-motion capability (high-touch vs PLG vs hybrid)
- SLA tier strategy (will agent have separate SLA or share platform SLA?)

## Workflow

### 1. Choose the packaging archetype

Use the decision rubric:

**Choose Included** when:
- Cost per resolved task is low and stable
- Customer expects the agent as baseline functionality (table stakes)
- Volume-tier control is feasible (cap usage in fair-use policy)
- Differentiation is platform-level, not agent-level
- ARPU expansion via tier upgrade is the strategy (not via attach)

**Choose Add-on** when:
- Cost per resolved task is meaningful and varies by usage
- Customer can opt in / out based on use case
- Sales motion supports attach-rate selling
- Revenue attribution to agent is required (investor, board)
- SLA tier on agent is meaningfully different from platform SLA

**Choose Standalone** when:
- Agent serves a different buyer / use case than the platform
- Agent has its own GTM motion
- Agent vertical is materially distinct
- Agent must be sold without the platform anchor

### 2. Build the packaging-economics model

Per `references/saas-agent-commercial-packaging-economics-template.md`, model each archetype:

**Included — full economic flow:**
- Tier price × number of customers
- Less: aggregate agent cost per customer (cost per resolved task × volume)
- Less: base-tier price erosion if absorbed (customers compare against unbundled offers)
- = Net contribution

**Add-on — full economic flow:**
- Platform fee × customers
- + Add-on price × (customers × attach rate)
- Less: agent cost (only on attached customers)
- Less: cannibalisation (customers who downgrade base tier to free budget for add-on)
- = Net contribution

**Standalone — full economic flow:**
- Standalone price × standalone customers
- Less: agent cost
- Less: separate sales / marketing cost
- = Net contribution

### 3. Stress-test the attach-rate assumption

Add-on packaging lives or dies on attach rate. Sanity-check the assumed attach rate against:
- Comparable add-ons in your category (e.g. premium AI features attach 15-40% historically; agent attach rates emerging at 20-50% in 2025-2026)
- Sales-cycle capacity (how many add-on conversations can the sales team have per quarter?)
- PLG-eligibility (can self-serve attach happen?)
- Customer-success motion (does CS surface the add-on to existing customers?)
- Pricing-vs-value alignment

Stress: attach rate 50%, 25%, 10%, 5% — does the plan still work at the low end?

### 4. Model the cannibalisation risk

In add-on packaging, some customers may downgrade their base tier to free budget for the agent add-on. This **erodes platform ARPU** even as agent ARPU grows. Net ARPU change:

```
Net ARPU change = (Add-on attach rate × Add-on price)
                  - (Downgrade rate × Base-tier price gap)
                  - (Discount given to attach × Add-on price)
```

If the cannibalisation > the add-on revenue, the packaging decision is destructive.

### 5. Model the base-tier price erosion risk

In Included packaging, the cost of the agent is absorbed in the base tier price. If competitors enter with cheaper unbundled offers, the base tier price comes under pressure. The Included-packaging plan must either:
- Raise the base tier price (testable but risky)
- Absorb the margin pressure
- Differentiate sufficiently on platform value that the agent inclusion is not the deciding factor

Document the defence.

### 6. Build the multi-product NRR composition

For an existing customer base layered with agent revenue:

```
NRR = (Starting MRR + Expansion + Upgrade + Add-on - Contraction - Churn) / Starting MRR
```

Decompose:
- Pure platform expansion (more seats, more tier)
- Agent add-on expansion (new attach)
- Agent usage expansion (existing attach + more usage)
- Cross-sell to other products
- Less: churn / downgrade

NRR should reconcile to ARR waterfall. Agent contribution to NRR should be explicit.

### 7. Plan the packaging migration

Packaging decisions are not permanent. Plan migration scenarios:
- Add-on → Included (when attach rate exceeds threshold)
- Add-on → Standalone (when agent revenue justifies separate logo)
- Standalone → Add-on (when agent revenue stalls and platform anchor needed)
- Included → Add-on (when cost variance becomes high and unbundling restores margin)

Each migration has revenue-recognition implications (per `saas-agent-revenue-recognition`) — contract modification accounting.

### 8. Set the free-trial discipline

For add-on and standalone packaging:
- Trial period (typically 14-30 days)
- Trial usage cap (to prevent cost drain)
- Conversion-rate target
- Trial-to-paid revenue recognition (do not recognise trial; recognise on conversion)
- Refund window post-conversion

### 9. Cross-load with SLA tier strategy

- Included packaging typically shares platform SLA — limited SLA-tier discipline
- Add-on packaging can carry distinct SLA terms — bronze / silver / gold add-on tiers
- Standalone packaging carries its own full SLA structure

If SLA-tier discipline matters (sector regulators, enterprise procurement), Add-on or Standalone is structurally easier than Included.

### 10. Wire to living-plan governance

Per cadence below.

## Quality Bar

- Packaging archetype chosen with explicit reasoning
- Economic model built for the chosen archetype
- Attach rate assumption stress-tested (5%, 10%, 25%, 50%)
- Cannibalisation modelled (where applicable)
- Base-tier price erosion modelled (where applicable)
- Multi-product NRR composition explicit
- Packaging migration scenarios considered
- Free-trial discipline defined (where applicable)
- SLA-tier strategy cross-loaded
- A sceptical Head of GTM would not laugh at the model

## Anti-Patterns

- "We'll bundle everything" without modelling base-tier erosion
- Attach-rate assumption pulled from thin air
- No cannibalisation model — overstates add-on revenue
- Free-trial without usage cap — drains cost
- Recognising trial revenue — fails ASC 606
- One SLA across Included + Add-on + Standalone — operationally impossible
- No revenue attribution method for Included — investor cannot see agent
- Standalone packaging with no separate GTM motion — sales team underdelivers
- "Packaging is marketing's job" — packaging is a CFO + Head of GTM + Head of Product decision

## Outputs

- Packaging archetype choice with reasoning
- Economic model (Included / Add-on / Standalone)
- Attach-rate sensitivity
- Cannibalisation model
- Base-tier erosion model
- Multi-product NRR composition
- Packaging migration scenarios
- Free-trial discipline
- SLA-tier cross-load
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Attach rate (Add-on) | monthly | Head of GTM + CFO | -5pp from plan |
| Conversion rate (free trial) | monthly | Head of GTM + Product | -3pp from plan |
| Cannibalisation rate (downgrade to free budget for add-on) | quarterly | Head of GTM + CFO | >5% of attaching customers downgrade |
| Net ARPU change (combined platform + agent) | monthly | CFO | -5% from plan |
| Multi-product NRR | monthly | CFO | -3pp from plan |
| Packaging-migration trigger watch | quarterly | CEO + Head of GTM | trigger threshold |
| Base-tier price-pressure signal | quarterly | CFO + Head of GTM | competitor unbundled offer |

## References

- `references/saas-agent-commercial-packaging-economics-template.md` — full worked model
- `skills/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md` — pricing primitive parent
- `skills/saas-pricing-and-packaging-strategy/SKILL.md` — SaaS packaging parent
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — rev-rec on packaging migration
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — cost floor
- `skills/saas-customer-success-operating-model/SKILL.md` — CS motion
- `skills/saas-gtm-motion-design/SKILL.md` — sales motion
- `book-extractions/walling-saas-playbook-extraction.md` — SaaS packaging
- `book-extractions/cotton-run-a-saas-business-extraction.md` — packaging-vs-pricing distinction

## Africa / Uganda Application Notes

- **Mobile-money packaging** — Included packaging often easier for African SMB customers (single monthly debit); Add-on adds purchase friction; Standalone requires standalone GTM
- **WhatsApp / USSD / SMS / IVR channel-cost pass-through** — agent add-on packaging must include channel-cost transparency; customers often do not realise channel cost until they see the bill
- **Public-sector packaging** — KE / NG / RW / UG / ZA public-sector tenders typically prefer Standalone (specific scope, specific budget line); Add-on does not fit procurement frameworks well
- **DFI / multilateral customer packaging** — milestone-paid pilots often Standalone; transition to Add-on or Included as deployment matures
- **SMB ARPU constraints in Africa** — SMB tier price ceilings UGX 50k-500k / month; agent Add-on price must fit within the customer's existing budget tolerance, not on top
- **Sovereign-AI bundled offers** — sovereign-AI tenders sometimes bundle agent + compute + data; effectively Included packaging at sovereign-AI level
- **Insurance / regulated-sector packaging** — Standalone often required because compliance / audit scope is different per regulator
- **Cannibalisation in African contexts** — SMB customers more price-sensitive than US benchmarks; cannibalisation rates 1.5-2x US benchmarks; budget shift more likely
