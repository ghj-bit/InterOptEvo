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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any non-negative amounts, or are the three meats (salmon, beef, pork) excluded from the dinner and only the four vegetables (okra, carrots, celery, cabbage) may be chosen?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) are not excluded. The dinner plan must include exactly one protein source from those three, along with at least two kinds of vegetables from the list of okra, carrots, celery, and cabbage.

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, should the model enforce that the chosen protein has a strictly positive amount (e.g., at least 100g) while the other two meats are exactly zero, or is it acceptable for the chosen protein to end up at zero grams as long as the other two meats are zero?

## Turn 2 - User Simulator

The chosen protein must have a strictly positive amount. It is not acceptable for the selected protein to end up at zero grams.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, should each selected vegetable have a strictly positive amount (e.g., at least 100g) while unselected vegetables are exactly zero, or is it acceptable for a selected vegetable to end up at zero grams as long as at least two vegetable types are designated as selected?

## Turn 3 - User Simulator

Each selected vegetable must have a strictly positive amount. It is not acceptable for a designated vegetable to end up at zero grams.

## Turn 4 - Generic Agent

QUESTION: What is the minimum amount (in grams) that any selected food—whether the chosen protein or a selected vegetable—must have to count as "strictly positive"?

## Turn 4 - User Simulator

The business facts do not specify a minimum gram threshold for "strictly positive." This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: For the "total weight must equal 600 grams" constraint, should the model enforce that the sum of all selected food amounts is exactly 600 grams, or is it acceptable for the total to be at most 600 grams (i.e., ≤ 600g)?

## Turn 5 - User Simulator

The total weight must be exactly 600 grams.

## Turn 6 - Generic Agent

QUESTION: For the fiber content, the brief lists fiber per 100g only for the four vegetables (okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g). What is the fiber content per 100g for each of the three meats (salmon, beef, pork), or should the model assume all three meats have zero fiber?

## Turn 6 - User Simulator

The model should assume all three meats have zero fiber.

## Turn 7 - Generic Agent

QUESTION: Are there any upper limits on how much of any single food can be included in the dinner (e.g., a maximum grams per food type), or can each selected food be any non-negative amount as long as the total is exactly 600g and the budget is not exceeded?

## Turn 7 - User Simulator

There are no upper limits on how much of any single food can be included. Each selected food can be any non-negative amount, as long as the total weight is exactly 600 grams and the total cost does not exceed the $15 budget.

## Turn 8 - Generic Agent

QUESTION: Should the model allow fractional grams of food (i.e., continuous amounts), or must the amounts be whole grams (integer)?

## Turn 8 - User Simulator

The business facts do not specify whether amounts must be whole grams or can be fractional. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there any requirement that the dinner must include at least one vegetable from each of the four listed types (okra, carrots, celery, cabbage), or is it sufficient to include any two or more of the four vegetables?

## Turn 9 - User Simulator

It is sufficient to include any two or more of the four vegetables.

## Turn 10 - Generic Agent

QUESTION: Should the model maximize total fiber intake in grams, or is there a different objective (e.g., maximize fiber per dollar, or maximize fiber per gram)?

## Turn 10 - User Simulator

The model should maximize total fiber intake in grams.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total fiber intake (in grams).
- **Foods available:** Salmon, beef, pork, okra, carrots, celery, cabbage.
- **Fiber per 100g:** Okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g; salmon, beef, pork all 0g.
- **Price per 100g:** Salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Total weight:** Exactly 600 grams.
- **Budget:** Total cost ≤ $15.
- **Protein constraint:** Exactly one of {salmon, beef, pork} must be selected with a strictly positive amount; the other two must be zero.
- **Vegetable constraint:** At least two of {okra, carrots, celery, cabbage} must be selected, each with a strictly positive amount; unselected vegetables must be zero.
- **No upper bounds** on any individual food amount.
- **Amounts:** Continuous (fractional grams allowed), pending internal confirmation on whether whole grams are required.
- **Minimum threshold for "strictly positive":** Not specified; pending internal confirmation.