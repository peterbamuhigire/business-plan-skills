---
name: meta-strategic-factor-analysis
description: Use when turning a PESTEL and five-forces scan into weighted EFAS, IFAS and SFAS tables and a TOWS matrix of candidate strategies; distinguishes `06-competitive-analysis`, which writes the competitor section, and `meta-strategic-options-evaluation`, which chooses between the options.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Strategic Factor Analysis

Reduce a situation scan to fewer than ten weighted, rated and justified strategic factors, then derive candidate strategies from them. The governing judgement: a factor list without weights, ratings, evidence and time horizons is opinion, and a strategy that answers no weighted factor is unanchored.

<!-- dual-compat-start -->
## Use When

- A business plan, marketing plan, turnaround plan or strategy review needs a disciplined situation analysis instead of a free-form SWOT.
- PESTEL drivers and five-forces ratings must be converted into EFAS (external) and IFAS (internal) weighted tables, condensed into an SFAS, and turned into a TOWS matrix.
- A marketing-plan situation analysis, section 04 key-driver summary or section 06 SWOT needs weighted factor evidence to consume.
- An existing SWOT has more than six items per box, parity strengths or generic opportunities and must be rebuilt.

## Do Not Use When

- Use `06-competitive-analysis` instead to write the plan's competitor section, competitor profiles and positioning narrative; this skill supplies its factor tables.
- Use `meta-strategic-options-evaluation` instead to choose between candidate strategies with SAFe, the strategy clock and the strategy-statement gate.
- Use `04-market-analysis` instead to size a market; use `meta-strategic-audit` for a read-only diagnostic of an existing organisation's whole strategy.
- Do not use when no evidence exists about the market, competitors or the firm's own performance; return the evidence gap list instead.

## Required Inputs

| Input artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Decision brief: organisation, scope, geography, horizon, audience | `00-client-intake` or engagement owner | Yes | Stop; weights cannot be set without knowing whose strategic position is being scored. |
| Macro-environment evidence (PESTEL, nonmarket, climate and political exposure) | `04-market-analysis`, Digital research engine, `country-context/` files | Yes | Build the driver list as hypotheses, mark each `VERIFY`, and cap confidence at low. |
| Industry evidence (rivals, buyers, suppliers, substitutes, entrants, complementors) | `04-market-analysis/references/industry-structure-porter.md`, `06-competitive-analysis` | Yes | Rate only the forces with evidence; mark the rest `not assessed`. |
| Internal evidence (financials, operating data, capabilities, team, culture) | Client records, `02`, `03`, `08`, `09`, `10` owners | Yes | Score IFAS factors from interviews only, flagged as management opinion. |
| Competitor or peer comparison for strengths | `06-competitive-analysis`, benchmark data | Conditional | Treat unverified strengths as parity items until a comparison exists. |

## Workflow

1. Confirm the decision, the unit being scored (company, business unit, programme) and the planning horizon. Stop if the unit is ambiguous; recover by asking which entity the plan funds or governs.
2. Scan PESTEL with market and nonmarket tags, then distil three to five key drivers, each with a "so what" for this organisation. Use [the situation-scan procedure](references/situation-scan-pestel-and-forces.md).
3. Define the industry (product, customer, geography, value-chain stage), rate each of the five forces plus complementors High / Medium / Low on named drivers, and record the direction of change over three to five years.
4. Build the EFAS: eight to ten opportunities and threats, weights summing to 1.00, each rated on the **Wheelen and Hunger 1-to-5 response scale** (5 = outstanding response, 3 = average, 1 = poor), weighted score, and a mandatory comment with evidence. Follow [the weighted-factor procedure](references/weighted-factor-tables-efas-ifas-sfas.md).
5. Build the IFAS the same way for eight to ten strengths and weaknesses. Admit a strength only if it passes VRIO against the firm's past, its named rivals and the industry; otherwise record it as parity or weakness.
6. Condense to an SFAS of fewer than ten factors: tag S, W, O or T (dual tags allowed), re-weight to 1.00, carry ratings, add the duration column (short under 1 year, intermediate 1 to 3 years, long over 3 years), and sanity-check the total against actual profitability and share. Block the SFAS if any factor did not appear in the scan.
7. Build the TOWS matrix from SFAS factors only; generate SO, ST, WO and WT candidate strategies that cite factor IDs. Test each against the four alternative criteria (mutually exclusive, likely to succeed, complete, internally consistent) and return the survivors to `meta-strategic-options-evaluation`.
8. Run acceptance checks, then hand off: tables to `06`, drivers to `04`, SFAS and TOWS to the marketing-plan situation analysis and to options evaluation. Revise and re-run affected steps when a consumer returns a contradiction.

## Quality Standards

- One rating scale is used and stated in every table header: Wheelen and Hunger 1 to 5, average 3.0. A deliverable never mixes it with the 1-to-4 EFE/IFE convention.
- Every table's weights sum to exactly 1.00, and every row has a comment naming its evidence and source grade.
- No box in the SWOT/TOWS carries more than six items; strengths are relative to named competitors, not parity qualities.
- Every SFAS factor traces back to a scan row; every TOWS strategy cites at least one S or W and one O or T factor ID.
- Weighted totals are presented as structured judgement, never as measurement, and are checked against actual performance.

## Anti-Patterns

- Listing twelve strengths such as "good customer service" and "experienced staff". Fix: keep only VRIO-tested differences against named rivals; move parity items out.
- Weights that sum to 1.10 or ratings on an unstated scale. Fix: normalise weights to 1.00 and print the scale in the header of every table.
- Rating the size of an opportunity instead of management's response to it. Fix: weight carries importance; the 1-to-5 rating scores how well the firm is responding today.
- Introducing a new factor in the SFAS or TOWS that the scan never examined. Fix: return to step 2 or 5, evidence the factor, then carry it forward.
- A TOWS matrix built from the raw SWOT with thirty unranked ideas. Fix: build it from the SFAS only and test each option against the four criteria.
- Opportunities the firm has no capacity to exploit. Fix: apply the opportunity-divided-by-capacity test and either fund the capability or drop the opportunity.

## Outputs

| Output artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Key-driver summary (PESTEL to three to five drivers) | `04-market-analysis`, marketing-plan situation analysis | Each driver has evidence, a direction and an implication for this organisation. |
| Five-forces-plus-complementors rating | `04-market-analysis`, `06-competitive-analysis` | Industry defined; each force rated on named drivers with a three-to-five-year direction. |
| EFAS, IFAS and SFAS tables | `06-competitive-analysis`, `meta-strategic-options-evaluation`, marketing-plan orchestrator | Weights sum to 1.00; scale stated; comments evidenced; SFAS under ten factors with durations. |
| TOWS matrix with candidate strategies | `meta-strategic-options-evaluation`, `07`, marketing plan | Each candidate cites factor IDs and passes the four alternative criteria or is marked rejected. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Factor evidence register | Table: factor ID, tag, evidence, source, source grade (A-E, 1-5), date | A reviewer can trace every weight and rating to a source or a labelled management judgement. |
| Weight and scale check | Totals row per table plus scale statement | Weights equal 1.00; one scale; totals compared with actual profit and share. |
| Rejected-factor and rejected-option log | List with reason | Items cut from the scan or TOWS are visible with the reason. |

<!-- dual-compat-end -->
## Capability Contract

Permission boundary: analysis and drafting only unless the engagement owner has authorised more. Read and search supplied evidence, `country-context/` files and neighbouring section outputs. Drafting factor tables and candidate strategies is permitted within the engagement's authority. Current market, regulatory or country facts come from the Digital research engine or the dated source register; do not state them from memory. Do not publish, contact third parties or present weighted scores as audited measurement. Finance facts behind internal factors follow the Chwezi finance doctrine.

## Degraded Mode

Without network research, competitor data or internal records, produce the tables with every unverified row flagged `VERIFY` or `management opinion`, cap confidence, and mark the affected checks `not assessed`. Return the narrowest qualified SFAS that the evidence supports plus the evidence gaps that would change weights. Never convert a missing comparison into a confirmed strength.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A claimed strength is matched by two or more named rivals | Record it as parity (table stakes), not a strength | Strategy built on an advantage competitors already hold. |
| A factor is both an opportunity and a threat | Dual-tag it (O+T) in the SFAS and weight it once | Double counting that inflates its importance. |
| EFAS or IFAS total diverges sharply from actual profit and share | Re-examine weights and ratings with the client before proceeding | Scores that flatter management and mislead the reader. |
| The client or another deliverable uses the 1-to-4 EFE/IFE scale | Convert to the 1-to-5 scale and state the conversion, or keep one scale for the whole deliverable | Mixed scales producing incomparable totals. |
| Evidence exists for fewer than eight factors | Produce a shorter table, state the gap, do not pad | Invented factors that fill a template. |
| A TOWS option cannot cite factor IDs | Drop it or return to the scan | Wish-list strategies with no analytical anchor. |

## Worked Example

A Mbarara dairy processor asks for a marketing-plan situation analysis. The scan yields fourteen candidate external factors; ranking and weighting keeps eight, with drought and feed-price volatility (T, 0.15, rated 2.0) and larger regional processors' price pressure (T, 0.15, rated 2.5) among the heaviest. The EFAS totals 2.80 on the Wheelen and Hunger 1-to-5 scale, below the 3.0 average, which matches the firm's falling margin. The SFAS keeps seven factors with durations; the TOWS yields a WT option (forward supply contracts with farmer cooperatives) and an SO option (freshness-led positioning in Kampala supermarkets), both passed to options evaluation. All figures are illustrative; the full tables are in [the worked example](references/worked-example-ugandan-dairy.md).

## References

- [Situation scan: PESTEL to key drivers and five forces with complementors](references/situation-scan-pestel-and-forces.md) - read at steps 2 and 3 for the scan procedure, nonmarket tags and force-rating drivers.
- [Weighted-factor tables: EFAS, IFAS, SFAS and TOWS](references/weighted-factor-tables-efas-ifas-sfas.md) - read at steps 4 to 7 for the full procedure, the rating scale, blank templates and the TOWS rules.
- [Worked Ugandan example (illustrative)](references/worked-example-ugandan-dairy.md) - read when a complete filled set of tables is needed as a pattern.
- [Country context index](../../../country-context/INDEX.md) - read before rating any country-specific driver.

## Read Next

- `meta-strategic-options-evaluation` - when the TOWS candidates must be screened and one strategy chosen.
- `06-competitive-analysis` - when the factor tables feed the written competitor section.
- `meta-strategic-audit` - when the whole existing strategy of an organisation needs a read-only diagnostic.
- `meta-business-model-design` - when the weak factors point at the business model rather than the strategy.
