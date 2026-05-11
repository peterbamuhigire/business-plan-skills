---
source: SaaS packaging practice (2024-2026); agent-products audit (2026); engine synthesis
frameworks: [Included vs Add-on vs Standalone; Attach-rate × ARPU lift × cannibalisation; Multi-product NRR composition; Free-trial discipline]
skill: saas-agent-commercial-packaging-economics
cross-reference: [saas-agent-pricing-strategy, saas-pricing-and-packaging-strategy, saas-unit-economics-and-cohort-model]
---

# Commercial Packaging Economics — Template + Worked Models

## 1. The packaging archetypes

| Archetype | Customer purchase decision | Visibility | Attach rate | Best when |
|---|---|---|---|---|
| Included | None (bundled in tier) | Hidden in tier price | 100% | Low / stable cost; differentiation at platform level |
| Add-on | Explicit yes/no | Visible separate line | 20-60% typical | Cost varies by usage; investor revenue attribution needed |
| Standalone | Separate contract | Separate logo | N/A | Distinct buyer / use case; distinct GTM |

## 2. Included packaging — worked model

### Scenario
- Existing platform: $200/month per customer
- 1,000 existing customers
- Decision: include agent in the platform
- Agent cost per resolved task: $3.50; expected 50 tasks/customer/month → $175/customer/month cost
- Decision: raise platform price to $300/month to absorb cost + retain margin

### Economics (annual)
- Pre-decision platform revenue: 1,000 × $200 × 12 = $2,400,000
- Pre-decision platform COGS (excl agent): 1,000 × $40 × 12 = $480,000
- Pre-decision gross profit: $1,920,000 (80% GM)

- Post-decision platform revenue: 1,000 × $300 × 12 = $3,600,000
- Post-decision platform COGS: ($40 + $175) × 1,000 × 12 = $2,580,000
- Post-decision gross profit: $1,020,000 (28.3% GM)

**Verdict:** Including the agent at this cost destroys gross margin. Either:
- Cap usage in fair-use policy (e.g. 25 tasks/customer/month free; overage $3.50/task)
- Choose Add-on packaging instead
- Improve cost per resolved task (engineering investment)

### Stress: cost variance
- Heavy-use customers (top 20% at 200 tasks/customer/month) consume $700/customer/month
- Light-use customers (bottom 50% at 10 tasks/customer/month) consume $35/customer/month
- Variance is enormous — Included packaging cross-subsidises light users with heavy users

### Recommendation
- Included packaging works only when cost variance is low or there is hard usage cap
- Otherwise: Add-on or Standalone

## 3. Add-on packaging — worked model

### Scenario
- Existing platform: $200/month, 1,000 customers
- Decision: agent as Add-on at $150/month (covers 30 tasks/customer/month at $5/task customer-facing price, $3.50 cost = $50 margin per customer)
- Attach rate: 30% in Year 1; 45% in Year 2; 55% in Year 3
- Cannibalisation: 10% of attaching customers downgrade base tier from $200 to $100 to free budget

### Year 1 economics
- Platform revenue (1,000 × $200 × 12): $2,400,000
- Cannibalisation: 300 attachers × 10% × $100 downgrade × 12 = -$36,000
- Net platform revenue: $2,364,000
- Add-on revenue: 300 customers × $150 × 12 = $540,000
- Add-on COGS (cost per resolved task × volume): 300 × $105 × 12 = $378,000
- Add-on gross profit: $162,000 (30% GM)
- Total revenue Y1: $2,904,000 vs $2,400,000 baseline
- Total revenue uplift: $504,000 (+21%)
- Total gross profit Y1: $1,920,000 (platform) - $36,000 (cannibalisation) + $162,000 (add-on) = $2,046,000
- vs baseline $1,920,000 → uplift $126,000

### Year 3 economics (with attach rate scaling and reliability improving cost)
- Cost per task improves to $2.80 (engineering); margin per attached customer: $150 - $84 = $66
- Attach rate 55%: 550 customers
- Add-on revenue Y3: 550 × $150 × 12 = $990,000
- Add-on COGS Y3: 550 × $84 × 12 = $554,400
- Add-on gross profit Y3: $435,600

### Cannibalisation stress
- If cannibalisation rises to 25% (customers downgrading aggressively):
  - Lost platform revenue: 550 × 25% × $100 × 12 = $165,000
  - Net Y3 add-on uplift: $435,600 - $165,000 = $270,600 — still positive, but materially lower
- If attach rate stalls at 20% and cannibalisation at 15%:
  - Add-on Y3 revenue: 200 × $150 × 12 = $360,000; gross profit $132,000
  - Cannibalisation: 200 × 15% × $100 × 12 = $36,000 lost platform revenue
  - Net uplift: $96,000 — marginal

### Stress matrix

| Attach rate Y3 | Cannibalisation rate | Net gross profit uplift Y3 |
|---|---|---|
| 55% | 10% | +$369,600 |
| 55% | 25% | +$270,600 |
| 45% | 15% | +$229,500 |
| 30% | 15% | +$140,400 |
| 20% | 15% | +$96,000 |
| 10% | 25% | +$11,000 |

**Verdict:** Add-on packaging is robust above 30% attach and below 20% cannibalisation. Below that, the economics are marginal.

## 4. Standalone packaging — worked model

### Scenario
- Agent sold as Standalone product at $400/month per customer; covers 80 tasks/customer/month at $5 customer-facing, $3.50 cost
- Margin per customer per month: $400 - $280 = $120 (30% GM)
- Separate GTM motion required: $200k Y1 sales investment to acquire 50 standalone customers Y1, 150 Y2, 300 Y3

### Y1 economics
- Standalone revenue: 50 × $400 × 12 = $240,000
- Standalone COGS: 50 × $280 × 12 = $168,000
- Standalone gross profit: $72,000 (30% GM)
- GTM investment: $200,000
- Y1 contribution: -$128,000 — heavily negative

### Y3 economics
- 300 customers; standalone revenue: 300 × $400 × 12 = $1,440,000
- COGS: 300 × $280 × 12 = $1,008,000 (with eng improvement → $230/customer)
- Adjusted COGS: 300 × $230 × 12 = $828,000
- Gross profit: $612,000 (42.5% GM)
- GTM cost ongoing: $250,000
- Y3 net contribution: $362,000

### CAC payback
- Y1 CAC: $200,000 ÷ 50 = $4,000 per customer
- Y1 gross profit per customer: $72,000 ÷ 50 = $1,440 per customer
- CAC payback: 2.8 years — borderline

**Verdict:** Standalone packaging works for distinct vertical or distinct buyer; CAC payback matters; pair with strong vertical positioning.

## 5. Multi-product NRR composition

For an agent-business with platform + agent add-on:

| Year | Starting MRR ($k) | Platform expansion | Agent attach expansion | Agent usage expansion | Contraction | Churn | Ending MRR | NRR |
|---|---|---|---|---|---|---|---|---|
| Y1 | 200 | +30 | +45 | +5 | -3 | -10 | 267 | 133% |
| Y2 | 267 | +40 | +60 | +12 | -5 | -14 | 360 | 135% |
| Y3 | 360 | +55 | +80 | +20 | -8 | -20 | 487 | 135% |

**Reporting discipline:** decompose NRR contributions per product line every monthly investor update. Investors compare against benchmark NRR (top-quartile SaaS: 120%+; top-quartile agent attach: 130%+).

## 6. Free-trial discipline

For Add-on and Standalone:

| Element | Discipline |
|---|---|
| Trial period | 14-30 days |
| Trial usage cap | 25 tasks (or equivalent); enforced |
| Trial cost cap | $500 per trial |
| Conversion target | 20-40% trial → paid |
| Trial revenue recognition | None (no revenue until conversion) |
| Trial discount on conversion | Optional; typically 10-25% first 3 months |
| Refund window post-conversion | 14 days |

## 7. Packaging migration triggers

| Direction | Trigger |
|---|---|
| Add-on → Included | Attach rate exceeds 75%; competitive pressure to bundle |
| Add-on → Standalone | Agent ARR exceeds 30% of total; distinct buyer emerging |
| Included → Add-on | Cost variance exceeds 3x across customer base; margin pressure |
| Standalone → Add-on | Standalone CAC payback >24 months; platform anchor needed |

## 8. SLA tier composition

| Packaging | SLA discipline |
|---|---|
| Included | Single platform SLA; limited tiering |
| Add-on | Tier SLA (bronze / silver / gold) feasible on add-on |
| Standalone | Full SLA discipline; tier-priced |

## 9. Worked decision framework

| Question | Included | Add-on | Standalone |
|---|---|---|---|
| Cost variance across customers | Low needed | OK | OK |
| Investor revenue attribution required | Hard | Easy | Easy |
| Attach-rate selling capacity | N/A | Required | N/A |
| Vertical specificity | Low | Medium | High |
| SLA tier discipline needed | Limited | Full | Full |
| Distinct buyer | No | No | Yes |
| Platform anchor needed | Yes | Yes | No |
| Sales-motion capability needed | Platform sales | Platform + attach motion | Distinct GTM |

## 10. Africa / Uganda overlay

- **SMB attach-rate ceilings** in Africa: typically 15-30% in Y1, 25-45% by Y3 — below US benchmarks (30-60%) due to price-sensitivity and budget cycles
- **Cannibalisation rates** in African SMB: 15-25% (higher than US 5-15%) due to budget pressure
- **Mobile-money debit consolidation** — Included packaging easier (single monthly debit) than Add-on (separate transaction friction)
- **Public-sector procurement** — Standalone strongly preferred (single line item, clear scope, clear SLA)
- **DFI / multilateral grant customers** — Standalone with milestone payment; transitions to Add-on or Included post-grant
- **Insurance / regulated-sector adoption** — Standalone packaging often required for regulatory scope discipline
- **Currency-of-record** — Included packaging in local currency simplifies SMB; Standalone in USD common for enterprise / cross-border
- **Local language packaging** — agents serving local-language customers may use channel-specific (USSD / WhatsApp) packaging that does not fit Included / Add-on / Standalone cleanly; document the hybrid
