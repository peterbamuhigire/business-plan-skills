# Process Costing and Feasibility Analysis

Reference content consolidated from Page (2015) *The Power of Business Process Improvement* and Dennis, Wixom & Tegarden (2021) *Systems Analysis and Design: An Object-Oriented Approach with UML*.

---

## FTE Calculation (Page, 2015)

### Adjusted Annual Hours

Before costing any process, calculate the actual available working hours per employee:

```
Adjusted Annual Hours = 2,080 − Vacation Hours − Sick Hours − Holiday Hours

Example (Uganda context):
  Base hours:        2,080 (40 hrs/week × 52 weeks)
  Annual leave:      −168  (21 days × 8 hrs)
  Sick leave:        − 40  (5 days × 8 hrs)
  Public holidays:   − 80  (10 days × 8 hrs)
  ─────────────────────────
  Adjusted hours:   1,792
```

### FTE Requirement

```
FTE = Total Annual Process Hours ÷ Adjusted Annual Hours

Example:
  A process requires 5,376 hours per year
  FTE = 5,376 ÷ 1,792 = 3.0 FTEs needed
```

This provides a defensible, bottom-up basis for staffing projections in financial plans — far more credible to investors than simply estimating headcount.

---

## Process Cost Structure (Page, 2015)

### Three Cost Components

Every process cost comprises three elements:

#### 1. People Cost

```
People Cost = (Annual Salary × FTE) × (1 + Employee Benefit Rate)

Example:
  Annual salary:       UGX 18,000,000
  FTE:                 3.0
  Benefit rate:        25% (NSSF, medical, etc.)
  People Cost = (18,000,000 × 3.0) × 1.25 = UGX 67,500,000
```

#### 2. Tool Cost

```
Tool Cost = Annual Tool/Licence Cost × FTE

Example:
  Software licence:    UGX 1,500,000/year per user
  FTE:                 3.0
  Tool Cost = 1,500,000 × 3.0 = UGX 4,500,000
```

#### 3. Overhead Cost

```
Overhead Cost = People Cost × Overhead Rate

Example:
  People Cost:         UGX 67,500,000
  Overhead rate:       30% (rent, utilities, admin allocated)
  Overhead Cost = 67,500,000 × 0.30 = UGX 20,250,000
```

### Total Process Cost

```
Total Process Cost = People Cost + Tool Cost + Overhead Cost

Example:
  67,500,000 + 4,500,000 + 20,250,000 = UGX 92,250,000/year
```

### Cost per Transaction

```
Cost per Transaction = Total Process Cost ÷ Annual Volume

Example:
  Total cost:          UGX 92,250,000
  Annual transactions: 12,000
  Cost per transaction = UGX 7,688
```

### Per-Minute Costing (Activity-Level)

For detailed activity-level costing:

```
Cost per Minute = Annual Salary ÷ Adjusted Annual Hours ÷ 60

Example:
  UGX 18,000,000 ÷ 1,792 ÷ 60 = UGX 167/minute

Activity cost = Cost per Minute × Activity Duration (minutes) × Annual Volume
```

### Hard vs Soft Cost Savings

When projecting savings from process improvements:

| Type | Definition | Treatment in Projections |
|---|---|---|
| **Hard savings** | Actual cash eliminated from the budget (headcount reduction, cancelled licences, reduced material costs) | Include in financial projections |
| **Soft savings** | Time freed up but not eliminated from budget (staff reassigned, capacity created) | Note as operational benefit but do NOT include as cost reduction in P&L |

Investors and lenders value hard savings. Soft savings demonstrate operational improvement but should be presented separately.

---

## Feasibility Analysis Framework (Dennis et al., 2021)

### Three Dimensions

Every significant investment (technology, new facility, expansion) should be evaluated across three feasibility dimensions:

#### 1. Technical Feasibility

Can the organisation build or deploy this solution?

| Factor | Assessment Questions |
|---|---|
| **Familiarity with technology** | Has the team used this technology before? |
| **Project size** | How large/complex is the implementation? |
| **Compatibility** | Does it integrate with existing systems? |
| **Technology risk** | Is the technology proven or experimental? |

Rate each factor Low/Medium/High risk. High risk in any factor requires mitigation plans.

#### 2. Economic Feasibility

Should the organisation invest? Follow the 7-step cost-benefit analysis:

1. Identify all costs (development and ongoing)
2. Identify all benefits (tangible and intangible)
3. Determine cash flows for each year
4. Assess risks to costs and benefits
5. Calculate NPV, ROI, and break-even
6. Determine intangible value
7. Make recommendation

#### 3. Organisational Feasibility

Will the people adopt and support it?

| Factor | Assessment Questions |
|---|---|
| **Strategic alignment** | Does this support the organisation's strategy? |
| **Champion** | Is there a senior sponsor driving adoption? |
| **Stakeholder analysis** | Who gains, who loses, who resists? |
| **User readiness** | Do staff have skills and willingness to adopt? |
| **Change management** | What training and support is needed? |

---

## Cost-Benefit Analysis Spreadsheet (Dennis et al., 2021)

### Standard Format for 5-Year Projections

```
                        Year 0    Year 1    Year 2    Year 3    Year 4    Year 5
BENEFITS
  Tangible benefits        —      xxx       xxx       xxx       xxx       xxx
  Intangible benefits      —      (note)    (note)    (note)    (note)    (note)
  Total Benefits           —      xxx       xxx       xxx       xxx       xxx

DEVELOPMENT COSTS
  Hardware/equipment     xxx        —         —         —         —         —
  Software/licences      xxx        —         —         —         —         —
  Labour (dev team)      xxx        —         —         —         —         —
  Training               xxx        —         —         —         —         —
  Other development      xxx        —         —         —         —         —
  Total Development      xxx        —         —         —         —         —

OPERATIONAL COSTS
  Maintenance              —      xxx       xxx       xxx       xxx       xxx
  Licences/subscriptions   —      xxx       xxx       xxx       xxx       xxx
  Staff (ongoing)          —      xxx       xxx       xxx       xxx       xxx
  Other operational        —      xxx       xxx       xxx       xxx       xxx
  Total Operational        —      xxx       xxx       xxx       xxx       xxx

NET CASH FLOW          (xxx)      xxx       xxx       xxx       xxx       xxx

DISCOUNT FACTOR         1.00     0.909     0.826     0.751     0.683     0.621
  (at 10% discount rate)

NPV of Cash Flow       (xxx)      xxx       xxx       xxx       xxx       xxx
Cumulative NPV         (xxx)      xxx       xxx       xxx       xxx       xxx

ROI = Total Benefits ÷ Total Costs × 100%
Break-even = Year where Cumulative NPV turns positive
```

### Key Financial Metrics

| Metric | Formula | Use |
|---|---|---|
| **NPV** | Sum of discounted cash flows | Overall value of investment |
| **ROI** | (Total Benefits − Total Costs) ÷ Total Costs × 100% | Return on investment |
| **Break-even** | Point where cumulative NPV ≥ 0 | Time to recover investment |
| **Payback period** | Time until cumulative undiscounted cash flow ≥ 0 | Simple recovery period |

---

## Alternative Matrix (Dennis et al., 2021)

### Weighted Scoring for Investment Decisions

When choosing between alternatives (e.g., build vs. buy, vendor A vs. vendor B):

```
                    Weight    Option A    Option B    Option C
TECHNICAL
  Familiarity        15%       4 (0.60)    3 (0.45)    5 (0.75)
  Compatibility      10%       3 (0.30)    4 (0.40)    4 (0.40)
  Risk               10%       4 (0.40)    2 (0.20)    3 (0.30)

ECONOMIC
  NPV                25%       5 (1.25)    4 (1.00)    3 (0.75)
  ROI                15%       4 (0.60)    4 (0.60)    3 (0.45)

ORGANISATIONAL
  Strategic fit       15%       4 (0.60)    3 (0.45)    5 (0.75)
  User readiness      10%       3 (0.30)    5 (0.50)    2 (0.20)

TOTAL               100%       4.05        3.60        3.60

Scoring: 1 = Very poor, 2 = Poor, 3 = Adequate, 4 = Good, 5 = Excellent
```

This structured approach demonstrates rigorous decision-making to investors and lenders.

---

## Application in Financial Projections

### Staffing Costs

Use FTE calculations to build bottom-up staffing projections:

1. List each core process from the operations plan
2. Estimate annual hours per process
3. Calculate FTEs required
4. Apply salary, benefits, and overhead rates
5. Project growth in process volume → growth in FTEs → growth in staffing costs

### Technology Investments

Apply the three-dimensional feasibility framework for any significant technology spend:

1. Demonstrate technical feasibility (can we do it?)
2. Present economic feasibility (NPV, ROI, break-even)
3. Address organisational feasibility (will it be adopted?)

### Process Improvement ROI

When projecting savings from operational improvements:

1. Calculate current cost per transaction
2. Estimate improved cost per transaction after redesign
3. Multiply saving per transaction × annual volume = annual saving
4. Separate hard savings (include in P&L) from soft savings (note separately)
5. Compare improvement costs against benefits using the CBA spreadsheet

---

## Citations

- Page, S. (2015) *The Power of Business Process Improvement: 10 Simple Steps to Increase Effectiveness, Efficiency, and Adaptability*. 2nd edn. New York: AMACOM.
- Dennis, A., Wixom, B.H. & Tegarden, D. (2021) *Systems Analysis and Design: An Object-Oriented Approach with UML*. 6th edn. Hoboken, NJ: Wiley.
