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

QUESTION: Should the dinner be limited to the four fiber-containing vegetables (okra, carrots, celery, cabbage), or may the three meats (salmon, beef, pork) also be selected as part of the 600 grams?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) may also be selected as part of the 600 grams. In fact, exactly one of those three protein sources must be included in the meal plan.

## Turn 2 - Generic Agent

QUESTION: For the required protein source, should I treat "exactly one of the three meats must be included" as a binary choice (pick one meat, any positive amount), or does the chosen meat need to meet a minimum amount?

## Turn 2 - User Simulator

Treat it as a binary choice: pick one meat, any positive amount. There is no minimum amount requirement for the chosen meat.

## Turn 3 - Generic Agent

QUESTION: Since the total weight must equal exactly 600 grams, should I treat the 600g as a hard equality (the plan must sum to exactly 600g), or is it a target that could be met within some tolerance?

## Turn 3 - User Simulator

Treat the 600g as a hard equality: the plan must sum to exactly 600 grams.

## Turn 4 - Generic Agent

QUESTION: Should the amounts of each food be continuous (any fractional gram allowed), or must they be whole grams?

## Turn 4 - User Simulator

The amounts of each food can be continuous; any fractional gram is allowed.

## Turn 5 - Generic Agent

QUESTION: For the fiber content, should I use the given per-100g values (okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g) and assume the three meats (salmon, beef, pork) contribute zero fiber?

## Turn 5 - User Simulator

Yes, use the given per-100g fiber values for the four vegetables and assume the three meats contribute zero fiber.

## Turn 6 - Generic Agent

QUESTION: For the cost constraint, should the $15 budget be a hard upper bound (total cost must be ≤ $15), and is the cost simply the sum of each food's amount times its per-100g price?

## Turn 6 - User Simulator

Yes, the $15 budget is a hard upper bound (total cost must be ≤ $15), and the cost is simply the sum of each food's amount times its per-100g price.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Continuous, non-negative amounts (in grams) for each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- **Objective:** Maximize total fiber intake, using per-100g fiber values (okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g); the three meats contribute zero fiber.
- **Constraints:**
  1. Total weight equals exactly 600 grams (hard equality).
  2. Total cost ≤ $15 (hard upper bound), where cost = sum of each food's amount × its per-100g price (salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3).
  3. Exactly one of the three meats (salmon, beef, pork) is included, as a binary choice with any positive amount (no minimum amount required).
- **Units:** Amounts in grams; prices and fiber given per 100g, so I will convert appropriately (e.g., price per gram = per-100g price / 100).