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

The three meats (salmon, beef, pork) are not excluded. The dinner plan must include exactly one protein source from those three, along with at least two kinds of vegetables from the list of okra, carrots, celery, and cabbage.

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" requirement, does the chosen meat have to be a positive amount (e.g., at least some minimum grams), or is it enough that only one meat type is allowed to be nonzero while its actual amount can be anything from zero up?

## Turn 2 - User Simulator

The chosen meat must be a positive amount. "Exactly one protein source is selected" means one of the three meats is included in the meal with a nonzero quantity, not that it can be zero.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, does each selected vegetable also have to be a positive (nonzero) amount, or is it enough that at least two vegetable types are allowed to be nonzero while their actual amounts can be anything from zero up?

## Turn 3 - User Simulator

Each selected vegetable must be a positive (nonzero) amount. "At least two kinds of vegetables are selected" means at least two of the four vegetable types are included in the meal with a nonzero quantity.

## Turn 4 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — does this 600g include the meat, i.e., the sum of the selected meat plus all selected vegetables must be exactly 600g, or is the 600g target for the vegetables only with the meat on top?

## Turn 4 - User Simulator

The 600g target includes the meat. The sum of the selected meat plus all selected vegetables must equal exactly 600 grams.

## Turn 5 - Generic Agent

QUESTION: Since the meats have no fiber content listed, should I treat salmon, beef, and pork as having 0g fiber per 100g when computing the fiber to maximize?

## Turn 5 - User Simulator

Yes, treat salmon, beef, and pork as having 0g fiber per 100g.

## Turn 6 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15 — is this a strict upper bound (cost ≤ $15, with leftover budget allowed to go unused), or must the spending come as close to $15 as possible?

## Turn 6 - User Simulator

It is a strict upper bound. The total cost must not exceed $15, and leftover budget is allowed to go unused.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Nonnegative continuous amounts (in grams) for each of the seven foods: salmon, beef, pork, okra, carrots, celery, cabbage.

- **Protein requirement:** Exactly one of the three meats (salmon, beef, pork) is selected, and its amount must be strictly positive (nonzero). The other two meats must be zero.

- **Vegetable requirement:** At least two of the four vegetables (okra, carrots, celery, cabbage) are selected, and each selected vegetable must have a strictly positive (nonzero) amount. The remaining vegetable(s) must be zero.

- **Weight constraint:** The sum of the selected meat plus all selected vegetables must equal exactly 600 grams.

- **Budget constraint:** Total cost must not exceed $15 (upper bound; leftover budget allowed).

- **Objective:** Maximize total fiber intake.

- **Fiber content per 100g:** okra 3.2g, carrots 2.7g, cabbage 2g, celery 1.6g; salmon, beef, pork = 0g.

- **Price per 100g:** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.