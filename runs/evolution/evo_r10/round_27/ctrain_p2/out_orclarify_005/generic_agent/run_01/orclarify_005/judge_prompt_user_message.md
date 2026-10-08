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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any non-negative amounts, or are the three meats (salmon, beef, pork) excluded from the dinner and only the four vegetables (okra, carrots, celery, cabbage) may be chosen?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) are not excluded. The dinner plan must include exactly one protein source from those three, along with at least two kinds of vegetables from the list of okra, carrots, celery, and cabbage.

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, does that mean the chosen meat must have a strictly positive amount (any amount > 0 counts), or must it meet some minimum portion size?

## Turn 2 - User Simulator

The chosen meat must have a strictly positive amount. Any amount greater than zero counts; there is no specific minimum portion size required.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, does each chosen vegetable need a strictly positive amount (any amount > 0 counts), or must each meet some minimum portion size?

## Turn 3 - User Simulator

Each chosen vegetable needs a strictly positive amount. Any amount greater than zero counts; there is no specific minimum portion size required.

## Turn 4 - Generic Agent

QUESTION: The fiber data is only given for the four vegetables (okra, carrots, celery, cabbage). What fiber content per 100g should I use for the three meats (salmon, beef, pork) in the objective?

## Turn 4 - User Simulator

The fiber content for the three meats (salmon, beef, pork) is 0g per 100g.

## Turn 5 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams. Does this 600g include the meat, or is the 600g target for the vegetables only (with the meat on top of that)?

## Turn 5 - User Simulator

The 600g target includes the meat. The total weight of all selected foods (the one chosen protein source plus the selected vegetables) must equal exactly 600 grams.

## Turn 6 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15. Does the $15 budget cover all selected foods (the meat plus the vegetables), or only the vegetables?

## Turn 6 - User Simulator

The $15 budget covers all selected foods, including the meat and the vegetables.

## Turn 7 - Generic Agent

QUESTION: Are there any upper limits on how much of any single food can be selected (e.g., a maximum grams per item), or can each selected food be any non-negative amount as long as the total is 600g?

## Turn 7 - User Simulator

There are no upper limits on how much of any single food can be selected. Each selected food can be any non-negative amount, as long as the total weight of all selected foods equals 600 grams.

## Turn 8 - Generic Agent

QUESTION: Since the objective is to maximize fiber and the meats have 0g fiber, the model would naturally push the meat amount toward zero (just above 0). Is that acceptable — i.e., the meat can be an arbitrarily small positive amount — or should the meat be a meaningful portion of the meal?

## Turn 8 - User Simulator

Yes, that is acceptable. The meat can be an arbitrarily small positive amount. There is no requirement for the meat to be a meaningful portion of the meal.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** grams of each of the 7 foods (salmon, beef, pork, okra, carrots, celery, cabbage), all non-negative.
- **Objective:** maximize total fiber intake. Fiber per 100g: okra 3.2, carrots 2.7, celery 1.6, cabbage 2.0; salmon, beef, pork all 0.
- **Weight constraint:** total weight of all selected foods = exactly 600g (meat included).
- **Budget constraint:** total cost of all selected foods ≤ $15. Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Protein requirement:** exactly one of {salmon, beef, pork} must be selected with a strictly positive amount (no minimum portion size; arbitrarily small positive is fine).
- **Vegetable requirement:** at least two of {okra, carrots, celery, cabbage} must be selected, each with a strictly positive amount (no minimum portion size).
- **No upper bounds** on any individual food amount.

This is a mixed-integer (binary selection) + continuous (grams) model: binary variables enforce "exactly one meat" and "at least two vegetables," continuous variables set the grams, with the weight equality, budget inequality, and fiber-maximizing objective.