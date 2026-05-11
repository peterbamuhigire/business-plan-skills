---
source: Walling, Cotton, van der Kooij; CIPS / Sales-enablement standards
frameworks: [ICP definition with 4 dimensions; Segmentation; Anti-ICP]
skill: 05-target-market
cross-reference: [saas-vertical-niche-selection, saas-gtm-motion-design, 04-market-analysis]
---

# SaaS ICP & Segmentation Template

## 1. The Four-Dimension ICP

The Ideal Customer Profile must be defined across four dimensions:

### A. Firmographic
- Industry / sub-vertical
- Company size (employees, revenue)
- Geography
- Stage / maturity
- Ownership type (private / public / cooperative / NGO / government)

### B. Technographic
- Existing tech stack (e.g., uses Stripe, M-Pesa, SAP, Salesforce, etc.)
- Maturity of digital adoption
- Engineering / IT capability
- Integration capability

### C. Behavioural
- Decision-making style (data-driven vs intuitive)
- Buying process (committee-based; founder-led; procurement-led)
- Past behaviour (have they bought similar tools? when? what failed?)
- Urgency / critical event sensitivity

### D. Psychographic
- Pain intensity (how badly does it hurt today?)
- Risk tolerance
- Growth ambition
- Cultural fit (innovation-friendly vs conservative)

## 2. The Anti-ICP (equally important)

Define who the product is NOT for. This is the discipline most plans miss.

Example (Ugandan dairy SaaS):
- **NOT** for cooperatives with <30 farmers (ARPU economics fail)
- **NOT** for cooperatives without M-Pesa or MoMo penetration (payment-rail mismatch)
- **NOT** for cooperatives that have formal Excel-based tooling already working
- **NOT** for cooperatives in remote areas with <60% 3G coverage

## 3. Segmentation Architecture

Most SaaS plans need 2-4 named segments:

| Segment | Sub-ICP | ACV | Volume | Motion |
|---|---|---|---|---|
| Segment A (core) | Cooperative 100-500 farmers, MoMo-mature | UGX 9M | 60 cust by Y3 | Solution sales |
| Segment B (growth) | Cooperative 500-2000 farmers, multi-location | UGX 25M | 25 cust by Y3 | Consultative |
| Segment C (anchor) | Cooperative unions / federations | UGX 50M+ | 5 cust by Y3 | Strategic / Provocative |

## 4. Persona Architecture (within ICP)

Define the named personas inside the ICP — each has different concerns, language, channels:

| Persona | Role | Concerns | Channel |
|---|---|---|---|
| **Champion** | Cooperative Secretary | Daily recordkeeping pain | WhatsApp, in-person |
| **Buyer** | Cooperative Chairperson | Governance, member benefit | In-person meetings, Phone |
| **Influencer** | MAAIF Extension Officer | Sector improvement | Training events, partnerships |
| **End User** | Field Officer / Treasurer | Ease of use | Mobile app, in-language |
| **Veto** | Cooperative Auditor | Compliance, audit trail | Documentation, formal demos |

## 5. ICP-Fit Scoring

For inbound leads / outbound targets, score against the ICP:

```
ICP-Fit Score = Σ (dimension match × weight)

Firmographic 30% × (industry match + size match + geo match) / 3
+ Technographic 25% × (stack maturity + integration capability) / 2
+ Behavioural 25% × (urgency + decision-style fit + history) / 3
+ Psychographic 20% × (pain intensity + cultural fit) / 2
= ICP-Fit Score (0-100)
```

Threshold: only AEs work leads scoring >60. <40 → don't pursue. 40-60 → marketing nurture.

## 6. Cohort Validation

Validate the ICP through cohort retention (per `saas-cohort-and-retention-model-template.md`):
- In-ICP cohort retention curve flattens earlier and higher
- Out-of-ICP cohort retention curve is steeper and lower
- This is the empirical proof of ICP correctness

If the in-ICP cohort underperforms the out-of-ICP cohort, the ICP definition is wrong.

## 7. Living-Plan Cadence

- Monthly: review which customers signed up and whether they're in-ICP
- Quarterly: refresh ICP based on win/loss data and cohort signals
- Annually: full ICP review at strategy refresh
- Trigger-replan: if a new "out-of-ICP" segment shows surprising retention, consider expanding ICP

## 8. Africa / Uganda Application Notes

- Persona language matters — "Chairperson" / "Secretary" / "Treasurer" map to cooperative structure familiar to Ugandan customers
- Cultural fit is meaningful — "innovation-friendly" cooperatives are often those with younger leadership or diaspora connections
- Anti-ICP for African plans often includes "remote / no-connectivity" segments unless designed for offline-first
- Multi-language ICP — define which language(s) the persona speaks; affects channel and content
- Public-sector vs private-sector is often a primary segmentation axis in African B2B SaaS
- NGO / donor-funded customer is a third bucket distinct from public and private; budget cycles differ
- ICP across multiple African countries usually requires per-country adjustment — "Kenya dairy cooperative" and "Uganda dairy cooperative" are not the same persona despite similar industry
