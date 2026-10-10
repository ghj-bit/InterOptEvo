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

QUESTION: Are the meats (salmon, beef, pork) available options for the dinner, or is the meal restricted to only the four vegetable items (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

The meats (salmon, beef, and pork) are available options. The meal is not restricted to only the four vegetable items.

## Turn 2 - Generic Agent

QUESTION: What is the fiber content per 100g for each of the three meats (salmon, beef, and pork), since the brief only lists fiber values for the four vegetables?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the total weight constraint of 600 grams a strict equality (the meal must weigh exactly 600 grams) or a maximum (the meal must weigh at most 600 grams)?

## Turn 3 - User Simulator

The total weight constraint is a strict equality. The meal must weigh exactly 600 grams.

## Turn 4 - Generic Agent

QUESTION: Is the $15 budget a strict ceiling (total cost must be at most $15) or an exact target (total cost must equal $15)?

## Turn 4 - User Simulator

The $15 budget is a strict ceiling. The total cost must be at most $15.

## Turn 5 - Generic Agent

QUESTION: Are the food quantities continuous (you can choose any fractional amount of each food) or must they be chosen in discrete units such as whole 100g portions?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any additional requirements the brief omits, such as a minimum or maximum amount of any specific food, a requirement to include at least one meat, or a limit on how many different foods can be selected?

## Turn 6 - User Simulator

Yes, there are two additional requirements:

1. Exactly one protein source (salmon, beef, or pork) must be selected.
2. At least two different kinds of vegetables from okra, carrots, celery, and cabbage must be selected.

## Turn 7 - Generic Agent

QUESTION: For the requirement that exactly one protein source must be selected, does "selected" mean that the chosen meat must have a strictly positive amount, or is it acceptable for the chosen meat to have a zero amount as long as the other two meats are zero?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: For the requirement that at least two different kinds of vegetables must be selected, does "selected" mean that each chosen vegetable must have a strictly positive amount, or is it acceptable for a chosen vegetable to have a zero amount as long as at least two of the four have positive amounts?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there a maximum weight limit for any single food item, or can any one food account for the entire 600 grams?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total fiber intake.
2.  **Decision Variables:** Amount of each of the 7 food items (salmon, beef, pork, okra, carrots, celery, cabbage).
3.  **Total Weight Constraint:** The sum of the weights of all selected foods must equal exactly 600 grams.
4.  **Budget Constraint:** The total cost of all selected foods must be less than or equal to $15.
5.  **Protein Constraint:** Exactly one of the three meats (salmon, beef, or pork) must be included in the meal.
6.  **Vegetable Constraint:** At least two of the four vegetables (okra, carrots, celery, cabbage) must be included in the meal.
7.  **Data:**
    *   Fiber (g/100g): Okra 3.2, Carrots 2.7, Celery 1.6, Cabbage 2.0.
    *   Price ($/100g): Salmon 4.0, Beef 3.6, Pork 1.8, Okra 2.6, Carrots 1.2, Celery 1.6, Cabbage 2.3.

**Explicit Assumptions (Unconfirmed Points):**
1.  **Fiber Content of Meats:** The fiber content per 100g for salmon, beef, and pork is unknown. I will assume the fiber content for all three meats is **0g** per 100g, as this is the standard nutritional value for lean meats and is the most conservative assumption for a fiber-maximization problem.
2.  **Variable Domain:** It is unconfirmed whether food quantities are continuous or discrete. I will assume **continuous** variables (any fractional amount of grams is allowed), which is standard for linear programming formulations of meal planning.
3.  **Definition of "Selected" (Protein):** It is unconfirmed if "selected" implies a strictly positive amount. I will assume that "exactly one protein source selected" means that **exactly one** of the three meat variables must be **strictly greater than zero**, and the other two must be exactly zero.
4.  **Definition of "Selected" (Vegetables):** It is unconfirmed if "selected" implies a strictly positive amount. I will assume that "at least two different kinds of vegetables selected" means that **at least two** of the four vegetable variables must be **strictly greater than zero**.
5.  **Individual Item Limits:** It is unconfirmed if there are individual maximum weight limits. I will assume there are **no individual maximum weight limits** other than the total 600g constraint.