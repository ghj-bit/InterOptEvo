# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U8, U2, U3, U4, U5
The Li family plans to invest their retirement fund in commercial real estate, and I need help deciding which properties to purchase, with the constraints that the total cost of purchased properties must not exceed the budget, and if they purchase Property 4, they cannot purchase Property 3.

Annual income: Property 1: $12,500, Property 2: $35,000, Property 3: $23,000, Property 4: $100,000.

Cost: Property 1: $1.5 million, Property 2: $2.1 million, Property 3: $2.3 million, Property 4: $4.2 million.

Budget: $7 million.

There is only one of each property available.

## Problem units
- U1 (context): The Li family plans to invest their retirement fund in commercial real estate. I need help deciding which properties to purchase.
- U2 (data): Annual income: Property 1: $12,500, Property 2: $35,000, Property 3: $23,000, Property 4: $100,000.
- U3 (data): Cost: Property 1: $1.5 million, Property 2: $2.1 million, Property 3: $2.3 million, Property 4: $4.2 million.
- U4 (data): Budget: $7 million.
- U5 (data): There is only one of each property available.
- U6 (objective): Maximize total annual income.
- U7 (constraint): The total cost of purchased properties must not exceed the budget.
- U8 (constraint): If they purchase Property 4, they cannot purchase Property 3.

## Hidden slot scoring rules
## H1: annual_income_definition
- Severity: P2
- Severity reason: The objective is clear—maximize the sum of incomes of selected properties—but the problem does not state whether the given annual income figures are gross or net of ongoing expenses (maintenance, taxes, etc.). The agent can still formulate a valid optimization model under the common assumption that these are net incomes, so this is a low-impact detail. Clarifying it prevents an overly optimistic income projection if the user intended gross figures.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must explicitly ask about the definition of the annual income—specifically whether it is gross or net, or whether expenses, taxes, or other deductions are already factored in.
- Reference acceptable questions:
  - Do the annual income numbers already account for property taxes, maintenance, and management costs, or are they just the rental income we'd collect before expenses?
  - Are the annual income amounts you gave the net income we actually get after all operating expenses, or do we need to subtract those ourselves?
- Failure modes:
  - The agent silently assumes the given annual incomes are net profit, leading to a model that ignores potential hidden costs.
  - The agent assumes there are no ongoing expenses at all, which could overstate the real return if the user had preliminary gross figures in mind.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the goal to maximize the total annual income from the purchased properties?

## Turn 1 - User Simulator

Yes, the goal is to maximize the total annual income from the purchased properties.

## Turn 2 - Generic Agent

QUESTION: Is the $7 million budget a hard cap on the total cost of purchased properties, meaning they can spend any amount up to and including $7 million?

## Turn 2 - User Simulator

Yes, the $7 million budget is a hard cap on the total cost of purchased properties.

## Turn 3 - Generic Agent

QUESTION: If they purchase Property 4, they cannot purchase Property 3 — does this restriction work only in that one direction (buying Property 4 blocks Property 3), or does it also mean that if they purchase Property 3 they cannot purchase Property 4?

## Turn 3 - User Simulator

The restriction works in both directions: if they purchase Property 4, they cannot purchase Property 3, and if they purchase Property 3, they cannot purchase Property 4.

## Turn 4 - Generic Agent

QUESTION: Are there any other restrictions or preferences I should know about, such as a minimum number of properties to purchase, a maximum number, or any other properties or conditions not mentioned?

## Turn 4 - User Simulator

No, there are no other restrictions or preferences.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision:** Choose which subset of the 4 properties to purchase. Each property is available in exactly one unit, so each is a binary (buy / don't buy) decision.
- **Objective:** Maximize total annual income from the purchased properties.
  - Property 1: $12,500/yr, Property 2: $35,000/yr, Property 3: $23,000/yr, Property 4: $100,000/yr.
- **Budget constraint (hard cap):** Total cost of purchased properties ≤ $7 million.
  - Property 1: $1.5M, Property 2: $2.1M, Property 3: $2.3M, Property 4: $4.2M.
- **Mutual exclusion:** Property 3 and Property 4 cannot both be purchased (two-way restriction).
- **No other constraints:** No minimum/maximum number of properties, no other conditions.

This is a 0-1 knapsack-style selection problem with one additional mutual-exclusion constraint.