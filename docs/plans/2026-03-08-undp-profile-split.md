# UNDP Profile Split & Standardisation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Split 200 consolidated UNDP business profiles into individual reference files with a standardised format across all 10 industry guides.

**Architecture:** Each `undp-business-profiles.md` file gets split into individual `undp-{kebab-name}.md` files in the same `references/` directory. The original consolidated file is renamed to `undp-business-profiles-consolidated.md` for traceability. All profiles adopt a single vertical-table format.

**Tech Stack:** Markdown files only — no code involved.

---

## Standardised Template

Every individual profile file MUST use this exact structure:

```markdown
# {Business Name}

**UNDP Ref:** #{number} | **Sub-sector:** {category}
**Source:** UNDP Uganda Compendium Vol. 2 (adjusted to March 2026 USD, ×1.27)

> {One-line description}

## Financial Summary

| Metric | Amount |
|--------|--------|
| Capital Investment | ${X} |
| Annual Revenue | ${X} |
| Annual Operating Costs | ${X} |
| Annual Profit | ${X} |
| Profit Margin | X% |
| Payback Period | {X} |

## Operations

- **Production Capacity:** {capacity with units and timeframe}
- **Key Equipment:** {comma-separated list}

## Market

{Market description — 1-3 sentences covering target customers, demand drivers, and competitive context}

## Data Quality Notes

{Only include this section if there are source inconsistencies or flags. Otherwise omit entirely.}
```

### Template Rules

1. **Financial Summary table** — always use vertical format with `| Metric | Amount |` headers
2. **Omit rows** where data is genuinely unavailable (use "N/A" only when the source explicitly states a figure but it's unclear)
3. **Currency** — use `$` prefix (all figures are already March 2026 USD estimates)
4. **Payback Period** — include in Financial Summary table if available; omit the row if not
5. **UNDP Ref number** — use from source where available (chemicals, construction, textiles, livestock formats have `#number`); for food-processing profiles that lack numbers, omit the `#number` portion and just show sub-sector
6. **Sub-sector** — taken from the `##` category heading in the consolidated file (e.g., "Dairy & Dairy Products", "Cleaning Products & Detergents")
7. **Data Quality Notes** — preserve ALL existing flags about source inconsistencies verbatim. This section is omitted entirely if the profile has no data issues.
8. **Soya Flour Processing** — has two plant sizes (Plant A: 30t/m and Plant B: 1t/d). Split into TWO separate files: `undp-soya-flour-processing-plant-a.md` and `undp-soya-flour-processing-plant-b.md`

---

## File Naming Convention

`undp-{kebab-case-name}.md`

Rules:
- Lowercase, hyphens for spaces
- Remove parenthetical info from name: "Juice Extraction (Apples/Fruits)" → `undp-juice-extraction.md`
- Remove hash/ampersand: "Tomato Sauce & Paste" → `undp-tomato-sauce-and-paste.md`
- Keep names concise but unambiguous within the industry directory

---

## Tasks by Industry

Each task processes one industry: rename the consolidated file, then create all individual profile files.

### Task 1: Food Processing (46 profiles)

**Files:**
- Rename: `industry-guides/food-processing/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 46 files in `industry-guides/food-processing/references/`:

**Dairy & Dairy Products (8):**
- `undp-powder-milk-production.md`
- `undp-cream-separation-plant.md`
- `undp-cheese-making.md`
- `undp-yoghurt-making.md`
- `undp-butter-making.md`
- `undp-ice-cream-making.md`
- `undp-ice-cream-balls.md`
- `undp-coconut-cream.md`

**Bakery & Confectionery (6):**
- `undp-bakery-bread.md`
- `undp-baking-biscuits.md`
- `undp-cupcake-manufacturing.md`
- `undp-cornflakes-manufacturing.md`
- `undp-citrus-peel-candy.md`
- `undp-banana-wafers.md`

**Beverages & Juices (7):**
- `undp-instant-coffee-powder.md`
- `undp-coffee-caffeine-processing.md`
- `undp-fruit-juice-canning.md`
- `undp-ice-candy-making.md`
- `undp-juice-extraction.md`
- `undp-fruit-squash-production.md`
- `undp-green-tea-powder.md`

**Spices, Condiments & Sauces (6):**
- `undp-chilli-sauce.md`
- `undp-curry-powder.md`
- `undp-essence-extraction-curry-leaves.md`
- `undp-mayonnaise.md`
- `undp-tomato-sauce-and-paste.md`
- `undp-fruit-salad-processing.md`

**Oils, Fats & Extracts (4):**
- `undp-essential-oil-production.md`
- `undp-neem-oil-extraction.md`
- `undp-oil-seed-extraction.md`
- `undp-desiccated-coconuts.md`

**Cereals, Grains & Flour (6):**
- `undp-rice-hulling-plant.md`
- `undp-soya-flour-processing-plant-a.md`
- `undp-soya-flour-processing-plant-b.md`
- `undp-dehulling-sesame-seeds.md`
- `undp-simsim-and-groundnut-paste.md`
- `undp-decorticated-cashew-nut.md`

**Fruits & Vegetables Processing (4):**
- `undp-drying-fruits.md`
- `undp-dehydrated-fruits-and-vegetables.md`
- `undp-fruit-bars.md`
- `undp-fruit-cheese.md`

**Meat, Fish & Poultry Processing (4):**
- `undp-smoking-fish.md`
- `undp-fish-pickles.md`
- `undp-poultry-processing-plant.md`
- `undp-turkey-packing.md`

**Other Food Processing (1):**
- `undp-sugar-processing.md`

### Task 2: Chemicals & Cosmetics (18 profiles)

**Files:**
- Rename: `industry-guides/chemicals-cosmetics/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 18 files in `industry-guides/chemicals-cosmetics/references/`:

**Cleaning Products & Detergents (6):**
- `undp-scented-phenyl.md`
- `undp-liquid-laundry-soap.md`
- `undp-disinfectant-fluids.md`
- `undp-scouring-powder.md`
- `undp-cleaning-powder.md`
- `undp-air-freshener.md`

**Personal Care & Cosmetics (7):**
- `undp-herbal-bath-soap.md`
- `undp-herbal-deodorant.md`
- `undp-toothpowder.md`
- `undp-nail-polish.md`
- `undp-petroleum-jelly.md`
- `undp-mosquito-repellent-cream.md`
- `undp-mosquito-coil.md`

**Paints, Inks & Industrial Chemicals (5):**
- `undp-paint-manufacturing.md`
- `undp-printing-ink.md`
- `undp-office-glue.md`
- `undp-spray-painting-services.md`
- `undp-refining-used-lubricating-oil.md`

### Task 3: Construction & Building Materials (13 profiles)

**Files:**
- Rename: `industry-guides/construction-building-materials/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 13 files in `industry-guides/construction-building-materials/references/`:

**Bricks, Blocks & Cement Products (4):**
- `undp-half-bricks.md`
- `undp-brick-making-black-soil.md`
- `undp-cement-based-products.md`
- `undp-manhole-covers.md`

**Tiles, Finishing & Decorative (4):**
- `undp-mosaic-terrazzo-tiles.md`
- `undp-pottery-products.md`
- `undp-low-dust-chalk.md`
- `undp-clay-pipes.md`

**Metal Fabrication & Workshop (1):**
- `undp-metal-workshop.md`

**Wood & Timber Products (2):**
- `undp-adhesive-plywood.md`
- `undp-seasoning-of-wood.md`

**Construction Services (2):**
- `undp-multi-storey-car-park.md`
- `undp-compound-designing.md`

### Task 4: Education & Social Enterprise (4 profiles)

**Files:**
- Rename: `industry-guides/education-social/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 4 files in `industry-guides/education-social/references/`:

- `undp-secondary-school.md`
- `undp-portable-medical-first-aid-kits.md`
- `undp-disposable-syringes.md`
- `undp-sanitary-towels.md`

### Task 5: Hospitality & Tourism (10 profiles)

**Files:**
- Rename: `industry-guides/hospitality-tourism/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 10 files in `industry-guides/hospitality-tourism/references/`:

**Food Service & Catering (3):**
- `undp-food-vending.md`
- `undp-wayside-restaurant.md`
- `undp-mobile-food-vending.md`

**Bars & Entertainment (2):**
- `undp-setting-up-a-bar.md`
- `undp-video-theatre.md`

**Budget Accommodation & Camping (2):**
- `undp-campsite.md`
- `undp-tent-house-event-hire.md`

**Hotels & Lodges (3):**
- `undp-forest-lodge.md`
- `undp-holiday-homes.md`
- `undp-four-star-branded-hotel.md`

### Task 6: Livestock, Aquaculture & Farming (22 profiles)

**Files:**
- Rename: `industry-guides/livestock-aquaculture/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 22 files in `industry-guides/livestock-aquaculture/references/`:

**Poultry & Eggs (3):**
- `undp-chicken-hatchery.md`
- `undp-rearing-local-hens.md`
- `undp-poultry-feeds-manufacturing.md`

**Livestock (4):**
- `undp-piggery.md`
- `undp-dog-breeding.md`
- `undp-dairy-farm.md`
- `undp-cattle-raising.md`

**Aquaculture & Fishing (2):**
- `undp-fish-farming.md`
- `undp-fishing-hooks-manufacturing.md`

**Apiculture & Sericulture (2):**
- `undp-beekeeping.md`
- `undp-sericulture-silk-farming.md`

**Horticulture & Crop Farming (3):**
- `undp-growing-watermelons.md`
- `undp-tomato-greenhouse.md`
- `undp-cultivation-of-flowers.md`

**Agri-Inputs (8):**
- `undp-animal-feed-plant.md`
- `undp-vermi-compost-production.md`
- `undp-vermi-culture.md`
- `undp-urea-molasses-block.md`
- `undp-fertilisers-from-dry-bones.md`
- `undp-activated-carbon-coconut-shell.md`
- `undp-activated-carbon-rice-husks.md`
- `undp-bio-fertilisers.md`

### Task 7: Light Manufacturing (49 profiles)

**Files:**
- Rename: `industry-guides/manufacturing-light/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 49 files in `industry-guides/manufacturing-light/references/`:

**Plastics & Rubber Products (17):**
- `undp-expanded-pet-pre-foams.md`
- `undp-plastic-bricks.md`
- `undp-buckets.md`
- `undp-rubber-bands.md`
- `undp-plastic-containers.md`
- `undp-rubber-washers.md`
- `undp-rubber-stamps.md`
- `undp-coloured-wax-crayons.md`
- `undp-rubber-moulded-products.md`
- `undp-rubber-erasers.md`
- `undp-plastic-ropes.md`
- `undp-printed-shopping-bags.md`
- `undp-acrylic-sheets.md`
- `undp-rubber-balloons.md`
- `undp-plastic-bottle-caps.md`
- `undp-rubber-adhesive.md`
- `undp-natural-rubber-adhesives.md`
- `undp-lldpe-mailing-covers.md`

**Paper, Stationery & Printing (9):**
- `undp-ball-pen-refills.md`
- `undp-screen-printing-unit.md`
- `undp-pencils.md`
- `undp-exercise-books.md`
- `undp-paper-envelopes.md`
- `undp-serviettes.md`
- `undp-cardboard-cartons.md`
- `undp-carbon-paper.md`
- `undp-hand-made-paper.md`

**Metal Products & Hardware (6):**
- `undp-metallic-fasteners.md`
- `undp-bolts-and-nuts.md`
- `undp-wire-nails.md`
- `undp-aluminium-powder.md`
- `undp-brass-and-bronze-castings.md`
- `undp-cement-brick-making.md`

**Crafts, Decorative & Specialty Items (10):**
- `undp-wax-candles.md`
- `undp-artists-colours.md`
- `undp-horn-buttons.md`
- `undp-toothbrush-making.md`
- `undp-decoration-of-glass-wares.md`
- `undp-brass-ware-flower-vases.md`
- `undp-synthetic-gem-cutting.md`
- `undp-bone-china.md`
- `undp-paint-brushes.md`
- `undp-spectacle-frames.md`

**Recycling & Waste Processing (2):**
- `undp-recycling-plastics.md`
- `undp-silver-extraction-from-wastes.md`

**Electronics & Industrial Components (3):**
- `undp-spindle-tapes.md`
- `undp-power-invertors.md`
- `undp-zinc-sulphate-production.md`

### Task 8: Mining & Extractives (4 profiles)

**Files:**
- Rename: `industry-guides/mining-extractives/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 4 files in `industry-guides/mining-extractives/references/`:

- `undp-silver-extraction.md`
- `undp-brass-and-bronze-casting.md`
- `undp-cement-bricks.md`
- `undp-catering-oil-and-gas.md`

### Task 9: Services (10 profiles)

**Files:**
- Rename: `industry-guides/services/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 10 files in `industry-guides/services/references/`:

**Vehicle & Equipment Services (3):**
- `undp-shock-absorber-reconditioning.md`
- `undp-servicing-motor-vehicles.md`
- `undp-refrigeration-service.md`

**Cleaning & Maintenance Services (2):**
- `undp-dry-cleaner-services.md`
- `undp-roof-cleaning-services.md`

**Technology & Digital Services (3):**
- `undp-video-filming.md`
- `undp-online-music-and-bookstore.md`
- `undp-business-call-centre.md`

**Personal Care Services (1):**
- `undp-beauty-salon.md`

**Fuel & Distribution Services (1):**
- `undp-mobile-fuel-distribution.md`

### Task 10: Textiles, Fashion & Leather (25 profiles)

**Files:**
- Rename: `industry-guides/textiles-fashion/references/undp-business-profiles.md` → `undp-business-profiles-consolidated.md`
- Create 25 files in `industry-guides/textiles-fashion/references/`:

**Garments & Apparel (6):**
- `undp-cotton-t-shirts.md`
- `undp-ready-made-garments-jeans.md`
- `undp-woollen-knitwear.md`
- `undp-king-cotton-knitted-wears.md`
- `undp-cotton-mosquito-nets.md`
- `undp-crocheting-and-embroidery.md`

**Leather Goods & Footwear (8):**
- `undp-leather-sandals.md`
- `undp-fancy-leather-gloves.md`
- `undp-shoe-polish.md`
- `undp-shoe-repairing.md`
- `undp-leather-purses.md`
- `undp-bathroom-sandals.md`
- `undp-leather-belts.md`
- `undp-rexene-works.md`

**Natural Fibre & Craft Products (6):**
- `undp-making-mats.md`
- `undp-banana-fabric-polymer.md`
- `undp-banana-fibre-products.md`
- `undp-bamboo-products.md`
- `undp-natural-fibre-yarn-ropes.md`
- `undp-sisal-fibre-handicrafts.md`

**Accessories & Jewellery (5):**
- `undp-jewellery-making.md`
- `undp-artificial-silk-flowers.md`
- `undp-plastic-bangles.md`
- `undp-school-bags.md`
- `undp-designer-cotton-bags.md`

### Task 11: Git Commit

**Step 1:** Stage all renamed and new files
**Step 2:** Commit with message: "Split 200 UNDP profiles into individual reference files with standardised format"

---

## Execution Notes

- **Parallelism:** Tasks 1-10 are fully independent — can be dispatched as parallel subagents
- **Each agent** reads the consolidated file for its industry and writes all individual files using the standardised template
- **Data fidelity:** All financial figures must be preserved exactly as they appear in the consolidated files. Do not recalculate or round.
- **Manufacturing-light compact format:** These profiles use inline format (`Capital: $X | Revenue: $Y`). The agent must parse these into the vertical table format.
- **Cross-listed profiles:** Some profiles appear in multiple industry guides (e.g., fishing hooks in both livestock and manufacturing). Each gets its own file in its respective directory — this is intentional.
