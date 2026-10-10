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

QUESTION: Should the 600-gram total weight constraint be treated as an exact equality (the selected foods must sum to exactly 600 grams) or as a maximum ceiling (the selected foods must not exceed 600 grams)?

## Turn 1 - User Simulator

It should be treated as an exact equality. The selected foods must sum to exactly 600 grams.

## Turn 2 - Generic Agent

QUESTION: Should the decision variables representing the amount of each food be continuous (allowing any fractional gram amount) or must they be restricted to integer gram values?

## Turn 2 - User Simulator

The decision variables should be continuous, allowing any fractional gram amount.

## Turn 3 - Generic Agent

QUESTION: Should the model allow selecting zero grams of any food, or is there a minimum amount that must be selected for each food that is included in the plan?

## Turn 3 - User Simulator

The model should allow selecting zero grams of any food. There is no minimum amount that must be selected for each food that is included in the plan.

## Turn 4 - Generic Agent

QUESTION: The brief lists fiber content only for okra, carrots, celery, and cabbage, but also lists prices for salmon, beef, and pork. Should salmon, beef, and pork be treated as available foods with zero fiber content, or should they be excluded from the model entirely?

## Turn 4 - User Simulator

Salmon, beef, and pork should be treated as available foods with zero fiber content.

## Turn 5 - Generic Agent

QUESTION: Should the total cost constraint be treated as a strict ceiling (total cost must be less than or equal to $15) or as an exact equality (total cost must equal exactly $15)?

## Turn 5 - User Simulator

The total cost constraint should be treated as a strict ceiling. The total cost must be less than or equal to $15.

## Turn 6 - Generic Agent

QUESTION: Should the fiber content values (e.g., okra 3.2g per 100g) be interpreted as the fiber content per 100 grams of the food as purchased, or per 100 grams of the edible portion after any preparation?

## Turn 6 - User Simulator

The fiber content values should be interpreted as the fiber content per 100 grams of the food as purchased.

## Turn 7 - Generic Agent

QUESTION: Should the price values (e.g., salmon $4 per 100g) be interpreted as the cost per 100 grams of the food as purchased, matching the fiber content basis?

## Turn 7 - User Simulator

Yes, the price values should be interpreted as the cost per 100 grams of the food as purchased, matching the fiber content basis.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total fiber intake.
- Decision variables: Continuous, non-negative amounts (in grams) of each of the seven foods: salmon, beef, pork, okra, carrots, celery, and cabbage.
- Fiber content (per 100g as purchased): okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g, salmon 0g, beef 0g, pork 0g.
- Price (per 100g as purchased): salmon $4.00, beef $3.60, pork $1.80, okra $2.60, carrots $1.20, celery $1.60, cabbage $2.30.
- Weight constraint: The sum of the selected food amounts must equal exactly 600 grams.
- Budget constraint: The total cost of the selected foods must be less than or equal to $15.
- Zero selection is allowed for any food; there are no minimum inclusion requirements.
- All fiber and price values are based on the food as purchased.

No open assumptions remain.