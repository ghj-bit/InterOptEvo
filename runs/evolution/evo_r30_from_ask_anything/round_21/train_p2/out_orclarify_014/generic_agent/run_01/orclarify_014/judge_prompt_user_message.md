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

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any continuous weight amount (for example, 150 grams of chicken), or must the protein also be bought in discrete 100-gram units?

## Turn 1 - User Simulator

You can buy the protein options in any continuous weight amount. They do not have to be in 100-gram units.

## Turn 2 - Generic Agent

QUESTION: Is the total weight limit of 800 grams a strict maximum that the combined weight of all protein and vegetables cannot exceed, or is it a target that you would prefer to hit exactly?

## Turn 2 - User Simulator

It is a strict maximum. The combined weight of all protein and vegetables cannot exceed 800 grams.

## Turn 3 - Generic Agent

QUESTION: Is the total budget of $20 a strict maximum that the combined cost of all protein and vegetables cannot exceed, or is it a target that you would prefer to spend exactly?

## Turn 3 - User Simulator

It is a strict maximum. The combined cost of all protein and vegetables cannot exceed $20.

## Turn 4 - Generic Agent

QUESTION: Are there any additional requirements or restrictions on the selection of protein and vegetable items, such as a minimum number of different types to include, a maximum number of packs of any single vegetable, or a requirement to include at least one protein option?

## Turn 4 - User Simulator

Yes, you must select at least three different types of vegetables.

## Turn 5 - Generic Agent

QUESTION: Is there a minimum number of different protein types you must select, or can you choose just one type of protein (or even zero) as long as the other constraints are met?

## Turn 5 - User Simulator

There is no minimum number of different protein types. You can choose just one type, or even zero, as long as the other constraints are met.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum limit on the number of 100g packs of any single vegetable type you can purchase, or can you buy any non-negative integer number of packs for each vegetable type?

## Turn 6 - User Simulator

There is no maximum limit on the number of packs for any single vegetable type. You can buy any non-negative integer number of packs for each vegetable type.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Protein:** Continuous, non-negative weights (in grams) for Chicken, Salmon, and Tofu.
    *   **Vegetables:** Non-negative integer counts of 100g packs for Broccoli, Carrots, Spinach, Bell Pepper, and Mushrooms.
3.  **Constraints:**
    *   **Total Weight:** The sum of the weight of all protein and the weight of all vegetable packs must be $\le$ 800 grams.
    *   **Total Cost:** The sum of the cost of all protein and the cost of all vegetable packs must be $\le$ $20.
    *   **Vegetable Variety:** At least 3 different types of vegetables must be selected (i.e., the sum of binary indicators for each vegetable type being $>0$ must be $\ge$ 3).
    *   **Protein Variety:** No minimum requirement for the number of protein types; zero or more types can be selected.
    *   **Pack Limits:** No maximum limit on the number of packs for any single vegetable type.
4.  **Data:**
    *   **Chicken:** 23g protein/100g, $3.00/100g.
    *   **Salmon:** 20g protein/100g, $5.00/100g.
    *   **Tofu:** 8g protein/100g, $1.50/100g.
    *   **Broccoli:** 2.8g protein/100g, $1.20/100g.
    *   **Carrots:** 0.9g protein/100g, $0.80/100g.
    *   **Spinach:** 2.9g protein/100g, $1.50/100g.
    *   **Bell Pepper:** 1.0g protein/100g, $1.00/100g.
    *   **Mushrooms:** 3.1g protein/100g, $2.00/100g.

**Assumptions:**
*   None. All critical formulation details were confirmed by the user.