# Process Automation Readiness Reference

Frameworks for assessing automation opportunities, selecting technology strategies, and making processes executable — drawn from BPM and systems analysis methodologies.

---

## Automation Levels Spectrum (Dumas et al.)

Processes exist on a spectrum from fully manual to fully automated:

| Level | Description | Example | Coordination |
|-------|-------------|---------|-------------|
| **Manual** | Paper-based, no IT involvement | Handwritten ledgers, physical filing, verbal instructions | Human memory and physical artefacts |
| **IT-supported** | Standalone applications assist individual tasks | Spreadsheets for calculations, email for communication | Human-driven, tools are isolated |
| **IT-enabled** | Integrated systems support the process, but humans coordinate | ERP for inventory, CRM for sales, manual handoffs between systems | Humans coordinate across systems |
| **BPMS-managed** | Automated workflow routing with some manual tasks | System assigns work items, tracks progress, escalates delays | System coordinates, humans execute tasks |
| **Fully automated** | Minimal human involvement, straight-through processing | Automated invoice matching, algorithmic trading, sensor-driven alerts | System coordinates and executes |

**Key principle**: Most businesses operate at the IT-supported or IT-enabled level. Moving to BPMS-managed or fully automated requires significant process maturity.

---

## When to Automate — Decision Framework (Dumas et al.)

### Automate When High On:

| Factor | Why It Favours Automation |
|--------|--------------------------|
| **Volume** | High repetitions justify the investment; manual processing becomes a bottleneck |
| **Standardisation** | Low variability means the process can be codified reliably |
| **Rule-based** | Decisions follow clear if-then logic that software can execute |
| **Data availability** | Required inputs are already in digital form |
| **Error impact** | Costly mistakes make automated checks and validations worthwhile |
| **Speed requirement** | Fast turnaround needed beyond human capability |

### Leave Manual When:

| Factor | Why It Favours Manual Processing |
|--------|--------------------------------|
| **Judgement required** | Complex, contextual decisions that require human intuition, empathy, or creativity |
| **Low volume** | Too few transactions to justify automation investment |
| **High variability** | Every case is different, making codification impractical |
| **Customer relationship value** | Human touch adds perceived value (e.g., relationship banking, bespoke consulting) |

### Assessment Matrix

For each candidate process, rate each factor (1-5) and calculate:
- **Automation score** = Sum of (Volume + Standardisation + Rule-based + Data availability + Error impact + Speed requirement)
- **Manual score** = Sum of (Judgement required + Variability + Relationship value)
- **Net automation benefit** = Automation score − Manual score
- Prioritise processes with the highest net automation benefit

---

## Automation Readiness Checklist (Dumas et al.)

Before proceeding with automation, confirm each item:

- [ ] Process is **documented and standardised** — as-is map exists and is validated
- [ ] **Volume justifies** automation investment — calculate transactions per period
- [ ] **Decision rules can be codified** — all branching logic is documented
- [ ] Required **data is digitally available** — no manual data entry required at inputs
- [ ] **Integration points identified** — upstream and downstream systems are known
- [ ] **Exception handling procedures defined** — what happens when the process cannot follow the standard path
- [ ] **Staff training plan prepared** — users know how to work with the automated process
- [ ] **ROI calculation shows positive return** — benefits exceed costs within acceptable payback period
- [ ] **Regulatory compliance confirmed** — automated process meets all legal and industry requirements

---

## BPMS Components (Dumas et al.)

A Business Process Management System (BPMS) consists of six core components:

| Component | Function |
|-----------|----------|
| **Process modelling tool** | Design and document process flows visually (BPMN notation) |
| **Execution engine** | Runs process instances, manages state transitions, enforces sequencing |
| **Worklist handler** | Assigns tasks to participants, manages work queues, tracks completion |
| **Integration middleware** | Connects the BPMS to external systems (ERP, CRM, databases, APIs) |
| **Monitoring dashboard** | Real-time visibility into process performance, bottlenecks, and SLA compliance |
| **Administration tools** | User management, access control, process versioning, configuration |

---

## BPMS Architecture Layers (Dumas et al.)

| Layer | Purpose | Technologies |
|-------|---------|-------------|
| **Presentation** | User interface for task execution, process monitoring, and administration | Web portals, mobile apps, forms |
| **Process** | Process logic, routing rules, business rules, escalation | BPMN engine, rule engine |
| **Integration** | Connectivity to external systems and data sources | APIs, message queues, ESB, webhooks |
| **Data** | Persistent storage of process instances, audit trails, and business data | Databases, document stores, data warehouses |

---

## Task Types in Process Automation (Dumas et al.)

| Task Type | Description | Automation Approach |
|-----------|-------------|-------------------|
| **User task** | Requires human input or decision | Present form/interface, human completes and submits |
| **Service task** | Invokes an external service or system | Automated API call, no human involvement |
| **Script task** | Executes a script or calculation | Automated inline execution |
| **Send task** | Sends a message to an external party | Automated email, notification, or API message |
| **Receive task** | Waits for an external message or event | System listens for trigger, then proceeds |
| **Manual task** | Physical activity performed outside the system | System tracks status but cannot automate the work itself |
| **Business rule task** | Evaluates a decision table or rule set | Automated decision based on codified rules |

**AI integration opportunity**: User tasks that involve pattern recognition, classification, or natural language processing are prime candidates for AI augmentation — the system can suggest or pre-fill, with human review.

---

## Decision Tables for Automation (Dumas et al.)

### Structure

A decision table maps input conditions to output actions:

| Condition 1 | Condition 2 | Condition 3 | → Action |
|-------------|-------------|-------------|----------|
| Value A | Value X | Value P | Action 1 |
| Value A | Value Y | Any | Action 2 |
| Value B | Any | Any | Action 3 |

### Properties of Well-Formed Decision Tables

| Property | Meaning |
|----------|---------|
| **Completeness** | Every possible combination of inputs maps to an action |
| **Non-redundancy** | No two rows produce the same action for the same conditions |
| **Consistency** | No two rows produce different actions for the same conditions |

### Use Cases for Decision Tables

- **Credit approval** — Income level × Credit score × Debt ratio → Approve/Decline/Review
- **Pricing rules** — Customer segment × Order volume × Season → Price tier
- **Eligibility screening** — Age × Income × Location → Eligible/Ineligible/Conditional
- **Routing** — Request type × Urgency × Value → Assigned team
- **Escalation** — SLA breach × Customer tier × Issue type → Escalation level

---

## Making Processes Executable — 9 Steps (Dumas et al.)

To move from a documented process to an executable automated process:

| Step | Activity | Output |
|------|----------|--------|
| 1 | **Refine granularity** | Break high-level tasks into atomic executable steps |
| 2 | **Define task types** | Classify each step as user, service, script, send, receive, manual, or business rule |
| 3 | **Design forms** | Create input/output interfaces for user tasks |
| 4 | **Define data model** | Specify all data objects, their attributes, and relationships |
| 5 | **Configure services** | Set up API connections, system integrations, and external service calls |
| 6 | **Define business rules** | Build decision tables and rule sets for automated decisions |
| 7 | **Assign participants** | Map roles and individuals to each task (role-based assignment preferred) |
| 8 | **Configure exception handling** | Define what happens when tasks fail, time out, or encounter unexpected conditions |
| 9 | **Test** | Execute the process with test data, verify all paths, fix defects |

---

## Automation Challenges and Mitigations (Dumas et al.)

| Challenge | Description | Mitigation |
|-----------|-------------|-----------|
| **Process standardisation** | Processes must be stable and documented before automation is viable | Complete BPI cycle first; standardise, then automate |
| **Exception handling** | Automated processes struggle with unusual cases | Design explicit exception paths; route exceptions to human handlers |
| **Change management** | Staff may resist automation (fear of job loss, loss of control) | Communicate benefits, involve staff in design, retrain for higher-value work |
| **Integration complexity** | Connecting multiple systems is technically challenging | Use middleware/APIs; start with loosely coupled integrations |
| **Maintenance** | Automated processes need ongoing updates as rules and systems change | Build change management procedures; version control for process definitions |
| **Over-automation** | Automating processes that should remain manual destroys value | Use the decision framework above; preserve human touch where it matters |

---

## Key Principle: Redesign Before Automating

> "Don't pave the cow path." — BPM proverb

Automating a broken or inefficient process merely produces broken or inefficient results faster.

Page reinforces this: *"Automation applied to an efficient operation magnifies efficiency; automation applied to an inefficient operation magnifies inefficiency."*

**The correct sequence**:
1. Document the as-is process
2. Analyse for waste, bottlenecks, and redundancy
3. Redesign the to-be process (eliminate waste first)
4. Standardise the improved process
5. **Then** automate

Skipping steps 2-4 is the most common and most expensive automation mistake.

---

## Design Strategies: Build vs Buy vs Outsource (Dennis et al.)

### Decision Framework

| Strategy | Strengths | Weaknesses | Best When |
|----------|-----------|------------|-----------|
| **Custom build** | Exact fit to requirements, full control, proprietary advantage | Expensive, slow, requires in-house skills, maintenance burden | Unique competitive need, in-house development skills, flexible timeline |
| **Packaged software (Buy)** | Faster deployment, proven reliability, vendor support, lower initial cost | May not fit exactly, vendor dependency, customisation limits, ongoing licence fees | Common business need, short timeframe, limited in-house skills |
| **Outsource** | Access to specialist skills, focus on core business, flexible scaling | Loss of control, communication challenges, dependency on vendor, security risks | Non-core function, skills gap, variable demand, cost reduction priority |

### Outsourcing Contract Types (Dennis et al.)

| Contract Type | Description | Risk Allocation |
|---------------|-------------|----------------|
| **Time-and-arrangements** | Pay for time and resources used; scope flexible | Risk with buyer (cost can escalate) |
| **Fixed-price** | Agreed price for defined deliverables; scope fixed | Risk with vendor (must deliver within budget) |
| **Value-added** | Payment tied to business outcomes or value delivered | Shared risk (aligned incentives) |

### Selection Criteria

For each technology component, evaluate:
- Strategic importance (core vs non-core)
- Availability of suitable packages
- In-house technical capability
- Timeline constraints
- Budget constraints
- Long-term maintenance requirements

---

## Citations

- Dumas, M., La Rosa, M., Mendling, J. and Reijers, H.A. (2013). *Fundamentals of Business Process Management*. Berlin: Springer.
- Dennis, A., Wixom, B.H. and Tegarden, D. (2021). *Systems Analysis and Design: An Object-Oriented Approach with UML*. 6th ed. Hoboken: Wiley.
