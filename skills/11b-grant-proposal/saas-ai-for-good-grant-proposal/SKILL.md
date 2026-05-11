---
name: saas-ai-for-good-grant-proposal
description: Build an AI-for-good grant proposal — Mozilla African Innovation Mradi, GSMA AI for Impact, IDRC AI4D, Google.org AI for Social Good, Microsoft AI for Good, Lacuna Fund (training-data grants), Patrick J. McGovern Foundation AI, Gates AI envelopes. Builds theory-of-change for AI interventions, AI ethics + impact measurement, training-data provenance, community-benefit articulation. Use when the AI-SaaS plan is grant-funded or grant-co-funded.
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
