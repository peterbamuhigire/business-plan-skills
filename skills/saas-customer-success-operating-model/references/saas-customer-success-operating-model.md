---
source: Cotton, Mersch, Garbugli, Gainsight / Totango / ChurnZero CS frameworks
frameworks: [Touch-model segmentation, Customer health score, Lifecycle pipeline, QBR, Save protocol]
skill: saas-customer-success-operating-model
cross-reference: [saas-unit-economics-and-cohort-model, saas-lifecycle-email-and-retention, saas-pricing-and-packaging-strategy]
---

# SaaS Customer Success Operating Model — Reference

## 1. The Three Touch Models

| Touch | ACV Threshold | CSM:Customer Ratio | Engagement | Tools |
|---|---|---|---|---|
| **High-touch** | >$50k | 1:25 | Named CSM; weekly check-ins; QBR; executive sponsor; in-person | CRM + CS platform; QBR templates |
| **Mid-touch** | $10-50k | 1:50-100 | Named CSM; monthly check-ins; QBR; mostly remote | CS platform; templated content |
| **Tech-touch** | <$10k | 1:200-500 | Automated lifecycle; CSM as escalation only | Email automation; in-product nudges; help centre |

Choice depends on:
- Unit economics (CSM cost must fit gross margin)
- Customer complexity (more complex → higher touch)
- Strategic importance (logos that need protection → higher touch)

## 2. The Customer Health Score

Composite 0-100 score across weighted dimensions. Standard weights:

| Dimension | Weight | Computation |
|---|---|---|
| Product usage frequency | 20% | DAU/MAU; login frequency; sessions per week |
| Product usage depth | 20% | % of key features used; feature-stickiness |
| NPS (rolling 90 days) | 15% | Promoters > 9, Passives 7-8, Detractors <7 |
| Support ticket health | 10% | Open / closed / age / sentiment |
| Payment health | 10% | On-time payment; no card declines |
| Executive sponsor health | 10% | Sponsor still in role; engaged; LinkedIn-active |
| Adoption velocity | 10% | Time-to-first-value met; onboarding milestones hit |
| Expansion signal | 5% | Usage near plan limits; new use-case mentions |

Bands:
- **Green** (80-100): healthy; CSM in maintenance + expansion mode
- **Amber** (50-79): attention needed; CSM proactive outreach
- **Red** (<50): at-risk; named save-plan with timeline

## 3. The Customer Lifecycle Pipeline

```
Stage              Owner             Time SLA            Exit Criterion
-----              -----             --------            --------------
Sign-up            Sales handoff     Day 0               Contract signed
Kickoff            CSM               Day 0-3             Kickoff call complete; goals set
Onboarding         CSM + Support     Day 3-30            Tech setup complete; user accounts created
First Value        CSM               Day 30-60           "Aha moment" hit (defined event in product)
Activation         Auto + CSM        Day 60-90           5+ users active; key features used
Adoption           CSM               Months 3-6          Department-wide adoption
Expansion          CSM               Months 6+           Usage triggers expansion conversation
Pre-renewal        CSM               Month 9-10          Renewal posture confirmed
Renewal            CSM               Month 11-12         Renewal closed (or save protocol)
Advocacy           CSM + Marketing   Ongoing             Case study; reference; referral; G2 review
```

## 4. Onboarding Milestones (the highest-leverage stage)

Garbugli's data: 40-60% of new users never come back without lifecycle email. CSM must own the equivalent for paid customers:

```
DAY 0: Kickoff call (high-touch); welcome email sequence triggered (all)
DAY 3: First admin user has created an account
DAY 7: First end-user has logged in
DAY 14: Key Feature 1 has been used
DAY 21: Key Feature 2 has been used
DAY 30: ≥3 users active; core workflow completed end-to-end
DAY 60: First Value moment achieved (specific metric for product)
DAY 90: Activation complete
```

Each milestone is a measurable event. Customers who don't hit DAY 7 trigger automated "are you stuck?" outreach. Customers who don't hit DAY 30 trigger CSM intervention.

## 5. The QBR (Quarterly Business Review) Template

For high-touch and mid-touch customers:

```
1. Review of last quarter's commitments and outcomes
2. Usage analytics (depth, breadth, trend)
3. Outcomes / ROI achieved
4. Roadmap preview and customer requests
5. Expansion opportunities discussed
6. Risk / health items
7. Next quarter's commitments and success metrics
```

QBR attendees: customer's executive sponsor + champion; CSM + AE.

## 6. The Expansion Playbook

Triggers for expansion conversation:

- Usage hits 80% of seat / API / volume allocation
- New use-case mentioned in usage analytics or support tickets
- New executive joins customer (may have additional budget)
- Adjacent department starts using product on guest accounts
- Customer publishes case study or PR about the product (advocacy = expansion-ready)
- Renewal approaching (built-in expansion conversation)

Expansion plays:
- Add seats
- Add modules
- Move up tier
- Add adjacent product (cross-sell)
- Multi-year prepay (cash + reduces churn risk)

## 7. The Save Protocol (when a customer cancels)

- **Hour 0-24**: Automated email acknowledging cancellation; offering 30-min "exit" call
- **Day 1-3**: CSM personal outreach offering: pause, downgrade, extended trial, dedicated account-rescue plan
- **Day 3-7**: Sales / executive escalation if customer is high-value
- **Day 7+**: Exit interview; capture reason; add to churn analysis
- **Day 30**: Re-engagement sequence if appropriate
- **Day 90**: Win-back campaign if appropriate

Best-in-class save rates: 15-30% of voluntary cancellations recovered.

## 8. CSM Compensation

OTE structure: 70-80% base, 20-30% variable.

Variable comp ties to:
- NRR per book of business (50% weight)
- Logo retention (20% weight)
- Customer health score average (15% weight)
- Customer-led growth signals (NPS, references, case studies) (15% weight)

Do NOT tie CSM comp to: new sales (that's AE's job), support metrics (that's support's job), product feature usage (that's product's KPI).

## 9. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Customer health-score dashboard | Daily / weekly | Head of CS |
| Cohort retention | Monthly | CFO + Head of CS |
| NRR by segment | Monthly | CFO + Head of CS |
| Save-plan reviews (red customers) | Weekly | Head of CS |
| QBR completion rate | Quarterly | Head of CS |
| Expansion pipeline | Monthly | Head of CS + VP Sales |
| CSM book of business rebalancing | Quarterly | Head of CS |
| CS team comp plan | Annually | Head of CS + CFO |

## 10. Africa / Uganda Application Notes

- **WhatsApp-first CS** — most African B2B customers prefer WhatsApp over email for ongoing engagement. Have a CSM-managed WhatsApp Business presence per high-touch customer.
- **In-person onboarding** for high-touch customers is disproportionately powerful in African business culture. Budget for travel.
- **CSM as field-implementation** — for many African deals, customers expect onsite training. Build this into CS comp model.
- **NPS in Africa** — response rates lower; supplement with usage signals.
- **Renewal timeline** — start renewal conversations 90+ days early due to procurement bureaucracy.
- **Multi-language CS** — if you serve multiple language markets, CSMs must cover the buyer's language (English + Swahili / Luganda / French / Arabic / Yoruba etc).
- **Health score adjustment** — payment health weight is higher in Africa (payment-rail issues are common); usage-frequency weight may be lower (intermittent connectivity).
- **Public-sector / NGO** — CS model is fundamentally different (donor cycles, budget renewals, change of leadership at fiscal year-end). May warrant a dedicated CSM specialism.
