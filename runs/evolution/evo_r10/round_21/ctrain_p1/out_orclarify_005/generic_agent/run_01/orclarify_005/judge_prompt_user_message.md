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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any non-negative amounts, or is the intended choice set limited to only the four fiber-bearing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The intended choice set includes all seven listed foods. You should allow selecting any of them in non-negative amounts, subject to the specific selection rules: exactly one protein source (salmon, beef, or pork) and at least two kinds of vegetables (from okra, carrots, celery, and cabbage).

## Turn 2 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" rule, does a vegetable count as "selected" only if its amount is strictly greater than zero, or is there a minimum amount (like a minimum grams) that a vegetable must reach to count as one of the two kinds?

## Turn 2 - User Simulator

A vegetable counts as "selected" only if its amount is strictly greater than zero. There is no minimum gram requirement.

## Turn 3 - Generic Agent

QUESTION: For the "exactly one protein source" rule, does the chosen protein need to be strictly greater than zero grams, and must the other two proteins be exactly zero grams?

## Turn 3 - User Simulator

Yes, the chosen protein must be strictly greater than zero grams, and the other two proteins must be exactly zero grams.

## Turn 4 - Generic Agent

QUESTION: Since the total weight must equal exactly 600 grams, is it acceptable for the model to use only a single vegetable (e.g., all 600g as okra) as long as the "at least two kinds of vegetables" rule is satisfied, or is there an implicit expectation that the 600g should be distributed across multiple foods?

## Turn 4 - User Simulator

The 600g must be distributed across multiple foods because the "at least two kinds of vegetables" rule requires at least two different vegetables to have amounts strictly greater than zero. Therefore, you cannot use only a single vegetable.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on how much of any single food can be selected (e.g., a maximum grams per food), or can a food in principle make up the entire 600g as long as the other selection rules are satisfied?

## Turn 5 - User Simulator

There is no upper limit on how much of any single food can be selected. A food can make up a large portion of the 600g as long as the other selection rules (exactly one protein, at least two vegetables, budget, and total weight) are satisfied.

## Turn 6 - Generic Agent

QUESTION: Is the fiber content of the three proteins (salmon, beef, pork) zero, so that only the four vegetables contribute to the fiber objective?

## Turn 6 - User Simulator

Yes, the fiber content of the three proteins (salmon, beef, pork) is zero. Only the four vegetables (okra, carrots, celery, cabbage) contribute to the fiber objective.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Non-negative continuous amounts (in grams) for each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- **Objective:** Maximize total fiber intake. Fiber (per 100g): okra 3.2g, carrots 2.7g, cabbage 2.0g, celery 1.6g; proteins have 0 fiber.
- **Constraints:**
  1. **Budget:** Total cost ≤ $15. Prices per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
  2. **Total weight:** Sum of all food amounts = exactly 600g.
  3. **Exactly one protein:** Exactly one of {salmon, beef, pork} has amount > 0; the other two are exactly 0.
  4. **At least two vegetables:** At least two of {okra, carrots, celery, cabbage} have amount strictly > 0.
- **No upper bounds** on any individual food amount.
- **No minimum gram threshold** for a food to count as "selected" — strictly greater than zero suffices.
- The 600g is distributed across multiple foods (guaranteed by the at-least-two-vegetables rule plus the one-protein rule, meaning at least 3 foods are positive).