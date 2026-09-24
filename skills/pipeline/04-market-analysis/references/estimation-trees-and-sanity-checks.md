# Estimation driver trees and sanity checks

Parent: [Market Analysis](../SKILL.md).

When to read: when a business plan, marketing plan or feasibility study needs
a market size, first-year volume or demand estimate and the data is thin.
Complements the fuller [market sizing methodology](market-sizing-methodology.md);
use this file for fast, transparent driver trees and the checks that stop
implausible numbers. Method sources: Lin, L. C. (2013) *Decode and Conquer*,
2nd edn, Impact Interview (estimation patterns); Croll, A. and Yoskovitz, B.
(2013) *Lean Analytics*, O'Reilly Media (dual-method divergence rule); Abrams,
R. M. (1993) *The Successful Business Plan*, The Oasis Press ("count and
discount"). All numbers below are illustrative.

## 1. Protocol

1. **Clarify scope:** geography (named at the level the business serves),
   period, unit (revenue or units; monthly or annual), and whether the answer
   is potential demand or expected sales.
2. **Announce the chain** of drivers before calculating.
3. **State each assumption and multiply as you go.** Write every step; never
   list assumptions and compute at the end.
4. Use ranges and a midpoint; round for tractable arithmetic.
5. Allow for peak and off-peak, new versus replacement buyers, and substitution.
6. **Estimate twice**, top-down and bottom-up. If the two differ widely, the
   model (usually a boundary or a unit) is wrong; explain the gap and plan on
   the lower, better-evidenced figure.
7. **Sanity-check** against a known reference (an operator's records, a
   supplier's volumes, a regulator's count) and explain any variance.
8. State the answer, its class (estimate), its biggest sensitivity and the
   evidence that would narrow it.

## 2. Driver-tree patterns

| Pattern | Chain | Good for |
|---|---|---|
| Per-outlet bottom-up | Customers per peak hour × items per customer × average price × peak hours ÷ peak share of daily revenue × trading days × outlets | Food stalls, shops, salons, clinics |
| Replacement cycle | Population in segment × ownership rate × replacement rate a year × category share × brand share | Durables, uniforms, school shoes, phones |
| Usage to load | Active users × sessions a week × actions per session ÷ seconds a week, × peak factor | Capacity planning for USSD, apps, call centres |
| Capacity | Peak arrivals per period and acceptable wait versus units served per cycle and cycle time | Transport, queues, service bays |
| New line or SKU | New households (or firms) a year × share needing the item × share buying through our channel × 1 ÷ comparable options listed × relative sell-through × unit contribution | Adding a product or service line |
| Account census (B2B) | Named organisations meeting the fit test (from registers) × likely buyers per organisation × annual spend × win rate | Captive B2B universes |

**Worked example (per-outlet, Kampala rolex stall):** peak hours 6–9 a.m. and
5–10 p.m. (8 hours); about 25 customers an hour × 1.2 items × UGX 2,500 ≈ UGX
75,000 an hour ≈ UGX 600,000 in peak; off-peak adds about 15% ≈ UGX 690,000 a
day. Cross-check with eggs used (trays a day × 30 ÷ eggs per item). Label as an
estimate; replace with observation counts.

## 3. Count, then discount

Observe directly where possible: count customers at different times of day,
time table turnover, count listings, count stalls. Then reduce the counts for
the plan's base case, because first-year businesses rarely match established
competitors' volumes.

## 4. Adoption check for first-year volumes

Year-one volume must be plausible against the share of the reachable market
that adopts early. If the forecast needs a large share of the served market in
year one for a new-to-market offer, it is almost certainly too high; reduce it
or show the evidence (pre-orders, contracts, pilot conversion). Different early
adopter groups often need different media and messages.

## 5. Market ladder

Name the denominator before sizing: potential market → available market (can
access and afford) → qualified available market (meets fit conditions) →
served market (deliberately targeted and reachable) → penetrated market
(already buying). Never present potential market as demand.

## 6. Anti-patterns

- A national population figure presented as the market. Fix: ladder down to the served market.
- One method only. Fix: top-down and bottom-up with the gap explained.
- Hidden arithmetic. Fix: show each multiplication with its assumption.
- No reference check. Fix: compare with an operator's or supplier's figures.
- Precise-looking outputs from rough inputs. Fix: ranges and a stated sensitivity.
