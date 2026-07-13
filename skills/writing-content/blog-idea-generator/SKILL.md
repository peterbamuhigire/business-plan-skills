---
name: blog-idea-generator
description: Use when the user wants blog topic ideas, editorial angles, or a content pipeline. Use content-writing for general copy and blog-writer for a complete article.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Blog Idea Generator

## Overview

Use this skill to generate a strong blog-topic pipeline grounded in the client's business, audience, and existing content. It is the ideation layer for website content programmes, not the article-writing layer.

## Use When

- Use when the user wants blog topic ideas, editorial angles, or a content pipeline.
- Use when populating or refreshing a topic backlog such as `topic-ideas.md`.
- Use when existing website content should inform what gets written next.

## Do Not Use When

- Do not use for writing the full article; hand off to the blog-writing workflow.
- Do not generate topics without checking for duplication against existing content.
- Do not produce generic SEO clichés unrelated to the client's expertise.


- Route to `content-writing` instead for general copy, or `blog-writer` for a complete article.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Blog Idea Generator brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Client website, services, audience, and positioning context
- Existing blog or content inventory
- Any language, SEO, or campaign priorities
- Constraints on tone, geography, or commercial focus

## Workflow

1. Read the available site and content context before ideating.
2. Identify the most relevant audience problems, search intents, and expertise angles.
3. Generate topic ideas using the most appropriate ideation methods.
4. Filter out duplicates, weak angles, and topics the client cannot credibly own.
5. Package the ideas with enough structure to support article drafting.
6. Flag gaps in source context that limit topic quality.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the ranked article idea register and that the decision concerns which ideas deserve a brief rather than duplicate current content.
- **Stop condition:** halt the affected conclusion if required evidence is missing (site audience, commercial goals, existing coverage, and credible source areas) or if the work could lead to this identified risk: producing search-shaped titles with no reader or evidence value.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Topics are specific, relevant, and commercially useful.
- Ideas align with the client's expertise and audience needs.
- The list balances search demand, brand authority, and variety.
- Each idea is developed enough to brief a writer.

## Anti-Patterns

- Generic “top 10 tips” ideas with no differentiation.
- Repeating existing articles under slightly different titles.
- Generating topics disconnected from the client's services or credibility.
- Prioritising volume over quality and relevance.
- Treating a generic blog idea generator template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to blog idea generator. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Blog Idea Generator deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A ranked or grouped list of blog ideas with usable briefs
- Notes on content gaps, duplicates, or strategic opportunities
- Any assumptions needing confirmation before writing begins


Generate 15-25 targeted blog post ideas, each presented as a 200-word hybrid summary with narrative brief + structured specs. The system adapts its ideation methods to the specific client and available information.

**Read `references/ideation-frameworks.md`** for the full 20-method library and selection logic.
**Read `references/content-formats.md`** for 20 content formats with structural templates.
**Read `sales-copywriting/references/headline-mastery.md`** for headline formulas and 4 U's scoring.

---

## Step 1: Gather Context

### Read client docs (mandatory)

Read every available file to build a complete picture:

1. `docs/en/company-profile.md` (and all enabled language versions)
2. `docs/en/services.md`  service offerings, target customers
3. `docs/en/pages.md`  existing website pages and content
4. `docs/sector-brief.md`  industry context (if present)
5. `docs/style-brief.md`  brand voice and tone
6. `blog-writer/references/topic-ideas.md`  existing topics (avoid duplicates)
7. `src/pages/en/blog/`  existing articles (avoid overlap)
8. All other `docs/en/` files  testimonials, FAQ, portfolio, about-story

Extract and note:
- What the business does (core services, products)
- Who they serve (audience segments, industries, company sizes)
- Where they operate (geographic focus, markets)
- What makes them different (competitive advantage, methodology)
- What expertise the author has (experience, credentials, stories)
- What problems customers face (pain points, challenges)
- What content already exists (published articles, covered topics)

### Guided interview (3-5 questions)

After reading docs, ask targeted questions to fill gaps. Ask one at a time. Skip questions already answered by docs.

**Core questions (ask what's missing):**

1. **Audience specifics**  "Who is your ideal reader? (Job title, company size, industry, location)"
2. **Top pain points**  "What are the top 3 problems your customers face that your business solves?"
3. **Content goals**  "What should readers DO after reading? (Contact you, book a demo, understand a concept?)"
4. **Competitor landscape**  "Name 2-3 competitors. What topics do they cover?"
5. **Unique knowledge**  "What do you know that competitors don't? What's your unfair advantage?"
6. **Customer questions**  "What questions do customers ask most before buying?"
7. **Content gaps**  "Topics you've wanted to write about but haven't?"
8. **Context/audience**  any additional context the user provides (specific themes, campaigns, seasonal needs)

If the user provides additional context (audience details, campaign goals, seasonal focus), incorporate it into the assessment.

---

## Step 2: Assess Available Information

Score each dimension to determine which ideation methods will work best:

| Dimension | Rich (3) | Moderate (2) | Sparse (1) |
|-----------|----------|--------------|------------|
| **Client docs** | Detailed company-profile, services, testimonials, stories | Basic company-profile and services | Minimal  just a business name and description |
| **Competitor visibility** | Named competitors with active blogs | Competitors named but blogs unknown | No competitor info |
| **Audience specificity** | Named segments with pain points | General audience description | Vague ("businesses") |
| **Industry dynamism** | Active news cycle, regulations, trends | Moderate change rate | Stable/static industry |
| **Existing content** | 5+ published articles to spin off | 1-4 articles | No existing content |
| **Customer interaction** | Direct customer questions available | Some FAQ data | No customer feedback |

---

## Step 3: Select Ideation Methods

Based on the assessment, select 5-7 methods from the 20-method library. **Always include Methods 1 and 2** as foundation.

### Selection Matrix

| Method | Best When | Min Score |
|--------|-----------|-----------|
| 1. Category Drilldown | Always |  (always include) |
| 2. Buyer Awareness Stages | Always |  (always include) |
| 3. Pain Point Mining | Client docs  2 or customer interaction  2 |  |
| 4. Competitor Gap Analysis | Competitor visibility  2 | Competitor 2+ |
| 5. Customer Question Mapping | Customer interaction  2 | Customer 2+ |
| 6. They Ask, You Answer | Customer interaction = 3 | Customer 3 |
| 7. Amazon/Review Mining | Product-based business | Client docs 2+ |
| 8. Spin-Off Posts | Existing content  2 | Content 2+ |
| 9. Media Mashup | Brand voice is informal/creative | Client docs 2+ |
| 10. Highlight Good/Bad | Industry has notable examples | Industry 2+ |
| 11. How-To/Tutorial Mining | Product/service has teachable processes | Client docs 2+ |
| 12. Success/Failure Stories | Client has real project stories | Client docs 3 |
| 13. Holiday/Event Mapping | Content calendar needs seasonal hooks | Any |
| 14. Newsjacking/Trends | Industry dynamism = 3 | Industry 3 |
| 15. Use Any Object | Need creative/lateral ideas | Any (creative fallback) |
| 16. Curated Roundups | Industry has notable resources | Industry 2+ |
| 17. Prediction Posts | Industry dynamism  2 | Industry 2+ |
| 18. Jargon/Glossary | Technical niche with newcomer audience | Audience 2+ |
| 19. Contrarian/Negative | Audience is sophisticated | Audience 3 |
| 20. Topic-Category Matrix | Need high volume quickly | Any (volume fallback) |

Announce: "Based on available information, I'm using methods: [list]. Here's why: [brief rationale]."

---

## Step 4: Generate Ideas

Run selected methods sequentially. Aim for 25-35 raw ideas, then filter to the best 15-25.

For each method, consult `references/ideation-frameworks.md` for detailed instructions and examples.

### Quality Filters

Remove any idea that fails:

| Filter | Test |
|--------|------|
| **High-value goal** | Does this help the reader make/save money, reduce risk, save time, or gain advantage? |
| **Unique angle** | Does this require knowledge that isn't commonly available? |
| **So-what test** | Would the target reader care enough to click? |
| **Longevity** | Will this still be relevant in 12 months? |
| **No overlap** | Not already published or in existing topic-ideas.md? |
| **Searchable** | Would someone type this into a search engine? |

### Tier Classification

| Tier | Purpose | Target Count |
|------|---------|-------------|
| **Tier 1: SEO drivers** | Attract organic traffic via long-tail keywords | 6-8 ideas |
| **Tier 2: Authority builders** | Establish expertise with deep guides and analysis | 5-7 ideas |
| **Tier 3: Thought leadership** | Build brand with opinions, predictions, stories | 4-5 ideas |

---

## Step 5: Create 200-Word Hybrid Summaries

For each approved idea, produce a summary in this exact format:

~~~markdown
### [Number]. [Working Title]

[3-4 sentence narrative brief: What this article is about, who it serves,
why it matters now, and the unique angle that makes it worth reading. This
paragraph should make someone want to write  and read  this article. It
captures the creative direction and emotional tone.]

- **Audience:** [specific reader segment  job title, industry, company size]
- **Buyer Stage:** [Awareness / Consideration / Decision]
- **Format:** [How-to / Case study / List / Opinion / Guide / Story / Comparison / Interview / Roundup / FAQ]
- **Angle:** [the specific twist that differentiates from competitors  1 sentence]
- **Key Points:**
  1. [what the article must cover  specific enough to outline from]
  2. [second key point]
  3. [third key point]
  4. [fourth key point  optional]
  5. [fifth key point  optional]
- **CTA Goal:** [what action the reader should take after reading]
- **SEO Keywords:** [primary keyword], [secondary keyword]
- **Tier:** [1: SEO driver / 2: Authority builder / 3: Thought leadership]
- **Est. Words:** [1,500-2,500]
~~~

### Summary Quality Rules

- The narrative must read like a creative brief  not a dry description
- Key points must be specific enough to outline section headings from
- Keywords must be realistic long-tail phrases someone would search
- The angle must be genuinely different from what a Google search would surface
- Every title must pass the 4 U's test (see `sales-copywriting/references/headline-mastery.md`): Useful, Unique, Urgent, Ultra-specific  score 3+ on at least 3 dimensions

---

## Step 6: Present and Refine

### Present to the User

Show ideas grouped by tier with full summaries. After presenting, ask:
- Which ideas excite you most?
- Any ideas to remove or modify?
- Any topics you expected but don't see?
- Any specific campaigns or seasonal needs to address?

Refine based on feedback. The user's input overrides the assessment.

---

## Step 7: Save Output

Save the final approved list to `blog-writer/references/topic-ideas.md`:

~~~markdown
# Blog Topic Ideas  [Client Name]

Generated: YYYY-MM-DD
Methods used: [list of methods applied]
Target audience: [summary]
Content categories: [list]

## Tier 1: SEO Drivers

### 1. [Title]
[Full 200-word hybrid summary as above]

## Tier 2: Authority Builders
...

## Tier 3: Thought Leadership
...

## Content Calendar Suggestion

| Month | Article 1 (Tier) | Article 2 (Tier) |
|-------|-------------------|-------------------|
| Month 1 | [title] (T1) | [title] (T2) |
...
~~~

If the file already exists, merge new ideas  don't overwrite existing topics. Mark previously written topics as `[PUBLISHED]`.

---

## Quality Checklist

Before finalising:

- [ ] At least 15 ideas across all 3 tiers
- [ ] Each idea has a complete 200-word hybrid summary
- [ ] No duplicate angles (each idea is distinct)
- [ ] At least 2 ideas per buyer awareness stage
- [ ] Ideas span at least 3 content categories
- [ ] Every title passes the 4 U's test (3+ dimensions at 3+)
- [ ] No overlap with existing published articles
- [ ] Mix of content formats (not all lists, not all how-tos)
- [ ] At least 3 ideas that showcase the author's unique expertise
- [ ] At least 2 ideas based on real customer questions (if data available)
- [ ] Content calendar covers at least 6 months at 2 articles/month
- [ ] All SEO keywords are realistic long-tail phrases
- [ ] Narrative briefs are compelling  they make you want to write the article

After writing, verify line count is under 500: wc -l blog-idea-generator/SKILL.md

---

## Business Plan Blog Ideas (Pre-Built Bank)

When generating blog posts about **business planning, entrepreneurship, management, or plan-writing**, first consult the pre-built idea bank before running the full ideation process:

**`references/book-derived-blog-ideas.md`**  106 original, book-sourced post ideas. Each idea includes: angle, target reader, hook sentence, source reference file, and recommended format. Derived from: Minto (Pyramid Principle), Rasiel (McKinsey Way), Damodaran (Valuation), Feld & Mendelson (Venture Deals), Agrawal et al. (Prediction Machines), Sinek (Start with Why), Miller (Building a StoryBrand), Gerber (Awakening the Entrepreneur Within  Fatal Assumption, impersonal dream, Four Dimensions, Golden Pyramid), Horowitz (Hard Thing About Hard Things  The Struggle, Peacetime/Wartime CEO, layoffs, people first, Ones and Twos), Hahn & Mangun (DIY Advertising  AIDA+Conviction hierarchy, direct mail, radio scripts, testing framework), Edwards & Douglas (Getting Business to Come to You  Marketing Pyramid, Referral Machine, Article Marketing Loop, niche positioning), Pinskey (101 Ways to Promote Yourself  picture business cards, radio guesting, press releases, self-promotion system), Ashley (Oxford Handbook of Commercial Correspondence  bank covering letters, Incoterms, complaints, payment methods, letters of credit, job offer letters), Fleisher & Bensoussan (Business and Competitive Analysis  Nine Forces, competitor profiling, win/loss analysis, benchmarking, war gaming, linchpin analysis), Cadle, Paul & Turner (Business Analysis Techniques  PESTLE vs Porter's Five Forces, SWOT/TOWS correctly used, McKinsey 7-S implementation check, swimlane process modelling, 72-tool analytical toolkit, CBA/NPV/payback compared), Hood (Words at Work  plain English, reversed triangle, report structure), Shiach (How to Write Essays  argument structure, paragraph formula, transitions), Geffner (Business English  Four Cs, parallelism, positive framing, expressions to avoid), and Rubie & Provost (How to Tell a Story  Provost Paragraph, high-concept hook, show vs tell, protagonist principle).

**When to use this bank:**
- Client is a business consultant, coach, accountant, or financial adviser
- Website covers entrepreneurship, business planning, funding, or strategy
- Content calendar needs authority-builder or thought-leadership pieces
- Audience is entrepreneurs, SME owners, or plan writers

**Each idea in the bank maps directly to a reference file**  so the blog writer can draw on deep, sourced content rather than generic advice. Reference the specific file listed in the "Draw from" field of each idea when writing the article.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Ranked article idea register decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to producing search-shaped titles with no reader or evidence value. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the ranked article idea register; writing idea briefs without publishing or scraping restricted sources is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If site audience, commercial goals, existing coverage, and credible source areas cannot be obtained, return a qualified ranked article idea register covering only the checks that remain supportable. Leave this decision unresolved: which ideas deserve a brief rather than duplicate current content. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which ideas deserve a brief rather than duplicate current content | Record the conclusion, source trail, owner, and review trigger in the ranked article idea register. | Risk of producing search-shaped titles with no reader or evidence value |
| Material evidence conflicts or remains uncertain | Check the tied ideas against existing coverage, reader questions, credible source depth, and commercial relevance before commissioning a brief. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: site audience, commercial goals, existing coverage, and credible source areas | Mark the decision on which ideas deserve a brief rather than duplicate current content `not assessed` in the ranked article idea register, and send it to the content strategist and site owner. | Otherwise, the work risks producing search-shaped titles with no reader or evidence value |

## Quality Standards


Accept the ranked article idea register only when evidence is sufficient for this decision: which ideas deserve a brief rather than duplicate current content. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of producing search-shaped titles with no reader or evidence value.

## Worked Example


A site already has three generic pricing articles. The idea register rejects near-duplicates and prioritises a sourced comparison that answers the target buyer's unresolved implementation question.

## References

- [`AGENTS.md`](../../../AGENTS.md) - repository routing, evidence, finance, and release rules.

<!-- dual-compat-end -->
