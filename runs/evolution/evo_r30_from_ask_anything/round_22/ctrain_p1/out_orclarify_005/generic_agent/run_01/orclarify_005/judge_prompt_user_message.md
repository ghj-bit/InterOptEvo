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

QUESTION: Are salmon, beef, and pork available as selectable dinner options, or should the selection be restricted to the four vegetable items (okra, carrots, celery, and cabbage) that have fiber data provided?

## Turn 1 - User Simulator

Salmon, beef, and pork are available as selectable dinner options. You should include exactly one of those three protein sources in the meal plan, along with at least two of the four vegetable items.

## Turn 2 - Generic Agent

QUESTION: Is the total weight constraint of 600 grams a strict equality that the selected foods must sum to exactly, or is it a maximum ceiling that the total weight must not exceed?

## Turn 2 - User Simulator

The total weight constraint is a strict equality. The selected foods must sum to exactly 600 grams.

## Turn 3 - Generic Agent

QUESTION: For the fiber content of the three protein sources (salmon, beef, and pork), should I treat their fiber contribution as zero grams per 100 grams since no fiber data was provided for them?

## Turn 3 - User Simulator

Yes, treat the fiber contribution of salmon, beef, and pork as zero grams per 100 grams.

## Turn 4 - Generic Agent

QUESTION: Is the budget of $15 a strict ceiling that the total cost must not exceed, or is it a target that the total cost should equal exactly?

## Turn 4 - User Simulator

The budget of $15 is a strict ceiling. The total cost of selected foods must not exceed $15.

## Turn 5 - Generic Agent

QUESTION: Are the quantities of each selected food item allowed to be any continuous non-negative amount, or must they be chosen in discrete increments such as whole 100-gram units?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Should the quantity of each selected food item be modeled as a continuous non-negative amount measured in grams, or as an integer number of 100-gram units?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there a minimum or maximum weight limit that applies to each individual food item selected in the meal plan?

## Turn 7 - User Simulator

No, there is no minimum or maximum weight limit that applies to each individual food item.

## Turn 8 - Generic Agent

QUESTION: Is the requirement to include at least two of the four vegetable items a hard constraint that must be satisfied, or is it a soft preference that can be relaxed if needed to meet the other constraints?

## Turn 8 - User Simulator

It is a hard constraint that must be satisfied.

## Turn 9 - Generic Agent

QUESTION: Is the requirement to include exactly one of the three protein sources a hard constraint that must be satisfied, or is it a soft preference that can be relaxed if needed to meet the other constraints?

## Turn 9 - User Simulator

It is a hard constraint that must be satisfied.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total fiber intake (in grams).
- Decision variables: Continuous, non-negative weight (in grams) for each of the seven food items: salmon, beef, pork, okra, carrots, celery, cabbage.
- Fiber content per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g, salmon 0g, beef 0g, pork 0g.
- Price per 100g: salmon $4.0, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- Constraint 1 (Budget): Total cost of selected foods must not exceed $15 (ceiling).
- Constraint 2 (Weight): Total weight of selected foods must equal exactly 600 grams (equality).
- Constraint 3 (Protein selection): Exactly one of salmon, beef, or pork must be included with positive weight.
- Constraint 4 (Vegetable selection): At least two of okra, carrots, celery, or cabbage must be included with positive weight.
- No individual item has a minimum or maximum weight limit beyond non-negativity.

Assumptions:
- The quantity of each food item is treated as a continuous non-negative variable (in grams), as the user did not confirm discrete units. This is flagged as an open assumption.