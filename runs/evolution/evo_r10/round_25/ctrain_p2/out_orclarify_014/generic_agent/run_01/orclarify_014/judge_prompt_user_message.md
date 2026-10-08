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

QUESTION: For the protein options (chicken, salmon, tofu), can you buy them in any amount (continuous grams), or are they also sold in fixed 100g units like the vegetables?

## Turn 1 - User Simulator

You can buy chicken, salmon, and tofu in any amount. They are not limited to fixed 100g units.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each protein you must or may include, or can any protein be left out entirely (zero grams)?

## Turn 2 - User Simulator

There is no minimum or maximum amount for each protein. You can include any amount of any protein, or leave any protein out entirely (zero grams).

## Turn 3 - Generic Agent

QUESTION: For the vegetables, is there any minimum or maximum number of packs of each vegetable you must or may buy, or can any vegetable be left out entirely (zero packs)?

## Turn 3 - User Simulator

There is no minimum or maximum number of packs for any specific vegetable. You can buy any number of packs of a vegetable, or leave any vegetable out entirely (zero packs), as long as you select at least three different types of vegetables in total.

## Turn 4 - Generic Agent

QUESTION: You mentioned selecting at least three different types of vegetables — does this mean at least three distinct vegetable types must each have at least one pack, or does it mean at least three packs total across any combination of vegetable types?

## Turn 4 - User Simulator

It means at least three distinct vegetable types must each have at least one pack.

## Turn 5 - Generic Agent

QUESTION: The 800g weight limit — does it apply to the combined weight of all proteins and all vegetables together, or only to the vegetables?

## Turn 5 - User Simulator

The 800g weight limit applies to the combined weight of all proteins and all vegetables together.

## Turn 6 - Generic Agent

QUESTION: The $20 budget — is it a strict cap (total cost must be less than or equal to $20), or must you spend exactly $20?

## Turn 6 - User Simulator

It is a strict cap. The total cost must be less than or equal to $20.

## Turn 7 - Generic Agent

QUESTION: When you say "maximize total protein intake," do you mean the sum of protein grams from both the proteins and the vegetables combined, or only the protein grams from the protein options (chicken, salmon, tofu)?

## Turn 7 - User Simulator

It means the sum of protein grams from both the proteins and the vegetables combined.

## Turn 8 - Generic Agent

QUESTION: Is there any requirement that you must include at least one type of protein, or is it acceptable to have zero grams of all proteins and only vegetables?

## Turn 8 - User Simulator

There is no requirement to include at least one type of protein. It is acceptable to have zero grams of all proteins and only vegetables.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or preferences I should know about, such as a maximum number of total food items, a requirement to use at least one protein type, or any other rule that would affect the plan?

## Turn 9 - User Simulator

No, there are no other constraints or preferences. The rules are:
- Maximize total protein intake (proteins + vegetables).
- Total cost must not exceed $20.
- Total weight must not exceed 800 grams.
- Proteins can be bought in any quantity.
- Vegetables are sold in 100g packs (whole packs only).
- At least three different types of vegetables must be selected.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein grams (from both proteins and vegetables combined).

**Decision variables:**
- Proteins (chicken, salmon, tofu): continuous, non-negative grams.
- Vegetables (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integer number of 100g packs.

**Constraints:**
1. Total cost ≤ $20.
2. Total weight (all proteins + all vegetables) ≤ 800g.
3. At least 3 distinct vegetable types must each have at least 1 pack.
4. No minimum or maximum on any individual protein or vegetable (beyond the above).
5. No requirement to include any protein.

**Data (per 100g):**
- Chicken: 23g protein, $3.00
- Salmon: 20g protein, $5.00
- Tofu: 8g protein, $1.50
- Broccoli: 2.8g protein, $1.20
- Carrots: 0.9g protein, $0.80
- Spinach: 2.9g protein, $1.50
- Bell Pepper: 1.0g protein, $1.00
- Mushrooms: 3.1g protein, $2.00