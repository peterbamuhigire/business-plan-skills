# Evidence discipline for marketing and plan claims

Parent: [Marketing Plan Orchestrator](../SKILL.md).

When to read: before writing any number, market statement, platform fact,
legal statement or competitive claim in a marketing plan or business-plan
sections 03–07, and when preparing the appendix source register. Shared by
`07-marketing-sales-strategy`, `04-market-analysis` and `05-target-market`.

## 1. Five evidence classes

Every material statement belongs to exactly one class, and the prose must make
the class visible.

| Class | Definition | Required marker in the text | Example phrasing |
|---|---|---|---|
| Verified fact | Observed or published, checked against a named source | Source and date | "UBOS reports [figure] for [year] ([publication], accessed [date])." |
| Management assumption | A number the owner chooses to plan on | "We assume" or "the plan assumes", plus the basis | "The plan assumes 30% of qualified enquiries convert, based on the August 2026 test (27%)." |
| Estimate | Derived by calculation from facts and assumptions | "We estimate", plus the method | "Bottom-up, we estimate the reachable market at UGX [x] (households × orders × price)." |
| Projection | A forward-looking result of the model under stated assumptions | "We project … if …" | "We project UGX [x] revenue in year two if retention holds at 60%." |
| Target | A chosen goal with a line in the sand | "Our target is … by [date]" | "Our target is 160 net new households by 30 June 2027." |

Never present a target or projection as a fact, or an assumption as research.

## 2. Currentness

- Volatile claims (law, tax, platform features and policies, prices, media
  rates, statistics, exchange rates, benchmarks) enter a plan only from the
  engine's currentness register (cite the claim ID and check date) or after
  verification through the Digital Research engine. Record source, publication
  or version date, access date and review date.
- Country and market facts must also pass `docs/source-registers/country-market-data.json`;
  an overdue entry blocks the conclusion that depends on it.
- Book methods are durable concepts. Book statistics and case results are
  historical illustrations, never benchmarks.
- Tax, accounting and statutory cost statements go to the Chwezi finance
  doctrine. Legal conclusions need a qualified reviewer.
- If a source cannot be reached, the claim is NOT_ASSESSED and the dependent
  conclusion is narrowed; it is never reported as passed.

## 3. Claims the engine never makes without its gates

- "Bankable", "investor-ready", "viable", "achievable" or "compliant" require
  the engine's evidence gates (market, operations, financial reconciliation,
  risk, funding and implementation) and the release bundle; marketing polish
  does not qualify a plan.
- Market sizes, growth rates, TAM/SAM/SOM, conversion benchmarks and
  audience sizes are never invented. If unavailable, show the method and leave
  the value as a labelled placeholder with the evidence request.
- Results (reach, engagement, conversion, ROI, client outcomes) are reported
  only from data, with the period and definition. A documented workflow is not
  an observed result.
- Testimonials, reviews and case results must be real, attributable and used
  with permission.

## 4. Source register row (appendix)

| Claim | Class | Value | Source (publisher, title, URL or locator) | Published or version date | Accessed | Review by | Tier (primary, originating publisher, secondary) | Used in section | Status (verified, partial, NOT_ASSESSED) |
|---|---|---|---|---|---|---|---|---|---|

## 5. Quick self-check before release

1. Does every number carry its class and source?
2. Are all volatile facts from the register or freshly verified, with dates?
3. Does any sentence call the plan bankable, viable or proven without the gates?
4. Are any figures from a book being used as current benchmarks?
5. Are placeholders clearly marked and listed as evidence requests?
