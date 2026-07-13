---
name: saas-ai-for-good-grant-proposal
description: Use when producing or reviewing the saas ai for good grant proposal component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS AI-for-Good Grant Proposal Skill

## Overview

AI-for-good grants follow different rubrics than commercial AI funding. Grantmakers weight theory-of-change, training-data provenance, community benefit, ethics, explainability, local-capacity-building, and impact measurement higher than ARR growth and Rule of 40. This skill builds the proposal that wins both substance and rubric.

## Use When

- AI-SaaS plan is grant-funded or grant-co-funded
- Africa-context AI plan is targeting AI-for-good envelopes
- Training-data acquisition or local-language coverage needs Lacuna Fund / Mozilla / IDRC-class funding
- AI ethics / governance / fairness build-out needs grant capital
- Public-sector AI implementation needs donor co-funding

## Do Not Use When

- Plan is pure commercial AI fundraise — use `saas-ai-funding-stage-playbook`
- Plan has no AI-for-good thesis (don't reverse-engineer one)

## Required Inputs

- Theory-of-change (problem → intervention → outputs → outcomes → impact)
- AI architecture and intended use
- Training-data provenance plan
- Community-benefit articulation
- Impact KPIs
- Ethics / governance / explainability plan
- Local-capacity-building commitments
- Co-funding sources and budget

## Workflow

1. **Build the theory-of-change** for the AI intervention per `references/saas-ai-grant-proposal-template.md`:
   - Problem statement (with quantified evidence)
   - Why AI specifically (not just any tech) addresses the problem
   - Inputs (data, compute, talent, partnerships)
   - Activities (build / train / deploy / measure)
   - Outputs (working product; users reached; data accrued; capacity built)
   - Outcomes (behavioural / institutional change at user / sector level)
   - Impact (long-term societal change, alignment with SDGs)
2. **State training-data provenance** — where does training data come from? consent? compensation? curation? bias-mitigation? This is the #1 question Lacuna Fund / Mozilla / IDRC AI4D ask.
3. **State community benefit** — who benefits, how is benefit measured, how is community consulted / governed, how is data sovereignty respected.
4. **State ethics and explainability commitments** — bias audits, fairness metrics, transparency to users, redress mechanisms, training data documentation (datasheets / model cards).
5. **State local-capacity-building** — local AI engineers trained, local university partnerships, open-source contributions, local-language coverage, knowledge transfer.
6. **Build impact KPIs** — for AI interventions, distinguish:
   - **Reach KPIs** (users served, languages covered)
   - **Outcome KPIs** (specific behavioural / institutional change)
   - **Impact KPIs** (long-term societal change linked to SDG targets)
   - **Equity KPIs** (gender, geography, income, disability, language)
7. **Map to grantmaker** per `references/ai-for-good-grantmaker-map.md`:
   - **Lacuna Fund** — training-data grants for ML in low-resource languages
   - **Mozilla African Innovation Mradi** — community-benefit AI in Africa
   - **GSMA AI for Impact** — mobile-tech-enabled AI for development
   - **IDRC AI4D Africa** — AI for Development continental programme
   - **Google.org AI for Social Good**
   - **Microsoft AI for Good**
   - **Patrick J. McGovern Foundation AI** — AI for social good globally
   - **Bill & Melinda Gates AI envelopes** — health, agriculture, gender
   - **Wellcome Trust** — health AI in LMICs
   - **Hewlett Foundation** — democracy / institutions AI
   - **Omidyar Network** — responsible technology
   - **Ford Foundation** — equitable technology
8. **Build the budget** in grantmaker-required format — line items aligned with the call (often: personnel, equipment, training, M&E, indirect cost cap).
9. **Build the M&E plan** — baseline, midline, endline; data sources; verification; reporting cadence.
10. **Build the ethics-and-governance statement** — institutional review (where applicable), data protection compliance, AI-incident protocol.
11. **Build the sustainability statement** — how the AI capability persists after grant period (commercial revenue path; institutional adoption; open-source community; partnership with public-sector).
12. **Wire to commercial plan** — explain how grant + commercial co-exist; avoid grant-dependency narrative.

## Quality Bar

- Theory-of-change explicit and quantified
- Training-data provenance honest and detailed
- Ethics commitments specific (not "we will be ethical")
- Local-capacity-building specific (numbers, partners, mechanisms)
- Impact KPIs include equity dimensions
- Budget format matches grantmaker requirements
- M&E plan operational, not aspirational
- Sustainability beyond grant period addressed
- Avoids grant-dependency narrative
- Aligns with named SDGs where required

## Anti-Patterns

- "AI will improve outcomes" without theory-of-change
- Training-data provenance left vague
- "We will be ethical" without specific commitments
- Impact KPIs all reach (no outcome / impact)
- Budget doesn't match grantmaker format
- M&E as afterthought
- "Sustainability via Series A" — circular logic for grant
- Generic grant proposal sent to multiple funders

## Outputs

- Full grant proposal in grantmaker format
- Theory-of-change diagram + narrative
- Training-data provenance statement
- Ethics / governance / explainability statement
- Local-capacity-building plan
- Impact KPI framework
- Budget (line-item)
- M&E plan
- Sustainability statement
- Cross-references to commercial plan sections

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Grant pipeline | monthly | Grants lead + CEO | major call closes |
| Live-grant M&E reporting | per grant cycle | Programme manager | reporting deadline |
| Impact KPI baseline / midline / endline | per grant plan | M&E lead | data quality issue |
| Training-data provenance audit | quarterly | Head of AI / Data | new data source |
| Grant-funded capacity-building outputs | quarterly | Programme manager | output slip |
| Sustainability check-in | quarterly | CEO + CFO + Grants | grant tail in <6 months |

## References

- `references/saas-ai-grant-proposal-template.md` — full template with sections + worked example
- `references/ai-for-good-grantmaker-map.md` — named grantmakers + thesis + rubric notes
- `skills/11b-grant-proposal/SKILL.md` — generic grant flow
- `skills/meta-sustainability/SKILL.md` — impact framework + IFC PS
- `skills/meta-monitoring-evaluation/SKILL.md` — M&E discipline
- `country-context/africa-regional/africa-ict-saas-market-context.md` — Section 7 grant ecosystem

## Africa / Uganda Application Notes

- **Mozilla African Innovation Mradi** is the most accessible AI-for-good vehicle for early-stage African AI startups; align with their community-benefit framing.
- **Lacuna Fund** is the canonical funder for African-language training datasets; co-author with Masakhane / Lelapa / Awarri where relevant.
- **GSMA AI for Impact** weights mobile-channel AI heavily — design around mobile / USSD / WhatsApp.
- **IDRC AI4D** prioritises research-and-policy; commercial-only plans struggle in their rubric.
- **DFI AI envelopes** (IFC, AfDB) work on longer cycles (12-18 months) and want commercial-plus-impact blends.
- **Sovereign-AI public-sector co-funding** is emerging in KE, NG, ZA, RW — track procurement portals.
- **Reporting language and compliance** matters — DFI-funded grants require ESG / IFC PS alignment, gender-disaggregated reporting, and rigorous M&E. Build the discipline early.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Funder call, eligibility rules, problem evidence, theory of change, work plan, budget, safeguards, and applicant credentials for saas ai for good grant proposal | Official funder documents, client evidence, implementing partners, and finance model | Yes | If absent, the official call, eligibility rule, beneficiary baseline, partner commitment, or budget basis is unavailable, mark the proposal blocked at that requirement and return the exact evidence request. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI-for-good grant proposal with funder compliance, additionality, responsible-AI safeguards, logframe, budget, and evidence plan | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai for good grant proposal exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai for good grant proposal release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Requirement matrix, claim-source register, results-chain test, budget-to-activity reconciliation, and partner proof | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai for good grant proposal decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai for good grant proposal review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai for good grant proposal, the controlling focus is AI-for-good additionality, beneficiary safeguards, evidence plan, responsible AI controls, and funder compliance. This skill may analyse the call and draft application material; it may not submit, sign declarations, invent beneficiaries or co-funding, contact the funder, or commit partners without explicit authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai for good grant proposal, loss of evidence about AI-for-good additionality, beneficiary safeguards, evidence plan, responsible AI controls, and funder compliance activates degraded mode. If the controlling saas ai for good grant proposal evidence is unavailable, the same boundary applies. When the official call, eligibility rule, beneficiary baseline, partner commitment, or budget basis is unavailable, mark the proposal blocked at that requirement and return the exact evidence request. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai for good grant proposal, a desirable activity does not contribute to a stated outcome or cannot be measured within the grant period| remove or redesign it and repair the results chain and budget | A fluent application can still fail eligibility, credibility, safeguarding, or value-for-money review |
| For saas ai for good grant proposal, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai for good grant proposal decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai for good grant proposal, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete ai-for-good grant proposal with funder compliance, additionality, responsible-ai safeguards, logframe, budget, and evidence plan, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai for good grant proposal decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect funder call, eligibility rules, problem evidence, theory of change, work plan, budget, safeguards, and applicant credentials and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce ai-for-good grant proposal with funder compliance, additionality, responsible-ai safeguards, logframe, budget, and evidence plan with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- AI-for-good grant proposal with funder compliance, additionality, responsible-AI safeguards, logframe, budget, and evidence plan must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Requirement matrix, claim-source register, results-chain test, budget-to-activity reconciliation, and partner proof must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai for good grant proposal, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai for good grant proposal, treating an unavailable funder call, eligibility rules, problem evidence, theory of change, work plan, budget, safeguards, and applicant credentials as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing ai-for-good grant proposal with funder compliance, additionality, responsible-ai safeguards, logframe, budget, and evidence plan that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An AI health triage grant promises rural reach but lacks consent, referral, bias, and clinical-oversight controls. Hold deployment funding, add the safeguard workstream and evidence gates, and retain only non-clinical pilot outcomes until approval.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai for good grant proposal; no local deep-dive reference is declared.
- For saas ai for good grant proposal claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
