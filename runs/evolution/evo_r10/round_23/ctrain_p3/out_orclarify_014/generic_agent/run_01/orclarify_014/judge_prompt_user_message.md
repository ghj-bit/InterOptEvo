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

QUESTION: For the protein options (chicken, salmon, tofu), are their quantities also restricted to whole 100g units (non-negative integers), or can they be purchased in any continuous amount?

## Turn 1 - User Simulator

They can be purchased in any continuous amount.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of protein or vegetables that must be included in the dinner, or is it acceptable to choose zero of any item?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific protein or vegetable item. It is acceptable to choose zero of any individual item, as long as the overall requirement of at least three different types of vegetables is met.

## Turn 3 - Generic Agent

QUESTION: You mentioned an overall requirement of at least three different types of vegetables — does this mean at least three distinct vegetable varieties must each have a positive (non-zero) number of packs, and is that the only requirement on the number of vegetable types?

## Turn 3 - User Simulator

Yes, at least three distinct vegetable varieties must each have a positive (non-zero) number of packs. That is the only requirement on the number of vegetable types.

## Turn 4 - Generic Agent

QUESTION: Regarding the budget and weight limits, are these hard constraints that must be strictly respected (total cost ≤ $20 and total weight ≤ 800g), or is there any flexibility or penalty for exceeding them?

## Turn 4 - User Simulator

They are hard constraints. Total cost must not exceed $20 and total weight must not exceed 800 grams.

## Turn 5 - Generic Agent

QUESTION: Is the objective purely to maximize total protein intake (in grams) from all food combined, with no other goals such as minimizing cost or maximizing variety?

## Turn 5 - User Simulator

Yes, the objective is purely to maximize total protein intake in grams from all food combined.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (grams) from all food combined.

**Decision variables:**
- Protein items (chicken, salmon, tofu): continuous, non-negative quantities (in 100g units or grams — any continuous amount allowed).
- Vegetable items (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost ≤ $20 (hard constraint).
2. Total weight of all food ≤ 800 grams (hard constraint).
3. At least 3 distinct vegetable varieties must each have a positive (≥1) number of packs.
4. No minimum or maximum on any individual item (zero is allowed for any single item, subject to the 3-vegetable rule).

**Data (per 100g):**

| Item | Protein (g) | Cost ($) |
|------|------------|----------|
| Chicken | 23 | 3.00 |
| Salmon | 20 | 5.00 |
| Tofu | 8 | 1.50 |
| Broccoli | 2.8 | 1.20 |
| Carrots | 0.9 | 0.80 |
| Spinach | 2.9 | 1.50 |
| Bell Pepper | 1.0 | 1.00 |
| Mushrooms | 3.1 | 2.00 |

All items contribute to both the protein objective and the weight/cost constraints.