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

QUESTION: Should the model allow choosing any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any amounts, or is the dinner restricted to only the four fiber-containing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The dinner is not restricted to only the four vegetables. The model should allow choosing from all seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage).

However, there are two specific restrictions on how those seven foods are selected:
1.  Exactly one protein source (salmon, beef, or pork) must be included.
2.  At least two different kinds of vegetables (from okra, carrots, celery, and cabbage) must be included.

## Turn 2 - Generic Agent

QUESTION: For the "at least two different kinds of vegetables" requirement, does "included" mean a strictly positive amount of each chosen vegetable, or is a tiny amount (e.g., 1 gram) enough to count a vegetable as included?

## Turn 2 - User Simulator

A strictly positive amount is required. A tiny amount like 1 gram would technically count as "included" under the literal wording, but for a practical dinner plan, I expect a meaningful portion of each selected vegetable. Please treat "included" as requiring a non-zero amount, but ensure the final plan reflects a realistic meal rather than token amounts.

## Turn 3 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, does "included" mean a strictly positive amount of that one protein (with the other two proteins at zero), or could the single chosen protein be present in only a token amount?

## Turn 3 - User Simulator

It means a strictly positive amount of that one protein, with the other two proteins at zero. The chosen protein should be a meaningful part of the meal, not just a token amount.

## Turn 4 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — is this a hard equality (the plan must sum to precisely 600g), or is 600g a target that could be slightly exceeded or fallen short of if needed?

## Turn 4 - User Simulator

It is a hard equality. The total weight of the selected foods must sum to exactly 600 grams.

## Turn 5 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15 — is this a hard upper bound (cost ≤ $15), and is it acceptable for the optimal plan to spend significantly less than $15 if that maximizes fiber?

## Turn 5 - User Simulator

Yes, it is a hard upper bound (cost ≤ $15). It is acceptable for the optimal plan to spend significantly less than $15 if that maximizes fiber intake.

## Turn 6 - Generic Agent

QUESTION: The fiber content is given only for the four vegetables (okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g per 100g). What fiber value should I use for the three proteins (salmon, beef, pork) — are they zero fiber, or do you have specific fiber values for them?

## Turn 6 - User Simulator

The three proteins (salmon, beef, pork) have zero fiber.

## Turn 7 - Generic Agent

QUESTION: Are the amounts of each food continuous (any fractional gram is allowed), or must each food be chosen in whole-gram (or some other discrete) increments?

## Turn 7 - User Simulator

The amounts of each food are continuous. Any fractional gram is allowed.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total fiber intake (in grams).

**Decision variables:** Continuous, non-negative amount (in grams) of each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.

**Data (per 100g):**
- Fiber (g): okra 3.2, carrots 2.7, celery 1.6, cabbage 2.0; salmon, beef, pork = 0.
- Price ($): salmon 4.0, beef 3.6, pork 1.8, okra 2.6, carrots 1.2, celery 1.6, cabbage 2.3.

**Constraints:**
1. **Budget (hard upper bound):** total cost ≤ $15. Spending less is fine.
2. **Weight (hard equality):** total weight of all selected foods = exactly 600 g.
3. **Exactly one protein:** exactly one of {salmon, beef, pork} has a strictly positive amount; the other two are zero. (Modeled with binary selection variables; the chosen protein gets a meaningful positive amount.)
4. **At least two vegetables:** at least two of {okra, carrots, celery, cabbage} have strictly positive amounts. (Modeled with binary selection variables; each selected vegetable gets a positive amount.)
5. **Non-negativity:** all amounts ≥ 0.

**Notes:**
- "Strictly positive" is enforced via binary variables with a small lower bound (epsilon) on selected items, ensuring a meaningful portion rather than a token amount.
- The plan should reflect a realistic meal, not token amounts.