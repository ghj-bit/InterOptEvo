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

QUESTION: Should the dinner be limited to only the four fiber-containing vegetables (okra, carrots, celery, cabbage), or may the meats (salmon, beef, pork) also be selected as part of the 600g meal?

## Turn 1 - User Simulator

The meats may also be selected. In fact, the meal must include exactly one protein source from salmon, beef, or pork, along with at least two of the four vegetables.

## Turn 2 - Generic Agent

QUESTION: For the "at least two of the four vegetables" requirement, does each selected vegetable need a minimum amount (e.g., at least 100g), or is any positive amount of a vegetable enough to count it as selected?

## Turn 2 - User Simulator

Any positive amount of a vegetable is enough to count it as selected.

## Turn 3 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, does the chosen meat need a minimum amount (e.g., at least 100g), or is any positive amount of that meat enough to count it as the selected protein?

## Turn 3 - User Simulator

Any positive amount of the chosen meat is enough to count it as the selected protein.

## Turn 4 - Generic Agent

QUESTION: Since the total weight must equal exactly 600g, is it acceptable for the model to assign a tiny positive amount (e.g., a few grams) to a vegetable or the meat just to satisfy the "at least two vegetables" and "exactly one protein" rules, or should each selected item have a meaningful minimum portion?

## Turn 4 - User Simulator

A tiny positive amount is acceptable to satisfy the "at least two vegetables" and "exactly one protein" rules.

## Turn 5 - Generic Agent

QUESTION: Are the amounts of each food allowed to be any continuous (fractional) weight, or must they be in whole units such as 100g portions?

## Turn 5 - User Simulator

The amounts of each food can be any continuous (fractional) weight.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize total fiber intake (grams of fiber).
- **Foods available:** salmon, beef, pork (proteins); okra, carrots, celery, cabbage (vegetables).
- **Fiber per 100g:** okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g. (Proteins have no fiber listed, so they contribute 0 fiber.)
- **Price per 100g:** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Budget:** total cost ≤ $15.
- **Weight:** total weight of all selected foods = exactly 600g.
- **Protein rule:** exactly one of {salmon, beef, pork} is selected (any positive amount counts as selected; the other two are 0).
- **Vegetable rule:** at least two of {okra, carrots, celery, cabbage} are selected (any positive amount counts as selected).
- **Amounts:** continuous (fractional) weights in grams, non-negative.
- **Tiny positive amounts** are acceptable to satisfy the selection rules.

I will formulate this as a mixed-integer linear program: continuous weight variables for each food, binary selection variables for the meats (exactly one = 1) and vegetables (at least two = 1), with big-M linking so a food's weight is positive only if selected, and the objective maximizing total fiber.