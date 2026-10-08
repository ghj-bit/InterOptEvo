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

QUESTION: For the protein options (chicken, salmon, tofu), are the quantities you can choose continuous (any gram amount, e.g., 150g of chicken), or must they also be purchased in whole 100g units like the vegetables?

## Turn 1 - User Simulator

The protein options can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum or maximum amount of each protein or vegetable type that must be included in the dinner (for example, at least one pack of each vegetable, or at least some chicken), or can any of them be left out entirely (zero quantity)?

## Turn 2 - User Simulator

You need to choose at least three different types of vegetables from the list, so make sure you include at least three distinct packs of different vegetables.

## Turn 3 - Generic Agent

QUESTION: When you say at least three different types of vegetables, does that mean at least three distinct vegetable types each with at least one pack, and is there any upper limit on how many packs of a single vegetable type you can buy (for example, can you buy 5 packs of mushrooms and 1 pack of broccoli)?

## Turn 3 - User Simulator

Yes, that means at least three distinct vegetable types each with at least one pack. There is no upper limit on how many packs of a single vegetable type you can buy, as long as the total cost and weight constraints are met.

## Turn 4 - Generic Agent

QUESTION: For the "at least three different types of vegetables" requirement, does each of those three types need at least one full 100g pack, or could one of the three types be represented by a partial pack?

## Turn 4 - User Simulator

Each of the three types needs at least one full 100g pack.

## Turn 5 - Generic Agent

QUESTION: Is there any requirement about the protein types, such as needing to include at least one type of protein, or can the dinner consist of vegetables only with zero protein?

## Turn 5 - User Simulator

There is no requirement to include at least one type of protein. The dinner can consist of vegetables only with zero protein.

## Turn 6 - Generic Agent

QUESTION: Is the $20 budget a hard cap that must not be exceeded, and is the 800g weight limit also a hard cap, or is there any flexibility in either constraint?

## Turn 6 - User Simulator

Both the $20 budget and the 800g weight limit are hard caps that must not be exceeded.

## Turn 7 - Generic Agent

QUESTION: Is there any requirement that the total weight of food must be exactly 800g, or can it be less than 800g as long as it doesn't exceed that limit?

## Turn 7 - User Simulator

The total weight can be less than 800g, as long as it does not exceed that limit.

## Turn 8 - Generic Agent

QUESTION: Is there any requirement that the total cost must be exactly $20, or can it be less than $20 as long as it doesn't exceed that budget?

## Turn 8 - User Simulator

The total cost can be less than $20, as long as it does not exceed that budget.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or preferences I should know about, such as a minimum total protein target, a preference for certain foods, or any other rules that would affect the dinner plan?

## Turn 9 - User Simulator

No, there are no other constraints or preferences.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total protein intake (in grams).

**Decision variables:**
- Protein quantities (chicken, salmon, tofu): continuous, non-negative, measured in grams (or 100g units).
- Vegetable packs (broccoli, carrots, spinach, bell pepper, mushrooms): non-negative integers, each pack = 100g.

**Constraints:**
1. Total cost ≤ $20 (hard cap).
2. Total weight ≤ 800g (hard cap).
3. At least 3 distinct vegetable types, each with at least 1 full 100g pack.
4. No upper limit on packs of any single vegetable type.
5. No requirement to include any protein type (zero protein is allowed).
6. No other constraints or preferences.

**Data (per 100g):**

| Food | Protein (g) | Cost ($) |
|------|-------------|----------|
| Chicken | 23 | 3.00 |
| Salmon | 20 | 5.00 |
| Tofu | 8 | 1.50 |
| Broccoli | 2.8 | 1.20 |
| Carrots | 0.9 | 0.80 |
| Spinach | 2.9 | 1.50 |
| Bell Pepper | 1.0 | 1.00 |
| Mushrooms | 3.1 | 2.00 |