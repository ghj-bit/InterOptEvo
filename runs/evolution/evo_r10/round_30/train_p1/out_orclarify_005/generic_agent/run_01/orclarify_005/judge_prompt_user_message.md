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

QUESTION: For the "exactly one protein source" requirement, does that mean the chosen protein must have a strictly positive amount (any amount greater than zero counts), or must it meet some minimum portion size?

## Turn 2 - User Simulator

The chosen protein must have a strictly positive amount. Any amount greater than zero counts; there is no minimum portion size requirement.

## Turn 3 - Generic Agent

QUESTION: For the "at least two kinds of vegetables" requirement, does each chosen vegetable need a strictly positive amount (any amount greater than zero counts), or must each meet some minimum portion size?

## Turn 3 - User Simulator

Each chosen vegetable needs a strictly positive amount. Any amount greater than zero counts; there is no minimum portion size requirement.

## Turn 4 - Generic Agent

QUESTION: The brief gives fiber content only for the four vegetables and no fiber values for salmon, beef, or pork — should I treat the fiber content of all three meats as zero grams per 100g?

## Turn 4 - User Simulator

Yes, treat the fiber content of salmon, beef, and pork as zero grams per 100g.

## Turn 5 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — should this be treated as a strict equality (the sum of all selected food weights must be exactly 600g, no more and no less)?

## Turn 5 - User Simulator

Yes, the total weight must be exactly 600 grams. No more and no less.

## Turn 6 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15 — should I treat this as a strict upper bound (total cost ≤ $15, with any leftover budget simply unused)?

## Turn 6 - User Simulator

Yes, treat the budget as a strict upper bound: total cost must be less than or equal to $15. Any leftover budget is simply unused.

## Turn 7 - Generic Agent

QUESTION: Are the food amounts allowed to be any continuous (fractional) values in grams, or must they be chosen in discrete units (e.g., whole 100g portions or some other fixed increment)?

## Turn 7 - User Simulator

The food amounts can be any continuous (fractional) values in grams. There is no requirement to choose in discrete units or fixed increments.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on how much of any single food can be selected (e.g., a maximum grams per food), or can a food in principle make up the entire 600g as long as the other constraints are satisfied?

## Turn 8 - User Simulator

There is no upper limit on how much of any single food can be selected. A food can, in principle, make up the entire 600g as long as all other constraints are satisfied.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize total fiber intake (in grams) for tonight's dinner.
- **Foods available (7):** salmon, beef, pork (proteins) and okra, carrots, celery, cabbage (vegetables).
- **Decision variables:** continuous, non-negative grams of each of the 7 foods. No upper bound on any single food.
- **Protein rule:** exactly one of {salmon, beef, pork} must be chosen with a strictly positive amount (no minimum portion size).
- **Vegetable rule:** at least two of {okra, carrots, celery, cabbage} must be chosen, each with a strictly positive amount (no minimum portion size).
- **Weight:** total weight of all selected foods must equal exactly 600 g.
- **Budget:** total cost must be ≤ $15 (leftover budget unused).
- **Fiber per 100 g:** okra 3.2, carrots 2.7, celery 1.6, cabbage 2.0; salmon, beef, pork = 0.
- **Price per 100 g:** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.

The "exactly one protein" and "at least two vegetables" rules are cardinality/selection constraints (each selected item must have amount > 0), which I will model with binary selection variables and a small positive lower bound (or an equivalent formulation) tied to the continuous amount variables.