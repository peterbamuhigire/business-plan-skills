Parent: [Writing Quality](../SKILL.md)

**When to read:** before drafting or revising any business-plan section, marketing plan, blog or article, to choose the right strategy emphasis, keywords, verbs and evidence phrasing. This file is the index and the shared rules; the section-level entries live in the companion files listed below.

# Business-Plan Phrase Bank: Index and Shared Rules

Method source: the power-paragraph sentence jobs, the evaluator scorecard and the strategy-type emphasis idea are adapted from Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*, McGraw-Hill. Tone discipline ("realistic optimism", facts before adjectives) is adapted from Abrams, R. M. (1993) *The Successful Business Plan: Secrets & Strategies*, 2nd edn, The Oasis Press. All templates, examples and rewrites in this bank are original to this engine. No figure in any example is a real market fact; figures are labelled illustrative or shown as `[slots]`.

## 1. Files in the bank

| File | Use it for |
|---|---|
| `business-plan-phrase-bank.md` (this file) | How to use the bank, register by reader, verb and precision-word banks, evidence and hedging phrasing, strategy-type field and emphasis table |
| `business-plan-phrase-bank-sections-01-08.md` | Pipeline sections 01 executive summary to 08 operations plan |
| `business-plan-phrase-bank-sections-09-16.md` | Pipeline sections 09 management team to 16 sustainability, including 11b grant proposal and 14 AI integration |
| `marketing-plan-phrase-bank.md` | A standalone marketing plan, from executive summary to risks, including SMART objective rewrites |
| `article-and-blog-phrase-guidance.md` | Blogs, articles and thought-leadership posts for a business audience |

## 2. How to use the bank

1. **Confirm the section.** Open the section entry in the matching file. Read its purpose line and the decision the reader makes from it. If the draft does not help that decision, fix the thinking before the wording.
2. **Confirm the strategy type.** Read `strategy_type` from the client intake brief (section 4 below). Use the emphasis table to decide which point the section must stress and which proof the reader will expect.
3. **Write the power paragraph first.** Each major section opens with a three- or four-sentence lead in which every sentence has one job: (1) the fact the reader needs, (2) why it matters, (3) the strategy-type emphasis, (4) the implication the reader should accept. Then give the situation, the company's response and the supporting tables.
4. **Pick templates, then fill slots with verified facts only.** A slot such as `[n]`, `[UGX amount]` or `[source, date]` is filled from the source-of-truth register, client records, the financial model or a cited source. If no verified value exists, do not guess. Either obtain it, restate the sentence as an assumption (section 6), or cut the sentence.
5. **Never ship an unfilled slot.** Before release, search the draft for `[` and `]`. Any remaining slot is a release blocker, not a style issue.
6. **Vary the wording.** Templates are sentence skeletons, not copy. Do not use the same template twice in one section, and do not open three consecutive sentences with the company name. Repeat key *phrases* across the plan (the executive summary should echo each section's lead phrase), not whole paragraphs.
7. **Run the rewrites test.** Compare your draft against the section's before→after pairs. If your sentence resembles a "before", rewrite it.
8. **Finish with the gates.** Run `anti-ai-slop`, then `language-standards` and `east-african-english` for register and spelling.

### Slot notation used throughout

`[Company]` the business the plan is for · `[Client]` a customer organisation · `[n]` a count · `[%]` a percentage · `[UGX amount]` a sum with thousand separators · `[place]` a named district, town, parish or estate · `[date]` a month and year or a quarter · `[named alternative]` what customers use today · `[source, date]` a named source and its publication date · `[metric]` a defined measure · `[role]` a job title.

### Numbers and money

- Write `UGX 18,500,000` or `UGX 18.5 million`; choose one style per document. Use `UGX 480 million`, not `UGX 480M`, in prose.
- State the period for every flow figure: "a month", "a year", "per litre", "per member".
- For non-Ugandan plans, use the local currency first (KES, TZS, RWF, USD) and give a conversion only with its rate and date.
- Round consistently. A projection shown as `UGX 1,237,418,000` claims false precision; `about UGX 1.24 billion` is honest.

## 3. Register by reader

The same fact is framed differently for different readers. Choose the register before drafting and keep it for the whole document.

| Reader | What they decide | Lead with | Register | Avoid |
|---|---|---|---|---|
| **Bank or SACCO credit officer** | Whether the loan will be repaid and what secures it | Cash flow, debt service cover, collateral, track record, owner's contribution | Formal, conservative, third person ("The Company", "[Company]") | Upside stories, valuation talk, "disrupt", unsupported growth rates |
| **Equity investor or angel** | Whether the business can grow enough to return the investment several times | Market driver, customer evidence, one key advantage, unit economics, team, use of funds, exit route | Confident and compressed; "we" acceptable in a pitch narrative, third person in the plan | Guaranteed-return language, lists of five advantages, hiding dilution |
| **Grant funder or DFI** | Whether the project delivers the funder's outcomes for the target beneficiaries, and survives after the grant | Problem evidence, beneficiaries, theory of change, measurable results, sustainability, cost per outcome | Formal, results-based, the funder's own terms (outputs, outcomes, indicators) | Commercial hype, vague "empowerment", outputs presented as outcomes |
| **Internal board or management** | Whether to approve the plan, the budget and who owns what | Objectives, choices and trade-offs, resources, owners, review dates | Direct, first-person plural, decision-oriented | Selling to people who already know the business; burying the ask |
| **Strategic partner** | Whether the partnership serves their interest | Each party's need stated with equal weight, what each contributes, how value is split | Courteous, balanced | Writing only about your own gain |

Universal rules for plan tone:

- **Realistic optimism.** Let facts lead the reader to the conclusion. Adjectives do not persuade a credit committee.
- **One calibrated superlative per section at most**, and only with its proof in the same or the next sentence. "The only paediatric-equipped practice north of Ntinda" needs the survey or map that shows it.
- **Conservative and honest.** State the weak point before the reader finds it, then state the control.
- **Named subject, numbers early.** "[Company] serves the 1,200 stockists…" not "There is an opportunity to serve many stockists…".
- **Forward-looking conclusions.** End a section on the position, share or result the company will reach, never on a recap ("As shown above…").
- **East African courtesy without padding.** Courteous phrases belong in cover letters and correspondence; plan sections state facts plainly.

## 4. Strategy-type field for client intake

> **For the lead integrator.** Add this field to `00-client-intake` (Phase 1 brief and source-of-truth register). Section skills read it to choose emphasis and proof.

**Field name:** `strategy_type`

**Structure:** `strategy_type: { primary: <value>, secondary: <value or null>, rationale: "<one sentence citing evidence>" }`

**Allowed values** (the seven strategy archetypes taught by Debelak, renamed as machine-safe values):

| Value | Definition (one line) | Typical East African example (illustrative) |
|---|---|---|
| `market_maker` | Introduces a concept or service that the target customers have not been offered before | First cold-chain-as-a-service for smallholder dairy around Mbarara |
| `market_enabler` | Helps an already proven, growing trend or product reach more users or uses | A solar-irrigation installer serving farmers who already buy pay-as-you-go solar |
| `technology_leader` | Wins through a tested technology that delivers a benefit customers rank as important | A crop-disease detection app validated with extension officers |
| `niche_marketer` | Serves a defined, stable subgroup with needs that general providers serve poorly | A paediatric dental clinic in Kira |
| `customer_solution` | Offers one complete answer to a problem customers now solve through several suppliers | One-stop company-registration, tax and social-security filing for SMEs |
| `performance_enhancer` | Does the same job measurably better (faster, more reliable, higher quality) than current options | Tracked, same-hour boda parcel delivery in Kampala |
| `efficiency_improver` | Delivers the same outcome at lower cost and passes part of the saving to customers | Pooled bulk purchasing for rural pharmacies |

**How to pick:**

1. Choose **one primary** type: the one that best answers "why will customers switch to us?". If two seem equal, choose the one the founder can prove today.
2. Add **at most one secondary** type only when a second emphasis changes at least two sections (for example, a `niche_marketer` whose advantage within the niche is price: secondary `efficiency_improver`).
3. Record a one-sentence rationale with its evidence (pilot data, customer interviews, contracts).
4. Revisit the field when the evidence changes. A plan whose sections stress different types without a recorded secondary reads as confused.

**Mapping from common strategy labels** (so intake conversations translate cleanly):

| Client says | Usually maps to | Check |
|---|---|---|
| "Low-cost", "cheapest", "price leader" | `efficiency_improver` | Is the cost advantage structural (scale, sourcing, process) or only a lower margin? A lower margin is not a strategy |
| "Premium", "differentiated", "quality" | `performance_enhancer` or `customer_solution` | What exactly performs better, measured how? |
| "First in Uganda", "new concept" | `market_maker` | Why has no one done it before, and why now? |
| "Riding the boom in X" | `market_enabler` | Is X proven with dated evidence? |
| "We have the technology" | `technology_leader` | Has it been field-tested with real users? |
| "Specialist", "focused", "boutique" | `niche_marketer` | Is the niche large enough and stable? |
| "Expansion", "turnaround", "second branch" | Not a strategy type. Record the business stage separately (intake already captures stage) and pick the type that explains *why the expansion or recovery will win customers* | |

## 5. Strategy-type emphasis table

For each type: which sections carry the weight, the keywords that signal the strategy, the proof a lender or investor will expect, and a sample thesis sentence (all figures illustrative).

### 5.1 `market_maker`

- **Emphasise:** 04 market analysis (why now), 05 target market (strength of unmet need), 06 competition (why current options are inadequate), 12 risk (adoption risk).
- **Keywords:** new to this market, unmet need, only recently viable, why now, early adopters, pilot uptake, adoption curve, customer education cost, first-mover window.
- **Proof expected:** pilot or pre-order data; a dated driver that explains why the opportunity did not exist earlier; willingness-to-pay evidence; customer-education budget.
- **Emphasis per section:** customers have a strong need current options ignore; the driver is recent; existing products are inadequate; the niche is receptive; the concept is markedly better; buyers will pay for it.
- **Sample thesis (illustrative):** "Since two processing plants opened near Mbarara in [year], milk volumes within 15 km have reached the density that makes shared chilling viable; ColdLink will be the first to offer it as a per-litre service."

### 5.2 `market_enabler`

- **Emphasise:** 04 market analysis (proven growth), 07 marketing and sales (channel partners), 06 competition (you grow the market with others).
- **Keywords:** proven demand, recognised category, installed base, new users, new applications, channel partners recommend, attach rate, growth constraint removed.
- **Proof expected:** dated growth evidence for the underlying trend; partner letters; the specific constraint you remove (finance, installation, training).
- **Emphasis per section:** the market is growing; the trend is recognised; new users are fuelling growth; other players value what you do; the market needs your service to keep growing.
- **Sample thesis (illustrative):** "Farmers who already own solar home systems are asking dealers for irrigation pumps they can pay for by mobile money; SunFlow supplies, installs and finances those pumps through the same dealers."

### 5.3 `technology_leader`

- **Emphasise:** 03 products and services (benefit, not features), 08 operations (production readiness), 12 risk (technical risk retired), 14 AI integration where relevant.
- **Keywords:** field-tested, validated, accuracy rate, uptime, ease of adoption, integration, maintenance, intellectual property, technical risk retired.
- **Proof expected:** test results with sample size and date; named pilot users; IP or licence status; implementation effort per customer.
- **Emphasis per section:** the technology meets a need customers rank as important; introduction risk is low because testing is done; implementation is easy; no major production hurdles remain.
- **Sample thesis (illustrative):** "In a [n]-farm trial in Gulu district during [season], LeafCheck identified cassava disease with [x]% agreement with extension officers; it now needs capital to train 200 village agents."

### 5.4 `niche_marketer`

- **Emphasise:** 05 target market (size and stability of the niche), 06 competition (why generalists underserve it), 07 marketing (reaching the niche cheaply), 10 financials (niche pricing).
- **Keywords:** defined segment, specialist, underserved by generalists, stable demand, word of mouth, referral rate, share of niche, specialist premium.
- **Proof expected:** a counted niche (number, place, current spend); evidence it is stable; referral or repeat data; the reason generalists ignore it.
- **Emphasis per section:** the group is large and stable; the market is unlikely to change; growth will continue; your advantage is major for this niche; the niche itself explains the better margin.
- **Sample thesis (illustrative):** "Smile Kids will serve only children's dentistry for the estimated [n] families in Kira, Najjera and Kyanja who now drive to central Kampala for it."

### 5.5 `customer_solution`

- **Emphasise:** 03 products and services (completeness), 05 target market (cost of the fragmented status quo), 08 operations (coordination capacity), 07 sales (one point of contact).
- **Keywords:** single point of contact, end-to-end, one invoice, fewer suppliers, time saved, coordination, service level, complete package.
- **Proof expected:** the number of suppliers or steps customers use today; the time or cost that consolidation removes; service-level commitments you can meet.
- **Emphasis per section:** there is no complete solution today; having one matters to this market; the solution fits the niche; it is noticeably better; completeness produces a significant benefit.
- **Sample thesis (illustrative):** "FileRight replaces the three to four agents a Kampala SME uses for registration, tax and social-security filings with one monthly fee and one accountable officer."

### 5.6 `performance_enhancer`

- **Emphasise:** 03 products and services (measured performance), 06 competition (head-to-head on the criterion that matters), 07 marketing (proof in the message), 10 financials (price premium).
- **Keywords:** measured improvement, faster by, reliability rate, error rate, on-time rate, guarantee, service level, performance gap, premium justified by.
- **Proof expected:** a measured comparison against named alternatives on the customer's top buying criterion; a reason the edge will not be copied quickly.
- **Emphasis per section:** customers feel current offers fall short; the edge will not be erased quickly; customers value the gain; current products do not serve the niche well; the advantage converts into sales.
- **Sample thesis (illustrative):** "[Company] delivers within Kampala in under 90 minutes with live tracking, against the half-day typical of informal boda dispatch, and merchants pay [UGX amount] more per parcel for that certainty."

### 5.7 `efficiency_improver`

- **Emphasise:** 08 operations (cost structure), 10 financials (unit cost and margin), 05 target market (constant or growing need), 06 competition (cost comparison).
- **Keywords:** unit cost, cost per [unit], volume discount, pooled purchasing, utilisation, overhead per unit, price advantage, cost passed on, margin sustained by.
- **Proof expected:** a costed comparison of the old and new way; the source of the saving (scale, sourcing, process, location); proof the saving survives competitor response.
- **Emphasis per section:** the need is constant or growing; customers already buy and will value the saving; efficiency matters to them; the saving is substantial; efficiency produces higher profit.
- **Sample thesis (illustrative):** "By pooling orders from [n] rural pharmacies in Lira and Apac, MedPool earns distributor discounts no single pharmacy qualifies for and passes half the saving back to members."

## 6. Evidence and hedging phrasing

Readers must always know whether a sentence reports a verified fact, an assumption, an estimate or a projection. Label each one; never let an assumption wear the grammar of a fact.

| Status | Use when | Phrasing patterns |
|---|---|---|
| **Verified fact** | The claim traces to a record, contract or named source | "[Company] signed supply agreements with [n] supermarkets in [month year]." · "According to [source, date], [finding]." · "Audited accounts for [year] show revenue of [UGX amount]." · "Sales records for [period] show [metric]." |
| **Client-supplied fact, not independently verified** | The founder provided it and it is plausible | "Management reports that [fact]; supporting records are in Appendix [x]." · "The founders state that [fact]; this will be confirmed during due diligence." |
| **Assumption** | A value the model depends on but no one can know yet | "Management assumes [value], based on [reason or comparable]." · "The projections assume [x]; if it is [y] instead, [consequence] (see sensitivity table)." · "This assumes [condition] continues through [period]." |
| **Estimate** | A present-day value derived by calculation from sourced inputs | "We estimate [metric] at [value], calculated as [n] × [value] from [sources]." · "Using [source, date] counts and a [%] adoption rate observed in the pilot, we estimate [value]." |
| **Projection** | A future value from the model | "We project [metric] of [value] by [date], on the assumption that [driver 1] and [driver 2]." · "The base case projects [value]; the downside case, with [change], projects [value]." |
| **Target** | A value the business commits to pursue | "[Company]'s target is [value] by [date], owned by [role] and reviewed [monthly]." |
| **Unknown** | Evidence does not yet exist | "No reliable figure for [metric] is available for [place]; [Company] will measure it during [pilot/phase] and report by [date]." |

Rules:

- **Hedge once, in the right place.** "Management assumes 55% occupancy in year one, based on the average of three comparable lodges in Fort Portal" is honest. "It is hoped that occupancy may possibly reach around 55%" is weak and evasive.
- **Do not hedge facts.** "The business should hopefully generate" is wrong if the sales record shows the figure.
- **Attach the source at the point of the claim**, with its date. "(UBOS, [year])" beats a footnote the reader must hunt for.
- **Market figures carry a scope label**: broad (everything customers buy for the same purpose) or narrow (direct competitors' products), and the geography.
- **Volatile facts** (tax rates, regulatory thresholds, prices, platform features) enter a plan only from the engine's currentness register or a checked primary source. Otherwise write them as a check: "The applicable [levy] rate must be confirmed with [authority] before submission."

## 7. Verb bank

Strong verbs carry commitment and show who does what. Choose the verb that states the exact action.

| Function | Verbs | Example (illustrative) |
|---|---|---|
| Commitment | will open, will hire, will install, will sign, will launch, will repay, will deliver | "[Company] will open its Mukono branch in March [year]." |
| Growth | add, extend, enter, double, open, recruit, reach | "The second van extends coverage to Kawempe and Kasangati." |
| Reduction | cut, shorten, reduce, remove, recover, lower | "Mobile-money links shorten collection from 45 to 20 days." |
| Evidence | shows, records, confirms, reports, measured, found | "The pilot log records 312 orders in 8 weeks." |
| Control | reviews, approves, reconciles, audits, monitors, caps | "The board reviews cash against budget every month." |
| Choice | chose, prioritises, concedes, rejects, defers | "[Company] chose Jinja over Mbale because…" |
| Money | invests, contributes, borrows, allocates, earns, spends | "The founders contribute UGX 90 million in equity." |
| Customer action | buy, switch, renew, refer, order, pay | "Riders renew the monthly plan at [x]%." |

### Weak → strong substitution table

| Weak or vague (wrong) | Strong and specific |
|---|---|
| aims to explore opportunities in | will enter [market] in [quarter] |
| is committed to excellence | [measured standard, e.g. answers every complaint within four working hours] |
| provides solutions | [installs / supplies / repairs / trains / finances] [object] |
| has a wide range of experience | has [n] years in [field], including [named result] |
| plans to grow significantly | projects revenue of [UGX amount] by [year], from [driver] |
| enhance efficiency | cut [process] time from [a] to [b] |
| strategic partnerships | signed agreements with [named partners] covering [scope] |
| a large and growing market | a [broad/narrow] market of about [value] ([source, date]) |
| customers love our product | [n] of [n] pilot customers reordered within [period] |
| world-class team | [named person] ran [function] at [named organisation] for [n] years |
| cutting-edge technology | [technology], tested at [n] sites for [period] |
| affordable prices | [UGX price], [x]% below [named alternative] |
| we hope to break even | the model reaches monthly break-even in month [n] at [volume] |
| funds will be used for growth | [UGX amount] buys [assets / hires / stock] that raise capacity from [a] to [b] |
| will empower communities | will employ [n] people in [place], [x]% of them women |
| is well positioned | holds [asset / contract / location] that competitors lack |

## 8. Precision-word bank

Nouns and phrases that carry evidence. Use them only when the plan contains the thing they name.

- **Customer and demand:** paying customers, repeat purchase rate, order book, letters of intent, signed offtake agreement, waiting list, conversion rate, average order value, churn, referral rate, catchment, footfall.
- **Market:** broad market, narrow market, serviceable market, obtainable share, market driver, forced action, substitute, direct competitor, indirect competitor, price point, switching cost.
- **Operations:** capacity, utilisation, lead time, throughput, reject rate, stock turn, service level, cold chain, standard operating procedure, supplier concentration.
- **Finance:** gross margin, EBITDA margin, net margin (after interest, tax and depreciation), contribution per unit, break-even volume, working capital cycle, debt service coverage ratio, payback period, owner's equity contribution, collateral, security, covenant.
- **Governance and people:** board, independent director, audit committee, key-person risk, vesting, succession, delegated authority, reporting line.
- **Impact and grants:** beneficiary, output, outcome, indicator, baseline, target, means of verification, theory of change, cost per beneficiary, exit and sustainability.

Label margins precisely: gross, EBITDA, operating, or net. Where a finance meaning is in doubt, check with the finance engine (`chwezi-accounting-doctrine`) before the figure ships.

## 9. Release checklist for any section built from this bank

- [ ] The section opens with its power paragraph, and each sentence does one job.
- [ ] The strategy-type emphasis for this section is present and matches `strategy_type`.
- [ ] Every number has a unit, period and source or a status label (fact, assumption, estimate, projection, target).
- [ ] No slot `[…]` remains.
- [ ] No template repeated within the section; sentence length varies.
- [ ] No banned vocabulary from `anti-ai-slop`; no unsupported superlative.
- [ ] The key phrase of the section appears in the executive summary.
- [ ] Red-flag phrases listed for this section are absent.
