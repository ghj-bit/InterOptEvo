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

QUESTION: Are salmon, beef, and pork available as selectable dinner items, or are they excluded from the menu and only the four vegetable items (okra, carrots, celery, cabbage) can be chosen?

## Turn 1 - User Simulator

Salmon, beef, and pork are available as selectable dinner items. You should include exactly one of them in the meal plan.

## Turn 2 - Generic Agent

QUESTION: Do salmon, beef, and pork have any fiber content per 100g that should be included in the fiber maximization objective, or should their fiber contribution be treated as zero?

## Turn 2 - User Simulator

The provided fiber data only lists okra, carrots, celery, and cabbage. The fiber contribution for salmon, beef, and pork should be treated as zero.

## Turn 3 - Generic Agent

QUESTION: Is the 600-gram total weight constraint a strict equality (the selected foods must sum to exactly 600 grams) or a ceiling (the selected foods must not exceed 600 grams)?

## Turn 3 - User Simulator

The 600-gram total weight constraint is a strict equality. The selected foods must sum to exactly 600 grams.

## Turn 4 - Generic Agent

QUESTION: Is the $15 budget a strict ceiling (total cost must not exceed $15) or a strict equality (total cost must equal exactly $15)?

## Turn 4 - User Simulator

The $15 budget is a strict ceiling. The total cost must not exceed $15.

## Turn 5 - Generic Agent

QUESTION: Can the amounts of each selected food be any continuous non-negative value (for example, 137.5 grams of okra), or must the quantities be restricted to whole units such as whole 100-gram portions?

## Turn 5 - User Simulator

I need to confirm this internally.

## Turn 6 - Generic Agent

QUESTION: Is there a minimum or maximum weight limit for any individual food item in the meal, or can each selected food range from 0 grams up to the full 600 grams?

## Turn 6 - User Simulator

I need to confirm this internally.

## Turn 7 - Generic Agent

QUESTION: Are there any additional requirements beyond the budget, the 600-gram total, and the exactly-one-meat rule, such as a minimum amount of vegetables, a maximum amount of any single item, or a requirement that all four vegetables must be included?

## Turn 7 - User Simulator

Yes, there is one additional requirement: the meal must include at least two different kinds of vegetables from okra, carrots, celery, and cabbage.

## Turn 8 - Generic Agent

QUESTION: Is the requirement to include at least two different kinds of vegetables a hard constraint that must be strictly satisfied, or is it a soft target that can be relaxed if needed to meet the other constraints?

## Turn 8 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total fiber intake.
- Decision variables: Weight (in grams) of each of the seven foods (salmon, beef, pork, okra, carrots, celery, cabbage).
- Variable domain: Continuous, non-negative weights for each food. (Assumed: quantities can be any non-negative real number, not restricted to whole 100g portions, as this was not confirmed.)
- Meat selection: Exactly one of salmon, beef, or pork must be included (i.e., exactly one meat has positive weight, the other two have zero weight).
- Vegetable constraint: At least two different kinds of vegetables from {okra, carrots, celery, cabbage} must be included (i.e., at least two vegetables have positive weight).
- Total weight: Sum of all selected food weights must equal exactly 600 grams.
- Budget: Total cost of all selected foods must not exceed $15.
- Fiber content per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g; salmon, beef, pork = 0g.
- Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.

Open assumptions:
- Quantities are continuous (not restricted to discrete portions). This was not confirmed by the user.
- No individual food has a minimum or maximum weight limit beyond the overall 600g total and the non-negativity constraint. This was not confirmed by the user.