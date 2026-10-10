# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U8, U9, U10, U12, U2, U3, U4, U5
I need help planning tonight's dinner, choosing a combination of protein and vegetables, to maximize total protein intake. Vegetables are sold in 100g packs and only whole packs can be purchased (non‑negative integer number of packs). Total cost must not exceed the budget and total weight of all food must not exceed 800 grams.

Protein options (per 100g):
- Chicken: 23g protein, $3.00 cost
- Salmon: 20g protein, $5.00 cost
- Tofu: 8g protein, $1.50 cost

Vegetable options (per 100g pack):
- Broccoli: 2.8g protein, $1.20 cost
- Carrots: 0.9g protein, $0.80 cost
- Spinach: 2.9g protein, $1.50 cost
- Bell Pepper: 1.0g protein, $1.00 cost
- Mushrooms: 3.1g protein, $2.00 cost

Total budget: $20.

Maximum total weight: 800 grams.

## Problem units
- U1 (context): I need help planning tonight's dinner, choosing a combination of protein and vegetables.
- U2 (data): Protein options (per 100g):
- Chicken: 23g protein, $3.00 cost
- Salmon: 20g protein, $5.00 cost
- Tofu: 8g protein, $1.50 cost
- U3 (data): Vegetable options (per 100g pack):
- Broccoli: 2.8g protein, $1.20 cost
- Carrots: 0.9g protein, $0.80 cost
- Spinach: 2.9g protein, $1.50 cost
- Bell Pepper: 1.0g protein, $1.00 cost
- Mushrooms: 3.1g protein, $2.00 cost
- U4 (data): Total budget: $20.
- U5 (data): Maximum total weight: 800 grams.
- U6 (objective): Maximize total protein intake.
- U7 (assumption): Protein options (chicken, salmon, tofu) can be bought in any quantity.
- U8 (assumption): Vegetables are sold in 100g packs.
- U9 (constraint): Total cost must not exceed the budget.
- U10 (constraint): Total weight of all food must not exceed 800 grams.
- U11 (constraint): At least three different types of vegetables must be selected.
- U12 (constraint): Only whole packs of vegetables can be purchased (non‑negative integer number of packs).

## Hidden slot scoring rules
## H1: protein_purchase_quantity_type
- Severity: P1
- Severity reason: Without this, the agent cannot know whether proteins are continuous or discrete, impacting variable definitions. Assuming incorrectly could lead to an incorrect model.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must explicitly ask about the purchase unit or whether proteins can be bought in fractional/continuous quantities versus discrete packs.
- Reference acceptable questions:
  - Can I buy fractional amounts of chicken, salmon, and tofu, or are they sold in discrete packs?
  - What is the purchase unit for the protein options? Is it by weight, by pack, or any amount?
- Failure modes:
  - Assuming proteins can only be purchased in whole 100g packs
  - Assuming continuous quantities without clarification

## H2: min_vegetable_types_required
- Severity: P1
- Severity reason: Without this, the agent misses a core constraint that requires at least three distinct vegetable types, leading to a different feasible set and an incorrect solution relative to the intended problem.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask about a requirement on the number of distinct vegetable types or a minimum count of vegetable varieties.
- Reference acceptable questions:
  - Is there a minimum number of different vegetable types I need to include?
  - Do I have to select at least a certain number of distinct vegetables from the list?
- Failure modes:
  - Assuming she just wants to maximize protein and vegetables are optional
  - Assuming she only needs to select one vegetable type


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any fractional amount (e.g., 150g of chicken), or must each protein also be bought in whole 100g units?

## Turn 1 - User Simulator

You can buy the proteins in any quantity you like, not necessarily in whole 100g units.

## Turn 2 - Generic Agent

QUESTION: Is the total weight limit of 800 grams intended to include both the protein and the vegetables, or does it apply only to the vegetables?

## Turn 2 - User Simulator

The 800-gram limit applies to the total weight of all food, including both the protein and the vegetables.

## Turn 3 - Generic Agent

QUESTION: Is the $20 budget intended to cover the combined cost of both the proteins and the vegetables, or is it a separate budget for each category?

## Turn 3 - User Simulator

The $20 budget covers the combined cost of both the proteins and the vegetables.

## Turn 4 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of your dinner planning problem:

**Objective**
- Maximize total protein intake (in grams).

**Decision Variables**
- Protein quantities (continuous, non-negative):
  - Chicken: grams purchased
  - Salmon: grams purchased
  - Tofu: grams purchased
- Vegetable packs (non-negative integers):
  - Broccoli packs (each 100g)
  - Carrot packs (each 100g)
  - Spinach packs (each 100g)
  - Bell Pepper packs (each 100g)
  - Mushroom packs (each 100g)

**Constraints**
1. Total cost ≤ $20 (combined for proteins and vegetables).
2. Total weight ≤ 800 grams (combined for proteins and vegetables).
3. Protein quantities can be any non-negative real number (not restricted to 100g units).
4. Vegetable quantities must be non-negative integers (whole 100g packs only).

**Data (per 100g)**

| Item | Protein (g) | Cost ($) |
|------|-------------|----------|
| Chicken | 23 | 3.00 |
| Salmon | 20 | 5.00 |
| Tofu | 8 | 1.50 |
| Broccoli | 2.8 | 1.20 |
| Carrots | 0.9 | 0.80 |
| Spinach | 2.9 | 1.50 |
| Bell Pepper | 1.0 | 1.00 |
| Mushrooms | 3.1 | 2.00 |

**No open assumptions** — all structural and parametric facts are confirmed.