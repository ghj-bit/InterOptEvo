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

QUESTION: Should the dinner be limited to only the four fiber-containing vegetables (okra, carrots, celery, cabbage), or may the meats (salmon, beef, pork) also be selected as part of the 600 grams?

## Turn 1 - User Simulator

The meats may also be selected. In fact, the plan must include exactly one protein source from salmon, beef, or pork, along with at least two of the four vegetables.

## Turn 2 - Generic Agent

QUESTION: For the "at least two of the four vegetables" requirement, does each selected vegetable need a minimum amount (e.g., at least 100g), or is any positive amount of a vegetable enough to count it as "selected"?

## Turn 2 - User Simulator

Any positive amount of a vegetable is enough to count it as selected.

## Turn 3 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — is that a hard equality (the plan must come out to precisely 600g), or is 600g a target that could be slightly exceeded or fallen short of if needed?

## Turn 3 - User Simulator

It is a hard equality. The total weight must come out to precisely 600 grams.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum or maximum amount for the single protein source, or can it be any positive amount as long as the total weight equals 600g?

## Turn 4 - User Simulator

There is no minimum or maximum amount specified for the protein source. It can be any positive amount, as long as the total weight of all selected foods equals 600 grams.

## Turn 5 - Generic Agent

QUESTION: Since the protein source must be included (exactly one of salmon, beef, or pork) and can be any positive amount, is there a minimum amount of protein that must be included (e.g., at least 100g), or can it be arbitrarily small (e.g., 1g)?

## Turn 5 - User Simulator

It can be arbitrarily small, such as 1g. There is no minimum amount specified for the protein source.

## Turn 6 - Generic Agent

QUESTION: For the vegetables, is there any minimum amount per selected vegetable (e.g., at least 100g), or can each selected vegetable also be arbitrarily small (e.g., 1g)?

## Turn 6 - User Simulator

Each selected vegetable can also be arbitrarily small, such as 1g. There is no minimum amount specified per vegetable.

## Turn 7 - Generic Agent

QUESTION: Is there any maximum amount for any single food item (e.g., no more than 300g of one item), or can any single food make up the entire 600g as long as the other requirements (one protein, at least two vegetables) are met?

## Turn 7 - User Simulator

There is no maximum amount for any single food item. Any single food can make up the entire 600g, as long as the other requirements (exactly one protein, at least two vegetables) are met.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total fiber intake (in grams).

**Foods available:**
- Proteins (exactly one must be selected): salmon ($4/100g), beef ($3.6/100g), pork ($1.8/100g)
- Vegetables (at least two must be selected): okra (3.2g fiber/100g, $2.6/100g), carrots (2.7g fiber/100g, $1.2/100g), celery (1.6g fiber/100g, $1.6/100g), cabbage (2g fiber/100g, $2.3/100g)

**Decision variables:**
- Continuous, non-negative weight (in grams) for each of the 7 foods.
- Binary selection variables for each food (to enforce "exactly one protein" and "at least two vegetables").

**Constraints:**
1. Total weight equals exactly 600g (hard equality).
2. Total cost does not exceed $15.
3. Exactly one protein source is selected (sum of protein binary variables = 1).
4. At least two vegetables are selected (sum of vegetable binary variables ≥ 2).
5. A food's weight is positive only if its binary selection variable is 1 (linking constraint).
6. No minimum or maximum per-item amount beyond the binary selection (any positive amount counts as "selected").

**Fiber content (per 100g):** okra 3.2g, carrots 2.7g, celery 1.6g, cabbage 2g. Proteins have no fiber content stated, so they contribute 0g fiber.

**Price (per 100g):** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.