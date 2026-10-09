# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U8, U2, U3, U4
I need help designing promotional packages to clear out last season's inventory. Total shirts used in packages cannot exceed 200, total pants used in packages cannot exceed 100, and the number of A packages sold must be at least 20 while the number of B packages sold must be at least 10.

Available inventory: 200 shirts, 100 pairs of pants.

Package A: 1 shirt, 2 pairs of pants, price £30. Package B: 3 shirts, 1 pair of pants, price £50.

Minimum desired sales: 20 package A, 10 package B.

## Problem units
- U1 (context): I need help designing promotional packages to clear out last season's inventory.
- U2 (data): Available inventory: 200 shirts, 100 pairs of pants.
- U3 (data): Package A: 1 shirt, 2 pairs of pants, price £30. Package B: 3 shirts, 1 pair of pants, price £50.
- U4 (data): Minimum desired sales: 20 package A, 10 package B.
- U5 (constraint): Total shirts used in packages cannot exceed 200.
- U6 (constraint): Total pants used in packages cannot exceed 100.
- U7 (constraint): Number of A packages sold must be at least 20.
- U8 (constraint): Number of B packages sold must be at least 10.
- U9 (objective): Maximize total revenue from selling packages A and B.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without knowing the objective, a modeling agent cannot define the optimization criterion. The entire problem formulation is impossible without specifying what should be maximized.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must explicitly ask about the optimization goal, mentioning "revenue" or "objective" or "maximize" in the context of what to optimize.
- Reference acceptable questions:
  - What exactly are we trying to maximize? Is it total revenue, profit, or something else?
  - Should we just focus on getting the most money from selling the packages?
- Failure modes:
  - Silent assumption that the goal is to maximize profit rather than revenue.
  - Incorrectly assuming the objective is to minimize leftover inventory.


# Full Transcript

## Turn 1 - Generic Agent

```json
{
  "action": "ASK",
  "question": "What is the main business objective for this promotional package design?",
  "options": [
    {
      "id": "A",
      "text": "Maximize total revenue from package sales."
    },
    {
      "id": "B",
      "text": "Maximize the total number of packages sold."
    },
    {
      "id": "C",
      "text": "Clear as much of the last season's inventory as possible."
    }
  ],
  "allow_other": true
}
```

Question:
What is the main business objective for this promotional package design?

Options:
A. Maximize total revenue from package sales.
B. Maximize the total number of packages sold.
C. Clear as much of the last season's inventory as possible.
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
  "question": "Are the minimum desired sales of 20 A packages and 10 B packages hard requirements that must always be met, or soft targets that can be missed if needed?",
  "options": [
    {
      "id": "A",
      "text": "They are hard requirements that must always be met."
    },
    {
      "id": "B",
      "text": "They are soft targets that can be missed with a penalty."
    },
    {
      "id": "C",
      "text": "They are soft targets that can be missed freely."
    }
  ],
  "allow_other": true
}
```

Question:
Are the minimum desired sales of 20 A packages and 10 B packages hard requirements that must always be met, or soft targets that can be missed if needed?

Options:
A. They are hard requirements that must always be met.
B. They are soft targets that can be missed with a penalty.
C. They are soft targets that can be missed freely.
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
  "question": "Does leftover inventory after packaging have any financial value or cost that should affect the objective?",
  "options": [
    {
      "id": "A",
      "text": "Leftover inventory has no salvage value or disposal cost."
    },
    {
      "id": "B",
      "text": "Leftover inventory has a salvage value that should be counted."
    },
    {
      "id": "C",
      "text": "Leftover inventory incurs a disposal cost that should be counted."
    }
  ],
  "allow_other": true
}
```

Question:
Does leftover inventory after packaging have any financial value or cost that should affect the objective?

Options:
A. Leftover inventory has no salvage value or disposal cost.
B. Leftover inventory has a salvage value that should be counted.
C. Leftover inventory incurs a disposal cost that should be counted.
D. None of the above — I'd like to explain in my own words.

## Turn 3 - User Simulator

```json
{
  "choice": "D",
  "comment": "The objective is only to maximize total revenue from selling packages A and B; no salvage value or disposal cost for leftover inventory was provided."
}
```

Business user response: none of the offered options match. The objective is only to maximize total revenue from selling packages A and B; no salvage value or disposal cost for leftover inventory was provided.

## Turn 4 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Is there any upper limit on how many packages can be sold beyond the inventory limits?",
  "options": [
    {
      "id": "A",
      "text": "No upper limit beyond available inventory."
    },
    {
      "id": "B",
      "text": "There is a maximum total number of packages that can be sold."
    },
    {
      "id": "C",
      "text": "There is a maximum for each package type separately."
    }
  ],
  "allow_other": true
}
```

Question:
Is there any upper limit on how many packages can be sold beyond the inventory limits?

Options:
A. No upper limit beyond available inventory.
B. There is a maximum total number of packages that can be sold.
C. There is a maximum for each package type separately.
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
  "question": "Are packages A and B sold independently, or is there any requirement linking their sales together?",
  "options": [
    {
      "id": "A",
      "text": "A and B are sold independently with no linkage."
    },
    {
      "id": "B",
      "text": "A and B must be sold together as a bundle."
    },
    {
      "id": "C",
      "text": "Selling one package type affects demand for the other."
    }
  ],
  "allow_other": true
}
```

Question:
Are packages A and B sold independently, or is there any requirement linking their sales together?

Options:
A. A and B are sold independently with no linkage.
B. A and B must be sold together as a bundle.
C. Selling one package type affects demand for the other.
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
  "action": "ASK",
  "question": "Is the decision limited to choosing how many of the predefined A and B packages to sell, or can the package compositions themselves be redesigned?",
  "options": [
    {
      "id": "A",
      "text": "Only choose how many A and B packages to sell; compositions are fixed."
    },
    {
      "id": "B",
      "text": "The package compositions can be redesigned as part of the decision."
    },
    {
      "id": "C",
      "text": "Both compositions and sales quantities can be decided."
    }
  ],
  "allow_other": true
}
```

Question:
Is the decision limited to choosing how many of the predefined A and B packages to sell, or can the package compositions themselves be redesigned?

Options:
A. Only choose how many A and B packages to sell; compositions are fixed.
B. The package compositions can be redesigned as part of the decision.
C. Both compositions and sales quantities can be decided.
D. None of the above — I'd like to explain in my own words.

## Turn 6 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 7 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "The business goal is to maximize total revenue from selling fixed-composition promotional packages A and B. Package A uses 1 shirt and 2 pairs of pants and sells for £30; Package B uses 3 shirts and 1 pair of pants and sells for £50. Available inventory is 200 shirts and 100 pairs of pants. Minimum sales requirements are 20 A packages and 10 B packages, and these are hard requirements. There is no upper limit on total packages beyond inventory, no salvage value or disposal cost for leftover inventory, and A and B are sold independently. The only decision is how many of each package to sell. Remaining minor assumption: package compositions and prices are fixed as given."
}
```

The business goal is to maximize total revenue from selling fixed-composition promotional packages A and B. Package A uses 1 shirt and 2 pairs of pants and sells for £30; Package B uses 3 shirts and 1 pair of pants and sells for £50. Available inventory is 200 shirts and 100 pairs of pants. Minimum sales requirements are 20 A packages and 10 B packages, and these are hard requirements. There is no upper limit on total packages beyond inventory, no salvage value or disposal cost for leftover inventory, and A and B are sold independently. The only decision is how many of each package to sell. Remaining minor assumption: package compositions and prices are fixed as given.