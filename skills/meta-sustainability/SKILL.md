---
name: meta-sustainability
description: Use when use at the start of an engagement to identify sustainability design requirements. Use a sector specialist for a detailed impact study.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# meta-sustainability

## Overview

Use this meta-skill to pre-screen, integrate, and audit sustainability across the suite. It acts as the sustainability gate before drafting, during drafting, and before final sign-off so environmental and social issues are handled systematically.

## Use When

- Use at the start of an engagement to identify sustainability design requirements.
- Use during drafting when sustainability issues affect products, operations, risk, or funding.
- Use before finalisation to audit whether the plan meets sustainability and funder-readiness expectations.

## Do Not Use When

- Do not use as a cosmetic ESG overlay detached from the business model.
- Do not replace the dedicated sustainability section when that artifact is required.
- Do not assume all sectors face the same sustainability issues.


- Route to the relevant sector specialist instead when a detailed impact study or certification is required.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Sustainability brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Business model, sector, geography, and operating footprint
- Funder, lender, or compliance context affecting sustainability requirements
- Available information on environmental, labour, community, and governance issues
- Any related section drafts that need sustainability integration or audit

## Workflow

1. Determine whether the task is pre-screening, in-draft integration, or final audit.
2. Identify the business's most material sustainability issues.
3. Map those issues to the relevant sections, controls, and funding requirements.
4. Check whether the plan's claims are measurable, owned, and operationally realistic.
5. Reconcile sustainability logic with risk, operations, finance, and implementation.
6. Flag any missing controls, evidence, or funder-readiness gaps.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the ESG screening and action register and that the decision concerns which impacts need mitigation, specialist study, or escalation.
- **Stop condition:** halt the affected conclusion if required evidence is missing (site, sector, labour, community, governance, and funder requirements) or if the work could lead to this identified risk: calling a plan sustainable before material impacts are assessed.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Sustainability work is materiality-led, not boilerplate-led.
- Findings translate into design, control, or funding implications.
- Environmental and social claims are evidence-aware and measurable.
- The output improves both resilience and fundability.

## Anti-Patterns

- Applying the same sustainability checklist to every sector.
- Writing ESG language with no operational consequence.
- Ignoring labour, community, or adaptation issues while focusing only on optics.
- Letting sustainability commitments drift away from budget and ownership.
- Treating a generic sustainability template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta sustainability. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Sustainability deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A sustainability pre-screen, integration map, or audit result
- Materiality-driven findings and section-level implications
- Any unresolved funder-readiness or control gaps


Mandatory sustainability pre-screen, integration guide, and audit tool for all business plans in this suite. Run this skill at the start of every engagement (Mode A), reference it during drafting (Mode B), and use it as a final gate before submission (Mode C).

---

## Why Sustainability Is Mandatory

Business plans that ignore environmental and social sustainability face three concrete risks: **regulatory risk** (NEMA permit rejections, UDB compliance requirements), **reputational risk** (community opposition, media exposure, customer attrition), and **lender/investor rejection** (IFC Performance Standards, UDB Environmental and Social Policy, aBi Finance eligibility criteria, UNCDF requirements all mandate environmental and social due diligence).

Uganda contributes less than 0.1% of global GHG emissions. The correct climate framing for Ugandan businesses is **ADAPTATION**  building resilience to rainfall variability, prolonged drought, flooding, and temperature shifts  rather than mitigation. Businesses that embed climate adaptation into their operating model are more resilient, not merely more responsible.

Sustainability is a competitive advantage, not a cost centre: eco-efficient operations carry lower resource bills; strong community relations provide a licence to operate; green credentials unlock concessional finance. Frontrunner companies that embed sustainability into core strategy outperform industry peers by 1625% on operational eco-efficiency (Leleux & van der Kaaij, 2019). Every business plan in this suite must treat sustainability as a design standard from Day 1.

---

## Three Operating Modes

### Mode A: Pre-Screen Gate
Run **before writing the business plan**  ideally at the `00-plan-assembly` stage. Identifies sustainability design requirements so they are built in from the outset, not retrofitted. Produces a sector-specific sustainability brief for the plan author.

### Mode B: Section Integration
Embedded sustainability guidance appears in sections **03** (Products & Services), **07** (Marketing & Sales), **08** (Operations), **12** (Risk Analysis), and **14** (AI Integration) during the drafting process. Each of those SKILL.md files carries sustainability checkpoints. When Mode B is active, cross-reference the relevant materialities identified in Mode A.

### Mode C: Sustainability Audit
Run **after all sections are drafted**, before final assembly. Generates the Sustainability Readiness Score (SRS) and a section-by-section compliance table. The SRS determines the appropriate submission pathway (commercial bank, DFI, or return to design).

---

## Sustainability Readiness Score (SRS)

Five dimensions, each scored **02**:
- **0** = Absent or not considered
- **1** = Partially addressed  mentioned but lacking specifics, budget, or accountability
- **2** = Fully integrated  substantive, budgeted, measurable, and assigned to a responsible person

| Dimension | Weight | Score (02) | Weighted Score |
|---|---|---|---|
| Environmental | 25% | | |
| Social | 25% | | |
| Strategy | 20% | | |
| Circular Economy | 15% | | |
| Governance | 15% | | |
| **TOTAL** | **100%** | | **/2.0** |

### Dimension Definitions

**Environmental (25%)**
- Waste management plan documented with disposal method and responsible party
- Water and energy efficiency measures specified (targets, not intentions)
- Emissions and pollution controls in place (air, water, soil  sector-dependent)
- NEMA compliance pathway confirmed: category A, B, or C; EIA certificate if required
- Climate adaptation measures identified and budgeted

**Social (25%)**
- Employment conditions compliant with Uganda Employment Act 2006 and NSSF Act
- Community impact assessment conducted or scoped
- Gender inclusion considered: women's employment, women customers, gender pay equity
- Land and resettlement plan in place if the business involves land acquisition or community displacement
- Customer and product safety standards met (UNBS, NDA, or sector equivalent)

**Strategy (20%)**
- Sustainability embedded in the mission or vision statement  not as a footnote
- 23 SDGs identified as most relevant; specific targets articulated
- Materiality identified: the key sustainability issue for this specific sector and business model
- Sustainability positions the business distinctively  not a generic CSR statement

**Circular Economy (15%)**
- Waste reduction or reuse mechanisms designed into operations
- By-product valorisation considered (e.g., manure  biogas; husks  briquettes)
- Packaging reduction or switch to biodegradable materials where applicable
- Supply chain sustainability assessed (primary supplier practices)

**Governance (15%)**
- Named individual (director, manager, or owner) accountable for sustainability performance
- Sustainability KPIs included in the monitoring and evaluation plan
- Stakeholder engagement process documented (who, how often, what is reported)
- Grievance mechanism in place (even a simple channel for community or worker complaints)

### Scoring Thresholds

| Score | Meaning | Submission Pathway |
|---|---|---|
|  1.6 / 2.0 (= 8.0/10) | High sustainability integration | DFI / impact investor submission ready |
|  1.2 / 2.0 (= 6.0/10) | Adequate sustainability integration | Commercial bank submission ready |
| < 1.2 / 2.0 | Sustainability gaps too significant | Return to design  address gaps before submission |

---

## Sector-Specific Sustainability Materialities  Uganda

| Sector | Primary Environmental Materiality | Primary Social Materiality | Key SDGs |
|---|---|---|---|
| Agriculture / Food processing | Water use, pesticide runoff, post-harvest waste, soil degradation | Smallholder farmer livelihoods, child labour avoidance, seasonal worker rights | SDG 2, 6 |
| Dairy | Manure management, methane, water abstraction | Animal welfare standards, milk handler health and safety | SDG 2, 13 |
| Poultry | Manure and ammonia, water use, feed waste | Worker biosafety, community odour impacts | SDG 2 |
| Construction | Soil erosion, dust, construction waste, NEMA EIA trigger | Worker safety (scaffolding, PPE), community disruption, land rights | SDG 11 |
| Manufacturing / Agri-processing | Effluent discharge, energy intensity, chemical waste storage | Worker safety, noise pollution, preference for local hiring | SDG 9 |
| Hospitality / Tourism | Water and energy use, solid waste, biodiversity near sites | Community benefit-sharing, local food sourcing, cultural respect | SDG 8, 12 |
| Healthcare | Medical waste segregation and disposal, chemical handling | Patient safety, equitable access, staff health | SDG 3 |
| Transport / Logistics | Fuel emissions, vehicle maintenance standards, tyre disposal | Driver safety, community road safety, working hours compliance | SDG 11 |
| Retail / Trade | Packaging waste, food waste, cold-chain energy | Fair supplier treatment, customer product safety, labelling | SDG 12 |
| Technology / Digital | E-waste, energy consumption (servers, devices) | Digital inclusion, data privacy, algorithmic fairness | SDG 9, 10 |
| Education / Training | Facility energy and water use | Safe learning environment, inclusivity (gender, disability, income) | SDG 4, 10 |
| Financial Services | Paper use, office energy | Financial inclusion, responsible lending, consumer protection | SDG 1, 10 |

---

## Mode A: Pre-Screen Gate

Run this 12-item checklist **before drafting begins**. Record answers in the plan brief.

1. **Top environmental risks**: State the two most significant environmental risks for this sector and business location (e.g., water scarcity, effluent runoff, deforestation).

2. **Top social risks**: State the two most significant social risks (e.g., worker safety, community displacement, gender-based exclusion, child labour in supply chain).

3. **NEMA category**: Confirm whether the business falls under NEMA Category A (full EIA required), Category B (environmental audit required), or Category C (self-certification sufficient). See the National Environment Act 2019 thresholds.

4. **EIA certificate requirement**: Does this business require an Environmental Impact Assessment certificate before construction or commencement of operations? If yes, build EIA timeline and cost into Section 13 (Implementation) and Section 10 (Financial Projections).

5. **Water and effluent**: Does the business abstract surface or groundwater, or discharge any effluent? If yes, a National Water and Sewerage Corporation or NES permit is required. Note abstraction volumes and discharge standards.

6. **Land acquisition or resettlement**: Does the business require land acquisition, lease of community land, or displacement of current occupants or users? If yes, a Resettlement Action Plan is mandatory for any DFI application.

7. **Employment**: Will the business employ workers, including casual, seasonal, or contracted staff? If yes, Employment Act 2006 compliance (contracts, leave, grievance procedures) and NSSF registration are mandatory from Day 1.

8. **Food, health, and product safety**: Does the business handle food, medicines, cosmetics, or any consumer product subject to standards regulation? If yes, UNBS certification (food) or NDA registration (pharmaceuticals/medical devices) must be built into the pre-opening compliance plan.

9. **Vulnerable groups**: Does the product or service disproportionately affect women, youth, children, persons with disabilities, or refugee communities? If yes, positive targeting (SDG 5, 10) or safeguarding obligations apply.

10. **SDG alignment**: Which 23 SDGs are most directly relevant to this business? Be specific: not merely "SDG 8 Decent Work" but "SDG 8.3  promote decent job creation and support micro and small enterprises."

11. **Climate adaptation priority**: What is the single most important climate adaptation measure for this business? Examples: drought-resistant input sourcing, flood-proof storage design, diversified crop or product mix, rainwater harvesting.

12. **ESMP requirement**: Is an Environmental and Social Management Plan (ESMP) required? Required for all UDB and DFI applications. Strongly recommended for any commercial bank loan above UGX 200M. If yes, use the template at `11-funding-request/references/esmp-template.md`.

---

## Mode C: Sustainability Audit

Run this section-by-section verification table after all sections are drafted.

| Plan Section | Sustainability Check | Pass / Fail |
|---|---|---|
| 02 Company Overview | Sustainability embedded in mission or vision  not bolted on as a footnote? | |
| 03 Products & Services | Sustainable design principles applied to product or service? Circular economy opportunities considered? | |
| 07 Marketing & Sales | Any green marketing claims substantiated with evidence? No greenwashing? | |
| 08 Operations | Waste, water, and energy efficiency measures documented with targets? | |
| 09 Management Team | Named sustainability champion identified with clear accountability? | |
| 10 Financial Projections | Sustainability capex and opex budgeted (NEMA fees, ESMP costs, eco-efficiency investment)? | |
| 12 Risk Analysis | Environmental and social risks included in the risk matrix with mitigation measures? | |
| 13 Implementation | Sustainability milestones (NEMA, EIA, ESMP, NSSF) included in Gantt chart? | |
| 14 AI Integration | AI energy use and data privacy considerations addressed? | |
| 16 Sustainability Strategy | Dedicated sustainability section present in the plan? | |

After completing the table, calculate the SRS using the scoring framework above. If any Pass/Fail item scores Fail, it must be corrected before submission.

---

## Quick Reference: SDG Alignment for Uganda SMEs

The six SDGs most relevant to Uganda small and medium enterprises:

| SDG | Title | Priority Action for Uganda SMEs |
|---|---|---|
| SDG 1 | No Poverty | Create direct employment; pay living wages above the poverty line; engage low-income supply chains |
| SDG 2 | Zero Hunger | Reduce post-harvest losses; improve food safety and nutrition; support smallholder farmers in the supply chain |
| SDG 3 | Good Health and Well-Being | Ensure worker occupational health; provide safe products; offer affordable healthcare-adjacent services |
| SDG 5 | Gender Equality | Employ and promote women at all levels; design products that serve women's needs; eliminate discriminatory practices |
| SDG 8 | Decent Work and Economic Growth | Register all workers; pay statutory benefits; create quality employment; support supply chain livelihoods |
| SDG 13 | Climate Action | Implement climate adaptation measures; reduce resource intensity; build supply chain resilience to climate shocks |

---

## References

The following reference files support this skill:

- **`references/sustainability-strategy-framework.md`**  Vectoring framework, Four Archetypes, Materiality Matrix, Business Case for Sustainability, Circular Economy principles, SDG integration, Six Capitals. Source: Leleux & van der Kaaij (2019), *Winning Sustainability Strategies*.

- **`references/sustainability-indicators-measurement.md`**  Indicator types (descriptive, performance, efficiency), PSR and DPSIR frameworks, headline vs aggregated indices, KPI selection guide. Source: Hak, Moldan & Dahl (2007), *Sustainability Indicators*.

- **`references/sustainability-decisions-policy.md`**  Quadruple Bottom Line (QBL), reform vs transformation, seven decision criteria, spillover and rebound effects, stakeholder deliberation. Sources: Dietz (2023); Waite (2023).

- **`11-funding-request/references/esmp-template.md`**  IFC/UDB-compliant Environmental and Social Management Plan template for DFI applications.

- **`16-sustainability-strategy/SKILL.md`**  Full sustainability strategy section generation (Section 16 of the business plan).

- **`meta-bankability-scoring/SKILL.md`**  CAMPARI compliance framework, which includes social licence to operate as a scoring dimension.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| ESG screening and action register decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to calling a plan sustainable before material impacts are assessed. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the ESG screening and action register; recording screening actions without certifying compliance is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If site, sector, labour, community, governance, and funder requirements cannot be obtained, return a qualified ESG screening and action register covering only the checks that remain supportable. Leave this decision unresolved: which impacts need mitigation, specialist study, or escalation. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which impacts need mitigation, specialist study, or escalation | Record the conclusion, source trail, owner, and review trigger in the ESG screening and action register. | Risk of calling a plan sustainable before material impacts are assessed |
| Material evidence conflicts or remains uncertain | Screen the disputed impact against the relevant site, workforce, community, and funder evidence, escalating material uncertainty to a specialist. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: site, sector, labour, community, governance, and funder requirements | Mark the decision on which impacts need mitigation, specialist study, or escalation `not assessed` in the ESG screening and action register, and send it to the ESG owner and relevant impact specialist. | Otherwise, the work risks calling a plan sustainable before material impacts are assessed |

## Quality Standards


Accept the ESG screening and action register only when evidence is sufficient for this decision: which impacts need mitigation, specialist study, or escalation. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of calling a plan sustainable before material impacts are assessed.

## Worked Example


A processing plant claims community benefit but has not assessed effluent or seasonal labour. Keep the positive claim unverified, screen both risks, and commission specialist work for any material gap.

<!-- dual-compat-end -->
