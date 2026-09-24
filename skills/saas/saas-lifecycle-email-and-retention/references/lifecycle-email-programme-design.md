Parent: [SaaS Lifecycle Email & Retention Skill](../SKILL.md)

When to read: when a SaaS plan must specify its lifecycle email and messaging programme, the data behind it, deliverability, team growth, and how it affects activation, retention, NRR and CAC payback.

# Lifecycle messaging programme: plan specification

This is the engine's specification for the lifecycle email (and messaging) part of a SaaS plan. It is organised as the plan sections a reviewer expects: why it matters financially, the customer stages it must cover, the data it needs, build order, writing and pacing rules, deliverability, measurement, team and the WhatsApp overlay. The SaaS email literature informs it, in particular Garbugli, É. (2020) *The SaaS Email Marketing Playbook*, which sets out a lifecycle-wide email framework. The stage table, rules and examples are this engine's; response-time studies, open-rate averages and tool names from the source are not used.

## 1. Why the programme belongs in the financial model

Channels deliver sign-ups; many sign-ups never return without follow-up. Email and opted-in messaging reach every stage at very low cost per contact, so small conversion gains compound. Section 10 should show lifecycle messaging as a lever on trial-to-paid conversion, churn and expansion in the LTV:CAC and CAC-payback model, with the assumed lift labelled and tested.

## 2. Customer stages the programme must cover

| Customer stage | Message aim | Trigger | Measure |
|---|---|---|---|
| Prospect (not yet signed up) | First meeting or trial | Named target list; consent and anti-spam rules checked per market | Replies, meetings |
| New user | Reach first value quickly | Sign-up | Activation rate, trial-to-paid |
| Active user | Deeper use of key features | Feature events | Feature adoption, active-use ratio |
| Paying customer with headroom | Upgrade or add modules | Usage near plan limits, team growth | Expansion ARR, NRR |
| At-risk customer | Prevent loss | Falling use, failed payment, support spikes | Save rate, churn |
| Satisfied customer | Bring others | A success moment (report delivered, milestone reached) | Referral sign-ups |
| Former customer | Win back | Cancellation plus a waiting period | Win-back rate |

For each, define trigger, number of messages, spacing, owner and measure.

## 3. Data plan (before any copy)

1. Map the customer journey: every state and transition.
2. Define profile fields: sign-up source, plan, last login, feature flags, MRR, satisfaction score, open support tickets.
3. Track events that trigger messages.
4. Build segments from fields and events (power users, at-risk, trial day 3, cancelled in the last 30 days).
5. Set rules: frequency caps, exclusions, send-time windows, test framework.

Budget event tracking and segmentation in the operations and data sections, not just a CRM. Compare hosted and self-hosted tools on current cost, deliverability and data-residency terms (see the data-protection rules in the marketing orchestrator's location and scope calibration).

## 4. Build order

Launch the new-user sequence first (usually the largest return), then triggers for the three most important activation events, then a cancellation save sequence, then periodic upgrade prompts, then optimise. Rank later sequences by audience size × likely impact, closeness to revenue, and build effort (single trigger before branching flows).

**Speed rule:** put a first-touch target for new sign-ups and inbound leads into the service level; automation makes an almost immediate first message possible. Set the target from the business's own conversion data.

## 5. Writing and pacing rules

- B2B messages in plain text or light formatting; they read as personal and tend to deliver better.
- Short, specific subject lines; curiosity without bait. Test several types (a number, a direct benefit, a personal note, a behaviour-based reference).
- One call to action per message.
- A named sender and a monitored reply address; replies are leads.
- Designed for phones and low bandwidth.
- Avoid spam-trigger wording, empty "just checking in" openings and personalisation that feels manufactured.
- Test local-language phrases alongside English where customers use them.

Pacing: new-user messages concentrated in the first two to four weeks; more frequent near trial expiry; behavioural messages on the event; a save message on cancellation and one follow-up about a week later; win-back as a short series over roughly a month, then stop.

## 6. Deliverability (budget and schedule it)

- SPF, DKIM and DMARC on every sending domain.
- Warm up sending volume gradually.
- Remove bounces, suppress long-term non-openers, validate addresses at sign-up.
- Protect engagement signals; complaints damage reputation.
- Separate subdomains for transactional, marketing and sales mail.
- Where local sending infrastructure has weaker reputation, test established providers.

## 7. Measurement

Do not rely on "industry average" open rates: privacy features distort opens and lists differ. Benchmark against the business's own history (this quarter against last). Improve in this order: delivery → opens (subject, timing) → message (offer, copy, action) → landing page → roll proven messages to more segments.

## 8. Team growth

Tie staffing to ARR milestones in the talent plan: founder with a freelancer → one dedicated lifecycle marketer → a small team (lead, writer, operations or analyst) → a full function (manager, writer, designer, operations, analyst).

## 9. Email and WhatsApp together

Where WhatsApp carries real-time conversation and email is mainly for records, orchestrate both: email for long-form content, receipts and records; opted-in messaging for urgent, relational and real-time contact. Follow platform business-messaging policies and data-protection consent and objection rules. A strong programme may differentiate a firm whose local rivals do little lifecycle work; test that before claiming it.

**Illustrative example.** A Kampala clinic-booking SaaS: sign-up triggers a named-sender email plus a WhatsApp welcome; day 2 shows how to send the first SMS reminder; day 5 prompts adding a second doctor (activation event); falling bookings for 14 days trigger a check-in call; after a clinic's 500th booking, a referral invitation.

## Release checks

- All seven customer stages covered with trigger, owner and measure.
- Data, events, segments and platform specified in operations or data sections.
- Lifecycle messaging modelled as a conversion and retention lever in Section 10.
- Deliverability infrastructure budgeted and scheduled.
- Benchmarks from the business's own history.
- First-touch target in the service level.
- Team growth tied to ARR milestones.
