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

QUESTION: For the protein options (chicken, salmon, tofu), can you buy any amount in continuous 100g units (e.g., 150g of chicken), or must proteins also be purchased in whole 100g packs like the vegetables?

## Turn 1 - User Simulator

Proteins can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each food type that must be included in the dinner (for example, at least one vegetable, or at least one protein), or can the plan include zero of any given food as long as the budget and weight limits are met?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific protein or vegetable type. You can include zero of any given food, as long as the overall budget and weight limits are met.

## Turn 3 - Generic Agent

QUESTION: Is there any requirement that the dinner must include at least one protein and at least one vegetable (i.e., the plan can't be all protein or all vegetables), or is it acceptable for the optimal plan to consist of only one category?

## Turn 3 - User Simulator

There is no requirement that the dinner must include at least one protein and at least one vegetable. It is acceptable for the plan to consist of only one category, as long as the budget and weight limits are met.

## Turn 4 - Generic Agent

QUESTION: The protein amounts are given per 100g — when you say proteins can be bought in any quantity, does that mean the weight of each protein can be any non-negative real number of grams (e.g., 137g of chicken), or must protein weights still be multiples of some unit like 10g or 100g?

## Turn 4 - User Simulator

The weight of each protein can be any non-negative real number of grams.

## Turn 5 - Generic Agent

QUESTION: The cost and protein values are given per 100g — should I treat these as exact linear rates that scale proportionally with weight (e.g., 150g of chicken costs $4.50 and provides 34.5g protein), or are there any fixed fees, discounts, or other non-linear cost considerations I should account for?

## Turn 5 - User Simulator

Treat the cost and protein values as exact linear rates that scale proportionally with weight. There are no fixed fees, discounts, or other non-linear cost considerations.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total protein intake (in grams).
- **Protein foods** (chicken, salmon, tofu): continuous, non-negative real weights in grams. Protein and cost scale linearly at the given per-100g rates (chicken 23g/$3.00, salmon 20g/$5.00, tofu 8g/$1.50 per 100g).
- **Vegetable foods** (broccoli, carrots, spinach, bell pepper, mushrooms): sold in 100g packs; decision variables are non-negative integers (number of whole packs). Protein and cost scale linearly per pack (broccoli 2.8g/$1.20, carrots 0.9g/$0.80, spinach 2.9g/$1.50, bell pepper 1.0g/$1.00, mushrooms 3.1g/$2.00 per 100g pack).
- **Constraints:**
  - Total cost ≤ $20.
  - Total weight (all proteins + all vegetable packs) ≤ 800 grams.
- **No other restrictions:** no minimum or maximum per food type, no requirement to include at least one protein or one vegetable, no fixed fees or non-linear costs. Any food may be zero.