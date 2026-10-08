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

QUESTION: Should the model allow selecting any of the seven listed foods (salmon, beef, pork, okra, carrots, celery, cabbage) in any amounts, or are the three meats (salmon, beef, pork) excluded from the dinner and only the four vegetables (okra, carrots, celery, cabbage) may be chosen?

## Turn 1 - User Simulator

The three meats (salmon, beef, pork) are not excluded. You may select from all seven listed foods. However, you must select exactly one protein source from the three meats (salmon, beef, or pork).

## Turn 2 - Generic Agent

QUESTION: For the "exactly one protein source" rule, does choosing a meat mean you must consume a positive amount of it (any amount greater than zero counts), or must the chosen meat meet some minimum amount?

## Turn 2 - User Simulator

Any amount greater than zero counts. There is no minimum amount required for the chosen meat.

## Turn 3 - Generic Agent

QUESTION: The brief lists fiber content only for the four vegetables (okra, carrots, celery, cabbage) and gives no fiber values for salmon, beef, or pork — should I treat the fiber content of the three meats as zero grams per 100g?

## Turn 3 - User Simulator

Yes, treat the fiber content of the three meats as zero grams per 100g.

## Turn 4 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — is this a strict equality (the selected foods must sum to precisely 600g, no more and no less), or is 600g a target that could be slightly exceeded or fallen short of?

## Turn 4 - User Simulator

It is a strict equality. The selected foods must sum to precisely 600 grams, no more and no less.

## Turn 5 - Generic Agent

QUESTION: The budget constraint says total cost must not exceed $15 — is $15 a hard ceiling (cost ≤ $15, with any leftover budget simply unused), or must the spending come as close to $15 as possible?

## Turn 5 - User Simulator

$15 is a hard ceiling. The total cost must not exceed $15, and any leftover budget is simply unused.

## Turn 6 - Generic Agent

QUESTION: Can the amounts of each food be any continuous (fractional) value in grams, or must the quantities be whole numbers of grams (or some other discrete unit)?

## Turn 6 - User Simulator

The amounts of each food can be any continuous (fractional) value in grams.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much of a single food can be selected (for example, a maximum amount per food), or can any one food make up the entire 600 grams as long as the other constraints are satisfied?

## Turn 7 - User Simulator

There is no limit on how much of a single food can be selected. Any one food can make up the entire 600 grams as long as the other constraints are satisfied.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Continuous, non-negative amount (in grams) for each of the 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- **Objective:** Maximize total fiber intake. Fiber per 100g: okra 3.2g, carrots 2.7g, cabbage 2.0g, celery 1.6g; salmon, beef, pork = 0g.
- **Protein rule:** Exactly one of the three meats (salmon, beef, pork) must be selected with a strictly positive amount; the other two must be zero.
- **Weight constraint:** Total weight of all selected foods must equal exactly 600 grams.
- **Budget constraint:** Total cost must not exceed $15 (hard ceiling; leftover budget unused). Price per 100g: salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.
- **No per-food upper bounds** beyond what the weight and budget constraints imply.
- **Quantities are continuous** (fractional grams allowed).