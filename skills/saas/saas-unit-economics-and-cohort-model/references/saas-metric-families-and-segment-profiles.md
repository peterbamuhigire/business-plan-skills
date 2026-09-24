Parent: [SaaS Unit Economics & Cohort Model Skill](../SKILL.md)

When to read: when a SaaS plan's financial section must meet a SaaS finance reviewer's expectations on metrics, segment profile, churn arithmetic, retention measures and benchmark discipline. Use with `skills/pipeline/10-financial-projections/references/saas-unit-economics-model-template.md` (formulas and worked example), `saas-financial-projection-template-3yr-5yr.md` (multi-step P&L, ARR waterfall, working-capital trough) and `saas-cohort-and-retention-model-template.md` (cohort matrices).

# SaaS financial language: a reviewer's checklist

This is the engine's checklist for the SaaS finance vocabulary a plan must use correctly. It runs as seven reviewer questions. It reflects common SaaS finance practice as described by practitioners such as Mersch, E. (2023) *Hacking SaaS*, FLG Partners, and Cotton, B. (2019) *How to Run a SaaS Business*; the questions, grouping, arithmetic examples and African checks are this engine's. Any numeric threshold must come from a current, dated benchmark with its peer set.

## Q1 — Is the revenue genuinely SaaS?

SaaS shows recurring subscriptions (not a one-off licence plus maintenance), customer operating spend (not capital purchases), customer success as revenue protection (not support as overhead), continuous releases, and live usage data feeding the product. If these are absent, route to `ict-product-company-business-plan` or run the tenancy test in `skills/pipeline/08-operations-plan/references/saas-tenancy-model-and-msp-trap-test.md`.

## Q2 — Are the three sets of metrics reported and defined?

| Set | Metrics and definitions |
|---|---|
| Revenue movement | ARR and MRR; new, expansion, contraction and churned ARR; net new ARR = new + expansion − contraction − churned; growth = net new ARR ÷ opening ARR; bookings (signed contract value, not revenue) |
| Customer economics | Fully loaded CAC; LTV = revenue per customer × gross margin × expected life (life ≈ 1 ÷ churn); LTV:CAC; CAC payback months; gross margin split between software and services; sales efficiency = annualised net new ARR ÷ prior-period sales and marketing spend |
| Financial health | Operating income; EBITDA and adjusted EBITDA with exclusions listed; free cash flow as the central line; burn multiple = net burn ÷ net new ARR; runway = cash ÷ monthly net burn; Rule of 40 = growth % + profit margin % for each projected year |

Every threshold (LTV:CAC ratio, payback, burn-multiple band, Rule-of-40 target) cites a current, dated source and peer set; thresholds from older books are not facts.

## Q3 — Is the income statement laid out for SaaS?

Revenue split into recurring software, recurring services and one-off services. Cost of revenue split into hosting, support, cloud operations and third-party software or data. Operating costs in research and development, sales and marketing (including customer success and commissions), and general and administrative. Template: `saas-financial-projection-template-3yr-5yr.md`.

## Q4 — Which customer profile drives cash?

| Profile | Billing | Cash consequence | Where to focus |
|---|---|---|---|
| Large organisations | Annual or multi-year in advance | Prepayments fund operations | Sales capacity, long cycles, high-touch selling |
| Small and mid-sized businesses | Mostly monthly | A cash trough: acquisition is paid up front and recovered over months; faster growth deepens it | Short payback, monthly churn |
| Consumers | Monthly, many small accounts | The deepest trough; reliance on self-serve and free tiers | Cohort curves, marketing efficiency |

Declare also whether the product is **horizontal** (one product for many industries: larger market, harder to stand out) or **vertical** (one industry: smaller market, deeper fit, stronger pricing, often payments or services added, needs sector knowledge). Local knowledge of payment rails, tax-system integration and languages often favours vertical SaaS in Africa; test with `saas-vertical-niche-selection`. Use benchmark ranges only for the declared profile and explain material departures.

## Q5 — Is churn calculated correctly?

- State the period. Annual retention = (1 − monthly churn)^12. Losing 5% of customers a month loses about 46% in a year; 5% a year is about 0.4% a month.
- Separate gross churn from net revenue retention, and customer (logo) churn from revenue churn.
- Separate involuntary loss (failed card, mobile-money time-out, network failure) from voluntary loss, with a target and recovery routine for each.
- Cut cohorts by acquisition source; test whether discount-acquired customers leave faster.
- Retention comes before acquisition: marketing cannot refill a leaking base.

## Q6 — Are early warning signs of churn tracked?

- **Net Promoter Score:** % scoring 9–10 minus % scoring 0–6 (range −100 to +100), on a set cadence; every detractor triggers a customer-success action; compare with competitors where data exists.
- **Customer health score:** usage, satisfaction, support tickets, payment record and sponsor strength (details in `saas-customer-success-operating-model`).
- Retention levers: honest qualification during sales, strong account management, strong support and customer success.

## Q7 — Is the model built and reviewed properly?

- Quarterly five-year model: ARR build; headcount tied to sales capacity (bookings = sellers × quota × attainment); cohort-based revenue; bookings → billings → revenue → cash; deferred-revenue schedule; cost ratios by function; sensitivity to churn, win rate, expansion, ramp time, CAC and gross margin.
- Deferred revenue appears on the balance sheet when customers prepay.
- Every pricing, packaging, geography, vertical and hiring decision is traced to its effect on these metrics, with the finance lead as a partner, not a scorekeeper.

**Illustrative example.** A Kampala HR SaaS reports 3% monthly logo churn and calls it "low". The reviewer converts it: (0.97)^12 ≈ 0.69, so about 31% of customers leave each year; splitting churn shows a third is failed mobile-money renewals, which gets its own recovery routine.

## African checks (run with current sources)

Whether gross margins are lower because of foreign-currency infrastructure and payment fees; whether annual prepayment is hard to win, requiring multi-year local-currency contracts with escalators; how foreign-currency costs against local-currency revenue deepen the cash trough; whether acquisition costs are higher because the category needs educating; whether finance-grade reporting early improves credibility with development-finance institutions and international investors.
