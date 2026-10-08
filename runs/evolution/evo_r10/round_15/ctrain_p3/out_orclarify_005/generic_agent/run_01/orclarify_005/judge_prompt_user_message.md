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

QUESTION: Should the model allow choosing any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any amounts, or are the three meats (salmon, beef, pork) excluded from the dinner and only the four vegetables (okra, carrots, celery, cabbage) may be selected?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) are not excluded. The dinner plan must include exactly one protein source from those three, along with at least two kinds of vegetables from the list of okra, carrots, celery, and cabbage.

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, does the chosen meat have to be a positive amount (i.e., you must actually eat some of it), or is it enough that only one meat type is allowed to be nonzero while that meat could in principle be zero?

## Turn 2 - User Simulator

The chosen meat must be a positive amount. You must actually eat some of the selected protein source; it cannot be zero.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, does each selected vegetable have to be a positive amount (actually eaten), or is it enough that at least two vegetable types are allowed to be nonzero while some of them could in principle be zero?

## Turn 3 - User Simulator

Each selected vegetable must be a positive amount. You must actually eat at least two different kinds of vegetables; they cannot be zero.

## Turn 4 - Generic Agent

QUESTION: The fiber content is only given for the four vegetables (okra, carrots, celery, cabbage) and not for the three meats. For the fiber-maximization objective, should the meats be treated as contributing zero fiber, or do you have fiber values for salmon, beef, and pork that I should use?

## Turn 4 - User Simulator

The meats should be treated as contributing zero fiber. I do not have fiber values for salmon, beef, or pork to use.

## Turn 5 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams. Does this 600 grams include the weight of the selected meat, or is the 600 grams the total weight of the vegetables only (with the meat's weight on top of that)?

## Turn 5 - User Simulator

The 600 grams is the total weight of all selected foods, including the selected meat and the vegetables.

## Turn 6 - Generic Agent

QUESTION: The budget is stated as "must not exceed $15." Is the $15 a ceiling (total cost can be less than or equal to $15), or must the total cost equal exactly $15?

## Turn 6 - User Simulator

The $15 is a ceiling. The total cost must be less than or equal to $15.

## Turn 7 - Generic Agent

QUESTION: Are the amounts of each food allowed to be any continuous (fractional) weight in grams, or must each food be chosen in whole-gram (or some other discrete) increments?

## Turn 7 - User Simulator

The amounts of each food can be any continuous (fractional) weight in grams.

## Turn 8 - Generic Agent

QUESTION: Is there any minimum or maximum amount (in grams) that must be eaten of the selected protein source or of each selected vegetable, or can any positive amount be as small as you like?

## Turn 8 - User Simulator

There is no specific minimum or maximum amount in grams for the selected protein source or each selected vegetable. Any positive amount is allowed, as long as the total weight equals 600 grams and the total cost does not exceed $15.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Decision variables: continuous (fractional) weight in grams for each of the seven foods — salmon, beef, pork, okra, carrots, celery, cabbage.
- Protein requirement: exactly one of the three meats (salmon, beef, pork) is selected, and its weight must be strictly positive (actually eaten). The other two meats must be zero.
- Vegetable requirement: at least two of the four vegetables (okra, carrots, celery, cabbage) are selected, and each selected vegetable must be strictly positive (actually eaten). The unselected vegetables are zero.
- Weight: the total weight of all selected foods (meat + vegetables) must equal exactly 600 grams.
- Budget: the total cost of all selected foods must be less than or equal to $15 (a ceiling, not an equality).
- Objective: maximize total fiber intake.
- Fiber (per 100g): okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2.0g; the three meats contribute zero fiber.
- Price (per 100g): salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- No per-food minimum or maximum weight beyond the positivity requirement for selected foods; any positive amount is allowed.