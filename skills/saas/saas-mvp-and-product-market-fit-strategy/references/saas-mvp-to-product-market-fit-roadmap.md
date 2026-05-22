---
source: Walling (SaaS Playbook); Sean Ellis; Rachleff; Garbugli activation; Hansen (Deploy Empathy)
frameworks: [PMF signals; Sean Ellis 40%; Retention curve; MVP scoping; Pivot framework]
skill: saas-mvp-and-product-market-fit-strategy
cross-reference: [saas-vertical-niche-selection, saas-unit-economics-and-cohort-model, idea-testing]
---

# SaaS MVP-to-PMF Roadmap

## 1. PMF Signals (use multiple; no single signal is sufficient)

### A. Sean Ellis 40% Test
Survey users: "How would you feel if you could no longer use this product?"
- Very disappointed
- Somewhat disappointed
- Not disappointed

PMF threshold: ≥40% say "Very disappointed."

### B. Retention Curve Flattening
Plot cohort retention curves (per `saas-cohort-and-retention-model-template.md`). PMF signal:
- After month 3-4, the curve flattens (doesn't continue declining)
- Plateau at >60% (consumer) / >75% (B2B SMB) / >85% (enterprise)

### C. Organic Referral Rate
≥25% of new signups come from word-of-mouth without paid acquisition.

### D. The Walling Shortcut
$10-20k MRR with stable retention. Below this, claims of PMF are usually premature.

### E. NPS Threshold
NPS ≥ 30 for B2B SMB; ≥ 40 for vertical SaaS; ≥ 50 for enterprise.

## 2. The Three Gates (Walling)

```
MVP (you've built something)
        │
        ▼
PMF (people want it and pay for it)
        │
        ▼
ESCAPE VELOCITY (you can find more of them every week)
        │
        ▼
SCALE (multiple channels, multiple segments, repeatable motion)
```

Most plans confuse these gates. Each gate requires different inputs, different metrics, different team.

## 3. MVP Scoping (the discipline of saying no)

The MVP is the smallest product that delivers value to the ICP. Discipline:

**INCLUDE:**
- The single core workflow your ICP needs
- The minimal integrations required (payment, identity)
- Just enough admin / settings to make it usable

**EXCLUDE:**
- Multi-tenant control plane (until you have 5+ paying customers)
- Anything that another product already solves (use integrations)
- Features that would impress a tier you're not targeting
- Localisation (one language first)
- Mobile app (if web works; or vice versa)
- Anything an advisor recommends but no customer has asked for

**Time budget:** MVP should ship in 12-26 weeks of solo / pair engineering. If it takes 12 months, the MVP is too big.

## 4. Customer-Conversation Cadence (Walling)

Pre-PMF, the founder must run:
- **10+ customer interviews per month** (prospect, customer, churned, not-bought)
- Logged in a shared doc
- Quarterly synthesis of patterns
- Insights feed product roadmap, positioning, pricing, ICP

This is non-delegable until PMF.

## 5. Feature Triage (Walling)

Every feature request falls in:

- **Crackpot** (10-15%): outside vision / capability — say no
- **No-Brainer** (15-25%): build now
- **In-Between** (60-75%): apply three filters
  1. What's the use case?
  2. What % of customers will use it?
  3. Does it fit the product vision?

## 6. The Pivot Framework

When the gate isn't reaching, pivot intelligently:

| Signal | Pivot type |
|---|---|
| Customer pull but wrong segment | **Segment pivot** — same product, different ICP |
| Segment right but feature mismatch | **Feature pivot** — keep customers, rebuild features |
| Both right but unit economics fail | **Pricing / packaging pivot** — same product, different price architecture |
| Channel works but customer doesn't | **Channel pivot** — different acquisition channel |
| Nothing working | **Category pivot** — different problem space |

Quarterly pivot-vs-persevere decision. Don't pivot prematurely (3 quarters minimum on a thesis); don't persevere when the signal is dead.

## 7. The 12-Month Path to PMF (illustrative)

```
Quarter 1: MVP Build
- Solo / pair build
- 10+ customer interviews/month (founder)
- First 5 design partners onboarded (free or paid pilot)
- Crackpot/No-Brainer/In-Between log started

Quarter 2: Iteration
- Ship core workflow improvements
- 5-10 paying customers
- First retention cohort visible (3 months of data)
- Pricing experiment 1

Quarter 3: Activation Discipline
- Ship onboarding milestones
- First Sean Ellis survey
- 15-25 paying customers
- Activation rate measured per cohort
- Pricing experiment 2

Quarter 4: PMF Test
- Sean Ellis ≥40%?
- Retention curve flattening?
- Organic referral ≥25%?
- MRR $10-20k?
- → DECISION: PMF achieved, pivot, or persevere?
```

## 8. Escape Velocity (post-PMF)

Once PMF is achieved, the gate is **repeatable acquisition**:
- One channel with sustained, predictable customer flow
- CAC payback <18 months
- Channel-CAC stable as spend scales

Most companies take 6-18 months post-PMF to reach Escape Velocity. This is when the first VP Sales / Head of Marketing hire becomes appropriate.

## 9. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Customer-conversation log | Weekly (founder) | Founder |
| Feature triage log | Continuous | Founder / Head of Product |
| Sean Ellis test | Quarterly | CEO + Head of Product |
| Retention cohort review | Monthly | Founder + CFO |
| Pivot-vs-persevere decision | Quarterly | Founder + Board |
| MVP-to-PMF roadmap review | Quarterly | Founder + Investors |

## 10. Africa / Uganda Application Notes

- **In-person customer interviews** disproportionately powerful — WhatsApp-to-coffee-meeting funnel for first 50 design partners.
- **Vertical-first MVP** is the structural default for African SaaS — local-context expertise is the moat.
- **PMF MRR threshold in African SaaS** is often $5-10k (vs Walling's $10-20k) because TAM and ARPU are smaller; adjust signal threshold.
- **Pilot / design-partner pricing**: free or steeply discounted pilots are common, but require explicit conversion-to-paid plan with timeline (don't drift into perpetual free pilots).
- **Multi-language onboarding** may be required from MVP for vertical-specific markets (Luganda for dairy cooperatives; Swahili for Kenya / Tanzania).
- **Mobile-first / offline-first**: many African ICPs require these from MVP; designing them in later is much more expensive.
- **NGO / donor-funded pilots**: can be a useful early-stage revenue source but the pivot to commercial customers must be planned — donor cycles don't sustain a company.
