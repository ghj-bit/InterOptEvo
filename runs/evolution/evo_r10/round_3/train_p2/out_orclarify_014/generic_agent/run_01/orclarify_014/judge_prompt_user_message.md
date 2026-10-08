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

QUESTION: For the protein options (chicken, salmon, tofu), are their quantities also restricted to whole 100g units (non-negative integer number of 100g portions), or can they be purchased in any continuous amount?

## Turn 1 - User Simulator

They can be purchased in any continuous amount. There is no restriction to whole 100g units for the protein options.

## Turn 2 - Generic Agent

QUESTION: Is the 800g maximum total weight a hard constraint that must be strictly respected (i.e., total weight of all food ≤ 800g), or is it a soft target where exceeding it is allowed if penalized?

## Turn 2 - User Simulator

It is a hard constraint. The total weight of all food must not exceed 800 grams.

## Turn 3 - Generic Agent

QUESTION: Is the $20 budget also a hard constraint (total cost must not exceed $20), or is it a soft target where exceeding it is allowed if penalized?

## Turn 3 - User Simulator

It is a hard constraint. The total cost must not exceed $20.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum requirement that at least one protein and at least one vegetable must be included in the dinner, or is it acceptable to choose zero of a category (e.g., only protein with no vegetables, or only vegetables with no protein)?

## Turn 4 - User Simulator

There is no explicit minimum requirement that at least one protein and at least one vegetable must be included. However, you must select at least three different types of vegetables.

## Turn 5 - Generic Agent

QUESTION: The requirement to select at least three different types of vegetables — does this mean at least three distinct vegetable types must each have a positive (≥1 pack) quantity, or could a vegetable type be "selected" with zero packs as long as three types are named?

## Turn 5 - User Simulator

It means at least three distinct vegetable types must each have a positive (≥1 pack) quantity.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on how many packs of any single vegetable type can be purchased, or can you buy any non-negative integer number of packs of each vegetable type (subject only to the total weight and budget constraints)?

## Turn 6 - User Simulator

There is no upper limit on how many packs of any single vegetable type can be purchased. You can buy any non-negative integer number of packs of each vegetable type, subject only to the total weight and budget constraints.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on the continuous quantity of any single protein type (e.g., max grams of chicken), or can you buy any non-negative continuous amount of each protein (subject only to the total weight and budget constraints)?

## Turn 7 - User Simulator

There is no upper limit on the continuous quantity of any single protein type. You can buy any non-negative continuous amount of each protein, subject only to the total weight and budget constraints.

## Turn 8 - Generic Agent

QUESTION: When you say "maximize total protein intake," does this mean maximizing the sum of protein grams from both the protein options AND the vegetable options combined, or only the protein grams from the protein options (chicken, salmon, tofu)?

## Turn 8 - User Simulator

It means maximizing the sum of protein grams from both the protein options and the vegetable options combined.

## Turn 9 - Generic Agent

QUESTION: Is there any other constraint or requirement I haven't asked about yet, such as a minimum or maximum total number of food items, a requirement to use all available budget, or any other business rule that should be included in the model?

## Turn 9 - User Simulator

No, there are no other constraints or requirements.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (sum of protein grams from both protein options and vegetable options).

**Decision variables:**
- Protein options (chicken, salmon, tofu): continuous, non-negative quantities (in grams or 100g units).
- Vegetable options (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost ≤ $20 (hard constraint).
2. Total weight of all food ≤ 800 grams (hard constraint).
3. At least three distinct vegetable types must each have a positive (≥1 pack) quantity.
4. No upper limits on individual protein quantities or individual vegetable pack counts beyond the total weight and budget constraints.
5. No minimum requirement for protein types (zero is allowed).
6. No other constraints.

**Data (per 100g):**
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00