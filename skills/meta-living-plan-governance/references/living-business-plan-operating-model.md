---
source: Cotton (MSPOT), Haines (post-implementation audit), Walling (customer-conversation cadence), engine synthesis
frameworks: [MSPOT, plan-vs-actual variance protocol, decision log, trigger-replan, cadence calendar]
skill: meta-living-plan-governance
cross-reference: [meta-quarterly-gameplan, meta-monitoring-evaluation, meta-board-and-investor-reporting]
---

# Living Business Plan Operating Model

A canonical reference for how every plan in this engine becomes — and stays — a living document. This file is referenced by every new and enhanced skill so that the living-plan discipline is consistent across the catalogue.

## 1. The Six Operating-Model Components

Every plan section must address all six. This is the harness that turns a snapshot document into an operating system.

| # | Component | Question Answered |
|---|---|---|
| 1 | **Data feed** | Which KPI / metric / external signal feeds this section? |
| 2 | **Cadence** | How often is this section reviewed? (weekly / monthly / quarterly / annual / trigger) |
| 3 | **Owner** | Which role on the team maintains it? |
| 4 | **Decision log** | Where do material changes / decisions get recorded with reasoning? |
| 5 | **Variance threshold** | At what plan-vs-actual gap does the section trigger a re-plan? |
| 6 | **Sunset policy** | When is outdated content archived? |

## 2. Cadence Hierarchy

- **Weekly metrics review** — KPI dashboard owner reviews leading indicators, raises flags
- **Monthly Business Review (MBR)** — Department heads + CEO; full operating-metric review; plan-vs-actual on revenue, churn, cash; decisions logged
- **Quarterly Board Review (QBR)** — Board + CEO + executive team; quarter-close metrics, narrative on strategy execution, decisions for next quarter; produces investor update
- **Annual Strategy Refresh** — Full plan review; new MSPOT; refreshed 3-year financials; team offsite; renewed Omissions list
- **Trigger Replan** — Event-driven; not on the calendar

## 3. The Mission / Strategy / Projects / Omissions / Tracking (MSPOT)

Single-page annual artefact (Cotton; HubSpot origin).

```
COMPANY MSPOT — YEAR ____

MISSION:
  [Why we exist. Rarely changes.]

STRATEGY:
  [How we win this year. Refreshed annually.]

PROJECTS:
  1. [Big initiative #1]
  2. [Big initiative #2]
  3. [Big initiative #3]
  4. [Big initiative #4]
  (5. [Optional big initiative #5])

OMISSIONS:
  - [Project / opportunity explicitly NOT funded this year, with one-line reason]
  - [...]
  - [...]

TRACKING:
  Primary KPIs (the dashboard):
    1. ARR — target ___ , review weekly
    2. NRR — target ___ , review monthly
    3. CAC Payback — target ___ , review monthly
    4. Burn Multiple — target ___ , review monthly
    5. Rule of 40 — target ___ , review quarterly
    6. NPS — target ___ , review quarterly
```

The Omissions list is the single highest-leverage discipline in the model. It is also the hardest. Most companies cannot say no.

## 4. The Decision Log Standard

A single canonical decision-log document (Notion / Coda / Confluence / shared doc). Each entry:

```
DECISION-ID: 2026-Q2-014
DATE: 2026-05-11
TITLE: Move enterprise tier from monthly to annual prepayment
ONE-LINE: Switch all enterprise contracts ($50k+ ACV) to annual prepay, with 15% discount incentive.

ALTERNATIVES CONSIDERED:
  A. Keep monthly billing (do-nothing case)
  B. Annual prepay with 15% discount (chosen)
  C. Annual prepay with 20% discount
  D. Quarterly prepay with 7% discount

EVIDENCE:
  - Customer interviews (12 enterprise customers, 9 willing to prepay annually for >10% discount)
  - Working-capital trough modelling: annual prepay reduces month-12 burn by 38%
  - Competitor scan: 4 of 6 named competitors offer annual prepay discount

ASSUMPTIONS:
  - Enterprise customers value 15% discount more than monthly cash flow flexibility
  - No more than 20% will negotiate for additional terms

DECISION-MAKER(S): CEO (final), CFO (sponsor), Head of Sales (executor)

EXPECTED OUTCOME / SUCCESS CRITERIA:
  - 60%+ of new enterprise contracts in next 2 quarters are annual prepay
  - Cash position at end of Q3 is at least UGX X higher than baseline plan
  - No more than 5% logo-churn increase from existing enterprise base

REVIEW DATE: 2026-10-31

OUTCOME (filled at review):
  [To be completed]
```

## 5. Variance Threshold Defaults

(Adjust per plan; defaults below.)

| Metric type | Default variance threshold for replan |
|---|---|
| Revenue (ARR / MRR) | ±15% from plan |
| Cost (OpEx) | ±20% from plan |
| Gross margin | ±5pp from plan |
| Churn (gross, monthly) | ±0.5pp from plan |
| NRR | ±10pp from plan |
| CAC payback | ±30% from plan |
| Cash runway | <6 months remaining (absolute, not %) |
| Burn multiple | >2.5 (absolute) |
| Headcount | ±15% from plan |

When threshold is breached, the variance protocol fires (Section 6).

## 6. The Plan-vs-Actual Variance Protocol

When variance exceeds threshold:

1. **Diagnose** the variance:
   - Execution failure (we did not run the plan)? — fix execution, not plan
   - Assumption failure (the world is different from what we assumed)? — re-plan
   - Both? — both
2. **Trace** the variance through dependent sections (a churn miss propagates: LTV → unit economics → runway → funding ask)
3. **Re-plan** only the affected sections; do not rewrite untouched sections
4. **Log** the variance, diagnosis, change, and decision-maker
5. **Communicate** to the board / investors with diagnosis and remediation
6. **Schedule** a follow-up at the next cadence to verify the remediation worked

## 7. Trigger-Replan Events (canonical list)

Force an immediate re-plan regardless of calendar cadence:

- Founder or C-suite departure
- Loss of customer representing >10% of ARR
- Currency depreciation / appreciation >10% in 30 days
- Regulatory event invalidating a material assumption
- Technology shock (key API deprecated, AI cost shift, security breach)
- Funding round closure
- M&A activity (own acquisition; key competitor acquired)
- Major key-supplier failure (extended cloud outage, payment-gateway suspension)
- Senior-team conflict that affects execution
- New major competitor with materially better economics

## 8. Section Ownership Defaults

| Section | Default owner |
|---|---|
| 01 Exec Summary | CEO |
| 02 Company Overview | CEO / Legal |
| 03 Products | CTO / Head of Product |
| 04 Market | Head of Strategy / Head of Marketing |
| 05 Target Market | Head of GTM / Marketing |
| 06 Competitive | Head of Strategy |
| 07 Marketing/Sales | Head of GTM (or CEO if no GTM head) |
| 08 Operations | COO / CTO |
| 09 Management/Team | CEO / Head of People |
| 10 Financial Projections | CFO (or Finance Lead) |
| 11 Funding Request | CEO + CFO |
| 12 Risk | CFO + COO |
| 13 Implementation Timeline | COO / Head of Product |
| 14 AI Integration | CTO / Head of AI |
| 16 Sustainability | CEO / Head of ESG |

## 9. Sunset / Archive Policy

- Content older than 12 months that has been superseded by 2+ quarterly updates is archived (read-only)
- Annual archive: a snapshot of the plan as it stood on Dec 31 of each year, preserved for institutional memory
- Decision-log entries are never deleted, only marked closed-with-outcome

## 10. Cadence Calendar Template

```
WEEKLY (every Monday 9–10am):
  - KPI dashboard review (Owner: CFO or designated metrics lead)
  - Flag colour: green / amber / red on each top-line metric
  - Decision log: any new entries?

MONTHLY (last Friday of month):
  - MBR — full operating review
  - Plan-vs-actual on revenue, cash, churn, headcount
  - Variance check against thresholds
  - MSPOT projects status
  - Investor update sent within 7 days

QUARTERLY (last week of quarter):
  - QBR — board pack assembled
  - Plan-vs-actual on all sections
  - Decision log review (any decisions due for outcome review?)
  - MSPOT projects: green/amber/red, with replan if needed
  - Customer-conversation digest (Walling cadence: 10+ interviews/month feeding strategy)

ANNUAL (Q4):
  - Annual strategy refresh
  - New MSPOT
  - 3-year financial re-plan
  - Team offsite
  - Renewed Omissions list
  - Archive snapshot of previous year's plan
```

## 11. Africa / Uganda Application Notes

- Sync the cadence calendar to the funder calendar: USAID / FCDO fiscal year (Oct–Sep), African DFI fiscal year (Jul–Jun for IFC; Jan–Dec for AfDB / UDB), corporate budget cycles (Jan–Dec for most East-African corporates).
- Quarterly board pack format: DFIs (UDB, AfDB, IFC) and patient-capital funds (Acumen, FMO, Norfund) expect specific KPI tables — adopt theirs early.
- Decision log should also capture **political-economy context** — many African enterprise decisions are co-determined by stakeholder politics; this knowledge dies with founder turnover unless logged.
- Trigger-replan additions for Africa: power outages affecting infrastructure SLA, internet undersea-cable cut, Central-Bank policy change affecting payment rails, NDA-level political event affecting public-sector buyer.
- MSPOT discipline is disproportionately powerful in African contexts because founder-led companies tend to chase every opportunity and rarely have an explicit "no" list. The Omissions section often unlocks more than the Projects section.
