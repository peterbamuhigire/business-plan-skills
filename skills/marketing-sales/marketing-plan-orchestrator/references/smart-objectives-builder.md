# SMART objective builder and quality test

Parent: [Marketing Plan Orchestrator](../SKILL.md).

When to read: whenever a marketing plan, business-plan section 07, campaign
brief or KPI dashboard states an objective or target. Also used by
`07-marketing-sales-strategy`, `meta-quarterly-gameplan` and the social-media
engine's strategy handoff. Pair it with
[location and scope calibration](location-and-scope-calibration.md).

## 1. What SMART means in this engine

| Letter | Meaning here | What must be visible in the sentence |
|---|---|---|
| S | Specific | One metric, one segment, one named place, one mechanism |
| M | Measurable | Baseline value with source and date; a defined numerator, denominator and window; a named tracking method |
| A | Accurate and achievable | Arithmetic reconciles with capacity, budget and the funnel; the target's source is stated (model maths, benchmark with year, or the firm's own trend) |
| R | Realistic | Credible against past performance and the market's size; stretching but not fantasy (Abrams's "reasonable" and "motivational" tests) |
| T | Time-bound | A deadline and interim checkpoints |
| + | Applicable | Fits the business, its location and its scope (city, region, country or cross-border), its payment and media realities and its legal context |

An objective that fails any row is a wish. Rewrite it or delete it.

## 2. The objectives cascade

Objectives must connect upward and downward. Build them in this order:

1. **Business objective** (owner: board or founder). Revenue, contribution,
   customers or market position. Example: monthly revenue, margin floor.
2. **Marketing objectives** (owner: marketing lead). The customer behaviour
   that delivers the business objective: new customers, retention, spend per
   customer, purchase frequency, share of a named segment.
3. **Communication objectives** (owner: marketing or agency). What the target
   must know, feel or believe first: awareness, consideration, message recall,
   preference, enquiry intent.
4. **Channel objectives** (owner: channel manager). What each channel must
   deliver at what cost: qualified enquiries, cost per qualified enquiry,
   conversion, reach and frequency.

Reconciliation test: multiplying the channel objectives through the funnel
must produce the marketing objectives, and the marketing objectives must
produce the business objective, within stated assumptions. If the arithmetic
does not close, one level is wrong.

Stockwell and Shaw's goal hierarchy helps rank what matters: **Goal 1** is the
problem that "keeps the owner awake" (for example profitable growth),
**Goal 2** supports management (for example support the field sales team),
**Goal 3** is a useful by-product (for example build an opted-in contact
list). Each becomes an objective with a value or percentage, a date and an
approver. Watch for conflicting goals (Stockwell, J. and Shaw, H. M. (1994)
*Direct Marketing Checklists*, NTC Business Books).

## 3. Lines in the sand

Every target is a **line in the sand**: a pre-committed number that decides
the next action. Record where the number comes from (Croll, A. and
Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly Media):

| Source of the line | When to use it | What to record |
|---|---|---|
| Business-model maths | The plan requires the number to work (for example, 30% of enquiries must convert for contribution to cover fixed costs) | The calculation |
| Benchmark | A comparable, sourced baseline exists | Source, year, market, and why it transfers |
| Self-derived trend | Neither exists | The firm's own trend from tests, and the ceiling it is approaching |

Rules: never lower a line merely to pass; move it only with evidence from a
specific segment showing value is being created at the new level; record who
may change it. Each KPI row carries: baseline (source, date) · line · source of
line · review date · action if hit · action if missed.

## 4. Slot-template

"[Verb: increase / reduce / reach / retain] [metric, defined] among
[segment] in [named place] from [baseline, source, date] to [target] by
[date], through [mechanism: 2–3 message themes delivered via named channels],
within [budget in UGX], measured by [tracking method], owned by [role] and
reviewed [cadence]."

## 5. SMART quality test (pass or fail)

Score each objective. Any **fail** item rejects it.

| Check | Pass condition | Automatic fail |
|---|---|---|
| Metric | A single named metric with numerator, denominator and window | "Awareness", "engagement", "brand presence" with no definition |
| Segment | Named segment matching the target-market definition | "Customers", "everyone", "the youth" |
| Place | Named geography at the level the business operates (parish, division, town, district, county, country, corridor) | No place, or a place larger than the business can serve |
| Baseline | Current value with source and date | Missing; "to be established" without a dated plan to establish it before launch |
| Target and line source | Number plus its source (model maths, benchmark, trend) | A round number with no derivation |
| Arithmetic | Funnel, capacity and budget reconcile | Target needs more customers than delivery can serve, or more enquiries than the budget buys |
| Time | Deadline plus at least one checkpoint | "This year", "soon", "ongoing" |
| Owner | A role accountable | "The team", "marketing" |
| Applicability | Uses local payment, media and legal realities | Imports a benchmark or channel that does not exist or is unlawful in the location |
| Evidence class | Target labelled as a target; baseline labelled as verified or estimated | Target presented as a forecast or a fact |

Vague goals that must fail: "Increase brand awareness." "Grow sales
significantly." "Become the leading provider in East Africa." "Go viral."
"Build a strong social media presence." "Reach more customers through digital
marketing."

Automated check: `tools/objective-check/check_objectives.py` applies these fail conditions to a JSON list of objectives (structured or one-sentence); `tests/test_marketing_objective_check.py` and `tests/fixtures/marketing-objectives.json` hold passing and failing examples.

## 6. Worked cascade (illustrative figures, Kampala)

A meal-prep business delivering weekday dinners to working households. All
numbers are illustrative placeholders showing the shape of a reconciled
cascade; replace them with the client's records.

- **Business:** Raise average monthly revenue from UGX 38m (January–June 2026
  average, sales ledger) to UGX 55m by 30 June 2027, holding contribution
  margin at or above 35%.
- **Marketing (acquisition):** Add 160 net active subscribing households in
  Kira Municipality and Nakawa Division by 30 June 2027 (baseline 345, CRM,
  1 September 2026), at UGX 110,000 average monthly spend. 160 × UGX 110,000 ≈
  UGX 17.6m, which closes the UGX 17m revenue gap.
- **Marketing (retention):** Raise the share of first-month subscribers who
  reorder in month two from 48% (April–August 2026 cohorts) to 60% by
  31 March 2027 through a day-10 WhatsApp check-in and a second-month menu
  choice. Line source: model maths (below 55%, acquisition cost is not repaid
  within four months).
- **Communication:** Raise aided awareness of the brand among working
  households in the two areas from the September 2026 baseline (intercept and
  WhatsApp-link survey, n = 300) by 15 percentage points by March 2027, with
  "no cooking after work" and "paid by mobile money weekly" as the two
  message themes.
- **Channel:** Generate 90 qualified WhatsApp enquiries a month from
  click-to-WhatsApp ads and resident-association sponsorships at no more than
  UGX 30,000 each (UGX 2.7m a month), converting 30% to subscriptions
  (27 new households a month). With about nine households lost a month, net
  growth is about 18 a month, or about 160 over nine months. Line source:
  self-derived from the August 2026 test (27% conversion).
- **Capacity check:** the kitchen and two boda riders serve 520 households;
  505 at the June 2027 target leaves 3% headroom, so a third rider is booked
  from March 2027.

## 7. Before and after

| Vague | SMART and applicable |
|---|---|
| Increase brand awareness in Gulu. | Raise unaided recall of [brand] among maize farmers with 2–10 acres in Gulu and Omoro districts from 12% (baseline survey, n = 250, August 2026) to 25% by the end of the March 2027 planting season, through two Luo-language radio spots a day on two stations and parish demonstration days; measured by a repeat survey of the same design. |
| Grow B2B sales. | Sign 14 new annual payroll-software contracts with Kampala firms of 50–300 staff by 30 June 2027 (baseline: 9 signed July 2025–June 2026, CRM), from 70 qualified demos at a 20% close rate; owned by the sales lead, reviewed weekly in the pipeline meeting. |
| Expand into Kenya. | Win 40 repeat-ordering pharmacy accounts in Nairobi County by 31 December 2027 through one distributor, at a landed price within 5% of the leading local brand; decision gate at 15 accounts by 30 June 2027 or stop. |
| Be active on social media. | Deliver 120 booked salon appointments a month from Instagram and WhatsApp in Ntinda and Kisaasi by February 2027 (baseline 45, booking book, September 2026), at no more than UGX 8,000 of ad spend per booking. |

## 8. Common failures and fixes

- Targets copied from another country's benchmark. Fix: rebuild from local
  records, a local test or model maths, and label the source.
- Objectives at one level only. Fix: build the cascade and reconcile it.
- Targets that exceed delivery capacity. Fix: sequence growth or add capacity
  first; do not raise the media budget to paper over it.
- Percentages without bases ("grow 50%"). Fix: state the base value and date.
- Objectives without owners or review dates. Fix: name the role and cadence in
  the control plan.
