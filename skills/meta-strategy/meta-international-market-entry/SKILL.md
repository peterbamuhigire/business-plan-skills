---
name: meta-international-market-entry
description: Use when choosing which foreign or regional market to enter and how, using Porter's Diamond, CAGE distance, institutional voids, defender retaliation and entry-mode choice (export, licensing, franchise, joint venture, subsidiary); distinguishes `04-market-analysis`, which sizes and describes a market.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# International Market Entry

Decide whether to expand beyond the home market, which country to enter first and by which mode, with a staged plan and kill criteria. Method sources: Johnson et al. (2017) *Exploring Strategy*, 11th edn, Pearson, chapter 9 (Yip drivers, Porter's Diamond, CAGE, institutional voids, retaliation, entry modes); Wheelen et al. (2018) *Concepts in Strategic Management and Business Policy*, 15th edn, Pearson, chapter 9 (entry-mode ladder, alliance fit, international control). The governing judgement: attractiveness alone never selects a country; distance, missing institutions and the incumbent's response decide whether the firm can win there.

<!-- dual-compat-start -->
## Use When

- A Ugandan or East African firm plans to sell into Kenya, Rwanda, Tanzania, South Sudan, the DRC or another country, and the plan must justify the country order and entry mode.
- A plan or marketing plan needs a market-selection exhibit comparing two to five candidate countries or regions.
- The owner must choose between exporting, licensing, franchising, a distributor, a joint venture or its own subsidiary.
- A foreign firm entering Uganda needs the same analysis from the other side (institutional voids, local-partner need, entry mode).

## Do Not Use When

- Use `04-market-analysis` instead to size and describe a chosen market; this skill decides which market and how to enter it.
- Use `ecommerce-unit-economics-and-cross-border-margin-model` instead for landed-cost and margin modelling of cross-border e-commerce.
- Use `meta-strategic-options-evaluation` instead when international expansion is one option among several strategic directions still being screened.
- Use the relevant `country-context/` file for a country's tax, regulatory and banking facts; this skill only lists the checks to run.
- Do not assert tariffs, rules of origin, licensing rules, tax rates or market statistics from memory; they are checks for the Digital research engine.

## Required Inputs

| Input artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Expansion objective, budget ceiling and time horizon | Owner or board | Yes | Stop; country ranking needs a stated objective and a limit on what can be committed. |
| Home-market advantage evidence | `meta-strategic-factor-analysis`, `06-competitive-analysis` | Yes | Run the Diamond and VRIO check first; do not rank countries for a firm with no transferable advantage. |
| Candidate countries (two to five) | Owner, `04-market-analysis` | Yes | Propose candidates from existing customers, trade corridors and diaspora demand, labelled provisional. |
| Country evidence: demand, rules, institutions, competitors | Digital research engine, `country-context/`, 04 trade references | Yes | Keep every country cell `VERIFY`; rank provisionally and cap confidence. |
| Product, margin and logistics data | `03`, `08`, `10`, finance owner | Conditional | Compare modes qualitatively; mark economics `not assessed`. |

## Workflow

1. State the objective and test the push: small home market, customers already buying from abroad, cost or learning gains. Stop if expansion is a response to home-market decline with no transferable advantage; recover by returning to options evaluation.
2. Identify the home-based advantage with Porter's Diamond (factor conditions, demanding home customers, related and supporting industries, domestic rivalry) and confirm it passes VRIO. Use [the market-selection reference](references/market-selection-cage-voids-diamond.md).
3. Screen candidates in three layers: a PESTEL country ranking, an institutional-voids check, and CAGE distance for this firm (cultural, administrative, geographic, economic).
4. Assess the defender in each candidate: attractiveness to us, the incumbent's reactiveness and clout. Re-rank; a lower-ranked but less-defended market may come first.
5. Choose the entry mode by weighing commitment, control, risk, speed and the voids found. Use [the entry-mode reference](references/entry-mode-choice-and-staging.md).
6. Link to trade frameworks: check EAC common-market and AfCFTA provisions relevant to the product through the 04 references and the Digital research engine, recording each as a dated check, never as a remembered rule.
7. Write a staged entry plan: pilot scope, milestones, investment per stage, kill criteria, and control arrangements. Block the recommendation if any Critical country check is `not assessed` and no mitigation exists.
8. Hand off: the chosen market to `04` for sizing, entry economics to `10`, partner and structure questions to the finance doctrine and legal review, country risks to `12`.

## Quality Standards

- The home-based advantage is named and shown to travel; the plan does not export a threshold quality.
- Every candidate country has a completed CAGE row, an institutional-voids row and a defender row, each with dated evidence or a `VERIFY` flag.
- Country facts (tariffs, rules of origin, licences, tax, currency controls, market data) are cited with source and date or listed as checks; none is asserted from memory.
- The entry mode is justified against at least two alternatives on commitment, control, risk and speed.
- The staged plan has a pilot, a budget per stage and a written kill criterion.

## Anti-Patterns

- Picking the largest or richest market first. Fix: add CAGE distance, institutional voids and defender reactiveness, then re-rank.
- Treating EAC membership as proof of easy access. Fix: check product-specific rules, standards, permits and non-tariff barriers through the Digital research engine and record the date checked.
- Setting up a subsidiary before proving demand. Fix: start with export, a distributor or a pilot partner and scale on evidence.
- Licensing away the distinctive competence. Fix: license only what rivals cannot turn against you; keep the core capability in-house.
- A joint venture with no exit or renegotiation clause. Fix: agree roles, dispute resolution, renegotiation and exit terms at formation.
- Assuming a service business travels like a product. Fix: plan for regulation, cultural fit and local presence, which make services harder to take abroad.

## Outputs

| Output artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Home-advantage statement (Diamond plus VRIO) | Owner, `06`, marketing plan | Names the advantage and why it transfers. |
| Country screening matrix (PESTEL, voids, CAGE, defender) | Board, funder, `04-market-analysis` | Two to five countries, every cell evidenced or flagged, re-ranked with reasons. |
| Entry-mode decision | `08-operations-plan`, `11-funding-request`, finance doctrine | Chosen mode compared with at least two alternatives. |
| Staged entry plan with kill criteria | `13-implementation-timeline`, `12-risk-analysis` | Pilot, stage budgets, milestones and kill criteria stated. |
| Country check list | Digital research engine, `country-context/` owners | Each check has an owner, source route and date. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Country evidence register | Table: country, claim, source, date checked, status | No country fact appears without source and date or a `VERIFY` flag. |
| Screening trace | Matrix with scores and re-ranking notes | A reviewer can see why the first market was chosen. |
| Mode comparison | Table of modes against commitment, control, risk, speed | The trade-off behind the chosen mode is visible. |

<!-- dual-compat-end -->
## Capability Contract

Permission boundary: analysis and drafting only unless the engagement owner has authorised more. Read and search supplied evidence, the 04 trade references and `country-context/` files; draft the screening, mode choice and staged plan. Current country, trade, tax and regulatory facts come only from the Digital research engine or the dated source register. Structure, transfer-pricing, withholding, VAT and permanent-establishment questions route to the Chwezi finance doctrine and legal review. Do not contact partners, sign heads of terms, register entities or commit funds without explicit authority.

## Degraded Mode

Without network research or country files, produce the framework with every country cell marked `VERIFY`, rank only on the firm's own evidence (customers, partners, logistics experience), mark the ranking provisional, narrow the recommendation to a qualified shortlist, and list the checks that would confirm it. Never treat an unverified trade rule as favourable.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| No home-based advantage passes VRIO | Stop expansion; return to options evaluation | Exporting a business that only survives on home familiarity. |
| Institutional voids are high (weak contract enforcement, few distributors, no market data) | Prefer a local partner, distributor or joint venture over a wholly owned entry | Losing control and cash in a market the firm cannot read. |
| The top-ranked market has a highly reactive, powerful incumbent | Consider entering a less-defended market first and plan for retaliation elsewhere | Triggering a price war on the incumbent's home ground. |
| Demand is unproven in the target country | Enter by export or distributor pilot with a kill criterion | Sunk subsidiary costs before evidence. |
| A partner would receive the distinctive competence | Restructure the deal or choose another mode | Creating a future competitor. |
| A Critical country check (licence, product standard, currency control) is `not assessed` | Block the recommendation until verified or mitigated | Plans built on an unverified permission. |

## Worked Example

A Kampala digital agency weighs Kigali, Nairobi and Juba (all facts to be verified). Diamond: its advantage is bilingual mobile-first campaign work for regional NGOs, built on demanding donor clients at home. CAGE: Nairobi is close culturally and administratively but has strong local agencies; Kigali has formal norms and French and Kinyarwanda needs; Juba has the highest institutional voids. Defender: Nairobi incumbents are reactive and well connected, so Nairobi drops from first to second. Mode: Kigali by a partnership with a local studio for six months, with a kill criterion of three signed retainers by month six; Juba only by project export to existing NGO clients. Tax and registration questions go to the finance doctrine and `country-context/` checks.

## References

- [Market selection: Diamond, CAGE, institutional voids and defender retaliation](references/market-selection-cage-voids-diamond.md) - read at steps 2 to 4 for procedures and templates.
- [Entry-mode choice and staging](references/entry-mode-choice-and-staging.md) - read at steps 5 to 7 for the mode ladder, alliance checklist and staged plan.
- [AfCFTA and East African trade framework](../../pipeline/04-market-analysis/references/afcfta-ea-trade-framework.md) - read at step 6 for trade-framework context; verify every rule's current status.
- [EAC common market framework](../../pipeline/04-market-analysis/references/eac-common-market-framework.md) - read at step 6 for movement of goods, services, workers and establishment rights.
- [Market type and entry analysis](../../pipeline/04-market-analysis/references/market-type-entry-analysis.md) - read for market-type and cost-of-entry logic in the chosen market.
- [Country context index](../../../country-context/INDEX.md) - read for available country files before any country claim.

## Read Next

- `04-market-analysis` - when the chosen market must be sized and described.
- `meta-strategic-options-evaluation` - when expansion competes with other strategic options.
- `ecommerce-unit-economics-and-cross-border-margin-model` - when cross-border margins decide the mode.
