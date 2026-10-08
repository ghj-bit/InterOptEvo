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

QUESTION: Should the 600g total weight include all foods (both the meats and the vegetables), or only the vegetables?

## Turn 1 - User Simulator

The 600g total weight includes all foods, both the meat and the vegetables.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum amount requirements for each individual food item, or can any food be included in any amount (including zero)?

## Turn 2 - User Simulator

There are no minimum or maximum amount requirements for each individual food item. Any food can be included in any amount, including zero, subject to the other constraints (exactly one protein, at least two vegetables, total weight 600g, and budget $15).

## Turn 3 - Generic Agent

QUESTION: You mentioned "exactly one protein" — does that mean exactly one of the three meats (salmon, beef, pork) must be chosen, and the other two must be zero?

## Turn 3 - User Simulator

Yes, exactly one of the three meats (salmon, beef, or pork) must be chosen, and the other two must be zero.

## Turn 4 - Generic Agent

QUESTION: You mentioned "at least two vegetables" — does that mean at least two of the four vegetables (okra, carrots, celery, cabbage) must be chosen with a positive amount, and can all four be included?

## Turn 4 - User Simulator

Yes, at least two of the four vegetables (okra, carrots, celery, cabbage) must be chosen with a positive amount, and all four can be included.

## Turn 5 - Generic Agent

QUESTION: When you say a vegetable must be "chosen with a positive amount," is there a minimum quantity (e.g., at least 1g or 10g) that counts as "chosen," or does any amount greater than zero count?

## Turn 5 - User Simulator

Any amount greater than zero counts as "chosen." There is no specific minimum quantity like 1g or 10g.

## Turn 6 - Generic Agent

QUESTION: For the fiber objective, should fiber be calculated only from the vegetables (okra, carrots, celery, cabbage), or should I also account for any fiber in the meats (salmon, beef, pork)?

## Turn 6 - User Simulator

Fiber should be calculated only from the vegetables (okra, carrots, celery, cabbage).

## Turn 7 - Generic Agent

QUESTION: Is the budget constraint a strict "must not exceed $15" (i.e., total cost ≤ $15), or should the total cost be exactly $15?

## Turn 7 - User Simulator

The budget constraint is "must not exceed $15," so the total cost must be less than or equal to $15.

## Turn 8 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total fiber intake (from vegetables only).

**Decision variables:** Amount (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage. All continuous, non-negative.

**Constraints:**
1. **Total weight:** Sum of all 7 food amounts = 600g (exactly).
2. **Budget:** Total cost ≤ $15.
3. **Exactly one protein:** Exactly one of {salmon, beef, pork} has a positive amount; the other two are zero.
4. **At least two vegetables:** At least two of {okra, carrots, celery, cabbage} have a positive amount (any amount > 0 counts).

**Data:**
- Fiber per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g (meats contribute 0 fiber).
- Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.

**Notes:**
- No per-item minimum or maximum quantities.
- The "at least two vegetables" and "exactly one protein" constraints are logical (combinatorial) constraints that will require binary variables or case enumeration in the formulation.