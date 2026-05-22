# Customer Metrics Reference

Comprehensive customer measurement formulas from Farris's "Marketing Metrics," growth marketing frameworks, and small business customer economics.

## Table of Contents

1. Customer Lifetime Value Models
2. Customer Acquisition Economics
3. Retention and Churn Metrics
4. Customer Profitability Analysis
5. Segment Valuation

## 1. Customer Lifetime Value Models

### Simple CLV

```
CLV = Average purchase value x Purchase frequency per year x Average customer lifespan (years)
```

**Example:** UGX 185,000 average order x 4 purchases/year x 5 years = UGX 3.7M CLV

### Contractual CLV (Subscription businesses)

```
CLV = ARPU x Gross margin % / Monthly churn rate

Where:
  ARPU = Average Revenue Per User per month
  Churn rate = % of customers who cancel per month
```

### CLV with Discount Rate (Farris)

```
CLV = Sum of [M x R^t / (1 + d)^t] for t = 1 to T

Where:
  M = Margin per customer per period
  R = Retention rate per period
  d = Discount rate (cost of capital)
  T = Time horizon in periods
```

### Simplified Discounted CLV

```
CLV = M x R / (1 + d - R)

Where:
  M = Annual margin per customer
  R = Annual retention rate
  d = Annual discount rate
```

**When to use which model:**

| Model | Best for | Limitations |
|---|---|---|
| Simple CLV | Early-stage estimates, simple businesses | Ignores time value of money |
| Contractual | SaaS, subscriptions, memberships | Assumes constant churn rate |
| Discounted | Investor-grade projections | Requires retention and discount rate data |

### Lifetime Customer Value — Small Business Approach

For small businesses without extensive data:

```
Step 1: Average sale amount = UGX X
Step 2: Number of transactions per year = Y
Step 3: Annual revenue per customer = X x Y
Step 4: Average customer relationship in years = Z
Step 5: Lifetime value = X x Y x Z
Step 6: Referral value = Lifetime value x Average referrals per customer
Step 7: Total customer value = Lifetime value + Referral value
```

This approach accounts for referral economics — a customer who refers two others is worth three times their direct CLV.

## 2. Customer Acquisition Economics

### Basic CAC

```
CAC = Total acquisition spend / New customers acquired
```

### Fully Loaded CAC

```
Fully Loaded CAC = (Marketing spend + Sales team cost + Tools/software + Overhead allocation)
                   / New customers acquired
```

### Channel-Specific CAC

```
Channel CAC = Spend on channel / Customers attributed to channel

Common channels:
  Paid search:    Ad spend / Conversions from paid search
  Social ads:     Ad spend / Conversions from social
  Content:        Content costs / Customers attributed to content
  Referral:       Incentive costs / Referred customers
  Events:         Event costs / Customers from events
  Direct sales:   Sales team cost / Deals closed
```

### CAC Payback Period

```
CAC Payback = CAC / (Monthly revenue per customer x Gross margin %)
```

| Payback Period | Assessment |
|---|---|
| < 6 months | Excellent — fast capital recovery |
| 6-12 months | Good — typical for SaaS |
| 12-18 months | Acceptable for high-CLV businesses |
| > 18 months | Risky — requires strong retention data |

## 3. Retention and Churn Metrics

### Churn Rate

```
Customer Churn Rate = Customers lost in period / Customers at start of period x 100

Revenue Churn Rate = MRR lost from churned customers / MRR at start of period x 100
```

### Net Revenue Retention (NRR)

```
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR x 100
```

| NRR | Assessment |
|---|---|
| > 120% | Excellent — growth from existing customers |
| 100-120% | Good — expansion offsets churn |
| 80-100% | Revenue shrinking from existing base |
| < 80% | Serious retention problem |

### Retention Rate

```
Retention Rate = 1 - Churn Rate
```

### Customer Engagement Score

Composite metric combining:
- Login frequency / usage frequency
- Feature adoption breadth
- Support ticket volume (inverse)
- NPS or satisfaction score
- Purchase recency

## 4. Customer Profitability Analysis

### Customer Profit (Farris)

```
Customer Profit = Revenue from customer
                - Cost of goods sold
                - Cost to serve (support, shipping, returns)
                - Cost to acquire (allocated CAC)
```

### Customer Profitability Index

```
Profitability Index = Customer Profit / Revenue from customer x 100
```

### Customer Segment Profitability Matrix

| Segment | Revenue | Cost to Serve | Profit | Profitability % | Action |
|---|---|---|---|---|---|
| High revenue / Low cost | High | Low | High | >30% | Protect and grow |
| High revenue / High cost | High | High | Medium | 10-30% | Reduce cost to serve |
| Low revenue / Low cost | Low | Low | Low | >30% | Develop or maintain |
| Low revenue / High cost | Low | High | Negative | <0% | Re-evaluate or exit |

### Share of Wallet (Farris)

```
Share of Wallet = Customer spend with us / Customer's total category spend x 100
```

High share of wallet = loyal, concentrated customer.
Low share of wallet = opportunity to capture more, or customer is hedging.

## 5. Segment Valuation

### Segment Value Score

```
Segment Value = Segment size x Penetration potential x Average CLV x Accessibility score

Where:
  Segment size = Number of potential customers
  Penetration potential = Realistic % capturable (1-20%)
  Average CLV = Expected lifetime value
  Accessibility score = 0.0-1.0 rating of how reachable the segment is
```

### Segment Prioritisation Matrix

Rank segments by:

1. **Attractiveness** (market size, growth rate, CLV potential)
2. **Fit** (alignment with capabilities, brand, values)
3. **Accessibility** (reachability through available channels)
4. **Profitability** (margin potential after cost to serve)

Score each 1-5, multiply for composite score. Pursue segments scoring >50 (out of 625).
