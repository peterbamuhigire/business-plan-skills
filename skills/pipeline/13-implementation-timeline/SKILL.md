---
name: 13-implementation-timeline
description: Use when producing or reviewing the 13 implementation timeline component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Implementation Timeline & Milestones Skill

## Overview

Generate Section 13 of the business plan: the implementation timeline. Use this skill to turn strategy into sequenced execution with milestones, owners, dependencies, and measurable progress checkpoints.

## Use When

- Use when drafting or revising the implementation timeline and milestones section.
- Use when the business needs a phased rollout, launch plan, or 90-day execution logic.
- Use when funders or operators need to see who does what, by when, and in what order.

## Do Not Use When

- Do not use before the operating model, funding needs, and strategic priorities are at least broadly defined.
- Do not create a calendar-shaped wish list with no ownership or dependencies.
- Do not ignore regulatory or capability gates that determine whether execution can start.

## Required Inputs

- Strategic priorities, operating model, and near-term commercial objectives
- Resource constraints, funding availability, and team ownership assumptions
- Country or regulatory context that affects launch or compliance timing
- Adjacent plan sections on operations, finance, risk, and monitoring

## Workflow

1. Confirm the business objective the timeline must deliver first.
2. Break execution into logical phases with gates, owners, and dependencies.
3. Attach milestones, resource needs, and measurable completion criteria.
4. Check that timing aligns with regulatory, staffing, and funding reality.
5. Reconcile the timeline with operations, cash flow, and risk assumptions.
6. Flag any blocking dependency that threatens the schedule.

## Quality Bar

- The sequence is executable, not merely aspirational.
- Owners, dates, and dependencies are explicit enough to manage.
- The timeline fits available capacity and capital.
- Milestones show decision points, not just activity lists.

## Anti-Patterns

- Timelines with no owners or no gating logic.
- Parallelising work that is legally or operationally sequential.
- Ignoring procurement, licensing, hiring, or capital-availability constraints.
- Milestones that cannot be measured or verified.

## Outputs

- A phased implementation timeline with milestones and owners
- Explicit dependencies, assumptions, and go/no-go points
- Cross-skill notes for finance, operations, monitoring, and risk



Generate an actionable implementation plan that converts the business strategy into phased, measurable execution. This is where the plan becomes a game plan.

## What to Generate

### Required Elements

1. **Phase breakdown**  Logical phases (pre-launch, launch, growth, scale)
2. **Key milestones**  Major achievements with target dates
3. **90-day game plans**  Quarterly action plans with weekly granularity
4. **Task assignments**  Who owns each milestone
5. **Dependencies**  What must happen before each phase begins
6. **Resource requirements**  People, money, and tools needed per phase
7. **Progress metrics**  How to measure milestone completion
8. **Go/no-go decision points**  Gates between phases
9. **Scope lock and change control**  What is in scope for each phase and how material changes are approved

### Pre-Phase 0: Regulatory Compliance Gate (Uganda)

Before Phase 1 can begin, all regulatory foundations must be in place. These are not optional and cannot be done in parallel with operations  they are legal prerequisites.

**NIN/BRN gate (2025 requirement):** From 2025, a company TIN cannot be issued without a valid NIN (National ID from NIRA) for individual directors, or BRN (Business Registration Number from URSB) for companies. Without a TIN, no trading licence can be issued, no bank account opened in the company's name, and no government contracts signed.

**Mandatory pre-launch checklist (Uganda):**
- [ ] All directors have valid National IDs (NIN from NIRA)
- [ ] URSB registration complete  Business Name Certificate or Certificate of Incorporation obtained
- [ ] TIN registered with URA (free; requires NIN/BRN)
- [ ] Trading licence obtained from KCCA (Kampala) or local council (upcountry)
- [ ] NSSF registration (mandatory if employing staff; voluntary for self-employed)
- [ ] EFRIS registration with URA (for VAT-registered businesses or those approaching the UGX 150M threshold)
- [ ] Sector-specific licences obtained (UNBS, NEMA, NDA, UTB, UCC, BoU  as applicable to the sector)
- [ ] Business bank account opened in the company name
- [ ] Tax Compliance Certificate (TCC) from URA  required for government tenders

Include these as explicit Week 14 tasks in the Phase 1 game plan. Flag which licences have processing times of 714 days and must be applied for immediately.

### Phase Framework

**Phase 1: Foundation (Months 1-3)**
- Legal setup (see Pre-Phase 0 above), team assembly, product development kickoff
- Key deliverable: All licences in place + MVP or service framework ready

**Phase 2: Launch (Months 4-6)**
- Market entry, first customers, initial marketing
- Key deliverable: First revenue or validated demand

**Phase 3: Growth (Months 7-12)**
- Scale operations, expand marketing, optimise unit economics
- Key deliverable: Break-even trajectory confirmed

**Phase 4: Scale (Year 2+)**
- Geographic expansion, product line extension, team growth
- Key deliverable: Sustainable profitability or Series A readiness

### 90-Day Game Plan Template (King's Method)

```text
Quarter: [Q1/Q2/Q3/Q4 Year]
Objective: [The one thing this quarter must achieve]

Week 1-4: [Month 1 actions]
  - [ ] Action item (Owner) [Metric]
  - [ ] Action item (Owner) [Metric]

Week 5-8: [Month 2 actions]
  - [ ] Action item (Owner) [Metric]

Week 9-12: [Month 3 actions]
  - [ ] Action item (Owner) [Metric]

Quarter-end review:
  - Did we hit the objective?
  - What worked / what didn't?
  - Adjustments for next quarter?
```

### Milestone Table Format

| # | Milestone | Target Date | Owner | Dependencies | Success Metric | Status |
|---|-----------|------------|-------|--------------|----------------|--------|
| 1 | [Name] | [Date] | [Who] | [What] | [How measured] | Planned |

### Work Breakdown Structure (WBS)

Decompose each phase into a hierarchical task structure (Dennis et al., 2021):

| Field | Description |
|---|---|
| Task name | Descriptive action item |
| Duration | Estimated days (use PERT: (Optimistic + 4Likely + Pessimistic)  6) |
| Dependencies | Predecessor task IDs |
| Owner | Person assigned |
| Deliverables | Tangible outputs |
| Status | Planned / In Progress / Complete |

Identify the **critical path**  the longest sequence of dependent tasks. Any delay on a critical-path task delays the entire project.

### Change Management Tracks

Every implementation requires four parallel tracks (Page, 2015):

1. **Change management**  Impact analysis, rollout strategy, sponsor engagement
2. **Testing**  Validate processes and tools work as designed before go-live
3. **Communication**  Sequence: clients first  stakeholders  process workers. Develop FAQs for anticipated concerns
4. **Training**  Use Know-Absorb-Apply hierarchy for learning objectives. Focus on doing the job, not just using the system

### Conversion Strategy Selection

Choose a go-live approach based on risk tolerance (Dennis et al., 2021):

| Strategy | Risk | Cost | Best for |
|---|---|---|---|
| Direct cutover | Highest | Lowest | Simple systems, forced deadlines |
| Parallel | Lowest | Highest | Mission-critical operations |
| Phased | Moderate | Moderate | Large, complex systems |
| Pilot | Moderate | Moderate | Multi-location businesses |

## Generation Process

1. Ask for: launch date (planned), team capacity, funding timeline, key constraints
2. Define major phases aligned with business lifecycle
3. Set milestones with specific, measurable success criteria
4. Build first 90-day game plan in weekly detail
5. Map dependencies between milestones
6. Assign ownership for every milestone
7. Define go/no-go gates between phases
8. State which milestone deliverables require formal acceptance and which changes trigger replanning

## Quality Criteria

- Milestones are specific and measurable (not "grow the business")
- Timeline is realistic given resources and funding
- Dependencies are mapped  no orphan milestones
- 90-day game plans are actionable at the weekly level
- Go/no-go gates prevent premature scaling
- Timeline aligns with funding runway (section 11) and hiring plan (section 09)
- Change management plan addresses communication, training, and stakeholder adoption
- Critical path is identified and monitored
- Scope creep risks and change-control rules are explicit when implementation complexity is high

## References

- **Procurement and funding approvals as blocking gates (Uganda public-procurement and NGO/donor practice)**: See `references/procurement-and-gating-schedule.md` for treating PPDA procurement approvals (staged evaluation, Contracts Committee award, NOBEB and standstill, Attorney-General clearance, contract signature) and funding releases (commitment-control / quarterly expenditure limits for public bodies; donor disbursement tranches and conditions precedent for NGO projects) as BLOCKING predecessor milestones; NGO/donor programme cycles (6/12/24-month phases, no-cost extensions, reporting-driven tranche release); the M&E quarterly programmatic + financial (flexed-budget variance) reviews that gate the next tranche/phase; and how to render these gates in a Gantt/work plan with owners, lead times, and explicit critical-path risk flags. Cross-references the ppda-uganda sector skill and the chwezi-accounting-doctrine PFM/NGO references. **Read when the implementation timeline depends on a procured contract or on released funds — do not schedule downstream delivery before the approval gate completes. Statutory monetary thresholds must be verified against the current PPDA instrument.**
- **PE-grade initiative portfolio design and governance (Umbrex, 2025)**: See `../11-funding-request/references/value-creation-plan-primer.md` for initiative portfolio design framework (object/population/mechanism/evidence dimensions), scope and objective-setting methodology, impact estimation (addressable base  driver change  adoption curve  leakage), sequencing constraints (data/systems/people/cash/commercial timing/operating stability), decision gates, three-layer governance model (workstream/enterprise/board), forum design principles, reporting cadence and dashboards, escalation ladder, risk scenarios (base/upside/downside) with triggers and contingencies, and first 100 days prioritisation. **Read when designing the implementation governance structure, sequencing initiatives, or building the operating cadence for any investor or lender-facing plan.**
- **Implementation and change management**: See `references/implementation-change-management.md` for three-phase implementation model, four parallel implementation tracks (change management/testing/communication/training), WBS structure, Gantt/PERT guidelines, PERT estimation formula, critical path analysis, conversion strategies, 4-step change management plan, adopter distribution model, 9 factors for successful change, and scope management  from Page (AMACOM, 2015) and Dennis, Wixom & Tegarden (Wiley, 2021)
- **Project charter, scope, and change control**: See `../book-extractions/project-management-integration-scope-extraction.md` for objective vs scope vs deliverable distinctions, charter discipline, WBS thinking, acceptance criteria, and scope-creep control. **Read when the implementation plan covers major buildouts, system deployments, or multi-stakeholder execution.**

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Approved initiatives, dependencies, procurement lead times, owners, costs, milestones, and funding availability for 13 implementation timeline | Section owners, operations plan, financial model, and implementation lead | Yes | If absent, a dependency, owner, lead time, or funding release date is unavailable, keep the activity unscheduled or show a range and identify the decision date. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Dependency-aware implementation schedule with gates, owners, costs, and recovery actions | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 13 implementation timeline exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 13 implementation timeline release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Critical-path map, milestone acceptance tests, resource reconciliation, and delay scenario | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 13 implementation timeline decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 13 implementation timeline review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 13 implementation timeline, the controlling focus is dependency order, critical path, milestone acceptance, procurement lead time, funding release, ownership, and delay recovery. This skill may plan and review delivery sequencing; it may not procure, assign people, change live operations, or declare milestones complete without owner evidence. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 13 implementation timeline, loss of evidence about 13 implementation timeline evidence, decisions, failure thresholds, ownership, and downstream handoffs activates degraded mode. If the controlling 13 implementation timeline evidence is unavailable, the same boundary applies. When a dependency, owner, lead time, or funding release date is unavailable, keep the activity unscheduled or show a range and identify the decision date. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 13 implementation timeline, a milestone begins before its prerequisite, funding, procurement, or acceptance evidence exists| resequence it, expose the critical-path impact, and define the recovery option | Calendar dates disguise infeasible dependencies and unfunded work |
| For 13 implementation timeline, A current legal, regulatory, tax, accounting, market, or platform claim controls the 13 implementation timeline decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 13 implementation timeline, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete dependency-aware implementation schedule with gates, owners, costs, and recovery actions, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 13 implementation timeline decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect approved initiatives, dependencies, procurement lead times, owners, costs, milestones, and funding availability and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce dependency-aware implementation schedule with gates, owners, costs, and recovery actions with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Dependency-aware implementation schedule with gates, owners, costs, and recovery actions must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Critical-path map, milestone acceptance tests, resource reconciliation, and delay scenario must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 13 implementation timeline, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 13 implementation timeline, treating an unavailable approved initiatives, dependencies, procurement lead times, owners, costs, milestones, and funding availability as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing dependency-aware implementation schedule with gates, owners, costs, and recovery actions that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A retail opening is scheduled before premises handover and equipment commissioning. Move staff training after safe site access, gate launch on commissioning acceptance, and show the cost and date effect of a two-week handover delay.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 13 implementation timeline; no local deep-dive reference is declared.
- For 13 implementation timeline claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
