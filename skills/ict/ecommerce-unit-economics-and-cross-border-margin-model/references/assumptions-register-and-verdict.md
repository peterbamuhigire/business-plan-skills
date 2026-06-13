# Assumptions Register and Verdict Rules

## Assumption Tags

| Tag | Meaning | Use in verdict |
|---|---|---|
| Company data | Provided from company records or systems. | Highest confidence if internally consistent. |
| Supplier quote | Logistics, payment, platform, customs broker, or vendor quote. | Use with date and validity period. |
| Official source | Regulator, customs authority, statutory rate, provider documentation. | High confidence. |
| Global proxy | Non-local benchmark used only because local data is absent. | Must be labelled and sensitivity-tested. |
| Indicative source | Analyst/vendor/blog estimate used for context only. | Never decisive on its own. |
| Inference | Calculated or estimated from partial data. | Needs explicit confidence and sensitivity. |

## Confidence Levels

- High: company records, official source, or current quote.
- Medium: triangulated but not primary.
- Low: proxy or inference that could materially change the verdict.

## Verdict Rules

Go:

- Positive contribution margin under base and reasonable downside scenario.
- CAC/payback acceptable for the company's cash cycle.
- Payment/logistics/compliance route is operationally feasible.

Conditional:

- Base case is viable but one or two variables can flip contribution negative.
- Requires pilot, renegotiated fees, improved conversion, lower returns, or working-capital support.

No-go:

- Contribution remains negative under realistic assumptions.
- Cash cycle is unaffordable.
- Required payment/logistics/compliance route is unavailable or too risky.
