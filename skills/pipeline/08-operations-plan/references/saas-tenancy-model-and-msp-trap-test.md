Parent: [Operations Plan Skill](../SKILL.md)

When to read: when a plan uses the words platform, multi-tenant, cloud-native or SaaS, and the reader must judge whether the architecture supports SaaS economics, how tenancy maps to pricing tiers, and what the management layer, onboarding and per-tenant cost model require. Build-versus-buy and per-tenant infrastructure costing sit in `saas-build-vs-buy-and-infra-cost-model.md`.

# Is it really SaaS? Tenancy and operating-model test

This is the engine's test for whether a "SaaS" plan has SaaS economics or is a hosted-services business in disguise. It runs as five questions, each with evidence to demand and a consequence for the model. It draws on the architecture-to-business reasoning in Golding, T. (2024) *Building Multi-Tenant SaaS Architectures*, O'Reilly Media (the difference between SaaS and managed-service delivery, tenancy models and the control plane). The questions, tables, rules and examples are this engine's. Margin bands, engineering percentages and vendor names from the source are not used.

## Question 1 — Which delivery model is this, honestly?

| Model | What the plan describes | What happens to costs as customers grow |
|---|---|---|
| Installed software | Each customer runs its own copy and version, often on its premises | Support and operations grow in step with customers; margins erode |
| Hosted per customer (managed-service model) | Each customer has a dedicated environment run by a central team; customers choose when to upgrade | Version drift, manual onboarding per customer, slower innovation, few customers per engineer |
| SaaS | All customers on one version, run through shared operations | Low extra operating cost per new customer |

**Warning phrases** that signal the hosted-per-customer model: "on-premise option", "dedicated environment for each client", "clients choose when to upgrade", "we customise for each client". **Consequence:** either reclassify the plan (services-style margins and staffing in Section 10) or require a dated roadmap to true SaaS.

## Question 2 — Does it deliver what SaaS promises the business?

Demand evidence for each claim the plan relies on:

| Business claim | Evidence to ask for |
|---|---|
| Fast change (features, pricing, packaging, new segments) | Single codebase, release cadence, feature flags |
| One team runs all customers | One management view across tenants |
| Freed engineering time for differentiation | Operating effort per customer falling over time |
| Onboarding without manual work per customer | Self-service or automated provisioning |
| Room to grow without specialist teams | Capacity plan for a large increase in tenants |
| Known cost per customer | Per-tenant cost measurement (Question 5) |

Reject a multi-tenant claim that cannot evidence most of these.

## Question 3 — How are resources shared, and does pricing match?

Multi-tenancy means onboarding, deploying and operating all customers through one management layer, not merely sharing servers.

| Sharing model | Cost per tenant | Fits |
|---|---|---|
| Shared (pooled) compute and storage | Low | Entry and volume tiers |
| Dedicated (siloed) resources for compliance, security or performance | High | Premium or enterprise tiers, priced to cover the cost |
| Mixed: some services shared, some dedicated | Medium | Middle tiers, feature-based |

Map every Section 07 pricing tier to its sharing model. Where data-protection rules require in-country storage, a region-dedicated design may be needed; check current law per market (see the marketing orchestrator's location and scope calibration for East African data-protection entries).

## Question 4 — Is the management layer funded?

Separate the **management layer** (onboarding, identity, billing, metering, tenant administration, deployment, monitoring) from the **product features**. Early SaaS firms often spend nearly everything on features and then cannot onboard, bill or operate at scale. The plan shows a deliberate share of engineering for the management layer in the early years and says why.

Also specify:

- **Onboarding:** self-service sign-up, provisioning (database, identity, billing), configuration and the first-value moment; track time to first value, self-service versus assisted share and onboarding cost per customer. Where users lack a stable email address, design phone-number sign-in with one-time codes and fall-backs.
- **Heavy-user protection:** in shared environments one heavy customer can slow others; use per-tenant limits and throttling, tier-based isolation, autoscaling rules and per-tenant monitoring, and cost them for any premium service level.

## Question 5 — Is cost per customer measured?

Measure per tenant: compute, storage, API calls and data transfer, third-party costs (AI tokens, payment fees, SMS, mobile-money charges), support tickets and custom-work hours. Show gross margin by customer segment, not only in total. Where AI features exist, model AI cost per tenant per month and decide whether to pass it through, cap it or include it (`saas-ai-cost-of-tenant-calculator`). Record foreign-currency exposure for tools priced in dollars.

Across the tenant life (sign-up → onboarding → activation → paid → expansion → renewal → loss or return), show the conversion, the automation and the owning team in Sections 07 and 08.

**Illustrative example.** A Kigali pharmacy-stock "platform" gives each pharmacy chain its own server and lets chains delay upgrades. Result of the test: hosted-per-customer model; Section 10 margins reset to services levels; a twelve-month roadmap to a shared codebase with a dedicated tier priced for chains that need in-country data storage.

## Release checks

- Delivery model classified; warning phrases resolved or a migration roadmap dated.
- Business claims evidenced.
- Every pricing tier mapped to a sharing model.
- Management-layer engineering budgeted.
- Onboarding flow, time to first value and onboarding cost specified.
- Per-tenant cost measurement in the operating model, including AI cost where claimed.
- Build-versus-buy decisions recorded for identity, billing, monitoring, AI and payments, with currency exposure.
