---
name: 08-operations-plan
description: Use when producing or reviewing the 08 operations plan component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Operations Plan Skill

## Overview

Generate Section 08 of the business plan: the operations plan. Use this skill to show how the business delivers its offer reliably, economically, and at a scale that matches the strategy.

## Use When

- Use when drafting or revising the operations plan for a business plan, proposal, or lender document.
- Use when the business must prove it can fulfil demand, manage inputs, and maintain quality.
- Use when facilities, staffing, supply chain, technology, or delivery processes are material to viability.

## Do Not Use When

- Do not use for abstract strategy with no process or resource detail.
- Do not describe ideal-state operations that the business cannot support.
- Do not treat operations as a dump for organisational facts better handled elsewhere.

## Required Inputs

- Offer definition, delivery model, target volumes, and service expectations
- Supplier, facility, staffing, technology, and process information
- Country or regulatory context where licences, standards, or infrastructure matter
- Adjacent sections on products, team, implementation, finance, and risk

## Workflow

1. Map the end-to-end operating model from input to delivery and support.
2. Identify the critical processes, assets, staffing, and supplier dependencies.
3. Show how quality, throughput, and customer experience are controlled.
4. Explain what scales, what breaks, and what must be strengthened as demand grows.
5. Reconcile the operating model with implementation timing and financial assumptions.
6. Flag weak points in capacity, compliance, or process reliability.

## Quality Bar

- A reader can see how the business actually delivers the offer.
- Operational claims match the staffing, facilities, and cost base in the plan.
- Process and quality controls are specific enough to inspire confidence.
- The section shows an executable operating model, not an aspiration.

## Anti-Patterns

- Listing equipment or departments without explaining the workflow.
- Assuming suppliers, staff, or systems will scale automatically.
- Ignoring bottlenecks, quality risk, or customer handoff failures.
- Operational promises that contradict budget, timeline, or team capacity.

## Outputs

- A finished or revised Section 08 operations plan
- Process, resource, and scaling logic linked to the wider plan
- Explicit operating assumptions, constraints, and risk dependencies



Generate a detailed operations plan that demonstrates the business can deliver on its promises efficiently and at scale.

## What to Generate

### Required Elements

1. **Business model operations**  How the business creates and delivers value
2. **Key processes**  Core workflows from order to delivery
3. **Supply chain**  Suppliers, procurement, inventory management
4. **Facilities and equipment**  Physical locations, machinery, office space
5. **Technology infrastructure**  Systems, software, platforms, integrations
6. **Quality control**  Standards, testing, compliance procedures
7. **Staffing and HR**  Headcount, roles, hiring timeline
8. **Key partnerships**  Outsourced functions, strategic alliances
9. **Operational KPIs**  Metrics for measuring operational health
10. **Scalability plan**  How operations scale with growth
11. **Cycle-time improvement logic**  How the business reduces delay before adding more cost
12. **Customer-experience operations**  How operations support the full buying, delivery, and support journey
13. **Digitisation and systems layer**  Which workflows stay manual, which are digitised, which tools support them, and why
14. **Industrial production and inventory logic**  For manufacturing, processing, warehousing, wholesale, logistics, and distribution businesses, show MRP-style material planning, capacity, scheduling, storage, material handling, quality, and resource-efficiency assumptions.
15. **Logistics network and transportation logic**  For import, export, distribution, delivery, fleet, wholesale, retail, agriculture aggregation, and physical-goods businesses, show the logistics network, inventory service level, transport mode, carrier or fleet model, route assumptions, documentation controls, reverse logistics, and exception workflows.
16. **Digital service delivery and DevOps logic**  For SaaS, software, platform, managed IT, hosting, or app businesses, show how software moves from change request to production, how releases are controlled, how incidents are handled, and how reliability is measured.
17. **Website operations layer**  For any material website, ecommerce, booking, content/SEO, portal, or web app component, show who owns updates, enquiries, analytics, hosting, security, backups, content quality, SEO monitoring, support, and post-launch improvement. Run `../meta-website-investment-planning/SKILL.md` where costs or operating assumptions are material.

### Process Documentation Format

For each core process:

```text
Process: [Name]
Trigger: [What initiates this process]
Steps: [Sequential workflow]
Owner: [Who is responsible]
Duration: [How long it takes]
Dependencies: [What it requires]
Output: [What it produces]
Quality check: [How quality is verified]
```

### Operational Metrics to Define

- Production/delivery capacity (units/month or clients/month)
- Lead time (order to delivery)
- Fulfilment rate
- Defect/error rate
- Inventory turnover (if applicable)
- Uptime/availability (for tech/SaaS)
- Deployment frequency, change lead time, change failure rate, mean time to restore service, incident severity count, and support tickets caused by defects or downtime for software businesses
- Cost per unit produced/delivered
- Inventory days by raw materials, WIP, finished goods, packaging, and spares where relevant
- Production yield, scrap, rework, setup/changeover time, and practical capacity utilisation for manufacturing businesses
- Warehouse storage utilisation, pick accuracy, inventory accuracy, dock-to-stock time, and order fulfilment cycle time for distribution-heavy businesses
- On-time pickup, on-time delivery, OTIF, transport cost per order/unit/km, load utilisation, route adherence, freight claims, damage rate, backorder rate, stockout rate, and carrier or fleet scorecard for logistics-heavy businesses
- Energy intensity, water intensity, waste cost, and recovered by-product value for resource-intensive operations

### Business Process Management Framework

For each core operational process, apply the BPM lifecycle (Dumas et al., 2013):

1. **Identify**  Map all processes using the process landscape model (management / core / support)
2. **Document**  Create as-is process models showing current workflows
3. **Analyse**  Classify activities as value-adding (VA), business-value-adding (BVA), or non-value-adding (NVA)
4. **Redesign**  Apply improvement techniques in order: eliminate bureaucracy  eliminate duplication  simplify  reduce cycle time  automate last (Page, 2015)
5. **Implement**  Execute changes with proper change management
6. **Monitor**  Track performance using the Devil's Quadrangle dimensions

### Hypergrowth redesign sequence (McNeill)

Apply this order inside the redesign phase:

1. Question every requirement
2. Delete every possible step
3. Simplify and optimise
4. Accelerate cycle time
5. Automate last

This sharpens the BPM rule: do not automate waste.

### Whole-customer-experience operations

Do not define operations too narrowly. The operating system must cover:
- response to enquiries
- quoting or proposal turnaround
- order intake
- fulfilment or onboarding
- issue resolution
- repeat-purchase or renewal support

For service, SaaS, and project businesses, these customer-facing moments often matter more than back-office efficiency alone.

### Process Performance Trade-offs (Devil's Quadrangle)

Every process optimisation involves trade-offs across four dimensions  time, cost, quality, and flexibility. The business strategy determines which to prioritise:

- **Cost leadership**  optimise for cost reduction (accept longer times, less flexibility)
- **Differentiation**  optimise for quality and flexibility (accept higher costs)
- **Speed-to-market**  optimise for time reduction (accept higher costs)

State explicitly which dimensions the business prioritises and acknowledge trade-offs (Dumas et al., 2013).

### Process Maturity Level

Rate the business's operational maturity (target Level 3+ for investor confidence):

| Level | Stage | Evidence |
|---|---|---|
| 1 | Initial | Ad-hoc, hero-dependent, undocumented |
| 2 | Repeatable | Key processes documented, roles defined |
| 3 | Defined | All processes standardised and measured |
| 4 | Managed | Quantitative monitoring and SLAs |
| 5 | Optimised | Continuous improvement culture |

## Generation Process

1. Ask for: business type (product/service/SaaS), production method, team size, key tools
2. Map core value-delivery processes
3. Identify supply chain dependencies and risks
4. Document technology stack and infrastructure
5. Define quality control procedures
6. Plan staffing needs aligned to growth projections
7. Set operational KPIs with targets
8. Identify which requirements can be questioned, deleted, simplified, or accelerated before any automation spend is proposed
9. Map where operational design affects the customer experience directly
10. State which operational data must be captured to manage quality, throughput, stock, service, and owner visibility
11. For industrial businesses, test sales volume against material availability, batch size, work-centre capacity, storage capacity, lead times, and cash tied in stock before accepting the forecast.
12. For logistics, import/export, wholesale, retail, and distribution-heavy businesses, test the revenue forecast against network design, replenishment frequency, safety stock, warehouse space, route capacity, carrier reliability, fleet downtime, customs or border lead time, reverse logistics, and transportation cost.
13. For software or SaaS businesses, test the growth plan against release capacity, deployment risk, monitoring coverage, incident response, support load, cloud cost, backup/restore readiness, and security controls before accepting the forecast.
14. For website-dependent businesses, test the growth plan against content production, SEO timeline, conversion rate, enquiry handling, maintenance, hosting, analytics, and website support capacity before accepting the forecast.

## Quality Criteria

- Processes are specific enough to execute, not just described at a high level
- Supply chain risks are identified with mitigation plans
- Technology choices are justified (not just trendy)
- Digitisation choices are proportional to the business stage and remove a real bottleneck
- Scalability plan shows how operations handle 2x, 5x, 10x growth
- Staffing plan aligns with financial projections in section 10
- Operations plan shows where delay is removed before new tools are added
- Customer-facing operating moments are explicit, not hidden inside back-office descriptions
- Process owners and escalation points are clear for critical workflows
- For industrial plans, the operations section names the bottleneck, states the practical capacity calculation, explains inventory policy, and reconciles yield/scrap assumptions with the financial model.
- For logistics-heavy plans, the operations section names the network design, inventory service-level policy, transport mode and carrier/fleet model, route assumptions, documentation controls, exception handling, and transport cost logic.
- For software and SaaS plans, the operations section explains the delivery pipeline, release control, rollback posture, observability, incident response, security checks, cloud cost logic, and the operating maturity stage appropriate to the business.

### Small Business Operational Efficiency (Kaza)

For SME operations plans, apply the bottleneck framework from Kaza's analysis of 20,000+ small businesses:

**Step 1  Identify the bottleneck:**
Ask: When the business is at capacity, where does work stack up? What one step, if faster, would allow the business to serve more customers? Is the *owner* the bottleneck  the person without whom nothing moves?

**Step 2  Subordinate everything else:**
Once the bottleneck is identified, every other part of the operation should be structured to keep the bottleneck running at optimal capacity. Do not invest in non-bottleneck improvements  they will not increase overall output.

**Step 3  Optimise utilisation (not 100%):**
Sustained 100% utilisation leads to quality degradation and staff burnout. Target optimal utilisation  high enough to be profitable, low enough to maintain quality and service standards.

**Step 4  Monetise underutilised assets:**
Identify assets (space, equipment, staff time) that are underutilised during off-peak hours and create revenue streams from them. Examples:
- A restaurant's dining space used for morning business meetings
- A salon using after-hours capacity for evening workshops
- A logistics vehicle used for delivery services on return journeys

**Owner-as-bottleneck diagnostic**  common in Ugandan SMEs:

| Symptom | Underlying issue | Solution |
|---|---|---|
| Nothing progresses when owner travels | All decisions centralised | Document decisions; delegate authority |
| Owner works 12+ hours daily but growth is flat | Owner is in the bottleneck role | Hire or train to relieve the constraint |
| Business cannot quote without owner | No pricing authority delegated | Create pricing guidelines; train staff |
| Customer service depends on owner's relationships | Proximity not systematised | Build CRM; train staff on relationship protocols |

**Capacity utilisation planning template:**

```text
Peak capacity: [units/clients per day at maximum]
Target utilisation rate: [7085% for most businesses]
Current utilisation: [actual current rate]
Bottleneck stage: [which step limits throughput]
Bottleneck relief plan: [hire / automate / streamline / outsource]
Underutilised assets: [what sits idle and when]
Asset monetisation idea: [revenue from idle capacity]
```

(Kaza, 2025)

## Value Chain Analysis (Porter)

For businesses that need to explain *where* competitive advantage comes from in operational terms, use Porter's value chain framework. The value chain disaggregates the firm into nine strategically relevant activities and reveals the structural sources of cost advantage and differentiation.

### The Nine Activities (brief reference)

**Primary activities** (directly involved in product creation and delivery):
1. Inbound Logistics  receiving, storing, distributing inputs
2. Operations  transforming inputs into the final product
3. Outbound Logistics  collecting, storing, distributing finished goods
4. Marketing & Sales  enabling buyers to purchase and inducing them to do so
5. Service  maintaining or enhancing product value after sale

**Support activities** (enabling the primary activities):
6. Procurement  purchasing inputs used across all activities
7. Technology Development  know-how and procedures embedded in each activity
8. Human Resource Management  recruiting, training, compensation firmwide
9. Firm Infrastructure  general management, finance, accounting, legal, quality

### Applying Value Chain to the Operations Plan

In the operations plan, use the value chain to:
- Identify **which primary activities create the most value** and deserve the most operational investment
- Explain **which activities are the primary cost drivers**  and how management will control them
- Show **where differentiation is created**  which specific activities make this business unique to buyers
- Describe **key linkages**  pairs of activities that must be coordinated to achieve quality or cost objectives

### Key Cost Drivers (Porter's 10 structural factors)

The most important cost drivers for Uganda/EA SMEs are typically: **scale** (reaching efficient volume), **learning** (cost reduction as cumulative output grows), **location** (labour cost, access to inputs), **discretionary policies** (quality standards, service levels, process choices), and **institutional factors** (regulatory compliance cost: EFRIS, UNBS, NIN/BRN).

**Cross-reference:** `references/value-chain-porter.md` for the full framework including all 10 cost drivers, differentiation/uniqueness drivers, competitive scope analysis, and a Uganda/EA application section with industry-by-industry examples.

## References

- **Procurement and funding approvals as blocking gates (Uganda)**: See `../13-implementation-timeline/references/procurement-and-gating-schedule.md` for treating PPDA procurement approvals (staged evaluation, Contracts Committee award, NOBEB and standstill, Attorney-General clearance, contract signature) and funding releases (commitment-control / quarterly expenditure limits; donor disbursement tranches and conditions precedent) as BLOCKING predecessor milestones in the operating and implementation schedule, with the M&E reporting cycle gating the next tranche/phase. **Read when the operations plan depends on a procured supply, work, or service contract, or on released public or donor funds — procurement and funding gates set when delivery can actually begin. Statutory monetary thresholds must be verified against the current PPDA instrument.**
- **Supplier and operational correspondence standards**: See `../00-plan-assembly/references/commercial-correspondence-ashley.md` for professional letter structure (block style), Incoterms 2000 quick-reference table (EXW/FOB/CIF/DDP and all variants), supplier enquiry and quotation language, order covering letter format, packing instruction standards, advice-of-dispatch wording, complaint letter principles (passive/impersonal language; no fault/blame), credit and open-account request structure, and Uganda/EA application notes (CIF Mombasa, mobile money vs letter of credit, cultural complaint framing)  Source: Ashley (OUP, 2003). **Read when writing the supply chain, procurement, or quality-control subsection, or when describing standard supplier correspondence procedures.**
- **Value chain and competitive advantage**: See `references/value-chain-porter.md` for the full value chain framework (9 activities), value system (supplier/channel/buyer linkages), 10 structural cost drivers, differentiation/uniqueness drivers, competitive scope, and Uganda/EA application notes  from Porter (1985)
- **Product development lifecycle**: See `../03-products-services/references/product-development-lifecycle.md` for VDPD process, prototyping, MVP development, manufacturing considerations, and innovation strategy (incremental vs. radical)  from Bates and Tidd & Bessant
- **Product management frameworks**: See `../03-products-services/references/product-management-frameworks.md` for product scaling strategies (8 approaches), experimentation techniques, and Key Value Areas for operational metrics  from Verwijs et al
- **Business process management**: See `references/business-process-management.md` for BPM lifecycle, Devil's Quadrangle performance trade-offs, value-added analysis, improvement technique wheel (SALT filter), 29 redesign heuristics, process maturity assessment, process metrics (CTE, Little's Law), scope definition, and process landscape mapping  from Dumas et al. (Springer, 2013) and Page (AMACOM, 2015)
- **Hypergrowth operations redesign**: See `references/hypergrowth-operations-algorithm.md` for McNeill's five-step redesign sequence (question, delete, simplify, accelerate, automate last), the whole-customer-experience operating lens, urgency and accountability practices, and dogfooding discipline. **Read when the operations challenge is speed, complexity, or customer friction rather than pure capacity shortage.**
- **Digital operating-model redesign**: See `../book-extractions/rogers-digital-transformation-playbook-extraction.md`, `../book-extractions/molenaar-demand-driven-business-strategy-extraction.md`, and `../meta-digital-transformation/SKILL.md` when deciding whether the real operational move is workflow digitisation, data capture, platform participation, or subscription/service redesign rather than more headcount or paper process.
- **DevOps operating model for software and SaaS businesses**: See `../../book-extractions/devops-operating-model-extraction.md` for CI/CD, release management, observability, incident response, IaC, DevSecOps, PHP/LAMP operations, cloud-native maturity, and business-plan translation of DevOps capabilities. **Read when the business sells software, runs a platform, hosts customer workloads, depends on digital service uptime, or needs a credible technology operations plan.**
- **Uganda operations context**: See `references/uganda-operations-context.md` for Uganda-specific operational infrastructure: power supply and backup (UMEME/UEDCL transition, UGX 720900/kWh grid tariff, generator and solar benchmarks), water supply (NWSC tariffs, borehole costs), Employment Act 2006 provisions (NSSF 15%, leave entitlements, redundancy pay, work permits), logistics and supply chain (Mombasa corridor lead times, SGR, cold chain), UNBS mandatory certification and EFRIS compliance, land tenure types (customary vs. registered), industrial parks (Namanve), and digital payment infrastructure (32M mobile money accounts, WhatsApp Business, EFRIS integration)  from IFC (2022), RSM/Baker Tilly (2025), NRC/Amanya (2025), and World Business Journal (2025)
- **Small business bottleneck analysis, capacity utilisation, asset monetisation**: See `../07-marketing-sales-strategy/references/small-business-unconventional-strategy.md` (Chapter 9) for Kaza's operational efficiency framework
- **Sustainable operations, lean green, and circular economy in Uganda**: See `references/sustainable-operations-framework.md` for the Quadruple Bottom Line operational test, SURF Framework (Sustainability Utilisation of Resources), 8 Lean Green waste types mapped to environmental impact, Industry 4.0 sustainability tools by Uganda SME feasibility, sustainable supply chain 5-question checklist, water and energy management with Uganda costs and payback periods, waste hierarchy with organic valorisation data, and worker wellbeing minimum standards under Employment Act 2006  Source: Waite (Routledge, 2023) and Kumar et al. (CRC, 2025). **Read when writing the sustainability subsection of the operations plan, specifying resource efficiency targets, or incorporating circular economy practices into operations.**
- **Industrial production, inventory, warehousing, MRP, scheduling, facilities, and green manufacturing**: See `../../book-extractions/industrial-production-inventory-planning-extraction.md` for material-requirements planning, master scheduling, safety stock, lot sizing, pegging, factory capacity, setup/changeover, warehouse slotting, material handling, quality traceability, and resource-efficiency metrics. **Read when the business manufactures, processes, warehouses, distributes, exports physical goods, or carries material inventory risk.**
- **Logistics network design, inventory service levels, transportation, carrier/fleet strategy, and trade documentation**: See `../../book-extractions/cltd-logistics-inventory-transportation-extraction.md` for CLTD-derived planning rules covering network design, inventory policy, transportation execution, 3PL/4PL/LLP models, Incoterms/customs controls, reverse logistics, and logistics KPIs. **Read when the business imports, exports, warehouses, distributes, delivers, aggregates agricultural output, operates a fleet, uses carriers, or carries meaningful stockout/backorder risk.**
- **Business process modelling, gap analysis, value proposition, and organisation modelling toolkit**: See `../meta-market-validation/references/business-analysis-techniques-cadle.md` (Chapter 4 tools: 3340) for structured descriptions of Value Proposition Analysis (Tool 33), Value Chain Analysis (Tool 34), Organisation Diagram (Tool 35), Business Event Analysis (Tool 36), Business Process Modelling/Swimlanes (Tool 37), Business Rules Analysis (Tool 38), Decision Tables (Tool 39), and Gap Analysis (Tool 40)  including as-is/to-be methodology, swimlane notation, and Uganda application notes for documenting informal operations  Source: Cadle, Paul & Turner (BCS, 2010). **Read when designing or documenting business processes for the operations plan, especially when formalising a previously undocumented informal business.**

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Process maps, demand profile, capacity, suppliers, controls, service levels, and cost drivers for 08 operations plan | Operations owner, site observation, supplier evidence, and approved model | Yes | If absent, process, capacity, supplier, or control evidence is unavailable, mark the operating claim untested and return the observation or trial needed. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Operations plan with process, capacity, sourcing, control, and contingency design | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 08 operations plan exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 08 operations plan release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Critical-process map, capacity calculation, supplier decision record, and exception/recovery plan | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 08 operations plan decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 08 operations plan review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 08 operations plan, the controlling focus is critical processes, capacity, location, sourcing, quality controls, service levels, contingencies, and operating cost. This skill may analyse and document operations; it may not order equipment, bind suppliers, change production, access live systems, or certify safety without explicit authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 08 operations plan, loss of evidence about critical processes, capacity, location, sourcing, quality controls, service levels, contingencies, and operating cost activates degraded mode. If the controlling 08 operations plan evidence is unavailable, the same boundary applies. When process, capacity, supplier, or control evidence is unavailable, mark the operating claim untested and return the observation or trial needed. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 08 operations plan, planned demand exceeds evidenced capacity or depends on a single unverified supplier| stage volume, add a tested contingency, and reconcile cost and timing before release | The plan promises sales that the operating system cannot deliver reliably |
| For 08 operations plan, A current legal, regulatory, tax, accounting, market, or platform claim controls the 08 operations plan decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 08 operations plan, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete operations plan with process, capacity, sourcing, control, and contingency design, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 08 operations plan decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect process maps, demand profile, capacity, suppliers, controls, service levels, and cost drivers and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce operations plan with process, capacity, sourcing, control, and contingency design with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Operations plan with process, capacity, sourcing, control, and contingency design must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Critical-process map, capacity calculation, supplier decision record, and exception/recovery plan must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 08 operations plan, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 08 operations plan, treating an unavailable process maps, demand profile, capacity, suppliers, controls, service levels, and cost drivers as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing operations plan with process, capacity, sourcing, control, and contingency design that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

Sales assume 200 daily orders while timed packing supports 120. Stage acquisition to 120 and test a second shift before accepting the higher forecast.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 08 operations plan; no local deep-dive reference is declared.
- For 08 operations plan claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.
- Apply the [book-driven commercial system and validation reference](../../meta-strategy/references/book-driven-commercial-system-and-validation.md) when connecting operations to demand, capacity, cash, working capital, service levels, and currentness.

<!-- dual-compat-end -->
