---
name: saas-marketing-channel-economics
description: Use when section 07 of any SaaS plan. Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Marketing Channel Economics Skill

## Overview

Most SaaS plans treat marketing as a single budget line. The discipline is channel-level economics: per-channel CAC, payback, scale ceiling, and concentration risk. This skill produces the channel portfolio with explicit economics per channel, identifies the marketing arbitrage opportunity (Cotton), and forces channel diversification.

## Use When

- Section 07 of any SaaS plan
- Existing marketing spend is concentrated >50% in a single channel (concentration risk)
- A new channel is being considered
- CAC has been creeping up (likely channel saturation)

## Do Not Use When

- The request belongs to the neighbouring route. Use the cross-sector meta skill when the decision is not specific to recurring-revenue SaaS economics or operations.
- The available evidence cannot support a responsible marketing channel economics conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Marketing Channel Economics brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Current marketing channels with spend and outcomes
- Funnel data per channel (visits, signups, paid customers)
- Customer LTV (from unit economics model)
- Target ARR / customer count
- Geography (some channels work in some markets, not others)

## Workflow

1. **Inventory current channels** with spend, customers, CAC, payback per channel:
   - SEO / organic content
   - Paid search (Google Ads)
   - Paid social (LinkedIn, Meta, X)
   - Content marketing (blog, podcast, video, newsletter)
   - Community (Slack, Discord, Telegram, sector-specific)
   - Partnerships / integrations
   - Events (conferences, webinars, owned)
   - WhatsApp Business / messaging
   - Outbound (BDR / SDR)
   - Referrals (customer-led growth)
   - PR / earned media
   - Influencer / KOL
   - Account-based marketing
2. **Compute per-channel CAC and payback** using `references/saas-marketing-budget-and-channel-mix-model.md` formulas.
3. **Compute scale ceiling** per channel — at what monthly spend does CAC degrade? (Most channels have a ceiling; identify it before hitting it.)
4. **Identify the marketing arbitrage** — channels where current market CAC is below the LTV-justified ceiling. Pour budget there until the arbitrage closes.
5. **Diversify across ≥3 channels** — channel concentration is risk. If 70% of customers come from one channel, an algorithm change can kill the business.
6. **Plan the channel portfolio for the next 12 months** — primary, secondary, experimental.
7. **Specify channel-by-channel KPIs and review cadence.**
8. **Cross-reference** Section 07 with the channel mix; Section 10 with the marketing budget.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the channel economics portfolio and that the decision concerns which channels to scale, test, cap, or stop.
- **Stop condition:** halt the affected conclusion if required evidence is missing (spend, attributed pipeline, conversion, CAC, payback, and scale ceiling) or if the work could lead to this identified risk: hiding channel concentration and bad payback inside blended CAC.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Each channel has CAC + payback computed (not estimated)
- Scale ceiling identified per channel
- Channel concentration <50% in primary channel (or remediation plan)
- ≥3 channels active or planned
- Arbitrage opportunity identified
- Africa-context channels (WhatsApp, community, in-person events) included where relevant

## Anti-Patterns

- "We'll do digital marketing" — undifferentiated
- 80%+ from one channel without diversification plan
- Ignoring WhatsApp / messaging in African plans
- Spending on channels without per-channel attribution
- "Brand" as a separate channel without metrics (brand is a moat lever; not a CAC channel)
- Influencer marketing without measurement


- Applying the wrong neighbouring route to saas marketing channel economics. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Marketing Channel Economics deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Per-channel economics table (channel / spend / customers / CAC / payback / ceiling)
- Channel portfolio (primary / secondary / experimental)
- Marketing arbitrage identified
- 12-month channel plan with budget
- Channel-level KPIs and review cadence
- Concentration-risk assessment

## References

- `references/saas-marketing-budget-and-channel-mix-model.md` — channel-by-channel formulas
- `book-extractions/cotton-run-a-saas-business-extraction.md` — marketing arbitrage; sales-and-marketing engine
- `book-extractions/walling-saas-playbook-extraction.md` — owned traffic moats
- `book-extractions/garbugli-saas-email-marketing-playbook-extraction.md` — lifecycle email channel
- `book-extractions/kennedy-magnetic-marketing-extraction.md` — attraction / conversion / retention
- `skills/digital-marketing-strategy/SKILL.md` — sister skill

## Africa / Uganda Application Notes

- **WhatsApp Business** is a primary B2B sales/marketing channel — design with WhatsApp Group + Broadcast + Click-to-Chat + Business Catalog.
- **Radio** is still meaningful for SMB and rural-targeted SaaS (e.g. agritech) — Bukedde, CBS, Capital FM, Radio Citoyenne, Joy FM.
- **In-person events** disproportionately effective — sector conferences, expos, university tech weeks.
- **Community-first** approaches (Telegram, WhatsApp groups, Facebook groups) often beat paid acquisition for African B2B.
- **Partner channels** (telcos, MFIs, cooperatives, NGOs, public extension officers) under-utilised — high CAC reduction.
- **SEO** for African keywords is often less competitive — opportunity for content moats.
- **Paid social** (LinkedIn) works for enterprise / SA / NG / KE; less effective for SMB / rural.
- **Influencer / KOL** in Africa: established sector experts, journalists, broadcasters often more effective than social-media influencers for B2B.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Channel economics portfolio decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to hiding channel concentration and bad payback inside blended CAC. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the channel economics portfolio; modelling channel allocations without changing live spend is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If spend, attributed pipeline, conversion, CAC, payback, and scale ceiling cannot be obtained, return a qualified channel economics portfolio covering only the checks that remain supportable. Leave this decision unresolved: which channels to scale, test, cap, or stop. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which channels to scale, test, cap, or stop | Record the conclusion, source trail, owner, and review trigger in the channel economics portfolio. | Risk of hiding channel concentration and bad payback inside blended CAC |
| Material evidence conflicts or remains uncertain | Separate attributed pipeline and spend by channel, then cap or pause the channel whose payback remains outside the approved limit. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: spend, attributed pipeline, conversion, CAC, payback, and scale ceiling | Mark the decision on which channels to scale, test, cap, or stop `not assessed` in the channel economics portfolio, and send it to the growth lead and finance owner. | Otherwise, the work risks hiding channel concentration and bad payback inside blended CAC |

## Quality Standards


Accept the channel economics portfolio only when evidence is sufficient for this decision: which channels to scale, test, cap, or stop. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of hiding channel concentration and bad payback inside blended CAC.

## Worked Example


Blended CAC looks acceptable, but one paid channel has long payback and no scale headroom. Separate attribution, cap the weak channel, and move only tested budget to the stronger route.

<!-- dual-compat-end -->
