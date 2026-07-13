# Sector regulatory gates

Use this screening contract before a sector assumption enters operations, implementation, risk,
funding or financial projections. The machine-readable source is
[`sector-regulatory-gates.json`](sector-regulatory-gates.json). A sector match triggers questions;
it does not prove that a licence applies or that compliance has been achieved.

## Release sequence

1. Classify the activity, jurisdiction, site, scale, product, customer, money flow and data flow.
2. Select every materially applicable sector family; mixed models use more than one.
3. Answer each applicability question with dated evidence or mark it `not assessed`.
4. Carry cost, timing, staffing, capital, control and downside effects into the model and schedule.
5. Stop the affected launch, claim, valuation or funding conclusion where a stop condition remains.
6. Obtain competent legal, regulatory, tax, environmental, technical or finance review where the
   conclusion exceeds plan-author capability.

## Gate families

| Sector family | Controlling gates |
| --- | --- |
| Agriculture and livestock | Biosecurity/product movement; land, water and environment |
| Food processing | Product standard/hygiene/label; waste and effluent |
| Healthcare and life sciences | Facility/product/professional licensing; claims substantiation |
| Education and training | Provider/award accreditation; safeguarding |
| Finance, fintech and insurance | Regulatory perimeter; money-flow controls |
| ICT, telecom and media | Communications licence; personal and sensitive data |
| Hospitality and tourism | Site/service approvals; environmental and community effects |
| Mining, extractives and energy | Resource rights; environmental/social/closure obligations |
| Construction and manufacturing | Site and commissioning; equipment/product conformity |
| Retail, ecommerce and trade | Controlled goods and customs; customer/returns/data controls |
| Transport and logistics | Operator/route/cargo approval; customs and landed cost |
| NGO, grant and donor | Eligibility; restricted funds/procurement/safeguarding controls |

Competent-source routes and refresh ownership are maintained in
[`docs/source-registers/country-market-data.md`](../docs/source-registers/country-market-data.md).
For another jurisdiction, replace the authority route with the competent local source and retain
the same evidence discipline. An unavailable check is never a pass.
