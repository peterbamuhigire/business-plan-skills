---
name: language-standards
description: Use when drafting or reviewing professional English, French, or Kiswahili content for African audiences and language-specific grammar, register, terminology, or localisation controls are required; use `east-african-english` for English-only country tone and `writing-quality` for persuasion.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Language Standards  Multi-Language Tone & Grammar

## Overview

Use this skill as the multilingual language-governance layer for the repository. It keeps English, French, and Kiswahili content professional, culturally appropriate, and internally consistent across translated or multi-language outputs.

## Use When

- Use when content is being created or reviewed across more than one supported language.
- Use when translation quality, tone consistency, or cultural fit matter.
- Use as a language overlay on top of another content skill.

## Do Not Use When

- Do not use as a substitute for core strategy, structure, or factual accuracy.
- Do not force identical phrasing across languages when natural usage differs.
- Do not let localisation drift into meaning changes.

## Required Inputs

- Source text or content brief
- Target language or set of languages
- Audience, country, and cultural context
- Any fixed terminology, brand language, or compliance phrasing

## Workflow

1. Identify the target language, audience, and purpose of the content.
2. Apply the relevant language-specific standards and tone rules.
3. Preserve meaning while adapting phrasing for natural local usage.
4. Keep terminology and brand cues consistent across languages.
5. Reconcile multilingual outputs with the source content and site structure.
6. Flag terms or nuances that require human confirmation.

## Quality Bar

- The language feels natural to its target audience.
- Meaning stays consistent across languages.
- Tone matches the brand and region.
- Terminology is controlled and repeatable.

## Anti-Patterns

- Word-for-word translation that sounds unnatural.
- Letting one language version drift strategically from the others.
- Mixing registers or regional variants unintentionally.
- Ignoring culture-specific connotations in business language.

## Outputs

- Language-standard-compliant content or edits across the supported languages
- Terminology and tone corrections
- Any localisation questions requiring follow-up



All website copy, headings, calls to action, descriptions, and microcopy must follow this style guide for their respective language. This is a cross-cutting standard applied throughout every content-writing step.

## Core Principles (All Languages)

1. **Clear and direct.** Sentences are straightforward, grammatically careful, logically structured.
2. **Formal and respectful.** Politeness is essential. Communication shows courtesy and humility.
3. **No excessive marketing language.** Avoid drama, exaggeration, slang.
4. **Professionally indirect.** Soften directives with courteous phrasing.
5. **Measured confidence.** Confident without arrogance.
6. **Culturally authentic.** Respect regional norms, preferences, sensitivities.

---

# ENGLISH (en)  British English, East African Professional Standard

Load `east-african-english` for the English spelling, dates, country register, courtesy, vocabulary, and CTA rules. This multilingual skill retains only cross-language decisions and the French and Kiswahili standards so the two entrypoints do not drift.

### Assertive Language (All Languages)

Hedging language communicates uncertainty. If you're not sure you're any good, how can prospects be? Replace weak phrasing with confident, assertive alternatives:

| Hedging (weak) | Assertive (strong) |
|---------------|-------------------|
| Feel free to reach out | Contact me / Get in touch |
| In case you're interested | Interested? Contact me |
| Perhaps we can work together | Let's work together |
| Maybe we're a good fit | Add a "Who is this for?" section |
| We might be able to help | We can help |
| It could potentially improve | It improves |

This applies across all three languages. In French: "N'hesitez pas a nous contacter" is acceptable (culturally standard), but avoid excessive hedging like "Il serait eventuellement possible de...". In Kiswahili: use direct invitations ("Wasiliana nasi" not "Labda unaweza kuwasiliana nasi").

### Cross-language anti-slop control

Apply `anti-ai-slop` while drafting and `ai-slop-audit` before release. Translate intent and evidence rather than banned-word lists mechanically; language-specific filler and condescension still require concrete correction.

---

# FRENCH (fr)  Francophone African Professional Standard

## Core Characteristics

1. **Formal francophone African French**  not Quebecois, not Belgian variants.
2. **Respectful and courteous**  professionalism with warmth.
3. **Standard French grammar and conventions**.
4. **Vous (formal)** throughout all professional communication  never "tu".
5. **Culturally appropriate** for Cote d'Ivoire, Cameroon, Senegal, DRC, Gabon.

## French Spelling and Grammar

Use standard French orthography:
- Accent marks required: e, e, e, e, a, u, c, ,
- Double-check diacritical marks (many African translators omit them)
- UTF-8 encoding mandatory

### Apostrophes in Astro JSX Templates (French, Swahili, all languages)

**CRITICAL:** Single-quoted JS strings inside Astro JSX expressions (`.astro` template section) CANNOT contain straight apostrophes (`'`). This breaks the build because the apostrophe terminates the string early.

**Rules for any text containing apostrophes (e.g. French `d'`, `l'`, `n'`, `qu'`; Swahili `ng'`):**
1. **Use double-quoted strings** for any JS string literal that contains an apostrophe: `"d'excellence"` not `'d\'excellence'`
2. **Never use `\u2019` escape sequences**  Astro's template compiler may not handle them correctly
3. **Never use backslash-escaped apostrophes** (`\'`) in JSX template expressions  they work in frontmatter JS but fail in template JSX
4. **HTML text content is fine**  apostrophes in regular HTML `<p>d'excellence</p>` work without escaping
5. For JSX expression strings that need both `"` and `'`, use template literals: `` `string with ' and "` ``

### Verb Conjugation
- Use **vous** for all formal communication (not tu)
- Example: "Veuillez remplir le formulaire" (not "Remplis le formulaire")
- Imperative form: "Veuillez" + infinitive for politeness

### Gender Agreement
All adjectives and past participles must agree with gender:
- "La page est completee" (feminine)
- "Le service est complete" (masculine)
- "Les pages sont completees" (feminine plural)

## French Dates and Numbers

- **Date format**: 17 fevrier 2026 (or 17 fevrier 2026)
- **Month names**: Lowercase (fevrier, not Fevrier)
- **Numbers**: Use space or period for thousands: 1 000 or 1.000 (not 1,000)
- **Decimal separator**: Comma (not period): 3,14 (not 3.14)
- **Currency**: Franc CFA (FCFA), Euro (), or specified in design-tokens.md

## Formal Registers and Politeness

### Standard Openings
- Madame, Monsieur,
- Chere Madame, Cher Monsieur,
- Greetings,

### Standard Closings
- Cordialement, (warm, professional)
- Respectueusement, (respectful)
- Avec mes meilleures salutations,
- Veuillez agreer l'expression de nos salutations distinguees.

### Courtesy Phrases (French)

- Nous vous prions de...
- Veuillez... (imperative form with "vous")
- Merci de votre attention.
- Nous apprecions votre partenariat.
- N'hesitez pas a nous contacter.
- Nous vous remercions de votre soutien continu.
- Nous attendons avec interet votre reponse.
- Si vous avez besoin de precisions supplementaires, veuillez nous contacter.

## French Vocabulary Standards

### Preferred Professional Terms
- Faciliter, mettre en uvre, entreprendre, coordonner
- Engager, soutenir, ameliorer, examiner, confirmer
- Conseiller, informer, communiquer
- Significatif, important, strategique, benefique, precieux

### Words to Avoid (Marketing Hype)

| Avoid | Use Instead |
|-------|-------------|
| revolutionnaire | innovant |
| "game-changing" | strategique |
| incroyable | remarquable |
| genial | excellent |
| dingue | etonnant |
| Liberez le pouvoir | Activez la capacite |

### Francophone African Terminology

Use terms understood across francophone Africa (not Canada-specific, not France-specific):
- Budget (not "subvention")
- Entreprise (company, not "compagnie")
- Personnel (staff, not "employes" alone)
- Client (customer/client, standard everywhere)
- Formation (training, widely used)

## French CTAs and Button Text

| English | French (Formal) |
|---------|-----------------|
| Sign Up | S'inscrire |
| Register | Creer un compte |
| Contact Us | Nous contacter |
| Learn More | En savoir plus |
| Submit | Soumettre |
| Download | Telecharger |
| Place Your Order | Passer votre commande |
| Get Started | Commencer maintenant |

## French-Specific Considerations

### In-Country Reviewer Required
All French content must be reviewed by a native francophone speaker from the target market (Cote d'Ivoire, Cameroon, Senegal, DRC, Gabon). Send for review before publishing.

### Text Expansion
French is typically 2040% longer than English. Design for 1.3x expansion:
- Buttons must accommodate longer labels
- Navigation items must wrap gracefully
- Form labels must not overlap fields

### Regional Variations
Avoid country-specific terms unless relevant:
- Use neutral francophone African vocabulary
- Avoid France-centric references
- Avoid Canadian (Quebecois) terminology

---

# KISWAHILI (sw)  East African Standard

## Core Characteristics

1. **Standard East African Kiswahili**  not regional dialects (Mombasa, Zanzibar variants).
2. **Formal/respectful register** throughout professional communication.
3. **Humble and relationship-focused**  Swahili culture emphasizes harmony.
4. **UTF-8 encoding** for proper character rendering.
5. **Simple sentence structure**  Kiswahili clarity values straightforward expression.

## Kiswahili Grammar and Structure

### Standard Kiswahili Conventions
- **Subject prefixes**: Proper noun classes (m-/ba, ki-/vi, n-, li-)
- **Verb conjugation**: Tense markers (-li-, -na-, -ta-, -ki-, -a)
- **Adjective agreement**: Must agree with noun class
- **No gender distinction** in pronouns (yeye = he/she)

### Formal Register (Habari Rasmi)

Use formal register in all professional communication:
- Avoid slang (sheng, Nairobi street language)
- Use full words (hakuna = do not have, not "hakuna matata")
- Respectful pronouns and address forms

### Tense Selection
- **Present habitual**: -na- (Anataka = He/she wants)
- **Near future**: -ta- (Atakuja = He/she will come)
- **Past completed**: -li- (Alifika = He/she arrived)
- **Conditional**: -ki-, -ngali (Akija = if he/she comes)

## Kiswahili Dates and Numbers

- **Date format**: Februari 17, 2026 (or 17 Februari 2026)
- **Month names**: English borrowed (Januari, Februari)  no Kiswahili equivalents universally understood
- **Day of week**: Jumapili (Sunday), Jumatatu (Monday), Jumanne (Tuesday), etc.
- **Numbers**: Use spaces for thousands: 1 000 (not 1,000)
- **Currency**: Shilingi (Sh, KES for Kenya), or specified in design-tokens.md

## Kiswahili Courtesy and Formality

### Standard Openings (Business)
- Habari yako? (How are you? formal)
- Tunataka kuwashukuru...  (We want to thank you...)
- Tunakuomba... (We kindly request...)

### Respectful Phrases (Kiswahili)

- **Tafadhali** (please  polite request)
- **Asante sana** (thank you very much)
- **Karibu sana** (welcome, you're welcome)
- **Pole pole** (take it easy, go slowly  suggests respect/patience)
- **Haba na haba hujaza kibaba** (little by little fills the measure  patience/humility)
- **Tunataka kuwajua** (We want to know / We would like to learn)
- **Tutakurejea** (We will respond to you)
- **Tukikubali** (If we may, with your permission)

### Closings
- **Kwa heshima** (with respect)
- **Wakati mwingine** (another time / we hope to hear from you)
- **Tunatumaini kuongea nayo upya** (We hope to speak with you again)

## Kiswahili Vocabulary Standards

### Preferred Professional Terms
- **Kusimamia** (to manage, oversee)
- **Kutekeleza** (to implement, execute)
- **Kushiriki** (to participate, engage)
- **Kusaada** (to help, support)
- **Kuboresha** (to improve, enhance)
- **Kupatiana** (to agree, coordinate)
- **Kuhakiki** (to verify, confirm)
- **Kuarifu** (to inform, notify)
- **Kujifunza** (to learn)
- **Muhimu** (important, significant)
- **Faida** (benefit, advantage)
- **Lengo** (goal, objective)

### Words to Avoid (Too Colloquial)
- Slang/sheng  use formal Kiswahili
- Hyperbolic marketing words
- English insertions without Kiswahili alternative available

## Kiswahili CTAs and Button Text

| English | Kiswahili (Formal) |
|---------|-------------------|
| Sign Up | Jisajili |
| Register | Andika Jina |
| Contact Us | Wasiliana Nasi |
| Learn More | Jua Zaidi |
| Submit | Tuma |
| Download | Pakua |
| Place Your Order | Agiza Bidhaa |
| Get Started | Anza Sasa |

## Kiswahili-Specific Considerations

### In-Country Reviewer Required
All Kiswahili content must be reviewed by a native Kiswahili speaker from East Africa (Kenya, Tanzania, or Uganda). Regional variants exist; ensure reviewer is from target market.

### Text Expansion
Kiswahili is typically 1030% longer than English. Design for 1.2x expansion:
- Buttons must flex for longer labels
- Navigation items must wrap gracefully
- Form labels must have clear spacing

### No Dialects
- Use standard East African Kiswahili
- Avoid Mombasa Swahili (maChinwali features)
- Avoid Zanzibari Swahili (historical variants)
- Avoid regional slang or sheng (Nairobi street language)

### Relationships and Harmony
Kiswahili communication culture emphasizes relationships:
- Lead with greetings and acknowledgment
- Use plural forms to show respect (sisi = we, kuambia mtu = speak to a person)
- Avoid direct criticism or bluntness
- Always acknowledge the relationship before asking for action

---

# When This Skill Applies

This skill is **cross-cutting**  it applies throughout all content generation:

- **All visible website text**: headings, body copy, service descriptions, about pages, CTAs
- **Meta descriptions and SEO text**
- **Alt text for images**: clear, descriptive, respectful, in target language
- **Error messages and form labels**: polite, never terse
- **Email templates and contact responses**
- **Microcopy**: tooltips, helper text, notifications

## Integration with Other Skills

- **i18n**: Determines which language versions are built
- **page-builder**: Applies language standards when creating content
- **seo**: Uses language standards for meta tags, titles, descriptions
- **sector-strategies**: Industry-specific tone within language standards
- **design-system**: Visualizes language standards in typography and layout

---

# Enforcement Checkpoints

Before publishing any page, verify:

- [ ] **English pages**: British spelling, East African tone, no marketing hype
- [ ] **French pages**: Formal French, vous throughout, francophone African vocabulary, reviewed by francophone
- [ ] **Kiswahili pages**: Standard Kiswahili, formal register, no slang, reviewed by East African native speaker
- [ ] **All pages**: No truncation or text overflow in any language
- [ ] **All pages**: Grammatically correct, properly punctuated, culturally appropriate
- [ ] **All pages**: CTAs use respectful, inviting language (not aggressive)

## Language-Specific Reviewers

Before publishing in any language, assign review:

- **English**: East African professional (optional native review; standards in this guide)
- **French**: Native francophone speaker from Cote d'Ivoire, Cameroon, Senegal, DRC, or Gabon
- **Kiswahili**: Native Kiswahili speaker from Kenya, Tanzania, or Uganda

All translations reviewed by in-country professionals before publishing.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Source text or brief, audience, purpose, language, country, and required action | Requester and owning content skill | Required | Ask for the missing language or purpose; do not guess |
| Approved terminology, brand voice, names, facts, and previous translations | Client glossary, translation memory, country context, and verified sources | Conditional | Create a terminology query list and preserve source terms |
| Legal, financial, medical, technical, or regulated wording | Subject-matter owner and current doctrine | Conditional | Keep it provisional until expert review |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| English, French, or Kiswahili draft or review | Intended reader and owning workflow | Meaning, register, grammar, terminology, localisation, and action are consistent |
| Terminology and localisation record | Author, translator, in-country reviewer, and approver | Material choices, unresolved terms, country variants, and expert-review needs are visible |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Bilingual or source-target quality check | Issue table or reviewed segment list | Checks completeness, meaning, names, numbers, dates, terminology, register, and omissions |
| Reviewer status | Named language, country, and subject-review record | Unreviewed translations are not described as native, certified, or publication-ready |

## Capability Contract

Review defaults to read-only. Edit only when authorised. Do not change facts, commitments, legal or financial effect, quoted speech, or approved claims in translation. Publishing, certified translation, and external messaging require explicit authority and an appropriate in-country professional reviewer.

## Degraded Mode

If a native reviewer, country context, terminology source, or source meaning is unavailable, return the narrowest qualified draft and query list. Mark affected segments `not assessed`; never claim native or certified quality from automated review alone.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| English-only East African tone is needed | Route to `east-african-english` | Duplicate and conflicting rules |
| French or Kiswahili text is reader-facing | Draft under this skill and require in-country review | False localisation confidence |
| Literal translation sounds unnatural but meaning is clear | Use an equivalent local construction and log the choice | Translationese |
| Regulated term is uncertain | Preserve source, flag it, and obtain expert approval | Changed legal or financial effect |

## Workflow

1. Confirm source, target language, country, audience, purpose, channel, voice, and approval route.
2. Extract protected facts, names, numbers, citations, terminology, and non-translatable elements.
3. Select the appropriate register and glossary; stop where source meaning or a regulated term is unresolved.
4. Draft for meaning and natural syntax, then check completeness segment by segment.
5. Verify names, figures, dates, quotations, links, legal and financial meaning, and calls to action.
6. Run language-specific, cultural, accessibility, and anti-slop checks.
7. Recover by reverting meaning-changing edits and raising a query to the source owner or in-country reviewer.
8. Release only with reviewer status and unresolved terminology visible.

## Quality Standards

The target text must preserve meaning and consequence while reading naturally for the named country and audience. French and Kiswahili publication requires competent in-country review; regulated content also requires subject review.

## Anti-Patterns

- Translating word for word. Fix: translate the sentence's intent and verify meaning against the source.
- Using one Kiswahili or French register for every country. Fix: record target country and obtain local review.
- Translating names, figures, or citations from memory. Fix: copy and verify them against the source.
- Replacing a regulated term with a smoother synonym. Fix: preserve it and ask the subject owner.
- Calling machine output native or certified. Fix: state review status and require a qualified human.
- Improving style by adding unsupported claims. Fix: preserve the source claim boundary.

## Worked Example

If a French draft contains a tax term with two plausible translations, retain the source term in the query record, use the provisional term consistently, and block publication until the relevant country and tax reviewer confirms it.
<!-- dual-compat-end -->

## References

- `../east-african-english/SKILL.md` for the English-only country register.
- `../writing-quality/SKILL.md` for argument, persuasion, and editorial structure.
- `../../meta-utility/anti-ai-slop/SKILL.md` and `../../meta-utility/ai-slop-audit/SKILL.md` for production and release gates.
