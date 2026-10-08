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

QUESTION: Are the protein options (chicken, salmon, tofu) also limited to whole 100g units, or can they be purchased in any amount (continuous grams)?

## Turn 1 - User Simulator

They can be purchased in any amount (continuous grams).

## Turn 2 - Generic Agent

QUESTION: Is there a minimum or maximum amount of each protein or vegetable that must be included in the dinner, or can any of them be left out entirely (zero)?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific protein or vegetable. Any of them can be left out entirely (zero), except that you must include at least three different types of vegetables.

## Turn 3 - Generic Agent

QUESTION: When you say at least three different types of vegetables must be included, does that mean at least one whole 100g pack of each of three different vegetable types, or could a type count as "included" with less than a full pack?

## Turn 3 - User Simulator

It means at least one whole 100g pack of each of three different vegetable types.

## Turn 4 - Generic Agent

QUESTION: Is the 800g weight limit a hard cap that must not be exceeded, or is it a target that you'd like to hit as closely as possible?

## Turn 4 - User Simulator

It is a hard cap that must not be exceeded.

## Turn 5 - Generic Agent

QUESTION: Is the $20 budget also a hard cap that must not be exceeded, or is it a target to hit as closely as possible?

## Turn 5 - User Simulator

It is a hard cap that must not be exceeded.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on how many 100g packs of a single vegetable type you can buy, or can you buy as many packs of one type as the budget and weight allow?

## Turn 6 - User Simulator

You can buy as many packs of one type as the budget and weight allow.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on how many grams of a single protein you can buy, or can you buy as many grams of one protein as the budget and weight allow?

## Turn 7 - User Simulator

You can buy as many grams of one protein as the budget and weight allow.

## Turn 8 - Generic Agent

QUESTION: Is the objective strictly to maximize total protein intake, with no secondary goal like minimizing cost or weight among solutions that achieve the same maximum protein?

## Turn 8 - User Simulator

Yes, the objective is strictly to maximize total protein intake.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total protein intake (grams). No secondary objective.
- **Protein options (continuous grams, non-negative):**
  - Chicken: 23g protein / 100g, $3.00 / 100g
  - Salmon: 20g protein / 100g, $5.00 / 100g
  - Tofu: 8g protein / 100g, $1.50 / 100g
- **Vegetable options (whole 100g packs, non-negative integer packs):**
  - Broccoli: 2.8g protein / pack, $1.20 / pack
  - Carrots: 0.9g protein / pack, $0.80 / pack
  - Spinach: 2.9g protein / pack, $1.50 / pack
  - Bell Pepper: 1.0g protein / pack, $1.00 / pack
  - Mushrooms: 3.1g protein / pack, $2.00 / pack
- **Constraints:**
  - Total cost ≤ $20 (hard cap)
  - Total weight ≤ 800g (hard cap)
  - At least 3 different vegetable types must each have ≥ 1 whole pack
  - No per-item minimums or maximums beyond the above
  - Any item can be zero (except the 3-vegetable-type requirement)