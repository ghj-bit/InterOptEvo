# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U8, U2, U3
I need help creating a plan for growing fruit on my farm, where the land used to grow apples should be at least three times the land used to grow lemons, and Vicky and David are unwilling to grow more than two types of fruit.

Farm total area: 120 acres.

Profit per acre: apples $2000, pears $1800, oranges $2200, lemons $3000.

## Problem units
- U1 (context): I need help creating a plan for growing fruit on my farm.
- U2 (data): Farm total area: 120 acres.
- U3 (data): Profit per acre: apples $2000, pears $1800, oranges $2200, lemons $3000.
- U4 (objective): Maximize total profit.
- U5 (constraint): The land used to grow apples should be at least twice the land used to grow pears.
- U6 (constraint): The land used to grow apples should be at least three times the land used to grow lemons.
- U7 (constraint): The land used to grow oranges must be twice the land used to grow lemons.
- U8 (constraint): Vicky and David are unwilling to grow more than two types of fruit.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without the objective, the modeling agent cannot formulate any meaningful optimization problem.
- Problem unit ID: U4
- Semantic hit rule: The Agent's question explicitly asks what the objective or goal of the optimization is, specifically inquiring whether it is profit maximization or another metric.
- Reference acceptable questions:
  - What is the main goal we're trying to achieve with this farm plan—are we looking to maximize profit, or something else?
  - Should the plan maximize total profit, or are we targeting a different objective like minimizing land use?
- Failure modes:
  - Silently assuming the objective is profit maximization without confirming
  - Proceeding directly to model formulation without clarifying the objective

## H2: apples_pears_min_ratio
- Severity: P1
- Severity reason: Without this constraint, the model will likely produce a plan that violates the intended planting proportion between apples and pears, leading to a materially different result.
- Problem unit ID: U5
- Semantic hit rule: The Agent's question asks about a lower‑bound ratio or proportionality between apple and pear acreage, mentioning either a minimum multiple or a specific relationship.
- Reference acceptable questions:
  - Is there any rule about how the apple acreage relates to the pear acreage, like a minimum ratio?
  - Do you need the area for apples to be at least twice the area for pears?
- Failure modes:
  - Assuming there is no required relationship between apple and pear acreage
  - Not asking about any planting‑ratio constraints

## H3: oranges_lemons_exact_ratio
- Severity: P1
- Severity reason: Without this constraint, the model would miss the exact proportionality rule between oranges and lemons, yielding a plan that may be invalid from the growers' perspective.
- Problem unit ID: U7
- Semantic hit rule: The Agent's question asks about an exact ratio or fixed relationship between orange and lemon acreage, specifically mentioning a factor of two or equality of the kind 'orange = 2 × lemon'.
- Reference acceptable questions:
  - Is there a fixed relationship between the orange and lemon acreage, for example must oranges be exactly twice the lemons?
  - Does the orange area need to be exactly twice the lemon area?
- Failure modes:
  - Assuming no fixed relationship between orange and lemon acreage
  - Forgetting to ask about a precise proportionality between these two fruits


# Atomic Question Map

Q1 (turn 1): Should the plan maximize total profit from the farm?
Q2 (turn 2): Which fruit types are actually available to grow on the farm: apples, pears, oranges, lemons, or only some subset of these?
Q3 (turn 3): Does the limit of no more than two types of fruit mean we can choose to grow one or two types, or must we grow exactly two types?
Q4 (turn 4): If the farm grows only apples or only lemons, does the rule that apple land must be at least three times lemon land still apply?
Q5 (turn 5): Must the plan use all 120 acres for fruit, or can some land be left unused?
Q6 (turn 6): Since the 120-acre usage question still needs internal confirmation, should we proceed for now by treating 120 acres as a maximum that may be left partly unused?
Q7 (turn 7): Is the limit of growing no more than two types of fruit a strict requirement that cannot be violated, or is it a preference that could be exceeded if it increases profit?
Q8 (turn 8): If the farm grows apples but no lemons, does the rule that apple land must be at least three times lemon land still apply, or is it only relevant when lemons are also grown?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Should the plan maximize total profit from the farm?

## Turn 1 - User Simulator

Yes, the goal is to maximize total profit from growing the fruit.

## Turn 2 - Generic Agent

QUESTION: Which fruit types are actually available to grow on the farm: apples, pears, oranges, lemons, or only some subset of these?

## Turn 2 - User Simulator

All four are available to consider: apples, pears, oranges, and lemons.

## Turn 3 - Generic Agent

QUESTION: Does the limit of no more than two types of fruit mean we can choose to grow one or two types, or must we grow exactly two types?

## Turn 3 - User Simulator

It means no more than two types, so growing one or two types would both be acceptable.

## Turn 4 - Generic Agent

QUESTION: If the farm grows only apples or only lemons, does the rule that apple land must be at least three times lemon land still apply?

## Turn 4 - User Simulator

Yes, that rule still applies. If there are no lemons, then the apple land requirement is at least three times zero, which is fine.

## Turn 5 - Generic Agent

QUESTION: Must the plan use all 120 acres for fruit, or can some land be left unused?

## Turn 5 - User Simulator

That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the 120-acre usage question still needs internal confirmation, should we proceed for now by treating 120 acres as a maximum that may be left partly unused?

## Turn 6 - User Simulator

Yes, for now treat 120 acres as a maximum that may be left partly unused.

## Turn 7 - Generic Agent

QUESTION: Is the limit of growing no more than two types of fruit a strict requirement that cannot be violated, or is it a preference that could be exceeded if it increases profit?

## Turn 7 - User Simulator

It’s a strict requirement that cannot be violated.

## Turn 8 - Generic Agent

QUESTION: If the farm grows apples but no lemons, does the rule that apple land must be at least three times lemon land still apply, or is it only relevant when lemons are also grown?

## Turn 8 - User Simulator

It still applies. If no lemons are grown, then the apple land just needs to be at least three times zero.

## Turn 9 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.850

Confidence rationale: All formulation-changing ambiguities are resolved: the objective is to maximize total profit; the four crops (apples, pears, oranges, lemons) are the decision variables in acres; the apple-to-lemon ratio constraint (apple land >= 3 * lemon land) applies unconditionally; at most two fruit types may be grown (strict cardinality constraint); and 120 acres is a maximum that may be left partly unused. The only residual uncertainty is that the 120-acre usage was provisionally set as a maximum pending internal confirmation, so the final plan may need revision if that changes to a full-utilization requirement.

Summary: Maximize total profit from allocating up to 120 acres among apples ($2000/acre), pears ($1800/acre), oranges ($2200/acre), and lemons ($3000/acre). Constraints: total planted area <= 120 acres; apple acres >= 3 * lemon acres (applies even when lemons are zero); at most two fruit types may be grown (strict). Land may be left unused. Decision variables are acres planted per fruit type.