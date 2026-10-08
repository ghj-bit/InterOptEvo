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

QUESTION: Should the model select from all seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage), or only from the four fiber-bearing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The model should select from all seven listed foods. The meal plan must include exactly one protein source (salmon, beef, or pork) and at least two kinds of vegetables from the list (okra, carrots, celery, and cabbage).

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, does that mean the chosen protein must have a positive amount (e.g., at least some minimum grams), or is it enough that only one of the three proteins is allowed to be selected (with the others at zero) even if the chosen one ends up at zero grams?

## Turn 2 - User Simulator

The chosen protein must have a positive amount. It is not enough for only one to be allowed if it ends up at zero grams; the selected protein must actually be included in the meal.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, does each selected vegetable also need a positive amount (actually included), or is it enough that at least two of the four vegetables are allowed to be selected even if some end up at zero grams?

## Turn 3 - User Simulator

Each selected vegetable needs a positive amount. The meal must actually include at least two different kinds of vegetables from the list.

## Turn 4 - Generic Agent

QUESTION: Since "positive amount" is required for the selected protein and vegetables, is there a minimum number of grams that each selected food must reach to count as actually included (for example, at least 10g or 50g), or is any amount greater than zero sufficient?

## Turn 4 - User Simulator

Any amount greater than zero is sufficient. There is no specific minimum gram threshold for a selected food to count as included.

## Turn 5 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — is that a strict equality (the meal must weigh exactly 600g, no more and no less), or is 600g a target that could be slightly exceeded or fallen short of?

## Turn 5 - User Simulator

It is a strict equality. The total weight of the selected foods must equal exactly 600 grams.

## Turn 6 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15 — is that a hard ceiling (cost ≤ $15), or should the model also try to minimize cost as a secondary goal after maximizing fiber?

## Turn 6 - User Simulator

It is a hard ceiling. The total cost must not exceed $15. There is no secondary goal to minimize cost; the only objective is to maximize fiber intake.

## Turn 7 - Generic Agent

QUESTION: The fiber content is given only for the four vegetables (okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g per 100g) — should the three proteins (salmon, beef, pork) be treated as having zero fiber in the objective, or do they have fiber values I should use?

## Turn 7 - User Simulator

The three proteins (salmon, beef, pork) should be treated as having zero fiber in the objective.

## Turn 8 - Generic Agent

QUESTION: Are the amounts of each food continuous (any fractional gram is allowed), or must each food be chosen in whole-gram (or some other discrete) increments?

## Turn 8 - User Simulator

The amounts of each food are continuous. Any fractional gram is allowed.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:** Continuous, non-negative amount (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.

**Objective:** Maximize total fiber intake. Fiber per 100g: okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g; salmon, beef, pork = 0g fiber.

**Constraints:**
1. **Total weight (strict equality):** sum of all 7 food amounts = exactly 600 grams.
2. **Budget (hard ceiling):** total cost ≤ $15. Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
3. **Exactly one protein:** exactly one of {salmon, beef, pork} has a positive amount; the other two are zero.
4. **At least two vegetables:** at least two of {okra, carrots, celery, cabbage} have a positive amount.
5. "Positive amount" means strictly greater than zero; no minimum gram threshold.

**Notes:**
- No secondary objective (cost minimization is not a goal).
- All amounts are continuous (fractional grams allowed).