# Google Ads: Search Intent, Campaign Structure, and Optimisation Frameworks

**Source:** Geddes, B. — Advanced Google AdWords, 3rd Edition (Wiley/Sybex, 2014) | **Application:** Google Search Ads strategy, keyword research, Quality Score, landing pages, campaign structure, bidding, ad copy

> Google Search Ads are the only advertising medium in which you reach customers at the exact moment they are expressing intent to buy. A searcher typing "plumber in Kampala" is not passively watching content — they are raising their hand and saying: "Sell to me." Your job is to be the most relevant, most credible answer to that request.

## The Psychology of Search: Why Google Ads Are Different

Every other advertising medium interrupts. Google Search Ads assist. This is the fundamental distinction that determines how you write ads, choose keywords, and design landing pages.

**The search process (Geddes):**
1. A person has a question, problem, or desire
2. They translate it into words and type it into Google
3. They scan results with pre-set expectations about what they will find
4. Your ad has 2–3 seconds to signal: "I have the answer to your question"
5. If your ad matches their expectation, they click
6. Your landing page must then deliver on the ad's promise

**Goal alignment — three parties in every search (Geddes):**

| Party | Goal |
|-------|------|
| **Searcher** | Find the answer to their question quickly and accurately |
| **Google** | Ensure the searcher always finds their answer on Google (drives repeat searches = ad revenue) |
| **Advertiser** | Show a relevant ad that converts the searcher into a customer at a profitable CPA |

**The key insight:** Google's interests align with the searcher, not the advertiser. Ads that serve the searcher (relevant, clear, helpful) are rewarded with higher positions at lower costs. Ads that ignore the searcher's intent are penalised with higher first-page bids and lower ad positions.

**Implication for business plan:** Google Ads strategy must be searcher-first. Write ads to answer the customer's question, not to broadcast your brand. Every element — keyword, ad copy, landing page — must continue the conversation the customer started.

---

## The Buying Funnel: Matching Keywords to Customer Intent

Keywords are not just search terms — they are signals of where a customer sits in their buying journey. Matching keyword strategy to buying stage increases conversion rates and reduces wasted spend (Geddes):

| Buying Stage | Customer Mindset | Example Keywords | Ad Approach | Landing Page |
|-------------|-----------------|-----------------|-------------|-------------|
| **Awareness** | "I have a problem — what are my options?" | "what is solar power", "types of water filters" | Educational; build awareness; broad keywords | Blog post, guide, explainer page |
| **Consideration** | "I'm comparing specific solutions" | "best water filter Uganda", "solar vs generator comparison" | Benefits-focused; differentiation; feature comparisons | Product/service comparison page |
| **Purchase** | "I'm ready to buy — where/from whom?" | "buy water filter Kampala", "solar installation near me" | Direct offer; price/location; urgency | Dedicated landing page with clear CTA |
| **Loyalty** | "I'm an existing customer needing support or repurchase" | "filter replacement", "[brand] customer service" | Retention-focused | Account/support page |

**EA keyword examples by stage:**

| Business | Awareness Keywords | Consideration Keywords | Purchase Keywords |
|---------|-------------------|----------------------|-----------------|
| Restaurant | "restaurants in Kampala" | "best rooftop restaurant Kampala" | "book table Kampala restaurant" |
| Cleaning service | "how to clean offices professionally" | "office cleaning companies Uganda" | "office cleaning service Kampala quote" |
| Solar installer | "solar power for homes" | "solar system prices Uganda" | "solar installation Kampala" |

**Rule:** Campaign budgets should weight heavily toward purchase-intent keywords. These have the highest conversion rates. Use awareness keywords only if budget allows, and only with content-driven landing pages.

---

## Keyword Match Types

Match types control which search queries trigger your ad. Getting this wrong means paying for irrelevant clicks (Geddes):

| Match Type | Syntax | What Triggers the Ad | Example Keyword | Triggered By |
|-----------|--------|---------------------|----------------|-------------|
| **Broad Match** | keyword | Any variation, synonym, related topic Google considers relevant | water filter | "clean water solutions", "home purification" (broad) |
| **Phrase Match** | "keyword" | The phrase in order, with possible additional words before or after | "water filter" | "buy water filter", "water filter Kampala", "affordable water filter" |
| **Exact Match** | [keyword] | Precisely that query (and very close variants) | [water filter Kampala] | "water filter Kampala", "water filters Kampala" |
| **Negative Match** | -keyword | Prevents ad from showing when this word appears | -free | Excludes searches containing "free" |

**Bidding hierarchy (Geddes' guideline):**
- Bid Exact Match at your target CPC
- Bid Phrase Match at 15% less than Exact
- Bid Broad Match at 15–25% less than Phrase

**Negative keywords are essential (Geddes):** Without negatives, broad and phrase match waste budget on irrelevant searches. A cleaning company would add negatives like: -free, -jobs, -training, -diy, -how to. Expect to add 20–50 negatives before a campaign is profitable.

**When negative keywords improve performance:**
- Conversion rate increases (only relevant searchers see the ad)
- Cost per conversion decreases (fewer wasted clicks)
- Click-through rate increases (ad shown only in relevant contexts)

**Match type strategy for EA SMEs starting out:** Begin with Phrase Match and Exact Match only. Add Broad Match only once the campaign is profitable and you want to discover new keyword ideas via the Search Terms report.

---

## Quality Score: The Most Important Number in Your Account

Quality Score (1–10) is Google's assessment of how relevant your keyword, ad copy, and landing page are to the searcher's query. It directly controls your ad cost and position.

**Ad Rank formula:**
```
Ad Rank = Quality Score × Maximum Bid
```

A competitor with Quality Score 8 bidding UGX 1,500 outranks you bidding UGX 3,000 at Quality Score 3. **Quality Score is how you beat larger competitors without outspending them.**

**Quality Score factors (Geddes):**

| Factor | Weight | How to Improve |
|--------|--------|---------------|
| **Click-through Rate (CTR)** | Highest | Write compelling ad copy; improve ad relevance to keyword |
| **Ad relevance to keyword** | High | Use tightly themed ad groups; include keyword in ad headline |
| **Landing page relevance** | High | Landing page must answer the ad's promise; topically aligned |
| **Landing page quality** | Medium | User experience: fast load, mobile-friendly, no pop-ups, clear navigation |
| **Historical account performance** | Medium | Well-managed accounts with good QS history are rewarded |

**Quality Score scale interpretation:**
- 1–3: Poor — your ads will rarely show, or only at very high bids; fix immediately
- 4–6: Average — acceptable but leaving money on the table; optimise
- 7–9: Good — competitive position; maintain and improve incrementally
- 10: Excellent — maximum discount on CPCs; highest ad positions for lowest cost

**Practical QS improvement workflow (Geddes):**
1. Export keyword list with Quality Scores into a spreadsheet
2. Sort by Quality Score ascending — lowest scores cost you the most
3. For QS 1–3: split keywords into more specific ad groups with tighter ad copy
4. For QS 4–6: rewrite ads to include exact keyword in headline; improve landing page
5. For QS 7+: maintain; focus effort elsewhere

---

## Campaign Structure: The Foundation of Account Performance

**The Account hierarchy:**
```
ACCOUNT
  └── CAMPAIGN (budget, geographic targeting, network, schedule)
        └── AD GROUP (theme = one topic; contains related keywords)
              ├── KEYWORDS (positive + negative)
              └── ADS (2–3 ads per ad group for testing)
```

**The Ad Group is the critical unit (Geddes):** Each ad group should represent one specific topic or product. All keywords within the ad group should be closely related so that one ad can be highly relevant to all of them.

**Tight ad group example (correct):**
- Ad Group: "Office Cleaning Kampala"
- Keywords: [office cleaning Kampala], "office cleaning Kampala", "commercial cleaning Kampala"
- Ad: "Professional Office Cleaning in Kampala — Daily, Weekly, Monthly Plans. Free Quote Today."
- Landing page: page specifically about office cleaning services in Kampala

**Loose ad group (incorrect):**
- Ad Group: "Cleaning"
- Keywords: office cleaning, home cleaning, carpet cleaning, window cleaning, school cleaning
- Ad: "Professional Cleaning Services — Call Us Today"
- Problem: One ad cannot be highly relevant to all five different search intents

**Campaign segmentation strategies (Geddes):**
- By product/service type: separate campaigns per major offering
- By geography: separate campaigns per city/region if pricing or demand differs
- By match type: Exact Match campaign (controlled) vs Broad Match campaign (discovery)
- By funnel stage: Purchase-intent campaign (high bid) vs Awareness campaign (low bid)
- By device: Mobile campaign (shorter CTAs, click-to-call) vs Desktop campaign

**EA campaign structure example — cleaning company:**
```
Campaign 1: Office Cleaning — Kampala (Exact/Phrase; budget: UGX 80,000/day)
  Ad Group 1: Office Cleaning Kampala
  Ad Group 2: Commercial Cleaning Kampala
  Ad Group 3: Corporate Cleaning Services

Campaign 2: Home Cleaning — Kampala (Exact/Phrase; budget: UGX 40,000/day)
  Ad Group 1: House Cleaning Kampala
  Ad Group 2: Domestic Cleaning Services

Campaign 3: Branded (company name keywords; budget: UGX 20,000/day)
  Ad Group 1: [Company Name] variations
```

---

## Writing Ad Copy That Converts

**The ad's job:** Signal to the searcher — in 130 characters or fewer — that you have the answer to their question, and that clicking your ad will deliver it.

**Ad copy elements (Google Ads expanded text / responsive search ad):**
- **Headline 1:** Include the main keyword; answer the search query directly
- **Headline 2:** Your unique selling proposition or key benefit
- **Headline 3:** Call to action or offer (Free Quote, Order Online, Call Now)
- **Description 1:** Expand on the benefit; address the buying stage (features for consideration; price/urgency for purchase)
- **Description 2:** Social proof, trust signal, or secondary offer

**USP development (Geddes):** Every ad must communicate one reason why the searcher should choose you over every other ad on the page. Generic ads ("Quality Service — Call Us") are invisible. Specific USPs ("1-Hour Response — 200+ Kampala Clients — Free Quote") win.

**Features vs benefits (Geddes):**
- Features describe what the product is: "5,000-litre storage tank", "ISO-certified cleaning products"
- Benefits describe what it does for the customer: "Never run out of water", "Safe for your family and pets"
- Match to buying stage: features for comparison-stage searchers; benefits for awareness-stage; both for purchase-stage

**Ad writing best practices (Geddes):**
- Match ad copy tightly to the keyword that triggered it
- Use sentence case or Title Case (not ALL CAPS — disapproved)
- Include the geographic location in ads for local businesses
- Add a price or offer if competitive (reduces unqualified clicks)
- Include a clear, specific CTA: "Get Free Quote", "Call Now", "Order Today", "Book Online"
- Avoid jargon for awareness-stage keywords; use it for expert/purchase-stage keywords
- Test 2–3 ads per ad group; rotate to find the highest-converting version

---

## Landing Pages: The Make-or-Break Element

**The landing page must continue the conversation the ad started (Geddes):**
> "Your ad copy is the only information the searcher has about your website before clicking. Your landing page must immediately confirm that they made the right choice in clicking."

If the searcher lands on a page that does not match their expectation set by the ad, they click the Back button. You paid for the click; they leave with nothing.

**Landing page requirements (Geddes):**
1. **Relevance:** Page content must directly address the search query and ad headline. If the ad said "Office Cleaning Kampala", the landing page must be about office cleaning in Kampala — not a generic homepage.
2. **Transparency:** Any claim made in the ad (free quote, same-day service, certified) must be substantiated on the landing page.
3. **Navigability:** Provide links to Home, About, Contact, and relevant product pages. Searchers who do not convert immediately should be able to explore.
4. **Speed:** Google measures landing page load speed. Pages loading in 5+ seconds on mobile lose both Quality Score and conversions.
5. **Mobile optimisation:** All EA traffic is predominantly mobile. Landing pages must display correctly on Android smartphones at all screen sizes.
6. **No intrusive pop-ups:** Exit pop-ups and load pop-ups are a policy violation and reduce Quality Score.
7. **Clear single CTA:** Every landing page must have one primary call to action (fill in form / call this number / send WhatsApp message).

**Landing page ≠ Homepage:** The homepage is for people who already know your business. Searchers arrive with a specific question. Send them to the page that answers that specific question directly.

**EA landing page considerations:**
- WhatsApp CTA button is more effective than a contact form for many EA businesses (instant response, familiar channel)
- Mobile money payment integration on landing pages for direct purchase journeys
- Page must load in under 3 seconds on 3G/4G (compress images; avoid heavy JavaScript)

---

## Bidding Strategy

**Cost Per Click (CPC) — the default starting point:**
- You pay only when someone clicks your ad; impressions are free
- Set a Maximum CPC per keyword — the most you are willing to pay per click
- Actual CPC charged is typically lower (1 cent above the next-highest bidder's Ad Rank ÷ your QS)

**Bidding options progression (Geddes):**

| Bidding Type | How It Works | When to Use |
|-------------|-------------|-------------|
| **Manual CPC** | You set bids per keyword | Starting out; learning which keywords convert |
| **Enhanced CPC** | Google adjusts your manual bids up or down based on conversion likelihood | Once you have 30+ conversions in the account |
| **Target CPA** | Google optimises all bids to achieve a target cost per conversion | Once you have 50+ conversions/month |
| **Maximise Conversions** | Google spends your budget to maximise total conversions | Once conversion tracking is solid |
| **Target ROAS** | Google optimises toward a revenue return target | eCommerce with variable product prices |

**Starting recommendation for EA SMEs:** Use Manual CPC for the first 30–60 days. This teaches you which keywords, ads, and times of day actually convert. Switch to Target CPA only after accumulating sufficient conversion data.

**Impression Share — diagnosing visibility problems (Geddes):**
- **Search Impression Share** = % of eligible impressions your ads actually received
- Below 60%: you are not showing often enough; either raise bids or improve Quality Score
- **Lost IS (Budget)**: ads not shown because daily budget was exhausted → raise budget or lower bids
- **Lost IS (Rank)**: ads not shown because Quality Score or bid too low → improve QS or raise bids

---

## Conversion Tracking: Non-Negotiable

**Without conversion tracking, you are flying blind (Geddes):** You cannot know which keywords, ads, or landing pages generate actual customers. You can only see clicks and costs — never enough to optimise.

**Conversions to track for EA businesses:**
- Phone call click (click-to-call button)
- WhatsApp button click (tracked as a goal in Google Analytics 4)
- Form submission / enquiry form
- Product purchase (eCommerce)
- Direction request (Google Maps)
- Email click

**GA4 + Google Ads integration:** Link Google Analytics 4 to Google Ads. Import GA4 conversion events as Google Ads conversions. This enables bidding strategies (Target CPA) and full attribution reporting.

---

## Google Ads vs Google Business Profile: Critical Distinction

Many EA businesses confuse these two Google products:

| Feature | Google Business Profile (GBP) | Google Search Ads |
|---------|-------------------------------|------------------|
| **Cost** | Free | Pay per click |
| **Placement** | Google Maps + "near me" searches | Top of Google Search results |
| **Control** | Limited (photos, reviews, hours, posts) | Full creative control |
| **When shown** | When Google determines local intent | When your keywords match |
| **Best for** | Local discovery; building credibility | Targeted, immediate customer acquisition |
| **Setup priority** | First — do this before running any ads | Second — complements GBP |

**EA priority order:**
1. Claim and optimise Google Business Profile (free; highest-impact for local search)
2. Generate Google reviews (ranking signal for both Maps and Ads)
3. Launch Google Search Ads targeting purchase-intent keywords in your city

---

## Dynamic Keyword Insertion (Advanced)

When your ad contains `{KeyWord:Default Text}`, Google automatically inserts the triggering keyword into the ad headline. This increases ad relevance to the search query, improving CTR and Quality Score.

**Example:** Keyword in account = "water filter", searcher types "ceramic water filter Kampala", ad headline becomes "Ceramic Water Filter Kampala" automatically.

**Use with caution:** Only in tightly themed ad groups where the inserted keyword will always make grammatical sense and is appropriate for all keyword variations in the group.

---

## Google Ads Budget Framework for EA SMEs

| Budget Tier | Daily Spend | Monthly | What to Expect |
|------------|-----------|---------|---------------|
| **Testing (seed)** | UGX 25,000–50,000 ($7–$14) | UGX 750,000–1.5M | Data collection; identify converting keywords; not yet optimised |
| **Growth** | UGX 75,000–150,000 ($20–$40) | UGX 2.3M–4.5M | Enough data to optimise; expect first profitable conversions |
| **Scaling** | UGX 200,000–500,000 ($55–$135) | UGX 6M–15M | Target CPA bidding; proven campaign; scale profitably |

**EA cost-per-click benchmarks (estimates for Uganda, 2026):**
- Local services (cleaning, plumbing, construction): UGX 1,500–5,000/click
- Food and restaurant: UGX 500–2,000/click
- Professional services (accounting, legal, consulting): UGX 3,000–10,000/click
- Retail / eCommerce: UGX 800–3,000/click

*Note: CPC varies by competition level and Quality Score. Higher Quality Score = lower actual CPC for the same position.*

---

## Search Terms Report: The Most Valuable Report in Google Ads

The Search Terms report shows the actual search queries that triggered your ads — not just the keywords you bid on. This reveals:
- Winning queries to add as exact match keywords
- Irrelevant queries to add as negatives
- New keyword ideas you had not considered
- Insights into how customers actually describe their problem

**Weekly optimisation routine:**
1. Check Search Terms report — add performing queries as keywords; add irrelevant terms as negatives
2. Review Quality Scores by keyword — identify QS 1–5 keywords for ad group restructuring
3. Check Impression Share — identify budget or rank issues
4. Review ad performance — pause the lowest CTR ad in each ad group; test a replacement
5. Check conversion data — adjust bids based on which keywords actually convert

---

## Source Notes

- Geddes, B. (2014) *Advanced Google AdWords*, 3rd Edition. Indianapolis, IN: Wiley/Sybex.
- Note: Google Ads interface has evolved significantly since 2014 (Google rebranded AdWords to Google Ads in 2018; expanded text ads replaced by responsive search ads; Smart Bidding automated strategies improved). Core principles of Quality Score, buying funnel matching, keyword structure, landing page quality, and ad copy relevance remain unchanged and are confirmed by current Google Ads documentation.
- EA-specific budget figures, UGX conversions, and local applications are this project's additions.
- For current Google Ads interface guidance, refer to Google Ads Help Centre (support.google.com/google-ads).
