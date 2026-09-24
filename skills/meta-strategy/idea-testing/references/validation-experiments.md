# Validation Experiments: Getting Stronger Evidence Before a Full Build

Use this reference after discovery experiments have given a clear direction. Validation experiments seek stronger evidence (real actions, payments and commitments). They cost more time and money but reduce risk before building. Escalate fidelity progressively: concierge, then single-feature product, then full build; never skip validation to go straight to build. The catalogue follows the experiment-library approach of Bland and Osterwalder (Testing Business Ideas, 2020), reorganised by the question each technique answers. Record each with the cards in test-learn-decide.md.

## 1. Choosing a technique

| Situation | Recommended experiment |
|---|---|
| Digital product; need to test the flow | Clickable prototype |
| Service business; validate before hiring | Concierge |
| Physical product; test sales | Pop-up store or presale |
| Business-to-business product with large deals | Letter of intent |
| Consumer product; need proof of demand | Presale or crowdfunding |
| Unsure the technical approach is possible | Technical spike |
| Have traffic; optimise conversion | Split test |
| Test price sensitivity | Mock sale or validation survey |
| Test with stitched-together tools | Mash-up |
| Test automation before building it | Simulated automation (wizard of Oz) |

## 2. Progression

1. Low fidelity: clickable prototype or concierge (one to two weeks; small budget).
2. Medium fidelity: pop-up store, presale or mock sale (two to four weeks; moderate budget).
3. High fidelity: single-feature product or mash-up (four to twelve weeks; larger budget).
4. Commitment: letter of intent or crowdfunding (confirms that a full build is justified).
Move up only when the current level yields at least medium-confidence evidence (see test-learn-decide.md). Set budgets in local currency from quotes.

## 3. Prototypes and delivery tests

### Clickable prototype
A digital mock-up with clickable zones to test flow. Evidence: moderate. Use after paper testing. Design screens in a prototyping tool (a slide deck with links will do); test internally; run facilitated sessions with 10 to 15 target customers, one asking and one noting; observe confusion and excitement without explaining. Metrics: task completion rate, time to complete key tasks, themes. For non-digital offers, use a hyperlinked brochure or a simulated messaging-conversation flow.

### Single-feature product
A working minimum product delivering the single most important feature. Evidence: strong (satisfaction plus payment). Use after discovery and lower-fidelity tests confirm need and concept. Takes one to three weeks to build and several to run.
1. Design the smallest version solving the most important customer job.
2. Test internally.
3. Acquire customers through channels proven in discovery.
4. Deliver and collect payment if applicable.
5. Gather structured satisfaction feedback.
Metrics: satisfaction (about 4 out of 5 or better), purchases, cost to deliver (unit economics), quotes on what was valued or missing. Examples: a food business sells one product through one channel; a service business delivers one package manually; a software idea runs first as a messaging-based service.

### Mash-up
Assemble existing tools or services into a working offer instead of building. Evidence: strong.
1. Map the process needed to deliver value.
2. Survey existing tools for each step.
3. Combine them and test internally.
4. Deliver to customers; measure satisfaction and payments.
5. Build custom parts only where existing tools proved insufficient.
Examples: messaging-app orders plus a spreadsheet for inventory plus mobile-money payments before an app; existing couriers before an own fleet; a shared commercial kitchen before your own processing plant.

### Concierge
Deliver entirely by hand with the customer knowing a person is doing the work. Evidence: strong. Ideal for services and before automation.
1. Plan every manual step.
2. Take orders by messaging, in person or a simple form.
3. Deliver and record every step and its time.
4. Charge at real price points.
5. Collect feedback after delivery.
6. Use cost and time data to decide on automation.
Metrics: satisfaction, time per delivery, revenue and cost per delivery, repeat purchases. Most successful local service businesses begin this way: the founder delivers everything, systematises what works, then hires and automates only what systemisation cannot handle. Early food-delivery services often started as messaging orders plus motorcycle couriers.

### Life-sized prototype
A non-functional but physically accurate model where presence matters (furniture, equipment, retail layout). Build from cardboard, foam or cheap boards; place it in the real environment; record reactions and quotes. Local fabricators can build mock-ups cheaply. Evidence: moderate.

### Simulated automation (wizard of Oz)
A front end that looks automated (page, app shell, messaging bot) with people fulfilling every request behind the scenes; customers believe it is automated. Evidence: strong (behaviour is real).
1. Build the front end.
2. Fulfil manually.
3. Measure conversion, satisfaction, retention and willingness to pay.
Decision: strong evidence justifies building the real system; weak demand is revealed before automation cost. Manually operated messaging "bots" are common and valid validation. A well-known marketplace founder pattern: visiting early suppliers and photographing their offerings by hand before building the platform.

### Technical spike
A small, time-boxed piece of code (one day to two weeks) proving a specific technical approach is feasible.
1. Define acceptance criteria.
2. Set the time box.
3. Code only for those criteria.
4. Report performance, complexity and a recommendation.
5. Decide build, borrow (existing library or service) or buy (third-party platform).
6. Discard the spike code; it is not production code.
Relevant to mobile-money integrations, USSD or SMS services and sensor deployments: can we integrate reliably under local network conditions?

## 4. Demand and commitment tests

### Simple landing page
One page with a headline (value proposition), three benefits and one call to action (sign-up, payment or enquiry). Drive traffic by ads, social posts, broadcast or email. Evidence: sign-ups moderate, payments strong. Metrics (verify): email sign-up conversion in the range of roughly 5 to 20 percent; payment conversion of 1 to 5 percent of visitors is a strong signal. A messaging business profile with a link is the lowest-friction local equivalent; measure clicks, conversations started and purchases.

### Mock sale
Present a real offer and price (several tiers if testing price sensitivity) with a "buy" button or pricing page; track clicks, sign-ups and payment details entered; stop before charging and explain the product is not yet available; follow up. Evidence: moderate to strong (clicks moderate, sign-ups after pricing moderate to strong, payment details entered strong). A well-known example added a plans-and-pricing page before writing product code and read the most popular tier from sign-ups.

### Presale
Collect payment before the product exists or is ready. Evidence: very strong.
1. State clearly what, when and at what price.
2. Say honestly that it is not yet available.
3. Accept mobile money, bank transfer or a payment gateway.
4. Track presales, order value and source.
Set a minimum viable quantity in advance ("we produce the first batch if we receive 50 orders by [date]") and compare revenue with first-batch cost. Risk: legal duty to deliver or refund; be conservative on dates; confirm in writing with receipts. Presales by messaging broadcast are common for small businesses.

### Crowdfunding
Raise money before building; tests viability, messaging and funds the first batch. Evidence: real payments, very strong for consumer products. Create a video, description and reward tiers; set a minimum goal equal to the first production run; drive traffic from your audience and press; track backers, average pledge and the most popular tier. Metric: funds raised versus goal (100 percent or more is strong). International platforms can be hard to use from some countries because of payment limits; use pre-order campaigns with mobile money or local payment gateways and document every pre-order.

### Letter of intent
A short non-binding written statement from a customer or partner confirming intent to buy or collaborate. Evidence: strong (stronger than verbal, weaker than payment). For business, institutional and procurement planning.
1. Hold conversations and confirm warm interest.
2. Prepare a one to two-page template.
3. Present it in or after a meeting, never cold.
4. Track number sent, signed and converted.
Sample wording: "We submit a non-binding letter of intent to [purchase X units / partner on Y / participate in Z] on these terms: [brief terms]. Signed: name, title, organisation, date." Customers who say they will buy a large quantity often write a much smaller figure on paper, so letters reveal real commitment. Government agencies, non-profits and large companies often require them before allocating supplier slots; request them early to qualify buyers.

### Pop-up store
A temporary stall or space testing face-to-face response and real sales. Evidence: strong. For physical products, food, fashion and consumer goods; not for business-to-business.
1. Find a site with target traffic.
2. Obtain permits (local authority trading permit, market authority permission).
3. Design the display.
4. Promote in advance.
5. Staff with people who observe and record reactions.
6. Collect enquiries, contacts, mock sales, presales and sales.
Metrics: visitors, enquiry rate, conversion, average transaction, themes from conversations. Venues: markets, mall atria, trade fairs, school open days, exhibitions, roadside stalls. A useful finding pattern: customers may be aware of the symptom without framing it as the problem you solve, which reshapes messaging.

### Split test
Run two versions (one variable changed) simultaneously to randomly split audiences; choose the winner on the conversion metric at about 95 percent confidence. Needs enough volume (often 100 or more events per variant). Useful for message copy, ad creative and price points; even manual splits (version A to the first 100 contacts, B to the next 100) give directional data.

### Validation survey
Quantifies confirmation of qualitative findings with specific questions ("Here is our offer at this price: how likely are you to buy?"), not general pain exploration. Metrics: share "very likely to buy" (a common bar is around 40 percent for consumers, lower for business buyers), acceptable price range (Van Westendorp price sensitivity analysis) and willingness to pay by segment. Avoid "Would you buy this?"; ask "If we launched tomorrow at [price], what would you do?" with specific options.

## 5. Plan-section prompts

- Which validation experiment fits the riskiest remaining assumption, and why?
- What are the pass and fail criteria set beforehand?
- What did customers actually do or pay, and what does it say about unit economics?
- Which level of fidelity is next, at what budget?

Sources consulted: Bland, D. and Osterwalder, A., Testing Business Ideas (Wiley, 2020), and general lean-experiment practice. Thresholds are planning assumptions.
