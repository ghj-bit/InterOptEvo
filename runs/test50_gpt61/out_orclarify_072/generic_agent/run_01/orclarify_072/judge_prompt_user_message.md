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

QUESTION: Should I choose the feasible combination of properties that maximizes the Li family’s total annual income?

## Turn 1 - User Simulator

Yes.

## Turn 2 - Generic Agent

READY_TO_MODEL

The goal is to maximize total annual income while:

- Keeping total purchase cost at or below `$7 million`
- Purchasing at most one of each property
- Not purchasing Properties 3 and 4 together

The optimal purchase is **Property 2 and Property 4**:

- Total cost: `$2.1M + $4.2M = $6.3M`
- Total annual income: `$35,000 + $100,000 = $135,000`
- Remaining budget: `$700,000`

This is better than every other feasible combination.