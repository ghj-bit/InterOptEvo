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

QUESTION: Are salmon, beef, and pork allowed in the dinner selection, or should the meal be limited to the four fiber-bearing vegetables (okra, carrots, celery, cabbage)?

## Turn 1 - User Simulator

Salmon, beef, and pork are allowed. In fact, the meal must include exactly one of those three protein sources. The four vegetables (okra, carrots, celery, and cabbage) are also part of the selection, with at least two of them required.

## Turn 2 - Generic Agent

QUESTION: For the protein source, is the amount of salmon/beef/pork chosen a continuous weight (any gram amount), or must it be a fixed portion size?

## Turn 2 - User Simulator

The amount is a continuous weight; any gram amount is allowed.

## Turn 3 - Generic Agent

QUESTION: For the vegetables, is the amount of each chosen vegetable also a continuous weight (any gram amount), or must each be a fixed portion size?

## Turn 3 - User Simulator

The amount of each chosen vegetable is also a continuous weight; any gram amount is allowed.

## Turn 4 - Generic Agent

QUESTION: When you say the meal must include at least two of the four vegetables, does that mean at least two vegetables must have a strictly positive weight, or is it enough that at least two are "selected" even if one ends up with zero weight?

## Turn 4 - User Simulator

At least two vegetables must have a strictly positive weight.

## Turn 5 - Generic Agent

QUESTION: Is the $15 budget a hard ceiling (total cost must be ≤ $15), or should the total cost be exactly $15?

## Turn 5 - User Simulator

The $15 budget is a hard ceiling; the total cost must be ≤ $15.

## Turn 6 - Generic Agent

QUESTION: The total weight must equal exactly 600 grams — does that 600g include the protein source, or is it only the vegetables that must sum to 600g?

## Turn 6 - User Simulator

The 600g total includes the protein source. The combined weight of the selected protein and vegetables must equal exactly 600 grams.

## Turn 7 - Generic Agent

QUESTION: Fiber content is only given for the four vegetables (salmon, beef, and pork have no fiber listed). Should I treat the protein sources as contributing 0g of fiber to the objective?

## Turn 7 - User Simulator

Yes, treat the protein sources as contributing 0g of fiber.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total fiber intake (grams).

**Decision variables:**
- Continuous weight (grams) for each of 7 foods: salmon, beef, pork, okra, carrots, celery, cabbage.
- Binary selection variables to enforce the "exactly one protein" and "at least two vegetables" rules.

**Fiber (per 100g):** okra 3.2, carrots 2.7, celery 1.6, cabbage 2.0; salmon/beef/pork = 0.

**Price (per 100g):** salmon $4, beef $3.6, pork $1.8, okra $2.6, carrots $1.2, celery $1.6, cabbage $2.3.

**Constraints:**
1. Total cost ≤ $15 (hard ceiling).
2. Total weight (protein + vegetables) = exactly 600g.
3. Exactly one of {salmon, beef, pork} is selected (positive weight).
4. At least two of {okra, carrots, celery, cabbage} have strictly positive weight.
5. All weights ≥ 0.

**Modeling notes:**
- "Strictly positive" for the at-least-two-vegetables rule will be enforced via a small epsilon lower bound (e.g., ≥ 1g) on selected vegetables, combined with binary selection variables.
- "Exactly one protein" enforced via binary variables summing to 1, with each protein weight bounded by M × its binary.
- The 600g equality constraint means the protein weight is determined by the vegetable weights (protein = 600 − sum of vegetable weights), so the protein must be non-negative, i.e., vegetable total ≤ 600g.