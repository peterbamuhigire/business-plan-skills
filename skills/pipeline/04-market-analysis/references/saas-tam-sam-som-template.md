---
source: Cotton, Mersch, OpenView, Bessemer State of the Cloud, Bottom-up / Tops-down methodology
frameworks: [TAM-SAM-SOM, Bottoms-up sizing, Tops-down sizing, Benchmark triangulation]
skill: 04-market-analysis
cross-reference: [saas-vertical-niche-selection, saas-icp-and-segmentation-template]
---

# SaaS TAM / SAM / SOM Template

## 1. The Definitions

- **TAM (Total Addressable Market)**: total annual revenue if 100% of the target market bought the product at the planned price
- **SAM (Serviceable Addressable Market)**: portion of TAM the company can realistically reach given product, geography, channel
- **SOM (Serviceable Obtainable Market)**: realistic market share the company can capture in the planned window (3-5 years)

## 2. The Three Sizing Methods (use all three; triangulate)

### A. Bottoms-up (most credible)

```
Number of potential customers in target ICP
× Average annual contract value (ACV) at planned pricing
= TAM (bottoms-up)
```

Worked example (Ugandan dairy cooperatives):
- ~2,500 registered dairy cooperatives in Uganda (UCDA + DDA registries)
- × UGX 9M average ACV at Tier 2 pricing
- = UGX 22.5 billion TAM (Uganda only)
- × 5 (East Africa cooperative count) = UGX 112.5 billion EAC TAM

### B. Tops-down (sanity-check)

```
Total industry revenue or industry IT spend (from industry reports)
× % spent on software / SaaS in the category
= Tops-down TAM
```

Worked example:
- Ugandan dairy sector ~$1.5B annual revenue (UBOS)
- × ~0.5% spend on cooperative-management technology (vertical SaaS benchmark)
- = $7.5M TAM (Uganda only) ≈ UGX 27.5B — directionally consistent with bottoms-up

### C. Benchmark triangulation

Find comparable companies in similar geographies:
- ARR / market-share / customer-count of comparable plays
- Implied total market from comparable's position

Example: Apollo Agriculture serves 1M+ farmers in Kenya at ~$XX revenue/year. If Ugandan dairy is 10% the size, the SaaS-addressable portion is 10% of Apollo's market.

## 3. SAM Computation

SAM filters TAM by:
- Geography (countries the plan will enter in 3-5 years)
- Segment (sub-tier: only cooperatives >100 farmers can afford Tier 2+)
- Channel reach (only cooperatives in MAAIF extension network = first reachable cohort)
- Regulatory (cooperatives must be registered → some informal groups excluded)

Worked example (Ugandan dairy):
- TAM: UGX 22.5B
- × 60% (cooperatives >100 farmers, can afford Tier 2+)
- × 80% (cooperatives in MAAIF extension network reach)
- × 95% (registered cooperatives)
- = SAM: UGX 10.3B

## 4. SOM Computation

SOM = SAM × realistic market share in the planning window.

Realistic market share by stage:
- Year 1: 0.5-2% of SAM
- Year 3: 5-15% of SAM
- Year 5: 15-30% of SAM (if winning)

Worked example (Year 3 target):
- SAM: UGX 10.3B
- × 12% (Year 3 reasonable share)
- = SOM: UGX 1.24B Year 3 revenue
- ↔ this should reconcile with the Year 3 ARR target in Section 10

## 5. Validation Checks

- Bottoms-up and tops-down should be within 50% of each other; if not, dig in
- SAM is typically 10-30% of TAM (more for narrow vertical; less for broad horizontal)
- SOM is typically 5-25% of SAM in 3-5 years (if you're winning)
- SOM should reconcile with the financial projection ARR

## 6. Living-Plan Cadence

- Annual TAM/SAM refresh
- Quarterly SAM check if entering new geographies / segments
- Trigger-replan if regulatory or major competitor move materially changes the addressable space

## 7. Africa / Uganda Application Notes

- Industry data is often less granular in African markets — supplement with local registries (NSSF, regulators, sector federations)
- Multi-country expansion within Africa multiplies TAM but doesn't multiply SAM equally — each country has different reach economics
- Currency: present TAM/SAM/SOM in both local currency and USD
- Formal vs informal: many African industries have large informal segments — be explicit about whether those are in TAM
- Public-sector / NGO segment: often a separate sizing because pricing dynamics differ
- Donor-funded segment: third bucket with grant-cycle dynamics
- Vertical-by-geography intersection is often the most credible SAM — "dairy cooperatives in East Africa with >100 farmers and existing M-Pesa / MoMo usage"
