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

QUESTION: Should the 600-gram total weight be an exact equality (the selected foods must weigh exactly 600g) or a maximum (at most 600g)?

## Turn 1 - User Simulator

It must be an exact equality. The total weight of the selected foods must equal exactly 600 grams.

## Turn 2 - Generic Agent

QUESTION: The fiber data is only given for okra, carrots, celery, and cabbage, but the price list also includes salmon, beef, and pork — should salmon, beef, and pork be selectable foods in the plan (with zero fiber), or are they excluded and only the four vegetables can be chosen?

## Turn 2 - User Simulator

Salmon, beef, and pork are selectable foods in the plan. They have zero fiber, but they are included as protein sources.

## Turn 3 - Generic Agent

QUESTION: Can you select any amount of each food (continuous quantities in grams), or must each food be chosen in fixed portions (e.g., whole 100g units)?

## Turn 3 - User Simulator

You can select any amount of each food in continuous quantities (grams).

## Turn 4 - Generic Agent

QUESTION: Is there any minimum or maximum amount that must be selected for each food (e.g., at least some of each, or a cap on any single food), or can any food be selected in any amount from 0 grams up to the full 600 grams?

## Turn 4 - User Simulator

There are no minimum or maximum amounts for individual foods. Any food can be selected in any amount from 0 grams up to the full 600 grams, subject to the other constraints.

## Turn 5 - Generic Agent

QUESTION: Is the $15 budget a hard cap (total cost must be at most $15, with any leftover budget simply unused), or must the total cost also equal exactly $15?

## Turn 5 - User Simulator

The $15 budget is a hard cap. The total cost must be at most $15, and any leftover budget is simply unused.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize total fiber intake (in grams).
- **Foods (7):** salmon, beef, pork, okra, carrots, celery, cabbage.
- **Decision variables:** continuous quantity (in grams) of each food, each ≥ 0, with no individual minimum or maximum.
- **Fiber content per 100g:** okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g; salmon, beef, pork = 0g fiber.
- **Price per 100g:** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Constraints:**
  1. Total weight must equal exactly 600 grams (equality).
  2. Total cost must be at most $15 (hard cap; leftover budget unused).
- **Objective:** Maximize total fiber = sum over foods of (grams / 100) × fiber-per-100g.

This is a linear program: 7 continuous non-negative variables, one equality constraint (weight = 600g), one inequality constraint (cost ≤ $15), and a linear objective (maximize fiber).