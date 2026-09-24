# Model-currentness and claim-currentness review - 25 September 2026

## Scope and evidence

- Engine: `C:\wamp64\www\business-plan-skills`. Source: Digital Research Kaizen currentness register 2026-09-24 (accessed 2026-09-25), claims MR-01 to MR-03, WA-01 to WA-05, NET-01 to NET-05, KE-01 to KE-11, UG-01 to UG-04, TZ-01 to TZ-02, LIC-01 to LIC-10. No fact outside that register was added.

## Model-currentness outcome (MR-01, MR-02, MR-03)

- Anthropic models overview checked live 2026-09-25 (T1): Claude Fable 5.1, Opus 5.5, Sonnet 5, Haiku 4.5 are current; Haiku 4.5 has a retirement floor of 2026-10-15. This session runs Claude Sonnet 5 (session self-report, partially verified).
- Decision RETAIN: the engine stays model-agnostic for Claude; no skill hard-codes a model, so the lineup requires no skill edit. Account-level availability of Opus 5.5 and Fable 5.1 and an engine-task quality, cost and latency comparison remain `NOT_ASSESSED`.
- Codex model pins in `AGENTS.md` are out of scope for Claude sessions (MR-03) and were not checked; that review stays `NOT_ASSESSED` until a Codex session runs it. Next review: 2026-10-15, then quarterly.

## Changes made from the wave

- WhatsApp "90%+ of smartphone users" is unsupported as worded (WA-01, refuted). Replaced in `docs/prompt-for-socials.md`; "ubiquitous", "dominant" and "ubiquity" wording softened in five reference files to dominant messaging channel plus check client audience data. Marketing-plan `location-and-scope-calibration.md` now cites Pew 2023 (adults, WA-02) as the best-attributed dated figure.
- Connectivity, Kenya and Tanzania data-protection and influencer statements aligned to NET-01/04, KE-01 to KE-06, TZ-01/02, UG-01 to UG-04; NOT_ASSESSED items (UG-03, UG-04 depth, NET-03, WA-05) stay as checks.
- Licence attribution: four remaining institutional briefs (Afreximbank, AFRODAD, MoICT&NG, Kenya Ministry of Mining) now read "cite only; licence terms not yet confirmed; do not reproduce text" because the register has no LIC record for them (remaining attribution TODO). World Bank and AfDB wording in the Uganda economic-outlook brief aligned to LIC-02 and LIC-04.
- GSMA (LIC-09): GSMA Intelligence text must not be paraphrased. The only GSMA-derived data point (`country-context/africa-regional/africa-ict-saas-market-context.md`, smartphone users) now instructs to cite the current report directly and carries the prior figure as an unverified planning note. Other GSMA mentions are programme names (AI for Impact, Innovation Fund), not GSMA content.
- Ten dated claim entries added to `docs/source-registers/country-market-data.json` and `.md`.

## Reversibility

Text-only edits; revert by file. Owner: business-plan engine maintainer.
