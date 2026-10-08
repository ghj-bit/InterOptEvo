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

QUESTION: For the protein options (chicken, salmon, tofu), can you buy them in any amount (continuous grams), or are they also sold in fixed pack sizes like the vegetables?

## Turn 1 - User Simulator

You can buy chicken, salmon, and tofu in any amount. They are not sold in fixed pack sizes; you can choose any continuous quantity of grams for each.

## Turn 2 - Generic Agent

QUESTION: Is there a minimum or maximum amount of each protein you must or may buy, or can you choose zero grams of any protein (including buying none of a particular protein)?

## Turn 2 - User Simulator

There is no minimum or maximum amount for each protein. You can choose zero grams of any particular protein, including buying none of a specific one.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum or maximum number of vegetable packs you must or may buy, or can you choose zero packs of any vegetable (including buying no vegetables at all)?

## Turn 3 - User Simulator

You must select at least three different types of vegetables. You can choose zero packs of any specific vegetable type, but you cannot buy no vegetables at all because you need at least three distinct vegetable types in your selection.

## Turn 4 - Generic Agent

QUESTION: When you say at least three different types of vegetables, does that mean at least three vegetable types must each have at least one pack (i.e., each of the three types contributes at least 100g), or could one of the three types have zero packs as long as three types are "selected"?

## Turn 4 - User Simulator

Each of the three different vegetable types must have at least one pack. You cannot count a type as "selected" if you buy zero packs of it.

## Turn 5 - Generic Agent

QUESTION: Is the 800g maximum total weight a hard ceiling (total weight must be at most 800g), or is it an exact target you must hit precisely?

## Turn 5 - User Simulator

The 800g maximum total weight is a hard ceiling. The total weight of all food must be at most 800 grams.

## Turn 6 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling (total cost must be at most $20), or is it an exact target you must spend precisely?

## Turn 6 - User Simulator

The $20 budget is a hard ceiling. The total cost must be at most $20.

## Turn 7 - Generic Agent

QUESTION: Is the objective to maximize total protein intake only, with no other goals (like minimizing cost or maximizing variety) to consider as a tiebreaker?

## Turn 7 - User Simulator

The objective is to maximize total protein intake only. There are no other goals or tiebreakers to consider.

## Turn 8 - Generic Agent

QUESTION: Are the protein and vegetable values given per 100g, meaning the total protein and cost scale linearly with the grams/packs you buy (e.g., 200g of chicken gives 46g protein and costs $6.00)?

## Turn 8 - User Simulator

Yes, the protein and cost values are per 100g. The total protein and cost scale linearly with the amount you buy. For example, 200g of chicken gives 46g protein and costs $6.00.

## Turn 9 - Generic Agent

QUESTION: For the vegetable packs, does each 100g pack count as exactly 100g toward the 800g total weight limit, so buying 3 packs of broccoli adds 300g to the total weight?

## Turn 9 - User Simulator

Yes, each 100g vegetable pack counts as exactly 100g toward the 800g total weight limit. Buying 3 packs of broccoli adds 300g to the total weight.

## Turn 10 - Generic Agent

QUESTION: Is there any upper limit on how many packs of a single vegetable type you can buy, or can you buy as many packs of one type as the budget and weight allow?

## Turn 10 - User Simulator

There is no upper limit on how many packs of a single vegetable type you can buy. You can buy as many packs of one type as the budget and weight allow.

## Turn 11 - Generic Agent

QUESTION: Is there any upper limit on the grams of a single protein you can buy, or can you buy as many grams of one protein as the budget and weight allow?

## Turn 11 - User Simulator

There is no upper limit on the grams of a single protein you can buy. You can buy as many grams of one protein as the budget and weight allow.

## Turn 12 - Generic Agent

QUESTION: Is there any requirement that you must buy at least one protein (i.e., at least some grams of chicken, salmon, or tofu), or could the optimal solution theoretically include zero protein and only vegetables?

## Turn 12 - User Simulator

There is no requirement that you must buy at least one protein. Theoretically, the solution could include zero protein and only vegetables, as long as the other constraints are met.

## Turn 13 - Generic Agent

QUESTION: Are there any other constraints or requirements I haven't asked about yet, such as a maximum number of total vegetable types, a requirement to include a specific food, or any other rule for tonight's dinner?

## Turn 13 - User Simulator

No, there are no other constraints or requirements. The rules are:
- Maximize total protein intake.
- Total cost must not exceed $20.
- Total weight must not exceed 800 grams.
- Vegetables are sold in 100g packs; only whole packs can be purchased.
- At least three different types of vegetables must be selected, with at least one pack of each.
- Proteins can be bought in any continuous amount.

## Turn 14 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (grams of protein). No tiebreakers.

**Decision variables:**
- Proteins (continuous, non-negative grams): chicken, salmon, tofu. No per-item minimum or maximum.
- Vegetables (non-negative integer number of 100g packs): broccoli, carrots, spinach, bell pepper, mushrooms. No per-type upper limit.

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
1. Total cost ≤ $20 (hard ceiling).
2. Total weight ≤ 800g (hard ceiling). Protein weight = grams bought; vegetable weight = 100g × number of packs.
3. At least three distinct vegetable types must each have ≥ 1 pack (a type with 0 packs does not count as selected).
4. Protein and vegetable protein/cost scale linearly with quantity.
5. No requirement to buy any protein; zero protein is allowed.
6. No other constraints.

**Model form:** Mixed-integer linear program (continuous protein variables, integer vegetable pack variables, binary selection variables for the "at least three types" rule).