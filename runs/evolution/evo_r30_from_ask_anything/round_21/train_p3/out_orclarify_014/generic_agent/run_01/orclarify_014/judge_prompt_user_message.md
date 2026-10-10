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

QUESTION: Are the protein options (chicken, salmon, tofu) also restricted to whole 100g units, or can they be purchased in any continuous amount?

## Turn 1 - User Simulator

They can be purchased in any continuous amount. There is no restriction to whole 100g units for the protein options.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that the total cost must not exceed, or is it a target that can be slightly exceeded if it yields significantly more protein?

## Turn 2 - User Simulator

It is a hard ceiling. The total cost must not exceed $20.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram maximum total weight a hard ceiling that the combined weight of all food must not exceed, or is it a target that can be slightly exceeded if it yields significantly more protein?

## Turn 3 - User Simulator

It is a hard ceiling. The total weight of all food must not exceed 800 grams.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum quantity requirements for any specific protein or vegetable option, such as requiring at least one pack of a certain vegetable or a minimum weight of a certain protein?

## Turn 4 - User Simulator

There are no minimum quantity requirements for any specific protein or vegetable option.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum limit on the number of packs of any single vegetable type, or can you purchase unlimited packs of any vegetable as long as the total weight and budget constraints are satisfied?

## Turn 5 - User Simulator

There is no maximum limit on the number of packs of any single vegetable type. You can purchase unlimited packs of any vegetable as long as the total weight and budget constraints are satisfied.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Proteins (Continuous, Non-negative):**
        *   $x_{chicken}$: Weight of chicken in grams.
        *   $x_{salmon}$: Weight of salmon in grams.
        *   $x_{tofu}$: Weight of tofu in grams.
    *   **Vegetables (Integer, Non-negative):**
        *   $n_{broccoli}$: Number of 100g packs of broccoli.
        *   $n_{carrots}$: Number of 100g packs of carrots.
        *   $n_{spinach}$: Number of 100g packs of spinach.
        *   $n_{pepper}$: Number of 100g packs of bell pepper.
        *   $n_{mushrooms}$: Number of 100g packs of mushrooms.
3.  **Constraints:**
    *   **Budget:** Total cost $\le$ $20.00.
        *   Cost = $0.03 x_{chicken} + 0.05 x_{salmon} + 0.015 x_{tofu} + 1.20 n_{broccoli} + 0.80 n_{carrots} + 1.50 n_{spinach} + 1.00 n_{pepper} + 2.00 n_{mushrooms}$.
    *   **Weight:** Total weight $\le$ 800 grams.
        *   Weight = $x_{chicken} + x_{salmon} + x_{tofu} + 100(n_{broccoli} + n_{carrots} + n_{spinach} + n_{pepper} + n_{mushrooms})$.
    *   **Non-negativity:** All variables $\ge 0$.
    *   **Integrality:** All vegetable variables ($n$) must be integers.
4.  **Data (Per 100g):**
    *   **Chicken:** 23g protein, $3.00 cost.
    *   **Salmon:** 20g protein, $5.00 cost.
    *   **Tofu:** 8g protein, $1.50 cost.
    *   **Broccoli:** 2.8g protein, $1.20 cost.
    *   **Carrots:** 0.9g protein, $0.80 cost.
    *   **Spinach:** 2.9g protein, $1.50 cost.
    *   **Bell Pepper:** 1.0g protein, $1.00 cost.
    *   **Mushrooms:** 3.1g protein, $2.00 cost.
5.  **Assumptions:**
    *   No minimum quantities required for any item.
    *   No maximum limits on individual item quantities other than those imposed by the global budget and weight constraints.
    *   Protein and vegetable weights are additive.