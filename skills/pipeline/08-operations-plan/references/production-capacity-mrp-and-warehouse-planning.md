Parent: [Operations Plan Skill](../SKILL.md)

When to read: when the plan involves manufacturing, food or agro-processing, fabrication, assembly, packaging, recycling, warehousing, distribution, wholesale, cold chain, or material-inventory risk. Also used by financial projections and the food-processing and light-manufacturing industry guides.

# Production Capacity, MRP, and Warehouse Planning

This reference turns manufacturing, inventory, facilities, scheduling, and green-production practice into business-plan procedures. It paraphrases material from APICS operations and inventory course material; ASCM *CLTD* warehousing modules; Orlicky, J. *Material Requirements Planning*, McGraw-Hill; and supplied texts on facilities and material handling, production scheduling, and green-manufacturing simulation (confirm edition details before citing).

## 1. Operating-model questions

| Area | Question the plan must answer |
|---|---|
| Demand | What units must be produced, stored, picked, and delivered per week or month? |
| Materials | Which raw materials, packaging, spares, and consumables are critical, and what are their lead times? |
| Capacity | What is the bottleneck: work centre, machine, labour skill, or storage area? |
| Scheduling | How are batches sequenced, and what set-up or changeover time does that create? |
| Inventory | What safety stock, reorder point, lot size, and shelf-life rules apply? |
| Warehouse | Where are items received, stored, staged, picked, packed, and dispatched? |
| Quality | What is inspected on receipt, in process, and before dispatch? |
| Resource use | What are energy, water, yield, scrap, rework, and waste per unit? |

## 2. Material requirements and inventory policy

- **Gross requirement:** total material needed for the sales or production plan.
- **Net requirement:** gross requirement minus usable stock and confirmed incoming supply.
- **Safety stock:** buffer for demand variation, lead-time variation, supplier reliability, or yield risk.
- **Reorder point:** expected demand during lead time plus safety stock.
- **Lot sizing:** order quantities shaped by minimum order quantity, batch size, shelf life, transport cost, or cash limits.
- **Pegging:** traceability from each material purchase to the order, batch, or forecast it serves.

Template for each critical material:

```text
Critical material: [name]
Monthly consumption at target output: [quantity]
Supplier lead time: [days]
Safety stock policy: [days or quantity]
Reorder trigger: [quantity]
Minimum order quantity / batch size: [quantity]
Cash tied up in safety stock: [currency]
Consequence if delayed: [production stop / quality downgrade / late delivery]
```

## 3. Capacity and scheduling

Do not state only "we will produce X units a month". Show why the capacity is credible:

- rated output per machine or work centre;
- available shift hours after breaks, maintenance, cleaning, and set-up;
- standard set-up or changeover time;
- standard run time per unit or batch;
- expected yield and scrap allowance;
- availability of skilled labour;
- a planned utilisation below 100 per cent to protect quality and recovery time.

```text
Work centre / process: [name]
Rated output: [units per hour]
Available hours per month: [hours]
Set-up / changeover allowance: [hours per month]
Expected yield: [percentage]
Practical monthly capacity: [units]
Planned monthly volume: [units]
Utilisation: [percentage]
Bottleneck implication: [constraint and first relief action]
```

## 4. Warehouse and material handling

Cover receiving, inspection, quarantine, storage zones, bin logic, forward-pick stock, packing, dispatch staging, returns, aisle access, pallet and racking needs, cold-store separation, and expansion space. Justify layout by material flow, not rent alone: reduce unnecessary movement, waiting, double handling, congestion, and spoilage.

## 5. Quality and traceability

Incoming inspection; batch or lot numbers; expiry and shelf-life tracking; first-expiry-first-out where relevant; in-process checks; final inspection and release; non-conformance handling; recall and corrective-action procedure; record retention for buyers, regulators, and lenders. Check current product-standard and food-safety requirements with the national standards body before stating them.

## 6. Resource-efficiency measures

| Measure | Formula |
|---|---|
| Energy intensity | kWh used ÷ saleable units |
| Water intensity | litres used ÷ saleable units |
| Material yield | saleable output ÷ material input |
| Scrap rate | scrap quantity ÷ material input |
| Rework rate | reworked quantity ÷ total output |
| Waste cost | disposal cost + lost material value + rework labour |
| Circular recovery | recovered by-product value ÷ total input value |

Link each measure to money: less waste raises gross margin, less energy improves cash flow, better yield reduces working-capital pressure.

## 7. Financial-model links

Explicit assumptions for raw-material cost, inventory days, labour and overtime, maintenance, power, fuel, water, waste disposal, compliance, yield loss, scrap, rework, packaging, production ramp-up, and capital expenditure by production stage.

## 8. Risk links

Supplier lead-time failure; single-source materials; raw-material price volatility; power or water interruption; equipment breakdown; cold-chain failure; quality rejection or recall; warehouse congestion; stock inaccuracy; expiry; environmental-permit failure; waste-disposal failure.

## 9. Review checklist

- [ ] The sales forecast fits production and warehouse capacity.
- [ ] The cash-flow model includes stock build-up before revenue.
- [ ] The capex schedule matches the implementation timeline.
- [ ] Critical inputs are tied to supplier or procurement assumptions.
- [ ] Quality and traceability controls are specific enough for buyers and regulators.
- [ ] Energy, water, waste, and yield improvements are expressed in operating and financial terms.
- [ ] The bottleneck and its first relief action are named.
