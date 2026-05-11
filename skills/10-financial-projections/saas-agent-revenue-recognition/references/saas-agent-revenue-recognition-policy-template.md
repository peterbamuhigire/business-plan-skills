---
source: ASC 606 (FASB 2014) / IFRS 15 (IASB 2014); Big-4 agent-business interpretive guidance 2024-2026; engine synthesis from agent-products audit (2026) and agent-SLA-commercial audit (2026)
frameworks: [ASC 606 5-step; IFRS 15 5-step; Variable consideration estimation and constraint; Principal-vs-agent indicators; Breakage; Contract modification]
skill: saas-agent-revenue-recognition
cross-reference: [saas-agent-deferred-revenue-and-credit-reserves, saas-agent-sla-cogs-treatment, saas-agent-pricing-strategy, meta-agent-revenue-recognition-policy]
---

# Agent Revenue Recognition Policy — Template + Worked Examples

This is the policy memo skeleton an audit firm or DD team will expect. Tailor the language; do not copy verbatim without review. Use British English; convert to US English on request for US audit firms.

## 1. Scope

This policy applies to revenue from the {agent product family / vertical agent product} comprising the following pricing primitives:

- {Per-resolution agent service}
- {Per-outcome agent service}
- {Platform subscription with success fee}
- {Prepaid task credits}
- {SLA-tier subscription bronze / silver / gold}
- {Per-step / per-agent platform service}

The policy is written under {ASC 606 / IFRS 15}; the company {does / does not} report under both frameworks. Where the two frameworks differ materially, the divergence is noted.

## 2. Framework

The company applies the five-step model:

1. Identify the contract with a customer
2. Identify the performance obligations in the contract
3. Determine the transaction price
4. Allocate the transaction price to the performance obligations
5. Recognise revenue when (or as) the entity satisfies a performance obligation

Each pricing primitive in scope is analysed per the five steps below.

## 3. Pricing primitive — Per-resolution agent service

### Step 1 — The contract
A master services agreement establishing the company's right to receive consideration for resolved tickets and the customer's right to receive resolution services. Enforceable rights and obligations. Commercial substance. Collectability is probable based on customer credit assessment.

### Step 2 — Performance obligations
Each resolved ticket is treated as a distinct service. The customer can benefit from each resolved ticket on its own (the resolution is the value delivered). The series guidance (ASC 606-10-25-15) is **not** applied because individual resolutions vary in substance and the pattern of transfer is not the same; therefore each resolution is a distinct performance obligation recognised at the point in time of acceptance.

### Step 3 — Transaction price
Fixed price per resolution as stated in the agreement: $X.XX per resolved ticket. Variable consideration components:
- **SLA credits** for breach of uptime / response-time / accuracy SLA — reduce transaction price; estimated using expected-value method; **constrained** to the amount for which it is probable no significant reversal will occur
- **Volume rebates** for monthly resolved-ticket thresholds — variable consideration; estimated and constrained
- **Refunds** for tickets the customer rejects within the rejection window — variable consideration; estimated as % of resolved tickets historically rejected

### Step 4 — Allocation
A per-resolution price applies to each resolved ticket; allocation is unit-by-unit. Where bundled with platform fee (Section 5 below), the standalone selling price of each component is observable from segmented pricing schedules; allocation is straightforward.

### Step 5 — Recognition
Recognised at the point in time of customer acceptance of the resolved ticket. Acceptance is evidenced by:
- Explicit acceptance click in the ticketing system; or
- Auto-acceptance after {N hours} of no rejection by the customer

The acceptance log in the ticketing system is the source-of-truth audit evidence. Revenue is reduced contemporaneously for expected SLA credits and refunds based on the constrained variable-consideration estimate. Estimates are reassessed quarterly.

### Worked example
- 10,000 resolved tickets in the quarter at $3.50/ticket = $35,000 gross
- Estimated SLA credits at 2.0% of gross (constrained from a 1.5-3.0% range) = $700
- Estimated refunds at 1.2% of gross (constrained from 0.8-1.8%) = $420
- Net revenue recognised = $35,000 - $700 - $420 = $33,880

## 4. Pricing primitive — Per-outcome agent service

### Step 1 — The contract
Master services agreement with outcome definition appendix. Counter-party verification process (claim paid; code accepted; permit issued; debt recovered) is specified contractually.

### Step 2 — Performance obligations
Each outcome is a distinct performance obligation. The customer obtains control of the outcome at the point of counter-party verification.

### Step 3 — Transaction price
Outcome-conditional. Examples:
- 12% commission on recovered amount (collections agent)
- $X per accepted medical code (medical-coding agent)
- $X per legal document filed and accepted (legal agent)

This is variable consideration estimated using:
- **Expected value** (probability-weighted) where multiple outcome levels exist
- **Most likely amount** where binary outcomes apply

Constraint applied: include only the amount for which it is probable no significant reversal will occur.

### Step 4 — Allocation
Per-outcome price applies to each outcome.

### Step 5 — Recognition
At the point in time the outcome is verified by the counter-party process. Recognition trigger evidence:
- Counter-party payment receipt (collections)
- Payer remittance advice with code acceptance (medical coding)
- Court / regulator filing acceptance (legal)
- Claim settlement notification (insurance)

### Worked example (collections agent)
- Portfolio assigned $1,000,000; commission 12% on recovered
- Historical recovery rate 35% (range 20-50%, std dev 8pp)
- Expected variable consideration = $1,000,000 × 35% × 12% = $42,000
- Constraint applied: only $30,000 is probable not to reverse (recovery could land at 25% giving $30,000 commission)
- Recognise $30,000 as cumulative recoveries occur and outcomes are verified
- Book additional $12,000 as variability resolves
- Reassess quarterly

## 5. Pricing primitive — Subscription + success fee

### Step 1 — The contract
Master services agreement with monthly platform fee and outcome-conditional success fee.

### Step 2 — Performance obligations
**Two distinct performance obligations:**
- (a) Platform access (delivered over time)
- (b) Success-fee outcome (delivered at point in time of outcome verification)

These are distinct because: (i) the customer can benefit from platform access independently of any specific success outcome (use of the platform, access to tools, reports); and (ii) the success fee is separately identifiable in the contract as a distinct outcome.

### Step 3 — Transaction price
Platform fee: fixed ($X/month). Success fee: variable consideration estimated + constrained.

### Step 4 — Allocation
Standalone selling price approach:
- Platform fee SSP = the monthly fee charged to customers who buy platform only
- Success fee SSP = the success fee charged to customers who buy success-fee only (rare) or estimated using expected-cost-plus-margin approach

If SSPs are observable, allocate directly. If not, estimate.

### Step 5 — Recognition
- Platform fee — recognised ratably over the subscription term (over time)
- Success fee — recognised at point in time of outcome verification, net of expected SLA credits and refunds

### Worked example
- Annual contract: $24,000 platform fee + estimated $40,000 success fee over the year
- Platform fee: $2,000/month over 12 months
- Success fee: recognised as each outcome verifies; estimate at quarter-end uses expected-value method; constraint applied

## 6. Pricing primitive — Prepaid task credits

### Step 1 — The contract
Customer prepays for N task credits redeemable over the contract term.

### Step 2 — Performance obligation
Stand-ready obligation to provide agent services in exchange for credit drawdown. Each credit consumed = a distinct service.

### Step 3 — Transaction price
Fixed: cash received at prepayment.

### Step 4 — Allocation
Per credit, at the contractual rate.

### Step 5 — Recognition
- Cash received on prepayment: recognised as **deferred revenue** (contract liability) on the balance sheet
- Recognised as revenue **as credits are consumed** (in the pattern matching consumption)
- **Breakage** — when the customer's exercise of remaining rights becomes remote, the remaining deferred revenue is recognised as breakage revenue (ASC 606 BC394 / IFRS 15.B46). Breakage is estimated using historical patterns (typically X% of prepaid credits go unused) and recognised proportionally as credits are consumed (proportional method) rather than waiting until expiry.

### Worked example
- Customer prepays $10,000 for 4,000 task credits at $2.50/credit
- Day 1: $10,000 cash received; $10,000 deferred revenue booked
- Month 1: 800 credits consumed; recognise (800 × $2.50) = $2,000 as revenue; deferred revenue balance $8,000
- Historical breakage = 8% of prepaid credits unused
- Proportional method: recognise breakage in proportion to expected non-breakage; that is, for each $1 recognised on consumed credits, recognise $0.087 of breakage
- Month 1 breakage = $2,000 × (8/92) = $174
- Total Month 1 revenue = $2,000 + $174 = $2,174
- Deferred revenue end of Month 1 = $10,000 - $2,000 - $174 = $7,826
- Reassess breakage assumption quarterly

## 7. Pricing primitive — SLA-tier subscription (bronze / silver / gold)

### Step 1 — The contract
Tier purchase with SLA schedule (uptime %, response time, accuracy, escalation timeliness, support hours).

### Step 2 — Performance obligation
Tier-level platform access delivered over time. Single performance obligation per tier.

### Step 3 — Transaction price
Tier price (fixed). Variable: SLA credits accrued during breach periods.

### Step 4 — Allocation
Per tier.

### Step 5 — Recognition
Ratable over the tier term. SLA credits reduce the transaction price at the time of the breach and are estimated quarterly.

### Worked example
- Gold tier: $5,000/month with 99.9% uptime, 1-hour response, 95% accuracy SLA
- Breach occurs in Month 2: uptime fell to 99.5% (below 99.9% SLA); contracted credit = 10% of monthly fee = $500
- Month 1 revenue: $5,000
- Month 2 revenue: $5,000 - $500 = $4,500
- Quarterly estimate going forward includes expected SLA-credit accrual based on historical breach rate

## 8. Pricing primitive — Per-step or per-agent platform (infrastructure)

### Step 1-4 (abbreviated)
Per-step metering or per-agent monthly fee.

### Step 5 — Recognition
- Per-step: as steps invoked (point-in-time per step, in practice aggregated and recognised periodically)
- Per-agent: ratable over the period the agent is active

## 9. Variable consideration estimation method

For each pricing primitive with variable consideration:

| Component | Method | Constraint applied |
|---|---|---|
| SLA credits | Expected value | Yes; include only constrained amount |
| Refunds | Expected value | Yes |
| Volume rebates | Most likely amount (binary) or expected value (tiered) | Yes |
| Success fee | Expected value | Yes |
| Outcome-conditional commission | Expected value | Yes |
| Breakage | Expected value based on historical pattern | Yes |

**Reassessment:** quarterly minimum; immediate on trigger events (SLA performance shift; foundation-model cost shock; new customer cohort behaviour; regulator action).

## 10. Principal-vs-agent analysis

For revenue from third-party services orchestrated by the agent:

| Indicator | Principal | Agent |
|---|---|---|
| Primary responsibility for fulfilling the promise | Yes → principal | No → agent |
| Inventory risk before / after transfer | Yes → principal | No → agent |
| Pricing discretion | Yes → principal | No → agent |
| Customer credit risk | Yes → principal | No → agent |

If majority of indicators point principal: recognise gross. If agent: recognise net (commission only). Document the determination; reassess on service-flow change.

## 11. Contract modifications

| Modification type | Treatment |
|---|---|
| Adds distinct services at standalone selling price | Separate contract; account prospectively |
| Adds distinct services but not at standalone selling price | Termination of original + creation of new contract; reallocate remaining transaction price |
| Does not add distinct services | Cumulative catch-up to revenue |

Common agent modifications: autonomy expansion (typically no new performance obligation; cumulative catch-up if pricing changes); SLA tier upgrade (new performance obligation if distinct tier; otherwise modification); new action class promoted (new performance obligation if priced separately).

## 12. Disclosure

Per ASC 606-10-50 / IFRS 15.110-129:
- Disaggregation of revenue by pricing primitive
- Contract balances (receivable, contract assets, contract liabilities)
- Performance obligations (description, when satisfied, significant payment terms, nature of goods/services, returns / refunds / warranties)
- Significant judgments — variable-consideration estimation; constraint; SSP; principal-vs-agent; recognition timing

## 13. Worked illustrative income statement extract

(in $ thousands; year)

| Line | Amount | Notes |
|---|---|---|
| Per-resolution revenue (gross) | 1,400 | 400,000 resolutions × $3.50 |
| Per-resolution SLA credits | (28) | 2.0% constrained estimate |
| Per-resolution refunds | (17) | 1.2% constrained estimate |
| Per-resolution revenue (net) | 1,355 |  |
| Per-outcome revenue (recognised) | 380 | Constrained estimate of $480 expected |
| Subscription revenue | 720 | $5k × 12 × 12 customers |
| Subscription SLA credits | (14) | Estimated 2% |
| Success-fee revenue (recognised) | 240 | Constrained estimate of $320 |
| Prepaid-credit revenue (consumed) | 180 | Out of $220 deferred prior period |
| Breakage revenue | 16 | Proportional method on historical 8% |
| Platform per-step revenue | 95 | As metered |
| **Total revenue** | **2,972** |  |

Balance sheet:
- Deferred revenue: $245 (remaining prepaid credit balance)
- SLA-credit reserve (accrued liability): $42 (next-period expected credits)
- Refund reserve: $19

## 14. Cross-references

- Deferred revenue and reserve mechanics: `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md`
- SLA-COGS treatment: `skills/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md`
- Pricing primitives: `skills/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md`
- Meta policy discipline: `skills/meta-agent-revenue-recognition-policy/SKILL.md`
- Accounting controls: `book-extractions/accounting-bookkeeping-finance-controls-extraction.md`

## 15. Africa / Uganda overlay

- **VAT and revenue recognition** — VAT is invoice-event-based, not recognition-event-based; for per-resolution micro-billing in Uganda (18% VAT), VAT is on the aggregated invoice; for prepaid credits VAT applies on prepayment; reconciliation between VAT-output and revenue-recognised must be documented.
- **Withholding tax** — Uganda 6% (Schedule 6), Kenya variable, Nigeria 5% on services — net the receivable; gross-up revenue recognition.
- **FX revaluation under IAS 21** — local-currency receivables revalue at each closing date; gain/loss to P&L; isolated from revenue recognition itself.
- **Mobile-money cash-vs-revenue** — recognition trigger is acceptance, not settlement; mobile-money settlement is T+0 to T+2; reconcile daily.
- **Public-sector receivables** — collectability constraint may defer recognition where DSO history exceeds 120 days.
- **Audit-firm acceptance** — KPMG, PwC, Deloitte, EY in-region accept IFRS 15 directly; mid-tier may need policy-memo support; local firms benefit from this template.
