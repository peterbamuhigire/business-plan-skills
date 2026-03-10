---
name: meta-monitoring-evaluation
description: Operational meta-skill that converts the business plan into a living Monitoring & Evaluation (M&E) framework. Generates KPI dashboards, reporting templates, review cadences, and performance tracking systems. Ensures the plan does not gather dust after funding.
---

# Monitoring & Evaluation (M&E) Meta-Skill

Convert the business plan from a static document into an active management tool with measurable KPIs, reporting cadences, and accountability structures.

## When to Use

Invoke AFTER the plan is complete and scored. This skill creates the operational infrastructure for plan execution tracking.

## What to Generate

### 1. KPI Dashboard

Define KPIs for each business function:

**Financial KPIs**
- Monthly revenue / MRR
- Gross margin %
- Net burn rate
- Cash runway (months)
- Revenue growth rate (MoM)

**Customer KPIs**
- New customers acquired
- Customer acquisition cost (CAC)
- Customer lifetime value (CLV)
- Churn rate
- Net Promoter Score (NPS)

**Operational KPIs**
- Fulfilment rate / delivery time
- Product defect rate
- Employee productivity
- Uptime / availability

**Marketing KPIs**
- Lead conversion rate
- Cost per lead
- Marketing ROI by channel
- Website traffic / engagement

### KPI Definition Template

```
KPI: [Name]
Category: [Financial / Customer / Operational / Marketing]
Definition: [Exactly what is measured]
Formula: [How it is calculated]
Data source: [Where the data comes from]
Frequency: [Daily / Weekly / Monthly / Quarterly]
Target: [Specific target value]
Threshold: [Minimum acceptable value]
Owner: [Who is responsible]
Action if below threshold: [What to do]
```

### 2. Reporting Framework

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Flash report | Weekly | Leadership | Top 5 KPIs, blockers, decisions needed |
| Monthly review | Monthly | Management | Full KPI dashboard, variance analysis |
| Board report | Quarterly | Board/investors | Financial performance, milestones, outlook |
| Annual review | Annually | All stakeholders | Full plan vs. actual, strategy refresh |

### 3. Review Meeting Structure

**Monthly review agenda (60 minutes):**
1. KPI dashboard review (15 min)
2. Variance analysis — what missed target and why (15 min)
3. Milestone progress update (10 min)
4. Decisions and resource allocation (10 min)
5. Action items for next month (10 min)

### 4. Plan vs. Actual Tracking

| Metric | Plan | Actual | Variance | Variance % | Status |
|--------|------|--------|----------|------------|--------|
| Revenue | $X | $X | +/- $X | +/- X% | On/Off track |

### 5. Early Warning System

Define triggers that signal the plan is going off track:

```
GREEN: All KPIs within 10% of target
AMBER: 1-2 KPIs off by 10-25%, corrective action initiated
RED: Any KPI off by >25% or cash runway < 3 months
```

### 6. Continuous Improvement Cycle

Integrate the Evaluate-Test-Assess-Execute cycle for ongoing process improvement (Page, 2015):

**Evaluate** (spend majority of time here):
- Review customer/client needs against scope definition
- Compare metrics to baseline — identify trends
- Verify process workers follow documented processes
- Assess whether internal controls eliminate errors
- Evaluate third-party vendor/supplier performance

**Test** — Implement changes on a small scale to validate before full rollout

**Assess** — Review test data, benchmark against industry standards, decide whether to proceed

**Execute** — Deploy across the organisation with communication, training, and updated impact analysis

### Continuous Improvement Schedule Template

| Business Process | Review Metrics | Client Needs | Internal Controls | Process Compliance | Vendor Evaluation |
|---|---|---|---|---|---|
| [Process A] | Monthly | Quarterly | Monthly | Quarterly | Annually |

### Process Metrics Framework (Three Perspectives)

Complement financial/customer/operational KPIs with process-specific metrics (Page, 2015):

- **Effectiveness** — Does the process produce desired results? (quality, customer satisfaction)
- **Efficiency** — Does it minimise resources and cycle time? (cost per transaction, CTE)
- **Adaptability** — Can it respond to changing needs? (time to implement changes, % non-standard cases handled)

Each process should have at least one metric from each perspective.

## Generation Process

1. Extract key metrics from all plan sections (04, 07, 08, 10, 13)
2. Define 15-20 KPIs across all business functions
3. Set targets aligned with financial projections
4. Build reporting templates for each cadence
5. Design review meeting structure
6. Create early warning system with trigger thresholds
7. Assign ownership for every KPI

## Funder Reporting Obligations

The M&E framework must incorporate reporting obligations tied to the funding source. These are contractual, not optional.

**For bank loans (commercial banks, UDB, ACF):** Lenders attach performance covenants to loans. Typical covenant monitoring requirements include:
- DSCR ≥ 1.25x — monitored quarterly; report to bank annually or upon request
- Current ratio ≥ 1.0x — monitored quarterly
- Quarterly management accounts (unaudited) to lending institution
- Annual audited accounts within 6 months of financial year end
- Insurance certificates on pledged collateral — renewed annually
- NSSF and URA compliance certificates upon request

**For development partner grants:** Quarterly narrative reports + quarterly financial reports against approved budget are typically required. Report formats vary by donor but generally include: activities completed, outputs achieved (with beneficiary counts disaggregated by gender), budget vs. actual variance explanation, risks encountered, and plans for next quarter. See `references/funder-reporting-requirements.md` for standard templates.

**For impact investors:** Double-bottom-line KPIs — financial performance PLUS social/environmental indicators (jobs created, women employed, smallholders reached, CO₂ reduced). See `references/funder-reporting-requirements.md` for sector-specific impact metrics.

Identify the funder type BEFORE designing the M&E framework, and embed the relevant reporting obligations into the review cadence.

## Quality Criteria

- KPIs are specific and measurable (not "improve customer satisfaction")
- Targets align with financial projections in section 10
- Reporting cadence is practical for the team size
- Early warning triggers are actionable
- Every KPI has a clear owner
- Process metrics cover all three perspectives: effectiveness, efficiency, and adaptability (Page, 2015)
- Continuous improvement cycle is scheduled with specific frequencies per process
- Funder reporting obligations are integrated into the review calendar

## References

- `references/funder-reporting-requirements.md` — Commercial bank covenant monitoring (DSCR, current ratio, insurance), mandatory bank reporting schedule, UDB and ACF reporting (ESMP semi-annual monitoring report template), development partner grant quarterly narrative and financial report templates, impact investor double-bottom-line KPIs by sector (agriculture, clean energy, education, health, housing, financial inclusion), Government of Uganda annual filing calendar
