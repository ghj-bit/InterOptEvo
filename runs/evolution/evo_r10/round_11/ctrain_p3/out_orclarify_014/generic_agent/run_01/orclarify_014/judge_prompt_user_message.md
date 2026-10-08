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

QUESTION: Is there any minimum or maximum amount of each food type that must be included in the dinner (for example, at least one pack of each vegetable, or at least some amount of each protein), or can the model choose zero of any food type?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific food type. The model can choose zero of any food type, except that at least three different types of vegetables must be selected.

## Turn 3 - Generic Agent

QUESTION: When you say at least three different types of vegetables must be selected, does that mean at least three vegetable types must have a positive (non-zero) number of packs, or does it mean at least three vegetable types must be present in the menu even if some end up with zero packs?

## Turn 3 - User Simulator

It means at least three vegetable types must have a positive (non-zero) number of packs.

## Turn 4 - Generic Agent

QUESTION: Is there any requirement that at least one protein type must be included in the dinner, or is it acceptable for the model to choose zero of all protein types and only vegetables?

## Turn 4 - User Simulator

There is no requirement that at least one protein type must be included. It is acceptable for the model to choose zero of all protein types and only vegetables.

## Turn 5 - Generic Agent

QUESTION: The budget is $20 and the weight cap is 800g — are these both hard constraints that must be satisfied, or is one of them a soft constraint that can be violated with a penalty?

## Turn 5 - User Simulator

Both are hard constraints that must be satisfied.

## Turn 6 - Generic Agent

QUESTION: Is the objective strictly to maximize total protein intake (in grams), with no other factors like cost minimization or variety considered as secondary goals?

## Turn 6 - User Simulator

Yes, the objective is strictly to maximize total protein intake in grams.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:**
  - Protein: continuous, non-negative quantities (in grams) for chicken, salmon, and tofu.
  - Vegetables: non-negative integer number of 100g packs for broccoli, carrots, spinach, bell pepper, and mushrooms.

- **Objective:** Maximize total protein intake (in grams).

- **Constraints:**
  - Total cost ≤ $20 (hard constraint).
  - Total weight ≤ 800g (hard constraint).
  - At least 3 different vegetable types must have a positive (non-zero) number of packs.
  - No minimum or maximum on any individual food type.
  - Zero of all protein types is allowed.

- **Data (per 100g):**
  - Chicken: 23g protein, $3.00
  - Salmon: 20g protein, $5.00
  - Tofu: 8g protein, $1.50
  - Broccoli: 2.8g protein, $1.20
  - Carrots: 0.9g protein, $0.80
  - Spinach: 2.9g protein, $1.50
  - Bell Pepper: 1.0g protein, $1.00
  - Mushrooms: 3.1g protein, $2.00