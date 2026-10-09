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

```json
{
  "action": "ASK",
  "question": "What is the Li family's main goal when choosing which properties to buy?",
  "options": [
    {
      "id": "A",
      "text": "Maximize total annual income from the purchased properties."
    },
    {
      "id": "B",
      "text": "Minimize total purchase cost while still buying properties."
    },
    {
      "id": "C",
      "text": "Balance income against cost, such as maximizing income per dollar spent."
    }
  ],
  "allow_other": true
}
```

Question:
What is the Li family's main goal when choosing which properties to buy?

Options:
A. Maximize total annual income from the purchased properties.
B. Minimize total purchase cost while still buying properties.
C. Balance income against cost, such as maximizing income per dollar spent.
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
  "question": "Can the Li family buy a partial share of a property, or must each property be bought entirely or not at all?",
  "options": [
    {
      "id": "A",
      "text": "Each property must be bought entirely or not at all."
    },
    {
      "id": "B",
      "text": "They may buy any fractional share of a property."
    },
    {
      "id": "C",
      "text": "They may buy fractional shares only for some properties."
    }
  ],
  "allow_other": true
}
```

Question:
Can the Li family buy a partial share of a property, or must each property be bought entirely or not at all?

Options:
A. Each property must be bought entirely or not at all.
B. They may buy any fractional share of a property.
C. They may buy fractional shares only for some properties.
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
  "question": "Are there any other business rules the Li family wants to apply beyond the budget limit and the Property 4/Property 3 exclusion?",
  "options": [
    {
      "id": "A",
      "text": "No other rules apply; only the budget limit and the Property 4/Property 3 exclusion matter."
    },
    {
      "id": "B",
      "text": "They also require a minimum total annual income from the purchased properties."
    },
    {
      "id": "C",
      "text": "They also require diversification, such as buying at least two different properties."
    }
  ],
  "allow_other": true
}
```

Question:
Are there any other business rules the Li family wants to apply beyond the budget limit and the Property 4/Property 3 exclusion?

Options:
A. No other rules apply; only the budget limit and the Property 4/Property 3 exclusion matter.
B. They also require a minimum total annual income from the purchased properties.
C. They also require diversification, such as buying at least two different properties.
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
  "action": "ASK",
  "question": "Does the Li family need to spend the full $7 million budget, or can they leave some budget unused?",
  "options": [
    {
      "id": "A",
      "text": "They may leave part of the budget unused."
    },
    {
      "id": "B",
      "text": "They must spend the entire $7 million budget."
    },
    {
      "id": "C",
      "text": "They must spend at least a specified minimum portion of the budget."
    }
  ],
  "allow_other": true
}
```

Question:
Does the Li family need to spend the full $7 million budget, or can they leave some budget unused?

Options:
A. They may leave part of the budget unused.
B. They must spend the entire $7 million budget.
C. They must spend at least a specified minimum portion of the budget.
D. None of the above — I'd like to explain in my own words.

## Turn 4 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 5 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Does the Li family have any requirement about how many properties they must purchase?",
  "options": [
    {
      "id": "A",
      "text": "No requirement; any number from zero to four is acceptable."
    },
    {
      "id": "B",
      "text": "They must purchase at least a minimum number of properties."
    },
    {
      "id": "C",
      "text": "They must purchase exactly a specified number of properties."
    }
  ],
  "allow_other": true
}
```

Question:
Does the Li family have any requirement about how many properties they must purchase?

Options:
A. No requirement; any number from zero to four is acceptable.
B. They must purchase at least a minimum number of properties.
C. They must purchase exactly a specified number of properties.
D. None of the above — I'd like to explain in my own words.

## Turn 5 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 6 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "Confirmed: The Li family wants to maximize total annual income by choosing which of the four properties to purchase in full, subject to a $7 million budget cap, a rule that Property 3 and Property 4 cannot both be purchased, and only one unit of each property being available. Unused budget is allowed, and there are no minimum income, diversification, or property-count requirements. Remaining minor assumption: none affecting the business problem."
}
```

Confirmed: The Li family wants to maximize total annual income by choosing which of the four properties to purchase in full, subject to a $7 million budget cap, a rule that Property 3 and Property 4 cannot both be purchased, and only one unit of each property being available. Unused budget is allowed, and there are no minimum income, diversification, or property-count requirements. Remaining minor assumption: none affecting the business problem.