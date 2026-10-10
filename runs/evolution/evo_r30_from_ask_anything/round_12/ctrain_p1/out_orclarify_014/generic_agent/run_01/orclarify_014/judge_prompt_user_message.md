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

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any fractional amount of each (for example, 150g of chicken), or must each protein also be bought in whole 100g units?

## Turn 1 - User Simulator

You can buy any amount of chicken, salmon, or tofu. They do not have to be in whole 100g units.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that must not be exceeded, or is it a target you would prefer to hit exactly?

## Turn 2 - User Simulator

The $20 budget is a hard ceiling. The total cost must not exceed $20.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram total weight limit a hard ceiling that must not be exceeded, or is it a target you would prefer to hit exactly?

## Turn 3 - User Simulator

The 800-gram total weight limit is a hard ceiling. The total weight of all food must not exceed 800 grams.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum quantity requirements for any specific protein or vegetable (for example, you must include at least one pack of broccoli, or you must include at least 100g of chicken), or can the plan include zero of any item?

## Turn 4 - User Simulator

There are no minimum quantity requirements for any specific protein or vegetable. You can include zero of any item, except that you must select at least three different types of vegetables.

## Turn 5 - Generic Agent

QUESTION: When you say you must select at least three different types of vegetables, does that mean you must buy at least one whole pack of each of at least three distinct vegetable types, or could you buy multiple packs of the same vegetable to count toward the three?

## Turn 5 - User Simulator

You must buy at least one whole pack of each of at least three distinct vegetable types. Buying multiple packs of the same vegetable does not count toward the three different types.

## Turn 6 - Generic Agent

QUESTION: Are there any maximum quantity limits on any specific protein or vegetable (for example, you cannot buy more than 2 packs of mushrooms, or you cannot buy more than 300g of chicken), or is the only limit on each item the overall 800g weight and $20 budget?

## Turn 6 - User Simulator

There are no maximum quantity limits on any specific protein or vegetable. The only limits are the overall 800g weight and $20 budget.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Proteins (Chicken, Salmon, Tofu):** Continuous, non-negative variables representing grams purchased.
    *   **Vegetables (Broccoli, Carrots, Spinach, Bell Pepper, Mushrooms):** Integer, non-negative variables representing the number of 100g packs purchased.
3.  **Constraints:**
    *   **Budget:** Total cost must be $\le$ $20.00.
    *   **Weight:** Total weight (grams of protein + 100g $\times$ number of vegetable packs) must be $\le$ 800g.
    *   **Vegetable Variety:** At least 3 distinct types of vegetables must be selected, with at least 1 pack of each selected type.
4.  **Data:**
    *   **Chicken:** 23g protein/100g, $3.00/100g.
    *   **Salmon:** 20g protein/100g, $5.00/100g.
    *   **Tofu:** 8g protein/100g, $1.50/100g.
    *   **Broccoli:** 2.8g protein/100g pack, $1.20/pack.
    *   **Carrots:** 0.9g protein/100g pack, $0.80/pack.
    *   **Spinach:** 2.9g protein/100g pack, $1.50/pack.
    *   **Bell Pepper:** 1.0g protein/100g pack, $1.00/pack.
    *   **Mushrooms:** 3.1g protein/100g pack, $2.00/pack.
5.  **Assumptions:**
    *   None. All critical facts were confirmed by the user.