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

QUESTION: For the protein options (chicken, salmon, tofu), are the amounts you can choose continuous (any weight in grams), or must they also be purchased in fixed 100g units like the vegetables?

## Turn 1 - User Simulator

The protein options (chicken, salmon, tofu) can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard cap that the total cost must stay at or under, or is it an exact target that the spending must equal?

## Turn 2 - User Simulator

The $20 budget is a hard cap; the total cost must stay at or under $20.

## Turn 3 - Generic Agent

QUESTION: Is the 800g maximum total weight a hard cap that the combined weight of all food must stay at or under 800g, or is it an exact target that the total weight must equal 800g?

## Turn 3 - User Simulator

The 800g maximum total weight is a hard cap; the combined weight of all food must stay at or under 800g.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum amount of protein or vegetables that must be included, or can the plan include zero of any item as long as the budget and weight caps are respected?

## Turn 4 - User Simulator

There is a minimum requirement for vegetables: you must include at least three different types of vegetables. There is no stated minimum amount for the protein options.

## Turn 5 - Generic Agent

QUESTION: For the "at least three different types of vegetables" requirement, does each of the three types need to be at least one full 100g pack, or could a type count toward the three even if you buy zero packs of it?

## Turn 5 - User Simulator

Each of the three types needs to be at least one full 100g pack.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many packs of a single vegetable type you can buy, or can you buy any non-negative whole number of packs of each type?

## Turn 6 - User Simulator

You can buy any non-negative whole number of packs of each vegetable type.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total amount of protein (chicken, salmon, tofu) you can buy, or can you buy any non-negative continuous amount of each protein type?

## Turn 7 - User Simulator

You can buy any non-negative continuous amount of each protein type.

## Turn 8 - Generic Agent

QUESTION: Is the objective to maximize the total protein intake (in grams) from all food combined, or is there a different goal such as minimizing cost or maximizing some other measure?

## Turn 8 - User Simulator

The objective is to maximize the total protein intake (in grams) from all food combined.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (grams) from all food combined.

**Decision variables:**
- Protein (continuous, non-negative): chicken, salmon, tofu — any weight in grams.
- Vegetables (non-negative integer packs of 100g each): broccoli, carrots, spinach, bell pepper, mushrooms.

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
2. Total weight of all food ≤ 800g (hard cap).
3. At least three different vegetable types must each be purchased in at least one full 100g pack.
4. No minimum on protein types; any non-negative continuous amount allowed.
5. No per-item upper limits; any non-negative whole number of packs per vegetable type.

**Model form:** Mixed-integer linear program (continuous protein variables + integer vegetable-pack variables), with binary indicators to enforce the "at least three distinct vegetable types" requirement.