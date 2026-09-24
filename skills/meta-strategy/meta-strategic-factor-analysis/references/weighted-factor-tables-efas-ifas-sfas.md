# Weighted-factor tables: EFAS, IFAS, SFAS and TOWS

Parent: [Strategic Factor Analysis](../SKILL.md)

Full procedure, rating scale and blank templates for workflow steps 4 to 7. The EFAS, IFAS and SFAS instruments follow Wheelen, T.L., Hunger, J.D., Hoffman, A.N. and Bamford, C.E. (2018) *Concepts in Strategic Management and Business Policy*, 15th edn, Pearson. That edition carries no TOWS matrix; the TOWS step below is this engine's synthesis, built on the SFAS so that only weighted factors generate options. The comparative-SWOT listing rules follow Johnson et al. (2017) *Exploring Strategy*, 11th edn, Pearson.

## 1. The rating scale (one scale for the whole deliverable)

This engine uses the **Wheelen and Hunger 1-to-5 response scale**. The rating scores how well management is **responding** to each factor today, not how large the factor is. Importance is carried by the weight.

| Rating | Meaning |
| --- | --- |
| 5.0 | Outstanding response |
| 4.0 | Above-average response |
| 3.0 | Average response |
| 2.0 | Below-average response |
| 1.0 | Poor response |

- Half-points (for example 3.5) are permitted.
- The weighted total of an average firm is **3.0**. The theoretical range is 1.0 to 5.0.
- State the scale in every table header: "Rating: Wheelen and Hunger 1-5 response scale; average firm = 3.0."
- **Why this scale and not another.** Fred David's EFE/IFE matrices, common in other textbooks, rate 1 to 4 with 2.5 as average. Mixing the two makes totals incomparable. Choose one scale per deliverable. This engine's default is 1 to 5 because it keeps a true midpoint and pairs with the SFAS duration column. If a client insists on 1 to 4, convert every table and state the conversion; never mix them.
- **Do not confuse it with the 0-to-5 competitive position rating** in `06-competitive-analysis/references/competitive-strategy-tools.md`. That instrument rates each competitor's standing on a key success factor; this one rates the firm's response to an environmental or internal factor. They answer different questions and may both appear, each with its own labelled scale.

## 2. EFAS procedure (external factors)

1. List the fifteen to twenty candidate opportunities and threats from the scan.
2. Rank them from most to least important. Fix the top three and bottom three first, then place the rest.
3. Keep eight to ten factors. Cut the others into the rejected-factor log with a reason.
4. Weight each from 1.0 (most important) to 0.0 by probable impact on the organisation's strategic position. **The weights sum to 1.00.**
5. Rate the current response to each factor on the 1-to-5 scale.
6. Weighted score = weight × rating.
7. Write the comment: why the factor was chosen, why the weight, why the rating, source and grade.
8. Sum the weighted scores. Compare the total with actual profitability and share. A total well above 3.0 in a firm losing share needs re-examination.

### Blank EFAS template

Rating: Wheelen and Hunger 1-5 response scale; average firm = 3.0.

| ID | External factor | Tag (O/T) | Weight | Rating (1-5) | Weighted score | Comment: evidence, source grade, reason for weight and rating |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E1 | | | | | | |
| E2 | | | | | | |
| E3 | | | | | | |
| E4 | | | | | | |
| E5 | | | | | | |
| E6 | | | | | | |
| E7 | | | | | | |
| E8 | | | | | | |
| **Total** | | | **1.00** | | | Compare with actual profit and share |

Comment slot: "[Factor] ([O/T]): weight [0.xx] because [impact on position]; rated [x.x] because [evidence of current response]; source grade [A-E][1-5]."

## 3. IFAS procedure (internal factors)

Same mechanics for eight to ten strengths and weaknesses, with one extra admission rule.

**VRIO filter before a strength is admitted:**

| Test | Question | If it fails |
| --- | --- | --- |
| Valuable | Does it let the firm charge more or cost less, measured against what customers value? | Not a strength; table stakes or weakness |
| Rare | Do two or more rivals already match it? (One rival matching still counts as rare.) | Parity: move out of strengths |
| Costly to imitate | Is it protected by complexity, causal ambiguity, tacit knowledge, location, licence or history? | Temporary advantage: shorten its duration |
| Organised to exploit | Do structure, systems and complementary capabilities let the firm use it? | Latent: record as weakness to fix |

Compare every internal factor with three baselines: the firm's own past, named key rivals, and the industry. Common false strengths in Ugandan plans: "we have a good website", "we use quality ingredients", "our staff are trained". Push for the linked capability (for example a farmer collection network with daily mobile-money settlement) that rivals would need years to copy.

### Blank IFAS template

Rating: Wheelen and Hunger 1-5 response scale; average firm = 3.0.

| ID | Internal factor | Tag (S/W) | VRIO result | Weight | Rating (1-5) | Weighted score | Comment: evidence and comparison baseline |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| I1 | | | | | | | |
| I2 | | | | | | | |
| I3 | | | | | | | |
| I4 | | | | | | | |
| I5 | | | | | | | |
| I6 | | | | | | | |
| I7 | | | | | | | |
| I8 | | | | | | | |
| **Total** | | | | **1.00** | | | |

## 4. SFAS procedure (strategic factors)

1. Take the most important EFAS and IFAS rows (usually the top four or five of each) so that fewer than ten remain.
2. Tag each S, W, O or T. A factor may carry two tags, for example "O+T" for a shift in retail channels that helps and hurts.
3. Re-weight so the SFAS set sums to 1.00.
4. Carry the ratings across unchanged unless new evidence exists.
5. Compute weighted scores.
6. Add the **duration** column: short (under 1 year), intermediate (1 to 3 years), long (over 3 years).
7. Write comments.
8. Use the SFAS to review the mission and objectives. Objectives take the form "To [raise/cut/win] [metric] from [baseline] to [target] by [date] in [segment/geography]." A statement without metric, baseline or date is a goal, not an objective.

**Rule:** no factor appears in the SFAS for the first time. Every row traces to an EFAS or IFAS row ID.

### Blank SFAS template

Rating: Wheelen and Hunger 1-5 response scale; average firm = 3.0.

| SFAS ID | Strategic factor (source row) | Tag | Weight | Rating (1-5) | Weighted score | Duration (S / I / L) | Comment |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| F1 | (E_) | | | | | | |
| F2 | (I_) | | | | | | |
| F3 | | | | | | | |
| F4 | | | | | | | |
| F5 | | | | | | | |
| F6 | | | | | | | |
| **Total** | | | **1.00** | | | | |

### Opportunity-divided-by-capacity test

Wheelen and Hunger frame strategic advantage as opportunity divided by capacity: SA = O ÷ (S − W). For each heavily weighted opportunity, ask whether the organisation's strengths minus its weaknesses give it the capacity to act. If not, either fund the capability (and name the cost) or drop the opportunity.

## 5. SWOT quality gate (reject and rebuild if any line is true)

- A box holds more than six items.
- A strength is a parity quality that rivals share.
- An opportunity or threat is generic ("economic growth", "competition").
- The SWOT has no weights, scoring or conclusion.
- A later option does not trace back to a SWOT or SFAS cell.

Optional comparative scoring (Johnson et al. 2017): list four to six key environmental changes as columns and three to five strengths and weaknesses as rows; score each cell +5 to −5 for whether the strength helps or the weakness blocks; total rows and columns; repeat for two or three rivals. This reveals relative exposure that a single-firm SWOT hides.

## 6. TOWS from the SFAS

| | Strengths (SFAS S rows) | Weaknesses (SFAS W rows) |
| --- | --- | --- |
| **Opportunities (SFAS O rows)** | **SO**: use strengths to capture opportunities | **WO**: fix weaknesses to capture opportunities |
| **Threats (SFAS T rows)** | **ST**: use strengths to blunt threats | **WT**: defend, retrench or partner to limit exposure |

Rules:

1. Use SFAS rows only, cited by ID in every cell (for example "SO-1: F2 × F5").
2. Generate at least one option per quadrant where evidence supports it; three to eight options in total is typical.
3. Test each option against the four criteria for alternatives:

| Criterion | Question |
| --- | --- |
| Mutually exclusive | Does choosing it preclude the others, so a real choice exists? |
| Likely to succeed | Is it feasible with a good probability of working? |
| Complete | Does it address the key strategic factors, not one of them? |
| Internally consistent | Does it fit the firm's other goals and policies? |

4. Combine compatible options into two or three mutually exclusive strategic alternatives (for example one growth, one stability or focus, one retrenchment or partnership). Pass them to `meta-strategic-options-evaluation`.

### Blank TOWS register

| Option ID | Quadrant | Factor IDs used | Option (one line) | Four-criteria result | Carried forward? |
| --- | --- | --- | --- | --- | --- |
| SO-1 | SO | | | | Yes / No, reason |
| ST-1 | ST | | | | |
| WO-1 | WO | | | | |
| WT-1 | WT | | | | |

## 7. Writing the result into a plan

- Factor summary sentence: "Of the [n] factors screened, [k] carry [xx]% of the weight. The plan answers each of them; any factor it does not address is named in the risk register."
- Present weights as structured judgement. Write "we weight" or "the team weighted", never "the data shows a weight of".
- Number the exhibits (Exhibit 4.1 EFAS, 4.2 IFAS, 4.3 SFAS, 4.4 TOWS) so later sections can cite them.
