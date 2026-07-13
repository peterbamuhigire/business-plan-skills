---
name: blog-writer
description: Use when the user asks for a blog article, blog post, or publishable long-form website content. Use content-writing for general copy and blog-writer for a complete article.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Blog Writer  Article Generation Skill

## Overview

Use this skill to write and publish a full blog article workflow, including topic development, article drafting, on-page structure, and website integration where the project supports it. It owns the article artifact, not just the idea stage.

## Use When

- Use when the user asks for a blog article, blog post, or publishable long-form website content.
- Use when the task includes article structure, SEO, and website content integration.
- Use when an approved topic needs to become a finished article.

## Do Not Use When

- Do not use for raw idea generation without committing to article production.
- Do not write on topics the client cannot credibly support with expertise or examples.
- Do not prioritise SEO formulas over usefulness, voice, and trustworthiness.


- Route to `content-writing` instead for general copy, or `blog-writer` for a complete article.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Blog Writer brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Topic, audience, and commercial purpose of the article
- Client voice, service context, and existing site structure
- Language, SEO, and publishing requirements
- Any related assets, references, or prior article ideas

## Workflow

1. Read the client and site context before drafting.
2. Confirm the article angle, audience intent, and outcome the article should create.
3. Draft the article with strong structure, human voice, and useful specificity.
4. Apply `premium-commercial-writing` when the article must build authority, support a premium offer, handle objections, or perform in SEO/AI search.
5. Apply SEO, design, and publishing integration requirements where relevant.
6. Reconcile the article with brand voice, existing content, and site structure.
7. Flag unsupported claims, weak sourcing, or missing assets.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the publication-ready article package and that the decision concerns whether the article is accurate, distinctive, accessible, and ready for approval.
- **Stop condition:** halt the affected conclusion if required evidence is missing (approved brief, audience, verified sources, voice, media rights, and publish target) or if the work could lead to this identified risk: publishing unsupported claims or unlicensed media.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The article is useful, credible, and publishable.
- Voice feels human and specific to the client.
- SEO and site-integration needs are met without degrading readability.
- The article advances brand authority or demand generation.

## Anti-Patterns

- AI-sounding filler and recycled content patterns.
- Writing for search engines instead of readers.
- Publishing claims or case-study language the client cannot support.
- Copying a visual or editorial pattern that conflicts with the existing site.
- Treating a generic blog writer template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to blog writer. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Blog Writer deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A finished article draft and related publishing updates where applicable
- SEO and structural elements needed for publication
- Any assumptions, sourcing gaps, or media dependencies


Generate detailed, rich, educating, and captivating blog articles with authentic human voice, professional photography, and full SEO optimisation. Each article is a marketing asset  a demonstration of expertise that builds trust and attracts clients through organic search.

**Use the `frontend-design` plugin** throughout article page creation for distinctive, high-quality design.

## Before Writing

Read these files first:

1. `docs/en/company-profile.md` (and all enabled language versions)  author background, services, expertise
2. `src/pages/en/blog.astro`  current blog index structure (check for existing articles)
3. `src/pages/fr/blog.astro`  French blog index (if FR enabled)
4. `src/layouts/BaseLayout.astro`  layout props, structured data, design system
5. `src/styles/global.css`  current styles (add prose styles if missing)
6. Existing articles in `src/pages/{lang}/blog/`  count them to determine layout variation
7. `photo-bank/`  scan for article photos the user has uploaded
8. `src/assets/images/_catalog.json`  current image catalog

Read the reference files as needed during writing:

- `references/human-voice-standards.md`  **READ FIRST**  AI vocabulary/phrase/structure blacklists, human voice techniques, self-check (ensures content sounds 100% human)
- `references/writing-craft.md`  7-step process, sentence craft, paragraph structure, opening hooks, clarity, conciseness
- `references/content-strategy.md`  audience segments, buyer journey, SEO strategy, R.E.S.U.L.T.S. framework, blog creation checklist, 5-stage keyword mapping
- `seo/references/seo-content-writing.md`  keyword density rules, search intent types, featured snippets, voice search, on-page SEO checklist
- `sales-copywriting/references/headline-mastery.md`  Read for ALL blog headlines (10 formulas + 4 U's scoring)
- `sales-copywriting/references/resistance-and-objections.md`  Read for persuasive and opinion articles
- `references/reader-experience.md`  touchpoint mapping, reader types, quality gates, tone calibration, publishing rhythm
- `references/storytelling.md`  authentic stories, human touch, cultural markers
- `references/editorial-standards.md`  punctuation, capitalisation, numbers, grammar, British spelling
- `references/article-design.md`  image requirements, layout variations, design variety system
- `references/ideation-and-research.md`  ideation techniques, research methods, competitor analysis, headline generation
- `references/topic-ideas.md`  curated topic suggestions (project-specific, if present)
- `../premium-commercial-writing/references/seo-ai-search-visibility.md`  Read for authority articles, service-led blogs, answer-engine visibility, entity coverage, and search intent matching
- `../premium-commercial-writing/references/commercial-persuasion-patterns.md`  Read for premium-offer articles, persuasive opinion pieces, lead magnets, objections, CTAs, and differentiation angles
- `blog-idea-generator/references/content-formats.md`  20 content formats with structural templates (How-to, Case study, List, Opinion, Guide, Story, Comparison, etc.)
- `sales-copywriting/references/fascination-bullets.md`  21 bullet point templates for engaging list items and key takeaways
- `sales-copywriting/references/closing-and-guarantees.md`  closing templates for strong article conclusions and CTAs

---

## User Input

The user provides:

1. **Article title** (or topic idea)
2. **Brief summary** (2-5 sentences describing what the article should cover)
3. **Photos** uploaded to `photo-bank/` (at least 3: 1 featured/hero + 2 in-article)

From this simple prompt, generate the complete article pipeline below.

---

## Article Content Pipeline

Build the article from verified research through outline, draft, editorial challenge, source checks, and publishing preparation. Keep research notes and generated media provenance with the article record.

See [`references/article-production-workflow.md`](references/article-production-workflow.md) for the detailed procedure.

## English Voice

Write as the author would write for a business audience  the register of a senior professional writing a LinkedIn article or industry blog. Not academic, not casual.

**Read `references/storytelling.md`** for authentic human touch and cultural markers.

- **Simple and clear.** Short sentences. One idea per paragraph. No jargon without explanation.
- **British spelling.** organisation, programme, centre, colour, specialise.
- **Warm but professional.** Polite, measured, confident. Not stiff, not chatty.
- **First person where natural.** "In my experience" and "I have found"  the author has authority.
- **Practical focus.** Every article should leave the reader with something they can use.
- **Real examples.** Reference actual business contexts and projects from the company profile.

| Use | Avoid |
|-----|-------|
| practical, effective, significant | cutting-edge, game-changing, revolutionary |
| I have found that | It is widely acknowledged that |
| In our experience | Research conclusively demonstrates |
| This approach works because | This paradigm shift enables |
| I recommend | One might consider |
| This works | This can potentially |
| Two approaches matter | There are several approaches |

**Contraction calibration:** Use contractions sparingly for natural rhythm (don't, can't, it's  2-4 per 500 words). Zero contractions sounds like AI or academia. Too many sounds casual.

**Commit, don't hedge:** Say what you think. "This is the best approach for SMEs" not "This could arguably be considered a viable approach." Readers trust writers who commit.

**Read `references/editorial-standards.md`** for punctuation, capitalisation, numbers, and grammar rules.

---

## French Voice

Write as a bilingual professional would for francophone African business readers  Dakar boardrooms and Abidjan tech meetups, not Parisian literary prose.

- **Formal but accessible.** Vous throughout. Professional register. Not stiff or bureaucratic.
- **Concrete vocabulary.** "entreprise" not "firme", "mettre en place" not "implementer", "formation" not "enseignement".
- **No anglicisms where French words exist.** Say "logiciel" not "software", "numerique" not "digital", "reseau" not "network". Technical terms (ERP, API, SaaS) stay in English.
- **Accents mandatory.** Every e, e, e, c, a, u must be correct. Gender agreement verified.

---

## SEO Requirements (Every Article)

### On-Page SEO Checklist

1. **Title tag**  `{Article Title}  {Author Name}` (under 60 chars). Must contain primary keyword. Don't write cute-only headlines  combine creative hook with search-practical keywords: "The Three-Hour Problem: Fixing Slow Reconciliation in Multi-Branch Retail". See `references/writing-craft.md` headline rules.
2. **Meta description**  under 155 chars. Must include primary keyword + geographic location.
3. **URL slug**  lowercase, hyphenated, keyword-rich: `/en/blog/erp-implementation-mistakes/`
4. **Heading hierarchy**  one h1 (article title), 4-7 h2s (main sections), h3s for subsections.
5. **Keyword placement:**
   - Primary keyword in the title (h1)
   - Primary keyword in the first 100 words
   - Primary keyword in at least one h2
   - Primary keyword in the conclusion
   - Secondary keywords distributed naturally through body text
   - **Never keyword-stuff.** Every instance must read naturally.
6. **Alt text**  every image has descriptive alt text. Include the primary keyword in the featured image alt.
7. **Internal links**  at least 3 per article: one to a service page, one to about/portfolio, one to contact.
8. **External links**  link to authoritative sources when citing facts or data (opens in new tab).

### Structured Data (Article JSON-LD)

Every article page must include:

~~~json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://site.com/en/about/"
  },
  "datePublished": "2026-03-01",
  "dateModified": "2026-03-01",
  "publisher": {
    "@type": "Organization",
    "name": "Company Name",
    "url": "https://site.com"
  },
  "description": "Meta description",
  "image": "https://site.com/path/to/featured-image.jpg",
  "inLanguage": "en-GB",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://site.com/en/blog/article-slug/"
  }
}
~~~

### Technical SEO

- **Canonical URL**  automatic from BaseLayout
- **Hreflang**  links between all language versions (automatic from BaseLayout)
- **Open Graph**  title, description, featured image via `ogImage={heroImg.src}` prop on BaseLayout (each article uses its own featured image, not the default site OG image)
- **Sitemap**  remove `noindex` after first real article so blog pages are indexed
- **Page speed**  all images optimised via Astro `<Image>`, lazy loading on in-article images

### Keyword Research Per Article

Every article targets at least one keyword cluster. Research what the target audience searches for:

- Use the primary service terms from the company profile
- Append geographic modifiers (city, country, region)
- Prefer long-tail phrases (higher intent, less competition)
- Include the primary keyword and 2-3 secondary keywords naturally

---

## Article Quality Standards

| Element | Standard |
|---------|----------|
| Word count | 1,500-2,500 words (EN) / 1,800-3,000 words (FR) |
| Paragraphs | 2-4 sentences each, max 5. One idea per paragraph. |
| Headings | h2 for main sections (4-7 per article), h3 for subsections |
| Lists | Use where content is naturally enumerable (max 9 items per list) |
| Images | 1 featured + 2-4 in-article (at least 1 landscape + 1 portrait) |
| Stories | At least 1 concrete story from the author's experience |
| Internal links | At least 3 (service, about/portfolio, contact) |
| CTA | Natural call to action in the conclusion |
| Read time | Calculate at 200 words/min (EN) or 180 words/min (FR) |

---

## Publishing Checklist

### Quality Gates (from `references/reader-experience.md`)
- [ ] **8-Second Test**  title, hero image, and first paragraph make you want to keep reading
- [ ] **Scanner Test**  headings, bold text, and first sentence of each section convey the key points
- [ ] **So-What Test**  every major claim is followed by what the reader can do with it
- [ ] **Ambiguity Test**  no word could mean two things to a non-native English speaker
- [ ] **Touchpoint Test**  every transition feels natural and the conclusion has a clear "what's next"

### Content Quality
- [ ] Article is detailed, educating, and provides genuine value
- [ ] At least one authentic story with specific details (places, outcomes)
- [ ] Concrete language throughout  no vague abstractions
- [ ] Active voice in 90%+ of sentences
- [ ] Opening hook captures attention (not a definition or generic statement)
- [ ] Conclusion has a clear, natural CTA
- [ ] No filler phrases (in order to, due to the fact that, it is important to note)
- [ ] No weak modifiers (really, very, quite, basically, actually)
- [ ] Every paragraph connects to the previous one with a logical bridge

### Human Voice (from `references/human-voice-standards.md`)
- [ ] Zero Tier 1 AI blacklist words (delve, tapestry, landscape, leverage, realm, navigate, foster, etc.)
- [ ] Zero banned AI phrases ("In today's...", "It's important to note...", "Game-changer", etc.)
- [ ] Burstiness present  3+ short sentences (<8 words) per 500-word section
- [ ] At least 3 clear opinions the author stands behind
- [ ] Paragraph lengths vary (1, 2, 3, 4 sentences  not all the same)
- [ ] Max 2 em dashes in the entire article
- [ ] No "Furthermore/Moreover/Additionally" as paragraph openers
- [ ] Stories contain at least one sensory or physical detail
- [ ] 2-4 contractions per 500 words (natural rhythm, not zero)

### Language
- [ ] English: British spelling, East African professional tone, warm but measured
- [ ] French: formal francophone African register, vous throughout, accents correct
- [ ] French article feels native  not a translation

### Images
- [ ] Featured image present, minimum 1200px wide, `loading="eager"`
- [ ] At least 2 in-article images (1 landscape + 1 portrait)
- [ ] All images have descriptive alt text
- [ ] All images use Astro `<Image>` component
- [ ] Images distributed through article body, not clustered

### Design
- [ ] Layout variation differs from the previous article
- [ ] Design matches article tone and website brand
- [ ] Mobile-responsive at 375px, 768px, 1280px
- [ ] Author bio section present
- [ ] `frontend-design` plugin used for design decisions

### SEO
- [ ] Title tag under 60 chars with primary keyword
- [ ] Meta description under 155 chars with keyword + location
- [ ] Primary keyword in first 100 words, one h2, and conclusion
- [ ] Article JSON-LD schema with all required fields including image (`heroImg.src`)
- [ ] OG image uses article's featured image via `ogImage={heroImg.src}` (not default site OG)
- [ ] Featured image is landscape orientation for optimal OG/social sharing display
- [ ] Internal links to at least 3 other pages
- [ ] Featured image alt text includes primary keyword
- [ ] Hreflang tags present

### Technical
- [ ] `npm run build` passes with no errors
- [ ] Blog index updated with new article card
- [ ] `noindex` removed from blog pages (if first real article)
- [ ] All images tracked in `_catalog.json`

## References

| File | When to Read |
|------|-------------|
| `references/writing-craft.md` | During outlining and writing  7-step process, lead types (9 techniques), article arc (nut 'graph, full circle), sentence craft, headline SEO formula, clarity, conciseness |
| `references/content-strategy.md` | During planning  audience segments, buyer journey, SEO strategy, pillar content, touchpoints |
| `references/reader-experience.md` | During planning and review  touchpoint mapping, reader types, quality gates, tone calibration |
| `references/storytelling.md` | During writing  authentic stories, cultural markers, the human touch |
| `references/editorial-standards.md` | During proofing  punctuation, capitalisation, numbers, grammar, British spelling |
| `references/article-design.md` | During page building  layout variations, image placement, design variety |
| `references/ideation-and-research.md` | During planning  ideation techniques (clustering, spin, 9 value-adding angles, W5 discovery), research methods (2X rule, evidence types), competitor analysis framework, headline generation |
| `references/topic-ideas.md` | When suggesting topics  curated list with keyword targets (project-specific, generated by blog-idea-generator skill) |
| `../premium-commercial-writing/references/seo-ai-search-visibility.md` | When an article must rank, answer search intent, earn AI-search citation, or build topical authority |
| `../premium-commercial-writing/references/commercial-persuasion-patterns.md` | When an article supports a premium offer, lead magnet, sales conversation, or objection-handling goal |

Cross-cutting skills that apply throughout:
- `language-standards`  language and tone standards for all languages
- `east-african-english`  detailed English voice guide (if present in project)
- `premium-commercial-writing`  commercial authority, premium positioning, proof, CTAs, and SEO/AI-search visibility
- `brand-alignment`  visual and messaging consistency with the overall website brand
- `seo`  multi-language SEO, hreflang, language-specific sitemaps (ensures articles are SEO-ready)
- `sales-copywriting`  headline formulas, fascination bullets, closing techniques (always active for all articles)

---

## Blog Index Page Structure

The blog index page (`/en/blog/`, `/fr/blog/`) is one of the most visited pages. Don't just show a grid of latest posts. Structure it for discovery:

1. **Blog focus statement** (1-2 sentences at the top)  tell readers what you blog about
2. **Featured posts row**  2-3 hand-picked posts (most popular, posts with lead magnets)
3. **Newsletter signup**  prominently placed for visitors impressed by your content
4. **Topic categories**  list several post categories so readers can jump to topics of interest
5. **Latest posts grid**  chronological listing below the curated sections

### Heading Substance Test

After writing a blog post, scroll through reading only the section headings. If a reader could learn everything from the headings alone, the article lacks substance  you've written "X obvious things about Y" formatted beautifully but without depth.

**Fix:** Don't just repeat what everyone else says. Add your own perspective, look at the topic from an unexpected angle, add a twist in the headings while keeping them clear, inject personality and humour.

### Blog Taxonomy Rules

If the site has blog categories and tags:
- All categories should contain approximately equal numbers of posts
- If one category is twice as large as the rest, split it into two
- Do not assign too many categories or tags to a single post
- Remove tags or categories used only once or twice
- Show categories early on the page (near the top), not hidden at the bottom in small grey text
- Each category and tag page should have a title and short description

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Publication-ready article package decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to publishing unsupported claims or unlicensed media. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the publication-ready article package; drafting files and previews; publication requires explicit approval is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If approved brief, audience, verified sources, voice, media rights, and publish target cannot be obtained, return a qualified publication-ready article package covering only the checks that remain supportable. Leave this decision unresolved: whether the article is accurate, distinctive, accessible, and ready for approval. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: whether the article is accurate, distinctive, accessible, and ready for approval | Record the conclusion, source trail, owner, and review trigger in the publication-ready article package. | Risk of publishing unsupported claims or unlicensed media |
| Material evidence conflicts or remains uncertain | Draft the disputed section from the verified source notes in two structures and retain the version that answers the reader question without unsupported claims. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: approved brief, audience, verified sources, voice, media rights, and publish target | Mark the decision on whether the article is accurate, distinctive, accessible, and ready for approval `not assessed` in the publication-ready article package, and send it to the editor and publishing owner. | Otherwise, the work risks publishing unsupported claims or unlicensed media |

## Quality Standards


Accept the publication-ready article package only when evidence is sufficient for this decision: whether the article is accurate, distinctive, accessible, and ready for approval. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of publishing unsupported claims or unlicensed media.

## Worked Example


A draft cites a market percentage with no traceable source. Remove or verify the figure, preserve the useful argument, record image rights, and return an unpublished review copy.

<!-- dual-compat-end -->
