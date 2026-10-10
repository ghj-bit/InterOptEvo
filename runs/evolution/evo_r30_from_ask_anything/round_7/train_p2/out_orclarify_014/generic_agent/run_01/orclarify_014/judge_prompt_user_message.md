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

QUESTION: Is the $20 budget a hard ceiling that the total cost must not exceed, or is it a target amount that you want to spend as close to as possible?

## Turn 2 - User Simulator

The $20 budget is a hard ceiling; the total cost must not exceed it.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram limit a hard ceiling that the total weight of all food must not exceed, or is it a target weight you want to get as close to as possible?

## Turn 3 - User Simulator

The 800-gram limit is a hard ceiling; the total weight of all food must not exceed it.

## Turn 4 - Generic Agent

QUESTION: For the protein options, is there a minimum or maximum amount of each specific protein (chicken, salmon, tofu) that you must or can include, or can the amount of each protein be any non-negative value including zero?

## Turn 4 - User Simulator

The amount of each protein can be any non-negative value, including zero.

## Turn 5 - Generic Agent

QUESTION: For the vegetable options, is there a minimum or maximum number of packs of each specific vegetable (broccoli, carrots, spinach, bell pepper, mushrooms) that you must or can include, or can the number of packs of each vegetable be any non-negative integer including zero?

## Turn 5 - User Simulator

The number of packs of each vegetable can be any non-negative integer, including zero.

## Turn 6 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of your dinner planning problem:

**Objective:**
- Maximize total protein intake (in grams).

**Decision Variables:**
- Protein amounts (continuous, non-negative):
  - Chicken: $c$ grams
  - Salmon: $s$ grams
  - Tofu: $t$ grams
- Vegetable packs (integer, non-negative):
  - Broccoli: $b$ packs
  - Carrots: $r$ packs
  - Spinach: $p$ packs
  - Bell Pepper: $l$ packs
  - Mushrooms: $m$ packs

**Constraints:**
1. **Budget (hard ceiling):** Total cost ≤ $20.
   - Cost = $3.00 \times (c/100) + 5.00 \times (s/100) + 1.50 \times (t/100) + 1.20 \times b + 0.80 \times r + 1.50 \times p + 1.00 \times l + 2.00 \times m$
2. **Weight (hard ceiling):** Total weight ≤ 800 grams.
   - Weight = $c + s + t + 100b + 100r + 100p + 100l + 100m$

**Protein Content (per 100g):**
- Chicken: 23g
- Salmon: 20g
- Tofu: 8g
- Broccoli: 2.8g
- Carrots: 0.9g
- Spinach: 2.9g
- Bell Pepper: 1.0g
- Mushrooms: 3.1g

**Total Protein to Maximize:**
- $23 \times (c/100) + 20 \times (s/100) + 8 \times (t/100) + 2.8 \times b + 0.9 \times r + 2.9 \times p + 1.0 \times l + 3.1 \times m$

**Confirmed Facts:**
- Proteins can be purchased in any non-negative quantity (continuous).
- Vegetables must be purchased in whole 100g packs (non-negative integers).
- Budget is a hard ceiling ($20).
- Weight is a hard ceiling (800g).
- No minimum or maximum constraints on individual protein or vegetable items beyond non-negativity.