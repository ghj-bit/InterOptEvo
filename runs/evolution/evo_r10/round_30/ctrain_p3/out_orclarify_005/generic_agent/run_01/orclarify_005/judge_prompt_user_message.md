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

QUESTION: Should the 600-gram total weight include all foods (both the meats and the vegetables), or only the vegetables?

## Turn 1 - User Simulator

The 600-gram total weight includes all foods, both the meats and the vegetables.

## Turn 2 - Generic Agent

QUESTION: Are the amounts of each food allowed to be any continuous weight (e.g., 137.5 g of okra), or must each food be chosen in whole 100-gram units?

## Turn 2 - User Simulator

The amounts of each food can be any continuous weight.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum or maximum amount required for any specific food (e.g., must include at least some salmon, or no more than a certain amount of beef), or can any food be chosen in any amount from zero up to the total?

## Turn 3 - User Simulator

There are no minimum or maximum amounts required for any specific food.

## Turn 4 - Generic Agent

QUESTION: Is the $15 budget a hard cap (total cost must be at most $15, with any leftover money simply unused), or must the spending come out to exactly $15?

## Turn 4 - User Simulator

The $15 budget is a hard cap; the total cost must be at most $15, and any leftover money is simply unused.

## Turn 5 - Generic Agent

QUESTION: The fiber content is only given for the four vegetables (okra, carrots, celery, cabbage) — should I treat the meats (salmon, beef, pork) as contributing zero fiber to the objective?

## Turn 5 - User Simulator

Yes, treat the meats (salmon, beef, pork) as contributing zero fiber to the objective.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** continuous, nonnegative weight (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage. No minimum or maximum on any individual food.
- **Objective:** maximize total fiber intake. Fiber per 100 g: okra 3.2, carrots 2.7, celery 1.6, cabbage 2.0; meats contribute 0 fiber.
- **Weight constraint:** total weight of all foods (meats + vegetables) must equal exactly 600 g.
- **Budget constraint:** total cost must be at most $15 (hard cap; leftover money unused). Cost per 100 g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **No other constraints** (no per-food bounds, no exact-spending requirement).

This is a linear program: maximize a linear fiber objective over a continuous polytope defined by one equality (weight = 600 g) and one inequality (cost ≤ $15), with nonnegativity.