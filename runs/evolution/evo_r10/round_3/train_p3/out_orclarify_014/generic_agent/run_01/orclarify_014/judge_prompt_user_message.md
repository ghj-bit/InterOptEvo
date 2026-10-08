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

QUESTION: For the protein options (chicken, salmon, tofu), are they also purchased in 100g units where only whole 100g units can be bought (non-negative integer number of 100g units), or can they be bought in any continuous amount?

## Turn 1 - User Simulator

They can be bought in any continuous amount. You do not need to purchase chicken, salmon, or tofu in whole 100g units.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of protein or vegetables that must be included in the dinner, or is it acceptable to buy zero of any particular item (including zero vegetables or zero protein) as long as the budget and weight constraints are satisfied?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific protein or vegetable item. It is acceptable to buy zero of any particular item, including zero of a specific protein or zero of a specific vegetable, as long as the budget and weight constraints are satisfied.

However, you must select at least three different types of vegetables in total.

## Turn 3 - Generic Agent

QUESTION: The requirement to select at least three different types of vegetables — does "select" mean that each of those three types must have at least one whole 100g pack purchased (i.e., a positive integer number of packs), or could a type count as "selected" even if only a fraction of a pack were used?

## Turn 3 - User Simulator

Each of the three types must have at least one whole 100g pack purchased. A type only counts as "selected" if you buy a positive integer number of packs for it.

## Turn 4 - Generic Agent

QUESTION: Is there any requirement about the protein items — for example, must you select at least one type of protein, or at least a certain number of different protein types, or is it fine to buy only vegetables and no protein at all?

## Turn 4 - User Simulator

There is no requirement to select any specific protein items. It is fine to buy only vegetables and no protein at all, as long as the budget and weight constraints are satisfied.

## Turn 5 - Generic Agent

QUESTION: The total weight limit of 800 grams — does this include both the protein items and the vegetable packs combined, or does it apply only to the vegetables?

## Turn 5 - User Simulator

The 800-gram limit applies to the total weight of all food, including both the protein items and the vegetable packs combined.

## Turn 6 - Generic Agent

QUESTION: The total cost budget of $20 — does this apply to the combined cost of both the protein items and the vegetable packs, or only to the vegetables?

## Turn 6 - User Simulator

The $20 budget applies to the combined cost of both the protein items and the vegetable packs.

## Turn 7 - Generic Agent

QUESTION: To confirm the objective: the goal is to maximize the total grams of protein from all food combined (protein items plus the protein content in the vegetable packs), correct?

## Turn 7 - User Simulator

Yes, the goal is to maximize the total grams of protein from all food combined, including both the protein items and the protein content in the vegetable packs.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein grams from all food combined (protein items + protein content in vegetable packs).

**Decision variables:**
- Protein items (chicken, salmon, tofu): continuous, non-negative amounts in grams.
- Vegetable packs (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost (protein + vegetables) ≤ $20.
2. Total weight (protein + vegetables) ≤ 800 grams.
3. At least 3 different vegetable types must each have ≥ 1 whole pack purchased.
4. No minimum or maximum on any individual item; zero is allowed for any protein item and for any vegetable type not among the three selected.

**Data (per 100g):**
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00