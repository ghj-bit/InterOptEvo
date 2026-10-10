# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U2, U9, U10, U3, U4, U5, U6
I need help planning dinner tonight, with the goal to maximize fiber intake, subject to the constraints that the total cost of selected foods must not exceed the budget of $15 and the total weight must equal 600 grams.

Fiber content per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g.

Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.

Budget: $15.

Total food intake target: 600 grams.

## Problem units
- U1 (context): I need help planning dinner tonight.
- U2 (objective): Maximize fiber intake.
- U3 (data): Fiber content per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g.
- U4 (data): Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- U5 (data): Budget: $15.
- U6 (data): Total food intake target: 600 grams.
- U7 (constraint): Exactly one protein source (salmon, beef, or pork) is selected.
- U8 (constraint): At least two kinds of vegetables from okra, carrots, celery, and cabbage are selected.
- U9 (constraint): Total cost of selected foods must not exceed the budget of $15.
- U10 (constraint): Total weight of selected foods must equal 600 grams.

## Hidden slot scoring rules
## H1: protein_selection_rule
- Severity: P1
- Severity reason: Without this information, the agent would assume any combination of protein sources is allowed, leading to a model that does not enforce the intended discrete choice structure and could select multiple proteins. This would make the model materially inaccurate for the user’s actual dinner planning problem.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must explicitly ask about the rule for selecting protein sources, such as whether exactly one protein must be chosen, or whether multiple proteins can be combined.
- Reference acceptable questions:
  - Are there any restrictions on how many types of protein I can choose? Should I pick exactly one?
  - Do I have to choose exactly one protein from salmon, beef, and pork, or can I combine them?
- Failure modes:
  - Assuming that any combination of proteins with continuous amounts is allowed.
  - Assuming that no protein is required.
  - Assuming that all three proteins must be included.

## H2: min_vegetable_types
- Severity: P1
- Severity reason: Without this information, the agent could allow selecting only one vegetable type, which would not satisfy the user’s requirement for variety and could produce a meal plan without sufficient vegetable diversity, leading to a materially different solution.
- Problem unit ID: U8
- Semantic hit rule: The agent's question must explicitly ask about the minimum number of vegetable types, such as whether at least two different vegetables must be selected.
- Reference acceptable questions:
  - Do I need to include at least a certain number of different vegetables? For example, must I pick at least two kinds?
  - Is there a minimum number of vegetable types I must choose from the list?
- Failure modes:
  - Assuming that only one type of vegetable can be selected.
  - Assuming that all four vegetables must be included.
  - Assuming that vegetables can be chosen arbitrarily without a minimum variety constraint.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are salmon, beef, and pork available as dinner options to be selected alongside the vegetables, or are they excluded from the food choices for this meal?

## Turn 1 - User Simulator

They are available. I want to pick exactly one protein source from salmon, beef, or pork to include in the meal plan alongside the vegetables.

## Turn 2 - Generic Agent

QUESTION: Is the total weight constraint of 600 grams a strict equality that must be met exactly, or is it a maximum limit that the total weight must not exceed?

## Turn 2 - User Simulator

It is a strict equality. The total weight of the selected foods must equal exactly 600 grams.

## Turn 3 - Generic Agent

QUESTION: Is the $15 budget a strict maximum limit that the total cost must not exceed, or is it a target that the total cost must equal exactly?

## Turn 3 - User Simulator

It is a maximum limit. The total cost of the selected foods must not exceed $15.

## Turn 4 - Generic Agent

QUESTION: Are the quantities of each food item allowed to be any non-negative continuous value, or must they be restricted to specific discrete units like whole servings or integer grams?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Should the model allow any non-negative continuous amount of each food item, or must the amounts be restricted to whole integer grams?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any additional requirements or restrictions on the meal plan, such as minimum or maximum amounts for specific foods, or rules about which foods must or must not be included?

## Turn 6 - User Simulator

Yes. Two additional requirements:

1. Exactly one protein source from salmon, beef, or pork must be selected.
2. At least two different kinds of vegetables from okra, carrots, celery, and cabbage must be selected.

## Turn 7 - Generic Agent

QUESTION: For the requirement that at least two different kinds of vegetables must be selected, does "selected" mean that the amount of each chosen vegetable must be strictly greater than zero, or is a non-negative amount (including zero) sufficient to count a vegetable as selected?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Does the requirement to select exactly one protein source mean that the amount of the chosen protein must be strictly greater than zero, or is a non-negative amount (including zero) sufficient to count the protein as selected?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the fiber content data provided for salmon, beef, and pork, or is the fiber intake calculated only from the vegetables?

## Turn 9 - User Simulator

The fiber intake is calculated only from the vegetables.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total fiber intake.
2.  **Fiber Source:** Fiber is calculated only from the vegetables (okra, carrots, celery, cabbage). Proteins (salmon, beef, pork) contribute 0g fiber.
3.  **Decision Variables:** The weight (in grams) of each of the 7 food items (salmon, beef, pork, okra, carrots, celery, cabbage).
4.  **Variable Domain:** Continuous, non-negative values (assumed, as the user did not confirm integer restrictions).
5.  **Protein Constraint:** Exactly one protein source (salmon, beef, or pork) must be selected. This implies the amount of the chosen protein is strictly greater than zero, and the amounts of the other two proteins are zero. (Assumed strict positivity for "selected" based on standard interpretation, though user did not explicitly confirm).
6.  **Vegetable Constraint:** At least two different kinds of vegetables (from okra, carrots, celery, cabbage) must be selected. This implies the amount of each chosen vegetable is strictly greater than zero. (Assumed strict positivity for "selected" based on standard interpretation, though user did not explicitly confirm).
7.  **Weight Constraint:** The sum of the weights of all selected foods must equal exactly 600 grams.
8.  **Budget Constraint:** The sum of the costs of all selected foods must not exceed $15.
9.  **Data:**
    *   **Fiber (per 100g):** Okra 3.2g, Carrots 2.7g, Celery 1.6g, Cabbage 2.0g. Proteins: 0g.
    *   **Price (per 100g):** Salmon $4.0, Beef $3.6, Pork $1.8, Okra $2.6, Carrots $1.2, Celery $1.6, Cabbage $2.3.

**Explicit Assumptions:**
*   Food quantities are continuous and non-negative.
*   "Selected" for proteins and vegetables implies a strictly positive amount (> 0g).
*   Proteins contribute no fiber to the objective function.