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

QUESTION: Are the protein options (chicken, salmon, tofu) also sold in 100g units where only whole 100g units can be purchased, or can they be purchased in any continuous amount?

## Turn 1 - User Simulator

They can be purchased in any continuous amount. You do not need to buy them in whole 100g units.

## Turn 2 - Generic Agent

QUESTION: Is the total weight limit of 800 grams a hard constraint that must not be exceeded, or is it a soft target where exceeding it is allowed if a penalty is applied?

## Turn 2 - User Simulator

It is a hard constraint. The total weight of all food must not exceed 800 grams.

## Turn 3 - Generic Agent

QUESTION: Is the total budget of $20 a hard constraint that must not be exceeded, or is it a soft target where exceeding it is allowed if a penalty is applied?

## Turn 3 - User Simulator

It is a hard constraint. The total cost must not exceed $20.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum quantity requirements for any specific protein or vegetable option, such as requiring at least one pack of a particular vegetable or a minimum weight of a particular protein?

## Turn 4 - User Simulator

There are no minimum quantity requirements for any specific protein or vegetable option. However, you must select at least three different types of vegetables from the list.

## Turn 5 - Generic Agent

QUESTION: Does the requirement to select at least three different types of vegetables mean that you must purchase at least one whole pack of each of three distinct vegetable types, or is it sufficient to purchase at least one pack total from three different vegetable categories?

## Turn 5 - User Simulator

It means you must purchase at least one whole pack of each of three distinct vegetable types.

## Turn 6 - Generic Agent

QUESTION: Are there any upper limits on the number of packs for any specific vegetable type, or is the only limit on vegetable quantities the total weight and budget constraints?

## Turn 6 - User Simulator

There are no upper limits on the number of packs for any specific vegetable type. The only limits on vegetable quantities are the total weight and budget constraints.

## Turn 7 - Generic Agent

QUESTION: Are there any upper limits on the continuous amount of any specific protein type, or is the only limit on protein quantities the total weight and budget constraints?

## Turn 7 - User Simulator

There are no upper limits on the continuous amount of any specific protein type. The only limits on protein quantities are the total weight and budget constraints.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Proteins (Chicken, Salmon, Tofu):** Continuous, non-negative variables representing the weight in grams purchased.
    *   **Vegetables (Broccoli, Carrots, Spinach, Bell Pepper, Mushrooms):** Integer, non-negative variables representing the number of 100g packs purchased.
3.  **Constraints:**
    *   **Total Weight:** The sum of the weight of all proteins and vegetables must not exceed 800 grams. (Hard constraint)
    *   **Total Cost:** The sum of the cost of all proteins and vegetables must not exceed $20. (Hard constraint)
    *   **Vegetable Variety:** At least three distinct vegetable types must be selected, with a minimum of one pack purchased for each of those three types. (Hard constraint)
4.  **Data:**
    *   **Protein (per 100g):**
        *   Chicken: 23g protein, $3.00
        *   Salmon: 20g protein, $5.00
        *   Tofu: 8g protein, $1.50
    *   **Vegetables (per 100g pack):**
        *   Broccoli: 2.8g protein, $1.20
        *   Carrots: 0.9g protein, $0.80
        *   Spinach: 2.9g protein, $1.50
        *   Bell Pepper: 1.0g protein, $1.00
        *   Mushrooms: 3.1g protein, $2.00
5.  **Assumptions:**
    *   None. All formulation-critical facts were confirmed by the user.