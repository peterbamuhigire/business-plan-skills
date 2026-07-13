---
name: saas-ai-talent-strategy
description: Use when producing or reviewing the saas ai talent strategy component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS AI Talent Strategy Skill

## Overview

Generic management-team plans say "we'll hire AI engineers." AI-aware investors and DFIs require specificity: which AI roles, at which ARR milestone, sourced from where, at what comp, with what tenure expectation, with what training-and-retention plan. This skill installs the discipline.

## Use When

- Section 09 of an AI-feature-led plan is being built
- Hiring plan is being designed
- A funder has asked specifically how AI capability will be built
- Plan is targeting public-sector / regulated-vertical AI procurement where local-talent requirements apply
- Plan needs to defend AI moat with team-as-moat evidence

## Do Not Use When

- AI is internal-efficiency only — use `09-management-team` standard
- Plan has no AI capability requirement

## Required Inputs

- AI roadmap with milestones (`saas-ai-product-strategy-and-roadmap`)
- ARR plan
- Geography of operation
- Comp budget envelope
- Current team composition

## Workflow

1. **Map AI roles to ARR milestones** per `references/saas-ai-talent-and-org-design-template.md`:
   - **Pre-PMF**: founding ML / applied-ML engineer (often founder); AI-aware product person
   - **$0-$1M**: + RAG engineer; + AI product manager
   - **$1-$5M**: + MLOps / AI infra; + eval / QA lead; + domain-expert-trainer
   - **$5-$20M**: + AI safety / governance lead; + AI policy / compliance; + 2-4 ML engineers
   - **$20M+**: Head of AI / VP AI; + research-engineering function (if proprietary models)
2. **Decide outsource-to-build-to-buy** for each role / function:
   - **Outsource**: fractional CTO / fractional Head of AI for pre-seed; specialist consultancies for one-off fine-tuning
   - **Build**: domain-aware roles (RAG engineers, AI PMs, eval leads) that learn the business
   - **Buy**: senior leadership (Head of AI) typically bought at series A or later; comp + equity matter
3. **Source from the African AI talent map** per `references/africa-ai-talent-map.md`:
   - **Lelapa AI** (Johannesburg) — local-language AI research / startup
   - **Masakhane** — pan-African NLP research network
   - **AIMS network** (South Africa, Senegal, Cameroon, Ghana, Tanzania, Rwanda) — Master's-level AI
   - **Carnegie Mellon Africa** (Rwanda) — top-tier AI / ML talent
   - **ALU AI track** (Rwanda / Mauritius)
   - **Andela AI talent pool**
   - **Deep Learning Indaba** alumni network — annual continental AI conference
   - **Black in AI Africa** chapter networks
   - **InstaDeep** alumni network (BioNTech subsidiary; African AI precedent)
   - **University CS departments** — Makerere AI Lab, Nairobi, Witwatersrand, Cape Town, Cairo, Pretoria, Cape Town, ABU Zaria, Lagos, Addis Ababa, Khartoum
4. **Set comp benchmarks** in local + USD:
   - Junior ML engineer: $1,500-3,500/mo (varies by country per Africa context Section 6)
   - Mid ML engineer: $3,000-5,500/mo
   - Senior ML engineer: $5,000-9,000/mo (in-country); $8,000-15,000/mo (remote-international)
   - Head of AI: $8,000-15,000/mo + equity
5. **Design the retention strategy** — equity ladder, technical leadership track, conference / paper / publishing budget, eval-and-research time, sabbatical policy. AI talent in Africa is recruited aggressively by US/EU companies; retention is a real problem.
6. **Design the training / upskilling plan** — internal AI literacy for non-AI roles; external training budgets; partnerships with AIMS, ALU, Lelapa.
7. **Map the diversity / inclusion targets** — gender, country, language, vertical-experience. DFIs require this; AI ethics requires this.
8. **Build the contingency plan** — what if Head of AI leaves? key-person dependency mitigation. (Trigger-replan event in `meta-living-plan-governance`.)
9. **Wire to risk** — talent risk in `saas-ai-risk-and-stress-test`.
10. **Wire to living plan** — hiring plan monthly review, retention quarterly, AI talent landscape semi-annual.

## Quality Bar

- AI roles mapped to ARR milestones with explicit titles and seniority
- Outsource-to-build-to-buy decision per role
- Sourcing strategy specifies African talent pool sources, not generic
- Comp benchmarks in local + USD
- Retention strategy explicit
- Training / upskilling plan
- Diversity / inclusion targets
- Key-person contingency
- Cross-reference to risk register

## Anti-Patterns

- "We'll hire AI talent" without role specification
- Generic LinkedIn-sourcing assumption when most African senior AI talent isn't on the public market
- Comp pegged to local SMB benchmarks (AI talent is paid at international tier)
- No retention plan when international competition is intense
- Diversity stated as aspiration without target
- Key AI personnel undefined / unprotected (no NDA, no IP assignment, no non-compete)

## Outputs

- AI org chart by ARR milestone
- Hiring plan with role × milestone × source × comp × seniority
- Sourcing strategy with named talent pools
- Retention plan
- Training / upskilling plan
- Diversity / inclusion targets
- Key-person contingency
- Cross-references to risk and operations

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Hiring plan status | monthly | Head of People + CTO | slip >30 days |
| AI team attrition | quarterly | Head of People | >20% annualised |
| Comp benchmark review | semi-annual | Head of People + CFO | market shift >15% |
| Retention plan effectiveness | quarterly | Head of People | departure of senior AI |
| Training / upskilling spend | quarterly | Head of People | underspend or no progress |
| AI talent landscape | semi-annual | CTO | new talent pool emerges or shrinks |
| Diversity targets | quarterly | Head of People | regression from target |

## References

- `references/saas-ai-talent-and-org-design-template.md` — role × ARR milestone matrix + comp + sourcing
- `references/africa-ai-talent-map.md` — sourcing detail per network
- `skills/09-management-team/SKILL.md` — generic management-team flow
- `skills/saas-sales-org-design-and-capacity-planning/SKILL.md` — GTM team plan (sister)
- `country-context/africa-regional/africa-ict-saas-market-context.md` — Section 6 talent context

## Africa / Uganda Application Notes

- **Remote-international competition** — top African ML talent earns US/EU comp working remotely; plan equity-and-mission as differentiators or accept higher cash comp.
- **Distributed-team-across-Africa** is now feasible (Nairobi, Lagos, Cape Town, Kigali, Cairo, Accra, Kampala) — design for it from day one if AI capability is load-bearing.
- **Local-context as moat** — hiring AI talent who understand cooperative governance, mobile-money rails, public-sector procurement is itself a moat that offshore talent cannot replicate quickly.
- **DFI requirements** often include local-talent-building, gender targets, training commitments — embed in talent plan from start.
- **Sovereign-AI tender requirements** often include local-citizen-engineer headcount minima — plan for compliance.
- **Visa / mobility constraints** between African countries can affect distributed-team viability; plan for it.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Role requirements, verified biographies, workload, organisation design, compensation assumptions, and hiring evidence for saas ai talent strategy | Founders, HR records, approved payroll model, and reference evidence | Yes | If absent, a biography, role need, workload, or pay assumption is unavailable, mark it unverified and keep the role or hire conditional. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Management-team section and staged organisation/hiring plan | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai talent strategy exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai talent strategy release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Credential trace, accountability map, hiring trigger, and payroll reconciliation | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai talent strategy decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai talent strategy review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai talent strategy, the controlling focus is AI product, data, ML, evaluation, governance, and scarce-talent sourcing choices. This skill may analyse roles and draft people plans using authorised records; it may not verify credentials by assertion, disclose sensitive HR data, hire, discipline, or set compensation without authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai talent strategy, loss of evidence about AI product, data, ML, evaluation, governance, and scarce-talent sourcing choices activates degraded mode. If the controlling saas ai talent strategy evidence is unavailable, the same boundary applies. When a biography, role need, workload, or pay assumption is unavailable, mark it unverified and keep the role or hire conditional. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai talent strategy, a named leader lacks evidenced capacity for a critical accountability| state the gap, assign interim ownership, and define the hire, adviser, or development trigger | Founder-centric organisation claims hide execution and governance gaps |
| For saas ai talent strategy, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai talent strategy decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai talent strategy, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete management-team section and staged organisation/hiring plan, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai talent strategy decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect role requirements, verified biographies, workload, organisation design, compensation assumptions, and hiring evidence and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce management-team section and staged organisation/hiring plan with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Management-team section and staged organisation/hiring plan must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Credential trace, accountability map, hiring trigger, and payroll reconciliation must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai talent strategy, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai talent strategy, treating an unavailable role requirements, verified biographies, workload, organisation design, compensation assumptions, and hiring evidence as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing management-team section and staged organisation/hiring plan that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A startup plans three data scientists before it has usable training data. Stage data engineering and product validation first, then trigger specialist ML hiring from an evidenced backlog.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai talent strategy; no local deep-dive reference is declared.
- For saas ai talent strategy claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
