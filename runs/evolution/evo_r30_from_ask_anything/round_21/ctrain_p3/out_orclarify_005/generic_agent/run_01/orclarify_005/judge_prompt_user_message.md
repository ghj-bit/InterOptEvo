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

QUESTION: Are salmon, beef, and pork available as selectable foods for this dinner, or should the selection be restricted to the four fiber-containing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

Salmon, beef, and pork are available as selectable foods. You should include exactly one of those three protein sources in the meal plan, along with at least two of the four vegetables (okra, carrots, celery, cabbage).

## Turn 2 - Generic Agent

QUESTION: For the protein source, is the amount chosen a continuous weight in grams, or must it be a specific fixed portion size?

## Turn 2 - User Simulator

The amount is a continuous weight in grams. There is no fixed portion size requirement; the total weight of all selected foods must simply equal 600 grams.

## Turn 3 - Generic Agent

QUESTION: For the vegetables, is the amount of each selected vegetable a continuous weight in grams, or must each be chosen in a specific fixed portion size?

## Turn 3 - User Simulator

The amount of each selected vegetable is a continuous weight in grams. There are no fixed portion size requirements; the total weight of all selected foods must simply equal 600 grams.

## Turn 4 - Generic Agent

QUESTION: Is the requirement to include at least two of the four vegetables a hard constraint that must be strictly satisfied, or is it a soft target that can be relaxed if it conflicts with the budget or weight constraints?

## Turn 4 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 5 - Generic Agent

QUESTION: Is the requirement to include exactly one of the three protein sources a hard constraint that must be strictly satisfied, or is it a soft target that can be relaxed if it conflicts with the budget or weight constraints?

## Turn 5 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 6 - Generic Agent

QUESTION: Is the total cost constraint a hard ceiling that must not be exceeded, or is it a soft target that can be violated if it helps maximize fiber intake?

## Turn 6 - User Simulator

It is a hard ceiling that must not be exceeded.

## Turn 7 - Generic Agent

QUESTION: Is the total weight requirement of 600 grams a hard equality that must be met exactly, or is it a soft target that can be approximated if it conflicts with the budget or fiber maximization?

## Turn 7 - User Simulator

It is a hard equality that must be met exactly.

## Turn 8 - Generic Agent

QUESTION: Are there any additional requirements or constraints for the dinner plan, such as minimum or maximum amounts for specific foods, exclusivity rules between vegetables, or other dietary restrictions?

## Turn 8 - User Simulator

No, there are no additional requirements or constraints beyond what has already been stated: exactly one protein source, at least two vegetables, total cost not exceeding $15, and total weight equal to 600 grams.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total fiber intake.
2.  **Decision Variables:** Continuous weights (in grams) for each of the 7 available foods (salmon, beef, pork, okra, carrots, celery, cabbage).
3.  **Selection Constraints (Hard):**
    *   Exactly one of the three protein sources (salmon, beef, pork) must be selected (weight > 0).
    *   At least two of the four vegetables (okra, carrots, celery, cabbage) must be selected (weight > 0).
4.  **Resource Constraints (Hard):**
    *   Total weight of all selected foods must equal exactly 600 grams.
    *   Total cost of all selected foods must not exceed $15.
5.  **Data:**
    *   **Fiber (per 100g):** Okra 3.2g, Carrots 2.7g, Celery 1.6g, Cabbage 2.0g. (Proteins have 0g fiber).
    *   **Price (per 100g):** Salmon $4.0, Beef $3.6, Pork $1.8, Okra $2.6, Carrots $1.2, Celery $1.6, Cabbage $2.3.
6.  **Assumptions:**
    *   Proteins (salmon, beef, pork) contribute 0g of fiber.
    *   "Selected" implies a weight strictly greater than 0.
    *   No other dietary restrictions or minimum/maximum portion sizes apply.