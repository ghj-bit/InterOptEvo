# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U8, U9, U10, U2
I need help creating a weekly production plan for two types of small motorcycles, where total weekly profit should be at least 3000 yuan and at least 5 units of Type A must be produced each week, while overtime is not allowed, and total weekly manufacturing time must not exceed 120 hours, total weekly assembly time must not exceed 80 hours, and total weekly inspection time must not exceed 40 hours.

| Type | Manufacturing (hours/unit) | Assembly (hours/unit) | Inspection (hours/unit) | Selling Price (Yuan/unit) |
| :---: | :---: | :---: | :---: | :---: |
| Type A | 20 | 5 | 3 | 650 |
| Type B | 0 | 7 | 6 | 725 |
| Max weekly capacity | 120 | 80 | 40 | - |
| Process cost (Yuan/hour) | 12 | 8 | 10 | - |

## Problem units
- U1 (context): I need help creating a weekly production plan for two types of small motorcycles.
- U2 (data): | Type | Manufacturing (hours/unit) | Assembly (hours/unit) | Inspection (hours/unit) | Selling Price (Yuan/unit) |
| :---: | :---: | :---: | :---: | :---: |
| Type A | 20 | 5 | 3 | 650 |
| Type B | 0 | 7 | 6 | 725 |
| Max weekly capacity | 120 | 80 | 40 | - |
| Process cost (Yuan/hour) | 12 | 8 | 10 | - |
- U3 (objective): Maximize weekly profit.
- U4 (objective): Idle time of each process should be minimized, with weights proportional to the corresponding hourly cost.
- U5 (constraint): Total weekly profit should be at least 3000 yuan.
- U6 (constraint): At least 5 units of Type A must be produced each week.
- U7 (constraint): Overtime is not allowed.
- U8 (constraint): Total weekly manufacturing time must not exceed 120 hours.
- U9 (constraint): Total weekly assembly time must not exceed 80 hours.
- U10 (constraint): Total weekly inspection time must not exceed 40 hours.

## Hidden slot scoring rules
## H1: missing_profit_maximization_objective
- Severity: P0
- Severity reason: Without an explicit objective to maximize weekly profit, the modeling agent cannot define an optimization direction. The problem would be ill‑posed and impossible to formulate as a meaningful optimization model.
- Problem unit ID: U3
- Semantic hit rule: The agent must ask about the objective function, explicitly inquiring what should be optimized (e.g., maximize profit or another metric).
- Reference acceptable questions:
  - What is the objective we are trying to achieve? Is it to maximize profit?
  - Should we maximize weekly profit, or is there another goal?
- Failure modes:
  - Silently assuming the objective is to minimize total cost.
  - Assuming the model only needs to satisfy constraints without a specific objective (feasibility).

## H2: missing_idle_time_minimization_objective
- Severity: P1
- Severity reason: The model would still be a coherent profit‑maximization problem, but the operational requirement to minimize idle time of each process with cost‑proportional weights is missing, making the plan materially different from the intended business problem.
- Problem unit ID: U4
- Semantic hit rule: The agent must ask about minimizing idle time or any multi‑objective aspect, specifically referencing idle time or unused capacity for the manufacturing, assembly, or inspection processes.
- Reference acceptable questions:
  - Do we also need to minimize idle time for the processes, and how should we weight it?
  - Is there a secondary goal like minimizing idle time, perhaps weighted by the hourly cost of each process?
- Failure modes:
  - Assuming only profit maximization matters, completely ignoring idle time considerations.
  - Assuming idle time is not part of the optimization and treating it only as a slack variable in constraints.
  - Assuming equal weights for idle time instead of using cost‑proportional weights.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the profit to be maximized the net profit after deducting the process costs (manufacturing 12 yuan/hour, assembly 8 yuan/hour, inspection 10 yuan/hour) from the selling price, or is it simply the total revenue from sales?

## Turn 1 - User Simulator

It is the net profit after deducting the process costs from the selling price.

## Turn 2 - Generic Agent

QUESTION: Should the production quantities of Type A and Type B be required to be whole numbers (integer units), or can they be fractional?

## Turn 2 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: The brief says "total weekly profit should be at least 3000 yuan" — is 3000 yuan a minimum profit requirement (a constraint the plan must satisfy), or is the goal to maximize profit with 3000 yuan just a target for reference?

## Turn 3 - User Simulator

It is a minimum profit requirement that the plan must satisfy.

## Turn 4 - Generic Agent

QUESTION: Since profit must be at least 3000 yuan, what should the plan actually optimize — for example, minimize total production cost, minimize total hours used, or is any feasible plan meeting all the requirements acceptable?

## Turn 4 - User Simulator

The plan should maximize weekly profit.

## Turn 5 - Generic Agent

QUESTION: Type B requires 0 hours of manufacturing — does this mean Type B uses no manufacturing time at all, or is the 0 a placeholder and Type B actually does consume some manufacturing time?

## Turn 5 - User Simulator

Type B uses no manufacturing time at all.

## Turn 6 - Generic Agent

QUESTION: The constraint says "at least 5 units of Type A must be produced each week" — is there also an upper limit on how many units of Type A (or Type B) can be produced per week, or is the only upper bound the resource capacities?

## Turn 6 - User Simulator

The only upper bounds are the resource capacities.

## Turn 7 - Generic Agent

QUESTION: Are there any minimum production requirements for Type B, or can Type B production be zero in a week?

## Turn 7 - User Simulator

There are no minimum production requirements for Type B; it can be zero.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two types of small motorcycles, Type A and Type B.
- **Decision variables:** Weekly production quantities x_A and x_B, both non-negative integers.
- **Objective:** Maximize total weekly net profit.
- **Net profit per unit:** Selling price minus process costs (manufacturing at 12 yuan/hour, assembly at 8 yuan/hour, inspection at 10 yuan/hour).
  - Type A: 650 − (20×12 + 5×8 + 3×10) = 650 − (240 + 40 + 30) = 650 − 310 = 340 yuan/unit
  - Type B: 725 − (0×12 + 7×8 + 6×10) = 725 − (0 + 56 + 60) = 725 − 116 = 609 yuan/unit
- **Constraints:**
  - Manufacturing time: 20·x_A + 0·x_B ≤ 120 hours
  - Assembly time: 5·x_A + 7·x_B ≤ 80 hours
  - Inspection time: 3·x_A + 6·x_B ≤ 40 hours
  - Minimum Type A production: x_A ≥ 5
  - Minimum profit: 340·x_A + 609·x_B ≥ 3000 yuan
  - No overtime (all resource limits are hard upper bounds)
  - x_A, x_B are non-negative integers
- **No upper bound** on production beyond resource capacities; **no minimum** for Type B.