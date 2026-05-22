# Business Process Management for Operations Planning

Reference content consolidated from Dumas et al. (2013) *Fundamentals of Business Process Management* and Page (2015) *The Power of Business Process Improvement: 10 Simple Steps*.

---

## BPM Lifecycle (Dumas et al., 2013)

Six phases forming a continuous cycle — business plans should demonstrate awareness that processes are not static:

1. **Process Identification** — Determine which processes are relevant and set priorities for improvement
2. **Process Discovery** — Document the current (as-is) state of each process
3. **Process Analysis** — Identify issues, bottlenecks, and waste in existing processes
4. **Process Redesign** — Design the improved (to-be) process
5. **Process Implementation** — Execute changes (technical and organisational)
6. **Process Monitoring** — Track performance and feed insights back into identification

For a business plan, demonstrate at minimum that core processes have been identified, documented, and analysed. Show that redesign and monitoring mechanisms are planned.

---

## Devil's Quadrangle (Dumas et al., 2013)

Four performance dimensions for any process. The key insight: **you cannot optimise all four simultaneously**. Improving one typically degrades another.

```
        Time
         /\
        /  \
       /    \
Cost /______\ Quality
       \    /
        \  /
         \/
      Flexibility
```

**Strategic alignment determines priority:**

| Business Strategy | Primary Dimension | Secondary | Accept Trade-off In |
|---|---|---|---|
| Cost leadership | Cost reduction | Time | Quality, Flexibility |
| Differentiation | Quality, Flexibility | — | Cost, Time |
| Speed-to-market | Time reduction | Quality | Cost |
| Mass customisation | Flexibility | Quality | Time, Cost |

A business plan must state which dimensions the operation prioritises and explicitly acknowledge the trade-offs.

---

## Process Identification (Dumas et al., 2013)

### Two Approaches

1. **Top-down (function-based)** — Start from organisational structure and functions, then identify processes within each
2. **Bottom-up (case-based)** — Start from case types (things the business handles) and trace the process for each

### Case Type Method

Name processes by their trigger-to-outcome pattern:

| Case Type | Trigger | Outcome |
|---|---|---|
| Order-to-Cash (O2C) | Customer order received | Payment collected |
| Quote-to-Order (Q2O) | Customer enquiry | Signed contract |
| Procure-to-Pay (P2P) | Purchase need identified | Supplier paid |
| Issue-to-Resolution (I2R) | Customer complaint | Issue resolved |
| Application-to-Approval (A2A) | Application submitted | Decision issued |

### Process Selection Matrix

Prioritise which processes to document and improve based on two axes:

```
High Dysfunction │ Quick wins    │ MUST DO
                 │ (easy fixes)  │ (critical)
─────────────────┼───────────────┼─────────────
Low Dysfunction  │ Low priority  │ Nice to have
                 │ (leave alone) │ (invest later)
                 └───────────────┴─────────────
                   Low Importance  High Importance
                   (Strategic)     (Strategic)
```

### Process Landscape Map

Organise all business processes into three bands:

```
┌─────────────────────────────────────────────────┐
│           MANAGEMENT PROCESSES                   │
│  (Strategic planning, Governance, Performance)   │
├─────────────────────────────────────────────────┤
│              CORE PROCESSES                      │
│  (Direct value creation — what customer pays for)│
│  e.g., O2C, Service Delivery, Product Dev        │
├─────────────────────────────────────────────────┤
│            SUPPORT PROCESSES                     │
│  (Enable core processes — HR, IT, Finance, Admin)│
└─────────────────────────────────────────────────┘
```

---

## Process Types (Dumas et al., 2013)

### Three Categories

1. **Core processes** — Directly create value for the customer. These are what the customer pays for.
2. **Support processes** — Enable core processes but are invisible to the customer (HR, IT, finance, procurement).
3. **Management processes** — Govern the organisation (strategic planning, performance management, compliance).

### Common Process Patterns

- **O2C (Order-to-Cash)** — Sales and fulfilment
- **Q2O (Quote-to-Order)** — Pre-sales and contracting
- **P2P (Procure-to-Pay)** — Purchasing and supplier management
- **I2R (Issue-to-Resolution)** — Customer service and complaints
- **A2A (Application-to-Approval)** — Loan processing, permits, onboarding

---

## Process Ingredients

Every process consists of seven elements:

1. **Events** — Things that happen (triggers and outcomes)
2. **Activities** — Work steps performed by actors
3. **Decision points** — Branches where the flow takes different paths
4. **Actors** — People or systems that perform activities
5. **Objects** — Physical or informational items consumed, produced, or transformed
6. **Outcomes** — Results of the process (positive or negative)
7. **Customers** — Internal or external recipients of the process output

---

## Value-Added Analysis (Dumas et al., 2013; Page, 2015)

### Three Activity Categories

| Category | Definition | Action |
|---|---|---|
| **Value-Adding (VA)** | Customer would pay for this activity; it transforms the product/service | Keep and optimise |
| **Business-Value-Adding (BVA)** | Business requires it (compliance, controls, reporting) but customer does not directly value it | Minimise |
| **Non-Value-Adding (NVA)** | Neither customer nor business benefits; pure waste | Eliminate |

### Application Methods

- **Page's approach**: Colour-code activities on the process map — green (VA), yellow (BVA), red (NVA) — to make waste visually obvious
- **Dumas's finding**: Typically only 5–45% of total cycle time is value-adding. The rest is waiting, handoffs, rework, and bureaucracy

### Key Questions for Classification

- Would the customer willingly pay for this step? → VA
- Does a law, regulation, or audit require this step? → BVA
- Is this step only done because "we've always done it"? → NVA

---

## Seven Wastes — TIMWOOD+H (Lean/Dumas et al., 2013)

| Waste | Operations Example |
|---|---|
| **T**ransportation | Unnecessary movement of materials between locations |
| **I**nventory | Excess stock tying up working capital |
| **M**otion | Unnecessary movement of people (poor layout, searching for tools) |
| **W**aiting | Idle time between process steps; queued work |
| **O**verproduction | Making more than needed or before needed |
| **O**ver-processing | More work than required (gold-plating, redundant approvals) |
| **D**efects | Errors requiring rework or scrap |
| **H**andoffs | Transferring work between people/departments (adds delay, errors, context loss) |

---

## Improvement Technique Wheel (Page, 2015)

Apply improvement techniques in this specific order — **automation is always last**:

1. **Eliminate Bureaucracy** — Remove unnecessary approvals, sign-offs, reviews. Use the SALT filter:
   - **S**tatutory — Is it required by law?
   - **A**udit — Is it required by auditors?
   - **L**egal — Is it required by legal/contracts?
   - **T**ax — Is it required for tax compliance?
   - If none apply, the step is likely bureaucracy and a candidate for elimination.

2. **Value-Added Analysis** — Classify every activity as VA, BVA, or NVA and eliminate NVA activities

3. **Eliminate Duplication** — Find and remove redundant steps, duplicate data entry, repeated verifications

4. **Simplification** — Reduce complexity in forms, procedures, communication, technology, and process flows

5. **Reduce Cycle Time** — Eliminate bottlenecks, parallelise activities, remove serial dependencies where possible

6. **Automation** — Only after all manual improvements have been made. As Bill Gates noted: *"Automation applied to an efficient operation will magnify the efficiency. Automation applied to an inefficient operation will magnify the inefficiency."*

---

## 29 Redesign Heuristics (Dumas et al., 2013)

Organised in seven categories. Key heuristics for business plan operations:

### Customer-Facing

| Heuristic | Description |
|---|---|
| **Control relocation** | Move checks and controls to the customer (self-service) |
| **Contact reduction** | Reduce number of contacts with customer per case |
| **Integration** | Combine with customer's or supplier's processes |

### Business Process Operation

| Heuristic | Description |
|---|---|
| **Activity elimination** | Remove non-value-adding activities entirely |
| **Activity composition** | Combine small activities into larger, composite ones |
| **Triage** | Split a general process into specialised variants (simple/complex) |
| **Parallelism** | Run independent activities simultaneously instead of sequentially |
| **Knock-out ordering** | Place checks/decisions that eliminate most cases earliest in the process |
| **Exception handling** | Separate normal flow from exception handling to streamline the main path |
| **Activity automation** | Use technology to perform activities previously done manually |

### Organisation

| Heuristic | Description |
|---|---|
| **Case manager** | Assign one person responsibility for each case end-to-end |
| **Resource centralisation** | Pool resources to improve utilisation and reduce idle time |
| **Flexible assignment** | Allow resources to handle multiple activity types |
| **Specialist-generalist** | Balance deep expertise with cross-functional capability |

### External Environment

| Heuristic | Description |
|---|---|
| **Outsourcing** | Transfer activities to external parties when they can do it better or cheaper |
| **Trusted party** | Accept information from trusted parties without re-verification |
| **Interfacing** | Standardise interfaces with partners to reduce friction |

---

## Process Maturity Assessment

Five levels — business plans targeting investor funding should demonstrate at least Level 3:

| Level | Stage | Characteristics | Evidence in Business Plan |
|---|---|---|---|
| 1 | **Initial** | Ad-hoc, hero-dependent, undocumented | No process section (red flag) |
| 2 | **Repeatable** | Key processes documented, roles defined | Process descriptions included |
| 3 | **Defined** | All processes standardised and measured | SOPs, KPIs, quality controls |
| 4 | **Managed** | Quantitative monitoring, SLAs in place | Dashboards, performance targets |
| 5 | **Optimised** | Continuous improvement culture, data-driven | Improvement roadmap, BPM tools |

---

## Process Performance Metrics

### Time Metrics

| Metric | Definition | Benchmark |
|---|---|---|
| **Cycle time (CT)** | Total elapsed time from trigger to outcome | Industry-specific |
| **Processing time (PT)** | Time actively working on the case | Usually 5–45% of CT |
| **Waiting time (WT)** | Time case spends idle between activities | Typically 55–95% of CT |
| **Cycle Time Efficiency (CTE)** | PT ÷ CT × 100% | 10% is common; 25%+ is world-class |

### Cost Metrics

- **Fixed costs** — Do not change with volume (rent, salaries, licences)
- **Variable costs** — Change proportionally with volume (materials, commissions)
- **Cost per case** — Total process cost ÷ number of cases processed

### Quality Metrics

- **Error rate** — Percentage of cases with errors
- **Rework rate** — Percentage of cases requiring rework
- **First-pass yield** — Percentage of cases completed correctly on first attempt

### Flexibility Metrics

- **Time to handle new product/service** — How quickly the operation adapts
- **Percentage of non-standard cases handled** — Ability to cope with variations

### Little's Law

A fundamental relationship for capacity planning:

```
WIP = λ × CT

Where:
  WIP = Work in Progress (number of cases in the system)
  λ   = Arrival rate (cases per time unit)
  CT  = Average cycle time
```

**Implication:** To reduce WIP (and thus working capital), you must either reduce arrival rate or reduce cycle time.

---

## Process Documentation Format (for Business Plans)

For each core process in the operations plan, document:

| Element | Description |
|---|---|
| **Process name** | Trigger-to-outcome format (e.g., Order-to-Delivery) |
| **Trigger** | What initiates the process |
| **Steps** | Sequential workflow with decision points |
| **Owner** | Person or role responsible end-to-end |
| **Duration** | Processing time and cycle time separately |
| **Dependencies** | Inputs, systems, upstream processes required |
| **Output** | What the process produces |
| **Quality check** | How quality is verified at each stage |
| **Process time vs Cycle time** | Distinguish active work from total elapsed time |

---

## Scope Definition Document (Page, 2015)

Before improving any process, define scope using these eight sections:

1. **Process Name** — Clear trigger-to-outcome name
2. **Process Owner** — Single accountable person
3. **Description** — What the process does and why it matters
4. **Scope** — Boundaries (where it starts and ends, what is in/out)
5. **Responsibilities** — Roles involved and their contributions
6. **Client/Client Needs** — Who receives the output and what they need
7. **Key Stakeholders** — Everyone affected by or interested in the process
8. **Measurements of Success** — How you know the process is performing well

This format is useful in business plans for demonstrating operational clarity to investors and lenders.

---

## Application in Business Plans

### For Startups

- Focus on designing efficient processes from the start (Level 2–3 maturity target)
- Document core processes with enough detail to show operational readiness
- Use the Devil's Quadrangle to justify operational priorities aligned with strategy
- Apply the improvement technique wheel to show awareness of continuous improvement

### For Existing Businesses Seeking Funding

- Show current process maturity level and improvement roadmap
- Include CTE metrics to demonstrate operational efficiency
- Use value-added analysis findings to justify planned improvements
- Quantify expected gains from process redesign (time, cost, quality)

### For All Business Plans

- Map at least the top 3–5 core processes using the documentation format above
- Include a process landscape map showing management, core, and support processes
- Reference the BPM lifecycle to demonstrate processes will be continuously monitored and improved
- Use Little's Law for capacity planning and working capital projections

---

## Citations

- Dumas, M., La Rosa, M., Mendling, J. & Reijers, H.A. (2013) *Fundamentals of Business Process Management*. Berlin: Springer.
- Page, S. (2015) *The Power of Business Process Improvement: 10 Simple Steps to Increase Effectiveness, Efficiency, and Adaptability*. 2nd edn. New York: AMACOM.
