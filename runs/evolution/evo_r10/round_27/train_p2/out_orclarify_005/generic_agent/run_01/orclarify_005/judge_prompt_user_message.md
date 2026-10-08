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

QUESTION: Should the model be limited to only the four fiber-bearing vegetables (okra, carrots, celery, cabbage), or can the three meats (salmon, beef, pork) also be selected as part of the 600g dinner (with zero fiber contribution)?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) can be selected as part of the 600g dinner. They contribute zero fiber, but they are part of the meal plan.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum amount constraints on how much of each food can be selected (for example, at least some of each, or a cap on any single food), or can each food range freely from 0 grams up to the full 600 grams?

## Turn 2 - User Simulator

There are no minimum or maximum amount constraints on how much of each food can be selected. Each food can range freely from 0 grams up to the full 600 grams, subject to the other constraints (exactly one protein, at least two vegetables, total weight 600g, and budget $15).

## Turn 3 - Generic Agent

QUESTION: You mentioned "exactly one protein" and "at least two vegetables" — should the model enforce exactly one of the three meats (salmon, beef, pork) and at least two of the four vegetables (okra, carrots, celery, cabbage) as part of the selection?

## Turn 3 - User Simulator

Yes, the model should enforce exactly one of the three meats (salmon, beef, pork) and at least two of the four vegetables (okra, carrots, celery, cabbage) as part of the selection.

## Turn 4 - Generic Agent

QUESTION: When you say "at least two vegetables," does that mean at least two vegetable types must be present with a positive amount (i.e., you can pick any 2, 3, or 4 of the four vegetables), or exactly two vegetable types?

## Turn 4 - User Simulator

It means at least two vegetable types must be present with a positive amount. You can pick any 2, 3, or 4 of the four vegetables.

## Turn 5 - Generic Agent

QUESTION: For the "exactly one protein" and "at least two vegetables" rules, does "present" mean a strictly positive amount (greater than 0 grams), or is a small epsilon threshold acceptable (e.g., at least 1 gram) to make the model numerically well-behaved?

## Turn 5 - User Simulator

"Present" means a strictly positive amount (greater than 0 grams).

## Turn 6 - Generic Agent

QUESTION: Is the total weight constraint exactly 600 grams (equality), or at most 600 grams (inequality)?

## Turn 6 - User Simulator

The total weight constraint is exactly 600 grams (equality).

## Turn 7 - Generic Agent

QUESTION: Is the budget constraint at most $15 (inequality), meaning the total cost of selected foods must not exceed $15?

## Turn 7 - User Simulator

Yes, the budget constraint is at most $15 (inequality), meaning the total cost of selected foods must not exceed $15.

## Turn 8 - Generic Agent

QUESTION: Are the food amounts continuous (you can select any fractional gram amount, e.g., 123.45 grams of okra), or must they be in whole-gram increments?

## Turn 8 - User Simulator

The food amounts are continuous; you can select any fractional gram amount.

## Turn 9 - Generic Agent

QUESTION: Is there any other constraint or preference I should be aware of, such as a maximum number of total food types, a preference for variety, or any other business rule not yet mentioned?

## Turn 9 - User Simulator

No, there are no other constraints or preferences. The rules are:

1. Maximize fiber intake.
2. Total cost must not exceed $15.
3. Total weight must equal 600 grams.
4. Exactly one protein source (salmon, beef, or pork) is selected.
5. At least two kinds of vegetables from okra, carrots, celery, and cabbage are selected.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total fiber intake (in grams).

**Decision variables:** Continuous, non-negative amounts (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.

**Data:**
- Fiber per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g; meats contribute 0g fiber.
- Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.

**Constraints:**
1. Total cost ≤ $15.
2. Total weight = 600 grams (equality).
3. Exactly one of the three meats (salmon, beef, pork) is selected (strictly positive amount).
4. At least two of the four vegetables (okra, carrots, celery, cabbage) are selected (each with strictly positive amount).
5. All amounts are continuous and non-negative.

No other constraints or preferences apply.