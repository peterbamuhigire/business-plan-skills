# Restaurant Cost Controls (Advanced): Pricing, Portions, Inventory, Break-Even, Menu Engineering, Tracking

Task reference for menu pricing, purchasing, break-even and monitoring sections of a restaurant plan. Core formulas and cost determination are in `cost-controls.md`.

Any figures are planning assumptions; re-verify against dated local prices. Tax and inventory-valuation policy: verify with the Chwezi finance engine.

## 1. Menu pricing

Three approaches:
1. Match competitors. Quick, but ignores your own cost structure; use only as a cross-check.
2. Cost-based:
   - Target cost percentage: `price = portion cost / target cost %`.
   - Menu pre-cost: set tentative prices, forecast volumes, compute projected cost %, adjust prices or portions until acceptable.
   - Target food cost % = 100% - profit % - fixed cost % - labour cost %.
3. Contribution margin: average contribution margin = (sales - cost of sales) / customers; `price = portion cost + average contribution margin`.

Inflation adjustment for future bookings: apply the pro-rata share of expected annual inflation to current cost, then divide by the target cost %; round to a sensible price point.

Menu layout: place items you most want sold in the prime reading positions (top third of a one-page menu, top centre of the right-hand page of a two-page menu, centre of a three-page menu).

## 2. Portion control and standard recipes

```
Standard portion cost = purchase price per unit / portions per unit
Recipe cost = sum(ingredient quantity x unit cost); portion cost = recipe cost / portions
Selling price = portion cost / desired cost %
```

Butcher test (portioned before cooking):
```
Yield % = usable weight / purchased weight
Usable value = total cost - value of secondary parts (trim, tips)
Cost per usable unit weight = usable value / usable weight
Portion cost = portion size x cost per usable unit weight
```

Cost factors for fast repricing when supplier prices move:
```
Cost factor per unit weight = cost per usable unit weight / purchase price per unit weight
Portion cost = cost factor x portion size x current supplier price
```

Cooking-loss test (portioned after cooking): record raw, trimmed, cooked and salable weights; cost per salable unit weight = original cost / salable weight.

Quantity planning:
```
Quantity to buy = (portions x portion size) / yield %
Portions obtainable = (quantity x yield %) / portion size
```

Run these tests for each protein and high-loss produce item and record results on the recipe card.

## 3. Purchasing and inventory

Valuation methods: actual purchase price (most accurate, needs marking); first-in first-out; weighted average; latest purchase price (simple, common in food service); last-in first-out (lowers reported profit; check local acceptability). Method choice can change inventory value by several per cent, so state the method in the plan.

```
Average inventory = (opening + closing) / 2
Inventory turnover = cost of food sold / average inventory
Book closing = opening + purchases - issues
Variance % = (book value - physical value) / total issues x 100
```

Guide: turnover of roughly two to four times a month (24-48 a year) suggests healthy stock levels for perishables-led operations; test locally. Investigate any material variance.

## 4. Break-even analysis

```
Sales = variable cost + fixed cost + profit
Variable rate = variable cost / sales
Contribution rate = 1 - variable rate
Item contribution margin = price - item variable cost
Break-even sales = fixed costs / contribution rate
Required sales = (fixed costs + desired profit) / contribution rate
Break-even customers = fixed costs / (average sale x contribution rate)
```

Present break-even for the base case and for a downside case (lower average check, higher food cost).

## 5. Menu engineering (Kasavana and Smith)

Classify each item by contribution margin (CM) against the menu average and by popularity (menu mix %) against a threshold of (1 / number of items) x 70%.

| Class | CM | Popularity | Action |
|---|---|---|---|
| Star | high | high | Keep unchanged; consider a price rise |
| Plowhorse | low | high | Keep; raise CM through price, portion or recipe |
| Puzzle | high | low | Keep; promote, reposition, rename |
| Dog | low | low | Remove or redesign |

Re-run monthly. Success test: average CM and total CM rise while food cost % stays flat or falls.

## 6. Daily, weekly and monthly tracking

```
Daily cost of food sold = directs + stores issues
  + adjustments that raise cost (transfers in from bar)
  - adjustments that lower cost (transfers out, staff sales, promotions)
  - employee meals
Daily food cost % = daily cost / daily food sales x 100
Cumulative % = total cost to date / total sales to date x 100
```

Cumulative tracking smooths timing distortions from directs bought on alternate days and stores issued in advance. Report formats: a cumulative sheet (directs, stores, additions, subtractions, cost and sales for today and to date, cost % both ways) and a management view comparing today with the same day last week and week to date with last week.

Frequency: daily food and beverage cost %; weekly comparison with the prior week; monthly cost %, inventory turnover and comparison with last month, the same month last year and budget. Reconcile book inventory with physical counts monthly.

## 7. Plan-section prompts

- State target cost percentages and how each menu price is derived.
- State yield-test and recipe-card procedure and who owns it.
- Show break-even sales and customers per day.
- State inventory valuation method and stock-count frequency.

Sources consulted: Dittmer, P.R. and Keefe, J.D., *Principles of Food, Beverage, and Labor Cost Controls*, 9th ed. (2009); Kasavana, M. and Smith, D., menu engineering method.
