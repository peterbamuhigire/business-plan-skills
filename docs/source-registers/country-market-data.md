# Country and market evidence register

Checked 13 July 2026; URA, NEMA and Bank of Uganda portals re-checked and three marketing entries added on 24 September 2026. The machine-readable source is
[`country-market-data.json`](country-market-data.json). This register identifies competent
starting sources; it does not validate any statistic copied from them. Every released claim still
needs its table or page, period, geography, definition, retrieval date, and applicability note.

| ID | Jurisdiction | Publisher | Claim families | Recheck due | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| `UG-UBOS-STATISTICAL-PUBLICATIONS` | Uganda | Uganda Bureau of Statistics | Population, national accounts, prices, labour, sector output | 2026-10-13 | verified-current | country-context maintainer |
| `KE-KNBS-STATISTICAL-ABSTRACT` | Kenya | Kenya National Bureau of Statistics | Population, national accounts, prices, labour, sector output | 2026-10-13 | verified-current | country-context maintainer |
| `TZ-NBS-STATISTICAL-ABSTRACT` | Tanzania | National Bureau of Statistics Tanzania | Population, national accounts, prices, labour, sector output | 2026-10-13 | verified-current | country-context maintainer |
| `UG-URA-TAX-GUIDANCE` | Uganda | Uganda Revenue Authority | Tax registration, returns, payments, customs | 2026-10-24 | verified-current | finance gate owner |
| `UG-URSB-BUSINESS-REGISTRATION` | Uganda | Uganda Registration Services Bureau | Entity registration, legal identity, annual filings | 2026-10-13 | verified-current | country-context maintainer |
| `UG-NEMA-REGULATIONS` | Uganda | National Environment Management Authority | Environmental screening, ESIA, waste, air, effluent | 2026-10-24 | verified-current | regulatory gate owner |
| `UG-UNBS-STANDARDS` | Uganda | Uganda National Bureau of Standards | Product standards, certification, testing, metrology | 2026-10-13 | verified-current | regulatory gate owner |
| `UG-UCC-LICENSING` | Uganda | Uganda Communications Commission | Communications licensing, spectrum, postal, broadcasting | 2026-10-13 | verified-current | regulatory gate owner |
| `UG-BOU-SUPERVISION` | Uganda | Bank of Uganda | Financial licensing, payments, credit institutions, foreign exchange | 2026-10-24 | verified-current | finance gate owner |
| `GLOBAL-WORLD-BANK-DATA` | Regional/Global | World Bank | Cross-country macroeconomic and development indicators | 2026-10-13 | verified-current | research lead |
| `UG-DPPA-2019-AND-REGULATIONS-2021` | Uganda | Parliament of Uganda; Minister of ICT | Data-protection registration, consent, direct-marketing objection right | 2027-03-23 | verified-with-caveat | marketing-plan maintainer |
| `KE-ODPC-DATA-PROTECTION-REGULATIONS-2021` | Kenya | Office of the Data Protection Commissioner | Direct-marketing conditions, objection right, opt-out, registration | 2027-03-23 | verified-current | marketing-plan maintainer |
| `UG-DATAREPORTAL-DIGITAL-2026` | Uganda | Kepios (DataReportal) | Internet users, social ad reach (floor only), cellular connections | 2026-11-30 | verified-with-caveat | marketing-plan maintainer |

## Refresh rule

Run `python -X utf8 tools/evidence-register/refresh_evidence_register.py --check` before release.
An overdue, duplicate, malformed, or jurisdiction-uncovered entry fails. Network checks are an
explicit maintainer action using `--check-urls`; CI validates the recorded evidence state without
pretending that an unavailable network request passed.
