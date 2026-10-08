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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage), or only the four fiber-containing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The model should allow selecting from all seven listed foods: salmon, beef, pork, okra, carrots, celery, and cabbage.

## Turn 2 - Generic Agent

QUESTION: For salmon, beef, and pork, should I treat their fiber content as 0 g per 100g (since no fiber values were given for them)?

## Turn 2 - User Simulator

Yes, treat the fiber content for salmon, beef, and pork as 0 g per 100g.

## Turn 3 - Generic Agent

QUESTION: Should the total weight be exactly 600 grams (equality), or at most 600 grams?

## Turn 3 - User Simulator

The total weight must be exactly 600 grams.

## Turn 4 - Generic Agent

QUESTION: Should the amount of each food be a continuous quantity (any gram amount allowed), or must each food be chosen in whole 100g units?

## Turn 4 - User Simulator

The amount of each food can be any continuous quantity; it does not need to be in whole 100g units.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum or maximum amount that must be selected for each food, or can any food be set to zero (i.e., not selected at all)?

## Turn 5 - User Simulator

Any food can be set to zero. There are no minimum or maximum amounts for individual foods, other than the overall constraints that exactly one protein source is selected and at least two kinds of vegetables are selected.

## Turn 6 - Generic Agent

QUESTION: When you say "exactly one protein source is selected," does that mean exactly one of salmon, beef, and pork must be chosen with a positive amount, while the other two must be zero?

## Turn 6 - User Simulator

Yes, exactly one of salmon, beef, or pork must be chosen with a positive amount, and the other two must be zero.

## Turn 7 - Generic Agent

QUESTION: When you say "at least two kinds of vegetables are selected," does that mean at least two of okra, carrots, celery, and cabbage must each have a positive amount?

## Turn 7 - User Simulator

Yes, at least two of okra, carrots, celery, and cabbage must each have a positive amount.

## Turn 8 - Generic Agent

QUESTION: For the "positive amount" requirement (exactly one protein, at least two vegetables), is any amount greater than zero sufficient, or is there a minimum positive amount (e.g., at least 1 gram) that counts as "selected"?

## Turn 8 - User Simulator

Any amount greater than zero is sufficient to count as "selected." There is no specific minimum positive amount like 1 gram.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Continuous, non-negative amount (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- **Objective:** Maximize total fiber intake.
- **Fiber content (g per 100g):** okra 3.2, carrots 2.7, celery 1.6, cabbage 2.0, salmon 0, beef 0, pork 0.
- **Price (per 100g):** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Constraints:**
  1. Total cost ≤ $15.
  2. Total weight = exactly 600 grams.
  3. Exactly one of {salmon, beef, pork} has a positive amount; the other two are zero.
  4. At least two of {okra, carrots, celery, cabbage} have a positive amount.
  5. Any amount > 0 counts as "selected"; no minimum positive amount.
  6. All amounts ≥ 0 (continuous).