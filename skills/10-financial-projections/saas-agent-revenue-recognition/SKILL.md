---
name: saas-agent-revenue-recognition
description: ASC 606 / IFRS 15 revenue recognition for agent products — per-resolution = point-in-time at successful resolution; per-outcome = point-in-time at outcome verification; subscription + success fee = bundled allocation with two performance obligations; prepaid task credits = deferred revenue with breakage; variable-consideration estimation under the constraint; principal-vs-agent. Sits on top of standard SaaS rev-rec. Use whenever an agent product is priced on a non-ratable basis.
---

# SaaS Agent Revenue Recognition Skill

## Overview

Standard SaaS revenue recognition assumes a ratable subscription with a single performance obligation delivered over time. Agent revenue does not behave that way:

- **Per-resolution pricing** triggers recognition at a point in time — when the customer accepts that the ticket is resolved.
- **Per-outcome pricing** triggers recognition at a point in time — when the counter-party process verifies the outcome (recovery posted, code accepted by payer, document filed and accepted, claim paid).
- **Subscription + success-fee hybrid** has two distinct performance obligations and a transaction-price allocation problem.
- **Prepaid task credits** create deferred revenue with breakage estimation under ASC 606 BC394 / IFRS 15.B46.
- **Outcome-conditional revenue** is variable consideration that must be estimated and then constrained.
- **Marketplace agents** that orchestrate third-party tools or services require a principal-vs-agent determination at the gross-vs-net revenue boundary.

Getting this wrong destroys investor trust, attracts audit qualification, and (most commonly) overstates revenue. Investors and auditors are increasingly explicit about agent rev-rec policy in 2026 because the patterns are new and the prior-period restatement risk is real.

This skill installs the agent revenue recognition discipline — the per-pricing-primitive policy memo that auditors and DD teams will request.

## Use When

- A SaaS / ICT plan ships an agent product priced on per-resolution, per-outcome, prepaid credits, subscription + success fee, or any other non-ratable primitive
- The plan must pass an audit (Big-4 / regional firm) or DFI / institutional DD
- An auditor or DD team has requested the revenue recognition policy memo
- The plan involves outcome-conditional revenue and the variable-consideration treatment must be defensible
- An agent platform sells to other agent builders and the principal-vs-agent test must be applied
- The financial model recognises agent revenue and the recognition trigger must be reconciled with the cash and billing cycle
- Cross-loaded with `saas-agent-pricing-strategy` and `saas-agent-deferred-revenue-and-credit-reserves`

## Do Not Use When

- The agent product is priced on a flat monthly subscription with a single deliverable (use standard SaaS rev-rec)
- The plan is pre-revenue and the pricing primitive is not yet committed (use directional treatment)
- The product is internal-efficiency only with no external customer (rev-rec does not apply)

## Required Inputs

- Pricing primitive(s) in use (from `saas-agent-pricing-strategy`)
- Contract templates or commercial-term sheets (from proposal session)
- Definition-of-done for "resolved" / "outcome" / "successful task" — must be objectively measurable
- SLA terms (credit % per breach; credit caps; credit currency)
- Refund policy (full / partial / none)
- Prepaid-credit terms (expiry; non-refundable; transferable; rollover)
- Variable-consideration scope (success fees, volume rebates, performance bonuses)
- Principal-vs-agent indicators (control of the service before transfer; primary responsibility; inventory risk; pricing discretion)
- Tax jurisdiction and applicable framework (US GAAP / IFRS / local GAAP)
- Audit firm (if appointed) and any prior rev-rec opinion on related products

## Workflow

### 1. Identify the pricing primitive(s) in scope

Map each revenue line in the plan to one of:
- **Per-resolution / per-task** — point-in-time recognition at acceptance
- **Per-outcome** — point-in-time recognition at counter-party verification
- **Subscription / platform fee** — ratable over contract term
- **Success fee on top of subscription** — variable consideration; estimated + constrained
- **Prepaid task credits** — deferred revenue, recognised as credits consumed; breakage estimated
- **Per-agent or per-seat tier** — ratable over contract term
- **Per-step (platform / infrastructure)** — usage-based; recognised as steps consumed
- **Outcome-based with refund** — variable consideration; recognised net of expected refunds (constrained)
- **SLA-tier (bronze / silver / gold)** — ratable per tier; SLA credits are reductions in transaction price

If multiple primitives are bundled in a single contract, treat each as a distinct revenue stream and apply the ASC 606 5-step model to the contract as a whole.

### 2. Apply the ASC 606 / IFRS 15 five-step model

Per `references/saas-agent-revenue-recognition-policy-template.md` — for each contract / contract type:

1. **Identify the contract** — enforceable rights and obligations; commercial substance; collectability probable
2. **Identify the performance obligations** — distinct goods or services; capable of being distinct + distinct in the context of the contract; common patterns:
   - Subscription / platform access = one performance obligation, delivered over time
   - Per-resolution agent service = a series of distinct services treated as a single performance obligation only if they meet ASC 606-10-25-15 (substantially the same + same pattern of transfer); typically agent resolutions are each distinct services recognised point-in-time per resolution
   - Implementation / onboarding = separate performance obligation if distinct, else combined with subscription
   - Success fee = often a separate performance obligation tied to a specific outcome
3. **Determine the transaction price** — fixed + variable + financing component + non-cash + consideration payable to customer:
   - **Variable consideration** for outcome pricing, success fees, volume rebates, refund risk — estimate using **expected-value** (probability-weighted) or **most-likely-amount** method, whichever better predicts entitled consideration
   - **Constraint on variable consideration** (ASC 606-10-32-11) — include only the amount for which it is probable a significant reversal will not occur; this is the discipline-keeping step
   - **SLA credits** — reduction in transaction price; estimate expected credits using same approach as variable consideration
   - **Refund liability** — reduction in transaction price for the portion expected to be refunded
4. **Allocate the transaction price** to performance obligations — based on standalone selling price (SSP); use observable SSP if available, else estimate (adjusted market assessment, expected cost plus margin, residual approach where permitted)
5. **Recognise revenue** when (or as) each performance obligation is satisfied:
   - **Point-in-time** for per-resolution / per-outcome / per-task — recognise when customer obtains control (typically acceptance / verification)
   - **Over time** for subscription / platform access — recognise ratably
   - **Series guidance** where applicable for repetitive distinct services

### 3. Determine recognition trigger per pricing primitive

| Primitive | Recognition trigger | Evidence required |
|---|---|---|
| Per-resolution | Customer acceptance of resolved ticket | Acceptance log; auto-acceptance after N hours of no rejection; tracked in ticketing system |
| Per-outcome | Counter-party verification of outcome (claim paid; code accepted; document filed) | Counter-party confirmation; objective external evidence |
| Subscription / platform fee | Ratable over contract term | Contract term in writing; service available |
| Success fee | Outcome achieved + counter-party verified | Same as per-outcome |
| Prepaid task credits | As credits consumed | Credit consumption log; per-credit policy |
| Breakage on prepaid | When customer's exercise of remaining rights becomes remote (typically tracked using historical breakage %) | Breakage estimate documented |
| Per-step (platform) | As steps invoked and metered | Metering log |
| SLA tier | Ratable over tier term; SLA credits reduce transaction price | Tier purchase + SLA-credit accrual |

### 4. Treat variable consideration

For outcome pricing, success fees, volume rebates, and refund risk:

- **Estimation method:** expected-value (probability-weighted across a range) is appropriate for many outcomes; most-likely-amount is appropriate when only two outcomes are possible (succeed / fail)
- **Constraint:** include the variable consideration only to the extent it is **probable** (US GAAP) / **highly probable** (IFRS) that a significant reversal will not occur when the uncertainty resolves
- **Reassessment:** update estimates at each reporting date; recognise change as cumulative catch-up

Worked example: a collections agent on per-outcome pricing earns 12% of recovered amount; historical recovery rate on assigned PAR>90 portfolios is 35%; portfolio value $1,000,000. Expected variable consideration = 35% × $1,000,000 × 12% = $42,000. Apply constraint: if historical variation is wide (e.g. 20-50% recovery), constrain to (e.g.) $30,000 — the amount for which it is probable no significant reversal will occur. Recognise $30,000 as cumulative recoveries occur; book the additional $12,000 over time as variability resolves.

### 5. Apply principal-vs-agent analysis

For agents that orchestrate third-party services (calling external APIs, brokering services, paying suppliers on behalf of customer):

- **Principal** indicators: primary responsibility for fulfilling the promise; inventory risk before or after transfer; discretion in establishing the price — recognise revenue **gross**
- **Agent** indicators: another party primarily responsible; no inventory risk; no pricing discretion — recognise revenue **net** (the commission only)

This determination materially changes top-line ARR and gross margin reporting. Document the test outcome and the indicators relied upon.

### 6. Treat contract modifications

Agent contracts modify often (autonomy expansion; new action class promoted; pricing change; SLA tier upgrade). For each modification:
- **Separate contract** if the modification adds distinct goods or services at standalone selling price
- **Termination + new contract** if the remaining services are distinct and price reflects fair standalone value
- **Cumulative catch-up** if the remaining services are not distinct

Document the modification treatment in the policy memo.

### 7. Document the auditor-ready policy memo

Per `references/saas-agent-revenue-recognition-policy-template.md`, produce a policy memo covering:
- Each pricing primitive in scope
- Performance obligations identified
- Transaction price determination including variable consideration method
- Constraint applied with reasoning
- Allocation method
- Recognition trigger with evidence
- Principal-vs-agent conclusion
- Contract-modification policy
- Examples and edge cases
- Cross-reference to the deferred revenue and reserve methodologies

This memo is the artefact that audit firms request. Without it, the plan is not audit-ready.

### 8. Wire to the financial model

- Each revenue line in the projection traces to a recognition trigger
- Variable consideration is shown net of constraint
- Refund and SLA-credit reserves are visible as reductions in transaction price
- Deferred revenue is visible on the balance sheet
- Breakage assumption is documented
- The cash and revenue lines reconcile (per-resolution cash can lead revenue by 1-3 days under mobile-money; enterprise per-outcome cash can lag revenue by 30-90 days)

### 9. Wire to living-plan governance

Assign cadence and owners per the cadence table below.

## Quality Bar

- Each revenue line in the plan maps to a documented pricing primitive
- The ASC 606 / IFRS 15 5-step analysis is shown explicitly (not implied)
- Variable consideration is estimated and constrained
- The constraint is non-trivial (auditors test whether the constraint was applied)
- Principal-vs-agent analysis is performed for marketplace / orchestration revenue
- Recognition trigger is named per primitive and tied to an evidence source
- Contract-modification policy is stated
- A worked example for each pricing primitive is in the policy memo
- The memo is written to auditor standard (defensible in a comment letter)
- Cross-referenced to deferred-revenue and reserve methodologies
- A Big-4 partner reviewing the plan would not laugh at the policy

## Anti-Patterns

- "We recognise on invoice" without identifying the performance obligation
- Recognising the full success-fee at contract signing — fails variable-consideration constraint
- Treating prepaid credits as revenue when sold — fails deferred-revenue rule
- No principal-vs-agent analysis for marketplace agents — overstates ARR and gross margin
- "We follow ASC 606" without showing the 5 steps — auditors test the steps
- Recognising per-resolution at billing rather than at acceptance — creates timing distortion
- No constraint on variable consideration — overstates current revenue
- No reassessment cadence for variable consideration — stale estimates persist
- Treating SLA credits as a marketing expense — they are a transaction-price reduction
- Recognising prepaid breakage at year-end without a defensible historical pattern
- Bundling subscription + success fee into one performance obligation — fails the distinct test

## Outputs

- Pricing primitive inventory with recognition trigger per primitive
- ASC 606 / IFRS 15 5-step analysis per contract type
- Variable-consideration estimation and constraint documentation
- Principal-vs-agent analysis (where applicable)
- Auditor-ready revenue recognition policy memo
- Contract-modification policy
- Worked examples per primitive
- Cross-reference to deferred revenue and reserves
- Cross-reference to SLA-COGS treatment
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Revenue recognition by primitive (variance vs plan) | monthly | CFO + Controller | -5% by primitive |
| Variable-consideration estimate reassessment | quarterly | Controller | estimate change >10% |
| Constraint reassessment | quarterly | Controller + CFO | constraint change |
| Principal-vs-agent reassessment | quarterly | Controller + CFO | service-flow change |
| Breakage estimate reassessment | quarterly | Controller | historical-pattern change |
| Policy memo refresh | annually + on new primitive | CFO + Controller + Auditor | new pricing primitive |
| Contract-modification log | continuous + monthly | Controller | modification volume spike |

## References

- `references/saas-agent-revenue-recognition-policy-template.md` — policy memo template with worked examples per primitive
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — liability side
- `skills/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md` — COGS-vs-contra-revenue
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — unit economics
- `skills/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md` — pricing primitives
- `skills/meta-agent-revenue-recognition-policy/SKILL.md` — meta policy declaration discipline
- `skills/meta-accounting-finance-review/SKILL.md` — accounting review gate
- `skills/meta-living-plan-governance/SKILL.md` — governance parent
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — this audit
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent product audit
- `book-extractions/accounting-bookkeeping-finance-controls-extraction.md` — controls

## Africa / Uganda Application Notes

- **Mobile-money settlement timing** — per-resolution agent revenue collected through MoMo / M-Pesa / Airtel Money / Wave / Orange Money settles T+0 to T+2; recognition trigger is still customer acceptance, not settlement, but the cash-vs-revenue reconciliation must be explicit. Recognise at acceptance; receivable until settlement; collected on settlement; reconcile daily.
- **IFRS in Africa** — most African markets (KE, NG, ZA, UG, TZ, RW, GH) use IFRS; Egypt uses EAS with IFRS convergence. IFRS 15 applies with effectively the same 5-step model as ASC 606; small wording differences (highly probable vs probable in the constraint) matter.
- **VAT timing** — VAT in Uganda (18%), Kenya (16%), Nigeria (7.5%), South Africa (15%), Rwanda (18%) is invoice-based, not revenue-recognition-based; for per-resolution micro-billing, VAT is on invoice issued, not on each individual resolution recognised. Document the VAT-vs-revenue-recognition reconciliation.
- **Withholding tax on services** in Uganda (6% under Sched 6), Kenya (variable), Nigeria (5%), South Africa (none on services), Rwanda (variable) — affects net receivable and the cash-vs-revenue line.
- **FX revaluation** — if revenue is recognised in local currency but reported in USD, FX revaluation under IAS 21 / ASC 830 is unavoidable; document the policy.
- **Public-sector receivables in Africa** can age 90-180 days — variable-consideration constraint must include collectability risk explicitly; high-DSO contracts may fail the "probable" collectability test, deferring recognition.
- **Sovereign-AI procurement contracts** often include local-currency pricing with USD index; treat the USD-index adjustment as variable consideration and apply the constraint.
- **DFI / multilateral pilots** sometimes pay on milestone delivery rather than ratable; treat each milestone as a performance obligation if distinct.
- **Audit firms in-region** — KPMG, PwC, Deloitte, EY have full IFRS 15 capability; mid-tier (BDO, RSM, Mazars, Grant Thornton) typically do; smaller local firms may need policy-memo support — provide it.
