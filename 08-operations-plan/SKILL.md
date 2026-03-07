---
name: operations-plan
description: Generate the operations plan section covering business processes, supply chain, facilities, technology infrastructure, quality control, staffing requirements, and key operational metrics. Shows how the business runs day-to-day.
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

## References

- **Product development lifecycle**: See `../03-products-services/references/product-development-lifecycle.md` for VDPD process, prototyping, MVP development, manufacturing considerations, and innovation strategy (incremental vs. radical) — from Bates and Tidd & Bessant
- **Product management frameworks**: See `../03-products-services/references/product-management-frameworks.md` for product scaling strategies (8 approaches), experimentation techniques, and Key Value Areas for operational metrics — from Verwijs et al
- **Business process management**: See `references/business-process-management.md` for BPM lifecycle, Devil's Quadrangle performance trade-offs, value-added analysis, improvement technique wheel (SALT filter), 29 redesign heuristics, process maturity assessment, process metrics (CTE, Little's Law), scope definition, and process landscape mapping — from Dumas et al. (Springer, 2013) and Page (AMACOM, 2015)
