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

QUESTION: Is the profit to be maximized/checked as selling price minus the process cost (manufacturing, assembly, inspection hours per unit times their hourly rates), i.e. Type A profit = 650 − (20×12 + 5×8 + 3×10) = 150 yuan and Type B profit = 725 − (0×12 + 7×8 + 6×10) = 517 yuan?

## Turn 1 - User Simulator

Yes, that is correct. The profit for each unit is calculated as the selling price minus the total process cost, where the process cost is the sum of the hours required for each process multiplied by the respective hourly rate.

So:
*   **Type A profit:** 650 − (20×12 + 5×8 + 3×10) = 150 yuan
*   **Type B profit:** 725 − (0×12 + 7×8 + 6×10) = 517 yuan

## Turn 2 - Generic Agent

QUESTION: Should the number of Type A and Type B motorcycles produced each week be restricted to whole units (integers), or can they be treated as continuous quantities?

## Turn 2 - User Simulator

The number of motorcycles produced must be whole units (integers). You cannot produce a fraction of a motorcycle.

## Turn 3 - Generic Agent

QUESTION: Is the "at least 3000 yuan weekly profit" a hard constraint that must be satisfied (i.e., the plan is infeasible if profit falls below 3000), or is 3000 a target to be met while the actual objective is to maximize profit?

## Turn 3 - User Simulator

The 3000 yuan is a hard constraint. The plan is infeasible if the total weekly profit falls below 3000 yuan. The actual objective is to maximize profit, subject to this minimum requirement.

## Turn 4 - Generic Agent

QUESTION: Is the "at least 5 units of Type A each week" a hard lower bound (Type A production must be ≥ 5, with no upper limit on Type A), or is it an exact target of exactly 5 units?

## Turn 4 - User Simulator

It is a hard lower bound. Type A production must be at least 5 units per week, with no upper limit specified for Type A.

## Turn 5 - Generic Agent

QUESTION: Since Type B requires zero manufacturing hours, is there any separate limit on Type B production (such as a maximum number of units per week), or is Type B only limited by the assembly (80 hours) and inspection (40 hours) capacities?

## Turn 5 - User Simulator

Type B is only limited by the assembly (80 hours) and inspection (40 hours) capacities. There is no separate maximum number of units per week for Type B.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables**
- x_A = number of Type A motorcycles produced per week (integer, ≥ 0)
- x_B = number of Type B motorcycles produced per week (integer, ≥ 0)

**Objective**
- Maximize total weekly profit = 150·x_A + 517·x_B
  - Type A profit: 650 − (20×12 + 5×8 + 3×10) = 150 yuan/unit
  - Type B profit: 725 − (0×12 + 7×8 + 6×10) = 517 yuan/unit

**Constraints**
1. Manufacturing time: 20·x_A + 0·x_B ≤ 120 hours
2. Assembly time: 5·x_A + 7·x_B ≤ 80 hours
3. Inspection time: 3·x_A + 6·x_B ≤ 40 hours
4. Minimum Type A production: x_A ≥ 5 (hard lower bound, no upper limit)
5. Minimum profit: 150·x_A + 517·x_B ≥ 3000 (hard constraint)
6. Integrality: x_A, x_B are non-negative integers

**Notes**
- Overtime is not allowed, so the three capacity figures (120, 80, 40) are strict upper bounds.
- Type B has no separate unit cap; it is limited only by assembly and inspection capacities.
- The 3000-yuan profit floor is a hard constraint (infeasibility if violated), while the objective is to maximize profit.