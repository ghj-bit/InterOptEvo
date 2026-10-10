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

QUESTION: For the protein options, is the amount of each protein (chicken, salmon, tofu) chosen in continuous grams, or must each also be purchased in discrete 100g units?

## Turn 1 - User Simulator

The protein options (chicken, salmon, and tofu) can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is the 800-gram weight limit a hard ceiling that must not be exceeded, or is it a soft target where exceeding it is allowed if a penalty is applied?

## Turn 2 - User Simulator

The 800-gram weight limit is a hard ceiling that must not be exceeded.

## Turn 3 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that total cost must not exceed, or is it a soft target where going over is allowed if a penalty is applied?

## Turn 3 - User Simulator

The $20 budget is a hard ceiling that total cost must not exceed.

## Turn 4 - Generic Agent

QUESTION: Are there any additional requirements the brief omits, such as a minimum quantity of a food that must be included if it is chosen, a requirement to include at least one protein and at least one vegetable, or any restriction on how many different protein or vegetable types can be selected?

## Turn 4 - User Simulator

You need to choose at least three different types of vegetables from the list, so make sure you include at least three distinct packs of different vegetables.

## Turn 5 - Generic Agent

QUESTION: Is the requirement to include at least three different vegetable types a hard constraint that must be satisfied, or is it a soft target where failing to meet it is allowed if a penalty is applied?

## Turn 5 - User Simulator

The requirement to include at least three different vegetable types is a hard constraint that must be satisfied.

## Turn 6 - Generic Agent

QUESTION: Is there any requirement to include at least one type of protein, or is it allowed to choose zero protein and only vegetables?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the vegetable packs, is there a maximum number of packs of any single vegetable type that can be purchased, or is there no upper limit on how many packs of one vegetable you can buy?

## Turn 7 - User Simulator

There is no upper limit on how many packs of one vegetable you can buy.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the total amount of protein (in grams) that can be purchased, or is the only limit on protein the overall 800-gram weight ceiling and the $20 budget?

## Turn 8 - User Simulator

The only limits on protein are the overall 800-gram weight ceiling and the $20 budget.

## Turn 9 - Generic Agent

QUESTION: Is the objective to maximize total protein intake (in grams) the sole goal, or is there a secondary goal such as minimizing cost among solutions that achieve the maximum protein?

## Turn 9 - User Simulator

The sole goal is to maximize total protein intake.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

Objective:
- Maximize total protein intake (in grams). Confirmed.

Decision variables:
- Protein: continuous, non-negative amounts (in grams) of chicken, salmon, and tofu. Confirmed.
- Vegetables: non-negative integer number of 100g packs of broccoli, carrots, spinach, bell pepper, and mushrooms. Confirmed.

Constraints:
- Total cost must not exceed $20 (hard ceiling). Confirmed.
- Total weight of all food must not exceed 800 grams (hard ceiling). Confirmed.
- At least three distinct vegetable types must be included (hard constraint). Confirmed.
- No upper limit on the number of packs of any single vegetable type. Confirmed.
- No upper limit on protein beyond the 800g weight ceiling and $20 budget. Confirmed.

Data (per 100g):
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00

Open assumptions:
- It is assumed that at least one type of protein must be included, since the user's request explicitly frames the problem as "choosing a combination of protein and vegetables." This was not explicitly confirmed but is implied by the brief.
- It is assumed that the "at least three different types of vegetables" constraint means at least three distinct vegetable types must each have a positive integer number of packs (i.e., at least one pack of each of at least three different vegetable types).