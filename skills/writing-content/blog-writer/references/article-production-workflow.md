# Article Content Pipeline

Parent skill: [`../SKILL.md`](../SKILL.md) (`blog-writer`).

### Step 0: Read Idea Summary (if available)

If `references/topic-ideas.md` exists and contains a summary for this article's topic:

1. Read the full 200-word hybrid summary for this topic
2. Extract and use as planning inputs:
   - **Audience**  target reader segment
   - **Buyer Stage**  awareness, consideration, or decision
   - **Format**  content format (how-to, case study, list, etc.)  read `blog-idea-generator/references/content-formats.md` for the structural template
   - **Angle**  the specific twist that differentiates this article
   - **Key Points**  section headings or core coverage areas
   - **CTA Goal**  what action the reader should take
   - **SEO Keywords**  primary and secondary targets
   - **Tier**  SEO driver, authority builder, or thought leadership
3. The idea summary is a starting point, not a straitjacket  adapt based on research in Step 1

If no idea summary exists, proceed directly to Step 1.

### Step 1: Research and Plan

1. Read the company profile to understand the author's expertise and experience. **Build a voice profile** (see `references/human-voice-standards.md`  Voice DNA Extraction): analyse the author's sentence patterns, vocabulary, opinions, register from their docs. Extract 5-10 characteristic sentences as tone anchors.
2. Identify the target audience segment for this article (see `references/content-strategy.md`)
3. Identify the reader types this article must serve: Scanner, Deep Diver, Sceptic, Action-Taker (see `references/reader-experience.md`)
4. Determine which buyer journey stage the article targets: Awareness, Consideration, or Decision
5. Identify 2-3 target SEO keywords from the topic (see Keyword Strategy below)
6. Choose the content organisation pattern (see `references/writing-craft.md`)
7. Choose an opening hook technique (question, startling fact, story, current event, bold assertion, poster child, scene-setter, significant detail, profile lead  see `references/writing-craft.md`)
8. Map the 5 touchpoints: pre-touch (title/meta), first touch (hero/opening), core touch (body), last touch (conclusion/CTA), in-touch (related articles/newsletter)
9. Produce an outline with 5-8 section headings (h2s)
10. Identify which stories from the author's experience to include (see `references/storytelling.md`)
11. Present the outline to the user for approval before writing

### Step 2: Process Article Photos

1. Scan `photo-bank/` for photos the user uploaded for this article
2. Measure dimensions of each photo
3. Copy to `src/assets/images/` following the photo-manager pipeline
4. Assign roles: **featured** (hero), **landscape** (in-article), **portrait** (in-article)
5. Update `_catalog.json` with article photo entries
6. Minimum: 1 featured + 1 landscape + 1 portrait = 3 photos. Maximum: 1 featured + 4 in-article = 5 photos.
7. If fewer than 3 photos are available, note what is needed and proceed with available images

### Step 3: Write English Article

Save to `docs/en/blog/{slug}.md`:

```markdown
---
title: "Article Title in Title Case"
slug: "article-slug-here"
date: "YYYY-MM-DD"
author: "Author Name"
category: "Category Name"
description: "SEO meta description  under 155 characters, includes primary keyword and location."
keywords: ["primary keyword", "secondary keyword", "tertiary keyword"]
featured_image: "filename-of-hero-image.jpg"
images: ["landscape-image.jpg", "portrait-image.jpg"]
read_time: "X min read"
---

Article body here...
```

**Writing requirements** (detailed in `references/writing-craft.md`):

- **1,500-2,500 words**  detailed, rich, educational. Every word earns its place.
- **Opening hook**  first paragraph grabs attention. Never open with a definition or generic statement. Consider poster child, scene-setter, significant detail, or profile lead types (see `references/writing-craft.md`).
- **Nut 'graph**  if the opening uses a story or anecdote, follow it (paragraphs 2-4) with a grounding paragraph that states what the article is actually about. Without this, soft openings feel directionless.
- **Pain point formula**  demonstrate understanding of the reader's problem before offering solutions.
- **At least one story** from the author's real experience with specific details (places, outcomes, lessons).
- **Concrete language**  specific numbers, named places, real examples. No vague abstractions.
- **Active voice**  at least 90% of sentences. Passive voice only when the actor is unknown or unimportant.
- **Sentence variety**  average 15-20 words. Mix short (8-10) with medium (25-30). Never exceed 35.
- **One idea per paragraph**  2-4 sentences each. Topic sentence leads.
- **Scannable**  clear h2 headings, bulleted lists where enumerable, bold for key terms.
- **Internal links**  link to relevant service, portfolio, about, and contact pages.
- **Image placement markers**  indicate where in-article images should appear: `[IMAGE: landscape-image.jpg  caption text]`
- **Full circle ending**  reconnect the conclusion to the opening. If you opened with a poster child, bring them back. If you opened with a scene, return to it transformed. Readers feel closure and reward.
- **CTA conclusion**  end with a clear, natural call to action (not a sales pitch).
- **Clarity**  use "because" not "since", "although" not "while", "can" for ability, "might" for possibility. No ambiguous words for multilingual readers.
- **Conciseness**  cut filler ("in order to"  "to", "due to the fact that"  "because"). Delete weak modifiers (really, very, quite, basically).
- **Linking flow**  every paragraph connects to the previous one with a logical bridge or transition word.

**Human voice requirements** (from `references/human-voice-standards.md`):

- **Zero AI vocabulary**  never use Tier 1 blacklist words (delve, tapestry, landscape, leverage, navigate, foster, realm, etc.). Check every sentence.
- **Zero AI phrases**  never open with "In today's...", "Have you ever wondered...", "It's important to note...". See full blacklist.
- **Burstiness mandatory**  every 500-word section must contain 3+ sentences under 8 words and 1+ sentence over 25 words.
- **Take positions**  at least 3 clear opinions per article. "I recommend" not "One might consider".
- **Client language**  mine vocabulary from docs/ files and use the client's own words.
- **Strategic contractions**  2-4 per 500 words (don't, can't, it's). Never in headlines.
- **Sensory detail in stories**  what it looked like, felt like, sounded like. Not just what happened.
- **Write then cut**  draft 30% more than needed, then cut ruthlessly in revision.
- **Max 2 em dashes per article**. Vary paragraph lengths (1 sentence, then 4, then 2).

### Step 4: Write French Article

Save to `docs/fr/blog/{slug}.md` with identical frontmatter structure.

**This is adaptation, not translation.** The French article must:

- Restructure paragraphs for natural French flow
- Use francophone African examples (Dakar, Abidjan, Douala) where English uses anglophone ones
- Feel like it was written in French first
- Use formal register throughout (vous, never tu)
- Follow West African francophone business conventions (see voice guides below)
- **1,800-3,000 words**  French naturally expands 20-30% from English
- Accents mandatory on every character (e, e, e, c, a, u, o, i)

### Quality Gate: Verify Against Idea Summary

If this article was generated from an idea summary (Step 0), verify alignment before proceeding to design:

- [ ] **Audience match**  article addresses the specified reader segment
- [ ] **Format compliance**  article follows the structural template for the specified format
- [ ] **Key points covered**  all key points from the summary are addressed in the article
- [ ] **Angle delivered**  the unique angle is evident, not generic
- [ ] **SEO keywords placed**  primary keyword in title, first 100 words, at least one h2, and conclusion
- [ ] **CTA goal achieved**  conclusion drives the specified action
- [ ] **Tier alignment**  Tier 1 articles prioritise SEO; Tier 2 prioritise depth; Tier 3 prioritise voice

If any check fails, revise the article before proceeding.

### Step 5: Design and Build Astro Pages

**Invoke the `frontend-design` plugin** for article page design.

1. Count existing articles to determine which layout variation to use (cycle through A, B, C, D)
2. Select colour accent based on article category/tone
3. Create `src/pages/en/blog/{slug}.astro` and `src/pages/fr/blog/{slug}.astro`
4. Include: Article JSON-LD schema, featured image, in-article images, author bio, CTA
5. Pass the featured image as the OG image: `<BaseLayout ... ogImage={heroImg.src}>`  each article must use its own featured image for Open Graph, not the default site OG image
6. Use `heroImg.src` in the JSON-LD `image` field: `"image": \`\${siteUrl}\${heroImg.src}\``
7. The featured image must be landscape orientation (wider than tall) for optimal OG display
8. Add prose styles to `global.css` if not already present

See `references/article-design.md` for layout variations, image treatment, and design variety system.

### Step 6: Update Blog Index

Update `src/pages/en/blog.astro` and `src/pages/fr/blog.astro`:

- Add the new article card with featured image thumbnail, title, category, date, read time, excerpt
- If this is the **first real article**: remove "Coming Soon" cards and remove `noindex` meta tag
- Keep the newsletter section
- Order articles newest-first

### Step 7: SEO Verification

Verify every SEO requirement (see full SEO checklist below):

- [ ] Title tag under 60 chars with primary keyword
- [ ] Meta description under 155 chars with primary keyword + location
- [ ] Article JSON-LD schema (headline, author, datePublished, publisher, description, image)
- [ ] Primary keyword in first 100 words, at least one h2, and conclusion
- [ ] Internal links to service/portfolio/contact pages
- [ ] Featured image has descriptive alt text with keyword
- [ ] Canonical URL correct
- [ ] Hreflang links between EN and FR versions

### Step 8: Build and Verify

Run `npm run build` and confirm:
- No build errors
- Article pages render correctly in both languages
- All images load and are optimised
- Blog index shows the new article

---
