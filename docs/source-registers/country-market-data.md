# Country and market evidence register

Original checks 13 July 2026; ten dated claim sources (data protection, influencer and advertising law, mobile speed, WhatsApp, GSMA licence) added on 25 September 2026 from the Kaizen currentness register 2026-09-24; URA, NEMA and Bank of Uganda portals re-checked and three marketing entries added on 24 September 2026. The machine-readable source is
[`country-market-data.json`](country-market-data.json). This register identifies competent
starting sources; it does not validate any statistic copied from them. Every released claim still
needs its table or page, period, geography, definition, retrieval date, and applicability note.

Claim-level review on 31 October 2026 renewed six of the ten overdue rows with narrowed claim families (the page evidence is in each row's `note` in the JSON), added the Bank of Uganda October 2026 monetary policy statement, and left four rows `stale` because the issuer page could not be read (certificate failure for UBOS and KNBS, HTTP 403 for UNBS, no body text on the Bank of Uganda supervision page). The table below is generated from the JSON by `--write-markdown` and checked against it by `--check`; do not edit its rows by hand.

<!-- register-table:start -->
| ID | Jurisdiction | Publisher | Claim families | Checked | Recheck due | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `UG-UBOS-STATISTICAL-PUBLICATIONS` | Uganda | Uganda Bureau of Statistics | Population, national accounts, prices, labour, sector output | 2026-07-13 | 2026-10-13 | stale | country-context maintainer |
| `KE-KNBS-STATISTICAL-ABSTRACT` | Kenya | Kenya National Bureau of Statistics | Population, national accounts, prices, labour, sector output | 2026-07-13 | 2026-10-13 | stale | country-context maintainer |
| `TZ-NBS-STATISTICAL-ABSTRACT` | Tanzania | National Bureau of Statistics Tanzania | Statistical abstract editions | 2026-10-31 | 2027-01-29 | verified-with-caveat | country-context maintainer |
| `UG-URA-TAX-GUIDANCE` | Uganda | Uganda Revenue Authority | Tax registration, returns, payments | 2026-10-31 | 2027-01-29 | verified-with-caveat | finance gate owner |
| `UG-URSB-BUSINESS-REGISTRATION` | Uganda | Uganda Registration Services Bureau | Entity registration, legal identity | 2026-10-31 | 2027-01-29 | verified-with-caveat | country-context maintainer |
| `UG-NEMA-REGULATIONS` | Uganda | National Environment Management Authority | Environmental screening, ESIA, waste, air, effluent | 2026-10-31 | 2027-01-29 | verified-with-caveat | regulatory gate owner |
| `UG-UNBS-STANDARDS` | Uganda | Uganda National Bureau of Standards | Product standards, quality marks, testing, metrology | 2026-07-13 | 2026-10-13 | stale | regulatory gate owner |
| `UG-UCC-LICENSING` | Uganda | Uganda Communications Commission | Communications licensing, telecommunications licensing | 2026-10-31 | 2027-01-29 | verified-with-caveat | regulatory gate owner |
| `UG-BOU-SUPERVISION` | Uganda | Bank of Uganda | Financial licensing, payments, credit institutions, foreign exchange | 2026-09-24 | 2026-10-24 | stale | finance gate owner |
| `GLOBAL-WORLD-BANK-DATA` | Regional/Global | World Bank | Cross-country macroeconomic comparison, development indicators | 2026-10-31 | 2027-01-29 | verified-with-caveat | research lead |
| `UG-DPPA-2019-AND-REGULATIONS-2021` | Uganda | Parliament of Uganda (Act 9 of 2019, now Cap. 97); Minister of ICT (S.I. 21 of 2021) | Data-protection registration, consent to collect, direct-marketing objection right, marketing data use | 2026-09-24 | 2027-03-23 | verified-with-caveat | marketing-plan maintainer |
| `KE-ODPC-DATA-PROTECTION-REGULATIONS-2021` | Kenya | Office of the Data Protection Commissioner | Direct marketing conditions, absolute objection right, opt-out requirement, controller registration | 2026-09-24 | 2027-03-23 | verified-current | marketing-plan maintainer |
| `UG-DATAREPORTAL-DIGITAL-2026` | Uganda | Kepios (DataReportal) | Internet users, social media ad reach, cellular connections | 2026-09-24 | 2026-11-30 | verified-with-caveat | marketing-plan maintainer |
| `KE-DPA-2019-S37-AND-GENERAL-REGS-2021` | Kenya | Parliament of Kenya; Cabinet Secretary ICT | Commercial use of personal data consent, direct marketing opt-out, objection right | 2026-09-25 | 2027-03-25 | verified-current | marketing-plan maintainer |
| `KE-MEDIA-COUNCIL-CODE-2025` | Kenya | Media Council of Kenya (Legal Notice 88 of 2025) | Sponsored content labelling, endorsement compensation disclosure | 2026-09-25 | 2027-03-25 | verified-with-caveat | marketing-plan maintainer |
| `KE-CONSUMER-PROTECTION-ACT-2012-S12` | Kenya | Parliament of Kenya | Misleading representation, false sponsorship or approval | 2026-09-25 | 2027-03-25 | verified-with-caveat | marketing-plan maintainer |
| `TZ-ONLINE-CONTENT-REGULATIONS-2020-2022` | Tanzania | Tanzania Communications Regulatory Authority | Online media licence, blogger definition, user accountability | 2026-09-25 | 2026-12-25 | verified-with-caveat | marketing-plan maintainer |
| `TZ-FAIR-COMPETITION-ACT-2003` | Tanzania | Parliament of Tanzania | Misleading or deceptive conduct | 2026-09-25 | 2027-03-25 | verified-with-caveat | marketing-plan maintainer |
| `UG-UCC-QOS-2024` | Uganda | Uganda Communications Commission | Mobile data download speed, latency, drive-test QoS | 2026-09-25 | 2027-01-25 | verified-with-caveat | marketing-plan maintainer |
| `KE-MOBILE-SPEED-SECONDARY-2025` | Kenya | StatRanker (secondary; Ookla page inaccessible) | Mobile median download speed | 2026-09-25 | 2026-12-25 | verified-with-caveat | marketing-plan maintainer |
| `KE-PEW-WHATSAPP-2024` | Kenya | Pew Research Center | WhatsApp use among adults | 2026-09-25 | 2027-03-25 | verified-with-caveat | marketing-plan maintainer |
| `EA-WHATSAPP-SHARE-CLAIM` | Regional/Global | Digital Research wave (synthesis) | WhatsApp share of smartphone or internet users | 2026-09-25 | 2027-03-25 | no-source-found | marketing-plan maintainer |
| `GLOBAL-GSMA-INTELLIGENCE-TERMS` | Regional/Global | GSMA Intelligence | GSMA data licence, citation rules | 2026-09-25 | 2027-03-25 | verified-with-caveat | marketing-plan maintainer |
| `UG-BOU-MPS-OCT-2026` | Uganda | Bank of Uganda | Central Bank Rate, headline inflation, inflation outlook | 2026-10-31 | 2026-11-30 | verified-current | finance gate owner |
<!-- register-table:end -->

## Refresh rule

Run `python -X utf8 tools/evidence-register/refresh_evidence_register.py --check` before release.
An overdue, duplicate, malformed, or jurisdiction-uncovered entry fails, and so does a Markdown table that differs from the JSON (regenerate it with `--write-markdown`). Network checks are an
explicit maintainer action using `--check-urls`; CI validates the recorded evidence state without
pretending that an unavailable network request passed.
