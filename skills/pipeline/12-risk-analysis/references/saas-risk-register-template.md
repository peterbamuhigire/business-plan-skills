---
source: Mersch (Hacking SaaS) ch. 11; Golding ch. 11; Cotton; engine COSO ERM + Bowtie heritage
frameworks: [SaaS-specific risk taxonomy; Risk register; Bowtie analysis; African context risks]
skill: 12-risk-analysis (and saas-risk-and-stress-test)
cross-reference: [meta-financial-stress-test, saas-bankability-and-investor-readiness, saas-unit-economics-and-cohort-model]
---

# SaaS Risk Register Template

The canonical SaaS / ICT risk taxonomy. Use to populate Section 12 (Risk Analysis) for any SaaS plan, plus the stress scenarios for `meta-financial-stress-test`.

## 1. Risk Categories (the SaaS taxonomy)

| Category | Examples |
|---|---|
| **Technical** | Outage; security breach; data loss; AI model deprecation; platform dependency |
| **Commercial** | Churn shock; key-customer concentration; pricing pressure; channel collapse |
| **Market** | Competitor entry; category commoditisation; macro slowdown; ICP shift |
| **Regulatory** | Data-residency law; sector regulation; tax change; fintech licensing |
| **Talent** | Founder departure; key-engineer loss; hiring failure; comp inflation |
| **Operational** | Payment-rail outage; FX shock; supply-chain (hardware); cloud-cost spike |
| **Financial** | Cash runway; funding-round failure; debt covenant breach |
| **Dependency** | Single cloud provider; single payment rail; single AI provider; single big customer |
| **Founder / Governance** | Founder conflict; cap-table dispute; board disagreement |
| **Reputational** | Public outage; customer-data scandal; legal dispute; PR crisis |

## 2. The Risk Register Format

```
RISK-ID: R-2026-Q2-014
TITLE: Single payment-rail dependency (M-Pesa)
CATEGORY: Dependency / Operational
PROBABILITY: Medium (3/5)
IMPACT: High (4/5) — 40% of customers, 60% of transactions on M-Pesa
INHERENT RISK: 12/25 (HIGH)

DESCRIPTION:
The company processes 60% of customer payments through Safaricom M-Pesa Daraja API. A
multi-day outage, API change, or regulatory restriction would block payments,
cause involuntary churn, and damage customer relationships.

TRIGGERS / EARLY SIGNALS:
- M-Pesa API error-rate >2% sustained
- Safaricom-CBK regulatory negotiations
- Press coverage of Daraja stability issues
- Customer-reported payment failures spiking

CONTROLS IN PLACE:
- 3-retry / 7-day dunning sequence (recovers 30-50% of payment failures)
- Daily payment-success-rate dashboard with alert <95%
- Secondary rail (Airtel Money + bank-direct-debit) for 25% of customers
- M-Pesa direct integration team relationship

ADDITIONAL MITIGATIONS PLANNED:
- Q2: Integrate Airtel Money as full secondary (target 25% volume)
- Q3: Add bank-direct-debit option for Tier 2+ customers (target 15% volume)
- Q4: Evaluate Cellulant aggregator for cross-rail redundancy

RESIDUAL RISK (after mitigations): 6/25 (MODERATE)

OWNER: CTO + CFO
REVIEW: Quarterly (next Q3 board meeting)
LAST UPDATED: 2026-04-15
```

## 3. Standard SaaS Risk Register (top 20 to consider)

| # | Risk | Cat | Likely Prob | Likely Impact | Default Mitigation |
|---|---|---|---|---|---|
| 1 | Cloud outage (AWS region) | Technical | 2/5 | 4/5 | Multi-AZ; backup region; status page |
| 2 | Security breach / data loss | Technical | 2/5 | 5/5 | SOC2; pen-testing; cyber insurance |
| 3 | Customer churn shock | Commercial | 3/5 | 5/5 | CS investment; cohort monitoring; save protocol |
| 4 | Key-customer concentration | Commercial | 3/5 | 5/5 | Diversification target; customer-cap policy |
| 5 | Competitor entry | Market | 4/5 | 3/5 | Moat investment; brand; switching costs |
| 6 | Data-residency regulation | Regulatory | 3/5 | 4/5 | Multi-region architecture; legal monitoring |
| 7 | Founder departure | Talent | 1/5 | 5/5 | Succession plan; key-person insurance; deep #2 |
| 8 | Key-engineer loss | Talent | 3/5 | 3/5 | Doc / pair / knowledge-management; retention plan |
| 9 | Payment-rail outage | Operational | 2/5 | 4/5 | Multi-rail; retry/dunning; dashboard |
| 10 | FX shock | Operational | 4/5 | 3/5 | FX-pass-through clauses; USD-priced tier |
| 11 | AI cost spike | Operational | 2/5 | 3/5 | Usage caps; cheaper models; cache; local fallback |
| 12 | Cash runway shortfall | Financial | 2/5 | 5/5 | Quarterly cash check; runway alarm <9 months |
| 13 | Funding-round failure | Financial | 3/5 | 4/5 | Bridge financing; revenue-financing options |
| 14 | Platform / API deprecation | Dependency | 2/5 | 4/5 | API versioning watch; fallback plans |
| 15 | Single cloud provider lock-in | Dependency | 4/5 | 2/5 | Cloud-agnostic architecture where feasible |
| 16 | Compliance failure (SOC2 / ISO / GDPR) | Regulatory | 2/5 | 4/5 | Compliance roadmap; consultancy engagement |
| 17 | Brand / reputational damage | Reputational | 2/5 | 3/5 | Crisis comms plan; PR retainer |
| 18 | Cap-table / board dispute | Governance | 1/5 | 5/5 | Clean docs; independent director; legal review |
| 19 | Pricing pressure (margin squeeze) | Commercial | 3/5 | 3/5 | Pricing experiments; expansion mechanic |
| 20 | Public-sector cycle dependency | Commercial | 3/5 | 3/5 | Private-sector diversification |

## 4. Africa-Specific Additions

Risks more salient in African contexts:

| # | Risk | Cat | Probability | Impact | Mitigation |
|---|---|---|---|---|---|
| A1 | Currency depreciation >15% | Operational | 4/5 | 4/5 | Local-currency contracts; USD-priced tier; hedging |
| A2 | Power outage / SLA failure | Operational | 4/5 | 3/5 | UPS / generator; SLA financial credits |
| A3 | Internet undersea cable cut | Operational | 2/5 | 3/5 | Multi-carrier; offline-first design |
| A4 | Central Bank circular changing fintech rules | Regulatory | 3/5 | 4/5 | Regulatory monitoring; legal counsel; sandbox engagement |
| A5 | Political instability / election cycle | Reputational | 2/5 | 4/5 | Scenario planning; geographic diversification |
| A6 | Donor-cycle revenue dependence | Commercial | 4/5 | 3/5 | Private-sector mix target |
| A7 | Local-language LLM quality | Technical | 3/5 | 2/5 | Multi-model; human-in-the-loop on critical paths |
| A8 | Tax / withholding-tax dispute | Regulatory | 3/5 | 3/5 | Local accountancy; quarterly tax filing |
| A9 | Mobile-money settlement delay | Operational | 3/5 | 3/5 | Cash buffer for settlement timing |
| A10 | Local-content / data-sovereignty | Regulatory | 3/5 | 4/5 | In-country data hosting plan |

## 5. The Stress-Test Scenarios (feeds `meta-financial-stress-test`)

The Top 5 stress scenarios every SaaS plan must model:

1. **Churn double** — what if monthly churn doubles? (Most common SaaS failure mode)
2. **NRR collapse** — what if expansion stops and contraction starts? (Indicates ICP / product issue)
3. **Top customer loss** — what if the #1 customer churns? (Concentration risk realised)
4. **FX 25% depreciation** — for African plans (FX-cost mismatch realised)
5. **Funding round failure** — what's the 12-month survival plan if next round doesn't close?

Each stress scenario in Section 12 should show: trigger, what happens financially, response plan, survival assessment.

## 6. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Top-5 risk dashboard | Monthly | CFO / COO |
| Full risk register review | Quarterly | CFO + COO + CEO |
| Mitigation status review | Monthly | Risk owners |
| Stress-test refresh | Quarterly | CFO |
| New-risk identification (post-mortem on incidents) | Per incident | CTO / COO / CFO |
| Annual risk-register full refresh | Annually | Board + Exec |

## 7. Risk-Adjusted Capital Planning

The plan should hold a capital cushion of:
- 6 months base operating cost (runway)
- + cost of mitigating the top 3 risks (cyber insurance, redundancy, hedging)
- + cost of recovering from the realised stress scenario

This is the "operational cushion" that DFI / patient-capital investors expect.
