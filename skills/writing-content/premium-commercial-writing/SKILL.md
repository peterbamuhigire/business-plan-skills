---
name: premium-commercial-writing
description: Use when the artifact must persuade a buyer, lender, investor, partner, board, grant committee, or premium client. Use content-writing for general copy and blog-writer for a complete article.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Premium Commercial Writing

## Overview

Use this skill as the premium writing layer above section-specific business-plan, marketing, blog, proposal, and document skills. It upgrades the commercial presentation of sound thinking: clearer positioning, stronger proof, better persuasion, better search visibility, and a more expensive-feeling reader experience.

## Use When

- Use when the artifact must persuade a buyer, lender, investor, partner, board, grant committee, or premium client.
- Use when a plan, proposal, article, sales page, website page, pitch narrative, or executive summary needs sharper commercial language.
- Use when copy must show differentiation, authority, proof, and next-step logic without sounding generic or AI-written.
- Use when content must be discoverable through SEO, featured snippets, or AI-search answer engines.
- Use alongside `writing-quality`, `content-writing`, `blog-writer`, `executive-summary`, `marketing-sales-strategy`, and `plan-assembly` when the work is client-facing or high-stakes.

## Do Not Use When

- Do not use to make weak strategy, poor economics, or unsupported claims sound premium.
- Do not invent market evidence, testimonials, traction, guarantees, credentials, or urgency.
- Do not add hype, luxury language, or aggressive sales pressure where the audience expects evidence and restraint.
- Do not copy protected source text, distinctive examples, long paraphrases, or quotes from books or third-party content.


- Route to `content-writing` instead for general copy, or `blog-writer` for a complete article.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Premium Commercial Writing brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Artifact type: plan section, full document, blog, website page, landing page, sales copy, proposal, or investor narrative.
- Reader and decision context: buyer, investor, lender, grant committee, board, executive, or search visitor.
- Offer, claim, proof, constraints, tone, and required next action.
- Existing facts, numbers, examples, brand language, and any SEO or AI-search target topics.

## Workflow

1. Confirm the reader's decision: what they must understand, believe, trust, and do next.
2. Identify the commercial promise, differentiated angle, proof assets, objections, and conversion or decision path.
3. Select the right reference file:
   - Use `references/premium-writing-quality-gate.md` for final review across any artifact.
   - Use `references/commercial-persuasion-patterns.md` for positioning, offer, proof, objections, CTAs, and premium sales copy.
   - Use `references/seo-ai-search-visibility.md` for blogs, website pages, thought leadership, and explainers.
   - Use `references/document-investor-polish.md` for business plans, executive summaries, proposals, funder packs, and investor-facing copy.
4. Rewrite the structure before polishing sentences if the argument, offer, or evidence sequence is weak.
5. Upgrade language for clarity, authority, specificity, reader relevance, and scanability.
6. Add proof, qualification, risk handling, and next-step logic where supported by the facts.
7. Run the quality gate and flag any remaining evidence, positioning, or credibility gaps.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the premium commercial revision and that the decision concerns which claims and sequence make the case persuasive without hype.
- **Stop condition:** halt the affected conclusion if required evidence is missing (reader decision, offer, proof, objections, tone, and next action) or if the work could lead to this identified risk: making weak economics sound premium through unsupported language.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The reader can state the core value, evidence, risk control, and next step without rereading.
- The writing feels specific to this business, customer, market, and decision context.
- Premium language is earned by proof, service design, positioning, economics, and reader benefit.
- SEO and AI-search elements improve discoverability without keyword stuffing or generic content.
- The final artifact sounds like a professional commercial writer and business strategist worked on it.

## Anti-Patterns

- Polished vagueness: confident prose with no numbers, named customer, channel, evidence, or mechanism.
- Premium theatre: luxury adjectives, exclusivity, and status cues without product or service substance.
- Feature dumping: long lists of what the business offers without benefits, outcomes, proof, or buyer context.
- Search filler: headings written for keywords but not for reader usefulness or answer quality.
- Over-persuasion: urgency, scarcity, guarantees, or objection handling that the business cannot honour.
- AI voice: generic openings, abstract nouns, uniform rhythm, and safe but empty claims.


- Applying the wrong neighbouring route to premium commercial writing. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Premium Commercial Writing deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Premium-ready draft or revised copy.
- Headline, lede, positioning, proof, CTA, and structure improvements.
- SEO or AI-search improvements where relevant.
- Notes on unsupported claims, missing proof, weak differentiation, or premium-credibility gaps.

## References

- `references/premium-writing-quality-gate.md` - final review checklist for premium commercial writing across plans, documents, blogs, proposals, and copy.
- `references/commercial-persuasion-patterns.md` - reader-first persuasion, differentiation, proof, objections, offer framing, CTAs, and premium tone.
- `references/seo-ai-search-visibility.md` - SEO and AI-search standards for answerable, entity-rich, useful, search-ready content.
- `references/document-investor-polish.md` - business-plan, proposal, executive-summary, and investor-document writing standards.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Premium commercial revision decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to making weak economics sound premium through unsupported language. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the premium commercial revision; revising authorised copy while preserving source claims is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If reader decision, offer, proof, objections, tone, and next action cannot be obtained, return a qualified premium commercial revision covering only the checks that remain supportable. Leave this decision unresolved: which claims and sequence make the case persuasive without hype. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which claims and sequence make the case persuasive without hype | Record the conclusion, source trail, owner, and review trigger in the premium commercial revision. | Risk of making weak economics sound premium through unsupported language |
| Material evidence conflicts or remains uncertain | Compare the persuasive revision with the evidence-led original and keep only changes that sharpen the decision without enlarging the claim. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: reader decision, offer, proof, objections, tone, and next action | Mark the decision on which claims and sequence make the case persuasive without hype `not assessed` in the premium commercial revision, and send it to the commercial editor and document owner. | Otherwise, the work risks making weak economics sound premium through unsupported language |

## Quality Standards


Accept the premium commercial revision only when evidence is sufficient for this decision: which claims and sequence make the case persuasive without hype. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of making weak economics sound premium through unsupported language.

## Worked Example


An investor summary calls the company a market leader without evidence. Replace the status claim with verified traction and operating proof, sharpen the funding consequence, and keep the tone restrained.

<!-- dual-compat-end -->
