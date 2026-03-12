---
name: operations-plan
description: Generate the operations plan section covering business processes, supply chain, facilities, technology infrastructure, quality control, staffing requirements, and key operational metrics. Shows how the business runs day-to-day. Incorporates Dumas et al.'s BPM lifecycle and Devil's Quadrangle trade-offs, Page's process redesign techniques, and Kaza's small business operational efficiency framework (bottleneck identification and subordination, capacity utilisation optimisation, owner-as-bottleneck diagnosis, and the asset utilisation principle — finding revenue-generating uses for underutilised capacity during off-peak periods).
---

# Operations Plan Skill

Generate a detailed operations plan that demonstrates the business can deliver on its promises efficiently and at scale.

## What to Generate

### Required Elements

1. **Business model operations** — How the business creates and delivers value
2. **Key processes** — Core workflows from order to delivery
3. **Supply chain** — Suppliers, procurement, inventory management
4. **Facilities and equipment** — Physical locations, machinery, office space
5. **Technology infrastructure** — Systems, software, platforms, integrations
6. **Quality control** — Standards, testing, compliance procedures
7. **Staffing and HR** — Headcount, roles, hiring timeline
8. **Key partnerships** — Outsourced functions, strategic alliances
9. **Operational KPIs** — Metrics for measuring operational health
10. **Scalability plan** — How operations scale with growth

### Process Documentation Format

For each core process:

```
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
- Cost per unit produced/delivered

### Business Process Management Framework

For each core operational process, apply the BPM lifecycle (Dumas et al., 2013):

1. **Identify** — Map all processes using the process landscape model (management / core / support)
2. **Document** — Create as-is process models showing current workflows
3. **Analyse** — Classify activities as value-adding (VA), business-value-adding (BVA), or non-value-adding (NVA)
4. **Redesign** — Apply improvement techniques in order: eliminate bureaucracy → eliminate duplication → simplify → reduce cycle time → automate last (Page, 2015)
5. **Implement** — Execute changes with proper change management
6. **Monitor** — Track performance using the Devil's Quadrangle dimensions

### Process Performance Trade-offs (Devil's Quadrangle)

Every process optimisation involves trade-offs across four dimensions — time, cost, quality, and flexibility. The business strategy determines which to prioritise:

- **Cost leadership** → optimise for cost reduction (accept longer times, less flexibility)
- **Differentiation** → optimise for quality and flexibility (accept higher costs)
- **Speed-to-market** → optimise for time reduction (accept higher costs)

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

## Quality Criteria

- Processes are specific enough to execute, not just described at a high level
- Supply chain risks are identified with mitigation plans
- Technology choices are justified (not just trendy)
- Scalability plan shows how operations handle 2x, 5x, 10x growth
- Staffing plan aligns with financial projections in section 10

### Small Business Operational Efficiency (Kaza)

For SME operations plans, apply the bottleneck framework from Kaza's analysis of 20,000+ small businesses:

**Step 1 — Identify the bottleneck:**
Ask: When the business is at capacity, where does work stack up? What one step, if faster, would allow the business to serve more customers? Is the *owner* the bottleneck — the person without whom nothing moves?

**Step 2 — Subordinate everything else:**
Once the bottleneck is identified, every other part of the operation should be structured to keep the bottleneck running at optimal capacity. Do not invest in non-bottleneck improvements — they will not increase overall output.

**Step 3 — Optimise utilisation (not 100%):**
Sustained 100% utilisation leads to quality degradation and staff burnout. Target optimal utilisation — high enough to be profitable, low enough to maintain quality and service standards.

**Step 4 — Monetise underutilised assets:**
Identify assets (space, equipment, staff time) that are underutilised during off-peak hours and create revenue streams from them. Examples:
- A restaurant's dining space used for morning business meetings
- A salon using after-hours capacity for evening workshops
- A logistics vehicle used for delivery services on return journeys

**Owner-as-bottleneck diagnostic** — common in Ugandan SMEs:

| Symptom | Underlying issue | Solution |
|---|---|---|
| Nothing progresses when owner travels | All decisions centralised | Document decisions; delegate authority |
| Owner works 12+ hours daily but growth is flat | Owner is in the bottleneck role | Hire or train to relieve the constraint |
| Business cannot quote without owner | No pricing authority delegated | Create pricing guidelines; train staff |
| Customer service depends on owner's relationships | Proximity not systematised | Build CRM; train staff on relationship protocols |

**Capacity utilisation planning template:**

```
Peak capacity: [units/clients per day at maximum]
Target utilisation rate: [70–85% for most businesses]
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
1. Inbound Logistics — receiving, storing, distributing inputs
2. Operations — transforming inputs into the final product
3. Outbound Logistics — collecting, storing, distributing finished goods
4. Marketing & Sales — enabling buyers to purchase and inducing them to do so
5. Service — maintaining or enhancing product value after sale

**Support activities** (enabling the primary activities):
6. Procurement — purchasing inputs used across all activities
7. Technology Development — know-how and procedures embedded in each activity
8. Human Resource Management — recruiting, training, compensation firmwide
9. Firm Infrastructure — general management, finance, accounting, legal, quality

### Applying Value Chain to the Operations Plan

In the operations plan, use the value chain to:
- Identify **which primary activities create the most value** and deserve the most operational investment
- Explain **which activities are the primary cost drivers** — and how management will control them
- Show **where differentiation is created** — which specific activities make this business unique to buyers
- Describe **key linkages** — pairs of activities that must be coordinated to achieve quality or cost objectives

### Key Cost Drivers (Porter's 10 structural factors)

The most important cost drivers for Uganda/EA SMEs are typically: **scale** (reaching efficient volume), **learning** (cost reduction as cumulative output grows), **location** (labour cost, access to inputs), **discretionary policies** (quality standards, service levels, process choices), and **institutional factors** (regulatory compliance cost: EFRIS, UNBS, NIN/BRN).

**Cross-reference:** `references/value-chain-porter.md` for the full framework including all 10 cost drivers, differentiation/uniqueness drivers, competitive scope analysis, and a Uganda/EA application section with industry-by-industry examples.

## References

- **Value chain and competitive advantage**: See `references/value-chain-porter.md` for the full value chain framework (9 activities), value system (supplier/channel/buyer linkages), 10 structural cost drivers, differentiation/uniqueness drivers, competitive scope, and Uganda/EA application notes — from Porter (1985)
- **Product development lifecycle**: See `../03-products-services/references/product-development-lifecycle.md` for VDPD process, prototyping, MVP development, manufacturing considerations, and innovation strategy (incremental vs. radical) — from Bates and Tidd & Bessant
- **Product management frameworks**: See `../03-products-services/references/product-management-frameworks.md` for product scaling strategies (8 approaches), experimentation techniques, and Key Value Areas for operational metrics — from Verwijs et al
- **Business process management**: See `references/business-process-management.md` for BPM lifecycle, Devil's Quadrangle performance trade-offs, value-added analysis, improvement technique wheel (SALT filter), 29 redesign heuristics, process maturity assessment, process metrics (CTE, Little's Law), scope definition, and process landscape mapping — from Dumas et al. (Springer, 2013) and Page (AMACOM, 2015)
- **Uganda operations context**: See `references/uganda-operations-context.md` for Uganda-specific operational infrastructure: power supply and backup (UMEME/UEDCL transition, UGX 720–900/kWh grid tariff, generator and solar benchmarks), water supply (NWSC tariffs, borehole costs), Employment Act 2006 provisions (NSSF 15%, leave entitlements, redundancy pay, work permits), logistics and supply chain (Mombasa corridor lead times, SGR, cold chain), UNBS mandatory certification and EFRIS compliance, land tenure types (customary vs. registered), industrial parks (Namanve), and digital payment infrastructure (32M mobile money accounts, WhatsApp Business, EFRIS integration) — from IFC (2022), RSM/Baker Tilly (2025), NRC/Amanya (2025), and World Business Journal (2025)
- **Small business bottleneck analysis, capacity utilisation, asset monetisation**: See `../07-marketing-sales-strategy/references/small-business-unconventional-strategy.md` (Chapter 9) for Kaza's operational efficiency framework
- **Sustainable operations, lean green, and circular economy in Uganda**: See `references/sustainable-operations-framework.md` for the Quadruple Bottom Line operational test, SURF Framework (Sustainability Utilisation of Resources), 8 Lean Green waste types mapped to environmental impact, Industry 4.0 sustainability tools by Uganda SME feasibility, sustainable supply chain 5-question checklist, water and energy management with Uganda costs and payback periods, waste hierarchy with organic valorisation data, and worker wellbeing minimum standards under Employment Act 2006 — Source: Waite (Routledge, 2023) and Kumar et al. (CRC, 2025). **Read when writing the sustainability subsection of the operations plan, specifying resource efficiency targets, or incorporating circular economy practices into operations.**
