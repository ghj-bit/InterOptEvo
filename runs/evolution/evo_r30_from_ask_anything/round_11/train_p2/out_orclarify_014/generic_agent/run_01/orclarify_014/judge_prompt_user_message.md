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

QUESTION: For the protein options (chicken, salmon, tofu), are you purchasing them in fixed 100g units where you can only buy whole 100g portions (non-negative integer number of 100g units), or can you purchase any continuous amount of protein (e.g., 150g of chicken)?

## Turn 1 - User Simulator

You can purchase any continuous amount of protein. Chicken, salmon, and tofu are not limited to whole 100g units; you can buy any quantity you like.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum quantity requirements for each specific protein or vegetable option (for example, "must include at least 100g of chicken" or "no more than 200g of salmon"), or is the only restriction that quantities must be non-negative?

## Turn 2 - User Simulator

There are no minimum or maximum quantity requirements for any specific protein or vegetable option. The only restriction is that quantities must be non-negative.

## Turn 3 - Generic Agent

QUESTION: Is the total weight limit of 800 grams a hard constraint that must be strictly adhered to, or is it a soft target where exceeding it is allowed if a penalty is applied?

## Turn 3 - User Simulator

The total weight limit of 800 grams is a hard constraint that must be strictly adhered to.

## Turn 4 - Generic Agent

QUESTION: Is the total budget of $20 a hard constraint that must be strictly adhered to, or is it a soft target where exceeding it is allowed if a penalty is applied?

## Turn 4 - User Simulator

The total budget of $20 is a hard constraint that must be strictly adhered to.

## Turn 5 - Generic Agent

QUESTION: Are there any other requirements or constraints for tonight's dinner that have not been mentioned yet, such as a requirement to include at least one protein source, a requirement to include at least one vegetable, or any exclusivity rules between specific food items?

## Turn 5 - User Simulator

Yes, there is one additional requirement: you must select at least three different types of vegetables from the list.

## Turn 6 - Generic Agent

QUESTION: Does the requirement to select at least three different types of vegetables mean that you must purchase a positive amount (at least one 100g pack) of each of those three vegetable types, or is it sufficient to simply have them available in the plan even if the quantity purchased is zero?

## Turn 6 - User Simulator

It means you must purchase a positive amount (at least one 100g pack) of each of those three vegetable types.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Proteins (Continuous, Non-negative):** Let $x_C, x_S, x_T$ be the grams of Chicken, Salmon, and Tofu purchased, respectively.
    *   **Vegetables (Integer, Non-negative):** Let $y_B, y_Ca, y_Sp, y_Pe, y_Mu$ be the number of 100g packs of Broccoli, Carrots, Spinach, Bell Pepper, and Mushrooms purchased, respectively.
3.  **Parameters (per 100g unit):**
    *   **Chicken:** 23g protein, $3.00 cost, 100g weight.
    *   **Salmon:** 20g protein, $5.00 cost, 100g weight.
    *   **Tofu:** 8g protein, $1.50 cost, 100g weight.
    *   **Broccoli:** 2.8g protein, $1.20 cost, 100g weight.
    *   **Carrots:** 0.9g protein, $0.80 cost, 100g weight.
    *   **Spinach:** 2.9g protein, $1.50 cost, 100g weight.
    *   **Bell Pepper:** 1.0g protein, $1.00 cost, 100g weight.
    *   **Mushrooms:** 3.1g protein, $2.00 cost, 100g weight.
4.  **Constraints:**
    *   **Budget:** Total cost $\le$ $20.
    *   **Weight:** Total weight $\le$ 800g.
    *   **Vegetable Variety:** At least 3 distinct vegetable types must be purchased with a quantity $\ge$ 1 pack.
    *   **Non-negativity:** All protein quantities $\ge$ 0; all vegetable pack counts $\ge$ 0.
    *   **Integrality:** Vegetable pack counts must be integers.

**Assumptions:**
*   None. All critical facts were confirmed during the interview.