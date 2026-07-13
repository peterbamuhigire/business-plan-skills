---
name: saas-ai-risk-and-stress-test
description: Use when producing or reviewing the saas ai risk and stress test component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Business model, assumptions, contracts, operating controls, risk evidence, scenario variables, and risk appetite for saas ai risk and stress test | All pipeline sections, client records, current research, and governance owners | Yes | If absent, probability, impact, control effectiveness, or scenario data is unavailable, mark the risk unassessed and use a bounded sensitivity rather than a false score. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai risk and stress test exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai risk and stress test release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Risk-source trace, scenario calculation, control-owner confirmation, and residual-risk decision | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai risk and stress test decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai risk and stress test review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai risk and stress test, the controlling focus is model degradation, hallucination, data rights, vendor concentration, inference cost, and scenario stress. This skill may inspect evidence and challenge assumptions in read-only mode; it may not change controls, accept risk for management, trigger contingency spending, or certify compliance. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai risk and stress test, loss of evidence about model degradation, hallucination, data rights, vendor concentration, inference cost, and scenario stress activates degraded mode. If the controlling saas ai risk and stress test evidence is unavailable, the same boundary applies. When probability, impact, control effectiveness, or scenario data is unavailable, mark the risk unassessed and use a bounded sensitivity rather than a false score. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai risk and stress test, a mitigation has no owner, trigger, budget, or evidence of effectiveness| treat it as planned rather than operating, raise residual risk, and define the test or owner needed | Decorative risk registers understate exposure and create false assurance |
| For saas ai risk and stress test, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai risk and stress test decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai risk and stress test, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai risk and stress test decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect business model, assumptions, contracts, operating controls, risk evidence, scenario variables, and risk appetite and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Risk-source trace, scenario calculation, control-owner confirmation, and residual-risk decision must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai risk and stress test, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai risk and stress test, treating an unavailable business model, assumptions, contracts, operating controls, risk evidence, scenario variables, and risk appetite as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A model update reduces accuracy for Luganda queries while the vendor price rises. Stress customer churn, remediation cost, and fallback routing rather than treating accuracy and cost as separate risks.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai risk and stress test; no local deep-dive reference is declared.
- For saas ai risk and stress test claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
