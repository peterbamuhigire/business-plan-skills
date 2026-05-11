---
name: saas-agent-pricing-strategy
description: Design agent-product pricing using the agent-specific pricing primitives — per-resolution / per-outcome / per-step / per-agent / hybrid — with intervention-credit reduction, success-conditional pricing, SLA-tied pricing, vendor-cost pass-through, and FX-corridor protection. Sits on top of `saas-ai-pricing-strategy`. Use whenever a SaaS plan ships an agent or multi-agent product whose value is measured in actions, outcomes, or resolutions rather than in seats or queries.
---

# SaaS Agent Pricing Strategy Skill

## Overview

AI-feature pricing (handled by `saas-ai-pricing-strategy`) covers tier x allowance x overage x FX. **Agent pricing** must additionally treat **outcome-conditional pricing** (you only pay when the agent succeeds), **intervention-credit reduction** (when HITL or human-final takes over, the customer is credited), **per-step pricing** (when the agent platform is sold to other agent builders), and **price-corridor analysis** (the band between minimum-margin price and maximum-willingness-to-pay) as first-class primitives.

The agent pricing decision is the most consequential commercial decision in an agent business because it determines:

- Whether the cost-floor (cost-per-resolved-task) sits below price (margin) or above (loss)
- Whether the customer's willingness-to-pay anchor is "per ticket" (replacing human cost) or "per seat" (replacing software cost) — these are wildly different
- Whether success and intervention are aligned between vendor and customer
- Whether FX shocks destroy margin
- Whether foundation-model price spikes destroy margin

## Use When

- Designing pricing for a single-agent or multi-agent product
- Section 07 is being built for an agent-product plan
- An AI-SaaS is moving from per-seat / per-query to per-resolution / per-outcome
- A pricing experiment is planned and the corridor analysis must be done first
- Pricing must be defensible to an agent-fund investor at A
- A vertical agent is being sold into a regulated market where outcome pricing is expected (legal, healthcare, finance, public-sector)

## Do Not Use When

- The product is an AI feature inside a normal SaaS — use `saas-ai-pricing-strategy`
- The product is not yet at PMF and pricing experimentation is premature — use `saas-mvp-and-product-market-fit-strategy` first
- The business is not SaaS / subscription / usage / outcome-based recurring

## Required Inputs

- Cost-per-resolved-task from `saas-agent-unit-economics-and-cogs` (USD + local)
- Agent gross margin target
- Customer willingness-to-pay anchor (what is the customer replacing? human FTE cost? per-ticket cost? per-case cost? per-claim cost?)
- Intervention rate and trend
- Task success rate and trend
- Failure / abandonment rate
- SLA expectations (resolution time; quality bar; escalation path)
- Competitor pricing (agent and non-agent)
- FX corridor (USD volatility vs local revenue)
- Vendor-cost concentration (one provider or multi-vendor)
- Contract length expectations (annual / multi-year for enterprise; monthly for SMB)

## Workflow

1. **Identify the value anchor** — what is the customer replacing? This sets the willingness-to-pay ceiling. Examples:
   - Replacing a tier-1 customer-service agent (UGX 1.2M / month fully loaded; ~UGX 1,000 per ticket at 1,200 tickets / agent / month) -> price per ticket should sit at 20-50% of UGX 1,000
   - Replacing a paralegal hour (USD 30-60 internal cost; USD 80-150 billed) -> price per outcome should be a fraction of the billed equivalent
   - Replacing a collections call-centre seat -> price per resolved case should be a fraction of the recovery commission
2. **Compute the cost-floor** — the minimum price that holds target gross margin given cost-per-resolved-task across the FX corridor and intervention range. Use `references/saas-agent-pricing-architecture.md`.
3. **Choose the pricing primitive(s)** — per-resolution, per-outcome, per-step, per-agent / per-seat, or hybrid. See decision rubric in references.
4. **Design the intervention-credit reduction** — when HITL or human-final takes over, what gets credited? Common patterns:
   - **Full credit** on HITL takeover (customer pays only on agent-only resolution) — generous; aligns incentives; risks revenue volatility
   - **Partial credit** on HITL takeover (customer pays 30-50%) — balanced
   - **No credit, but capped intervention budget** — customer pays per attempt; budget cap protects them
   - **Tiered credit by reason** (model failed = full credit; customer ambiguity = no credit) — most aligned but operationally complex
5. **Add the SLA tie** — what happens if SLA breached (response time, quality bar, escalation timeliness)? Common: 5-15% credit per SLA breach; absolute cap on monthly credits.
6. **Set the vendor-cost pass-through clause** — agent businesses are USD-cost exposed. Contracts >12 months should include a price-adjustment clause tied to provider pricing (e.g. "if blended LLM cost rises >25% YoY, vendor may adjust price with 60-day notice"). DFI and enterprise customers expect this in 2026.
7. **Run the price-corridor analysis** — for each pricing primitive, compute:
   - **Minimum-margin price** (cost-floor x (1 / (1 - target_gm)))
   - **Competitive-anchor price** (alternative cost: human FTE / competing software / status quo / "do nothing")
   - **Value-ceiling price** (customer's willingness-to-pay maximum)
   - The viable corridor is from min-margin to value-ceiling; price should sit above competitive anchor and below value-ceiling.
8. **Stress the pricing** — at provider 2x, at intervention rate 2x, at FX 20% depreciation, at failure rate 2x: does the price still hold target margin? Where does it break?
9. **Compose with the AI / SaaS pricing layers** — agent pricing typically sits inside a broader contract (platform fee + agent usage). Specify how agent usage rolls up to ARR, NRR, and ACV.
10. **Wire to the living plan** — assign cadence and owners.

## Quality Bar

- Cost-floor explicitly computed from `saas-agent-unit-economics-and-cogs`
- Value anchor named and justified (not "industry rate" hand-waving)
- Pricing primitive chosen with reasoning; alternatives considered
- Intervention-credit policy designed; not absent
- SLA-tie included; not absent
- Vendor-cost pass-through clause specified for contracts >12 months
- Price corridor diagrammed (min-margin / competitive-anchor / value-ceiling / chosen point)
- Stress-tested across provider 2x, intervention 2x, FX 20%, failure 2x
- FX-corridor protection explicit when revenue is local currency
- Cross-referenced to agent unit economics and to risk register

## Anti-Patterns

- "Per-seat" pricing on agent products — destroys value-capture (the customer's cost-replacement anchor is per-task, not per-seat)
- "Per-query" pricing on agent products — customer counts internal steps; resentment grows; cost-pass-through fight at every renewal
- Per-resolution price set without cost-floor analysis — silent margin loss
- Per-resolution price set above value-ceiling — undermines adoption
- No intervention-credit policy — customer pays for failed agent and is angry; churn risk
- No SLA tie — enterprise procurement will not sign
- No vendor-cost pass-through clause — first provider price hike kills the contract margin
- Pricing in local currency with USD costs and no FX clause — first 15% depreciation eats your margin
- Annual contract pricing with no review trigger — model deprecation 6 months in changes economics
- "Outcome-based pricing" without defining outcome rigorously — the legal exposure is huge
- Bundle pricing that hides the agent — investor cannot attribute agent revenue and discounts the multiple

## Outputs

- Pricing primitive choice (with rationale)
- Pricing schedule (per-resolution / per-outcome / per-step / per-agent / hybrid)
- Intervention-credit policy
- SLA schedule with credits
- Vendor-cost pass-through clause
- Price corridor (min-margin / competitive-anchor / value-ceiling / chosen point)
- Stress-test under provider 2x, intervention 2x, FX 20%, failure 2x
- FX-corridor protection design
- Composition with platform / tier pricing
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Cost-floor vs price | weekly | CFO + Head of Agent | margin headroom <5pp |
| Intervention rate impact on revenue | weekly | CFO | revenue -5% vs plan |
| SLA-credit accruals | weekly | Customer Success | credit accrual >2% of MRR |
| Price-corridor refresh | quarterly | Head of GTM + CFO | corridor narrows |
| Competitor pricing scan | quarterly | Head of GTM | new entrant undercuts >20% |
| Vendor-cost-pass-through trigger watch | continuous | CFO + CTO | provider raises >25% |
| Win / loss pricing analysis | quarterly | Head of GTM | pricing-driven loss rate up |
| FX corridor breach | continuous | CFO | breach of designed corridor |

## References

- `references/saas-agent-pricing-architecture.md` — primitives, corridor analysis, worked examples
- `references/agent-pricing-and-positioning.md` — positioning ("we charge per resolved ticket, not per seat")
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — cost floor
- `skills/07-marketing-sales-strategy/saas-ai-pricing-strategy/SKILL.md` — AI pricing parent
- `skills/saas-pricing-and-packaging-strategy/SKILL.md` — SaaS pricing parent
- `skills/meta-pricing-strategy/SKILL.md` — Kennedy / Marrs pricing discipline
- `book-extractions/kennedy-no-bs-price-strategy-extraction.md` — pricing-psychology
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit
- `book-extractions/walling-saas-playbook-extraction.md` — SaaS pricing

## Africa / Uganda Application Notes

- The **value anchor in African markets** for agent products is often **a fractional FTE replacement** because tier-1 staff are cheaper (UGX 800k-1.5M / month loaded for tier-1 CX, UGX 1.5M-3M for tier-2). Per-ticket / per-resolution anchors are usually UGX 200-800 (USD 0.05-0.22) — much lower than US benchmarks (USD 1-5 per ticket).
- **Agent value-capture in Africa is volume-driven**, not price-driven. Plan on 5-50x the resolved-task volume of an equivalent US plan to hit the same revenue per agent.
- **WhatsApp / USSD / SMS / IVR channels** require channel-cost pass-through in the agent pricing because the per-conversation tariff is real and varies by aggregator and by country.
- **Mobile-money settlement** (MTN MoMo, Airtel Money, M-Pesa, Wave, Orange Money) for per-resolution micro-billing has per-transaction fees (1-2.5%) — model into cost or aggregate billing.
- **Currency risk on USD-cost agents with local-currency revenue** is the most common margin killer. Either price in USD-equivalent and let local currency float, or include explicit FX corridor headroom (10-15%) in price.
- **DFI / multilateral customers** (UNCDF, World Bank pilots, GIZ, FCDO) expect outcome-based contracts but on cost-recovery terms — margin compressed; build in cost-plus overhead allowance.
- **Public-sector agent contracts** (KE Huduma automation, NG NIMC, RW Irembo, UG NITA-U e-Gov) frequently demand fixed-fee or capped per-citizen-interaction pricing; demand cost-floor protection language and a maximum-volume clause.
- **Subscription + usage hybrid** works in African SMB / mid-market: low-platform fee (UGX 200k-1M / month) plus per-resolved-task variable; reduces SMB churn vs pure-usage.
- **Sovereign-AI procurement** may require pricing in local currency with USD index — design the contract clause.
