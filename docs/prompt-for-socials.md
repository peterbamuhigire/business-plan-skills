# Kickstart Prompt — Social Media & Digital Marketing Consultancy Skills Suite

Use this prompt verbatim (or lightly adapted) as your **first message** in a fresh Claude Code session inside the new empty repo you have already pulled locally.

---

## Scope Overview

This suite covers the **complete documentation toolkit** of a professional social media and digital marketing consultancy — from winning new business to delivering strategy, managing execution, reporting results, and training client teams. Every major deliverable a consultancy produces is represented as a skill, including PowerPoint presentation decks.

**Total skills:** ~40 across 9 groups. This is a full production suite, not a starter kit.

---

## The Prompt

```
You are bootstrapping a new Claude Code skills suite called **social-media-skills** — a complete documentation and deliverable toolkit for running a professional social media and digital marketing consultancy. Consultants use these skills to produce every document they need: from agency credentials and proposals, through strategy documents and content plans, to monthly reports, PowerPoint presentations, and client training guides.

Your skills directory is at C:\Users\Peter\.claude\skills. Before doing anything else, read the skill-writing skill at C:\Users\Peter\.claude\skills\skill-writing\SKILL.md so you understand the conventions for creating skills in this environment. Also read C:\Users\Peter\.claude\skills\claude-guides\skill-best-practices.md if it exists.

---

## Project Brief

**What this suite does:**
Enables a solo consultant or small agency to produce every deliverable in the social media and digital marketing consultancy lifecycle — professionally, consistently, and quickly.

**Platforms in scope:** Facebook, LinkedIn, WhatsApp Business, Instagram, YouTube, TikTok, X/Twitter — and website content (blog posts and editorial calendar only; web design is handled by a separate suite and is out of scope here).

**Presentation decks:** Skills prefixed deck- generate complete slide-by-slide content outlines in markdown format. Each slide entry includes: slide number, headline/key message, bullet points, speaker notes, and visual direction. The output is paste-ready into PowerPoint, Canva, or Google Slides — the skill does not generate the actual .pptx file but makes building it trivial.

**Default country context:** Uganda/East Africa. All examples, platform penetration data, pricing, and cultural references should reflect the Ugandan market unless the user specifies otherwise. Platform defaults for Uganda/EA:
- WhatsApp: dominant messaging platform, 90%+ smartphone users
- Facebook: largest social platform, all demographics
- Instagram: urban, 18–35, aspirational content
- TikTok: fast-growing, 16–30, entertainment-first
- YouTube: research, tutorial, long-form video
- LinkedIn: B2B, professionals, formal sector
- X/Twitter: opinion leaders, journalists, public figures, public sector

**Out of scope:** Actual graphic design, video editing/production, paid ad campaign management (bidding, creative testing), influencer contracts/payments, web design/development.

---

## Task: Bootstrap the Full Skill Suite

Create the complete directory structure, CLAUDE.md, and all SKILL.md files for this project. Do NOT write placeholder content — write complete, production-ready skills from the start.

---

### Step 1: Create CLAUDE.md

Create a CLAUDE.md in the repo root with these conventions:

**Naming conventions:**
- Business development skills: prefix biz-dev- (e.g., biz-dev-proposal)
- Client onboarding skills: numbered 01- through 04-
- Strategy skills: numbered 05- through 09-
- Planning skills: numbered 10- through 13-
- Platform skills: prefix platform- (e.g., platform-facebook)
- Execution playbooks: prefix playbook- (e.g., playbook-crisis-comms)
- Presentation deck skills: prefix deck- (e.g., deck-strategy-presentation)
- Meta/analytical skills: prefix meta- (e.g., meta-reporting)
- Training skills: prefix training- (e.g., training-client-team)
- Utility/generation skills: plain names (e.g., caption-writer)

**Authoring rules:**
- Every skill MUST have a SKILL.md with YAML frontmatter (name, description only)
- SKILL.md must stay under 500 lines; reference files go in references/ subfolder
- British English spelling throughout (organisation, colour, programme, behaviour, analyse, strategise)
- Always ask for: client business name, industry, country/city, and primary goal before generating any deliverable
- Source referencing: cite frameworks where they add credibility (parenthetical on first use; full reference in appendices section of the output document)
- Every skill must have a Required Input section and a Quality Criteria section

---

### Step 2: Business Development Skills

These skills help the consultant win new clients.

**biz-dev-credentials/**
Purpose: Generate the agency credentials document — the "who we are" document sent to prospective clients. Output: 1–2 page credentials document covering: agency overview and founding story, services offered (with plain-English descriptions), the approach/methodology (how the agency works), 3 anonymised client success stories (results-focused), team profiles (consultant bio format), and contact/next steps. Also includes a version as a deck outline (8 slides) for presenting credentials in person.

**biz-dev-proposal/**
Purpose: Generate a professional service proposal / Statement of Work for a prospective client. Sections: executive summary of the proposed engagement, understanding of the client's situation and goals, recommended scope of work (phased if appropriate), deliverables list with descriptions, timeline and milestones, investment (pricing table with options), terms and conditions placeholder, and next steps. Includes a proposal cover letter template. Output should be professional enough to sign without editing.

**biz-dev-pricing-menu/**
Purpose: Generate a services and pricing menu the consultant can share with enquiries. Format: tiered packages (Starter / Growth / Premium) covering social media management retainers, one-off strategy projects, content creation add-ons, training workshops, and reporting-only retainer. Each package lists: what is included, what is not included, monthly investment range, and ideal client type. Also includes a pricing rationale guide for the consultant (how to justify rates in a client conversation).

**biz-dev-case-study/**
Purpose: Generate a polished client case study from raw information the consultant provides. Input: client industry (anonymise if needed), challenge they faced, what was done, results achieved. Output: a 1-page case study in the Problem / Approach / Results / What the Client Said format, plus a 3-slide deck version for presentations.

---

### Step 3: Client Onboarding Skills (01–04)

**01-client-brief/**
Purpose: Structured intake questionnaire and brief template to gather all information needed before generating any strategy or content. Covers: business overview, target audience demographics, current social media presence (platforms, follower counts, posting history), competitors (3–5 named), content goals, tone of voice preferences, brand guidelines (logo, colours, fonts — ask client to share files), posting frequency expectations, budget for paid social if applicable, internal approval workflow, and content restrictions (topics to avoid). Output: a completed brief document and a summary "client at a glance" card (one page, shareable with the wider team).

**02-platform-audit/**
Purpose: Audit the client's existing presence on each relevant platform. Output: audit table per platform showing follower count, posting frequency, last post date, average engagement rate estimate, profile completeness score (10-point scale), and key gaps. Includes a competitive benchmarking section comparing the client against 3 competitors on the same metrics. Ends with a prioritised list of quick wins (changes to make in the first week). Also outputs a deck outline (6 slides: platform-by-platform findings + overall recommendation).

**03-audience-personas/**
Purpose: Develop 2–4 audience personas for the client based on the client brief and platform audit. Each persona includes: name, archetype label, age/gender/location, income/education/occupation, platforms used and peak usage times, content they engage with, pain points and goals, triggers that make them follow a brand, triggers that make them unfollow, and how the client's product/service fits their life. Personas are the foundation for all channel and content decisions. Output: persona cards (one per page, table format) plus a summary matrix.

**04-brand-voice-intake/**
Purpose: Develop the client's social media brand voice and visual identity brief. Output: brand voice guide (4–6 tone attributes, each with examples of right/wrong phrasing), platform tone adjustments (LinkedIn is more formal than TikTok — show how the same message changes), a vocabulary list (words to use / words to avoid), emoji policy, and hashtag brand identity. Visual identity section: image style direction (photography style, colour palette usage, typography guidance for graphics) — note this is guidance for briefing a designer, not actual design. Output is the standalone brand document the whole team uses.

---

### Step 4: Strategy Skills (05–09)

**05-social-media-strategy/**
Purpose: The master social media strategy document. Primary deliverable for strategy-only client engagements. Sections: situation analysis (where the client is now — market, competitors, current digital presence), strategy statement (what the social media presence will achieve and why), platform selection rationale (which platforms, with explicit reasoning using audience personas), brand voice summary, content pillars (3–5 pillars with descriptions), posting frequency and content mix by platform, community management principles, paid social integration guidance, KPI framework with 90-day targets, and a 90-day milestone roadmap. Apply the POEM model (Paid/Owned/Earned) and the RACE framework (Reach/Act/Convert/Engage) as the structural backbone. Cite Bodnar and Cohen (2012), Chaffey (2024), and Kotler et al. (2023) where relevant.

**06-digital-marketing-strategy/**
Purpose: Full-scope digital marketing strategy (broader than social media alone). Sections: digital situation audit (POEM model), target customer digital journey map (RACE framework), channel strategy (social, email, SEO content, paid search, influencer — with budget allocation rationale), content marketing strategy (blog + video + social as an integrated system), email marketing overview (list building, nurture sequences, broadcast strategy), measurement framework (COCA / TLV calculation, ROI targets by channel), and 12-month implementation roadmap. This skill coordinates with 05-social-media-strategy (social channels) and 12-website-content-plan (blog). Output is the boardroom-level document.

**07-email-marketing-strategy/**
Purpose: Standalone email marketing strategy for clients who have or want an email list. Sections: list building strategy (opt-in mechanisms on website, social, WhatsApp), list segmentation (leads / active customers / lapsed customers / VIPs), welcome sequence (5-email onboarding flow with briefs for each email), newsletter strategy (frequency, content mix, subject line approach), promotional email framework (offer emails, launch sequences), reactivation sequence for lapsed subscribers, and KPIs (open rate, click rate, unsubscribe rate, revenue per email). Includes 12 email subject line formulas with examples. Assumes Mailchimp or Brevo as the tool (reference both).

**08-influencer-marketing-strategy/**
Purpose: Influencer marketing strategy for clients who want to use creators and influencers. Sections: influencer tier definitions (nano 1K–10K / micro 10K–100K / macro 100K+ — with EA context: nano and micro often outperform macro for trust), how to identify right-fit influencers (audience match, engagement rate benchmarks, content quality), outreach approach (what to say, what to offer), campaign brief template for influencers, content usage rights guidance (not legal advice — refer to a lawyer for contracts), performance metrics (reach, engagement, link clicks, discount code redemptions, attributed sales), and a Uganda/EA influencer ecosystem note (Instagram and TikTok creators, YouTube vloggers, WhatsApp group admins as micro-influencers).

**09-campaign-strategy/**
Purpose: Plan a single focused marketing campaign (product launch, seasonal offer, awareness drive, event promotion). Output: campaign strategy document covering: campaign objective (SMART), target audience (from personas), campaign concept and core message, channel plan (which platforms, what content, in what sequence), campaign timeline (pre-launch / launch / sustain / close-out phases), content production list (what needs to be created), paid amplification plan if applicable, budget allocation, and success metrics. Includes a campaign brief template for briefing creative partners.

---

### Step 5: Planning Skills (10–13)

**10-content-pillars/**
Purpose: Define and develop the client's content pillars — the 3–5 thematic buckets that all content draws from. For each pillar: name, one-sentence purpose statement, example post types, percentage of content mix, platforms it suits best, and 10 starter content ideas. Apply the 10-4-1 rule (Bodnar and Cohen) and the Hero/Hub/Hygiene content tier model. Output includes a content pillar map (visual table) and a content pillar reference card the social media manager keeps on their desk.

**11-content-calendar/**
Purpose: Generate a 90-day master content calendar (month-by-month) showing what gets posted, on which platform, in which week, content type, pillar, and content brief (2 sentences). Output as a structured table. Includes: Ugandan/EA national holidays and observances, relevant international awareness days (World Environment Day, International Women's Day, etc.), industry-specific seasonal hooks, campaign windows, and a weekly rhythm template. The calendar coordinates across all selected platforms for cross-platform consistency and content repurposing opportunities.

**12-website-content-plan/**
Purpose: Generate a 90-day blog and website content plan (content only — no web design or technical SEO). Output: 12 blog post titles with 200-word content briefs each, editorial calendar mapping posts to weeks, suggested internal linking structure between posts, and primary keyword theme per post. Each brief includes: target reader persona, search intent, 5 key questions the post must answer, suggested article structure (H2 headings), word count guide, and recommended call to action. Also includes 4 content upgrade ideas (lead magnets tied to specific posts to build the email list).

**13-campaign-brief/**
Purpose: Generate a detailed campaign brief document for a specific campaign (used to brief internal team or external creative partners). Covers: campaign background and objective, target audience, key message (one sentence), campaign concept, deliverables list by platform, content specifications per deliverable (dimensions, length, format), do's and don'ts (brand guidelines reference), timeline with deadlines, approval process, and success metrics. This is the operational planning document; 09-campaign-strategy is the strategic document. Both are needed for a full campaign.

---

### Step 6: Platform-Specific Skills

Each generates a detailed, standalone content plan for that platform. Create all seven.

**platform-facebook/**
Covers: Page optimisation checklist (profile photo, cover, About section, CTA button, pinned post), content mix (image posts, video, Reels, Stories, polls, events, link posts — with recommended ratios), posting frequency (5×/week recommended for EA SMEs), Facebook Groups strategy (when to create, how to grow and moderate, content types), click-to-WhatsApp post strategy, Messenger auto-reply setup guidance, 30-day content plan with specific post ideas and captions, community management response templates (positive comments, complaints, DMs), and Facebook-specific KPIs.

**platform-instagram/**
Covers: Profile optimisation (bio with clear value proposition, link-in-bio strategy using Linktree or similar, Highlights structure), content types (Feed posts, Reels, Stories, Carousels), Reels strategy (hook in first 2 seconds, captions for silent viewing, trending audio guidance), grid aesthetic planning (colour palette and visual consistency), hashtag strategy (mix of niche/community/broad, 5–10 per post — avoid banned hashtags), UGC and collaboration approach, 30-day content plan with specific post ideas and caption templates, and Instagram-specific KPIs (reach, saves, shares, Reel views, follower growth rate).

**platform-linkedin/**
Covers: Company Page vs. personal profile strategy (when to prioritise each), content types (text posts, articles, document/carousel posts, native video, polls, events), thought leadership content approach (founder visibility, professional insight posts), B2B lead generation through content (content that attracts decision-makers), employee advocacy activation guide, posting frequency (3×/week for pages; 5×/week for personal profiles), 30-day content plan, connection growth and engagement tactics, and LinkedIn-specific KPIs (impressions, engagement rate, follower growth, post clicks, InMail response rate).

**platform-whatsapp/**
Covers: WhatsApp Business app setup checklist (business profile, catalogue, greeting message, away message, quick replies, labels), broadcast list strategy and segmentation (prospects / active customers / VIP clients), broadcast content guidelines (value-first: tips, news, exclusive offers — never spam), WhatsApp Status content plan (daily frequency, content types: behind-the-scenes, product showcases, quick tips), WhatsApp Groups strategy (when to create, naming, rules, moderation, content rhythm), opt-in capture methods (lead magnets, QR codes, click-to-WhatsApp ads) and opt-out etiquette, 30-day broadcast message calendar with templates, and WhatsApp-specific KPIs (estimated open rate, catalogue views, enquiry volume, conversion rate from broadcast).

**platform-tiktok/**
Covers: Account setup and profile optimisation (bio, profile link, category selection), content strategy philosophy (entertain first, sell later; authenticity over production quality), video structure templates (Hook 0–3s / Value 3–15s / CTA final 3s for standard; Hook 0–3s / Story 3–50s / Twist / CTA for longer), content series concepts (repeatable formats that build audience return behaviour), sound and music approach (trending sounds vs. original audio — general guidance; not specific tracks as these change), duet and stitch content ideas, posting frequency guide (1–2×/day for growth phase; 4–5×/week for maintenance), 30-day video content plan with concepts and hooks, and TikTok-specific KPIs (video views, completion rate, follower growth, profile visits, link clicks, shares).

**platform-youtube/**
Covers: Channel setup and optimisation (channel art, About section, channel trailer, playlist structure, end screen and cards), video type taxonomy (tutorial/how-to, vlog/behind-the-scenes, product showcase, client testimonial, Q&A / FAQ, reaction/commentary), YouTube SEO content guidance (title structure, description first 150 characters, tags approach, thumbnail text guidance — note: not technical SEO audit), video cadence (weekly minimum for algorithm traction), Shorts strategy (repurpose TikTok/Reels content, separate Shorts shelf), community tab usage, 30-day content plan with video topics, titles, and 3-sentence video briefs, and YouTube-specific KPIs (views, watch time hours, subscribers, CTR on impressions, average view duration, top traffic sources).

**platform-x-twitter/**
Covers: Profile optimisation (bio with keywords, pinned tweet strategy, header image), content types (single posts, threads, quote posts, polls, Spaces, list curation), posting frequency guide (3–5×/day for visibility — X rewards volume more than other platforms), thread strategy (educational threads as lead magnets and authority builders), community building tactics (replies as discovery, strategic following, list building), X's role in the EA media ecosystem (journalists, opinion leaders, public sector, NGOs — note this audience composition in the EA context), 30-day content plan, and X-specific KPIs (impressions, engagement rate, follower growth, profile visits, link clicks, mention volume).

---

### Step 7: Execution Playbooks

These are operational reference documents for the social media manager running the account day-to-day.

**playbook-community-management/**
Purpose: Standard operating procedures for managing the client's online community. Covers: response time SLAs by platform (Facebook comments: 2 hours; DMs: 4 hours; etc.), response templates by scenario (positive feedback, product enquiry, complaint, offensive comment, competitor mention, media inquiry), escalation protocol (when to involve the client directly), how to handle negative reviews on Google/Facebook, growing community engagement (conversation starters, engagement pods, pinned questions), and a monthly community health scorecard template.

**playbook-crisis-communications/**
Purpose: Social media crisis response playbook. Covers: crisis severity classification (Level 1: minor complaint / Level 2: viral negative post or media pickup / Level 3: major reputational threat), response protocol per level (who does what, in what order, within what timeframe), holding statement templates (acknowledge → investigate → update cadence), what NOT to do in a crisis (delete comments, go silent, be defensive, use humour), platform-specific crisis actions (pause scheduled posts, change ad creative, moderate comments), post-crisis review process, and a one-page crisis card the client keeps handy. Apply basic crisis communications principles (acknowledge, empathise, act, update).

**playbook-content-production/**
Purpose: Content production brief and shoot direction guide — helps the consultant brief a client's in-house team (or a photographer/videographer) to create content. Covers: photography brief template (scene description, required shots list, lighting guidance, do's and don'ts), video brief template (scene, dialogue/voiceover script, length, call to action, B-roll list), graphic design brief template (dimensions by platform, key message, colour palette reference, font reference, image guidance), how to batch-produce content (dedicate one shoot day to create 30 days of content), and a content shoot checklist.

**playbook-social-media-policy/**
Purpose: Generate a social media policy document for the client's employees — rules for how staff should (and should not) represent the company on their personal social media accounts. Covers: purpose and scope, what employees may post about the company (encouraged behaviours), what is prohibited (confidential information, client data, competitor commentary, legal matters), how to handle customer enquiries received via personal channels, how to disclose affiliation when posting about the company, consequences for policy violations, and a simple approval request process for employees who want to share company content. Output is a complete policy document the client can adopt with their legal review.

---

### Step 8: Presentation Deck Skills

These skills generate slide-by-slide content outlines in structured markdown. Each slide entry includes: **Slide [N] — Title | Headline (the one thing the audience must remember) | Bullets (3–5 max) | Speaker Notes | Visual Direction**. The output is paste-ready into PowerPoint, Canva, or Google Slides.

**deck-strategy-presentation/**
Purpose: Generate a 14-slide social media strategy presentation deck for presenting the strategy to the client. Structure: (1) Title slide, (2) Agenda, (3) Your audience — persona overview, (4) Where you are now — audit findings, (5) Where we are going — strategy statement and goals, (6) Platform selection — why these channels, (7) Content pillars — the themes, (8) What we will post — content mix examples, (9) Posting rhythm — frequency by platform, (10) Community management — how we engage, (11) Measuring success — KPI dashboard, (12) 90-day roadmap, (13) Investment and next steps, (14) Thank you / Q&A. Apply Minto's Pyramid Principle for slide sequencing (conclusion first, then evidence).

**deck-monthly-report/**
Purpose: Generate a 10-slide monthly performance report presentation for client delivery. Structure: (1) Title and period, (2) Executive summary — 3 key takeaways, (3) KPI scorecard — target vs. actual by platform, (4) Platform highlights — top metrics per platform, (5) Best-performing content — top 3 posts with performance data and analysis, (6) What worked and why, (7) What we are testing next month, (8) Content calendar preview — next 30 days, (9) Issues and recommendations, (10) Thank you. Tone: professional but conversational; clients should leave the meeting feeling informed and confident.

**deck-quarterly-review/**
Purpose: Generate a 16-slide quarterly strategy review presentation. More substantial than the monthly report — revisits the strategy and recommends adjustments. Structure: (1) Title, (2) Quarter in numbers — headline KPIs, (3) Progress vs. 90-day targets, (4) Platform-by-platform performance, (5) Audience growth and engagement trends, (6) Content performance analysis — what the data tells us, (7) Competitor snapshot — what changed in the competitive landscape, (8) Strategy assessment — what is working, what is not, (9) Recommended strategy adjustments, (10) New opportunities identified, (11) Proposed content pillars refresh (if needed), (12) Campaign recommendations for next quarter, (13) Budget performance and reallocation recommendations, (14) Q2 / Q3 / Q4 roadmap (depending on quarter), (15) Proposed next quarter priorities, (16) Questions and next steps.

**deck-campaign-proposal/**
Purpose: Generate a campaign proposal presentation deck for presenting a specific campaign idea to the client for approval. Structure: (1) Title and campaign name, (2) The opportunity — why now?, (3) Campaign objective and success metrics, (4) Target audience for this campaign, (5) Campaign concept — the big idea, (6) How it works — channel by channel execution plan, (7) Content examples — mock-ups described in words (not actual designs), (8) Timeline — pre-launch / launch / sustain / close, (9) What we need from you — client responsibilities, (10) Investment — budget breakdown, (11) Expected results — projected metrics, (12) Next steps and approval. Tone: persuasive and enthusiastic; this deck wins the campaign budget.

**deck-credentials/**
Purpose: Generate an 8-slide agency credentials/capabilities deck for pitching to prospective clients. Structure: (1) Cover — agency name and tagline, (2) Who we are — founder story + team, (3) What we do — services overview (not a full list — 3 core offerings, simply stated), (4) How we work — methodology in 3–4 steps, (5) Results we have delivered — 3 case study snapshots (challenge / approach / result / metric), (6) Who we work with — client types and industries (without naming clients if confidentiality is needed), (7) What working with us looks like — onboarding, communication, reporting, (8) Let us talk — CTA with contact details. Keep tone confident but not boastful; let the results speak.

**deck-annual-review/**
Purpose: Generate an 18-slide annual performance and strategy refresh presentation. Comprehensive end-of-year review used to renew retainers and set direction for the year ahead. Structure: (1) Title, (2) Year in numbers — 5 headline metrics, (3) Goals we set vs. results we achieved, (4) Platform-by-platform performance trends (12-month view), (5) Audience growth story, (6) Top 5 content pieces of the year — with learnings, (7) Brand voice evolution — how the brand sounds today vs. 12 months ago, (8) Campaigns — what ran and what worked, (9) Competitor landscape — how the market moved, (10) What we learned about your audience, (11) Channels to grow in Year 2, (12) Channels to reduce or exit, (13) Year 2 strategy statement, (14) Content pillar refresh, (15) Year 2 KPI targets, (16) Year 2 campaign calendar preview, (17) Investment recommendation for Year 2, (18) Thank you and next steps.

---

### Step 9: Meta/Analytical Skills

**meta-competitor-analysis/**
Purpose: Analyse 3–5 competitors' social media and digital marketing presence. Output: competitor comparison table (platforms used, follower counts, posting frequency, content style, average engagement rate estimate, paid ad activity visible via Meta Ad Library, strengths, weaknesses), gap analysis (where the client can win), and 5 strategic recommendations. Includes a note on where to find competitor data (Meta Ad Library, LinkedIn, TikTok search, Google search, SimilarWeb free tier).

**meta-content-audit/**
Purpose: Audit the client's existing content if they have a history. Output: content performance summary by platform (what performed above/below average), top-performing and worst-performing content types, content pillar coverage analysis (which pillars are over/under-represented), tone and consistency rating, and 5 priority improvements to make in the first 30 days. Includes an audit data collection template (what to record from each post).

**meta-reporting/**
Purpose: Generate a written monthly social media performance report (document version — separate from the deck). Sections: period summary, platform-by-platform KPI table (target vs. actual with traffic light ratings), top 3 posts with performance data and analysis, what worked / what did not / what to test, paid social performance (if applicable), and recommendations for next month. Professional, client-ready format the consultant can email between formal presentations.

**meta-roi-framework/**
Purpose: Calculate and present the ROI of the client's social media and digital marketing investment. Covers: Total Lifetime Value (TLV) calculation, Cost of Customer Acquisition (COCA) by channel, COCA:TLV ratio benchmarks (healthy = 3:1 minimum), contribution of social media to pipeline (attribution methodology for non-ecommerce businesses), break-even analysis for content investment, and a 12-month ROI projection table. Also includes talking points for the consultant to justify their retainer fee using these metrics. Based on Bodnar and Cohen (2012) ROI formula: (TLV − COCA) ÷ COCA.

**meta-content-repurposing/**
Purpose: Generate a content repurposing plan to maximise output from each piece of content created. Covers: the Content Factory model (one long-form piece → multiple short-form outputs), platform repurposing matrix (YouTube video → YouTube Short / TikTok / Instagram Reel / LinkedIn post / blog summary / WhatsApp broadcast / X thread), 10 worked examples showing one source content → 5+ platform outputs, and a weekly content repurposing workflow the social media manager can follow. Repurposing reduces content production cost by 60–70% — quantify this for the client.

---

### Step 10: Training Skills

**training-client-team/**
Purpose: Generate a social media training guide for the client's internal team (employees who will assist with content creation or community management). Covers: how the company's social media strategy works (plain-English summary), what each team member can and cannot post, how to take good photos/videos on a smartphone (practical tips for behind-the-scenes content), how to use scheduling tools (Buffer / Hootsuite — basic overview), the approval workflow for content, how to respond to customer messages, and how to report performance to the social media manager. Format: a printable training workbook (not a presentation — the consultant delivers this in a 2-hour workshop).

**training-diy-content/**
Purpose: Generate a DIY content creation guide for clients who want to manage some or all of their own content after the initial strategy engagement. Covers: how to use Canva for social media graphics (with specific template guidance), how to film and edit short videos on a smartphone (CapCut workflow), how to use the content calendar provided, how to write captions using the brand voice guide, when and how to boost posts (basic paid social for non-specialists), how to read platform analytics (what to look at, what it means), and when to call the consultant for support. Format: a friendly, jargon-free handbook the client keeps and references independently.

---

### Step 11: Utility Skills

**caption-writer/**
Purpose: Write social media captions for any platform from a brief. Input: platform, content type, topic, key message, CTA, tone. Output: 3 caption variations (short / medium / long), with hashtag suggestions for each. Apply platform-specific conventions (LinkedIn: no hashtag spam; Instagram: 5–10 relevant tags; TikTok: 3–5 plus trending; X: 1–2 only).

**hashtag-strategy/**
Purpose: Generate a complete hashtag strategy for a client. Output: 5 branded hashtags, 10 niche hashtags (industry + location specific), 10 community hashtags (broader audience discovery), 5 awareness/trending hashtags — all organised by platform with usage frequency guidance. Covers EA-specific hashtag communities (#UgandaTwitter, #MadeInUganda, #NairobiTwitter, #KenyaBusinesses, etc.) and warns against shadow-banned tags.

**content-ideas/**
Purpose: Generate 30 fresh content ideas for a client given their industry, target audience, and content pillars. Output: structured table with idea title, platform, content type, pillar assignment, and 2-sentence content brief for each. Can be run quarterly as a content bank refresh.

**email-copywriter/**
Purpose: Write email marketing copy — newsletters, promotional emails, welcome sequences, and reactivation emails. Input: email type, audience segment, key message, offer (if any), CTA. Output: subject line (3 options), preheader text, email body (formatted with headers for scanability), and CTA button text. Applies the principle that emails must earn the right to sell — value first, sell second.

**blog-post-writer/**
Purpose: Write a complete blog post from a content brief. Input: topic, target reader persona, search intent, key questions to answer, word count, CTA. Output: SEO-optimised title, meta description (155 characters), introduction (hook + promise), body with H2/H3 structure, conclusion, and CTA paragraph. Applies the Pyramid Principle for structure (answer first, evidence after). Blog posts must be practical and specific — not generic.

---

## Conventions for All SKILL.md Files

- YAML frontmatter: name and description only (no other fields)
- Description must include what the skill does AND when to invoke it — this is the primary trigger mechanism
- Body: under 500 lines, imperative language ("Ask for...", "Generate...", "Apply...")
- Reference files go in references/ subfolder; link them from SKILL.md with a note on when to read each
- Do not create README.md, CHANGELOG.md, or any auxiliary documentation files
- Every skill must include a "Required Input" section (what to ask before generating)
- Every skill must include a "Quality Criteria" section (5–8 bullets defining good output)
- For deck- skills: every slide entry must follow the format: Slide N — Title | Headline | Bullets | Speaker Notes | Visual Direction

---

## Skill Creation Process

For each skill, in order:
1. Create the skill directory
2. Write the SKILL.md with complete, production-ready content (not placeholders)
3. If the skill needs reference material, create references/ files and link them from SKILL.md
4. After completing all skills, create memory/MEMORY.md as a concise project index

Use the skill-writing conventions from C:\Users\Peter\.claude\skills\skill-writing\SKILL.md throughout.

Start by creating CLAUDE.md, then build skills group by group in the order above. Announce which skill you are creating before starting each one.

The total skill count is approximately 40 skills. This is a large session — work systematically through each group before moving to the next.
```

---

## Key Deliverable Categories (Summary)

| Category | Skills | What They Produce |
|---|---|---|
| **Business Development** | 4 | Credentials, proposals, pricing, case studies |
| **Client Onboarding** | 4 | Brief, platform audit, personas, brand voice |
| **Strategy** | 5 | Social strategy, digital strategy, email, influencer, campaign |
| **Planning** | 4 | Content pillars, 90-day calendar, blog plan, campaign brief |
| **Platform Plans** | 7 | Facebook, Instagram, LinkedIn, WhatsApp, TikTok, YouTube, X |
| **Execution Playbooks** | 4 | Community management, crisis comms, content production, policy |
| **Presentation Decks** | 6 | Strategy, monthly report, quarterly review, campaign, credentials, annual |
| **Meta/Analytical** | 5 | Competitor analysis, content audit, reporting, ROI, repurposing |
| **Training** | 2 | Client team training, DIY content guide |
| **Utilities** | 5 | Captions, hashtags, content ideas, email copy, blog writing |
| **Total** | **~46** | Full consultancy documentation suite |

---

## Notes for Adapting This Prompt

- **Country context:** Defaults to Uganda/EA. To change, add "Default country context is Kenya — use KES, reference KRA, CBK, KEPSA, and M-Pesa penetration 80%."
- **Paid ads scope:** The current scope excludes paid ad campaign management. To add it, create a `meta-paid-social/` skill covering Facebook Ads Manager, Google Ads, and TikTok Ads campaign planning. Add it as a second-session expansion.
- **Integration with business-plan-skills:** The `05-social-media-strategy` and `06-digital-marketing-strategy` outputs complement the `digital-marketing-strategy` and `07-marketing-sales-strategy` skills in business-plan-skills. Use both suites together when a business plan client also needs a detailed social media execution plan.
- **Deck format:** All deck- skills output markdown outlines, not .pptx files. If you want actual file generation, a separate PowerPoint automation skill (using python-pptx) can be added in a later session.
