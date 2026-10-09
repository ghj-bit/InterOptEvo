# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U2, U3, U4
I need help deciding which restaurants to purchase to maximize annual income, and the total cost of purchased restaurants must not exceed the investment budget.

Annual revenue of each restaurant: Restaurant A: $15,000, Restaurant B: $40,000, Restaurant C: $30,000, Restaurant D: $50,000.

Cost of each restaurant: Restaurant A: 1.6 million, Restaurant B: 2.5 million, Restaurant C: 1.8 million, Restaurant D: 3 million.

Investment budget: 6 million.

## Problem units
- U1 (context): I need help deciding which restaurants to purchase to maximize annual income.
- U2 (data): Annual revenue of each restaurant: Restaurant A: $15,000, Restaurant B: $40,000, Restaurant C: $30,000, Restaurant D: $50,000.
- U3 (data): Cost of each restaurant: Restaurant A: 1.6 million, Restaurant B: 2.5 million, Restaurant C: 1.8 million, Restaurant D: 3 million.
- U4 (data): Investment budget: 6 million.
- U5 (objective): Maximize annual income.
- U6 (constraint): Each restaurant can be purchased at most once.
- U7 (constraint): Total cost of purchased restaurants must not exceed the investment budget.
- U8 (constraint): If Restaurant D is purchased, then Restaurant A cannot be purchased.

## Hidden slot scoring rules
## H1: binary_purchase_constraint
- Severity: P1
- Severity reason: Without clarifying that purchases are all-or-nothing, the agent may model fractional investment, leading to a materially different optimization problem and solution.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must explicitly ask about whether the purchase is binary (whole restaurant) or allows fractional shares.
- Reference acceptable questions:
  - Can the family buy only a part of a restaurant, or do they have to buy the entire restaurant?
  - Is fractional ownership allowed, or is each purchase an all-or-nothing decision?
- Failure modes:
  - Assuming fractional investment is allowed and solving a continuous knapsack problem.
  - Modeling purchase amounts as continuous variables without 0-1 integrality.

## H2: conditional_exclusion_restaurant_D_and_A
- Severity: P1
- Severity reason: If the agent remains unaware of this dependency, the model will treat all restaurant choices as independent, likely selecting both A and D if budget allows, which is not allowed.
- Problem unit ID: U8
- Semantic hit rule: The agent's question must explicitly ask about a restriction or dependency involving Restaurant A and D, particularly that buying D prevents buying A.
- Reference acceptable questions:
  - Are there any restrictions between buying certain restaurants, such as not being able to buy both A and D?
  - If they purchase Restaurant D, does that affect whether they can purchase Restaurant A?
- Failure modes:
  - Assuming all restaurants are independent and including both A and D in the solution when budget allows.
  - Modeling a standard 0-1 knapsack without mutual exclusion constraints.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are you allowed to purchase at most one of each restaurant, or can you buy multiple units of the same restaurant?

## Turn 1 - User Simulator

We can purchase at most one of each restaurant.

## Turn 2 - Generic Agent

QUESTION: Is the goal to maximize total annual revenue, or is there some other income measure (like profit after subtracting costs) you want maximized?

## Turn 2 - User Simulator

The goal is to maximize total annual revenue.

## Turn 3 - Generic Agent

QUESTION: Should every dollar of the 6 million budget be spent, or is it fine to leave part of the budget unused?

## Turn 3 - User Simulator

It is fine to leave part of the budget unused.

## Turn 4 - Generic Agent

QUESTION: Are there any other constraints besides the budget, such as a limit on the number of restaurants you can buy or required restaurants you must include?

## Turn 4 - User Simulator

There is one additional constraint: if Restaurant D is purchased, then Restaurant A cannot be purchased.

## Turn 5 - Generic Agent

QUESTION: Is that restriction one-way only (D excludes A), or does it also work the other way (buying A also prevents buying D)?

## Turn 5 - User Simulator

The restriction is one-way only: if Restaurant D is purchased, then Restaurant A cannot be purchased.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision:** Choose at most one of each restaurant A, B, C, D (binary buy/skip).
- **Objective:** Maximize total annual revenue of purchased restaurants.
- **Revenues:** A = $15,000; B = $40,000; C = $30,000; D = $50,000.
- **Costs:** A = 1.6M; B = 2.5M; C = 1.8M; D = 3.0M.
- **Budget:** Total cost ≤ 6.0M; unused budget is allowed (no requirement to spend it all).
- **Extra constraint:** One-way — if D is purchased, then A cannot be purchased (D ⇒ not A). Buying A does not restrict D beyond this.
- **No other constraints** (no limit on count, no required restaurants).

Model: binary variables x_A, x_B, x_C, x_D ∈ {0,1}; maximize 15000·x_A + 40000·x_B + 30000·x_C + 50000·x_D subject to 1.6M·x_A + 2.5M·x_B + 1.8M·x_C + 3.0M·x_D ≤ 6.0M and x_A + x_D ≤ 1.