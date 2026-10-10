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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in the dinner, or should the protein items (salmon, beef, pork) be excluded because they have no fiber content listed?

## Turn 1 - User Simulator

The model should allow selecting from all seven listed foods. The protein items (salmon, beef, pork) are part of the meal plan, even though they have no fiber content listed.

Please include exactly one protein source from salmon, beef, or pork in the dinner.

## Turn 2 - Generic Agent

QUESTION: When you say to include exactly one protein source, does that mean the dinner must contain a positive amount of exactly one of salmon, beef, or pork (with the other two at zero), or does it mean the dinner must contain at least one of them but could contain multiple?

## Turn 2 - User Simulator

It means the dinner must contain a positive amount of exactly one of salmon, beef, or pork, with the other two at zero.

## Turn 3 - Generic Agent

QUESTION: Should the amounts of each food be treated as continuous values (allowing any fractional gram), or must they be whole numbers of grams?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Should the amounts of each food be treated as continuous values (allowing any fractional gram), or must they be whole numbers of grams?

## Turn 4 - User Simulator

The amounts of each food should be treated as continuous values, allowing any fractional gram.

## Turn 5 - Generic Agent

QUESTION: Should the total weight of 600 grams be treated as a strict equality constraint (the total must be exactly 600 grams), or as a maximum limit (the total must be at most 600 grams)?

## Turn 5 - User Simulator

The total weight of 600 grams should be treated as a strict equality constraint. The total must be exactly 600 grams.

## Turn 6 - Generic Agent

QUESTION: Should the budget of $15 be treated as a maximum limit (total cost must be at most $15), or as a strict equality constraint (total cost must be exactly $15)?

## Turn 6 - User Simulator

The budget of $15 should be treated as a maximum limit. The total cost must be at most $15.

## Turn 7 - Generic Agent

QUESTION: For the protein items (salmon, beef, pork), should I assume their fiber content is 0 grams per 100 grams, since no fiber value was provided for them?

## Turn 7 - User Simulator

Yes, assume their fiber content is 0 grams per 100 grams.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total fiber intake.
- Decision variables: Continuous, non-negative amounts (in grams) for each of the seven foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- Protein constraint: Exactly one of salmon, beef, or pork must have a positive amount; the other two must be zero.
- Weight constraint: Total weight of all selected foods must equal exactly 600 grams.
- Budget constraint: Total cost of all selected foods must be at most $15.
- Fiber content per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g, salmon 0g, beef 0g, pork 0g.
- Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- All amounts are continuous (fractional grams allowed).
- All amounts are non-negative.