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

QUESTION: Is the total cost constraint a hard ceiling where the sum of all protein and vegetable costs must be less than or equal to $20, or is there a separate budget allocation for proteins versus vegetables?

## Turn 2 - User Simulator

It is a hard ceiling. The total cost of all protein and vegetables combined must be less than or equal to $20. There is no separate budget allocation.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram weight limit a hard ceiling where the sum of all protein and vegetable weights must be less than or equal to 800 grams, or is there a separate weight limit for proteins versus vegetables?

## Turn 3 - User Simulator

It is a hard ceiling. The total weight of all protein and vegetables combined must be less than or equal to 800 grams. There is no separate weight limit for proteins versus vegetables.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum quantity requirements for any specific protein or vegetable option, such as requiring at least one pack of a certain vegetable or a minimum weight of a certain protein?

## Turn 4 - User Simulator

There are no minimum quantity requirements for any specific protein or vegetable option. However, you must select at least three different types of vegetables from the list.

## Turn 5 - Generic Agent

QUESTION: Does the requirement to select at least three different types of vegetables mean that you must purchase at least one whole pack of each of the three selected vegetable types?

## Turn 5 - User Simulator

Yes, you must purchase at least one whole pack of each of the three selected vegetable types.

## Turn 6 - Generic Agent

QUESTION: Are there any maximum quantity limits for any specific protein or vegetable option, such as a cap on the number of packs of a specific vegetable or the weight of a specific protein?

## Turn 6 - User Simulator

No, there are no maximum quantity limits for any specific protein or vegetable option.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (in grams).
2.  **Decision Variables:**
    *   **Proteins:** Continuous, non-negative variables representing the weight (in grams) of Chicken, Salmon, and Tofu.
    *   **Vegetables:** Integer, non-negative variables representing the number of 100g packs of Broccoli, Carrots, Spinach, Bell Pepper, and Mushrooms.
3.  **Constraints:**
    *   **Budget:** Total cost of all proteins and vegetables must be $\le$ $20.
    *   **Weight:** Total weight of all proteins and vegetables must be $\le$ 800 grams.
    *   **Vegetable Diversity:** At least three distinct vegetable types must be selected.
    *   **Vegetable Minimums:** For each vegetable type selected, at least one whole pack (100g) must be purchased.
    *   **No Max Limits:** There are no upper bounds on the quantity of any specific protein or vegetable.
4.  **Data:**
    *   **Proteins (per 100g):**
        *   Chicken: 23g protein, $3.00
        *   Salmon: 20g protein, $5.00
        *   Tofu: 8g protein, $1.50
    *   **Vegetables (per 100g pack):**
        *   Broccoli: 2.8g protein, $1.20
        *   Carrots: 0.9g protein, $0.80
        *   Spinach: 2.9g protein, $1.50
        *   Bell Pepper: 1.0g protein, $1.00
        *   Mushrooms: 3.1g protein, $2.00