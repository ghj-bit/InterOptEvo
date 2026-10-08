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

QUESTION: For the protein options (chicken, salmon, tofu), can you purchase any fractional amount (e.g., 150g of chicken), or must proteins also be bought in whole 100g units like the vegetables?

## Turn 1 - User Simulator

Proteins can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each protein or vegetable that must be included in the dinner, or can any of them be left out entirely (zero quantity)?

## Turn 2 - User Simulator

There is no minimum or maximum amount for any specific protein or vegetable. Any of them can be left out entirely (zero quantity), except that you must include at least three different types of vegetables.

## Turn 3 - Generic Agent

QUESTION: When you say at least three different types of vegetables must be included, does each of those three types need to be at least one full 100g pack, or could a type count as "included" with a smaller amount?

## Turn 3 - User Simulator

Each of the three types must be at least one full 100g pack.

## Turn 4 - Generic Agent

QUESTION: Is the $20 budget a hard cap that total cost must stay at or under, and is the 800g weight limit also a hard cap that total weight must stay at or under?

## Turn 4 - User Simulator

Yes, both are hard caps. Total cost must not exceed $20, and total weight must not exceed 800 grams.

## Turn 5 - Generic Agent

QUESTION: Is the goal purely to maximize total protein grams, with no other objective like minimizing cost or maximizing variety, as long as the budget and weight caps are respected?

## Turn 5 - User Simulator

Yes, the goal is purely to maximize total protein grams, with no other objective like minimizing cost or maximizing variety, as long as the budget and weight caps are respected.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total protein grams. No secondary objectives (cost, variety) matter.
- **Proteins (continuous, any non-negative quantity, measured in grams):**
  - Chicken: 23g protein / 100g, $3.00 / 100g
  - Salmon: 20g protein / 100g, $5.00 / 100g
  - Tofu: 8g protein / 100g, $1.50 / 100g
- **Vegetables (integer packs, each pack = 100g, non-negative integer number of packs):**
  - Broccoli: 2.8g protein, $1.20
  - Carrots: 0.9g protein, $0.80
  - Spinach: 2.9g protein, $1.50
  - Bell Pepper: 1.0g protein, $1.00
  - Mushrooms: 3.1g protein, $2.00
- **Constraints:**
  - Total cost ≤ $20 (hard cap).
  - Total weight (proteins + vegetables) ≤ 800g (hard cap).
  - At least three different vegetable types must be included, and each of those three must be at least one full 100g pack (i.e., at least 1 pack each for three distinct vegetable types).
  - No per-item minimums or maximums otherwise; any item may be zero.
- **Decision variables:** continuous grams for each protein; integer pack counts for each vegetable.

I will now formulate and solve this mixed-integer linear program.