---
source: Outcome-pricing practice in agent businesses 2024-2026; ASC 606 / IFRS 15 variable-consideration constraint; engine synthesis from agent-SLA-commercial audit (2026)
frameworks: [Wins/loses test; Margin-volatility model; Constrained-revenue impact; Decision matrix; Dispute-resolution]
skill: saas-agent-outcome-pricing-business-case
cross-reference: [saas-agent-revenue-recognition-policy-template, saas-agent-refund-reserve-methodology, saas-agent-pricing-strategy]
---

# Outcome Pricing Business Case — Template + Worked Models

## 1. The wins test (must score 5+/7 to adopt)

| Test | Pass criterion |
|---|---|
| High TCV per customer | ACV >$10k (typically $25k+ for outcome pricing to be worth the measurement overhead) |
| Narrow, objectively measurable success definition | Outcome is binary or has clear quantitative thresholds; both parties agree on definition pre-contract |
| Low outcome variance | Outcome rate std dev < 20% of mean; range < 30pp |
| Short verification lag | < 7 days from action to verification |
| Clean attribution | Counter-party process attributes outcome to your action without ambiguity |
| Customer prefers risk-transfer | Customer states willingness to pay 1.5-3x more per outcome to pay only on success |
| Vendor cost-per-attempt low | Cost per attempt < 25% of per-outcome price |

## 2. The loses red flags (any 2+ → avoid outcome pricing)

- High outcome variance (std dev > 20%; range > 30pp)
- Attribution ambiguity
- Long verification lag (> 30 days)
- Counter-party can refuse verification
- Customer-side gaming risk (customer-marked outcomes)
- Low TCV
- High cost per attempt
- No reserve capacity for refund / dispute volatility

## 3. Margin-volatility model (worked)

**Scenario A — Collections agent on per-debt recovery (outcome pricing candidate)**

| Input | Value |
|---|---|
| Cost per attempt | $40 |
| Per-outcome price | $200 (12% of $1,666 recovered) |
| Attempts per customer per month | 100 |
| Expected outcome rate | 35% |
| Outcome rate std dev | 8pp |
| Outcome rate range | 20% - 50% |

| Scenario | Outcome rate | Contribution / customer / month |
|---|---|---|
| Best case | 50% | 50 × $200 - 100 × $40 = $6,000 |
| +1 std dev | 43% | 43 × $200 - 4,000 = $4,600 |
| Expected | 35% | 35 × $200 - 4,000 = $3,000 |
| -1 std dev | 27% | 27 × $200 - 4,000 = $1,400 |
| Worst plausible | 20% | 20 × $200 - 4,000 = $0 |
| -2 std dev | 19% | 19 × $200 - 4,000 = -$200 |
| Catastrophic | 12% | 12 × $200 - 4,000 = -$1,600 |

**Volatility ratio** = ($6,000 - $0) / $3,000 = 200% — very high

**Recommendation:** hybrid pricing
- Monthly floor: $1,500 per customer (covers 75% of cost)
- Per-outcome top-up: $150 per recovery (vs $200 pure outcome)
- Result: expected contribution at 35% = $1,500 + 35 × $150 - $4,000 = $2,750 (similar to pure outcome)
- Worst case at 20%: $1,500 + 20 × $150 - $4,000 = $500 (floor protects from loss)
- Volatility ratio reduced to ~100%

**Scenario B — Legal filing agent (outcome pricing fits)**

| Input | Value |
|---|---|
| Cost per attempt | $5 |
| Per-outcome price | $50 (per document filed and accepted) |
| Outcome rate | 95% |
| Outcome rate std dev | 2pp |

Even at worst case (89% acceptance), margin = 89 × $50 - 100 × $5 = $4,000 (per 100 attempts); contribution is robust. Outcome pricing adopted.

## 4. Constrained-revenue model

Under ASC 606 / IFRS 15, variable consideration is constrained to the amount probable not to reverse.

**Scenario A (collections):**
- Expected annual revenue (outcome rate 35%): 12 × 35 × $200 = $84,000 per customer
- Constraint: probable not to reverse = outcome rate ≥ 25%
- Constrained recognised revenue: 12 × 25 × $200 = $60,000 per customer
- Reserved upside (recognised as actuals come in): $24,000 per customer
- Recognised vs booked: 71% of expected

For investor reporting:
- Disclose the constraint
- Show the recognised vs expected gap
- Show how the gap closes over the year as outcomes verify

## 5. Decision matrix

| Customer / context | TCV | Variance | Lag | Attribution | Recommendation |
|---|---|---|---|---|---|
| Enterprise insurer claims | High | Low | Short | Clean | Outcome pricing |
| SMB collections | Medium | High | Short | Medium | Hybrid (floor + success) |
| Public-sector citizen-service | Medium | High | Long | Ambiguous | Per-resolution |
| Legal filing | Medium | Low | Short | Clean | Outcome pricing |
| Medical coding | Medium | Medium | Short-medium | Clean | Hybrid + refund reserve |
| Agri-advisory yield | Low | High | Very long | Ambiguous | Subscription |
| CX resolution | Medium | Low | Short | Customer-attributed | Per-resolution; outcome if customer accepts |

## 6. Dispute-resolution mechanism design

For outcome pricing to function commercially, design:

| Element | Specification |
|---|---|
| Success definition | In contract; specific and measurable; pre-agreed |
| Verification mechanism | Counter-party process / external evidence / both; named source |
| Dispute window | 14 days from outcome event |
| Dispute escalation | Customer Success → Head of CS → CFO + Legal (>$5k) |
| Evidence requirements | Audit log, telemetry, counter-party confirmation |
| Refund SLA | 14 days from dispute resolution |
| Reserve | Refund reserve sized at trailing dispute rate × forward outcome volume × adjustment |
| Insurance | E&O coverage scope-test; document gaps |

## 7. Investor narrative discipline

Tell the outcome-pricing story honestly:

- **Headline:** "We charge per verified outcome"
- **Margin volatility:** "Expected margin is X% with std dev Y; worst plausible is Z"
- **Mitigation:** "Floor + success structure protects against -2 std dev"
- **Recognition vs booking:** "Recognised revenue runs at 70-80% of expected under the variable-consideration constraint; the gap closes as outcomes verify"
- **Dispute discipline:** "Dispute rate trailing X%, dispute resolution Y days, reserve Z% of revenue"
- **Reserve adequacy:** "Refund reserve at $A; sized off trailing actual"

## 8. Cross-references

- Revenue recognition (variable consideration): `saas-agent-revenue-recognition-policy-template.md`
- Refund reserve: `saas-agent-refund-reserve-methodology.md`
- Pricing primitives: `saas-agent-pricing-strategy`
- Risk register: `saas-agent-sla-risk`
- Financial controls: `meta-agent-sla-financial-controls`

## 9. Africa / Uganda overlay

- **Collections / recovery outcome pricing in Africa** — viable but recovery-rate variance is wider than US benchmarks (15-55% range vs 20-50% US); hybrid pricing strongly recommended
- **Mobile-money settlement as verification** — for collections, M-Pesa / MoMo / Airtel Money payment confirmation = verification event; chain is robust
- **Public-sector outcome pricing in Africa** — verification lag 60-180 days through budget cycles; cash-conversion strain; prefer fixed-fee or per-resolution
- **DFI / multilateral milestone-pricing** — looks like outcome pricing; treat as performance-obligation-per-milestone
- **FX corridor on per-outcome price** — USD cost vs local-currency outcome; if outcome price quoted in local currency, FX swing erodes margin; quote in USD-equivalent or include FX-adjustment clause
- **Counter-party reliability in African contexts** — public-sector counter-party process can be slow / unreliable; document the risk
- **Insurance E&O coverage** — thin in Africa; reserve must absorb dispute cost where insurance does not cover
- **Outcome-pricing reserves for African insurer customers** — insurers themselves expect outcome pricing on agent vendors but require reserve evidence; provide it
