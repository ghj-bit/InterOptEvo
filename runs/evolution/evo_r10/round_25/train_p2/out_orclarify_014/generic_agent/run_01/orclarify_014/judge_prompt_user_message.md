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

QUESTION: For the protein options (chicken, salmon, tofu), are their quantities also restricted to whole 100g units (non-negative integer multiples of 100g), or can they be purchased in any continuous amount?

## Turn 1 - User Simulator

They can be purchased in any continuous amount. There is no restriction to whole 100g units for the protein options.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of protein or vegetables that must be included in the dinner, or is it acceptable to choose zero of any particular food item (including choosing no vegetables at all)?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific food item. However, you must select at least three different types of vegetables. It is acceptable to choose zero of any particular protein or vegetable item, provided the requirement of at least three distinct vegetable types is met.

## Turn 3 - Generic Agent

QUESTION: For the "at least three different types of vegetables" requirement, does each of the three selected vegetable types need to be at least one full 100g pack, or could a type count as "selected" with a fractional pack (even though only whole packs can be purchased)?

## Turn 3 - User Simulator

Each of the three selected vegetable types must be at least one full 100g pack. Since only whole packs can be purchased, a type counts as "selected" only if you buy at least one whole pack of it.

## Turn 4 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that the total cost must stay at or below, and is the 800g weight limit also a hard ceiling that the total weight must stay at or below (i.e., both are "must not exceed" constraints with no penalty for coming in under)?

## Turn 4 - User Simulator

Yes, both are hard ceilings. The total cost must not exceed $20, and the total weight must not exceed 800 grams. There is no penalty for coming in under these limits.

## Turn 5 - Generic Agent

QUESTION: When you say "maximize total protein intake," does this mean maximizing the sum of protein from both the protein options and the vegetable options combined, or only the protein from the three protein options (chicken, salmon, tofu) while vegetables are just a side requirement?

## Turn 5 - User Simulator

It means maximizing the sum of protein from both the protein options and the vegetable options combined.

## Turn 6 - Generic Agent

QUESTION: Is there any requirement that at least one of the three protein options (chicken, salmon, tofu) must be included in the dinner, or could the optimal solution theoretically consist only of vegetables?

## Turn 6 - User Simulator

There is no requirement that at least one of the three protein options must be included. Theoretically, the solution could consist only of vegetables, provided the other constraints are met.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake, where total protein = sum of protein from all protein options (chicken, salmon, tofu) plus sum of protein from all vegetable options (broccoli, carrots, spinach, bell pepper, mushrooms).

**Decision variables:**
- Protein options (chicken, salmon, tofu): continuous, non-negative quantities measured in grams (or in 100g units, continuous).
- Vegetable options (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost ≤ $20 (hard ceiling).
2. Total weight of all food ≤ 800 grams (hard ceiling).
3. At least three distinct vegetable types must be selected, where a vegetable type counts as "selected" only if at least one whole 100g pack of that type is purchased.
4. No minimum or maximum on any individual food item (other than the non-negativity and the integer-pack rule for vegetables).
5. No requirement to include any protein option; a vegetables-only solution is permissible.

**Data (per 100g):**
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00

**Model type:** Mixed-integer linear program (continuous variables for protein, integer variables for vegetable packs, with binary indicators to enforce the "at least three distinct vegetable types" constraint).