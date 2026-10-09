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

```json
{
  "action": "ASK",
  "question": "How are restaurant purchases treated in this decision?",
  "options": [
    {
      "id": "A",
      "text": "Each restaurant is either fully purchased or not purchased at all."
    },
    {
      "id": "B",
      "text": "A restaurant can be purchased in partial ownership with cost and revenue scaled to the owned share."
    },
    {
      "id": "C",
      "text": "Restaurants can be purchased in whole units only, but multiple units of the same restaurant are possible."
    }
  ],
  "allow_other": true
}
```

Question:
How are restaurant purchases treated in this decision?

Options:
A. Each restaurant is either fully purchased or not purchased at all.
B. A restaurant can be purchased in partial ownership with cost and revenue scaled to the owned share.
C. Restaurants can be purchased in whole units only, but multiple units of the same restaurant are possible.
D. None of the above — I'd like to explain in my own words.

## Turn 1 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 2 - Generic Agent

```json
{
  "action": "ASK",
  "question": "What does 'annual income' mean for each purchased restaurant?",
  "options": [
    {
      "id": "A",
      "text": "Annual income is exactly the annual revenue listed for each restaurant."
    },
    {
      "id": "B",
      "text": "Annual income is annual revenue minus some annual operating cost not listed here."
    },
    {
      "id": "C",
      "text": "Annual income is a net profit figure that already accounts for all costs."
    }
  ],
  "allow_other": true
}
```

Question:
What does 'annual income' mean for each purchased restaurant?

Options:
A. Annual income is exactly the annual revenue listed for each restaurant.
B. Annual income is annual revenue minus some annual operating cost not listed here.
C. Annual income is a net profit figure that already accounts for all costs.
D. None of the above — I'd like to explain in my own words.

## Turn 2 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 3 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Does the investment budget need to be fully spent, or can part of it remain unused?",
  "options": [
    {
      "id": "A",
      "text": "The budget is an upper limit; unused budget is allowed."
    },
    {
      "id": "B",
      "text": "The budget must be fully spent on purchased restaurants."
    },
    {
      "id": "C",
      "text": "The budget must be spent as much as possible, but small leftover is acceptable."
    }
  ],
  "allow_other": true
}
```

Question:
Does the investment budget need to be fully spent, or can part of it remain unused?

Options:
A. The budget is an upper limit; unused budget is allowed.
B. The budget must be fully spent on purchased restaurants.
C. The budget must be spent as much as possible, but small leftover is acceptable.
D. None of the above — I'd like to explain in my own words.

## Turn 3 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 4 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "The user wants to select which restaurants to purchase to maximize total annual income, where each restaurant is either fully purchased or not purchased, annual income equals the listed annual revenue, and the total purchase cost must not exceed the $6 million budget with unused budget allowed. Confirmed facts: whole-restaurant purchase only; income equals listed annual revenue; budget is an upper limit. Remaining minor assumption: no other business rules (e.g., exclusivity, dependencies) apply."
}
```

The user wants to select which restaurants to purchase to maximize total annual income, where each restaurant is either fully purchased or not purchased, annual income equals the listed annual revenue, and the total purchase cost must not exceed the $6 million budget with unused budget allowed. Confirmed facts: whole-restaurant purchase only; income equals listed annual revenue; budget is an upper limit. Remaining minor assumption: no other business rules (e.g., exclusivity, dependencies) apply.