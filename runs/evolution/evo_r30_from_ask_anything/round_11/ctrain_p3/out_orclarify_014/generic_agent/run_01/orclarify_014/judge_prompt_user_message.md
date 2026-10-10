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

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any continuous weight (for example, 150g of chicken), or must proteins also be bought in discrete 100g units like the vegetables

## Turn 1 - User Simulator

You can buy the proteins in any continuous weight. They are not limited to 100g units.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that the total cost must not exceed, or is it a target that you would prefer to hit exactly

## Turn 2 - User Simulator

The $20 budget is a hard ceiling. The total cost must not exceed $20.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram maximum total weight a hard ceiling that the combined weight of all proteins and vegetables must not exceed

## Turn 3 - User Simulator

Yes, the 800-gram maximum total weight is a hard ceiling. The combined weight of all proteins and vegetables must not exceed 800 grams.

## Turn 4 - Generic Agent

QUESTION: Are there any additional requirements or restrictions beyond the budget and weight limits, such as a minimum number of different protein types, a minimum number of different vegetable types, or a requirement to include at least one of each

## Turn 4 - User Simulator

Yes, you must select at least three different types of vegetables.

## Turn 5 - Generic Agent

QUESTION: When you say you must select at least three different types of vegetables, does that mean you must purchase at least one 100g pack of each of at least three distinct vegetable types

## Turn 5 - User Simulator

Yes, you must purchase at least one 100g pack of each of at least three distinct vegetable types.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum or maximum number of different protein types you must select, or can you choose any combination of the three proteins including just one

## Turn 6 - User Simulator

You can choose any combination of the three proteins, including just one.

## Turn 7 - Generic Agent

QUESTION: Is there any minimum or maximum total weight requirement for the proteins specifically, or is the only weight constraint the 800-gram total

## Turn 7 - User Simulator

The only weight constraint is the 800-gram total.

## Turn 8 - Generic Agent

QUESTION: Is there any minimum or maximum number of 100g packs you can purchase for any single vegetable type

## Turn 8 - User Simulator

No, there is no minimum or maximum number of 100g packs for any single vegetable type, other than the requirement to buy at least one pack of at least three distinct vegetable types.

## Turn 9 - Generic Agent

QUESTION: Is there any minimum or maximum weight you can purchase for any single protein type

## Turn 9 - User Simulator

No, there is no minimum or maximum weight for any single protein type.

## Turn 10 - Generic Agent

QUESTION: Is the objective to maximize total protein intake in grams, or is there another goal such as maximizing protein per dollar

## Turn 10 - User Simulator

The objective is to maximize total protein intake in grams.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total protein intake in grams.
- Decision variables:
  - Protein weights (continuous, non-negative) for chicken, salmon, and tofu.
  - Vegetable pack counts (non-negative integers) for broccoli, carrots, spinach, bell pepper, and mushrooms.
- Constraints:
  - Total cost must not exceed $20 (hard ceiling).
  - Total weight of all proteins and vegetables must not exceed 800 grams (hard ceiling).
  - Must purchase at least one 100g pack of each of at least three distinct vegetable types.
- Data:
  - Protein options (per 100g):
    - Chicken: 23g protein, $3.00 cost
    - Salmon: 20g protein, $5.00 cost
    - Tofu: 8g protein, $1.50 cost
  - Vegetable options (per 100g pack):
    - Broccoli: 2.8g protein, $1.20 cost
    - Carrots: 0.9g protein, $0.80 cost
    - Spinach: 2.9g protein, $1.50 cost
    - Bell Pepper: 1.0g protein, $1.00 cost
    - Mushrooms: 3.1g protein, $2.00 cost
- Assumptions:
  - None. All formulation-critical facts are confirmed.