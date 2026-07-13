---
name: saas-agent-pricing-strategy
description: Use when producing or reviewing the saas agent pricing strategy component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

## SLA-Tier Pricing Economics Subsection

When agent pricing includes **multi-tier SLA** (bronze / silver / gold or similar), the pricing primitive interacts with the SLA-tier choice in commercially material ways. The full discipline lives in `saas-agent-commercial-packaging-economics/SKILL.md` (packaging dimension) and `saas-agent-sla-risk/SKILL.md` (risk dimension); the pricing subsection here covers:

**Tier-mix economics.**
- Bronze tier (lowest commitment): typically priced 20-40% below blended; attracts price-sensitive customers; SLA-credit risk lower in absolute terms
- Silver tier (standard): the anchor tier; pricing aligned to corridor analysis; SLA-credit risk moderate
- Gold tier (premium): priced 50-150% above blended; serves regulated / enterprise; SLA-credit risk higher in absolute terms (richer credits) but lower in % (tighter operational discipline)

**Cannibalisation risk.**
- If gold tier is too premium-priced, customers downgrade to silver, eroding ARPU
- If bronze tier is too cheap, customers downgrade from silver, eroding ARPU
- Monitor monthly tier-mix; alert on >10% mix shift toward lower tier

**Base-tier erosion risk.**
- When agent product is bundled into a base tier ("agent included"), the base-tier price must rise to absorb agent cost; failing to raise base price = silent margin loss
- Alternative: hold base-tier price, add agent-tier above (add-on or standalone)

**SLA-credit risk per tier.**
- Bronze SLA-credit cap: typically 10-15% of monthly fee
- Silver SLA-credit cap: 20-30%
- Gold SLA-credit cap: 30-50% (sometimes uncapped on response-time but capped on uptime)
- Reserve methodology must size separately per tier (richer tiers = richer credit exposure but lower breach probability)

**FX-corridor per tier.**
- Bronze tier: often local-currency-priced; lower FX-corridor tolerance
- Silver / Gold: USD-indexed common; better FX-corridor protection
- Reserve currency choice per tier

**Cross-reference.**
- `saas-agent-commercial-packaging-economics/SKILL.md` — Included / Add-on / Standalone packaging interplay
- `saas-agent-outcome-pricing-business-case/SKILL.md` — when outcome pricing wins vs loses
- `saas-agent-sla-risk/SKILL.md` — tier-specific SLA-credit risk
- `saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — per-tier reserve methodology
- `saas-agent-investor-narrative-on-sla/SKILL.md` — tier mix narrative for investors

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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| ICP, buying process, channel evidence, price tests, unit economics, and sales capacity for saas agent pricing strategy | Customer research, CRM records, approved financial model, and sales owner | Yes | If absent, price, margin, conversion, or capacity evidence is unavailable, return a testable commercial hypothesis and cap the recommendation at pilot scale. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pricing or packaging decision with margin and adoption guardrails | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent pricing strategy exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent pricing strategy release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Price metric rationale, willingness-to-pay evidence, margin bridge, and failure thresholds | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent pricing strategy decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent pricing strategy review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent pricing strategy, the controlling focus is agent task metric selection, included usage, overage, SLA credits, and willingness-to-pay evidence. This skill may analyse commercial options and draft tests; it may not launch prices, purchase media, contact prospects, alter contracts, or promise outcomes without explicit authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent pricing strategy, loss of evidence about agent task metric selection, included usage, overage, SLA credits, and willingness-to-pay evidence activates degraded mode. If the controlling saas agent pricing strategy evidence is unavailable, the same boundary applies. When price, margin, conversion, or capacity evidence is unavailable, return a testable commercial hypothesis and cap the recommendation at pilot scale. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent pricing strategy, a package or channel grows headline demand while weakening gross margin, trust, or delivery capacity| reject or constrain it, quantify the guardrail, and test the next credible option | Growth recommendations can consume cash or create obligations the business cannot fulfil |
| For saas agent pricing strategy, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent pricing strategy decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent pricing strategy, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete pricing or packaging decision with margin and adoption guardrails, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent pricing strategy decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect icp, buying process, channel evidence, price tests, unit economics, and sales capacity and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce pricing or packaging decision with margin and adoption guardrails with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Pricing or packaging decision with margin and adoption guardrails must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Price metric rationale, willingness-to-pay evidence, margin bridge, and failure thresholds must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent pricing strategy, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent pricing strategy, treating an unavailable icp, buying process, channel evidence, price tests, unit economics, and sales capacity as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing pricing or packaging decision with margin and adoption guardrails that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A per-seat plan allows a small team to run millions of agent actions. Replace seat-only pricing with an evidenced included task allowance and overage, while retaining a predictable customer bill.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent pricing strategy; no local deep-dive reference is declared.
- For saas agent pricing strategy claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
