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

QUESTION: For the protein options (chicken, salmon, tofu), are the amounts you can choose continuous (any weight in grams, e.g., 137g of chicken), or must they also be purchased in whole 100g units like the vegetables?

## Turn 1 - User Simulator

The protein options (chicken, salmon, tofu) can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each food type that must be included (for example, at least one vegetable pack, or at least some protein), or can the plan include zero of any given food as long as the budget and weight limits are met?

## Turn 2 - User Simulator

You need to choose at least three different types of vegetables from the list, so make sure you include at least three distinct packs of different vegetables.

## Turn 3 - Generic Agent

QUESTION: Is there any requirement about the protein foods, such as needing at least one type of protein, or can the plan theoretically include zero protein and only vegetables?

## Turn 3 - User Simulator

There is no specific minimum requirement for protein foods. The plan can theoretically include zero protein and only vegetables, as long as the budget and weight limits are met and at least three different types of vegetables are selected.

## Turn 4 - Generic Agent

QUESTION: When you say at least three different types of vegetables, does that mean at least three distinct vegetable varieties each with at least one 100g pack, or could you buy multiple packs of the same vegetable and still count it as one type?

## Turn 4 - User Simulator

It means at least three distinct vegetable varieties, each with at least one 100g pack.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on how many packs of a single vegetable you can buy, or can you buy as many packs of one vegetable as the budget and weight allow?

## Turn 5 - User Simulator

There is no upper limit on how many packs of a single vegetable you can buy, as long as the total cost does not exceed the budget and the total weight does not exceed 800 grams.

## Turn 6 - Generic Agent

QUESTION: Is the $20 budget a hard cap that the total cost must stay at or below, or is there a preference to spend as close to $20 as possible?

## Turn 6 - User Simulator

The $20 budget is a hard cap; the total cost must stay at or below $20.

## Turn 7 - Generic Agent

QUESTION: Is the 800g weight limit a hard cap that total food weight must stay at or below, or is there a preference to get as close to 800g as possible?

## Turn 7 - User Simulator

The 800g weight limit is a hard cap; the total food weight must stay at or below 800 grams.

## Turn 8 - Generic Agent

QUESTION: Are the protein amounts and costs listed per 100g of food, meaning if you buy 200g of chicken you get 46g protein and pay $6.00, or are they fixed amounts per serving regardless of weight?

## Turn 8 - User Simulator

The protein amounts and costs are listed per 100g of food.

## Turn 9 - Generic Agent

QUESTION: Is there any requirement that the total protein intake must meet a minimum target, or is the only goal to maximize total protein within the budget and weight constraints?

## Turn 9 - User Simulator

There is no minimum target for total protein intake. The only goal is to maximize total protein within the budget and weight constraints.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (in grams).

**Decision variables:**
- Protein foods (chicken, salmon, tofu): continuous, non-negative amounts in grams.
- Vegetable packs (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost ≤ $20 (hard cap).
2. Total weight ≤ 800g (hard cap).
3. At least 3 distinct vegetable varieties must be included, each with at least 1 pack.
4. No upper limit on packs of any single vegetable.
5. No minimum requirement for protein foods (can be zero).
6. No minimum target for total protein.

**Data (per 100g):**

Protein foods:
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50

Vegetable packs (each 100g):
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00