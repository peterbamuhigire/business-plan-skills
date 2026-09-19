# Healthcare payer assumptions and volume-to-cash reconciliation

This reference implements B08-A02 for health-sector business plans. It is a
synthetic planning and reconciliation contract. It does not assert a payer
rate, reimbursement rule, coverage condition, claims deadline, or statutory
requirement. Current contracts and payer authority must be verified before use.

## Separate the assumption layers

| Layer | Required fields | Evidence state |
|---|---|---|
| Patient/access | patient or member segment, access channel, eligibility, referral, no-show | Source, period, owner, reviewer |
| Service/quality | service type, competency, quality or safety gate, completed units | Operational record and reviewer |
| Volume | scheduled, completed, eligible, claimed, accepted, rejected units | Period and reconciliation key |
| Rate | tariff or agreed rate, currency, effective period, contract locator | `verified` only after current authority review |
| Timing | claim date, acceptance date, remittance date, patient receipt date | Claim/remittance source |
| Payer/patient | payer responsibility, patient responsibility, adjustments, dispute | Contract or approved assumption |

Unknown, disputed, stale, or unresolved payer terms are `blocked` or
`not_assessed`; they cannot be filled by a benchmark.

## Volume-to-cash chain

1. Reconcile scheduled and completed services to eligible units, then to claims
   submitted and accepted. Preserve rejection reasons and source locators.
2. Apply only a current, reviewed rate or label the amount as a synthetic or
   management assumption. Keep payer and patient portions distinct.
3. Reconcile accepted claims and patient receipts to remittances, adjustments,
   ending AR, and the ledger control account. Never plug an unexplained gap.
4. Record timing separately: a delayed remittance cannot increase same-day cash.
5. Route disputed coverage, rate, quality, or recognition questions to the
   finance and clinical/contract reviewers before a plan conclusion is released.

## Reconciliation fields

| Check | Formula / invariant | Failure state |
|---|---|---|
| Service volume | completed = eligible + ineligible + documented exceptions | Missing classification is `not_assessed`. |
| Claim volume | submitted = accepted + rejected + pending | Unexplained difference is `blocked`. |
| Receivable | opening AR + accepted claims + evidenced adjustments - remittances = ending AR | Difference is reported with locator. |
| Cash | opening cash + payer remittances + patient receipts - paid outflows = closing cash | Timing or currency gap blocks aggregation. |
| Ledger tie-out | ending AR schedule = ledger control balance for same period/basis | Finance reviewer required. |

The acceptance oracle is exact recomputation from declared synthetic inputs.
The fixture in `tests/fixtures/phase1-kaizen-contracts.json` includes a passing
case and missing-rate failure case.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B08 book-study concept, applied to a synthetic health-sector planning reconciliation. |
| Publication/version date | Book-study source; no payer contract, tariff, claims rule, or statute is asserted. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; payer and authority terms are time-sensitive. |
| Review date | Before any health-sector external release and whenever a contract or payer authority changes. |
| Support status | Supported as a reconciliation schema and invariant; not payer advice or a claims certification. |
| Uncertainty | Current rates, eligibility, timing terms, quality rules, and ledger definitions are `not_assessed`. |
