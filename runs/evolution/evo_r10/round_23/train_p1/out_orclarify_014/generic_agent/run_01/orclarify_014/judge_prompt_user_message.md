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

QUESTION: For the protein options (chicken, salmon, tofu), are they also sold in fixed 100g units that must be bought in whole units, or can they be purchased in any continuous amount (e.g., 150g of chicken)?

## Turn 1 - User Simulator

They can be purchased in any continuous amount. You do not need to buy them in whole 100g units.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each food type that must be included in the dinner, or can any food type be left out entirely (zero amount) as long as the total weight and budget constraints are satisfied?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific food type. Any food type can be left out entirely (zero amount), provided the total weight and budget constraints are satisfied.

## Turn 3 - Generic Agent

QUESTION: Is the 800g weight limit a hard cap that must not be exceeded, or is it a target that you would like to reach as closely as possible (i.e., you could go slightly over if it meaningfully increases protein)?

## Turn 3 - User Simulator

It is a hard cap that must not be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the $20 budget also a hard cap that must not be exceeded, or is it a target you'd like to stay within as closely as possible?

## Turn 4 - User Simulator

It is a hard cap that must not be exceeded.

## Turn 5 - Generic Agent

QUESTION: When you say "maximize total protein intake," do you mean the total protein from all foods combined (both proteins and vegetables), or only the protein from the protein options (chicken, salmon, tofu)?

## Turn 5 - User Simulator

It means the total protein from all foods combined, including both the protein options and the vegetables.

## Turn 6 - Generic Agent

QUESTION: Since vegetables come in 100g packs and proteins can be bought in any continuous amount, is there any requirement that the total weight of proteins plus vegetables must exactly equal 800g, or is it fine to use less than 800g total if that gives more protein?

## Turn 6 - User Simulator

It is fine to use less than 800g total. The 800g limit is a maximum, not a target to reach exactly.

## Turn 7 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total protein intake (sum of protein from all protein options and all vegetable options combined).

**Decision variables:**
- Protein options (chicken, salmon, tofu): continuous, non-negative amounts (in grams or in 100g units — any real-valued quantity is allowed).
- Vegetable options (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost ≤ $20 (hard cap).
2. Total weight of all food ≤ 800g (hard cap).
3. No minimum or maximum per food type; any food can be zero.
4. Total weight does not need to reach 800g; using less is fine.

**Data (per 100g):**

| Food | Protein (g) | Cost ($) |
|------|-------------|----------|
| Chicken | 23 | 3.00 |
| Salmon | 20 | 5.00 |
| Tofu | 8 | 1.50 |
| Broccoli | 2.8 | 1.20 |
| Carrots | 0.9 | 0.80 |
| Spinach | 2.9 | 1.50 |
| Bell Pepper | 1.0 | 1.00 |
| Mushrooms | 3.1 | 2.00 |

This is a mixed-integer linear program (MILP): continuous variables for the three proteins, integer variables for the five vegetable pack counts, with two linear constraints (budget and weight) and a linear objective (total protein).