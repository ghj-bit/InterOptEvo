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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any nonnegative amounts, or are the three meats (salmon, beef, pork) excluded from the dinner and only the four vegetables (okra, carrots, celery, cabbage) may be chosen?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) are not excluded. The dinner must include exactly one protein source from those three, along with at least two kinds of vegetables from okra, carrots, celery, and cabbage.

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, should the model force the chosen protein to have a strictly positive amount (i.e., it must actually be eaten in some quantity), or is it acceptable for the selected protein's amount to be zero as long as only that one protein is allowed in the menu?

## Turn 2 - User Simulator

The chosen protein must have a strictly positive amount. It needs to actually be included in the meal plan, not just allowed on the menu.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, should each selected vegetable also have a strictly positive amount (actually eaten), or is it enough that at least two vegetable types are allowed on the menu even if one of them ends up at zero grams?

## Turn 3 - User Simulator

Each selected vegetable must have a strictly positive amount. At least two vegetable types must actually be included in the meal, not just allowed on the menu.

## Turn 4 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — should this 600g be the sum of all selected foods (the one protein plus the vegetables), or should the 600g apply only to the vegetables with the protein counted separately?

## Turn 4 - User Simulator

The 600g is the sum of all selected foods, including the one protein and the vegetables.

## Turn 5 - Generic Agent

QUESTION: The fiber data is only given for the four vegetables (okra, carrots, celery, cabbage) — what fiber content per 100g should I use for the protein (salmon, beef, pork), or should the protein be treated as contributing zero fiber to the objective?

## Turn 5 - User Simulator

The protein should be treated as contributing zero fiber to the objective.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum or maximum amount limits on how much of any single food can be included (for example, a cap on how many grams of one vegetable, or a minimum serving size), or can each selected food be any positive amount as long as the total is 600g and the budget is met?

## Turn 6 - User Simulator

There are no minimum or maximum amount limits on any single food. Each selected food can be any positive amount, as long as the total weight is 600g and the total cost does not exceed $15.

## Turn 7 - Generic Agent

QUESTION: Since the total weight must equal exactly 600g and the budget is a "not exceed $15" cap, is it acceptable for the total cost to come in under $15 (i.e., the budget is a ceiling, not an exact target), or must the spending also equal exactly $15?

## Turn 7 - User Simulator

The budget is a ceiling. It is acceptable for the total cost to come in under $15.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize total fiber intake (grams of fiber).
- **Foods available:** 7 items — salmon, beef, pork (proteins) and okra, carrots, celery, cabbage (vegetables).
- **Protein rule:** Exactly one of the three proteins must be chosen, and its amount must be strictly positive (actually eaten).
- **Vegetable rule:** At least two of the four vegetables must be chosen, and each chosen vegetable's amount must be strictly positive.
- **Weight:** The sum of all selected foods (the one protein plus the chosen vegetables) must equal exactly 600 grams.
- **Budget:** Total cost of selected foods must not exceed $15 (a ceiling, not an exact target).
- **Fiber content per 100g:** okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g; proteins contribute 0 fiber.
- **Price per 100g:** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **No per-food minimum or maximum amount limits** beyond the positivity requirement for selected items.

This is a mixed-integer (binary selection + continuous amounts) optimization: choose which protein and which vegetables, then allocate grams to maximize fiber subject to the exact 600g weight and the $15 budget ceiling.