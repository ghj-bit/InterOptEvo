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

QUESTION: For the protein options (chicken, salmon, tofu), are you allowed to purchase any continuous weight (for example, 150 grams of chicken), or must the protein also be bought in discrete units such as 100-gram portions

## Turn 1 - User Simulator

You can buy the protein options in any continuous weight. For example, you could purchase 150 grams of chicken. They do not need to be bought in discrete 100-gram portions.

## Turn 2 - Generic Agent

QUESTION: Is the $20 budget a hard ceiling that the total cost must not exceed, or is it a target that you would prefer to hit

## Turn 2 - User Simulator

The $20 budget is a hard ceiling. The total cost must not exceed $20.

## Turn 3 - Generic Agent

QUESTION: Is the 800-gram maximum total weight a hard ceiling that the combined weight of all protein and vegetables must not

## Turn 3 - User Simulator

Yes, the 800-gram maximum total weight is a hard ceiling. The combined weight of all protein and vegetables must not exceed 800 grams.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum quantity requirements for any specific protein or vegetable option, or can you choose to purchase zero of

## Turn 4 - User Simulator

There are no minimum quantity requirements for any specific protein or vegetable option. You can choose to purchase zero of any particular protein or vegetable, as long as you select at least three different types of vegetables overall.

## Turn 5 - Generic Agent

QUESTION: Does the requirement to select at least three different types of vegetables mean that you must purchase at least one 100g pack of each of those three

## Turn 5 - User Simulator

Yes, selecting at least three different types of vegetables means you must purchase at least one 100g pack of each of those three distinct vegetable types.

## Turn 6 - Generic Agent

QUESTION: Are there any upper limits on how many 100g packs of any single vegetable type you can

## Turn 6 - User Simulator

No, there are no upper limits on how many 100g packs of any single vegetable type you can purchase.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total number of different protein types you can

## Turn 7 - User Simulator

No, there is no limit on the total number of different protein types you can include.

## Turn 8 - Generic Agent

QUESTION: Is there any requirement to include at least one type of protein in the

## Turn 8 - User Simulator

No, there is no requirement to include at least one type of protein.

## Turn 9 - Generic Agent

QUESTION: Are the protein and vegetable costs and protein contents provided per 100g of actual food weight, meaning that if you buy 150g of chicken it costs $4.50 and provides 34.5g of

## Turn 9 - User Simulator

Yes, the costs and protein contents are per 100g of actual food weight. So, 150g of chicken would cost $4.50 and provide 34.5g of protein.

## Turn 10 - Generic Agent

QUESTION: Is the objective to maximize the total grams of protein from both the protein options and the vegetable

## Turn 10 - User Simulator

Yes, the objective is to maximize the total grams of protein from both the protein options and the vegetables.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total protein intake (grams) from both protein sources and vegetables.
2.  **Decision Variables:**
    *   **Proteins (Chicken, Salmon, Tofu):** Continuous, non-negative variables representing weight in grams.
    *   **Vegetables (Broccoli, Carrots, Spinach, Bell Pepper, Mushrooms):** Non-negative integer variables representing the number of 100g packs.
3.  **Constraints:**
    *   **Budget:** Total cost $\le$ $20.00 (Hard ceiling).
    *   **Weight:** Total weight of all food $\le$ 800 grams (Hard ceiling).
    *   **Vegetable Diversity:** Must purchase at least one pack of at least three distinct vegetable types.
    *   **Non-negativity:** All variables $\ge$ 0.
4.  **Parameters (per 100g):**
    *   **Chicken:** 23g protein, $3.00
    *   **Salmon:** 20g protein, $5.00
    *   **Tofu:** 8g protein, $1.50
    *   **Broccoli:** 2.8g protein, $1.20
    *   **Carrots:** 0.9g protein, $0.80
    *   **Spinach:** 2.9g protein, $1.50
    *   **Bell Pepper:** 1.0g protein, $1.00
    *   **Mushrooms:** 3.1g protein, $2.00
5.  **Assumptions/Clarifications:**
    *   Protein can be bought in any continuous weight (e.g., 150g).
    *   Vegetables are sold only in whole 100g packs.
    *   No minimum quantity required for any specific protein or vegetable type, except for the "at least 3 distinct vegetable types" rule.
    *   No upper limit on the number of packs of any single vegetable.
    *   No requirement to include any protein type.
    *   Costs and protein values scale linearly with weight for proteins and are fixed per pack for vegetables.