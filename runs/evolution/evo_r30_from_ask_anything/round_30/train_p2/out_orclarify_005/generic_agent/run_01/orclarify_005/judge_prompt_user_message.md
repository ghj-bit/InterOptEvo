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

QUESTION: Should the model select quantities from all seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage), or only from the four fiber-containing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The model should select quantities from all seven listed foods, but with two restrictions:

1.  Exactly one protein source (salmon, beef, or pork) is selected.
2.  At least two kinds of vegetables from okra, carrots, celery, and cabbage are selected.

## Turn 2 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" restriction, does "selected" mean that the quantity of each chosen vegetable must be strictly greater than zero, or is a quantity of zero grams acceptable for a vegetable that is considered "selected"?

## Turn 2 - User Simulator

"Selected" means the quantity of each chosen vegetable must be strictly greater than zero.

## Turn 3 - Generic Agent

QUESTION: Are the quantities of the seven foods continuous (allowing any fractional gram amount) or must they be integer grams?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Should the model allow fractional gram amounts for the foods, or must each food quantity be a whole number of grams?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the $15 budget a hard ceiling (total cost must be less than or equal to $15) or an exact target (total cost must equal $15)?

## Turn 5 - User Simulator

The $15 budget is a hard ceiling; the total cost must be less than or equal to $15.

## Turn 6 - Generic Agent

QUESTION: Is the 600-gram total weight an exact equality (total weight must equal 600 grams) or a ceiling (total weight must be less than or equal to 600 grams)?

## Turn 6 - User Simulator

The 600-gram total weight is an exact equality; the total weight must equal 600 grams.

## Turn 7 - Generic Agent

QUESTION: Are there any minimum or maximum quantity limits for any specific food item, such as a minimum portion size for the selected protein or a maximum amount for any vegetable?

## Turn 7 - User Simulator

No, there are no minimum or maximum quantity limits for any specific food item.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total fiber intake.
2.  **Decision Variables:** Quantities (in grams) of seven foods: salmon, beef, pork, okra, carrots, celery, and cabbage.
3.  **Variable Domain:** Continuous, non-negative real numbers (assumed, as integrality was not confirmed).
4.  **Constraints:**
    *   **Total Weight:** The sum of all food quantities must equal exactly 600 grams.
    *   **Budget:** The total cost of all selected foods must be less than or equal to $15.
    *   **Protein Selection:** Exactly one of the three proteins (salmon, beef, pork) must be selected (quantity > 0), and the other two must be 0.
    *   **Vegetable Selection:** At least two of the four vegetables (okra, carrots, celery, cabbage) must be selected (quantity > 0).
    *   **No Individual Bounds:** There are no specific minimum or maximum quantity limits for any single food item beyond the non-negativity constraint.
5.  **Data:**
    *   **Fiber (per 100g):** Okra 3.2g, Carrots 2.7g, Celery 1.6g, Cabbage 2.0g. (Proteins have 0g fiber).
    *   **Price (per 100g):** Salmon $4.00, Beef $3.60, Pork $1.80, Okra $2.60, Carrots $1.20, Celery $1.60, Cabbage $2.30.

**Explicit Assumptions:**
*   The quantities of foods are continuous variables (fractional grams are allowed).
*   Salmon, beef, and pork contain 0g of fiber.