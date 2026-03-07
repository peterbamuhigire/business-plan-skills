# Retail Analytics and Metrics Reference

> References: *Analytics for Retail* by Okunev (Apress, 2022); *Retail Management: A Strategic Approach* by Berman & Evans (Pearson, 2013); *Retail Management* by Tiwari (Global Media, 2008)

> Figures adapted to Ugandan context (UGX).

---

## 1. Core Retail KPIs

Every retail business tracks a set of **key performance indicators (KPIs)** that reveal how the basic functions of the company are working (Okunev 2022, ch. 4). The table below lists the core metrics, their formulas, and worked examples in UGX.

| Metric | Formula | Worked Example (UGX) |
|---|---|---|
| **Gross Sales (Revenue)** | Sum of all sales receipts in a period | Monthly receipts total UGX 45,000,000 |
| **Net Sales** | Gross Sales − (Discounts + Returns + Allowances) | 45,000,000 − (2,000,000 + 800,000 + 200,000) = **UGX 42,000,000** |
| **Cost of Goods Sold (COGS)** | Beginning Inventory + Net Purchases + Labour + Materials − Ending Inventory | 8,000,000 + 22,000,000 + 1,500,000 + 500,000 − 7,000,000 = **UGX 25,000,000** |
| **Gross Profit** | Net Sales − COGS | 42,000,000 − 25,000,000 = **UGX 17,000,000** |
| **Gross Profit Margin %** | (Gross Profit ÷ Net Sales) × 100 | (17,000,000 ÷ 42,000,000) × 100 = **40.5%** |
| **Operating Profit** | Gross Profit − Total Operating Expenses | 17,000,000 − 9,000,000 = **UGX 8,000,000** |
| **Net Profit** | Net Sales − (COGS + Operating Expenses + Taxes + Interest) | 42,000,000 − (25,000,000 + 9,000,000 + 2,400,000 + 600,000) = **UGX 5,000,000** |
| **Net Profit Margin %** | (Net Profit ÷ Net Sales) × 100 | (5,000,000 ÷ 42,000,000) × 100 = **11.9%** |
| **Average Order Value (AOV)** | Net Sales ÷ Number of Transactions | 42,000,000 ÷ 1,200 = **UGX 35,000** |
| **Units per Transaction (UPT)** | Quantity Sold ÷ Number of Transactions | 3,600 ÷ 1,200 = **3.0 items** |
| **Conversion Rate %** | (Number of Purchases ÷ Number of Visitors) × 100 | (1,200 ÷ 4,800) × 100 = **25%** |
| **Basket Size (value)** | Total Units Sold × Average Selling Price | Same derivation as AOV; track alongside UPT |
| **Initial Markup %** | [(Ticket Price − COGS) ÷ Ticket Price] × 100 | [(50,000 − 25,000) ÷ 50,000] × 100 = **50%** |

**Benchmarks (Okunev 2022):** A good net profit margin is ~20%; 10% is acceptable; below 5% is weak. A good gross profit margin for online retail is 46–65%. Track these KPIs daily, weekly, monthly, and year-on-year.

---

## 2. Inventory Metrics

Effective inventory management is critical because stock is typically a retailer's largest single expense (Okunev 2022, ch. 4; Berman & Evans 2013, ch. 16).

| Metric | Formula | Benchmark / Notes |
|---|---|---|
| **Inventory Turnover** | Quantity Sold ÷ Average Inventory on Hand | Higher = stronger sales; grocery 12–20×, apparel 4–6×, general merch 6–10× |
| **Inventory Turnover (cost basis)** | COGS ÷ Average Inventory at Cost | Preferred by finance teams; removes markup distortion |
| **Average Inventory** | (Beginning Inventory + Ending Inventory) ÷ 2 | Use units, cost, or retail value depending on audience |
| **Sell-Through Rate %** | [Units Sold ÷ (Units Sold + Beginning Units on Hand)] × 100 | Good range: 40%–80% (Okunev 2022) |
| **Weeks of Supply** | On-hand Inventory (units) ÷ Weekly Unit Sales | Lower = leaner stock; target depends on lead time |
| **Stock-to-Sales Ratio** | Stock Value (EOM) ÷ Net Sales (month) | Good range: 0.16–0.25 (Okunev 2022) |
| **GMROI** | Gross Margin (UGX) ÷ Average Inventory at Cost | Supermarket ~300%; clothing ~300% achieved differently (Berman & Evans 2013) |
| **GMROI (expanded)** | (Gross Margin % × Net Sales) ÷ Avg Inventory at Cost | Combines profitability and sales-to-stock ratio |
| **Shrinkage Rate %** | (Book Inventory − Physical Inventory) ÷ Book Inventory × 100 | Industry average 1–3%; >3% signals theft/damage problems |
| **Fill Rate %** | (Orders Shipped ÷ Total Orders) × 100 | Target as close to 100% as possible |

### Worked Example — GMROI (UGX)

A Kampala clothing shop has:
- Net sales: UGX 120,000,000/year
- COGS: UGX 66,000,000
- Average inventory at cost: UGX 18,000,000

```
Gross margin = 120,000,000 − 66,000,000 = UGX 54,000,000
Gross margin % = 54,000,000 ÷ 120,000,000 = 45%
Sales-to-stock ratio = 120,000,000 ÷ 18,000,000 = 6.67
GMROI = 54,000,000 ÷ 18,000,000 = 300%
```

A GMROI of 300% means the shop earns UGX 3.00 in gross margin for every UGX 1.00 invested in inventory.

---

## 3. Sales Productivity Metrics

Productivity metrics reveal how efficiently a retailer converts resources (space, people, time) into revenue (Berman & Evans 2013, ch. 12; Tiwari 2008, ch. 5).

| Metric | Formula | Typical Range |
|---|---|---|
| **Sales per Square Metre** | Net Sales ÷ Selling Area (m²) | Varies widely; grocery UGX 3–8 m/m²/year; specialty UGX 2–6 m/m²/year |
| **Sales per Square Foot** | Net Sales ÷ Selling Area (ft²) | Convert: 1 m² ≈ 10.76 ft² |
| **Sales per Employee** | Net Sales ÷ Number of Employees (FTE) | Benchmark against same format; higher = more efficient |
| **Sales per Labour Hour** | Net Sales ÷ Total Labour Hours Worked | Useful for shift scheduling; track daily |
| **Transactions per Labour Hour** | Number of Transactions ÷ Total Labour Hours | Measures checkout/service efficiency |

### Worked Example — Sales per Square Metre (UGX)

A 200 m² convenience shop generates UGX 480,000,000 in annual net sales:

```
Sales per m² = 480,000,000 ÷ 200 = UGX 2,400,000/m²/year
Sales per m²/month = 2,400,000 ÷ 12 = UGX 200,000/m²/month
```

---

## 4. Customer Metrics

Understanding customer economics is essential for budgeting marketing spend and forecasting growth (Okunev 2022, ch. 11; Berman & Evans 2013, ch. 7).

| Metric | Formula | Notes |
|---|---|---|
| **Customer Acquisition Cost (CAC)** | Total Marketing & Sales Spend ÷ New Customers Acquired | Include advertising, promotions, sales staff time |
| **Customer Lifetime Value (CLV)** | (Average Purchase Value × Purchase Frequency × Customer Lifespan) − CAC | Core metric for investment decisions |
| **CLV (margin-based)** | (Avg Order Value × Gross Margin % × Purchase Frequency × Avg Customer Lifespan) | More conservative; uses margin not revenue |
| **Customer Retention Rate %** | [(Customers at End − New Customers) ÷ Customers at Start] × 100 | Above 70% is good for most retail formats |
| **Customer Churn Rate %** | 100 − Retention Rate | Track monthly or quarterly |
| **Customer Growth Rate %** | [(Customers End − Customers Start) ÷ Customers Start] × 100 | Positive growth sustains long-term revenue |
| **Repeat Purchase Rate %** | Repeat Customers ÷ Total Customers × 100 | Higher for convenience/grocery; lower for specialty |

### Worked Example — CLV (UGX)

A Kampala boutique estimates:
- Average order value: UGX 85,000
- Purchases per year: 4
- Gross margin: 45%
- Average customer lifespan: 3 years
- CAC: UGX 30,000

```
CLV = (85,000 × 0.45 × 4 × 3) − 30,000
    = 459,000 − 30,000
    = UGX 429,000
```

**Rule of thumb:** CLV should be at least 3× CAC. Here the ratio is 429,000 ÷ 30,000 = **14.3×** — very healthy.

---

## 5. Space Performance

Space is one of the most constrained and costly resources for Ugandan retailers. The following metrics help evaluate whether every square metre justifies its cost (Tiwari 2008, ch. 5; Berman & Evans 2013, ch. 13).

| Metric | Formula | Use |
|---|---|---|
| **Sales per m²** | Net Sales ÷ Total Selling Area (m²) | Primary space productivity measure |
| **Gross Margin per m²** | Gross Profit ÷ Total Selling Area (m²) | Shows profitability of space, not just revenue |
| **Net Profit per m²** | Net Profit ÷ Total Selling Area (m²) | True bottom-line space efficiency |
| **Stock Holding per m²** | Inventory Value (at cost) ÷ Total Selling Area (m²) | Indicates capital intensity of floor space |
| **Sales per Linear Metre** | Category Sales ÷ Linear Shelf Metres Allocated | Used for planogram optimisation |
| **Hot-Spot Ratio** | Sales from Zone ÷ % of Floor Area Occupied by Zone | >1.0 = zone outperforms its share of space |

### Space Allocation Decision Framework

1. Rank departments/categories by **margin per m²**.
2. Increase allocation to categories with margin per m² above store average.
3. Reduce allocation (or renegotiate supplier terms) for categories below average.
4. Use **hot-spot analysis** to identify high-traffic zones and place high-margin items there (Tiwari 2008).

---

## 6. Financial Ratios for Retail

Financial ratios enable a retailer to assess liquidity, leverage, profitability, and efficiency (Okunev 2022, ch. 5; Berman & Evans 2013, ch. 12).

### 6.1 Liquidity Ratios

| Ratio | Formula | Healthy Range |
|---|---|---|
| **Current Ratio** | Current Assets ÷ Current Liabilities | >1.5 is good; <1.0 signals inability to cover short-term debt |
| **Quick Ratio (Acid Test)** | (Cash + Accounts Receivable + Marketable Securities) ÷ Current Liabilities | >1.0 means firm can cover debt without selling inventory |
| **Cash Ratio** | Operating Cash Flow ÷ Current Liabilities | 0.5–1.0 preferred for retail (Okunev 2022) |

### 6.2 Debt / Leverage Ratios

| Ratio | Formula | Healthy Range |
|---|---|---|
| **Debt Ratio** | Total Liabilities ÷ Total Assets | <0.4 is better; >0.6 means difficulty borrowing |
| **Interest Coverage Ratio** | EBITDA ÷ Interest Expenses | >2.0 is comfortable; <1.5 signals trouble |
| **Debt Service Coverage** | Net Operating Income ÷ Total Debt Service | >1.0 positive; >2.0 can carry additional loans |

### 6.3 Profitability Ratios

| Ratio | Formula | Healthy Range |
|---|---|---|
| **Gross Profit Margin %** | (Net Sales − COGS) ÷ Net Sales × 100 | Grocery 20–30%; apparel 45–65%; specialty 50–70% |
| **Net Profit Margin %** | Net Profit After Tax ÷ Net Sales × 100 | >20% good; 10% acceptable; <5% weak |
| **EBITDA Margin %** | EBITDA ÷ Net Sales × 100 | Varies; higher is better |
| **Return on Assets (ROA)** | Net Profit ÷ Total Assets × 100 | >5% considered good (Okunev 2022) |
| **Return on Net Worth (RONW)** | Net Profit Margin × Asset Turnover × Financial Leverage | See Strategic Profit Model below |

### 6.4 Efficiency / Activity Ratios

| Ratio | Formula | Notes |
|---|---|---|
| **Asset Turnover** | Net Sales ÷ Total Assets | Higher = more revenue per UGX of assets |
| **Inventory Turnover** | COGS ÷ Average Inventory at Cost | See Section 2 |
| **Collection Period (days)** | (Accounts Receivable ÷ Net Sales) × 365 | >1.33× credit terms = slow receivables |
| **Accounts Payable to Net Sales** | Accounts Payable ÷ Annual Net Sales | Above industry average = over-reliance on supplier finance |

### The Strategic Profit Model (Berman & Evans 2013)

```
Return on Net Worth = Net Profit Margin × Asset Turnover × Financial Leverage

Where:
  Net Profit Margin  = Net Profit After Tax ÷ Net Sales
  Asset Turnover     = Net Sales ÷ Total Assets
  Financial Leverage = Total Assets ÷ Net Worth
```

**Worked Example (UGX):**

A general merchandise retailer:
- Net profit after tax: UGX 19,250,000
- Net sales: UGX 330,000,000
- Total assets: UGX 325,000,000
- Net worth: UGX 168,000,000

```
Net Profit Margin  = 19,250,000 ÷ 330,000,000 = 5.83%
Asset Turnover     = 330,000,000 ÷ 325,000,000 = 1.015
Financial Leverage = 325,000,000 ÷ 168,000,000 = 1.935
RONW = 0.0583 × 1.015 × 1.935 = 11.4%
```

---

## 7. Performance Benchmarks by Retail Format

The table below provides typical ranges drawn from the sources and adapted to the Ugandan market. Ranges are indicative; actual performance depends on location, management, and scale.

| Metric | Grocery / Supermarket | General Merchandise | Specialty / Boutique | Convenience |
|---|---|---|---|---|
| **Gross Margin %** | 18–28% | 30–42% | 45–65% | 22–35% |
| **Net Profit Margin %** | 1–4% | 3–8% | 8–20% | 2–5% |
| **Inventory Turnover (×/year)** | 12–20 | 6–10 | 4–8 | 15–25 |
| **GMROI** | 250–350% | 200–300% | 200–400% | 250–350% |
| **Sell-Through Rate %** | 70–90% | 50–75% | 40–70% | 75–90% |
| **Stock-to-Sales Ratio** | 0.08–0.15 | 0.20–0.35 | 0.25–0.45 | 0.06–0.12 |
| **Conversion Rate %** | 80–95% | 20–40% | 15–35% | 85–95% |
| **Sales per m² (UGX m/year)** | 3–8 | 1.5–4 | 2–6 | 4–10 |
| **Sales per Employee (UGX m/year)** | 40–80 | 30–60 | 25–50 | 50–90 |
| **Shrinkage %** | 1–3% | 1.5–3% | 1–2.5% | 2–4% |
| **Current Ratio** | 1.0–1.5 | 1.5–2.5 | 1.5–3.0 | 1.0–1.5 |
| **Debt Ratio** | 0.4–0.6 | 0.3–0.5 | 0.2–0.4 | 0.4–0.6 |
| **ROA** | 4–8% | 5–12% | 8–18% | 5–10% |
| **Asset Turnover** | 2.5–3.5 | 1.5–2.5 | 1.0–2.0 | 2.5–3.5 |

*Sources: Berman & Evans 2013, Table 12-3; Okunev 2022, ch. 4–5; Tiwari 2008.*

---

## 8. Forecasting Methods

Retail forecasting moves from gut-feel estimation to data-driven prediction (Okunev 2022, ch. 11; Tiwari 2008).

### 8.1 Regression (Time-Series Linear)

1. Collect monthly sales data from inception.
2. Calculate a **12-month centred moving average** to smooth seasonality.
3. Compute a **seasonal ratio** = Actual Sales ÷ Moving Average for each month.
4. Average each month's ratios across years → **unadjusted seasonal index**.
5. Adjust so all 12 indices sum to 12.0 → **adjusted seasonal index**.
6. **Deseasonalise** each month: Actual Sales ÷ Adjusted Index.
7. Run a **linear regression** on deseasonalised data: Ŷ = mx + b.
8. **Re-seasonalise** forecast: Predicted = Regression Value × Adjusted Index.

### 8.2 Moving Averages

| Type | Formula | Use |
|---|---|---|
| Simple Moving Average (SMA) | Sum of last *n* periods ÷ *n* | Smooths short-term noise |
| Weighted Moving Average | Σ(Weight × Period Value) ÷ Σ Weights | Gives more weight to recent data |
| Exponential Smoothing | Forecast = α × Actual + (1 − α) × Previous Forecast | α between 0.1 (stable) and 0.3 (volatile) |

### 8.3 Seasonal Adjustment

- Use the **adjusted seasonal index** from 8.1 above.
- Multiply the base forecast by the index to obtain the seasonal forecast.
- Review and update indices annually as patterns shift.

### 8.4 Scenario Analysis

Create three scenarios using the base forecast (Okunev 2022, ch. 11):

| Scenario | Growth Assumption | Purpose |
|---|---|---|
| **Conservative (Low)** | Base − 5 to 10 pp | Worst-case planning; set minimum inventory |
| **Base (Normal)** | Regression-derived % | Budget and staffing baseline |
| **Optimistic (High)** | Base + 5 to 10 pp | Upside opportunity; stretch targets |

Apply each scenario to:
- **Campaign analysis** — weekly breakdown of expected versus actual sales for a promotional period.
- **Consumer segmentation** — allocate revenue across loyal (80/20 rule), sale-driven, and new customers.

---

## 9. Daily / Weekly / Monthly Tracking

### 9.1 What to Measure and When

| Frequency | Metrics | Actions |
|---|---|---|
| **Daily** | Net sales, transactions, conversion rate, AOV, UPT, footfall, units sold by SKU, shrinkage incidents | Adjust floor staff, replenish fast movers, flag anomalies |
| **Weekly** | Sell-through rate, weeks of supply, weekly units sold, sales per labour hour, stock-to-sales ratio, fill rate | Reorder decisions, markdown candidates, staff scheduling |
| **Monthly** | Gross/net profit margins, inventory turnover, GMROI, sales per m², sales per employee, customer metrics (CAC, retention), cash flow | P&L review, space reallocation, marketing budget adjustments |
| **Quarterly** | Financial ratios (current, quick, debt, ROA, RONW), customer lifetime value, scenario forecast update | Strategic review, bank/investor reporting, lease negotiations |
| **Annually** | Full strategic profit model, year-on-year growth, benchmark comparison by format, seasonal index recalculation | Business plan update, capital budgeting, expansion decisions |

### 9.2 Dashboard Structure

A retail analytics dashboard should present information in layers:

**Layer 1 — Executive Summary (top of dashboard)**
- Today's net sales vs. target (UGX)
- Month-to-date net sales vs. plan
- Gross margin % (MTD)
- Conversion rate (today and trailing 7-day)

**Layer 2 — Operational Detail (middle panels)**
- Top 10 selling SKUs (units and revenue)
- Bottom 10 SKUs by sell-through (markdown candidates)
- Stock-to-sales ratio by category
- Labour productivity: sales per hour, transactions per hour

**Layer 3 — Financial Health (bottom panels)**
- Cash position and cash flow trend
- Inventory turnover (trailing 12 months)
- GMROI by department
- Accounts payable ageing

**Layer 4 — Strategic (monthly/quarterly overlay)**
- Customer acquisition cost trend
- CLV : CAC ratio
- Forecast vs. actual (regression model)
- Scenario variance analysis

### 9.3 Key Reporting Principles

1. **Compare like with like** — compare same day of week, same season last year.
2. **Use rolling averages** — a 4-week rolling average smooths daily noise.
3. **Flag exceptions** — set thresholds (e.g., conversion rate drops >5 pp from 7-day average) to trigger investigation.
4. **Act on variance** — positive variance may signal under-stocking; negative variance may require promotional response or cost review.
5. **Track the 80/20** — 80% of sales typically come from 20% of customers and 20% of SKUs (Okunev 2022). Focus monitoring accordingly.

---

*End of reference.*
