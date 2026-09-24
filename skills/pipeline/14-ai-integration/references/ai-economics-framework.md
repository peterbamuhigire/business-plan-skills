# AI Economics: Prediction, Judgment and Workflow Redesign

**Use for:** the AI integration section (14) of a business plan, especially deciding where AI is worth adopting and how to state it credibly. The framework is the prediction-economics approach of Agrawal, Gans and Goldfarb; structure and wording are the engine's own.

## 1. Core idea: AI makes prediction cheap

Current AI supplies prediction: using known information to fill in missing information (forecasting, classifying, inferring). When something fundamental gets cheaper, its use expands into old and new applications; its complements rise in value and its substitutes fall.

**Plan application.** Every business has predictions embedded in operations (demand, default, churn, quality, price). Identify where they sit and whether AI can make them cheaper, faster or more accurate.

## 2. Anatomy of a decision (seven elements)

| Element | Meaning | AI role |
|---|---|---|
| Input data | Fed to the model at run time | Collected by people or sensors |
| Training data | Historical data to build the model | Must be assembled; quality bounds model quality |
| Prediction | Missing information filled in | Increasingly automated |
| Judgment | Value placed on outcomes and errors | Stays human; rises in value |
| Action | Response to prediction plus judgment | Human or automated by stakes and speed |
| Outcome | The result | Feeds back |
| Feedback data | Outcome data used to improve the model | Needed for continuous improvement |

A prediction is not a decision. Prediction reduces uncertainty; judgment sets the payoffs; both are needed before action.

## 3. What rises and falls in value

**Rises (complements):**
- **Judgment:** defining the reward function, that is, the relative cost of each type of error. Example: a card issuer must weigh blocking a legitimate card against allowing fraud.
- **Data:** training, input and feedback data; proprietary data is strategic because it enables better predictions than rivals can make.
- **Action capacity:** the ability to act on a prediction (stock, logistics, relationships). Existing operators often hold this advantage.

**Falls:** human prediction tasks that a machine matches (route memorisation replaced by navigation, subjective scouting by statistical models, routine image reading, document review, fraud monitoring, customer triage). Roles usually change rather than vanish: less calculation, more analysis and judgment.

## 4. Redesign the workflow, not the task

Adding AI to an unchanged process yields little. Redesign around cheap prediction (as with process reengineering; the classic case is cutting an accounts-payable function by redesign rather than by automating the old process).

Steps:
1. Define the workflow objective.
2. Break it into tasks.
3. Locate the prediction in each task.
4. Estimate AI return per task.
5. Redesign the whole workflow.

**AI Canvas (one row per task):** action; prediction needed; judgment (how outcomes and errors are valued); outcome and success metric; input data; training data; feedback loop.

## 5. Two adoption modes

- **Tool (operational):** AI improves one task inside an existing workflow (autocomplete, fraud flags, FAQ chatbots, inventory forecasts). Incremental; strategy unchanged. Most early SME adoption.
- **Transformation (strategic):** prediction becomes accurate enough to tip a core business trade-off and change the model itself (for example, moving from ship-after-order to shipping ahead of demand, which also requires returns logistics and new data).

Conditions for strategic adoption: (1) a core trade-off creates cost or friction; (2) uncertainty drives that trade-off; (3) prediction reduces the uncertainty enough to change the best strategy.

**Plan prompt.** Name the uncertainty limiting the business, then test whether an available tool reduces it enough to change what the business does.

## 6. Stakes: recoverable versus catastrophic errors

Same error rate, different stakes.

| Error | Consequence | Stakes |
|---|---|---|
| Wrong product recommendation | Customer searches again | Low |
| Harmful content allowed through | Reputation, regulation | High |
| Missed diagnosis | Missed treatment | Very high |
| Vehicle misreads obstacle | Accident | Catastrophic |

- Recoverable errors: deploy with lighter oversight.
- Catastrophic errors: keep a human in the loop until accuracy is proven at a high threshold.

Most early SME uses (chatbots, inventory forecasting, post scheduling) are recoverable. Use robust human review for medical advice, credit decisions and collateral valuation.

## 7. Human-machine division of labour

| Category | Data situation | Who leads |
|---|---|---|
| Known knowns | Rich data | Machine |
| Known unknowns | Sparse data | Human |
| Unknown unknowns | Not in past data | Neither predicts; human reasons by analogy |
| Unknown knowns | Correlations masking causation problems | Human judgment to avoid misleading the model |

**Prediction by exception:** machines handle routine cases at scale; humans intervene on flagged, unusual or low-confidence cases (the analogue of management by exception).

Keep human: judgment and reward-function setting; high-stakes decisions; rare or novel situations; decisions needing empathy or trust; cases where the data-generating process is poorly understood. Machines can learn to imitate human judgment only where decisions are numerous and observable.

## 8. Timing: early or fast follower

Early adopters have scale, data and margin to absorb experimentation cost; later adopters benefit from falling costs and proven tools and can reach the same outcome.

- **Adopt early if:** the model has an uncertainty-driven trade-off AI can resolve; competitors are deploying; data perishes quickly.
- **Wait if:** sector tools are immature; implementation risk is high; margins cannot absorb transition cost.
- Warning: incumbents that wait too long may face AI-native rivals with data and model advantages that are costly to overtake.

## 9. Practical guidance for small businesses

1. **Start with the prediction, not the tool.** Typical SME predictions: who will return, refer or churn; next week's or month's stock need; which leads convert; best price; which supplier invoices contain errors.
2. **Data before deployment.** Check for historical outcome data, whether it is digitised, and whether outcomes are labelled. For many Ugandan SMEs the first step is record digitisation.
3. **Low stakes first:** personalisation, FAQ bots, stock alerts, scheduling.
4. **Preserve judgment:** AI proposes; humans confirm where error cost is significant.
5. **Redesign workflows:** ask how the process would look if the prediction were free and reliable.

## 10. Worked examples (prediction framework by function)

| Function | Old flow | Redesigned flow | Judgment kept human | Uganda example |
|---|---|---|---|---|
| Customer service | Human triages and answers | AI classifies and answers routine queries; human takes complex ones | Escalation; handling unhappy customers | WhatsApp bot for balance, reset and eligibility FAQs at a SACCO or agent |
| Inventory | Manager estimates from past sales plus buffer | AI forecasts demand by item for two to four weeks; manager reviews anomalies | Supplier relations; new-product decisions; cash trade-offs | Distributor using a spreadsheet forecast on 12 months of sales |
| Marketing | Same offer to all | AI segments by behaviour, personalises, learns | Brand voice; ethics; key accounts | Shop or agri-input dealer sending different offers to frequent, lapsed and new buyers |
| Credit | Officer reviews subjectively | AI scores from transaction and mobile money data; officer reviews score and reasons | Character; guarantee quality; overriding the model | SACCO or MFI using psychometric or transaction scoring |
| Quality control | Manual inspection | Camera and model flag defects; inspector reviews flags | Thresholds; borderline cases; batch rejection | Coffee or dairy processor using phone-based image checks |

## 11. Uganda and East Africa context

**Infrastructure:** mobile connectivity is wide but data cost matters; power reliability varies outside Kampala (plan offline fallbacks); smartphone use is rising but feature phones remain common in rural areas; digital literacy varies; most SME records are informal or on paper.

**Favour** mobile-first tools (WhatsApp, USSD, SMS), low-data or offline-capable options, pre-trained models rather than in-house builds, and integration with existing platforms (mobile money, accounting software).

**Tool categories (verify current price and availability before citing):**

| Function | Approach | Cost level | Need |
|---|---|---|---|
| Customer communication | WhatsApp Business chatbot | Low to medium | Smartphone, data |
| Demand forecasting | Spreadsheet forecasting; inventory apps | Free to low | Sales records |
| Segmentation | Email platform segmentation | Free to low | Email list |
| Content | General-purpose AI assistants; design tools | Free to low | Smartphone |
| Credit scoring | Psychometric tools; mobile money data | Medium | Provider partnership |
| Translation | Machine translation services | Free | Internet |
| Local-language voice | Emerging Swahili and Luganda assistants | Low | Smartphone |
| Image inspection | Cloud vision services; custom apps | Medium | Phone camera |
| Bookkeeping support | Accounting software analytics | Free to medium | Internet |
| Price intelligence | Online marketplace monitoring | Free | Internet |

**Data strategy for low-digitisation firms:**
1. Digitise transactions (mobile money statements, basic POS).
2. Record customer outcomes (returned, paid on time, referred).
3. Label history (for a loan book, mark repaid and defaulted; this becomes training data).
4. Start small: a few hundred records can reveal patterns with basic tools.

**Regional landscape (re-verify):** Kenya leads in fintech AI; Uganda's national IT authority (NITA-U) leads policy work; Rwanda is investing in AI infrastructure; EAC common market and AfCFTA digital trade provisions will shape cross-border data and data-sovereignty questions.

## 12. Checklist for the AI integration section

**A. Foundation**
- [ ] Three to five key predictions driving outcomes
- [ ] Data available: exists, digitised, labelled
- [ ] Workflows mapped and embedded prediction identified

**B. Tool selection**
- [ ] Named tools (not "we will use AI")
- [ ] Fit to local infrastructure (mobile-first, data cost, offline)
- [ ] Prediction each tool makes and its input data
- [ ] Judgment retained by humans and who holds it

**C. Implementation mode**
- [ ] Operational or strategic
- [ ] If strategic: the uncertainty resolved and how the model changes
- [ ] If operational: estimated productivity gain and saving

**D. Risk**
- [ ] Each application classed low or high stakes
- [ ] Human oversight process for high stakes
- [ ] Algorithmic bias risks for the customer base
- [ ] Data security measures

**E. Data and learning**
- [ ] How training data is obtained or built
- [ ] How feedback data is captured
- [ ] Data ownership sits with the business, not a supplier
- [ ] Timeline from manual records to AI-ready data

**F. Competitive position**
- [ ] Competitor AI use and stage
- [ ] Any early-mover advantage
- [ ] Proprietary data that could sustain an advantage

**G. Workforce**
- [ ] Tasks automated and roles changed
- [ ] Training or reskilling
- [ ] New judgment-intensive roles (exception handlers, data stewards)

**H. Investment and return**
- [ ] Cost (tools, digitisation, training, integration)
- [ ] Return (saving, revenue, risk reduction)
- [ ] Payback period and its assumptions

## 13. Cross-references

- 03 products and services: `business-models-innovation-teece.md`
- 05 target market: `uganda-consumer-demographics-2025.md`
- 07 marketing: `social-business-brand-strategy.md`
- 08 operations: `small-business-unconventional-strategy.md`
- 10 financial projections: `financial-model-templates.md`
- 11 funding request: `11-funding-request/SKILL.md` (CAMPARI)
- 12 risk analysis: `uganda-risk-context.md`
- 14: `process-automation-readiness.md`, `uganda-ict-ip-guidelines.md`

Sources consulted: Agrawal, A., Gans, J. and Goldfarb, A. (2022), *Prediction Machines: The Simple Economics of Artificial Intelligence* (updated edition), Harvard Business Review Press; Hammer, M. and Champy, J. (1993), *Reengineering the Corporation*. Cite in the plan on first use with a full entry in the appendices.
