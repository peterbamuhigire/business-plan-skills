# Equity Term Sheets: Founder's Negotiation Reference

Use this reference when Section 11 (Funding Request) proposes equity, convertible or quasi-equity funding, and when the plan must show the founders understand the economics and control terms they are offering. It covers angel, seed and later rounds, and the East African investor landscape. The mechanics follow standard venture-finance practice (including Feld and Mendelson); the worked numbers are generic illustrations to be replaced with the plan's own model. Typical ranges (discounts, interest, fees, cheque sizes) are market conventions that change; verify with current deal data and with counsel. Verify company-law and tax treatment with local counsel and the Chwezi finance engine.

## 1. Economics and control

Every equity term sheet reduces to two things:
- Economics: the return investors receive in a sale, wind-down or listing, and all terms affecting it (valuation, liquidation preference, participation, anti-dilution, dividends, option pool).
- Control: the ability to direct or veto (board composition, protective provisions, drag-along, conversion terms).
Terms that affect neither are largely irrelevant; heavy negotiation time spent elsewhere signals inexperience or distraction. Founders hold common stock; investors usually hold preferred stock with special rights. Preferred can convert to common at any time, but not back.

## 2. Pre-money and post-money valuation

| Term | Definition |
|---|---|
| Pre-money | Value before the investment (negotiated) |
| Post-money | Pre-money + investment |
| Investor ownership | Investment / post-money |
Worked pattern: investment I, pre-money P, post-money P + I, investor share I / (P + I).
Trap: a statement such as "I will invest X at a valuation of V" often means V is post-money, so pre-money is V - X. Always confirm: "I assume you mean V pre-money."
Drivers of valuation (early stage is a judgement): stage; competition for the deal (multiple term sheets are the best leverage); team experience; market size and fashion; macro climate; financial numbers at later stages (revenue, EBITDA, burn, growth). See `business-valuation-methods.md`.

## 3. Option-pool effect on pre-money

The unissued employee option pool is counted in the pre-money, so a larger pool demanded by the investor lowers the effective pre-money.
Formula: effective pre-money = stated pre-money - value of the additional pool shares required (pool increase x post-money value).
Illustration: at a stated pre-money P with investment I, if the investor requires a post-round unissued pool of x% and the existing pool is y%, then the extra (x - y)% of post-money value comes out of P. Compute this in the model before agreeing.
Negotiation options: argue for a smaller pool backed by a hiring budget; accept a larger pool in return for a higher stated pre-money; ask for a post-money pool addition. Bring an option budget listing every planned hire and approximate grant size to the next financing.

## 4. Liquidation preference

Applies in any liquidation event (sale, merger, wind-down), not only bankruptcy. Two parts: the preference multiple (paid to preferred before common) and participation (whether preferred also shares in the remainder).
| Participation type | Meaning |
|---|---|
| Non-participating | Investor takes the preference or converts to common, not both |
| Fully participating | Takes the preference and shares pro rata as if converted |
| Capped participation | Participates until total return reaches a cap, then stops (or converts if better) |
Waterfall method (use in the model for each exit value E, investor share s, investment I, multiple m):
- Non-participating: investor gets the greater of m x I and s x E.
- Fully participating: m x I + s x (E - m x I).
- Capped at c x I: the lesser of the fully participating amount and c x I, or s x E if conversion pays more.
- Founders and common receive the remainder.
Test three exits (low, mid, high) for each structure. Participation matters most at mid-range exits; at high exits investors convert; below the preference, common gets nothing regardless.
Multiple rounds: stacked (later series paid first) versus blended or pari passu (shared pro rata by invested capital). Push for 1x non-participating; treat 2x or higher as a warning about investor character. Whatever structure is accepted in the first round sets the precedent.

## 5. Anti-dilution

Protects investors in a later lower-priced round by lowering the earlier preferred conversion price.
| Type | Effect |
|---|---|
| Full ratchet | Earlier price resets to the new lower price regardless of volume; very dilutive; rare outside distressed deals |
| Broad-based weighted average | Adjusts for size of the down-round issue; the usual standard |
Formula: NCP = OCP x (CSO + CSP) / (CSO + CSAP), where NCP is the new conversion price, OCP the old, CSO the common stock outstanding on a fully diluted basis (broad-based counts all convertible securities and options), CSP the shares the new money would buy at the old price, and CSAP the shares actually issued.
Standard carve-outs: option-pool shares; shares issued for non-cash consideration in acquisitions; equipment or bank financing shares; shares where a majority of preferred waives.
Position: accept broad-based weighted average; resist full ratchet; build value so a down round does not occur.

## 6. Cap table construction

A cap table shows ownership before and after each financing. Method for a round with a required post-round unissued pool:
1. Founders' shares F are known; they will equal (1 - investor share - pool share) of the post-round total.
2. Total post-round shares T = F / (1 - s - p), where s is the investor's post-money share and p the post-round pool percentage.
3. Investor shares = s x T; pool shares = p x T.
4. Price per share = investment / investor shares.
5. Check: (founder shares + pool shares) x price = pre-money.
Model post-investment ownership for every term-sheet scenario before accepting one. Each later round dilutes everyone pro rata; ungranted options fall away in effect on exit ("reverse dilution").
Converting notes: three methods differ in who bears dilution: pre-money method (founders and new investors share; pre-money fixed; the usual assumption); percentage-ownership method (founders bear all dilution; investor percentage fixed); dollars-invested method (post-money = pre-money + new money + note principal; a compromise). Confirm which the term sheet uses.

## 7. Founder vesting

Standard: four years with a one-year cliff (nothing vests before 12 months; 25% at the cliff; the rest monthly over 36 months). Vested fraction at leaving = months served / 48 after the cliff (for example 18 months gives 37.5%). Investors will impose vesting on founders who lack it; founders who started earlier can negotiate credit for time served. Vesting protects all founders against a co-founder leaving with a large stake and aligns incentives; treat it as team architecture, not just investor control.
Acceleration on acquisition: single trigger (acquisition alone vests everything; resisted because acquirers want retention); double trigger (acquisition plus termination without cause; the usual standard, often with a defined period of acceleration).

## 8. Shareholder rights

- Pro-rata (pre-emption) rights: investors may buy their share of future issues to maintain ownership. Expected; resist "super pro-rata"; define "major investor" to limit who holds the right.
- Drag-along: a majority class can compel all shareholders to vote for a sale. Variants: preferred drags common; departed-founder shares vote proportionally with the rest. Position: tie the trigger to a majority of common as well, so you can be dragged only if a majority of holders with equal rights agree.
- Tag-along (co-sale): if a founder sells to a third party, investors may join pro rata on the same terms; nearly impossible to remove; negotiate an exemption for small sales below a threshold.
- Information rights: accept standard periodic reporting.
- Registration rights: relevant only on listing; accept standard terms.

## 9. Convertible notes and SAFEs

A convertible note is debt that converts into equity at the next priced round, avoiding a valuation negotiation at seed.
| Term | Convention (verify) | Meaning |
|---|---|---|
| Discount | Commonly 10% to 30% | Conversion at a percentage below the next round price |
| Interest | Commonly mid single digits to low double digits | Annual interest on principal |
| Valuation cap | Negotiated | Maximum effective valuation at conversion |
| Maturity | Commonly 12 to 24 months | Date for conversion or repayment |
| Qualified financing | A minimum round size | Triggers automatic conversion |
Discount arithmetic: conversion price = round price x (1 - discount); shares = note amount / conversion price. Cap arithmetic: the conversion price is the lower of the discounted price and the cap price (cap / fully diluted pre-round shares).
New investors may treat the cap as a ceiling for their own price; keep note terms confidential until a new lead agrees a price.

| Note | Priced equity round |
|---|---|
| No up-front valuation negotiation | Valuation set immediately |
| Faster and cheaper | Thorough; preferred rights established |
| Defers price; may give a higher effective price | Clear ownership from day one |
| Maturity creates pressure if no round follows | No maturity risk |
| Debt rights give investors leverage in trouble | Only equity rights |

SAFE (simple agreement for future equity): a warrant-like instrument, not debt; no interest or maturity; may carry a cap, a discount and a most-favoured-nation clause (better terms given to later SAFE holders flow back). Compared with a note: no interest, no maturity, pro-rata right may be absent, equity treatment on the balance sheet, less investor leverage. Local counsel are often more familiar with equity rounds than SAFEs; convertible notes appear in accelerator contexts. Confirm counsel's experience with any instrument used, and confirm that the instrument is valid under local company law.

## 10. Board and protective provisions

Board: the board can dismiss the chief executive and approves budgets, option plans, financings and major spend. Typical early boards: three seats (founder or chief executive elected by common, investor elected by preferred, one independent by mutual consent) or five (two founders or chief executive plus founder, two investors, one independent). The independent director is the swing vote and mentor; independent directors often receive a small option grant vesting over several years (verify current norms). Limit board observers, who influence without accountability.
Protective provisions require investor consent for: changing preferred rights; changing authorised shares; creating equal or senior share classes; repurchasing common; selling the company or change of control; amending constitutional documents; changing board size; paying dividends; borrowing above a threshold; bankruptcy; licensing away intellectual property.
Positions: raise the debt threshold (most commonly accepted); use a single class vote across all preferred series; avoid consent thresholds far above a simple majority (a very high threshold lets a small holder block the company).

## 11. What to fight for and what to concede

| Fight hard | Target |
|---|---|
| Pre-money valuation | As high as justified by market data |
| Option pool size | Match the realistic hiring budget to the next round |
| Liquidation preference | 1x non-participating; resist full participation |
| Participation cap | A cap if participation cannot be avoided |
| Board composition | Balanced; not investor-controlled |
| Protective provisions | Single class vote; no series-by-series vetoes |
| Vesting credit | Credit for time served |
| Anti-dilution | Broad-based weighted average only |

| Concede gracefully | Note |
|---|---|
| Registration rights | Only matter at listing |
| Pro-rata right | Limit to major investors |
| Tag-along | Negotiate a small-sale floor |
| Non-cumulative dividends | Require board majority to declare |
| Information rights | Standard reporting is good practice |
| Drag-along | Can protect founders; tie to common majority |
Three objectives in negotiation: a good and fair result, an intact relationship, and full understanding of the deal.

## 12. The investment process and fund logic

Process: warm introductions beat cold outreach; involve a senior partner, not just an associate; diligence covers deck, model, team, pipeline and competition (an investor demanding long projections from a pre-revenue firm is not an early-stage investor); most decisions need partnership approval, so confirm it before granting exclusivity; a signed term sheet is not cash, but most deals close unless diligence finds material problems.
Fund logic: funds have a fixed life (commonly about ten years, with new investments mainly in the first half); management fee pays salaries and carried interest on profits is the real incentive; funds seek very high multiples on winners because most holdings fail; a fund late in its life is under pressure to produce liquidity, which shapes exit behaviour.
What they seek beyond numbers: team quality, market size able to return the fund's target multiple, defensible model, early traction, founder-market fit.
Leverage: run a competitive process, time investor conversations to converge, and do not name other investors until competing term sheets exist.

## 13. East African investor landscape (verify current status of each)

| Investor type | Typical instrument | Typical cheque (verify) |
|---|---|---|
| Angel networks | Equity or convertible note | Small |
| Accelerators | Equity for a small percentage | Small to medium |
| Impact investors | Preferred equity | Medium |
| Development finance institutions | Equity or quasi-equity | Medium to large |
| National development bank | Mainly debt, some equity windows | Local-currency range |
| Diaspora investors | Equity or SAFE | Small to medium |
Localisation:
- Most regional rounds use equity; confirm counsel can structure preferred shares under the Companies Act.
- Impact investors usually target lower exit multiples over longer periods than venture funds and offer lighter terms.
- Development finance institutions require audited accounts, environmental and social management compliance, board policies and quarterly reporting.
- The exit market is thin (limited M&A, no dedicated SME exchange), so liquidation preferences matter more and acquisition is the main exit path; plan buy-back or put mechanisms.

## 14. Ten checks before signing

1. Confirm pre- or post-money.
2. Compute the effective pre-money after the option pool.
3. Prefer 1x non-participating; resist full participation.
4. Remember the first-round structure sets the precedent.
5. Accept broad-based weighted average anti-dilution only.
6. Keep the board balanced with a truly independent director.
7. Accept vesting with credit for time served and double-trigger acceleration.
8. Treat notes as deferral, not elimination, of the price question; disclose cap terms only after price is agreed.
9. Use multiple term sheets as leverage without naming investors.
10. Treat the term sheet as the blueprint of the final agreements.

## 15. Plan-section prompts

- Amount sought, instrument, proposed pre-money and resulting ownership.
- Use of funds and milestones to the next round.
- Cap table before and after, with the option pool.
- Waterfall at low, mid and high exit values.
- Governance offered (board, reserved matters).
- Exit routes and time horizon.

Sources consulted: Feld and Mendelson, Venture Deals, 4th ed., Wiley, 2019 (structure and standard terms, adapted); local company-law guidance to be confirmed with counsel.
