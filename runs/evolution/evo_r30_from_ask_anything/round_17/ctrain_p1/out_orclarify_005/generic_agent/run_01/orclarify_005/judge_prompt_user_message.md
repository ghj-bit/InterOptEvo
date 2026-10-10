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

QUESTION: Are salmon, beef, and pork available as options for this dinner, or should the selection be restricted to the four fiber-containing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

Salmon, beef, and pork are available as options. You should include exactly one of those three protein sources in the meal plan, along with at least two of the four vegetables.

## Turn 2 - Generic Agent

QUESTION: For the "at least two of the four vegetables" requirement, does this mean you must select at least two distinct vegetable types (each with a positive amount), or is it acceptable to select only one vegetable type as long as the total vegetable weight is at least 200 grams?

## Turn 2 - User Simulator

It means you must select at least two distinct vegetable types, each with a positive amount.

## Turn 3 - Generic Agent

QUESTION: For the "exactly one of those three protein sources" requirement, does this mean you must select exactly one distinct protein type (salmon, beef, or pork) with a positive amount, or is it acceptable to select none of the three proteins as long as the vegetable requirement is met?

## Turn 3 - User Simulator

It means you must select exactly one distinct protein type (salmon, beef, or pork) with a positive amount.

## Turn 4 - Generic Agent

QUESTION: Is the total weight constraint of 600 grams a strict equality (the sum of all selected food weights must be exactly 600 grams), or is it a maximum (the sum must be at most 600 grams)?

## Turn 4 - User Simulator

It is a strict equality: the sum of all selected food weights must be exactly 600 grams.

## Turn 5 - Generic Agent

QUESTION: Is the budget constraint of $15 a strict ceiling (the total cost must be at most $15), or is it a strict equality (the total cost must be exactly $15)?

## Turn 5 - User Simulator

It is a strict ceiling: the total cost must be at most $15.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum or maximum weight limits for each individual food item (e.g., a minimum portion size for the protein or for each vegetable), or can any selected food have any positive weight as long as the total is exactly 600 grams?

## Turn 6 - User Simulator

There are no minimum or maximum weight limits for each individual food item. Any selected food can have any positive weight as long as the total is exactly 600 grams.

## Turn 7 - Generic Agent

QUESTION: Should the fiber intake calculation include only the fiber from the selected vegetables, or should I also account for any fiber content in the selected protein (salmon, beef, or pork)?

## Turn 7 - User Simulator

The fiber intake calculation should include only the fiber from the selected vegetables.

## Turn 8 - Generic Agent

QUESTION: Are the food weights and costs continuous variables (meaning you can select any fractional amount of a food, like 123.45 grams), or must the weights be whole numbers (integer grams)?

## Turn 8 - User Simulator

The food weights and costs are continuous variables, meaning you can select any fractional amount of a food.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total fiber intake.
2.  **Fiber Source:** Fiber is calculated only from the selected vegetables (okra, carrots, celery, cabbage). Proteins (salmon, beef, pork) contribute 0g fiber.
3.  **Decision Variables:** Continuous, non-negative weights (in grams) for each of the 7 food items.
4.  **Protein Constraint:** Exactly one of the three proteins (salmon, beef, pork) must be selected with a positive weight. The other two must have zero weight.
5.  **Vegetable Constraint:** At least two of the four vegetables (okra, carrots, celery, cabbage) must be selected with a positive weight.
6.  **Total Weight Constraint:** The sum of the weights of all selected foods must be exactly 600 grams.
7.  **Budget Constraint:** The total cost of all selected foods must be less than or equal to $15.
8.  **Data:**
    *   **Fiber (per 100g):** Okra 3.2g, Carrots 2.7g, Celery 1.6g, Cabbage 2.0g.
    *   **Price (per 100g):** Salmon $4.0, Beef $3.6, Pork $1.8, Okra $2.6, Carrots $1.2, Celery $1.6, Cabbage $2.3.
9.  **Assumptions:**
    *   No minimum or maximum weight limits for individual items other than the "positive weight" requirement for selected items.
    *   Weights are continuous variables.