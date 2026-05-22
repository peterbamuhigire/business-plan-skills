---
name: saas-agent-sla-cogs-treatment
description: Classify SLA-related cost lines correctly — HITL labour for SLA defence (COGS); SLA credits issued (contra-revenue, NOT opex); outcome refunds (contra-revenue, NOT COGS); retraining amortisation tied to SLA quality (COGS); SLA-monitoring infrastructure (COGS); customer-success cost for SLA management (S&M); legal cost defending SLA disputes (G&A). Disclosure policy. Use whenever an agent product has SLA commitments and the income-statement classification matters.
---

# SaaS Agent SLA-COGS Treatment Skill

## Overview

SLA-related cost lines hit the income statement in four places — **COGS**, **contra-revenue**, **S&M**, or **G&A**. The classification is not a stylistic choice; it is an accounting policy under ASC 606 / IFRS 15 (for the contra-revenue items) and under standard cost-classification guidance (for the opex items). Getting it wrong:

- Overstates revenue (if SLA credits are misclassified as opex)
- Understates COGS (if SLA-defence HITL labour is misclassified as G&A)
- Distorts gross margin (the metric investors lean on hardest)
- Triggers audit adjustments and DD findings

This skill installs the classification discipline and the disclosure policy.

## Use When

- An agent product has contractual SLA commitments and credits, refunds, or related costs
- The income statement must reconcile to gross margin and contribution margin investors will lean on
- An audit firm or DD team has asked for the cost-classification policy
- Cross-loaded with `saas-agent-revenue-recognition`, `saas-agent-deferred-revenue-and-credit-reserves`, and `saas-agent-unit-economics-and-cogs`

## Do Not Use When

- The agent product has no SLA commitments and no refunds
- The plan is pre-revenue and the cost shape is not yet committed (use directional treatment)

## Required Inputs

- Pricing primitive(s) (from `saas-agent-pricing-strategy`)
- SLA terms (from contract templates)
- Cost-line inventory (HITL labour, retraining cost, observability cost, eval cost, CS cost, legal cost, refund-processing cost)
- Functional org chart (who does SLA defence, who manages disputes, who delivers customer success)
- Tooling cost breakdown (LLM, observability, audit-log retention, SLA-monitoring)

## Workflow

### 1. Apply the classification policy

Per `references/saas-agent-sla-cogs-policy.md`, classify each SLA-related cost line:

**COGS (Cost of Revenue):**
- HITL labour deployed specifically to defend SLA (humans intervene to restore service quality)
- HITL labour deployed on eval-flagged tickets to maintain accuracy SLA
- Retraining cost amortisation tied to SLA-relevant quality metrics
- SLA-monitoring infrastructure (telemetry, alerting, dashboards)
- Eval cost specifically on SLA-relevant metrics (accuracy, latency, refusal rate)
- Audit-log retention infrastructure for SLA-evidence purposes
- LLM cost retried because SLA quality threshold not met on first attempt
- Refund-processing cost (mobile-money fees, payment-gateway fees on refund issuance)

**Contra-revenue (reduction of revenue, NOT opex):**
- SLA credits issued (because of breach)
- Outcome refunds (because of failed verification)
- Volume rebates (variable consideration)

**Sales & Marketing (S&M):**
- Customer-success management of SLA conversations
- Account-management time on SLA-tier upsell / downsell
- SLA-as-differentiator marketing content

**General & Administrative (G&A):**
- Legal cost defending SLA disputes
- Compliance cost responding to regulator-mandated SLA standards
- Senior management time on SLA escalations
- Insurance premium for SLA-related liability coverage

### 2. Build the policy memo

Per `references/saas-agent-sla-cogs-policy.md` — produce a policy memo covering:
- Cost-line inventory with classification per line
- Allocation rules for shared cost lines (e.g. an eval engineer who works on both SLA-relevant evals and product-improvement evals — split by time)
- Disclosure language for the audited financial statements

### 3. Wire to the COGS waterfall

Cross-load with `saas-agent-unit-economics-and-cogs`. Each COGS line in the waterfall must map to a classification decision documented here.

### 4. Wire to the contra-revenue presentation

Cross-load with `saas-agent-revenue-recognition`:
- Gross agent revenue
- Less: SLA credits
- Less: refunds
- Less: volume rebates
- Net agent revenue (this is the line that flows to gross margin)

### 5. Reconcile to gross margin

Gross margin = (Net agent revenue - COGS) / Net agent revenue

The SLA-COGS items are part of the COGS subtraction. The SLA-credit and refund items have already reduced revenue (above the GM line) — they do NOT also reduce COGS.

This is the policy that prevents double-counting.

### 6. Worked example

| Line | Amount ($k) | Classification | Notes |
|---|---|---|---|
| Gross agent revenue | 3,000 | Revenue | Before reductions |
| SLA credits issued | (60) | Contra-revenue | 2.0% of gross |
| Refunds issued | (45) | Contra-revenue | 1.5% of gross |
| Net agent revenue | 2,895 |  |  |
| LLM cost (incl. SLA-driven retries) | (480) | COGS | Per `saas-agent-unit-economics-and-cogs` |
| Tool cost | (180) | COGS |  |
| HITL labour (SLA-defence portion) | (120) | COGS | 60% of HITL allocated to SLA defence |
| HITL labour (general intervention) | (80) | COGS | 40% general |
| Retraining amortisation (SLA-relevant) | (45) | COGS |  |
| SLA-monitoring infrastructure | (35) | COGS |  |
| Eval cost (SLA-relevant) | (30) | COGS |  |
| Audit-log retention | (20) | COGS |  |
| Refund-processing fees | (12) | COGS |  |
| **Total COGS** | **(1,002)** |  | 34.6% of net revenue |
| **Gross profit** | **1,893** |  | **65.4% gross margin** |
| Customer Success (SLA-management share) | (80) | S&M | 50% of CS allocated to SLA |
| Customer Success (other) | (80) | S&M |  |
| Legal (SLA-dispute share) | (15) | G&A | 30% of legal allocated to SLA |
| Insurance (SLA-related coverage) | (24) | G&A |  |
| Other opex | (1,200) | S&M / G&A / R&D |  |
| **Operating income** | **494** |  |  |

### 7. Disclosure language

Include in the audited financial statements a note covering:
- SLA-credit policy (contra-revenue, estimated under variable-consideration constraint)
- Refund policy (contra-revenue, estimated under variable-consideration constraint)
- HITL labour classification (COGS where deployed on customer service delivery)
- Retraining amortisation policy (COGS if quality-related; R&D if capability-related)
- Eval cost allocation policy
- Insurance classification

### 8. Wire to bankability and DD

Bankability scorecards (especially DFI / institutional) check:
- Is gross margin reported on net revenue (after SLA credits + refunds)?
- Is HITL labour in COGS?
- Is SLA-credit visible separately?

The classification policy is the artefact that satisfies the check.

### 9. Wire to living-plan governance

Per cadence table below.

## Quality Bar

- Every SLA-related cost line is classified
- Shared cost lines have a documented allocation rule
- SLA credits are contra-revenue, not opex (the #1 misclassification)
- Refunds are contra-revenue, not COGS
- HITL labour for SLA defence is COGS, not S&M
- Retraining classification documented (COGS vs R&D)
- Policy memo defensible in an audit
- Disclosure language drafted
- Gross margin computed on net revenue
- Cross-referenced to rev-rec, reserves, unit economics

## Anti-Patterns

- SLA credits as marketing expense — wrong
- Refunds as COGS — wrong
- HITL labour as S&M — wrong if for service delivery
- All retraining as R&D — wrong if quality-related
- Mixing SLA-monitoring and product observability without allocation
- "We classify intuitively" — audit will require documentation
- Reporting gross margin on gross revenue — overstates
- No disclosure language drafted — DD finding

## Outputs

- Cost-line inventory with classification
- Allocation rules for shared cost lines
- SLA-COGS policy memo
- Disclosure language draft
- Worked income-statement example
- Cross-reference to rev-rec, reserves, unit economics
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| SLA-related COGS share (% of revenue) | monthly | CFO + Controller | +3pp MoM |
| HITL allocation (SLA vs general) | quarterly | Controller + Head of Agent | allocation shift >10% |
| Retraining classification reassessment | quarterly | Controller + CFO + CTO | new training programme |
| Contra-revenue accuracy (credit + refund net visible) | monthly | Controller | reclassification needed |
| Gross-margin reconciliation (net revenue base) | monthly | CFO | misclassification found |
| Policy memo refresh | annually | CFO + Controller + Auditor | new cost line |

## References

- `references/saas-agent-sla-cogs-policy.md` — full classification policy and disclosure language
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — contra-revenue side
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserve side
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — COGS waterfall consumer
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls
- `skills/meta-accounting-finance-review/SKILL.md` — accounting review gate
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit
- `book-extractions/accounting-bookkeeping-finance-controls-extraction.md` — controls reference

## Africa / Uganda Application Notes

- **HITL labour in Africa** is materially cheaper than US benchmarks (UGX 4,000-8,000/hour fully loaded vs USD 30-60/hour in the US); the SLA-defence-HITL line is smaller in absolute USD terms but the classification rule is the same
- **Mobile-money refund-processing fees** (1-2.5%) — clearly COGS (cost of delivering the refund)
- **VAT classification of SLA credits** — Uganda VAT (18%), Kenya (16%), Nigeria (7.5%), South Africa (15%), Rwanda (18%) — SLA credits as transaction-price reductions reduce VAT-output proportionally; document the policy
- **Public-sector contracts in Africa** — SLA-defence cost may include in-country support staff cost (data-residency requirement); classify as COGS
- **Sovereign-AI compute cost premium** — in-region GPU is 1.5-3x US/EU; the cost is COGS regardless of where SLA defence happens
- **Insurance premium classification** — AI E&O coverage where available; G&A; document allocation between SLA-related and general
- **Local audit firm coaching** — provide the worked example; clarify the contra-revenue concept which mid-tier firms may not have seen before
