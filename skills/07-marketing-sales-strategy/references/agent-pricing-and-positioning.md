---
source: Agent-products business-plan audit (2026); Kennedy/Marrs pricing discipline; 2024-2026 agent-VC and enterprise procurement practice
frameworks: [Agent pricing positioning; "Per resolved" not "per seat" narrative; SLA-tied positioning]
skill: 07-marketing-sales-strategy
cross-reference: [saas-agent-pricing-strategy, saas-agent-pricing-architecture, saas-agent-moat-and-wrapper-risk]
---

# Agent Pricing and Positioning — Reference

For Section 07. Detailed pricing architecture in `saas-agent-pricing-strategy/references/saas-agent-pricing-architecture.md`.

## 1. Positioning Discipline

The agent pricing positioning is a separate decision from the pricing primitive. Strong agent positioning:

- "We charge per resolved ticket, not per seat" — anchors customer's value frame on outcome
- "You only pay when the agent succeeds" — outcome-conditional
- "We earn when you recover" — for outcome businesses (collections, sales-development)
- "Per-citizen-interaction at SLA" — for public-sector
- "Per-step on platform; per-resolution on retail" — for platform plays

Avoid:
- "Per-seat" framing (gives away outcome value)
- "Per-query" framing (commoditises and invites cost-pass-through fight)
- Bundling that hides agent value
- "AI subscription" (sounds like a tool)

## 2. Pricing Primitive Recap

Choose:
- **Per-resolution** — CX, collections, ticket-resolution agents
- **Per-outcome** — payment recovered, contract signed, appointment scheduled, claim processed
- **Per-step** — agent platforms / infrastructure
- **Per-agent / per-seat** — agent-as-employee positioning (sales, analyst); less aligned but procurement-friendly
- **Hybrid** — platform fee + per-resolution variable (most common for mid-market / enterprise)

## 3. Pricing Architecture Recap

- **Cost floor** — from `saas-agent-unit-economics-and-cogs`
- **Value anchor** — what customer replaces (human FTE / per-ticket BPO cost / competing software)
- **Value ceiling** — customer's WTP maximum
- **Chosen price** — typically 60-75% of value ceiling for premium; 40-55% for penetration
- **Intervention-credit policy** — full / partial / capped / tiered
- **SLA tie** — credits for breach; cap on monthly credit accrual
- **Vendor-cost pass-through clause** — mandatory for contracts >12 months
- **FX corridor** — mandatory when revenue is local currency

## 4. Sales Motion Implications

Per-resolution / per-outcome pricing demands:
- Rigorous "resolved" / "outcome" definition in MSA (legal exposure if loose)
- Monthly invoice with per-resolution detail (procurement friction)
- Reconciliation workflow with customer (a sales / CS task)
- Forecasting discipline (revenue volatility -> rolling forecast)
- Commission complexity for sales team (commission on what? consider booked-MRR-equivalent)

Per-agent / per-seat pricing is procurement-friendly but pricing-power-weak; consider as a transition pricing for SMB / mid-market while building outcome data, then move to outcome pricing.

## 5. Narrative Frames

For investor / customer narrative:

- "We replace the call centre seat at 20-40% of cost with better SLA" (CX agent)
- "We recover the unrecoverable, on commission only" (collections agent)
- "Your back-office at 1/3 the cost with full audit trail" (ops agent)
- "Sector-leading vertical agent with regulator-accepted audit log" (vertical agent)
- "Agent platform: build vertical agents in 8 weeks, not 18 months" (platform)

## 6. Anti-Patterns

- Per-seat agent pricing
- Per-query agent pricing
- No intervention-credit policy
- No SLA tie
- No vendor-cost pass-through clause
- Local-currency pricing with USD costs and no FX clause
- Outcome pricing without rigorous outcome definition
- Bundling that hides agent value
- Commission structure misaligned with usage-based revenue

## 7. Cross-References

- Architecture: `saas-agent-pricing-strategy/references/saas-agent-pricing-architecture.md`
- Cost floor: `saas-agent-unit-economics-and-cogs`
- Moat-based premium: `saas-agent-moat-and-wrapper-risk`
- Pricing skill: `meta-pricing-strategy`
