---
name: digital-marketing-strategy
description: Use when a business plan needs an evidence-based digital marketing, channel, content, campaign, measurement, budget, or justified AI-assisted marketing section; use `entrepreneurial-demand-generation` for full-funnel demand logic and social-media skills for campaign production.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Digital Marketing Strategy Skill

## Overview

Use this skill to design the digital marketing layer of a business plan or growth plan. It covers channels, online acquisition logic, and AI-assisted marketing workflows where those materially affect growth.

## Use When

- Use when a plan needs a digital marketing strategy, online channel plan, or AI-assisted marketing workflow.
- Use when digital acquisition and digital presence are meaningful parts of the go-to-market model.
- Use when the standard marketing section needs deeper digital detail.

## Do Not Use When

- For the complete marketing mix and standalone plan, use [marketing-plan-orchestrator](../marketing-plan-orchestrator/SKILL.md); this skill owns its digital layer.
- Do not use without a defined offer, audience, and commercial objective.
- Do not confuse a channel list with a strategy.
- Do not force digital channels into a model where they are not economically relevant.

## Required Inputs

- Offer, audience, and business goal
- Existing online presence, channel constraints, and budget assumptions
- Geography and language context affecting digital behaviour
- Any wider marketing, sales, or AI-integration assumptions

## Workflow

1. Identify the audience, channels, and digital objectives that matter.
2. Select the most relevant online acquisition and retention paths.
3. Where a website, ecommerce, landing pages, content hub, SEO, or online lead capture matters, run `meta-website-investment-planning` so the plan includes website role, content/SEO architecture, stack, maintenance, analytics, and realistic costs.
4. Define content, paid, social, search, and automation roles where appropriate.
5. Reconcile the digital plan with budget, operations, and sales capacity.
6. Integrate AI-assisted marketing only where it improves execution materially.
7. Flag weak channel assumptions or capability gaps.

## Quality Bar

- The digital plan is commercially grounded and channel-specific.
- Channel choices match the audience and budget reality.
- AI usage is practical, not ornamental.
- Digital activity connects back to measurable growth outcomes.
- Website and SEO recommendations include content, conversion, measurement, maintenance, and cost assumptions instead of treating "having a website" as a strategy.

## Anti-Patterns

- Recommending every major digital channel at once.
- Assuming online demand without proof of audience behaviour.
- Treating AI tooling as strategy.
- Digital spend assumptions that do not reconcile with projections.

## Outputs

- A digital marketing strategy and channel plan
- AI-assisted marketing recommendations where justified
- Explicit assumptions, metrics, and capability gaps



## Purpose

Assess whether digital channels materially serve the buyer and business model.
Include a digital strategy when justified by that evidence. Include AI-assisted
marketing only when a defined task, evaluation, data boundary, human owner and
fallback justify it; a plan does not require AI for its own sake.

This skill generates both sections. It draws on eight primary reference frameworks:

**Strategy and cross-channel frameworks:**
- **McDonald, Wilson, Chaffey** (Marketing Plans, 9th ed)  POEM model, RACE framework, 6 digital channels, IMC, omnichannel, measurement  `references/marketing-plans-chaffey.md`
- **Bodnar and Cohen** (B2B Social Media Book): historical lead-generation context in `references/b2b-social-media.md`. Its ratios, legacy metrics and platform instructions are not current execution rules; use Section 2.7 economics and current primary-source verification.
- **Robinson** (Digital Marketing Playbook 2023)  7 channel tactics, SMART goals, analytics  `references/digital-marketing-playbook.md`
- **Kotler, Kartajaya, Setiawan** (Marketing 6.0)  metamarketing, phygital natives, 5 micro-trends, immersive CX, Gen Z/Alpha characteristics  `references/marketing-60-kotler.md`
- **Lamplugh** (AI Marketing Playbook, 2nd ed)  AI tools by function: chatbots, personalisation, email automation, SEO, content, lead scoring  `references/ai-marketing-playbook.md`
- **Keshwani** (55 Digital Marketing Masterpieces)  campaign frameworks, storytelling, UGC, viral video, influencer, retargeting, 5-point campaign analysis  `references/digital-marketing-campaigns.md`

**Platform-specific references:**
- **Marshall and Yu** (Definitive Guide to TikTok Advertising)  80/20 content strategy, Power Triangle, Why/How/What framework, 15-second video structure, Spark Ads, TikTok metrics, campaign setup  `references/tiktok-advertising.md`
- **Geddes** (Advanced Google AdWords)  buying funnel keyword matching, Quality Score, campaign structure, ad copy, landing pages, match types, bidding strategy  `references/google-ads.md`
- **Mathew, Jack** (YouTube Marketing 2021)  channel setup/optimisation, YouTube SEO, algorithm signals (CTR/AVD/watch time), video types, monetisation (YPP/brand deals/lead gen), YouTube Ads, EA adaptations (Luganda/Swahili niches, mobile-first, RPM context)  `references/youtube-marketing.md`
- **Rouhiainen** (101 Facebook Marketing Tips)  Page optimisation, organic content strategy, Facebook Groups, Reels/Stories, ad campaign structure, click-to-WhatsApp ads, lead gen forms, Facebook Shop, Messenger automation, Meta AI tools 2026, EA low-budget strategy (UGX 5,000/day), content calendar  `references/facebook-marketing.md`
- **Multi-author + Kane** (Social Media Marketing 2021-22; Social Media Marketing and Online Business 2021)  Instagram (profile/Reels/Shopping/micro-influencers), Twitter/X (EA role/threads), LinkedIn (B2B lead gen/personal brand), Podcasting (EA first-mover), Blogging/SEO (long-tail EA keywords), content repurposing (Content Factory model), creator economics (6 monetisation streams)  `references/social-media-platforms.md`
- **Willis** (Social Media Marketing in 2024)  Facebook monetisation tools (In-Stream Ads, Fan Subscriptions, Facebook Stars), TikTok organic growth (algorithm signals, Promote feature, Creator Marketplace, Creator Fund, live streams), Instagram account takeovers, and the most comprehensive passive income framework in this library: affiliate programmes (Amazon Associates, ShareASale, CJ, Jumia), digital product types and EA platforms (Selar, Gumroad, Payhip), YouTube monetisation paths, Patreon/Substack subscription models, income diversification portfolio, EA income scenario  `references/facebook-marketing.md` (15), `references/tiktok-advertising.md` (organic/creator section), `references/social-media-platforms.md` (Part 8)

---

## Step 1: Gather Information Before Writing

Ask for any missing information before drafting. Minimum required:

1. **Business type:** B2B, B2C, or both? (determines lead gen approach and channel priority)
2. **Location:** Country and city/town (determines platform availability and mobile money context)
3. **Target customer:** Demographics, digital behaviour, preferred platforms
4. **Current digital presence:** Website? Facebook page? WhatsApp Business? Google listing?
5. **Monthly marketing budget:** UGX / KES / TZS / RWF amount, or estimate
6. **Sales cycle:** How long from first contact to purchase? (affects attribution and content strategy)
7. **Primary marketing goal:** Lead generation? Awareness? Retention? eCommerce sales?
8. **B2B-specific (if applicable):** Average sale value, observed retention, fully loaded CAC, contribution and payback assumptions

If information is missing, state your assumptions clearly and flag them for verification.

---

## Step 2: Structure of the Digital Marketing Strategy Section

Generate the following subsections in order. Adjust depth based on plan length requirements.

---

### 2.1 Digital Marketing Overview

Write a concise explanation covering:
- The digital landscape in the business's market (EA-specific platform penetration, mobile-first context)
- Why digital marketing is specifically suited to this business type
- The overall digital marketing objective (what the strategy will achieve)

**Key framing:** "Digital marketing is not a separate strategy  it is the primary channel through which [Business Name]'s integrated marketing communications plan is executed. The goal is not online presence for its own sake, but measurable customer acquisition and retention at a viable cost." (McDonald, Wilson, and Chaffey, 2024)

---

### 2.2 Digital Situation Audit

Assess the current state across three dimensions:

**Owned media audit:**
| Asset | Status | Quality Assessment |
|-------|--------|-------------------|
| Website | Exists / Not yet built | Load speed, mobile-optimised, clear CTA |
| WhatsApp Business | Active / Not yet set up | Product catalogue, auto-reply configured |
| Facebook Business Page | Active / Inactive | Followers, last post date, response rate |
| Google Business Profile | Claimed / Unclaimed | Photos, reviews, hours complete |
| Email list | X contacts | Opt-in, engaged, segmented |

**Paid media assessment:**
- Current ad spend (if any) and results achieved
- Platforms used, acquisition cohort and media-only versus fully loaded CAC estimate

**Earned media assessment:**
- Existing reviews (Google, Facebook)
- Word-of-mouth referral volume (ask client to estimate % of new customers from referrals)
- Social mentions / shares

**Competitor digital audit:**
- Are competitors running Facebook Ads? (searchable via Meta Ad Library: facebook.com/ads/library)
- Do competitors have a Google Business listing?
- What content are competitors posting?
- Where are the gaps this business can exploit?

---

### 2.3 POEM Strategy (Paid, Owned, Earned)

Structure the digital marketing strategy across the three media types (McDonald, Wilson, and Chaffey, 2024):

**Owned and managed destinations (test readiness, cost and control):**
List the owned assets the business will build/maintain and what each contributes:
- Website: [specific pages, content focus, conversion goals]
- WhatsApp Business: [catalogue, broadcast list, automation, response SLA]
- Facebook Business Page: [content cadence, community management]
- YouTube / TikTok channel: [video content focus]
- Email list: [opt-in mechanism, nurture sequence]
- Google Business Profile: [photos, posts, review response]

**Paid media (conditional investment):**
- Compare candidate channels using buyer/account evidence and the intended decision.
- Record spend ceiling, production cost, labour, tools and measurement cost.
- Define permitted audience parameters and verify current account/region eligibility.
- Choose an objective linked to a tested destination and accountable follow-up.
- Set a provisional acquisition ceiling from cohort contribution, cash, payback and downside scenarios with the finance owner; lifetime revenue alone is insufficient.

**Earned media (accelerate through excellence):**
- Neutral review invitation strategy consistent with current platform rules; do not selectively solicit only satisfied customers.
- Referral programme (if applicable)
- PR: any local media, industry associations, community groups that will amplify content
- Relevant community participation only with administrator rules, member expectations and permission respected; no unsolicited group seeding.

---

### 2.4 RACE Framework: Customer Journey Map

Apply the RACE framework (Chaffey, SmartInsights.com, in McDonald et al., 2024) to map how the business will guide customers from first awareness to loyal advocate:

**REACH** (attract strangers to become prospects):
- Channels: [e.g. Facebook Ads, TikTok organic, Google Search, referrals]
- Content: [e.g. problem-awareness posts, brand introduction videos]
- KPI: Monthly reach, new follower growth, website sessions

**ACT** (encourage prospects to engage):
- Channels: [e.g. WhatsApp catalogue, Facebook page content, website blog]
- Content: [e.g. product showcase, how-to videos, FAQ posts]
- KPI: WhatsApp enquiries per month, content engagement rate, landing page time-on-page

**CONVERT** (turn engaged prospects into paying customers):
- Channels: [e.g. WhatsApp DM follow-up, Google Ads call-to-action, in-person visit]
- Content: [e.g. testimonials, pricing transparency, offer/discount for first purchase]
- KPI: Qualified enquiry-to-sale conversion, cohort CAC with cost boundary, collected revenue and contribution

**ENGAGE** (retain customers and build advocacy):
- Channels: [e.g. WhatsApp broadcast tips, loyalty offer, post-sale check-in]
- Content: [e.g. how-to-use tips, new product alerts, exclusive customer offers]
- KPI: Repeat purchase, lifetime contribution with cohort/horizon limits, qualified referrals and service experience

---

### 2.5 Channel Strategy

Prioritise channels based on the business's target audience, budget, and goals. For each selected channel, specify:

**Channel investment workpaper (complete one row per candidate):**

| Decision field | Evidence required |
|---|---|
| Channel and role | Buying situation, observed audience/account evidence and alternative routes |
| Invest, test, maintain or defer | Specific reason, uncertainty and condition for reconsideration |
| Total resource envelope | Media, fees, labour, production, tools, destination and follow-up cost |
| Production and response cadence | Available owner hours, sample effort and service commitment; label proposed cadence as a pilot |
| Readiness | Rights, account/region eligibility, tested destination, CRM and response owner |
| Evaluation | Qualified outcome, observation window, comparison, cost boundary and attribution limits |
| Decision rule | Spend cap, evidence minimum, stop/revise rule and review owner/date |

**Channel selection rationale:** For each channel, state why it is or is not appropriate for this specific business. Not every channel is right for every business.

---

### 2.6 Content Strategy

Define what content will be produced, who will produce it, and at what cadence.

**Content pillar framework (adapt to business):**

| Candidate role | Buyer question and proof | Possible format |
|---|---|---|
| Education | Which consequential decision does the buyer need help making? | Demonstration, explanation or decision tool |
| Service/product proof | What authorised sample or result supports the promise? | Annotated work, permissioned case or labelled demonstration |
| People and process | Which delivery responsibility or craft decision matters? | Practitioner explanation or process walkthrough |
| Offer | Who is this for, what is included, and what happens next? | Service explanation or relevant invitation |

Allocate effort from buyer questions, funnel gaps, proof availability and team
capacity. No universal content percentages or 10-4-1 quota applies. Test the
proposed mix and retain only formats that serve a defined job.

**Content calendar:** Create a monthly content calendar (4-week plan) specifying:
- Platform  content type  topic  who creates it  publish date  CTA

**Content production resources:**
- Choose capture equipment from the creative brief, audio/lighting needs and acceptance standard; test a representative sample.
- Route graphic production to the design engine; verify tool suitability, licence and current cost.
- Choose video editing from format, caption, rights and workflow requirements; verify current tool cost.
- ChatGPT/Claude: first drafts of captions, blog posts, email copy (always edit for brand voice)

---

### 2.7 Acquisition economics and contribution

Agree cost, cohort, time period and contribution definitions with the finance
owner. CAC divides matching acquisition costs by new customers; distinguish
media-only from fully loaded cost. Lifetime contribution requires evidence for
retention, fulfilment/service cost, returns and the time horizon. Revenue-based
lifetime value is not profit and does not establish a safe acquisition ceiling.

ROAS is attributed revenue divided by media spend; report its attribution window
and limitations. Incremental marketing ROI uses incremental contribution before
marketing less incremental marketing cost, divided by incremental marketing cost.
Without credible causal evidence, report attributed contribution and withhold
incremental ROI. Never subtract marketing cost twice.

Reconcile cash payback, sales lag, capacity and downside scenarios. Use neither
a universal CAC/LTV percentage nor an automatic forecast of declining CAC.
Keep self-reported discovery alongside tracking/CRM evidence and reconcile
duplicates. See [marketing decision workpapers](../marketing-plan-orchestrator/references/marketing-decision-workpapers.md).

---

### 2.8 Budget Allocation

Present the digital marketing budget as a table:

| Category | Months 1–3 | Months 4–6 | Months 7–12 | Annual Total |
|----------|-----------|-----------|------------|-------------|
| Owned media (staff time, tools) | | | | |
| Paid advertising (Facebook, Google) | | | | |
| Content production (design, video, photography) | | | | |
| Influencer partnerships | | | | |
| Analytics tools / CRM | | | | |
| **Total** | | | | |

**Budget decision:** Build the budget from objectives, evidence, production and sales capacity, cash constraints and bounded tests. A percentage of revenue may be a comparison, not a universal spending rule.

**Startup allocation decision:** Compare total costs, learning value and capacity across viable routes. Authorise a bounded paid test only with a working destination, response owner, measurement plan and affordable loss ceiling. Owned and earned media also consume resources; an organic conversion history is useful evidence, not a universal prerequisite.

---

### 2.9 Platform, campaign, measurement, and AI detail

Load only the directly relevant reference:

- `references/social-media-platforms.md`, `references/google-ads.md`, `references/facebook-marketing.md`, `references/tiktok-advertising.md`, or `references/youtube-marketing.md` for channel selection and execution.
- `references/digital-marketing-campaigns.md` for campaign design and measurement cadence.
- `references/marketing-60-kotler.md` for phygital and generational behaviour, after verifying present-day applicability.
- `references/ai-marketing-playbook.md` for AI-assisted marketing decisions, human review, privacy, cost, and failure controls.

Do not copy tool, platform, budget, demographic, or performance claims from a reference without verifying the current product, geography, date, evidence, and client fit.

---

## Step 4: Cross-References

After generating this section, note that:
- Market analysis (Section 04) should provide the target customer profile and competitive digital landscape
- Marketing and sales strategy (Section 07) should reference this section for digital channel tactics
- Financial projections (Section 10) should include the digital marketing budget as a line item
- AI integration (Section 14) should reference this section for marketing AI use cases
- Implementation timeline (Section 13) should schedule the digital marketing setup activities in Months 1–3

---

## References

- **Brand as media company**: See `references/brand-as-media-company.md` for the three pillars of social business (People/Process/Platforms), five content narrative inputs  hero narrative, brand tone of voice, content tiers by channel (Tier 1 Hero/Tier 2 Hub/Tier 3 Hygiene), converged media execution model (Paid/Owned/Earned interdependence), employee and customer advocacy programmes, minimum viable content governance, and EA context (WhatsApp as Tier 3, Facebook as Tier 2)  from Brito (*Your Brand, The Next Media Company*, Pearson, 2013). **Read when building the brand content narrative or structuring multi-channel content operations.**

---

## Citation Format

For business plan use, cite as follows (first use):

- McDonald, Wilson, and Chaffey's (2024) POEM framework
- Historical B2B acquisition frameworks require the contribution and cohort corrections in Section 2.7 before financial use.
- Robinson's (2023) seven-channel digital marketing model
- Kotler, Kartajaya, and Setiawan's (2023) phygital natives framework
- Lamplugh's (2024) AI marketing implementation roadmap
- Keshwani's (2023) five-point campaign analysis framework
- Marshall and Yu's (2022) Why/How/What video framework and Power Triangle
- Geddes' (2014) Quality Score and buying funnel keyword framework
- Mathew's (2021) YouTube SEO framework, video type taxonomy, and monetisation paths
- Willis's (2024) passive income framework and platform monetisation tools

Full references for the appendix:
- McDonald, M., Wilson, H., and Chaffey, D. (2024) *Marketing Plans: Profitable Strategies in the Digital Age*, 9th Edition. Hoboken, NJ: Wiley.
- Bodnar, K. and Cohen, J.L. (2012) *The B2B Social Media Book*. Hoboken, NJ: Wiley.
- Robinson, D. (2023) *The Digital Marketing Playbook for 2023*. Self-published.
- Kotler, P., Kartajaya, H., and Setiawan, I. (2023) *Marketing 6.0: The Future Is Immersive*. Hoboken, NJ: Wiley.
- Lamplugh, M. (2024) *The AI Marketing Playbook: Concepts, Methods, Applications*, 2nd Edition. Boston, MA: Mercury Learning and Information.
- Keshwani, A. (2023) *55 Digital Marketing Masterpieces: Inspiring Your Next Winning Campaign*. Bangalore: The Write Order Publications.
- Marshall, P. and Yu, D. (2022) *The Definitive Guide to TikTok Advertising: How to Access 1 Billion People in 10 Minutes*. Chicago, IL: Perry Marshall & Associates.
- Geddes, B. (2014) *Advanced Google AdWords*, 3rd Edition. Indianapolis, IN: Wiley/Sybex.
- Mathew, J. (2021) *YouTube Marketing 2021: Do YouTuber's Secrets for Business with the Beginner's Guide to Growing Your Social Video Channel a Money Machine*. Self-published.
- Rouhiainen, L. (2021) *101 Facebook Marketing Tips and Strategies for Small Businesses*. Self-published.
- Various authors (2021) *Social Media Marketing 2021-22: Beginners Guide to Making Money Online*. Self-published.
- Brito, M. (2013) *Your Brand, The Next Media Company: How a Social Business Strategy Enables Better Content, Smarter Marketing, and Deeper Customer Relationships*. Indianapolis, IN: Que Biz-Tech/Pearson.
- Kane, A. (2021) *Social Media Marketing and Online Business 2021: Beyond 2020 Rise to the Top of the Main eCommerce Platforms*. Self-published.
- Willis, T. (2024) *Social Media Marketing in 2024: Mastering Facebook, Instagram, TikTok, Make Passive Income and More*. Self-published.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Target customer, offer, journey, proof, price, goals, capacity, and business-plan assumptions | Client intake and owning plan sections | Required | Return hypotheses and evidence requests, not channel certainty |
| Channel, campaign, cohort, content, conversion, retention, and attribution evidence | Analytics, CRM, advertising, sales, interviews, and experiments | Conditional | Mark performance and targets unassessed |
| Marketing cost, revenue, refund, contribution, and payback definitions | Chwezi Accounting Doctrine and finance model | Required for ROI claims | Keep budget and return conclusions conditional |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Digital marketing strategy section | Business-plan pipeline, founder, and operating team | Objectives, journey, channel roles, content, campaigns, budget, measurement, and justified AI use reconcile |
| Channel and experiment register | Marketing, sales, finance, and reviewers | Each initiative has audience, hypothesis, owner, cost cap, metric, stop rule, and evidence status |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Channel selection and claim register | Audience behaviour, source, date, channel role, countercase, and decision | No platform is selected because it is fashionable or assumed universal |
| Marketing economics reconciliation | CAC, contribution, refund, retention, attribution, and payback definitions | Measures reconcile to finance data and current Chwezi doctrine |

## Capability Contract

Read or search access is required; editing or mutation is allowed only with authorised permission.

Planning defaults to read-only. Do not publish content, launch campaigns, contact audiences, install tracking, upload customer data, change prices, or spend budget without explicit authority. AI use must respect privacy, consent, brand, factual review, security, and human approval.

## Degraded Mode

Without research, analytics, platform access, current documentation, or finance definitions, return a hypothesis-led strategy and validation backlog. Mark channel performance, budget efficiency, and AI capability `not assessed`; never invent benchmarks or claim a tool function is current.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Customer intent is proven in search | Test intent-led search and landing paths | Paying for broad awareness when demand is active |
| Offer or conversion is unproven | Use small owned, earned, and research tests before paid scale | Amplifying a weak proposition |
| Channel evidence is weak or audience fit uncertain | Run a bounded experiment with a stop rule | Permanent budget allocation by assumption |
| AI use adds measurable operating value and controls exist | Stage a human-reviewed pilot | Trend-led automation or harmful output |

## Workflow

1. Confirm decision, audience, offer, proof, journey, geography, capacity, budget authority, and plan dependencies.
2. Audit current channels, content, conversion, retention, attribution, privacy, and customer evidence.
3. Map objectives to customer behaviours and choose only channels with a supported role.
4. Define content, campaign, landing, sales handoff, retention, and measurement as one system.
5. Reconcile budget, CAC, contribution, refunds, retention, and payback with Chwezi doctrine and the finance model.
6. Assess AI use case by customer value, operating value, data permission, human oversight, cost, and failure mode.
7. Create staged experiments with owners, cost caps, metrics, stop rules, and recovery actions.
8. Release only after claim verification, privacy, finance, feasibility, and anti-slop gates pass.

## Quality Standards

The strategy must tie every channel and AI use to a customer behaviour, operating owner, budget, measure, and stop decision. Current platform claims and financial returns require verified sources and reconciled definitions.

## Anti-Patterns

- Including every platform. Fix: select channels by customer behaviour, intent, capacity, and evidence.
- Setting targets from uncited benchmarks. Fix: use client baselines or labelled test targets.
- Counting reach as commercial success. Fix: connect reach to qualified action, conversion, retention, and contribution.
- Automating customer communication without review. Fix: define data permission, escalation, factual checks, and human ownership.
- Hiding attribution limits. Fix: state the method, blind spots, and decision tolerance.
- Spending before economics reconcile. Fix: apply Chwezi doctrine and stage budget behind evidence gates.

## Worked Example

A local repair firm has verified high-intent search demand but weak enquiry handling. Prioritise a small search test and landing-to-WhatsApp response process, cap spend until conversion and contribution are observed, and defer AI chat automation until message volume and escalation controls justify it.
<!-- dual-compat-end -->
