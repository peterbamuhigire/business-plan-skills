---
name: saas-marketing-channel-economics
description: Design and audit the SaaS marketing channel mix on per-channel economics — CAC, payback, scale ceiling, channel concentration risk. Per-channel: SEO/content, paid (Google/Meta/LinkedIn), community, partnerships, events, WhatsApp/messaging, ABM, referrals. Forces the marketing budget to be a defended portfolio of measured channels, not a single line item.
---

# SaaS Marketing Channel Economics Skill

## Overview

Most SaaS plans treat marketing as a single budget line. The discipline is channel-level economics: per-channel CAC, payback, scale ceiling, and concentration risk. This skill produces the channel portfolio with explicit economics per channel, identifies the marketing arbitrage opportunity (Cotton), and forces channel diversification.

## Use When

- Section 07 of any SaaS plan
- Existing marketing spend is concentrated >50% in a single channel (concentration risk)
- A new channel is being considered
- CAC has been creeping up (likely channel saturation)

## Required Inputs

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

## Outputs

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
