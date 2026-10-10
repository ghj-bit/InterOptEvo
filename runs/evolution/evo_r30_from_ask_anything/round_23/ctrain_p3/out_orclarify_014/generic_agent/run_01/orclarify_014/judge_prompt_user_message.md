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

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any continuous weight (for example, 150g of chicken), or must proteins also be bought in discrete 100g units

## Turn 1 - User Simulator

You can buy the proteins in any continuous weight. For example, you could purchase 150g of chicken. They do not need to be in discrete 100g units.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum quantity requirements for each specific protein or vegetable option, such as requiring at least one pack of a certain vegetable or limiting the amount of a specific

## Turn 2 - User Simulator

There are no minimum or maximum quantity requirements for any specific protein or vegetable option. You can choose any amount of each, subject to the overall budget, weight limit, and the requirement to include at least three different types of vegetables.

## Turn 3 - Generic Agent

QUESTION: Does the requirement to include at least three different types of vegetables mean that you must purchase at least one 100g pack of each of three distinct vegetable

## Turn 3 - User Simulator

Yes, you must purchase at least one 100g pack of each of three distinct vegetable types.

## Turn 4 - Generic Agent

QUESTION: Are there any other constraints or preferences, such as a maximum number of total vegetable packs, a requirement to include at least one protein type, or a preference for specific

## Turn 4 - User Simulator

No, there are no other constraints or preferences.

## Turn 5 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Proteins (Chicken, Salmon, Tofu):** Continuous, non-negative weights (in grams).
    *   **Vegetables (Broccoli, Carrots, Spinach, Bell Pepper, Mushrooms):** Non-negative integer number of 100g packs.
3.  **Constraints:**
    *   **Budget:** Total cost $\le$ $20.00.
    *   **Weight:** Total weight of all food $\le$ 800 grams.
    *   **Vegetable Diversity:** At least 3 distinct types of vegetables must be selected, with at least 1 pack (100g) of each selected type.
4.  **Data:**
    *   **Chicken:** 23g protein/100g, $3.00/100g.
    *   **Salmon:** 20g protein/100g, $5.00/100g.
    *   **Tofu:** 8g protein/100g, $1.50/100g.
    *   **Broccoli:** 2.8g protein/100g, $1.20/100g.
    *   **Carrots:** 0.9g protein/100g, $0.80/100g.
    *   **Spinach:** 2.9g protein/100g, $1.50/100g.
    *   **Bell Pepper:** 1.0g protein/100g, $1.00/100g.
    *   **Mushrooms:** 3.1g protein/100g, $2.00/100g.
5.  **Assumptions:**
    *   None. All critical facts were confirmed by the user.