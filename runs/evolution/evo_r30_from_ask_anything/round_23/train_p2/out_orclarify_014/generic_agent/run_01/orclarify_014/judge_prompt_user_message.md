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

QUESTION: For the protein options (chicken, salmon, tofu), are their quantities chosen in continuous grams, or must they also be purchased in discrete 100g units like the vegetables

## Turn 1 - User Simulator

The protein options (chicken, salmon, tofu) can be bought in any quantity you like, not necessarily in whole packs.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that the total cost must not exceed, or is it a target

## Turn 2 - User Simulator

The $20 budget is a hard ceiling; the total cost must not exceed it.

## Turn 3 - Generic Agent

QUESTION: Is the 800 gram maximum total

## Turn 3 - User Simulator

Yes, the 800 grams is a hard maximum for the total weight of all food.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum quantity requirements for any specific protein or vegetable

## Turn 4 - User Simulator

There are no minimum quantity requirements for any specific protein. For vegetables, you must select at least three different types from the list.

## Turn 5 - Generic Agent

QUESTION: When you say you must select at least three different types of vegetables, does that mean you must purchase at least one 100g pack of each of at

## Turn 5 - User Simulator

Yes, you must purchase at least one 100g pack of each of at least three different vegetable types.

## Turn 6 - Generic Agent

QUESTION: Are there any maximum quantity limits on how many 100g packs of any single vegetable

## Turn 6 - User Simulator

No, there are no maximum quantity limits on how many 100g packs of any single vegetable can be purchased.

## Turn 7 - Generic Agent

QUESTION: Are there any maximum quantity limits on the grams of any

## Turn 7 - User Simulator

No, there are no maximum quantity limits on the grams of any specific protein.

## Turn 8 - Generic Agent

QUESTION: Are there any other requirements or

## Turn 8 - User Simulator

No, there are no other requirements.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:**
Maximize total protein intake (in grams).

**Decision Variables:**
1.  **Proteins (Continuous, Non-negative):**
    *   $x_{chicken}$: grams of chicken
    *   $x_{salmon}$: grams of salmon
    *   $x_{tofu}$: grams of tofu
2.  **Vegetables (Integer, Non-negative):**
    *   $y_{broccoli}$: number of 100g packs of broccoli
    *   $y_{carrots}$: number of 100g packs of carrots
    *   $y_{spinach}$: number of 100g packs of spinach
    *   $y_{pepper}$: number of 100g packs of bell pepper
    *   $y_{mushrooms}$: number of 100g packs of mushrooms

**Data (per 100g):**
*   **Chicken:** 23g protein, $3.00
*   **Salmon:** 20g protein, $5.00
*   **Tofu:** 8g protein, $1.50
*   **Broccoli:** 2.8g protein, $1.20
*   **Carrots:** 0.9g protein, $0.80
*   **Spinach:** 2.9g protein, $1.50
*   **Bell Pepper:** 1.0g protein, $1.00
*   **Mushrooms:** 3.1g protein, $2.00

**Constraints:**
1.  **Budget:** Total cost $\le$ $20.00.
    *   Cost = $0.03 x_{chicken} + 0.05 x_{salmon} + 0.015 x_{tofu} + 1.20 y_{broccoli} + 0.80 y_{carrots} + 1.50 y_{spinach} + 1.00 y_{pepper} + 2.00 y_{mushrooms}$
2.  **Weight:** Total weight $\le$ 800g.
    *   Weight = $x_{chicken} + x_{salmon} + x_{tofu} + 100(y_{broccoli} + y_{carrots} + y_{spinach} + y_{pepper} + y_{mushrooms})$
3.  **Vegetable Variety:** Must purchase at least one pack of at least 3 different vegetable types.
    *   This is typically modeled using binary indicator variables $z_i$ for each vegetable type $i$, where $z_i = 1$ if $y_i \ge 1$, and $\sum z_i \ge 3$.
4.  **Non-negativity:**
    *   $x_{protein} \ge 0$ (continuous)
    *   $y_{vegetable} \ge 0$ (integer)

**Assumptions:**
*   None. All critical facts were confirmed by the user.