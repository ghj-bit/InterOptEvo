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

QUESTION: Are salmon, beef, and pork available as selectable foods for this dinner, or is the menu limited to the four fiber-containing vegetables (okra, carrots, celery, and cabbage)?

## Turn 1 - User Simulator

Salmon, beef, and pork are available as selectable foods. The menu is not limited to the four vegetables; you can choose from all seven items (the three proteins and the four vegetables).

## Turn 2 - Generic Agent

QUESTION: Do the three proteins (salmon, beef, and pork) have any fiber content per 100g that should be included in the fiber maximization objective, or should their fiber contribution be treated as zero?

## Turn 2 - User Simulator

The fiber contribution for salmon, beef, and pork should be treated as zero.

## Turn 3 - Generic Agent

QUESTION: Is the total weight constraint of 600 grams a strict equality (the selected foods must sum to exactly 600 grams) or a maximum ceiling (the selected foods must not exceed 600 grams)?

## Turn 3 - User Simulator

The total weight constraint is a strict equality; the selected foods must sum to exactly 600 grams.

## Turn 4 - Generic Agent

QUESTION: Are the quantities of each food allowed to be any continuous non-negative amount (for example, 137.5 grams of okra), or must each selected food be chosen in whole 100-gram units?

## Turn 4 - User Simulator

The quantities of each food can be any continuous non-negative amount.

## Turn 5 - Generic Agent

QUESTION: Is the $15 budget a strict ceiling (total cost must be less than or equal to $15) or an exact target (total cost must equal exactly $15)?

## Turn 5 - User Simulator

The $15 budget is a strict ceiling; the total cost must be less than or equal to $15.

## Turn 6 - Generic Agent

QUESTION: Are there any additional requirements on the selection, such as a minimum quantity for any food, a maximum quantity for any food, a requirement to include at least one protein, or a limit on how many of the seven foods can be chosen?

## Turn 6 - User Simulator

Yes, there are two additional requirements:

1. Exactly one protein source (salmon, beef, or pork) must be selected.
2. At least two different kinds of vegetables from okra, carrots, celery, and cabbage must be selected.

## Turn 7 - Generic Agent

QUESTION: For the requirement that exactly one protein source must be selected, does "selected" mean the chosen protein must have a strictly positive quantity (greater than zero grams), or is it acceptable for the chosen protein to have a quantity of zero grams as long as the other two proteins are zero?

## Turn 7 - User Simulator

"Selected" means the chosen protein must have a strictly positive quantity (greater than zero grams).

## Turn 8 - Generic Agent

QUESTION: For the requirement that at least two different kinds of vegetables must be selected, does "selected" mean each of those vegetables must have a strictly positive quantity (greater than zero grams)?

## Turn 8 - User Simulator

Yes, "selected" means each of those vegetables must have a strictly positive quantity (greater than zero grams).

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total fiber intake.
- Decision variables: Continuous, non-negative quantities (in grams) for each of the seven foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- Fiber content per 100g: Okra 3.2g, Carrots 2.7g, Celery 1.6g, Cabbage 2.0g, Salmon 0g, Beef 0g, Pork 0g.
- Price per 100g: Salmon $4, Beef $3.6, Pork $1.8, Okra $2.6, Carrots $1.2, Celery $1.6, Cabbage $2.3.
- Weight constraint: The sum of the quantities of all selected foods must equal exactly 600 grams.
- Budget constraint: The total cost of all selected foods must be less than or equal to $15.
- Protein constraint: Exactly one of salmon, beef, or pork must have a strictly positive quantity, and the other two must have a quantity of zero.
- Vegetable constraint: At least two of okra, carrots, celery, or cabbage must have a strictly positive quantity.

Assumptions:
- None. All formulation-critical facts have been confirmed.