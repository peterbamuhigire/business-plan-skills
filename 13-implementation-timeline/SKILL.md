---
name: implementation-timeline
description: Generate the implementation timeline with phased milestones, Gantt-style breakdown, 90-day game plans, accountability assignments, and progress metrics. Based on Jan B. King's "Business Plans to Game Plans" methodology for converting strategy into executable action.
---

# Implementation Timeline & Milestones Skill

## Use When

- Use when this skill is the primary workflow for the requested task.
- Use when creating, reviewing, or improving this skill's main artifact.
- Use when this output must align with adjacent sections, assumptions, or audience requirements.

## Do Not Use When

- Do not use when another section or meta-skill is the primary owner of the task.
- Do not use when the required inputs are unavailable and cannot be stated transparently as assumptions.
- Do not use for provider-specific UI behaviour; keep the workflow portable.

## Required Inputs

- Business, client, or proposal context relevant to this skill
- Country, audience, funder, or user context where relevant
- Available assumptions, evidence, constraints, and dependencies
- Adjacent section outputs where consistency matters

## Workflow

1. Clarify the objective, audience, and scope for this skill.
2. Gather the minimum required inputs and note any missing assumptions.
3. Read the referenced materials only as needed.
4. Produce or revise the artifact using the skill-specific method below.
5. Reconcile the output with adjacent sections, numbers, risks, and evidence.
6. Flag unresolved gaps, assumptions, or follow-up work.

## Quality Bar

- Output is specific, decision-useful, and not generic
- Assumptions are explicit where relevant
- Claims align with the rest of the plan, proposal, or workflow
- Wording is structured, concise, and audience-appropriate

## Anti-Patterns

- Generic filler that could describe any business or situation
- Hidden assumptions or unsupported claims
- Contradictions with financials, implementation, risk, or audience requirements
- Provider-specific operating assumptions embedded in the portable workflow

## Outputs

- The primary artifact or analysis owned by this skill
- Any key assumptions, open questions, and cross-skill dependencies



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

```
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
  - Did we hit the objectiveSection 
  - What worked / what didn'tSection 
  - Adjustments for next quarterSection 
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

## Quality Criteria

- Milestones are specific and measurable (not "grow the business")
- Timeline is realistic given resources and funding
- Dependencies are mapped  no orphan milestones
- 90-day game plans are actionable at the weekly level
- Go/no-go gates prevent premature scaling
- Timeline aligns with funding runway (section 11) and hiring plan (section 09)
- Change management plan addresses communication, training, and stakeholder adoption
- Critical path is identified and monitored

## References

- **PE-grade initiative portfolio design and governance (Umbrex, 2025)**: See `../11-funding-request/references/value-creation-plan-primer.md` for initiative portfolio design framework (object/population/mechanism/evidence dimensions), scope and objective-setting methodology, impact estimation (addressable base  driver change  adoption curve  leakage), sequencing constraints (data/systems/people/cash/commercial timing/operating stability), decision gates, three-layer governance model (workstream/enterprise/board), forum design principles, reporting cadence and dashboards, escalation ladder, risk scenarios (base/upside/downside) with triggers and contingencies, and first 100 days prioritisation. **Read when designing the implementation governance structure, sequencing initiatives, or building the operating cadence for any investor or lender-facing plan.**
- **Implementation and change management**: See `references/implementation-change-management.md` for three-phase implementation model, four parallel implementation tracks (change management/testing/communication/training), WBS structure, Gantt/PERT guidelines, PERT estimation formula, critical path analysis, conversion strategies, 4-step change management plan, adopter distribution model, 9 factors for successful change, and scope management  from Page (AMACOM, 2015) and Dennis, Wixom & Tegarden (Wiley, 2021)
