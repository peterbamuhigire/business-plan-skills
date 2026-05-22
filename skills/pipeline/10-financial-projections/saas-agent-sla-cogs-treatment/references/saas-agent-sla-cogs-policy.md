---
source: ASC 606 / IFRS 15 transaction-price-reduction guidance; ASC 705 / ASC 605 (where applicable) on cost classification; Big-4 SaaS practice 2024-2026; engine synthesis from agent-SLA-commercial audit (2026)
frameworks: [Cost-line classification policy; Contra-revenue vs COGS vs S&M vs G&A; Allocation rules; Disclosure language; Reconciliation discipline]
skill: saas-agent-sla-cogs-treatment
cross-reference: [saas-agent-revenue-recognition-policy-template, saas-agent-credit-reserve-methodology, saas-agent-unit-economics-template]
---

# SLA-COGS Classification Policy — Cost-Line Inventory and Disclosure Language

## 1. Scope

This policy classifies every SLA-related cost line in the agent business across:
- Contra-revenue (reduction of revenue under ASC 606 / IFRS 15)
- COGS (cost of revenue)
- Sales & Marketing (S&M)
- General & Administrative (G&A)
- Research & Development (R&D)

The classification is binding for management reporting and audited financial statements. Reclassifications require CFO approval and (if material) auditor consultation.

## 2. The classification table

| Cost line | Classification | Allocation rule | Rationale |
|---|---|---|---|
| SLA credits issued (uptime / response / accuracy breach) | **Contra-revenue** | Per-customer per-breach; estimated under variable-consideration constraint | ASC 606 / IFRS 15: variable consideration that reduces transaction price |
| Outcome refunds (failed verification) | **Contra-revenue** | Per-failed-outcome; estimated under variable-consideration constraint | Same as above |
| Volume rebates | **Contra-revenue** | Per-tier or per-customer | Same as above |
| Customer concession credits (one-off goodwill) | **Contra-revenue** if commercial nature; **G&A** if marketing-driven | Documented per credit | Judgement; document each |
| HITL labour deployed to defend SLA (intervene to meet uptime / response / accuracy) | **COGS** | Allocate by ticket-time logged against SLA-defence cases | Direct labour for service delivery |
| HITL labour deployed on eval-flagged tickets to maintain accuracy | **COGS** | Same | Same |
| HITL labour deployed on customer-success conversations | **S&M** | By time | CS not service delivery |
| HITL labour deployed on standard intervention (not SLA-driven) | **COGS** | By time | Direct labour |
| Retraining cost amortisation tied to SLA-relevant quality | **COGS** | Amortise across the period the retraining benefit applies | Quality-related cost of revenue |
| Retraining cost amortisation tied to new-capability development | **R&D** | Same | Capability is R&D not COGS |
| SLA-monitoring infrastructure (telemetry, alerting, dashboards) | **COGS** | All if dedicated; allocated if shared | Direct cost of running the SLA-bearing service |
| Observability cost (general; not SLA-specific) | **COGS** | Same | Direct cost of running the service |
| Eval cost (SLA-relevant metrics) | **COGS** | Allocate by eval-suite categorisation | Direct cost of quality assurance |
| Eval cost (capability / new-feature evals) | **R&D** | Same | Capability is R&D |
| Audit-log retention infrastructure | **COGS** | All | Direct cost of running the service |
| LLM cost retried due to SLA breach risk | **COGS** | Retry overhead in unit-economics waterfall | Same as base LLM cost |
| Foundation-model migration cost (forced by deprecation) | **COGS** (amortised) | Amortise across migration benefit period | Cost of maintaining service |
| Refund-processing fees (mobile-money, payment-gateway) | **COGS** | Per refund | Direct cost of refund delivery |
| Customer-success management of SLA conversations | **S&M** | Allocate by time | CS is S&M function |
| Account-management time on SLA-tier upsell / downsell | **S&M** | By time | S&M |
| SLA-as-differentiator marketing content | **S&M** | All | Marketing |
| Legal cost defending SLA disputes | **G&A** | Per matter | Legal is G&A |
| Compliance cost responding to regulator-mandated SLA standards | **G&A** | Per matter | Compliance is G&A |
| Senior management time on SLA escalations | **G&A** | Allocate by time | Management overhead |
| Insurance premium for SLA-related liability coverage (AI E&O, cyber, product liability) | **G&A** | Per policy | Insurance is G&A |
| Sales commission on SLA-tier upsell | **S&M** | Per deal | Commission is S&M |
| Allocation of finance / accounting time on SLA-credit accounting | **G&A** | By time | Back-office G&A |
| Sustainability tracking on SLA-driven energy use | **G&A** (or **COGS** if direct) | Document | Judgement |

## 3. Allocation rules for shared cost lines

Several cost lines support multiple functions. Apply the following allocation rules:

### HITL labour
- Track time by category in the ticketing / case-management system
- Categories: SLA-defence; standard intervention; CS conversation; training / shadow
- Monthly allocation by aggregate time per category
- Document the allocation policy

### Eval engineering time
- Track eval-suite categorisation: production-quality eval (COGS) vs new-capability eval (R&D)
- Monthly allocation by time-tracking
- Document the allocation

### Observability / monitoring infrastructure
- If a single tool serves both SLA-monitoring (COGS) and product analytics (S&M / R&D), allocate by usage or by feature
- Document the allocation

### Customer-success time
- Split by activity: SLA management (S&M); SLA-credit dispute handling (G&A if legal-adjacent); cross-sell / upsell (S&M); renewal management (S&M)
- Monthly allocation

### Foundation-model retraining and migration
- Quality-driven retraining (e.g. retraining to meet accuracy SLA) → COGS (amortised)
- Capability-driven retraining (e.g. retraining for new vertical) → R&D
- Migration forced by provider deprecation → COGS (amortised, because service continuity)

## 4. Disclosure language for the audited financial statements

Sample disclosure language:

### Revenue recognition note (excerpt)
> The Company recognises revenue under {ASC 606 / IFRS 15}. Service Level Agreement (SLA) credits issued to customers for breaches of contractual uptime, response-time, or accuracy commitments are accounted for as **reductions of the transaction price** (variable consideration), estimated using the expected-value method and subject to the constraint that the Company includes such reductions only to the extent it is {probable / highly probable} that a significant reversal in the cumulative amount of revenue recognised will not occur. Outcome refunds on per-outcome service contracts are accounted for in the same manner. Estimates are reassessed quarterly and updated upon trigger events.

### Cost of revenue note (excerpt)
> Cost of revenue includes labour costs of personnel deployed directly on agent service delivery (including Human-in-the-Loop interventions used to maintain SLA performance), infrastructure costs (LLM provider fees, tool-invocation fees, audit-log retention, SLA-monitoring telemetry and alerting), evaluation costs related to production-quality assurance, and amortisation of model retraining costs associated with sustaining service quality. Cost of revenue is presented net of allocations to research and development for capability-development activities.

### SLA reserve note (excerpt)
> The Company maintains a customer-credit liability reflecting SLA credits earned in the current reporting period but not yet processed. The liability is sized by reference to the trailing twelve-month SLA credit issuance rate applied to the forward twelve-month revenue projection, adjusted for known forward-looking changes in service-level commitments, customer mix, and reliability-engineering investments. The methodology is reassessed quarterly. Changes in estimate are recognised through revenue as a cumulative catch-up adjustment.

## 5. Reconciliation discipline

Each reporting period:
- Total gross agent revenue (from billing system)
- Less: SLA credits issued (from SLA-monitoring + approval log)
- Less: refunds issued (from refund log)
- Less: volume rebates (from contract calculations)
- = Net agent revenue (reported)

The reconciliation is a controls evidence item — reviewed at month-end close.

## 6. Worked income statement (extended example)

| Line | Amount ($) | Source |
|---|---|---|
| Gross agent revenue | 3,000,000 | Billing system |
| SLA credits issued | (60,000) | SLA-monitoring approval log |
| Refunds issued | (45,000) | Refund log |
| Volume rebates | (12,000) | Contract calc |
| **Net agent revenue** | **2,883,000** |  |
| LLM cost | 360,000 | Provider invoices |
| LLM retry overhead | 80,000 | Allocation from unit economics |
| Tool cost | 180,000 | Tool-vendor invoices |
| Channel cost (WhatsApp / SMS / USSD / IVR) | 95,000 | Aggregator invoices |
| HITL labour (SLA-defence portion) | 120,000 | Time-tracking, 60% allocation |
| HITL labour (general intervention) | 80,000 | Time-tracking, 40% allocation |
| Retraining amortisation (quality) | 45,000 | Amortisation schedule |
| SLA-monitoring infrastructure | 35,000 | Tooling invoices |
| Other observability | 25,000 | Tooling invoices |
| Eval cost (production quality) | 30,000 | Time-tracking, allocation |
| Audit-log retention | 20,000 | Storage invoices |
| Refund-processing fees | 12,000 | Payment-gateway invoices |
| **Total COGS** | **1,082,000** |  |
| **Gross profit** | **1,801,000** |  |
| **Gross margin** | **62.5%** | On net agent revenue |
| Customer Success (SLA-management) | 80,000 | Time-tracking, 50% allocation |
| Customer Success (other) | 80,000 | 50% allocation |
| Sales commissions on SLA-tier upsell | 30,000 | Commission ledger |
| Marketing (SLA-differentiator content) | 25,000 | Marketing ledger |
| Other S&M | 600,000 |  |
| Engineering (R&D) | 800,000 | Excludes COGS share |
| Eval cost (capability) | 40,000 | Time-tracking, allocation |
| Retraining amortisation (capability) | 30,000 | Amortisation schedule |
| Legal (SLA disputes) | 15,000 | Legal invoices |
| Insurance (SLA-related coverage) | 24,000 | Insurance invoices |
| Compliance | 30,000 |  |
| Other G&A | 250,000 |  |
| **Operating income** | **(173,000)** | Negative; agent business at growth stage |

## 7. Cross-references

- Rev-rec policy: `saas-agent-revenue-recognition-policy-template.md`
- Reserve methodology: `saas-agent-credit-reserve-methodology.md`
- Refund methodology: `saas-agent-refund-reserve-methodology.md`
- Unit economics: `saas-agent-unit-economics-template.md`
- Controls: `meta-agent-sla-financial-controls/SKILL.md`

## 8. Africa / Uganda overlay

- **HITL labour bands** — Uganda UGX 800k-1.5M / month tier-1; UGX 1.5M-3M tier-2 fully loaded; allocation policy the same as US
- **Mobile-money refund fees** — clearly COGS; 1-2.5% per transaction
- **Sovereign-AI in-region compute premium** — 1.5-3x US/EU; COGS regardless
- **VAT classification** — SLA credits reduce VAT-output proportionally on the net revenue basis
- **Withholding tax** — local-currency receivable net of WHT; gross-up revenue recognition
- **Public-sector contract overhead** — local-entity / local-support cost = COGS (direct cost of service)
- **DFI / multilateral DD** — explicitly checks contra-revenue treatment of SLA credits; provide the policy memo
