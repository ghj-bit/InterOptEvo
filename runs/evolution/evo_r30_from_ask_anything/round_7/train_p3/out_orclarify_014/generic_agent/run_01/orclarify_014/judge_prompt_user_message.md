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

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any fractional amount (e.g., 150g of chicken), or must each protein also be bought in whole 100g units?

## Turn 1 - User Simulator

You can buy the proteins in any quantity you like, not necessarily in whole 100g units.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that the total cost must not exceed, or is it a target that you would prefer to hit exactly?

## Turn 2 - User Simulator

The $20 budget is a hard ceiling; the total cost must not exceed it.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram limit a hard ceiling that the total weight of all food must not exceed, or is it a target that you would prefer to hit exactly?

## Turn 3 - User Simulator

The 800-gram limit is a hard ceiling; the total weight of all food must not exceed it.

## Turn 4 - Generic Agent

QUESTION: For the vegetable options, is there any limit on how many 100g packs of a single vegetable type you can buy, or can you buy any non-negative integer number of packs of each vegetable type?

## Turn 4 - User Simulator

You can buy any non-negative integer number of packs of each vegetable type.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum requirement for the total amount of protein you must consume, or is the only goal to maximize total protein intake subject to the budget and weight limits?

## Turn 5 - User Simulator

There is no minimum protein requirement. The only goal is to maximize total protein intake subject to the budget and weight limits.

## Turn 6 - Generic Agent

QUESTION: Is there any requirement that you must include at least one type of protein and at least one type of vegetable in the plan, or is it acceptable to choose only proteins or only vegetables if that maximizes protein intake?

## Turn 6 - User Simulator

You must include at least one type of protein and at least one type of vegetable.

## Turn 7 - Generic Agent

QUESTION: For the requirement to include at least one type of protein, does that mean you must purchase a positive amount of at least one protein type, or must you purchase a positive amount of every protein type listed?

## Turn 7 - User Simulator

You must purchase a positive amount of at least one protein type.

## Turn 8 - Generic Agent

QUESTION: For the requirement to include at least one type of vegetable, does that mean you must purchase at least one pack of at least one vegetable type, or must you purchase at least one pack of every vegetable type listed?

## Turn 8 - User Simulator

You must purchase at least one pack of at least one vegetable type.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total protein intake (in grams).
- Decision variables:
  - Protein quantities (chicken, salmon, tofu) in grams: continuous, non-negative.
  - Vegetable packs (broccoli, carrots, spinach, bell pepper, mushrooms) in 100g units: non-negative integers.
- Hard constraints:
  - Total cost ≤ $20.
  - Total weight ≤ 800 grams.
  - At least one protein type must be purchased in a positive amount.
  - At least one vegetable type must be purchased in at least one pack.
- Data (per 100g):
  - Chicken: 23g protein, $3.00
  - Salmon: 20g protein, $5.00
  - Tofu: 8g protein, $1.50
  - Broccoli: 2.8g protein, $1.20
  - Carrots: 0.9g protein, $0.80
  - Spinach: 2.9g protein, $1.50
  - Bell Pepper: 1.0g protein, $1.00
  - Mushrooms: 3.1g protein, $2.00
- No minimum protein requirement.
- No per-type upper bounds on protein quantity or vegetable packs.
- All facts above are confirmed; no open assumptions remain.