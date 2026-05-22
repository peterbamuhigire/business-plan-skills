---
name: saas-ai-risk-and-stress-test
description: Build the AI-specific risk register and stress-test scenarios for a SaaS plan — cost spike, model deprecation, performance drift, hallucination liability, data-rights / training-data lawsuits, data residency, vendor concentration, prompt injection, eval-coverage gaps, regulatory exposure (EU AI Act, KE / NG / ZA / RW AI policy), and FX on USD-denominated AI cost. Output a populated risk register with mitigation owners and a stress-test scenario set for `meta-financial-stress-test`. Use whenever AI is material to a SaaS plan.
---

# SaaS AI Risk & Stress Test Skill

## Overview

Generic risk registers cover technology, market, regulatory, talent, and financial risk. They miss the AI-specific failure modes that have become bankruptcy-level risks in 2026: model deprecation forcing migration, foundation-model platform commoditisation, hallucination-event liability in regulated verticals, data-rights / training-data lawsuits, prompt injection in agentic flows, and FX shock on USD-denominated AI COGS. This skill installs the AI risk discipline.

## Use When

- AI is material in a SaaS plan (>2% of ARR or load-bearing to product)
- Section 12 (Risk Analysis) is being built or reviewed for an AI plan
- `meta-financial-stress-test` is being run on an AI-feature-led plan
- Investor or DFI has asked for AI risk specifically
- Plan operates in a regulated vertical (health, finance, legal, public-sector)

## Do Not Use When

- AI is internal-efficiency only — use `12-risk-analysis` generic flow
- Plan is pre-architecture (risk register requires architecture)

## Required Inputs

- AI architecture (which providers, which models, which dependencies)
- Vertical / regulatory environment
- Customer-data sensitivity (PII, PHI, financial, child, biometric)
- Eval pipeline maturity (coverage %, sampling rate, governance)
- AI-incident history (if any)
- Geography (data residency, AI policy jurisdiction)
- Vendor concentration (% of AI cost / capability on single provider)

## Workflow

1. **Populate the AI risk register** per `references/saas-ai-risk-register-template.md` — 14 risk categories minimum, scored by likelihood × impact, with mitigation owner, mitigation status, review cadence.
2. **Map AI risks to plan sections** — cost risks → Section 10; legal / regulatory → 12; talent → 09; ops → 08; product → 03.
3. **Build the AI stress-test scenarios** per `references/saas-ai-stress-test-scenarios.md` — minimum 6 quantified scenarios that feed `meta-financial-stress-test`:
   - **AI cost spike** — provider doubles pricing
   - **Model deprecation** — forced migration in 6 months
   - **Hallucination event** — production incident triggers reserve drawdown + customer churn
   - **Data-rights lawsuit** — training-data provenance challenged
   - **GPU scarcity / sovereign-AI tender loss** — capacity reduction
   - **FX shock** — local currency depreciates 20% against USD
4. **Assess regulatory exposure** — map applicable regimes (EU AI Act if EU customers, NIST AI RMF if US enterprise, KE / NG / ZA / RW / UG AI frameworks if Africa-targeting). State current compliance posture and gap-to-compliance.
5. **Test eval coverage** — what % of production AI behaviour is covered by automated evals? Coverage <60% is high risk; coverage <30% is bankability-blocking for regulated verticals.
6. **Test vendor concentration** — if >80% of AI cost / capability is on one provider, declare as a risk and design a fallback path.
7. **Build the AI-incident runbook** — what happens when a sev-1 AI incident (wrong answer with customer harm) occurs? Reserve drawdown, customer comms, regulator notification, eval gap closure.
8. **Wire to living plan** — risk register quarterly review; eval coverage monthly; provider-pricing monthly; model-deprecation watch monthly; regulatory watch quarterly.

## Quality Bar

- Risk register has 14+ AI-specific risks; not stuffed with generic SaaS risks
- Each risk has likelihood × impact × mitigation owner × review cadence
- Stress scenarios are quantified, not narrative
- Regulatory exposure stated by jurisdiction with current compliance posture
- Eval coverage stated as a number (or "not yet measured" = honesty + roadmap)
- Vendor concentration stated as a percentage
- AI-incident runbook exists
- Cross-reference to Section 10 (financial stress test) is explicit

## Anti-Patterns

- "AI risk: cost spike. Mitigation: we'll switch models." — toy answer
- No quantified stress scenarios
- "We comply with regulations" — which? in which jurisdictions? as of what date?
- Eval coverage left undefined
- Vendor concentration ignored when single-provider
- Hallucination risk not addressed in regulated verticals
- AI-incident runbook missing

## Outputs

- Populated AI risk register (likelihood × impact × owner × cadence)
- AI stress-test scenarios (quantified for financial plan)
- Regulatory exposure map by jurisdiction
- Eval coverage statement
- Vendor concentration statement
- AI-incident runbook
- Cross-references to Sections 08, 09, 10, 14, 16

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Risk register review | quarterly | CEO + Head of AI | new top-3 risk |
| Provider pricing | monthly | Head of AI / CTO | any change |
| Model-deprecation watch | monthly | Head of AI / CTO | provider notice |
| Eval coverage | monthly | Head of AI / QA | -5pp from baseline |
| Hallucination rate sampling | monthly | Head of AI | +1pp absolute |
| Vendor concentration | quarterly | CFO + CTO | >80% on single provider |
| Regulatory watch | quarterly | Head of Legal / Compliance | new rule / enforcement |
| AI-incident log | continuous + monthly review | Head of AI | any sev-1 |

## References

- `references/saas-ai-risk-register-template.md` — full register with 14+ risk categories, mitigation playbook
- `references/saas-ai-stress-test-scenarios.md` — quantified scenarios for `meta-financial-stress-test`
- `skills/12-risk-analysis/SKILL.md` — generic risk-analysis flow
- `skills/meta-financial-stress-test/SKILL.md` — stress-test discipline; AI scenarios feed here
- `skills/14-ai-integration/SKILL.md` — AI integration context
- `book-extractions/mersch-hacking-saas-extraction.md` — SaaS CFO risk discipline
- `book-extractions/tod-building-multi-tenant-saas-architectures-extraction.md` — multi-tenant architecture risks

## Africa / Uganda Application Notes

- **Data residency risk** is a primary risk in Africa: KE DPA, NG NDPA 2023, ZA POPIA, UG DPPA, RW Data Protection Law all create cross-border data restrictions. Foundation-model APIs storing data outside compliant jurisdictions is a real exposure.
- **FX risk on USD AI cost** is acute when local currency is volatile (NGN, EGP, GHS, ZMW). Hedging is often not feasible; pricing headroom is the mitigation.
- **Regulatory uncertainty** — KE National AI Strategy, NG NITDA AI roadmap, ZA AI policy framework, RW AI policy 2023, AU continental AI strategy all evolving. Plans should declare current posture, not promise future compliance.
- **Sovereign-AI tender risk** — public-sector procurement increasingly favouring local AI; loss of a single anchor tender can be a stress event.
- **Local-language AI quality risk** — if product depends on Swahili / Hausa / Luganda / Yoruba inference quality, model changes can degrade quality without warning; monitoring required.
- **Payment-rail-on-AI-customer risk** — when AI cost is metered, mobile-money payment failures create cash-flow risk distinct from AI cost risk.
- **GPU access risk** — Cassava / Africa Data Centres / Liquid GPU capacity is constrained; long-term reservations are limited; this is a capacity-planning risk for AI-platform plans.
