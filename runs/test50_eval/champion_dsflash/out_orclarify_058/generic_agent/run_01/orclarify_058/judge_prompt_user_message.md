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


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Should the farm grow exactly two types of fruit, or at most two types?

## Turn 1 - User Simulator

At most two types.

## Turn 2 - Generic Agent

QUESTION: Is the 120 acres a limit that the total planted area must not exceed, or must all 120 acres be planted?

## Turn 2 - User Simulator

The 120 acres is a limit that the total planted area must not exceed.

## Turn 3 - Generic Agent

QUESTION: For the "apples at least three times lemons" rule, does it apply only when both apples and lemons are among the chosen fruits, or must it hold regardless?

## Turn 3 - User Simulator

It must hold regardless.

## Turn 4 - Generic Agent

QUESTION: If lemons are not grown at all, is the apples-at-least-three-times-lemons rule automatically satisfied?

## Turn 4 - User Simulator

Yes, if lemons are not grown at all, the rule is automatically satisfied.

## Turn 5 - Generic Agent

QUESTION: Since at most two fruit types may be grown, and the apple-lemon ratio rule must hold regardless, is it acceptable to grow only lemons (with zero apples), or does growing lemons require also growing apples?

## Turn 5 - User Simulator

It is acceptable to grow only lemons with zero apples.

## Turn 6 - Generic Agent

QUESTION: Can a fruit type be chosen with zero acres planted (i.e., is choosing a type the same as committing to grow it), or does each chosen type need a positive acreage?

## Turn 6 - User Simulator

Each chosen type needs a positive acreage.

## Turn 7 - Generic Agent

QUESTION: Is there any minimum positive acreage required for a chosen fruit (like a whole number of acres or a minimum block size), or can it be any positive amount?

## Turn 7 - User Simulator

It can be any positive amount.

## Turn 8 - Generic Agent

QUESTION: Is the goal to maximize total profit?

## Turn 8 - User Simulator

Yes, the goal is to maximize total profit.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or business rules I should know about, such as limits on water, labor, or per-fruit caps?

## Turn 9 - User Simulator

No, there are no other constraints or business rules beyond what has already been discussed.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total profit.
- **Land:** Total planted area must not exceed 120 acres (not required to use all of it).
- **Fruit types:** Apples, pears, oranges, lemons. At most two types may be grown.
- **Chosen types:** Each chosen type must have strictly positive acreage; any positive amount is allowed (no minimum block size, no integer requirement).
- **Apple–lemon rule:** Apples' acreage must be at least three times lemons' acreage, and this must hold regardless of which fruits are chosen. If lemons are not grown, the rule is automatically satisfied.
- **Growing only lemons (zero apples) is allowed.**
- **Profit per acre:** apples $2000, pears $1800, oranges $2200, lemons $3000.
- **No other constraints** (no water, labor, or per-fruit caps).

Model: choose a subset of at most two fruit types, assign positive acreage to each chosen type, total ≤ 120, with the apple–lemon ratio rule enforced whenever apples and lemons are both present (and trivially satisfied otherwise), maximizing total profit.