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

QUESTION: Are the annual revenue figures for each restaurant the net profit after all operating expenses, or are they gross revenue from which I should subtract additional costs?

## Turn 1 - User Simulator

The annual revenue figures are the net profit after all operating expenses.

## Turn 2 - Generic Agent

QUESTION: Are the restaurant costs one-time purchase prices, or do they include recurring annual expenses?

## Turn 2 - User Simulator

The restaurant costs are one-time purchase prices.

## Turn 3 - Generic Agent

QUESTION: Can you purchase a restaurant more than once, or is each restaurant available for purchase only once?

## Turn 3 - User Simulator

Each restaurant is available for purchase only once.

## Turn 4 - Generic Agent

READY_TO_MODEL
I understand you need to select a subset of the four available restaurants to purchase, with the goal of maximizing the total annual net profit from the selected restaurants, subject to the constraint that the total one-time purchase cost does not exceed the $6 million investment budget.

Confirmed details:
- Objective: Maximize total annual net profit.
- Constraint: Total one-time purchase cost <= $6,000,000.
- Each restaurant can be purchased at most once (binary decision).
- The annual revenue figures provided are net profits.
- The cost figures are one-time purchase prices.

Data:
- Restaurant A: Profit $15,000, Cost $1,600,000
- Restaurant B: Profit $40,000, Cost $2,500,000
- Restaurant C: Profit $30,000, Cost $1,800,000
- Restaurant D: Profit $50,000, Cost $3,000,000