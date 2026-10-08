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

QUESTION: Should the 600-gram total weight be treated as an exact requirement (the selected foods must sum to exactly 600g), or as a maximum (the selected foods must not exceed 600g)?

## Turn 1 - User Simulator

It must be an exact requirement. The total weight of the selected foods must equal exactly 600 grams.

## Turn 2 - Generic Agent

QUESTION: The fiber content is only given for okra, carrots, celery, and cabbage, but the price list also includes salmon, beef, and pork — should salmon, beef, and pork be treated as having zero fiber (and thus selectable as fillers to hit the 600g and spend the budget), or should the dinner be restricted to only the four fiber-containing vegetables?

## Turn 2 - User Simulator

The dinner should not be restricted to only the four vegetables. Salmon, beef, and pork are selectable protein sources. They should be treated as having zero fiber for the purpose of maximizing fiber intake, but they are part of the meal plan to help meet the 600g weight requirement and stay within the budget.

## Turn 3 - Generic Agent

QUESTION: Are the food amounts continuous (you can select any fractional gram amount of each food), or must each food be selected in whole 100g units?

## Turn 3 - User Simulator

The food amounts are continuous. You can select any fractional gram amount of each food.

## Turn 4 - Generic Agent

QUESTION: Is there any upper limit on how much of any single food can be selected (for example, a maximum number of grams per food), or can each food be chosen in any non-negative amount up to the 600g total?

## Turn 4 - User Simulator

There is no upper limit on how much of any single food can be selected. Each food can be chosen in any non-negative amount, subject only to the total weight equaling 600 grams and the total cost not exceeding $15.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Continuous, non-negative amount (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- **Objective:** Maximize total fiber intake. Fiber per 100g: okra 3.2g, carrots 2.7g, cabbage 2.0g, celery 1.6g; salmon, beef, pork = 0g fiber.
- **Constraints:**
  - Total weight must equal exactly 600 grams (sum of all selected food amounts = 600).
  - Total cost must not exceed $15. Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **No per-food upper bounds** beyond the 600g total.
- **No integrality** — fractional grams allowed.

This is a linear program: maximize a linear fiber objective over a 600g equality and a $15 budget inequality, with 7 non-negative continuous variables.