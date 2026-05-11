---
source: Wes Bush (ProductLed Growth), OpenView PLG benchmarks, Reforge, Bessemer
frameworks: [PLG suitability test; PLG funnel; PLG-to-Enterprise transition; PLG cost economics]
skill: saas-gtm-motion-design
cross-reference: [saas-pricing-and-packaging-strategy, saas-mvp-and-product-market-fit-strategy, 07-marketing-sales-strategy]
---

# SaaS Product-Led Growth Business Case

## 1. The PLG Suitability Test

PLG is suitable only if ALL of the following are true:

1. **Time-to-value < 10 minutes** — new user reaches a useful outcome in their first session
2. **Self-service onboarding** — no human required; sign-up → use → upgrade flows without sales touch
3. **Bottoms-up adoption pattern** — individual / team can adopt without enterprise procurement
4. **Viral or share-friendly architecture** — single user spreads to colleagues / customers naturally (Loom share links; Calendly meeting URLs; Figma invites)
5. **Low support cost per free user** — infra and support cost <$1 per free user per month

If any fail, the business needs sales-assisted GTM. Or hybrid (PLG-to-Enterprise dual funnel).

## 2. PLG Funnel Economics

```
                                  Volume        Conversion       Result
                                  -----------   -----------      -----------
Anonymous traffic                 1,000,000     —                website visits / mo
Sign-ups                          50,000        5%               free signups
Activated users                   25,000        50%              reached first value
Paid conversion                   1,500         6% of activated   monthly paying customers
Annual upgrade / expansion        300           20% of paid       higher-tier annual contracts
Enterprise upsell                 30            10% of expanded   enterprise contracts (via sales)
```

Key levers:
- **Sign-up rate** (visit → free user): driven by clear value proposition, low friction, transparent pricing
- **Activation rate** (free user → activated): driven by onboarding design, first-value speed, in-product education
- **Paid conversion** (activated → paid): driven by paywall design, feature-gating, usage limits, in-product upgrade prompts
- **Expansion** (paid → higher tier): driven by usage growth, team expansion, module adoption
- **Enterprise** (PLG → sales-assisted): driven by usage signals (team-size, security needs)

## 3. PLG Investment Requirements

PLG looks cheap but requires significant investment:

| Component | Investment |
|---|---|
| Product design / UX | Significantly more than sales-led product (UX is the sales rep) |
| Onboarding design | Dedicated PM + designer for onboarding |
| In-product analytics | Mixpanel / Amplitude / Heap from day 1 |
| Lifecycle automation | Customer.io / Iterable / Vero from day 1 |
| Self-service infrastructure | Stripe / Paystack / Chargebee billing automation |
| Free-tier infrastructure | Cloud + AI cost for free users |
| Help centre + docs | Comprehensive self-service support |
| Community | Slack / Discord / WhatsApp community management |
| Brand / content | High-volume content engine to drive top of funnel |

PLG companies (HubSpot, Atlassian, Slack, Notion, Calendly) spend 25-40% of revenue on R&D — higher than sales-led — because the product IS the sales motion.

## 4. PLG-to-Enterprise Transition (Dual Funnel)

Most mature PLG companies eventually add sales-assisted enterprise motion. The transition triggers:

- Usage signals: team size > 20, multiple admins, integration with enterprise systems
- Security signals: SSO / SAML requests, security questionnaires
- Compliance signals: requests for SOC2, ISO27001, data-residency
- Contract signals: requests for MSA, custom terms, annual prepay

When triggered: hand off from self-serve to AE-assisted close. The free + paid PLG users in the org become the AE's internal champions.

## 5. PLG Pricing Architecture

Compatible pricing structures:
- **Freemium tier** (genuine value; limits drive upgrade)
- **Paid tiers** transparent on website
- **Usage-based scaling** for natural expansion
- **Enterprise tier** "Contact us" — opens the sales-assisted door

Incompatible:
- Custom pricing on every tier (PLG requires transparency)
- Sales-only pricing (defeats the self-serve promise)
- Free trial with mandatory credit card (high friction for PLG; ok for trial-led)

## 6. PLG Common Failure Modes

- Building PLG product but having sales-led pricing (transparency mismatch)
- Insufficient onboarding investment (users don't activate)
- Free tier too restrictive (no genuine value)
- Free tier too generous (no upgrade trigger)
- Infrastructure cost per free user too high (margin destruction)
- Premature enterprise sales hire (PLG hasn't proven first)

## 7. Living-Plan Cadence (PLG-specific)

| Element | Cadence | Owner |
|---|---|---|
| Activation rate dashboard | Daily | Head of Product / Growth |
| Free-to-paid conversion | Weekly | Head of Growth |
| Cohort retention by acquisition source | Monthly | Head of Product + CFO |
| Free-tier infra cost per user | Monthly | CTO + CFO |
| In-product experiment results | Weekly | Head of Growth |
| PLG-to-Enterprise transition signal review | Monthly | Head of GTM |

## 8. Africa / Uganda Application Notes

- **PLG works less well for African vertical SaaS** because:
  - Time-to-value often requires onboarding help (lower digital literacy in some segments)
  - Local-language UX may be required from day 1 (raises onboarding investment)
  - Mobile-money / payment-rail integration adds onboarding friction
  - In-person / relational selling norm makes self-service harder culturally
- **PLG works well for African SaaS targeting:**
  - Tech-savvy professional segment (developer tools, marketing tools, design tools)
  - International / diaspora buyers
  - B2C / freelancer markets
- **Hybrid models** (PLG free tier + sales for SMB+) are increasingly common
- **WhatsApp-assisted PLG** is a hybrid pattern: PLG signup + WhatsApp Business assist for the first 7 days. Reduces drop-off; preserves self-serve economics.
- **Mobile-money payment friction** is a PLG hurdle — design tap-to-pay flows; pre-load card via SDK; support multiple rails.
- **Community-led growth** is more important than US PLG benchmarks suggest — sector WhatsApp / Telegram groups are the African equivalent of Slack communities.
