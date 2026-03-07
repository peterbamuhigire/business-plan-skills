# Implementation & Change Management Reference

Frameworks for structured project implementation and organisational change management, drawn from BPM and systems analysis methodologies.

---

## Three-Phase Implementation Model (Page)

Page structures implementation into three sequential phases after the process has been analysed and improved.

### Phase 1: Design (Steps 1-7 of BPI Roadmap)

| Step | Activity | Output |
|------|----------|--------|
| 1 | Process inventory | Complete list of business processes |
| 2 | Establish scope | Boundaries, constraints, process selected for improvement |
| 3 | Process mapping | As-is process map with all steps documented |
| 4 | Time and cost estimation | Baseline metrics for current process |
| 5 | Process verification | Validated map confirmed with process workers |
| 6 | Process improvement | To-be process map with improvements applied |
| 7 | Controls and metrics | Measurement system for the improved process |

### Phase 2: Development

- **Build tools** — Create or configure the systems, forms, templates, and technology needed to support the new process
- **Develop report specifications** — Define what data will be captured and how it will be reported
- **Gain client approval** — Review deliverables with the process owner/sponsor before proceeding
- **Manage task dependencies** — Sequence development tasks so that dependent items are completed in the correct order

### Phase 3: Implementation

Implementation runs four parallel tracks simultaneously:

#### Track 1: Change Management
- Refine impact analysis — assess how each stakeholder group is affected
- Validate responsibility assignments — confirm who owns each new process step
- Determine rollout strategy — phased, pilot, parallel, or direct cutover
- Engage sponsors to champion the change

#### Track 2: Testing
- Confirm the redesigned process works as intended
- Validate that tools and technology function correctly
- Run end-to-end tests with representative scenarios
- Document and resolve defects before go-live

#### Track 3: Communication
- Identify **audience** — who needs to know what
- Define **goals** — what each audience should understand and do
- Craft **key messages** — clear, consistent, tailored to each group
- Select **vehicles** — email, meetings, newsletters, intranet, posters
- **Sequencing** — communicate in this order:
  1. Clients/customers first (they experience the change externally)
  2. Stakeholders and sponsors (they champion the change)
  3. Process workers (they execute the change daily)

#### Track 4: Training
- Identify **audience** — who needs training and at what level
- Define **learning objectives** using the Know-Absorb-Apply hierarchy:
  - **Know** — Awareness of the new process and why it changed
  - **Absorb** — Understanding of how to perform each step
  - **Apply** — Ability to execute the process independently
- Determine **approach** — classroom, one-on-one, computer-based, on-the-job
- Develop **tools** — manuals, quick-reference cards, videos, practice environments
- Prepare **facilitators** — train-the-trainer approach for scalability
- Focus training on doing the job, not just using the system

---

## Implementation Time Estimates (Page)

Typical durations for each BPI step (actual times vary by process complexity):

| BPI Step | Simple Process | Moderate Process | Complex Process |
|----------|---------------|-----------------|----------------|
| Process inventory | 1-2 weeks | 2-4 weeks | 4-8 weeks |
| Establish scope | 1 week | 1-2 weeks | 2-4 weeks |
| Process mapping | 2-4 weeks | 4-8 weeks | 8-16 weeks |
| Time/cost estimation | 1-2 weeks | 2-4 weeks | 4-8 weeks |
| Process verification | 1 week | 1-2 weeks | 2-3 weeks |
| Process improvement | 2-4 weeks | 4-8 weeks | 8-16 weeks |
| Controls and metrics | 1-2 weeks | 2-4 weeks | 4-8 weeks |
| Development | 4-8 weeks | 8-16 weeks | 16-32 weeks |
| Implementation | 2-4 weeks | 4-8 weeks | 8-16 weeks |

**Key insight**: The design phase typically takes longer than expected. Rushing design leads to rework during implementation.

---

## Work Breakdown Structure (Dennis et al.)

A WBS is a hierarchical decomposition of the total scope of work into manageable tasks.

### Task Attributes

Each task in the WBS should include:

| Field | Description |
|-------|-------------|
| Task name | Descriptive action item (verb + noun) |
| Duration | Estimated time in days or hours |
| Dependency | Predecessor task(s) that must complete first |
| Status | Planned / In Progress / Complete |
| Person assigned | Individual responsible for completion |
| Deliverables | Tangible outputs or artefacts produced |
| Priority | Critical / High / Medium / Low |

### Evolutionary WBS

For iterative projects, organise the WBS by:
- **Workflows** (columns) — e.g., Analysis, Design, Development, Testing, Deployment
- **Phases** (rows) — e.g., Inception, Elaboration, Construction, Transition
- **Iteration tasks** (cells) — specific activities within each workflow-phase intersection

This structure supports agile or iterative implementation where phases overlap and tasks are revisited.

---

## Gantt Chart Guidelines (Dennis et al.)

- **Format**: Horizontal bar chart where each bar represents a task's duration
- **Milestones**: Shown as diamond shapes at key dates
- **Dependencies**: Arrows connecting predecessor tasks to successor tasks
- **Readability**: Limit to **20-30 tasks per chart** — break larger projects into sub-charts
- **Updates**: Shade completed portions of each bar to show progress
- **Baseline**: Save the original schedule as a baseline to track variance

### Gantt Chart Best Practices for Business Plans

- Show major phases and milestones only (detail goes in operational documents)
- Use colour coding for different workstreams or departments
- Highlight the critical path
- Include key decision gates

---

## Network Diagrams — PERT/CPM (Dennis et al.)

### PERT Weighted Average Estimation

For each task, gather three estimates:

```
PERT Estimate = (Optimistic + 4 × Most Likely + Pessimistic) ÷ 6
```

**Example**:
- Optimistic: 5 days
- Most likely: 8 days
- Pessimistic: 17 days
- PERT estimate: (5 + 32 + 17) ÷ 6 = **9 days**

### Critical Path Method (CPM)

- The **critical path** is the longest sequence of dependent tasks through the project
- Any delay on a critical-path task delays the entire project by the same amount
- Tasks not on the critical path have **slack** (float) — they can be delayed without affecting the project end date
- **Managing the critical path**: focus resources, monitoring, and risk mitigation on critical-path tasks

### Forward and Backward Pass

- **Forward pass**: Calculate earliest start and earliest finish for each task
- **Backward pass**: Calculate latest start and latest finish working from the project deadline
- **Slack** = Latest Start − Earliest Start (tasks with zero slack are on the critical path)

---

## Conversion Strategies (Dennis et al.)

### By Approach

| Strategy | Description | Risk | Cost | Best For |
|----------|-------------|------|------|----------|
| Direct cutover | Old system stops, new system starts immediately | Highest | Lowest | Simple systems, forced deadlines, low-risk processes |
| Parallel | Both systems run simultaneously until new is proven | Lowest | Highest | Mission-critical operations, financial systems |
| Phased | New system rolls out in modules/stages | Moderate | Moderate | Large, complex systems with separable components |
| Pilot | New system tested at one location/unit first | Moderate | Moderate | Multi-location businesses, testable environments |

### By Location

| Strategy | Description | Best For |
|----------|-------------|----------|
| Pilot | Deploy at one location, learn, then expand | Testing approach before broad rollout |
| Simultaneous | Deploy everywhere at once | Small organisations, urgent deadlines |
| Phased by location | Roll out location by location over time | Large, geographically dispersed organisations |

### Selection Criteria

Choose based on: risk tolerance, budget, timeline pressure, system complexity, number of locations, and organisational readiness for change.

---

## Change Management 4-Step Plan (Dennis et al.)

### Step 1: Revise Management Policies

- Update **standard operating procedures** (SOPs) to reflect the new process
- Adjust **measurements and rewards** — people do what they are measured on
- Reallocate **resources** to support the new way of working
- If policies still reward old behaviour, people will revert

### Step 2: Assess Costs and Benefits from Adopters' Perspective

- **Perceived** costs and benefits matter more than **actual** costs and benefits
- For each stakeholder group, identify:
  - Personal costs (learning curve, status change, workload during transition)
  - Personal benefits (easier work, new skills, career advancement)
  - Certainty of each (guaranteed vs speculative)
  - Transition costs (temporary productivity loss)

### Step 3: Motivate Adoption

Two strategy types:

- **Informational strategy**: Convince through evidence, demonstration, and logic
  - Works when individual benefits are clear
  - Use pilot results, testimonials, demonstrations
  - Stress "painkillers" (solving existing pain) over "vitamins" (nice-to-have improvements)

- **Political strategy**: Use organisational authority and social pressure
  - Works when individual benefits are low but organisational benefits are high
  - Executive mandates, peer pressure, make adoption the path of least resistance

### Step 4: Enable Adoption Through Training

- Focus training on the **20% of functions used 80% of the time**
- Provide multiple training formats (classroom, self-paced, on-the-job coaching)
- Offer ongoing support — helpdesk, superusers, reference materials
- Schedule training close to go-live (training too early is forgotten)

---

## Adopter Distribution (Dennis et al.)

| Category | Percentage | Characteristics | Strategy |
|----------|-----------|-----------------|----------|
| Ready adopters | 20-30% | Enthusiastic, see the benefits, willing to try | Support them, make them proponents and internal champions |
| Reluctant adopters | 40-60% | Wait and see, follow the majority, need reassurance | They follow the flow — once ready adopters succeed, reluctant adopters follow |
| Resistant adopters | 20-30% | Oppose change, focus on costs, may actively undermine | Generally ignore — do not let them consume disproportionate time and energy |

**Key insight**: Focus energy on supporting ready adopters rather than converting resistant ones. When the majority sees ready adopters succeeding, the reluctant middle follows.

---

## Nine Factors for Successful Change (Dennis et al.)

For change to succeed, the following factors must be present:

| # | Factor | Description |
|---|--------|-------------|
| 1 | Personal reason | Each individual sees a personal benefit |
| 2 | Organisational reason | Clear business case for the change |
| 3 | Top management support | Senior leaders visibly champion the change |
| 4 | Business sponsor | A specific executive owns the change initiative |
| 5 | Credibility | The change team has expertise and trust |
| 6 | Low personal costs | Transition costs for individuals are manageable |
| 7 | Clear plan | Implementation steps are transparent and logical |
| 8 | Credible change agent | The person leading the change is trusted and competent |
| 9 | Clear mandate | Everyone knows the change is expected, not optional |

**Risk assessment**: If three or more factors are weak, the change initiative is at high risk of failure. Address weak factors before proceeding.

---

## Scope Management (Dennis et al.)

### Scope Creep

- **Definition**: Uncontrolled growth in project scope after the project begins
- **Impact**: The most common cause of project cost and schedule overruns
- **Causes**: Unclear initial requirements, stakeholder additions, gold-plating by the team

### Timeboxing

- Fix the **deadline** and adjust **features** to fit
- Prioritise features: Must-have → Should-have → Could-have → Won't-have (MoSCoW method)
- Deliver core functionality on time rather than everything late

### Scope Change Control

- Only allow additions that are **absolutely necessary**
- Require formal change requests with impact analysis
- Every addition must identify what will be removed or delayed in exchange
- Maintain a **parking lot** for future enhancements

---

## Citations

- Page, S. (2015). *The Power of Business Process Improvement: 10 Simple Steps to Increase Effectiveness, Efficiency, and Adaptability*. 2nd ed. New York: AMACOM.
- Dennis, A., Wixom, B.H. and Tegarden, D. (2021). *Systems Analysis and Design: An Object-Oriented Approach with UML*. 6th ed. Hoboken: Wiley.
