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

QUESTION: For the protein options (chicken, salmon, tofu), can you buy them in any amount (continuous weight in grams), or are they also sold in fixed pack sizes like the vegetables?

## Turn 1 - User Simulator

You can buy chicken, salmon, and tofu in any amount. They are not sold in fixed pack sizes; you can choose any continuous weight in grams.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each protein or vegetable type that must be included in the dinner, or can any of them be left out entirely (zero amount)?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific protein or vegetable type. You can leave any of them out entirely (zero amount), except that you must include at least three different types of vegetables.

## Turn 3 - Generic Agent

QUESTION: When you say at least three different types of vegetables must be included, does each of those three types need at least one full 100g pack, or could a type count as "included" with a smaller amount?

## Turn 3 - User Simulator

Each of the three different vegetable types must have at least one full 100g pack.

## Turn 4 - Generic Agent

QUESTION: Is the total protein intake to be maximized the sum of protein from both the proteins and the vegetables, or only the protein from the protein options?

## Turn 4 - User Simulator

The total protein intake to be maximized is the sum of protein from both the protein options and the vegetables.

## Turn 5 - Generic Agent

QUESTION: Is the $20 budget a hard cap on the total cost of everything (proteins plus vegetables), or is it a target you'd like to spend as close to as possible?

## Turn 5 - User Simulator

The $20 budget is a hard cap on the total cost of everything (proteins plus vegetables).

## Turn 6 - Generic Agent

QUESTION: Is the 800-gram maximum weight a hard cap on the combined weight of all proteins and vegetables, or does it apply only to one of the two groups?

## Turn 6 - User Simulator

The 800-gram maximum weight is a hard cap on the combined weight of all proteins and vegetables.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total protein intake = sum of protein from all proteins + all vegetables.
- **Protein variables (continuous, grams, ≥ 0):** chicken (23g protein / 100g, $3.00 / 100g), salmon (20g / 100g, $5.00 / 100g), tofu (8g / 100g, $1.50 / 100g). No per-item minimums or maximums; any can be zero.
- **Vegetable variables (integer packs of 100g, ≥ 0):** broccoli (2.8g, $1.20), carrots (0.9g, $0.80), spinach (2.9g, $1.50), bell pepper (1.0g, $1.00), mushrooms (3.1g, $2.00).
- **Vegetable diversity constraint:** at least 3 distinct vegetable types, each with ≥ 1 full pack.
- **Budget constraint (hard cap):** total cost of proteins + vegetables ≤ $20.
- **Weight constraint (hard cap):** total weight of proteins + vegetables ≤ 800g.
- No other constraints; leftover budget or weight is fine (no requirement to spend or fill).