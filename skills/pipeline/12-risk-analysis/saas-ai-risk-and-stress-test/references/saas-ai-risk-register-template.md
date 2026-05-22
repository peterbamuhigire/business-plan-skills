---
source: Mersch ch. 11; Golding ch. 11; EU AI Act; NIST AI RMF; KE / NG / ZA / RW AI policy; engine synthesis
frameworks: [14-category AI risk register; likelihood × impact × owner × cadence; AI-incident classification; mitigation playbook]
skill: saas-ai-risk-and-stress-test
cross-reference: [meta-financial-stress-test, saas-ai-stress-test-scenarios, saas-ai-unit-economics-and-cogs, saas-ai-sustainability-and-ethics]
---

# SaaS AI Risk Register — Template

## 1. The 14 AI risk categories

For each: likelihood (H/M/L), impact (H/M/L), composite priority (1-5), mitigation, mitigation owner, mitigation status, review cadence.

| # | Risk | Description | Mitigation | Owner | Cadence |
|---|---|---|---|---|---|
| 1 | **AI cost spike** | Provider raises premium-model rates 50-200% | Multi-provider router; local-model fallback; aggressive cache | CFO + Head of AI | monthly |
| 2 | **Model deprecation** | Provider deprecates model on 6-12 month notice; forced migration | Multi-model router; eval-comparison ready; migration budget reserve | Head of AI / CTO | monthly |
| 3 | **Performance degradation** | New version of same model changes behaviour (regression) | Eval suite covering load-bearing flows; canary deploys; rollback path | Head of AI / QA | weekly |
| 4 | **Hallucination liability** | High-stakes feature produces wrong answer; customer harm + legal exposure | Eval coverage; human-in-loop for high-stakes; liability reserve; insurance | Head of AI + Head of Legal | monthly + sev-1 on incident |
| 5 | **Data-rights / training-data lawsuit** | Training-data provenance challenged in court | Provenance audit; consent + licensing; switch to documented-corpus models | Head of AI + Head of Legal | quarterly + per new data source |
| 6 | **Data sovereignty / residency** | AI provider stores customer data in non-compliant jurisdiction | Provider EULA review; in-region deployment options; data classification | Head of AI + Head of Compliance | quarterly + per new jurisdiction |
| 7 | **Vendor concentration** | >80% AI cost / capability on single provider | Multi-provider router; fallback evaluation; secondary contracts | CFO + CTO | quarterly |
| 8 | **Prompt injection / adversarial input** | User input compromises AI behaviour (jailbreak; data exfiltration) | Input sanitisation; output filtering; eval coverage; red-team | Head of AI / Security | monthly |
| 9 | **Eval-coverage gap** | Production AI behaviour not adequately covered by automated evals | Eval coverage roadmap; production sampling for human review | Head of AI / QA | monthly |
| 10 | **Bias / fairness regulatory exposure** | AI decisions show bias by gender / race / income / language / disability | Bias audit cadence; fairness metrics; remediation playbook | Head of AI / Ethics committee | semi-annual + on incident |
| 11 | **Foundation-model platform commoditisation** | Provider releases competing capability in your category | Vertical depth; workflow moat; data accrual; multi-provider strategy | CEO + Head of Strategy | quarterly |
| 12 | **GPU / compute scarcity** | Hosted-GPU availability constrained; capacity reduction or price hike | Multi-region; reservation contracts; non-GPU fallback design | CTO | quarterly |
| 13 | **FX shock on USD AI cost** | Local currency depreciates 10-30% against USD; AI cost % of revenue rises | FX corridor pricing; re-pricing triggers; partial USD revenue mix | CFO | monthly |
| 14 | **Regulatory / policy shift** | EU AI Act / NIST AI RMF / KE / NG / ZA / RW AI policy creates new requirements | Regulatory watch; compliance roadmap; legal counsel | Head of Legal / Compliance | quarterly + per new rule |

## 2. AI-incident classification

| Severity | Definition | Response time | Notification |
|---|---|---|---|
| **Sev-1** | Customer harm; safety event; regulatory-notifiable | Immediate (within hours) | CEO + Board + Customers affected + Regulator (per jurisdiction) |
| **Sev-2** | Customer-impacting performance / accuracy issue | Same day | Head of AI + affected customers |
| **Sev-3** | Internal-impact / near-miss | Within 48h | Head of AI + log only |

## 3. AI-incident runbook (one-page)

1. **Detect** — eval alert / customer report / sampling flag / monitoring alarm
2. **Triage** — severity classification; impact scoping; affected-customer list
3. **Contain** — disable feature / route to human / rollback model / restrict access
4. **Communicate** — customer comms within stated SLA; regulator notification per jurisdiction
5. **Diagnose** — root cause (model / data / prompt / integration / provider)
6. **Remediate** — fix root cause; deploy with canary; verify with extended eval
7. **Reserve drawdown** — if liability event, reserve allocation triggered
8. **Learn** — eval-suite extension to cover this failure mode; document in decision log
9. **Report** — post-mortem in monthly investor update; sev-1 in immediate board comms

## 4. Likelihood × Impact scoring

Each risk:

| Likelihood | Description | Probability |
|---|---|---|
| H | Probable within 12 months | >50% |
| M | Possible within 12 months | 15-50% |
| L | Unlikely within 12 months | <15% |

| Impact | Description |
|---|---|
| H | Existential / material customer harm / >20% revenue impact / regulatory penalty |
| M | Material but recoverable; 5-20% revenue / margin impact |
| L | Manageable; <5% impact |

| Composite priority | Mapping |
|---|---|
| 5 | H×H — Top priority; immediate mitigation required |
| 4 | H×M or M×H |
| 3 | M×M or H×L or L×H |
| 2 | M×L or L×M |
| 1 | L×L |

## 5. Mitigation maturity scale

For each mitigation: rate as

- **0 — Aspirational**: stated in plan; no action
- **1 — Designing**: design phase
- **2 — Building**: implementation underway
- **3 — Operating**: live and effective
- **4 — Audited**: external / internal audit confirms effectiveness

A risk register where most mitigations are at maturity 0-1 is not bankable. Investors will check.

## 6. Living-Plan Cadence

(Replicated from `saas-ai-risk-and-stress-test/SKILL.md`.)

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Risk register review | quarterly | CEO + Head of AI | new top-3 risk |
| Provider pricing | monthly | Head of AI / CTO | any change |
| Model-deprecation watch | monthly | Head of AI / CTO | provider notice |
| Eval coverage | monthly | Head of AI / QA | -5pp |
| Hallucination rate sampling | monthly | Head of AI | +1pp |
| Vendor concentration | quarterly | CFO + CTO | >80% on single provider |
| Regulatory watch | quarterly | Head of Legal / Compliance | new rule / enforcement |
| AI-incident log | continuous + monthly | Head of AI | any sev-1 |

## 7. Africa / Uganda specifics

| Risk extension | Africa-specific concern |
|---|---|
| Data sovereignty | KE DPA, NG NDPA, ZA POPIA, UG DPPA, RW Data Protection — cross-border AI compliance |
| FX shock | NGN, GHS, EGP, ZMW high-volatility; UGX, KES, TZS moderate |
| Sovereign-AI tender loss | Public-sector procurement increasingly favours in-country AI; anchor-tender churn risk |
| Local-language quality degradation | Foundation-model updates can degrade Swahili / Hausa / Yoruba / Luganda quality without notice |
| GPU scarcity in-region | Cassava / Liquid / Africa Data Centres capacity constrained; reservation contracts limited |
| Mobile-money payment failure on AI-metered billing | Payment-rail failure creates billing dispute, not AI failure; separately track |
| Regulatory uncertainty | KE, NG, ZA, RW, UG AI frameworks evolving; declare current posture, monitor changes |
