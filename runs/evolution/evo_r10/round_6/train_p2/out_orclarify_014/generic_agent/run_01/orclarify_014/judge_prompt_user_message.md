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

QUESTION: For the protein options (chicken, salmon, tofu), can you buy any amount in continuous 100g units (e.g., 150g of chicken), or must protein also be purchased in whole 100g units like the vegetables?

## Turn 1 - User Simulator

Protein can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each food type that must be included (for example, at least one vegetable, or at least one protein), or can the plan include zero of any given food as long as the budget and weight limits are met?

## Turn 2 - User Simulator

You need to choose at least three different types of vegetables from the list, so make sure you include at least three distinct packs of different vegetables.

## Turn 3 - Generic Agent

QUESTION: Is there any requirement about the protein side, such as needing at least one type of protein, or can the plan theoretically include zero protein and only vegetables?

## Turn 3 - User Simulator

The plan can theoretically include zero protein and only vegetables, as long as the budget and weight limits are met.

## Turn 4 - Generic Agent

QUESTION: When you say at least three different types of vegetables, does that mean at least three distinct vegetable varieties each with at least one pack, or could two packs of the same vegetable count toward the three?

## Turn 4 - User Simulator

It means at least three distinct vegetable varieties, each with at least one pack.

## Turn 5 - Generic Agent

QUESTION: Is the $20 budget a hard cap that total cost must not exceed, or is it an exact target that must be spent precisely?

## Turn 5 - User Simulator

The $20 budget is a hard cap; total cost must not exceed it.

## Turn 6 - Generic Agent

QUESTION: Is the 800g weight limit a hard cap that total weight must not exceed, or is it an exact target that must be hit precisely?

## Turn 6 - User Simulator

The 800g weight limit is a hard cap; total weight must not exceed it.

## Turn 7 - Generic Agent

QUESTION: Is there any requirement that the total protein intake must meet a minimum target, or is the only goal to maximize protein with no minimum floor?

## Turn 7 - User Simulator

The only goal is to maximize protein intake; there is no minimum floor.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (in grams).

**Decision variables:**
- Protein (chicken, salmon, tofu): continuous, non-negative quantities in grams (or 100g units).
- Vegetables (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Data (per 100g):**
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00

**Constraints:**
1. Total cost ≤ $20 (hard cap).
2. Total weight ≤ 800g (hard cap).
3. At least 3 distinct vegetable varieties, each with at least 1 pack.
4. No minimum protein requirement; zero protein is allowed.
5. No minimum or maximum per food type beyond the above.

**No other hidden rules or floors.**