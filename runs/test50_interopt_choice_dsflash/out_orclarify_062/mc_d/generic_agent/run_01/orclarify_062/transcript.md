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