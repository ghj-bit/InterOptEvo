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

QUESTION: For the "exactly one protein source" requirement, does the chosen meat have to be a positive amount (e.g., at least some minimum grams), or is it enough that only one meat type is allowed to appear in the plan (with the other two at zero)?

## Turn 2 - User Simulator

The chosen meat must be a positive amount. It is not enough for only one meat type to be allowed to appear; the selected protein source must actually be included in the meal plan with a non-zero quantity.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, does each chosen vegetable also have to be a positive (non-zero) amount, or is it enough that at least two vegetable types are allowed to appear (with the others at zero)?

## Turn 3 - User Simulator

Each chosen vegetable must be a positive (non-zero) amount. It is not enough for at least two vegetable types to merely be allowed to appear; the meal plan must actually include at least two of them with non-zero quantities.

## Turn 4 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — does this 600g include the protein (meat) weight as well, or is the 600g target for the vegetables only with the meat weight on top?

## Turn 4 - User Simulator

The 600g target includes the protein (meat) weight as well. The total weight of all selected foods—both the one protein source and the vegetables—must equal exactly 600 grams.

## Turn 5 - Generic Agent

QUESTION: The fiber content is only given for the four vegetables (okra, carrots, celery, cabbage) — what fiber value should I use for the protein sources (salmon, beef, pork): treat them as 0g fiber per 100g, or do you have specific fiber values for the meats?

## Turn 5 - User Simulator

Treat the protein sources (salmon, beef, pork) as 0g fiber per 100g.

## Turn 6 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15 — is it acceptable to spend less than $15 (i.e., the budget is a ceiling), or must the total cost come as close to $15 as possible?

## Turn 6 - User Simulator

The budget is a ceiling. It is acceptable to spend less than $15.

## Turn 7 - Generic Agent

QUESTION: Are the food quantities allowed to be any continuous (fractional) gram amounts, or must each food be chosen in whole-gram (or some other discrete) increments?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the exactness of the 600g total and the "positive amount" requirements make the model sensitive to how small a quantity counts as "included," should I treat quantities as continuous (any fractional gram allowed, with "positive" meaning strictly greater than zero), or do you need a minimum practical portion size (e.g., at least 10g or 50g) for any food that is included?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: As a default I'll treat quantities as continuous (any fractional gram allowed, with "included" meaning strictly greater than zero) — is that acceptable, or do you need a minimum practical portion size (e.g., at least 10g or 50g) for any food that is included?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Continuous, nonnegative gram amounts for each of the seven foods (salmon, beef, pork, okra, carrots, celery, cabbage).
- **Protein constraint:** Exactly one of the three meats (salmon, beef, pork) is included with a strictly positive amount; the other two are zero.
- **Vegetable constraint:** At least two of the four vegetables (okra, carrots, celery, cabbage) are included with strictly positive amounts.
- **Weight constraint:** Total weight of all selected foods (meat + vegetables) equals exactly 600 grams.
- **Budget constraint:** Total cost ≤ $15 (a ceiling; spending less is fine).
- **Objective:** Maximize total fiber intake.
- **Fiber (per 100g):** okra 3.2g, carrots 2.7g, cabbage 2.0g, celery 1.6g; salmon, beef, pork = 0g.
- **Price (per 100g):** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **Quantities:** Treated as continuous (fractional grams allowed); "included" means strictly greater than zero. (This was deferred by the client; I adopt the continuous reading as the default and flag it.)