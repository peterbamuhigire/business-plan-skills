---
name: meta-monitoring-evaluation
description: Use when translating a completed or near-complete plan into execution monitoring. Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Monitoring & Evaluation (M&E) Meta-Skill

## Overview

Use this meta-skill after the plan is built to convert it into a measurable management system. It defines KPIs, reporting rhythms, ownership, and review structures so the plan can be run, not just written.

## Use When

- Use when translating a completed or near-complete plan into execution monitoring.
- Use when funders, management, or boards need KPI dashboards and reporting logic.
- Use when accountability and review cadence matter as much as strategy design.

## Do Not Use When

- Do not use before the strategy, operations, and financial model are stable enough to measure.
- Do not create KPI lists with no clear strategic owner or review cadence.
- Do not confuse monitoring with retrospective narrative reporting only.


- For `meta-monitoring-evaluation`, route to the relevant plan-section skill instead when the request is section drafting rather than cross-section analysis.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Monitoring Evaluation brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Completed or near-complete plan sections
- Strategic goals, operating model, and financial targets
- Audience requirements for reporting or accountability
- Any existing scorecards, templates, or funder indicators

## Workflow

1. Identify the decisions the monitoring system must support.
2. Build the scorecard and KPI structure from strategy, not from random metrics.
3. Assign ownership, frequency, thresholds, and review cadence.
4. Reconcile indicators with the plan's financial, operational, and impact logic.
5. Make reporting usable for managers, funders, and accountability structures.
6. Flag metrics that are impossible to measure or easy to game.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the monitoring and evaluation framework and that the decision concerns which indicators and review cadence can govern implementation.
- **Stop condition:** halt the affected conclusion if required evidence is missing (theory of change, baseline, owners, and data sources) or if the work could lead to this identified risk: selecting impressive indicators that nobody can collect or act on.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- KPIs reflect strategy and operating reality.
- Metrics, thresholds, and owners are clear enough to manage.
- Reporting cadence matches the business rhythm.
- The system can be used without constant reinterpretation.

## Anti-Patterns

- KPI dashboards disconnected from strategy.
- Too many indicators and no real decision logic.
- Measures with no owner, no cadence, or no data source.
- Reporting frameworks that conflict with financial or operational definitions.
- Treating a generic monitoring evaluation template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta monitoring evaluation. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Monitoring Evaluation deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A measurable M&E framework, dashboard, and review structure
- KPI ownership and reporting cadence
- Any monitoring gaps or data-collection risks


Convert the business plan from a static document into an active management tool with measurable KPIs, reporting cadences, and accountability structures.

## When to Use

Invoke AFTER the plan is complete and scored. This skill creates the operational infrastructure for plan execution tracking.

## What to Generate

### 1. Balanced Scorecard and KPI Dashboard

Build the dashboard using Balanced Scorecard logic first, then populate with KPIs. Every KPI should sit inside one of four perspectives:

- **Financial** - what success looks like to owners, lenders, and investors
- **Customer / Market** - what target customers must experience
- **Internal Process** - what operations must excel at
- **Learning / Capability** - what people, systems, and capabilities must improve

Do not start with a random KPI list. Start with strategy, then cascade measures.

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

~~~text
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
~~~

### Strategy Map Requirement

Before locking the KPI dashboard, produce a one-page strategy map:

1. Learning / capability enablers
2. Internal process improvements those enablers unlock
3. Customer outcomes those process improvements should create
4. Financial outcomes expected from those customer outcomes

Each KPI should have a visible causal path to the next perspective.

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
2. Variance analysis  what missed target and why (15 min)
3. Milestone progress update (10 min)
4. Decisions and resource allocation (10 min)
5. Action items for next month (10 min)

### 4. Plan vs. Actual Tracking

| Metric | Plan | Actual | Variance | Variance % | Status |
|--------|------|--------|----------|------------|--------|
| Revenue | $X | $X | +/- $X | +/- X% | On/Off track |

### 5. Early Warning System

Define triggers that signal the plan is going off track:

~~~text
GREEN: All KPIs within 10% of target
AMBER: 1-2 KPIs off by 10-25%, corrective action initiated
RED: Any KPI off by >25% or cash runway < 3 months
~~~

### 6. Continuous Improvement Cycle

Integrate the Evaluate-Test-Assess-Execute cycle for ongoing process improvement (Page, 2015):

**Evaluate** (spend majority of time here):
- Review customer/client needs against scope definition
- Compare metrics to baseline  identify trends
- Verify process workers follow documented processes
- Assess whether internal controls eliminate errors
- Evaluate third-party vendor/supplier performance

**Test**  Implement changes on a small scale to validate before full rollout

**Assess**  Review test data, benchmark against industry standards, decide whether to proceed

**Execute**  Deploy across the organisation with communication, training, and updated impact analysis

### Continuous Improvement Schedule Template

| Business Process | Review Metrics | Client Needs | Internal Controls | Process Compliance | Vendor Evaluation |
|---|---|---|---|---|---|
| [Process A] | Monthly | Quarterly | Monthly | Quarterly | Annually |

### Process Metrics Framework (Three Perspectives)

Complement financial/customer/operational KPIs with process-specific metrics (Page, 2015):

- **Effectiveness**  Does the process produce desired results? (quality, customer satisfaction)
- **Efficiency**  Does it minimise resources and cycle time? (cost per transaction, CTE)
- **Adaptability**  Can it respond to changing needs? (time to implement changes, % non-standard cases handled)

Each process should have at least one metric from each perspective.

### KPI Design Rules

Apply these rules before approving any KPI set:

- pair **leading indicators** with **lagging indicators**
- keep each KPI SMART and decision-relevant
- avoid vanity metrics with no owner or threshold
- define the exact data source before using the KPI
- separate outcome KPIs from activity KPIs
- limit the core scorecard to the few measures that management will actually review

Use a practical default:

- 3-5 KPIs per Balanced Scorecard perspective
- 12-16 core KPIs total
- more detail in supporting reports, not the headline dashboard

## Generation Process

1. Identify the strategic objective and funding context
2. Build the strategy map across the four Balanced Scorecard perspectives
3. Extract key metrics from plan sections 04, 07, 08, 10, 13, and 16
4. Define 12-16 core KPIs plus support metrics
5. Set baseline, target, threshold, frequency, and owner for every KPI
6. Pair leading and lagging indicators for each major objective
7. Build reporting templates for each cadence
8. Design review meeting structure and escalation paths
9. Create the early warning system with trigger thresholds

## Funder Reporting Obligations

The M&E framework must incorporate reporting obligations tied to the funding source. These are contractual, not optional.

**For bank loans (commercial banks, UDB, ACF):** Lenders attach performance covenants to loans. Typical covenant monitoring requirements include:
- DSCR  1.25x  monitored quarterly; report to bank annually or upon request
- Current ratio  1.0x  monitored quarterly
- Quarterly management accounts (unaudited) to lending institution
- Annual audited accounts within 6 months of financial year end
- Insurance certificates on pledged collateral  renewed annually
- NSSF and URA compliance certificates upon request

**For development partner grants:** Quarterly narrative reports + quarterly financial reports against approved budget are typically required. Report formats vary by donor but generally include: activities completed, outputs achieved (with beneficiary counts disaggregated by gender), budget vs. actual variance explanation, risks encountered, and plans for next quarter. See `references/funder-reporting-requirements.md` for standard templates.

**For impact investors:** Double-bottom-line KPIs  financial performance PLUS social/environmental indicators (jobs created, women employed, smallholders reached, CO2 reduced). See `references/funder-reporting-requirements.md` for sector-specific impact metrics.

Identify the funder type BEFORE designing the M&E framework, and embed the relevant reporting obligations into the review cadence.

## Quality Criteria

- KPIs are specific and measurable (not "improve customer satisfaction")
- Scorecard begins with strategy map logic, not a disconnected metric list
- Targets align with financial projections in section 10
- Reporting cadence is practical for the team size
- Early warning triggers are actionable
- Every KPI has a clear owner
- Leading and lagging indicators are balanced
- Process metrics cover all three perspectives: effectiveness, efficiency, and adaptability (Page, 2015)
- Continuous improvement cycle is scheduled with specific frequencies per process
- Funder reporting obligations are integrated into the review calendar

## References

- `../../book-extractions/data-analytics-business-planning-extraction.md`  Use when KPI dashboards, AI analytics, forecasts, scenario analysis, or data-quality controls are part of the execution monitoring system.
- `references/balanced-scorecard-kpi.md` - Balanced Scorecard perspectives, strategy mapping, KPI-cascade logic, and leading/lagging-indicator design from Kaplan, Krause, and Arora
- `references/funder-reporting-requirements.md` - Commercial bank covenant monitoring (DSCR, current ratio, insurance), mandatory bank reporting schedule, UDB and ACF reporting (ESMP semi-annual monitoring report template), development partner grant quarterly narrative and financial report templates, impact investor double-bottom-line KPIs by sector (agriculture, clean energy, education, health, housing, financial inclusion), Government of Uganda annual filing calendar
- `meta-sustainability/references/sustainability-indicators-measurement.md`  Six indicator types (descriptive/performance/efficiency/policy effectiveness/welfare/sentinel), DPSIR framework with Uganda examples, composite indices, 5-step KPI-building process with common failure modes, 8-row minimum viable KPI set for Uganda SMEs, monitoring system design, and external audit requirements for DFI loans >UGX 200M  Source: Hak, Moldan & Dahl (SCOPE/Island Press, 2007). **Read when designing the sustainability KPI dashboard and embedding environmental/social indicators into the M&E framework.**
- `16-sustainability-strategy/SKILL.md`  Sustainability KPI dashboard (7-row format with baseline, Year 1 and Year 3 targets); sustainability KPIs must be integrated into the M&E framework alongside financial KPIs

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Monitoring and evaluation framework decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to selecting impressive indicators that nobody can collect or act on. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the monitoring and evaluation framework; drafting the indicator register and reporting templates is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If theory of change, baseline, owners, and data sources cannot be obtained, return a qualified monitoring and evaluation framework covering only the checks that remain supportable. Leave this decision unresolved: which indicators and review cadence can govern implementation. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which indicators and review cadence can govern implementation | Record the conclusion, source trail, owner, and review trigger in the monitoring and evaluation framework. | Risk of selecting impressive indicators that nobody can collect or act on |
| Material evidence conflicts or remains uncertain | Pilot the indicator with its actual owner and source, rejecting it if collection cost or ambiguity prevents a timely management response. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: theory of change, baseline, owners, and data sources | Mark the decision on which indicators and review cadence can govern implementation `not assessed` in the monitoring and evaluation framework, and send it to the M&E lead and programme owner. | Otherwise, the work risks selecting impressive indicators that nobody can collect or act on |

## Quality Standards


Accept the monitoring and evaluation framework only when evidence is sufficient for this decision: which indicators and review cadence can govern implementation. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of selecting impressive indicators that nobody can collect or act on.

## Worked Example


A jobs programme proposes an indicator that requires records no partner collects. Replace it with a sourceable measure, assign the owner and cadence, and document what management decision it will trigger.

<!-- dual-compat-end -->
