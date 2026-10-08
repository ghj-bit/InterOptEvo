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

QUESTION: Are the meats (salmon, beef, pork) allowed in the dinner, or should the meal be limited to the four vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The meats are allowed. In fact, the meal must include exactly one protein source from salmon, beef, or pork.

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" rule, does it mean exactly one of the three meats is chosen (with any amount), or exactly one meat type at a fixed portion size?

## Turn 2 - User Simulator

It means exactly one of the three meat types is chosen, with any amount.

## Turn 3 - Generic Agent

QUESTION: The fiber table only lists values for the four vegetables and none for the meats — should I treat the fiber content of salmon, beef, and pork as zero grams per 100g?

## Turn 3 - User Simulator

Yes, treat the fiber content of salmon, beef, and pork as zero grams per 100g.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum or maximum amount for each food (for example, a minimum portion of the chosen meat, or a cap on any single ingredient), or can every selected food range from 0 up to whatever the 600g total allows?

## Turn 4 - User Simulator

There is no minimum or maximum amount for each food. Every selected food can range from 0 up to whatever the 600g total allows.

## Turn 5 - Generic Agent

QUESTION: If the chosen meat has zero fiber, does the 600g total weight still have to be met exactly (so the meat counts toward the 600g even though it adds no fiber), or should the 600g be met by the vegetables only?

## Turn 5 - User Simulator

The 600g total weight must be met exactly by all selected foods, including the meat. The meat counts toward the 600g even though it adds no fiber.

## Turn 6 - Generic Agent

QUESTION: Is the $15 budget a hard ceiling (total cost must be ≤ $15), or should the spending be as close to $15 as possible?

## Turn 6 - User Simulator

The $15 budget is a hard ceiling. The total cost must be less than or equal to $15.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** grams of each of the 7 foods (salmon, beef, pork, okra, carrots, celery, cabbage), all continuous and ≥ 0.
- **Protein rule:** exactly one of the three meats (salmon, beef, pork) is chosen, with any amount (the other two meats are 0).
- **Weight constraint:** total weight of all selected foods must equal exactly 600 g (meat counts toward the 600 g).
- **Budget constraint:** total cost ≤ $15 (hard ceiling).
- **Objective:** maximize total fiber intake.
- **Fiber per 100 g:** okra 3.2, carrots 2.7, cabbage 2.0, celery 1.6; salmon, beef, pork = 0.
- **Price per 100 g:** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **No per-food minimums or maximums** beyond the 600 g total and the budget.