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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any amount, or are the three meats (salmon, beef, pork) excluded from the dinner selection?

## Turn 1 - User Simulator

The three meats are not excluded. I want to include exactly one protein source from salmon, beef, or pork in the dinner plan.

## Turn 2 - Generic Agent

QUESTION: When you say "exactly one protein source," do you mean that the total weight of the chosen meat must be a single positive amount (with the other two meats at zero), or that you must pick exactly one meat type and then choose its weight freely?

## Turn 2 - User Simulator

I mean that you must pick exactly one meat type and then choose its weight freely, with the other two meats at zero.

## Turn 3 - Generic Agent

QUESTION: For the vegetables (okra, carrots, celery, cabbage), can you select any combination of them in any non-negative amounts, or are there any restrictions on which vegetables must or must not be included?

## Turn 3 - User Simulator

There is one restriction: the meal must include at least two different kinds of vegetables from okra, carrots, celery, and cabbage.

## Turn 4 - Generic Agent

QUESTION: When you say the meal must include at least two different kinds of vegetables, does that mean at least two vegetable types must have a strictly positive weight, or is it acceptable for one of the selected vegetable types to have zero weight as long as two others are present?

## Turn 4 - User Simulator

It means at least two vegetable types must have a strictly positive weight.

## Turn 5 - Generic Agent

QUESTION: Is the total weight constraint of 600 grams a strict equality (the total must be exactly 600 grams) or a maximum (the total must be no more than 600 grams)?

## Turn 5 - User Simulator

It is a strict equality: the total weight must be exactly 600 grams.

## Turn 6 - Generic Agent

QUESTION: Is the budget constraint of $15 a strict maximum (total cost must be no more than $15) or a strict equality (total cost must be exactly $15)?

## Turn 6 - User Simulator

It is a strict maximum: the total cost must be no more than $15.

## Turn 7 - Generic Agent

QUESTION: Are the weights of the selected foods allowed to be any non-negative real number (continuous), or must they be chosen in discrete increments such as whole 100g units?

## Turn 7 - User Simulator

The weights can be any non-negative real number.

## Turn 8 - Generic Agent

QUESTION: Since the fiber content is only provided for the four vegetables (okra, carrots, celery, cabbage) and not for the three meats, should I assume that salmon, beef, and pork each contribute 0 grams of fiber per 100g to the objective?

## Turn 8 - User Simulator

Yes, assume that salmon, beef, and pork each contribute 0 grams of fiber per 100g.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total fiber intake (in grams).
- Decision variables: Continuous, non-negative weights (in grams) for each of the seven foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- Protein constraint: Exactly one of the three meats (salmon, beef, pork) must be selected with a strictly positive weight; the other two meats must have zero weight.
- Vegetable constraint: At least two of the four vegetable types (okra, carrots, celery, cabbage) must have a strictly positive weight.
- Total weight constraint: The sum of all selected food weights must equal exactly 600 grams.
- Budget constraint: The total cost of all selected foods must be no more than $15.
- Fiber content per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g, salmon 0g, beef 0g, pork 0g.
- Price per 100g: salmon $4.00, beef $3.60, pork $1.80, okra $2.60, carrots $1.20, celery $1.60, cabbage $2.30.
- All weights are continuous and non-negative.

No open assumptions remain; all formulation-critical facts have been confirmed.