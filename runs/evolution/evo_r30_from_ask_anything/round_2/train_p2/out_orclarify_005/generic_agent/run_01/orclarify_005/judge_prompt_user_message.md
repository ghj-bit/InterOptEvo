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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage), or are the three meats (salmon, beef, pork) excluded from the dinner plan because they have no fiber content listed?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) are included in the dinner plan. I want to pick exactly one protein source from those three.

## Turn 2 - Generic Agent

QUESTION: For the fiber objective, should I treat the fiber content of salmon, beef, and pork as 0 grams per 100g, or do you have specific fiber values for those meats that I should use?

## Turn 2 - User Simulator

Treat the fiber content of salmon, beef, and pork as 0 grams per 100g.

## Turn 3 - Generic Agent

QUESTION: Regarding the constraint that the total weight must equal 600 grams, should this be a strict equality constraint (total weight exactly 600g) or an upper bound constraint (total weight at most 600g)?

## Turn 3 - User Simulator

It should be a strict equality constraint: total weight exactly 600 grams.

## Turn 4 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, should the model allow any positive amount of the chosen protein (e.g., 10g of salmon) or must the chosen protein have a minimum weight (e.g., at least 100g)?

## Turn 4 - User Simulator

The model should allow any positive amount of the chosen protein. There is no minimum weight requirement.

## Turn 5 - Generic Agent

QUESTION: Should the amounts of each food be allowed to be any continuous value (e.g., 123.45 grams of okra), or must they be restricted to whole grams or some other discrete unit?

## Turn 5 - User Simulator

The amounts of each food can be any continuous value.

## Turn 6 - Generic Agent

QUESTION: Should the model allow zero grams of any of the four fiber-containing vegetables (okra, carrots, celery, cabbage), or must each of them be included with a positive amount?

## Turn 6 - User Simulator

The model should allow zero grams of any of the four fiber-containing vegetables, as long as at least two different kinds of vegetables are included with a positive amount.

## Turn 7 - Generic Agent

QUESTION: Should the model allow zero grams of the chosen protein source, or must the selected protein have a strictly positive amount?

## Turn 7 - User Simulator

The selected protein must have a strictly positive amount.

## Turn 8 - Generic Agent

QUESTION: Is the $15 budget a strict upper bound (total cost must be less than or equal to $15) or must the total cost be exactly $15?

## Turn 8 - User Simulator

The $15 budget is a strict upper bound: total cost must be less than or equal to $15.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Maximize total fiber intake (in grams).
- **Decision Variables:** Continuous, non-negative weights (in grams) for each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- **Protein Constraint:** Exactly one of {salmon, beef, pork} must be selected with a strictly positive weight; the other two must be zero.
- **Vegetable Constraint:** At least two of {okra, carrots, celery, cabbage} must be included with a strictly positive weight; the others may be zero.
- **Weight Constraint:** Total weight of all selected foods must equal exactly 600 grams.
- **Budget Constraint:** Total cost of all selected foods must be less than or equal to $15.
- **Fiber Content (per 100g):** Salmon 0g, Beef 0g, Pork 0g, Okra 3.2g, Carrots 2.7g, Celery 1.6g, Cabbage 2.0g.
- **Price (per 100g):** Salmon $4, Beef $3.6, Pork $1.8, Okra $2.6, Carrots $1.2, Celery $1.6, Cabbage $2.3.
- **Variable Domain:** All weights are continuous and non-negative.

**Open Assumptions:** None. All formulation-critical facts have been confirmed.