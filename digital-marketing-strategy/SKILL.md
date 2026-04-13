---
name: digital-marketing-strategy
description: Generate the digital marketing strategy and AI strategy sections for a business plan. Use this skill whenever a business plan requires a digital marketing section, online marketing plan, social media strategy, or AI-assisted marketing plan. Every business plan must include both a digital marketing strategy and an AI marketing integration section.
---

# Digital Marketing Strategy Skill

## Use When

- Use when this skill is the primary workflow for the requested task.
- Use when creating, reviewing, or improving this skill's main artifact.
- Use when this output must align with adjacent sections, assumptions, or audience requirements.

## Do Not Use When

- Do not use when another section or meta-skill is the primary owner of the task.
- Do not use when the required inputs are unavailable and cannot be stated transparently as assumptions.
- Do not use for provider-specific UI behaviour; keep the workflow portable.

## Required Inputs

- Business, client, or proposal context relevant to this skill
- Country, audience, funder, or user context where relevant
- Available assumptions, evidence, constraints, and dependencies
- Adjacent section outputs where consistency matters

## Workflow

1. Clarify the objective, audience, and scope for this skill.
2. Gather the minimum required inputs and note any missing assumptions.
3. Read the referenced materials only as needed.
4. Produce or revise the artifact using the skill-specific method below.
5. Reconcile the output with adjacent sections, numbers, risks, and evidence.
6. Flag unresolved gaps, assumptions, or follow-up work.

## Quality Bar

- Output is specific, decision-useful, and not generic
- Assumptions are explicit where relevant
- Claims align with the rest of the plan, proposal, or workflow
- Wording is structured, concise, and audience-appropriate

## Anti-Patterns

- Generic filler that could describe any business or situation
- Hidden assumptions or unsupported claims
- Contradictions with financials, implementation, risk, or audience requirements
- Provider-specific operating assumptions embedded in the portable workflow

## Outputs

- The primary artifact or analysis owned by this skill
- Any key assumptions, open questions, and cross-skill dependencies



## Purpose

Every business plan produced by this skills suite must include:
1. A **Digital Marketing Strategy**  how the business will use digital channels to reach customers, generate leads, and convert sales
2. An **AI Marketing Integration** section  how AI tools will be embedded in the marketing and sales process

This skill generates both sections. It draws on eight primary reference frameworks:

**Strategy and cross-channel frameworks:**
- **McDonald, Wilson, Chaffey** (Marketing Plans, 9th ed)  POEM model, RACE framework, 6 digital channels, IMC, omnichannel, measurement  `references/marketing-plans-chaffey.md`
- **Bodnar and Cohen** (B2B Social Media Book)  ROI formula, COCA/TLV, 5-step lead generation, 10-4-1 rule  `references/b2b-social-media.md`
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

1. **Business type:** B2B, B2C, or bothSection  (determines lead gen approach and channel priority)
2. **Location:** Country and city/town (determines platform availability and mobile money context)
3. **Target customer:** Demographics, digital behaviour, preferred platforms
4. **Current digital presence:** WebsiteSection  Facebook pageSection  WhatsApp BusinessSection  Google listingSection 
5. **Monthly marketing budget:** UGX / KES / TZS / RWF amount, or estimate
6. **Sales cycle:** How long from first contact to purchaseSection  (affects attribution and content strategy)
7. **Primary marketing goal:** Lead generationSection  AwarenessSection  RetentionSection  eCommerce salesSection 
8. **B2B-specific (if applicable):** Average sale value, average customer lifetime, COCA target

If information is missing, state your assumptions clearly and flag them for verification.

---

## Step 2: Structure of the Digital Marketing Strategy Section

Generate the following subsections in order. Adjust depth based on plan length requirements.

---

### 2.1 Digital Marketing Overview

Write 23 paragraphs covering:
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
- Platforms used and COCA estimate

**Earned media assessment:**
- Existing reviews (Google, Facebook)
- Word-of-mouth referral volume (ask client to estimate % of new customers from referrals)
- Social mentions / shares

**Competitor digital audit:**
- Are competitors running Facebook AdsSection  (searchable via Meta Ad Library: facebook.com/ads/library)
- Do competitors have a Google Business listingSection 
- What content are competitors postingSection 
- Where are the gaps this business can exploitSection 

---

### 2.3 POEM Strategy (Paid, Owned, Earned)

Structure the digital marketing strategy across the three media types (McDonald, Wilson, and Chaffey, 2024):

**Owned media (build first, lowest cost, permanent):**
List the owned assets the business will build/maintain and what each contributes:
- Website: [specific pages, content focus, conversion goals]
- WhatsApp Business: [catalogue, broadcast list, automation, response SLA]
- Facebook Business Page: [content cadence, community management]
- YouTube / TikTok channel: [video content focus]
- Email list: [opt-in mechanism, nurture sequence]
- Google Business Profile: [photos, posts, review response]

**Paid media (amplify what works; COCA-disciplined):**
- Primary paid channel (usually Facebook/Meta Ads for EA consumer; Google Ads for high-intent search)
- Monthly budget allocation
- Target audience parameters
- Campaign objective (awareness, traffic, leads, conversions)
- COCA target: state what maximum acquisition cost is acceptable given TLV

**Earned media (accelerate through excellence):**
- Review generation strategy (ask every satisfied customer; platform-specific)
- Referral programme (if applicable)
- PR: any local media, industry associations, community groups that will amplify content
- WhatsApp group seeding: identify relevant WhatsApp groups where target customers gather

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
- KPI: Conversion rate (enquiry to sale), COCA per channel, revenue from digital leads

**ENGAGE** (retain customers and build advocacy):
- Channels: [e.g. WhatsApp broadcast tips, loyalty offer, post-sale check-in]
- Content: [e.g. how-to-use tips, new product alerts, exclusive customer offers]
- KPI: Repeat purchase rate, TLV, referral rate, Google/Facebook review count

---

### 2.5 Channel Strategy

Prioritise channels based on the business's target audience, budget, and goals. For each selected channel, specify:

**Recommended channel priority template (adapt to business):**

| Channel | Priority | Monthly Budget | Content Frequency | KPI |
|---------|----------|---------------|-------------------|-----|
| WhatsApp Business | Primary | Staff time only | Daily response; weekly broadcast | Enquiry  sale conversion rate |
| Facebook (organic) | Primary | Staff time only | 45 posts/week | Enquiries from posts, engagement rate |
| Facebook Ads | Secondary | [Budget] | Campaign-based | CPL, COCA |
| Google Business Profile | Primary | Free (staff time) | Weekly post + review responses | Local search impressions, directions requests |
| YouTube/TikTok (video) | Secondary | Staff time | 2 video/week | Views, WhatsApp leads from video |
| Website / SEO | Medium-term | Content + basic hosting | 2 blog posts/month | Organic sessions, enquiry form submissions |
| Email marketing | B2B only | Low (tool cost) | 2 per month | Open rate, leads from email |
| LinkedIn | B2B only | Staff time | 3 per week | Connection growth, InMail responses |
| Influencer | Optional | [Budget] | Campaign-based | Attributable leads per influencer |

**Channel selection rationale:** For each channel, state why it is or is not appropriate for this specific business. Not every channel is right for every business.

---

### 2.6 Content Strategy

Define what content will be produced, who will produce it, and at what cadence.

**Content pillar framework (adapt to business):**

| Pillar | Description | % of Content | Formats |
|--------|-------------|-------------|---------|
| Education | Teach customers something useful (how-to, tips, FAQs) | 40% | Video, WhatsApp tip, blog post |
| Social proof | Show customers that others trust and use the business | 30% | Testimonials, case studies, before/after |
| Brand/culture | Show the people, process, and values behind the business | 20% | Behind-the-scenes, team photos, production |
| Promotion | Direct offer, product launch, call-to-action | 10% | Offer post, product showcase with price |

**Apply 10-4-1 rule** (Bodnar and Cohen, 2012): For every 15 posts, 10 share/curate others' content, 4 are original insights, 1 is a direct promotional post.

**Content calendar:** Create a monthly content calendar (4-week plan) specifying:
- Platform  content type  topic  who creates it  publish date  CTA

**Content production resources:**
- Smartphone camera: sufficient for all social video
- Canva (free): graphic design for posts and stories
- CapCut (free): video editing for Reels/TikTok/YouTube Shorts
- ChatGPT/Claude: first drafts of captions, blog posts, email copy (always edit for brand voice)

---

### 2.7 ROI Framework: COCA and TLV

This section makes the financial case for the digital marketing investment (Bodnar and Cohen, 2012).

**Step 1: Calculate TLV (Total Lifetime Value)**
- Average sale value: [amount in local currency]
- Average number of purchases per customer per year: [number]
- Average customer retention period: [years]
- TLV = Average sale  Annual purchases  Retention years = [TLV]

**Step 2: Set COCA target**
- A healthy COCA:TLV ratio for most businesses is 1030%
- Maximum acceptable COCA = TLV  20% = [target COCA]
- This is the budget ceiling per new customer acquired

**Step 3: Track COCA by channel**
- Facebook Ads spend  customers from Facebook = Facebook COCA
- Staff time on WhatsApp  rate  customers from WhatsApp = WhatsApp COCA
- Total marketing costs  total new customers = blended COCA

**Step 4: Calculate ROI quarterly**
- ROI % = (TLV  COCA)  COCA  100

**Attribution approach:** Use first-action attribution (record how the customer first heard about the business). Track in a simple Google Sheet: date | customer name | how they heard of us | sale value | referral given (Y/N).

**Note for business plan:** Include a table projecting COCA and TLV for Year 1 through Year 3, showing how increasing brand awareness and customer retention reduce COCA over time and increase TLV through repeat purchases.

---

### 2.8 Budget Allocation

Present the digital marketing budget as a table:

| Category | Month 13 | Month 46 | Month 712 | Annual Total |
|----------|-----------|-----------|------------|-------------|
| Owned media (staff time, tools) | | | | |
| Paid advertising (Facebook, Google) | | | | |
| Content production (design, video, photography) | | | | |
| Influencer partnerships | | | | |
| Analytics tools / CRM | | | | |
| **Total** | | | | |

**As % of projected revenue:** Digital marketing budget should be 515% of projected monthly revenue for growth-stage businesses. Established businesses may invest 38%.

**Startup allocation principle:** Begin with owned and earned media (low cost). Move to paid media only once COCA tracking is in place and at least one converting content format has been identified.

---

### 2.9 Platform-Specific Ad Strategy

For businesses planning paid digital advertising, provide platform-specific guidance for each relevant channel. Do not include all platforms  select based on the business type, target audience, and budget.

**Google Search Ads**  include when:
- The business serves customers who actively search for the product/service (plumbers, lawyers, schools, cleaning services, hardware)
- There is clear purchase-intent search volume for the category in the target city
- Budget allows: minimum UGX 25,00050,000/day to gather meaningful data

Apply the buying funnel keyword framework (Geddes, 2014): classify keywords by funnel stage (awareness  consideration  purchase); weight budget toward purchase-intent keywords; assign each ad group one tight topic; match landing page to ad copy precisely.

Include:
- 35 core keyword themes with match types
- Quality Score optimisation actions (tight ad groups, keyword in headline, relevant landing page)
- Campaign budget allocation and CPA target
- Conversion events to track (WhatsApp click, call, form, purchase)

**TikTok Ads**  include when:
- Primary target audience is aged 1835
- The business has or can create short video content (any business can)
- Budget allows: minimum UGX 75,000/day ($20) per ad group
- The business already has a proven offer or existing funnel (TikTok amplifies; it does not validate)

Apply the Why/How/What framework (Marshall and Yu, 2022): plan at least one video in each category; structure 15-second ads with Hook (05s)  Pain/Solution (510s)  CTA (1015s); repurpose existing best-performing content from Facebook or WhatsApp first.

Include:
- Content plan: 3 Why + 3 How + 3 What videos for launch
- Ad format: In-Feed Ads for all; Spark Ads if organic posts already performing
- Campaign objective selection (Video Views / Traffic / Conversions / Lead Gen)
- Metrics to track: video completion rate, engagement rate, CPA, ROAS

**Platform decision table  use to select which platforms to include:**

| Business Type | Primary Platform | Secondary | Skip |
|--------------|----------------|-----------|------|
| Local services (cleaning, plumbing, events) | Google Search | Facebook | TikTok (lower intent) |
| Food / restaurant / hospitality | Facebook + Instagram | TikTok | Google (lower search volume) |
| Retail / fashion / beauty | TikTok + Instagram | Facebook | Google (browse-driven, not search) |
| B2B services | LinkedIn + Google Search | Facebook | TikTok |
| Agriculture / FMCG / rural | Facebook (WhatsApp integration) | Google | TikTok (lower rural penetration) |
| Youth-focused / education / fitness | TikTok | Instagram | Google (awareness stage) |
| eCommerce (online store) | Facebook + Google Shopping | TikTok |  |

---

### 2.10 Phygital Customer Profile and Generational Context

If the business serves younger customers (under 35), apply the phygital natives framework (Kotler, Kartajaya, and Setiawan, 2023):

**Assess which customer cohort the business primarily serves:**

| Cohort | Birth Years | Digital Behaviour | Content Preference | EA Marketing Implication |
|--------|------------|------------------|-------------------|--------------------------|
| Gen X | 19651980 | Internet-adopter | Email, Facebook, WhatsApp | Trust professional tone; value reliability |
| Millennials (Gen Y) | 19811996 | Digital-confident | Facebook, Instagram, YouTube | Value sustainability + social proof |
| Gen Z | 19972012 | Digital-native (phygital) | TikTok, Instagram, YouTube Shorts | Authenticity, short-form video, community |
| Gen Alpha | 2013+ | AI/Metaverse native | TikTok, gaming, AI chat | Immersive, interactive, hyper-personal |

**For Gen Z and Gen Alpha audiences, apply these content principles:**
- Lead with authenticity: raw, unfiltered content > polished corporate ads
- Short-form video first (first 3 seconds must hook; add captions  60%+ watch without sound)
- Community-based channels (WhatsApp groups, Facebook Groups) convert better than paid feed ads
- Show values alignment: sustainability, local employment, DEI  in proof, not slogans
- Pragmatic messaging: show price and value clearly; avoid hype and unverifiable claims
- Experience over product: market what the product enables (lifestyle, outcome), not just its features

**Phygital loop mapping:** For businesses serving phygital native customers, map the phygital customer journey:
Online discovery (TikTok/Facebook)  Physical visit or WhatsApp  Mobile Money payment  UGC creation (WhatsApp Status/TikTok)  Peer referral (WhatsApp group)  Repeat cycle

---

### 2.11 Campaign Strategy

For each major campaign planned in Year 1, apply the 5-point campaign framework (Keshwani, 2023):

| Element | Detail |
|---------|--------|
| **Problem Statement** | What specific business challenge does this campaign solveSection  |
| **Process** | Which channel, creative approach, and tactic will be usedSection  |
| **Expected Result** | Quantified outcome (X leads, X% reach increase, X new customers) |
| **What Should Work Most** | The primary mechanism driving the result (storytellingSection  social proofSection  offerSection ) |
| **Success Metric** | How will success be measured and trackedSection  |

**Campaign type selection guide:**

| Business Goal | Recommended Campaign Type | Primary Channel |
|--------------|--------------------------|----------------|
| Build brand awareness | Storytelling / founder video | Facebook organic + TikTok |
| Generate leads quickly | Lead generation offer + paid ad | Facebook Ads + WhatsApp |
| Build social proof | UGC testimonial campaign | Google Reviews + Facebook posts |
| Reach new audiences | Micro-influencer partnership | Instagram + WhatsApp referral |
| Retain existing customers | Loyalty email/WhatsApp sequence | WhatsApp broadcast + Email |
| Re-engage lost prospects | Retargeting campaign | Meta Pixel retargeting |
| B2B lead generation | Content marketing + LinkedIn | Blog + LinkedIn + Email |

**Storytelling content types (by effectiveness for EA SMEs):**
1. **Founder story**  why you started, what problem you solve, who you serve
2. **Customer transformation**  before/after, real client (with permission), specific numbers
3. **Behind-the-scenes**  production process, team, quality control, sourcing
4. **Educational how-to**  teach something useful; establishes authority
5. **Community impact**  jobs created, local suppliers, environmental practice

---

### 2.12 KPIs and Measurement Dashboard

Define the 610 metrics that will be reviewed monthly:

**Monthly marketing review dashboard:**

| Metric | Channel | Measurement Tool | Month 1 Target | Month 12 Target |
|--------|---------|-----------------|---------------|----------------|
| Total leads generated | All | CRM/spreadsheet | [X] | [X] |
| WhatsApp enquiries | WhatsApp | Manual count | [X] | [X] |
| Facebook page reach | Facebook | Meta Business Suite | [X] | [X] |
| Website sessions | Website | Google Analytics | [X] | [X] |
| New customers acquired | All | Sales records | [X] | [X] |
| COCA (blended) | All | Marketing budget  customers | [X] | [X] |
| Conversion rate (lead  sale) | All | CRM | [X] | [X] |
| Google reviews | Google | Google Business | [X] | [X] |
| Facebook ad CPL | Facebook Ads | Meta Ads Manager | [X] | [X] |
| TLV (current cohort) | All | Customer records | [X] | [X] |

**Review cadence:**
- Weekly: Post performance, ad spend, enquiry volume, responses pending
- Monthly: Full dashboard review, budget vs. results, channel optimisation decisions
- Quarterly: COCA/TLV calculation, strategy review, budget reallocation

---

## Step 3: AI Marketing Integration Section

Every business plan must include a standalone AI Marketing Integration section. Generate this after the Digital Marketing Strategy.

### AI Marketing Integration

**Opening statement:** Artificial intelligence is not a future technology for this business  it is available today at low or zero cost, and embedding it in marketing operations from Year 1 provides measurable competitive advantage in content velocity, customer responsiveness, and data-driven decision-making.

**Section structure:**

**1. AI-Assisted Content Creation**
- Tools: Claude (claude.ai), ChatGPT, or Gemini for drafting social media captions, blog posts, email copy, product descriptions, and ad copy
- Process: Brief the AI with brand voice, target audience, and specific goal  edit output  publish
- Time saving: Estimated X hours/week (calculate based on content volume)
- Critical note: AI-generated content must always be reviewed and edited. AI produces first drafts; the human adds accuracy, brand personality, and local context.

**2. AI-Assisted Customer Service**
- WhatsApp Business API (via WATI, Twilio, or similar) with automated FAQ responses, enquiry routing, and lead qualification flows
- Applicable if the business receives more than 20+ WhatsApp enquiries per day
- Chatbot handles: hours/location queries, price enquiries (with catalogue link), booking requests, order status
- Human handles: complaints, complex custom orders, negotiation, relationship management

**3. AI-Powered Ad Optimisation**
- Meta Advantage+ (Facebook/Instagram): algorithmic ad delivery that automatically finds the highest-converting audience  use broad targeting and let the algorithm optimise
- Google Performance Max: similar automatic optimisation across Google channels
- Both require 12 weeks of data before algorithm optimises effectively; do not turn off campaigns too early

**4. AI Analytics and Insights**
- Google Analytics 4 includes AI-powered anomaly detection and predictive metrics
- Meta Business Suite provides AI-driven audience insights and content performance summaries
- Simple prompt-based analysis: export marketing data to Google Sheets  paste into Claude/ChatGPT with the question "What patterns do you seeSection  What should I changeSection "

**5. AI for Personalisation**
- Email platforms (Mailchimp, Brevo) with AI send-time optimisation
- Dynamic content blocks in email (show different product recommendations based on customer purchase history)
- WhatsApp broadcast lists segmented by customer type (new leads vs. existing customers vs. VIP clients)

**AI implementation roadmap (Month 112):**

| Month | AI Action |
|-------|-----------|
| 12 | Set up Claude/ChatGPT for content drafting; create prompt templates for your most frequent content types |
| 23 | Enable Meta Advantage+ on all Facebook/Instagram campaigns |
| 34 | Install Google Analytics 4; set up conversion events |
| 6 | Evaluate WhatsApp automation (WATI or similar) if enquiry volume justifies |
| 912 | Review AI tools across all channels; identify what to expand, automate further, or retire |

---

## Step 4: Cross-References

After generating this section, note that:
- Market analysis (Section 04) should provide the target customer profile and competitive digital landscape
- Marketing and sales strategy (Section 07) should reference this section for digital channel tactics
- Financial projections (Section 10) should include the digital marketing budget as a line item
- AI integration (Section 14) should reference this section for marketing AI use cases
- Implementation timeline (Section 13) should schedule the digital marketing setup activities in Month 13

---

## References

- **Brand as media company**: See `references/brand-as-media-company.md` for the three pillars of social business (People/Process/Platforms), five content narrative inputs  hero narrative, brand tone of voice, content tiers by channel (Tier 1 Hero/Tier 2 Hub/Tier 3 Hygiene), converged media execution model (Paid/Owned/Earned interdependence), employee and customer advocacy programmes, minimum viable content governance, and EA context (WhatsApp as Tier 3, Facebook as Tier 2)  from Brito (*Your Brand, The Next Media Company*, Pearson, 2013). **Read when building the brand content narrative or structuring multi-channel content operations.**

---

## Citation Format

For business plan use, cite as follows (first use):

- McDonald, Wilson, and Chaffey's (2024) POEM framework
- Bodnar and Cohen's (2012) ROI formula: (TLV  COCA)  COCA
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
