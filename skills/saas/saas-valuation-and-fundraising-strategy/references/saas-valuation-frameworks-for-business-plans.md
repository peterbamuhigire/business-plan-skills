---
source: Cotton, Mersch, Bessemer State of the Cloud, SaaS Capital Index, OpenView, NVCA Yearbook
frameworks: [ARR Multiples, Rule of 40 adjustment, NRR adjustment, Burn Multiple adjustment, DCF, Berkus, Scorecard, Venture Method]
skill: saas-valuation-and-fundraising-strategy
cross-reference: [meta-valuation, saas-bankability-and-investor-readiness, saas-funding-stage-playbook]
---

# SaaS Valuation Frameworks for Business Plans

## 1. The ARR Multiple — the Industry Default

SaaS is valued primarily on **revenue multiples**, not earnings multiples. Why: in growth-stage SaaS, near-term earnings are deliberately suppressed by S&M investment, but ARR is real, recurring, and a leading indicator of future cash flow.

### Base multiple by growth rate (Bessemer / public-comparable data, normalised)

| YoY ARR growth | Base multiple (US public SaaS) | African private SaaS (US discount 30-50%) |
|---|---|---|
| <20% | 3-5× ARR | 2-3× |
| 20-30% | 5-8× | 3-5× |
| 30-50% | 8-12× | 5-8× |
| 50-75% | 12-18× | 8-12× |
| 75-100% | 18-25× | 12-15× |
| >100% | 25-40× | 15-20× |

### Rule of 40 adjustment

| Rule of 40 score | Multiple adjustment |
|---|---|
| <0 | -2 to -4× |
| 0-20 | -1 to -2× |
| 20-30 | -0.5 to -1× |
| 30-40 | baseline |
| 40-60 | +1 to +2× |
| 60-80 | +2 to +3× |
| >80 | +3 to +5× |

### NRR adjustment

| NRR | Multiple adjustment |
|---|---|
| <90% | -2× |
| 90-100% | -1× |
| 100-110% | baseline |
| 110-120% | +1× |
| 120-130% | +2× |
| >130% | +3× |

### Burn Multiple adjustment

| Burn Multiple | Multiple adjustment |
|---|---|
| <0.5 (FCF positive) | +2× |
| 0.5-1.5 | +0.5 to +1× |
| 1.5-2.0 | baseline |
| 2.0-3.0 | -0.5× |
| >3.0 | -1 to -2× |

### Worked example

Company: $5M ARR, 70% YoY growth, NRR 115%, Rule of 40 = 70+(-15) = 55, Burn Multiple = 1.2.

- Base multiple: 12× (for 70% growth, US public) = lower band 10×, upper 18×
- Rule of 40 adjustment: +1× (R40 between 40-60)
- NRR adjustment: +1× (NRR 110-120%)
- Burn Multiple adjustment: +0.5× (BM 0.5-1.5)
- US public adjusted: 12.5-20.5× ARR = $62.5M-$103M
- African private discount 40%: $37.5M-$62M valuation range

## 2. DCF for SaaS (>$20M ARR, near-profitable)

```
Year                    Y1   Y2   Y3   Y4   Y5   Y6   Y7   Y8   Y9   Y10  Terminal
Revenue                                                                  TV
- COGS
= Gross Profit
- S&M
- R&D
- G&A
= EBIT
- Tax (effective rate)
= NOPAT
+ D&A
- CapEx
- ΔWC (significant for growth SaaS)
= FCF
Discount factor (WACC)
PV of FCF
                                                                         TV at Y10:
                                                                         FCF_Y10 × (1+g) / (WACC-g)
                                                                         OR exit multiple × Y10 ARR

Enterprise Value = Σ PV of FCFs + PV of Terminal Value
- Net Debt
= Equity Value
```

WACC for African private SaaS: 12-18% (vs 10-12% US private SaaS).
Terminal growth rate: 2-3% (long-run inflation + minor real growth).

## 3. Berkus Method (pre-revenue / pre-PMF)

Maximum pre-money: $2.0-$2.5M. Add up to $500k for each of five factors (US), or scale down 40-60% for African early-stage:

| Factor | Max value (US) | African adjustment |
|---|---|---|
| Sound idea / base value | $0.5M | $0.2-0.3M |
| Prototype / reduced technology risk | $0.5M | $0.2-0.3M |
| Quality management team | $0.5M | $0.2-0.3M |
| Strategic relationships / reduced market risk | $0.5M | $0.2-0.3M |
| Product rollout / sales / reduced production risk | $0.5M | $0.2-0.3M |

Score each factor honestly; sum.

## 4. Scorecard Method (Bill Payne)

Find regional comparable median pre-money for similar stage / sector. Adjust by:
- Team strength (+/-30%)
- Size of opportunity (+/-25%)
- Product/Tech (+/-15%)
- Competitive environment (+/-10%)
- Marketing/Sales channel (+/-10%)
- Need for additional capital (+/-5%)
- Other (+/-5%)

## 5. Venture Method (work back from exit)

```
Target Exit Value (e.g. acquisition at $50M)
÷ Target IRR multiple over investment period (e.g. 10× over 7 years = ~38% IRR)
= Target Post-money valuation at investment
- Round size
= Pre-money valuation
```

Account for dilution from future rounds (typical: 2-3 more rounds before exit, each diluting 15-25%).

## 6. Comparables — finding the right ones

**Public-comparable benchmarks** (regularly updated):
- Bessemer Cloud Index (cloud100.bvp.com)
- SaaS Capital Index (saascapital.com)
- Meritech Capital comparables

**Private comparable databases:**
- Pitchbook (paid)
- Crunchbase (basic free; pro paid)
- Africa-specific: Partech Africa, Briter Bridges, Disrupt Africa, MEST Africa

**Africa-specific comparable rounds:**
- Briter Bridges quarterly funding reports
- Disrupt Africa annual reports
- Local-fund LP letters

## 7. Living-Plan Discipline for Valuation

- Refresh comparables quarterly
- Refresh multiples table annually (markets change)
- Re-value the company at major operational milestones (PMF, $1M ARR, $5M ARR, $10M ARR, profitability)
- Track plan-vs-actual on the inputs to multiples (growth, NRR, Burn Multiple) monthly

## 8. Africa / Uganda Application Notes

- Africa public-SaaS comparables are scarce (only a few — Andela, Flutterwave, Interswitch, MNT-Halan are not pure SaaS). Use US/Europe comparables with discount.
- Discount range for African private SaaS vs US public: 30-50% at growth stage, 50-70% at early stage.
- DFI / patient capital often pays a premium to pure-market price for ESG/impact value — useful arbitrage for African SaaS.
- Strategic buyers (Liquid, Safaricom, MTN, Telkom, big banks) often pay revenue multiples 1.5-3× higher than financial buyers because of strategic synergy.
- Local secondary market is thin; plans should not assume liquidity events on cap-table-locked timeframes.
