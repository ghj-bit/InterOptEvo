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

QUESTION: Should the 600-gram total include only the four fiber vegetables (okra, carrots, celery, cabbage), or should it also include the meats (salmon, beef, pork) as part of the 600 grams?

## Turn 1 - User Simulator

The 600-gram total should include the meats (salmon, beef, or pork) as well as the vegetables. The entire meal plan, including the selected protein source and the selected vegetables, must add up to exactly 600 grams.

## Turn 2 - Generic Agent

QUESTION: Can you select more than one meat (e.g., both salmon and beef), or must you pick exactly one protein source for the meal?

## Turn 2 - User Simulator

You must pick exactly one protein source for the meal.

## Turn 3 - Generic Agent

QUESTION: Are the amounts of each food (meat and each vegetable) continuous (any fractional gram allowed), or must they be chosen in whole-gram or some discrete unit?

## Turn 3 - User Simulator

The amounts can be continuous; any fractional gram is allowed.

## Turn 4 - Generic Agent

QUESTION: Are all four vegetables (okra, carrots, celery, cabbage) allowed to be included in any amount, or must you pick only some of them?

## Turn 4 - User Simulator

You must include at least two different kinds of vegetables from the list of okra, carrots, celery, and cabbage.

## Turn 5 - Generic Agent

QUESTION: When you say "at least two different kinds of vegetables," does that mean each of the included vegetables must have a positive (nonzero) amount, or is it enough that two vegetable types are "selected" even if one of them ends up with zero grams?

## Turn 5 - User Simulator

Each included vegetable must have a positive (nonzero) amount.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum or maximum amount for the single meat you choose, or can the meat amount be any nonnegative continuous value (including zero)?

## Turn 6 - User Simulator

The meat amount can be any nonnegative continuous value, including zero.

## Turn 7 - Generic Agent

QUESTION: Is the $15 budget a hard cap (total cost must be ≤ $15), or must you spend exactly $15?

## Turn 7 - User Simulator

The $15 budget is a hard cap; the total cost must not exceed $15.

## Turn 8 - Generic Agent

QUESTION: Since the meat has no fiber listed, should I treat the fiber of salmon, beef, and pork as 0 g per 100g for the objective?

## Turn 8 - User Simulator

Yes, treat the fiber of salmon, beef, and pork as 0 g per 100g for the objective.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Goal:** Maximize total fiber intake (grams) for a single dinner.

**Foods and data (per 100g):**
- Meats (fiber = 0): salmon $4, beef $3.6, pork $1.8
- Vegetables: okra (3.2g fiber, $2.6), carrots (2.7g fiber, $1.2), celery (1.6g fiber, $1.6), cabbage (2g fiber, $2.3)

**Decisions:**
- Choose exactly one protein source (salmon, beef, or pork).
- Choose amounts of vegetables from {okra, carrots, celery, cabbage}.
- All amounts are continuous, nonnegative (fractional grams allowed).

**Constraints:**
1. Total weight of the entire meal (meat + all vegetables) must equal exactly 600 grams.
2. Total cost of all selected foods must not exceed $15 (hard cap).
3. At least two different vegetable kinds must be included, and each included vegetable must have a strictly positive (nonzero) amount.
4. The meat amount can be any nonnegative continuous value, including zero.

**Objective:** Maximize total fiber = sum over vegetables of (amount in 100g units × fiber per 100g). Meats contribute 0 fiber.