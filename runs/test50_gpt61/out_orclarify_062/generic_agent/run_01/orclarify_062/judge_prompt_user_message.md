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

QUESTION: Can each restaurant be purchased at most once, or may multiple locations of the same restaurant be purchased?

## Turn 1 - User Simulator

Each restaurant can be purchased at most once.

## Turn 2 - Generic Agent

READY_TO_MODEL

Confirmed understanding: Each restaurant can be purchased at most once. Select a combination of restaurants that maximizes annual revenue, with total purchase cost no greater than the $6 million investment budget.

The optimal purchase is:

- Restaurant B: Cost $2.5 million; annual revenue $40,000
- Restaurant D: Cost $3.0 million; annual revenue $50,000

**Total cost:** $5.5 million  
**Remaining budget:** $500,000  
**Total annual revenue:** **$90,000**

This is the highest annual income achievable within the budget.