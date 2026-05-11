---
source: John Doerr (OKR), Christina Wodtke, Andy Grove, Cotton MSPOT, Klaus Wertenbroch (KPI trees)
frameworks: [North-Star Metric, KPI Tree, OKR cascade, Living-Plan integration]
skill: meta-living-plan-governance
cross-reference: [meta-monitoring-evaluation, meta-quarterly-gameplan, saas-unit-economics-and-cohort-model]
---

# SaaS OKR & KPI Tree Template

## 1. The North-Star Metric (NSM)

Every SaaS company should have one North-Star Metric — the single number that best represents whether the company is creating customer value.

| Company type | Typical NSM |
|---|---|
| Marketplaces | Gross Merchandise Value (GMV) |
| Communication SaaS | Daily active conversations / messages |
| Productivity SaaS | Weekly active users completing key workflow |
| Vertical SaaS | Customers reaching activation milestone |
| Fintech SaaS | Transactions per active customer per month |

Worked example (Ugandan dairy SaaS):
- **NSM**: "Cooperatives that recorded ≥80% of monthly milk transactions in the platform"
- Not ARR (lagging), not signups (vanity), but value-delivery proxy.

## 2. The KPI Tree (cascading)

Decompose NSM into KPIs that drive it:

```
NORTH-STAR: Cooperatives with ≥80% transaction capture (= "active cooperatives")
│
├── Acquisition: New cooperatives onboarded / month
│    ├── Marketing-qualified leads (MQLs)
│    │    ├── SEO traffic
│    │    ├── WhatsApp inquiries
│    │    └── Partner-referred leads
│    └── MQL → Customer conversion rate
│
├── Activation: % of new customers reaching ≥80% capture in 90 days
│    ├── Time-to-first-transaction
│    ├── Onboarding milestones hit
│    └── Field-officer engagement rate
│
├── Retention: Active cooperative retention rate
│    ├── Monthly platform-usage frequency
│    ├── Payment-success rate
│    └── Customer health score
│
├── Expansion: Average modules per active cooperative
│    ├── Module-attach rate
│    ├── Per-cooperative farmer growth
│    └── Tier-upgrade rate
│
└── Referral: Customers acquired via existing customer reference
     ├── NPS
     ├── Reference willingness
     └── Co-marketing engagement
```

Every leaf is an actionable metric. Every branch is a strategic lever.

## 3. The OKR Cascade

OKRs operationalise the KPI tree into time-bound goals.

### Company OKR (Annual)
```
OBJECTIVE: Become Uganda's primary dairy-cooperative operating system.

KEY RESULTS:
KR1: Reach 80 active cooperatives by year-end (vs 35 starting)
KR2: Achieve >75% activation rate for new cohorts (vs 55% baseline)
KR3: Net Revenue Retention >110% (vs 95% baseline)
KR4: Rule of 40 score ≥30 (vs 15 baseline)
```

### Department / Team OKRs (Quarterly)

#### Sales Q3 OKR
```
OBJECTIVE: Build the repeatable solution-sales motion.
KR1: Close 15 new cooperatives (vs 8 in Q2)
KR2: Reduce sales-cycle length to 75 days median (vs 95)
KR3: Win rate >35% on qualified opportunities (vs 28%)
KR4: Build pipeline 3.5× quota (vs 2.8×)
```

#### Customer Success Q3 OKR
```
OBJECTIVE: Lift activation and reduce churn.
KR1: New-cohort activation rate >75% by end-quarter
KR2: Gross logo churn <1.8% monthly (vs 2.5% baseline)
KR3: NRR 108% (vs 102%)
KR4: NPS >40 (vs 28)
```

#### Product Q3 OKR
```
OBJECTIVE: Ship the modules that drive expansion.
KR1: Launch Module-3 (farmer-scoring) with ≥20 cooperatives using
KR2: Reduce time-to-first-transaction to <14 days (vs 22)
KR3: Increase weekly usage depth from 3.2 to 4.5 features/week per cooperative
```

## 4. OKR Discipline (Doerr / Wodtke)

- 3-5 OKRs per quarter at company level
- 3-5 KRs per O, each measurable and ambitious
- 70% of KRs achieved = healthy stretch (100% = sandbagging; 50% = overstretching)
- Owner per KR (not "the team")
- Review at MBR (monthly progress) + QBR (quarter-end scoring)

## 5. Integration with MSPOT

OKRs operationalise MSPOT:

| MSPOT field | OKR mapping |
|---|---|
| Mission | unchanged framing |
| Strategy | the annual O at company level |
| Projects | the KRs and the resourced initiatives |
| Omissions | the things that didn't make the KRs |
| Tracking | the KPI tree dashboard |

## 6. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| KPI dashboard | Daily/Weekly | CFO + Heads |
| OKR progress check-in | Bi-weekly | OKR owners + manager |
| Monthly progress review | Monthly | CEO + Heads |
| Quarterly OKR score + new OKR set | Quarterly | Company-wide |
| KPI tree refresh | Annually | CEO + Heads |
| NSM review | Annually | CEO + Board |

## 7. Anti-Patterns

- **KPIs that aren't tied to NSM** — vanity metrics with no decision implication
- **OKRs that are tasks** ("Launch X by Dec") rather than outcomes ("Achieve X usage by Dec")
- **Too many OKRs** — focus dilution
- **OKRs without owners** — group accountability is no accountability
- **No KR ambition** — 100% achievement signals OKRs are too easy
- **Static KPI tree** — the tree should refresh as the business evolves

## 8. Africa / Uganda Application Notes

- **NSM definition often differs** for African SaaS — value-delivery proxy matters more than ARR because customer growth feeds ARR with lag.
- **Activation metrics are leading indicators** of African SaaS health because of payment-rail churn lag.
- **OKR cadence in African business culture** — quarterly review can fold into the EAC / Kenya / Nigeria business calendars (Q1 January cycle is dominant).
- **Public-sector / NGO customer OKRs** may need separate cadence (donor-cycle alignment).
- **WhatsApp-based OKR check-ins** with field teams who are not at HQ are increasingly common.
- **OKR translation** — for multi-language teams, KR formulations should be available in working languages of the team.
