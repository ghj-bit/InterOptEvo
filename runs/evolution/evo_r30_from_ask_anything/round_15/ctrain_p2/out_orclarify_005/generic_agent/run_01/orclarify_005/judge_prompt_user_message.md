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

QUESTION: Are salmon, beef, and pork available as options for this dinner, or should the selection be limited to the four vegetable items (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

Salmon, beef, and pork are available as options. You should include exactly one of those three protein sources in the meal plan, along with at least two of the four vegetable items.

## Turn 2 - Generic Agent

QUESTION: Is the 600-gram total weight a strict equality that the selected foods must sum to exactly, or is it a maximum ceiling that the total weight must not exceed?

## Turn 2 - User Simulator

The 600-gram total weight is a strict equality. The selected foods must sum to exactly 600 grams.

## Turn 3 - Generic Agent

QUESTION: Is the $15 budget a strict ceiling that the total cost must not exceed, or is it a target that the total cost should equal exactly?

## Turn 3 - User Simulator

The $15 budget is a strict ceiling. The total cost of the selected foods must not exceed $15.

## Turn 4 - Generic Agent

QUESTION: Is the fiber content for salmon, beef, and pork zero, or do you have specific fiber values per 100g for those three protein sources that I should use in the model?

## Turn 4 - User Simulator

The fiber content for salmon, beef, and pork is zero.

## Turn 5 - Generic Agent

QUESTION: Is the "at least two of the four vegetable items" requirement a hard constraint that must be satisfied, or is it a soft preference that can be relaxed if needed to meet the other constraints?

## Turn 5 - User Simulator

It is a hard constraint. The meal must include at least two different kinds of vegetables from okra, carrots, celery, and cabbage.

## Turn 6 - Generic Agent

QUESTION: Is the "exactly one of the three protein sources" requirement a hard constraint that must be satisfied, or is it a soft preference that can be relaxed if needed to meet the other constraints?

## Turn 6 - User Simulator

It is a hard constraint. The meal must include exactly one of the three protein sources: salmon, beef, or pork.

## Turn 7 - Generic Agent

QUESTION: Is the amount of each selected food a continuous variable (any fractional gram is allowed), or must the quantities be whole grams or some other discrete unit?

## Turn 7 - User Simulator

The amount of each selected food is a continuous variable. Any fractional gram is allowed.

## Turn 8 - Generic Agent

QUESTION: Is there a minimum quantity of each selected food that must be included, or can a selected food have an arbitrarily small positive amount?

## Turn 8 - User Simulator

There is no minimum quantity specified. A selected food can have an arbitrarily small positive amount.

## Turn 9 - Generic Agent

QUESTION: Is there a maximum quantity limit for any single food item, or can a single food item make up the entire 600-gram total weight?

## Turn 9 - User Simulator

There is no maximum quantity limit for any single food item.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize total fiber intake (in grams).
2. **Decision Variables:** Continuous, non-negative quantities (in grams) for each of the 7 food items: salmon, beef, pork, okra, carrots, celery, cabbage.
3. **Fiber Content (per 100g):**
   - Salmon: 0g
   - Beef: 0g
   - Pork: 0g
   - Okra: 3.2g
   - Carrots: 2.7g
   - Celery: 1.6g
   - Cabbage: 2.0g
4. **Price (per 100g):**
   - Salmon: $4.00
   - Beef: $3.60
   - Pork: $1.80
   - Okra: $2.60
   - Carrots: $1.20
   - Celery: $1.60
   - Cabbage: $2.30
5. **Constraints:**
   - **Total Weight (Equality):** Sum of all selected food quantities must equal exactly 600 grams.
   - **Budget (Ceiling):** Total cost of selected foods must not exceed $15.
   - **Protein Selection (Hard):** Exactly one of {salmon, beef, pork} must be included (quantity > 0).
   - **Vegetable Selection (Hard):** At least two of {okra, carrots, celery, cabbage} must be included (quantity > 0).
   - **Non-negativity:** All quantities must be ≥ 0.
   - **No Minimum/Maximum per Item:** No additional bounds on individual food quantities beyond non-negativity and the total weight constraint.

**Assumptions:**
- None. All formulation-critical facts were confirmed by the user.