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

QUESTION: Is the annual income you want to maximize the sum of the listed annual revenues of the restaurants you purchase (i.e., revenue minus nothing else), or should I subtract the purchase cost or any other expenses from revenue when computing income?

## Turn 1 - User Simulator

Yes, the annual income to maximize is simply the sum of the listed annual revenues of the restaurants you purchase. Do not subtract the purchase cost or any other expenses from the revenue when computing the income.

## Turn 2 - Generic Agent

QUESTION: Is each restaurant available for purchase at most once (a standard 0/1 selection), or could you buy multiple copies of the same restaurant?

## Turn 2 - User Simulator

Each restaurant can be purchased at most once.

## Turn 3 - Generic Agent

QUESTION: Is the $6 million investment budget a hard ceiling that the total purchase cost must not exceed, or is it an exact amount that must be spent?

## Turn 3 - User Simulator

The $6 million investment budget is a hard ceiling; the total purchase cost must not exceed it.

## Turn 4 - Generic Agent

QUESTION: Are there any other constraints or rules I should account for — for example, a requirement to buy at least one restaurant, a limit on the number of restaurants, or any pairing/dependency rules between restaurants — or is the only constraint the $6 million budget ceiling?

## Turn 4 - User Simulator

There is one additional dependency rule: if Restaurant D is purchased, then Restaurant A cannot be purchased.

## Turn 5 - Generic Agent

QUESTION: Is the dependency rule one-way only (purchasing D forbids A, but A can still be purchased without D), or is it two-way (A and D can never be purchased together, regardless of which one is chosen)?

## Turn 5 - User Simulator

The rule is one-way only: purchasing D forbids A, but A can still be purchased without D.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Binary selection for each of the four restaurants (A, B, C, D); each can be purchased at most once.
- **Objective:** Maximize total annual income = sum of the annual revenues of the purchased restaurants (no costs or other expenses subtracted).
  - Revenues: A = $15,000; B = $40,000; C = $30,000; D = $50,000.
- **Budget constraint:** Total purchase cost ≤ $6,000,000 (hard ceiling, not an exact spend).
  - Costs: A = $1.6M; B = $2.5M; C = $1.8M; D = $3.0M.
- **Dependency rule (one-way):** If D is purchased, then A cannot be purchased. A may still be purchased when D is not.
- **No other constraints:** No minimum number of restaurants, no maximum count, no other pairing rules.

This is a 0/1 integer program with four binary variables, one budget constraint, and one conditional (implication) constraint.