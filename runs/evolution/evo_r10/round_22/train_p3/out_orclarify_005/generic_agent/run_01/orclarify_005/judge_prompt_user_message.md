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

QUESTION: The fiber data is only given for the four vegetables (okra, carrots, celery, cabbage), while the three meats (salmon, beef, pork) have no fiber listed — should I treat the meats as having zero fiber, or are they not allowed in the meal at all?

## Turn 2 - User Simulator

The meats are allowed in the meal. You should treat them as having zero fiber.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum or maximum amount limits for any individual food (for example, a minimum portion of meat, or a cap on how much of one vegetable you can use), or can each food be chosen in any amount from zero up to the 600g total?

## Turn 3 - User Simulator

There are no minimum or maximum amount limits for any individual food. Each food can be chosen in any amount from zero up to the 600g total, subject to the other constraints.

## Turn 4 - Generic Agent

QUESTION: Can the amounts of each food be any fractional value (for example, 137.5 grams of okra), or must each food be chosen in whole-gram (or whole-100g) increments?

## Turn 4 - User Simulator

The amounts can be any fractional value. There is no requirement to use whole-gram or whole-100g increments.

## Turn 5 - Generic Agent

QUESTION: Is the $15 budget a hard ceiling (total cost must be at most $15), or should I also treat it as something to use up as much as possible?

## Turn 5 - User Simulator

The $15 budget is a hard ceiling. The total cost must be at most $15.

## Turn 6 - Generic Agent

QUESTION: If multiple food combinations achieve the same maximum fiber intake, is there any tie-breaker preference (for example, prefer cheaper meals, prefer including meat, or prefer fewer distinct foods), or is any optimal combination acceptable?

## Turn 6 - User Simulator

Any optimal combination is acceptable. There is no tie-breaker preference.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize total fiber intake from the selected foods.
- **Foods available:** salmon, beef, pork, okra, carrots, celery, cabbage. Each can be chosen in any fractional amount from 0 up to the total.
- **Fiber (per 100g):** okra 3.2g, carrots 2.7g, cabbage 2.0g, celery 1.6g; salmon, beef, pork = 0g.
- **Price (per 100g):** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Constraints:**
  - Total weight of selected foods must equal **exactly 600g**.
  - Total cost must be **at most $15** (hard ceiling).
  - No per-food minimum or maximum limits.
- **Variables:** continuous (fractional grams allowed).
- **Tie-breaking:** none — any optimal combination is acceptable.

This is a linear program: maximize fiber subject to an exact weight equality and a cost upper bound, with nonnegative continuous variables.