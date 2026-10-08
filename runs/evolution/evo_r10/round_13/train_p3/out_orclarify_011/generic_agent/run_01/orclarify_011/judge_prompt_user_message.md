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

QUESTION: For the profit target of at least 3000 yuan per week, should profit be calculated as total selling revenue minus the process costs (manufacturing, assembly, inspection) applied to the hours actually used, or as total selling revenue minus the process costs applied to the full weekly capacity (120, 80, 40 hours) regardless of how much is used?

## Turn 1 - User Simulator

Profit should be calculated as total selling revenue minus the process costs applied to the hours actually used.

## Turn 2 - Generic Agent

QUESTION: Should the number of Type A and Type B motorcycles produced each week be restricted to whole units (integers), or is it acceptable to treat them as continuous quantities in the plan?

## Turn 2 - User Simulator

The number of Type A and Type B motorcycles produced each week must be restricted to whole units (integers).

## Turn 3 - Generic Agent

QUESTION: The table shows Type B requires 0 hours of manufacturing, which means the 120-hour manufacturing limit only constrains Type A (max 6 units). Is that 0 correct, or should Type B actually consume some manufacturing time?

## Turn 3 - User Simulator

The 0 is correct. Type B does not consume any manufacturing time.

## Turn 4 - Generic Agent

QUESTION: The brief says "total weekly profit should be at least 3000 yuan" — is this a hard constraint that the plan must satisfy (i.e., infeasible if profit can't reach 3000), or is 3000 a target to maximize (i.e., maximize profit subject to the other constraints, with 3000 being a minimum acceptable level)?

## Turn 4 - User Simulator

The 3000 yuan is a hard constraint. The plan must satisfy a total weekly profit of at least 3000 yuan.

## Turn 5 - Generic Agent

QUESTION: Since profit must be at least 3000 yuan (a hard constraint) and there is no other stated goal, what should the plan actually optimize — for example, minimize total process cost, minimize total hours used, maximize total units produced, or is any feasible plan that meets all constraints acceptable?

## Turn 5 - User Simulator

The plan should maximize weekly profit.

## Turn 6 - Generic Agent

QUESTION: Are there any upper limits on how many units of Type A or Type B can be produced per week (e.g., demand caps or storage limits), or are the only upper bounds the resource constraints (manufacturing, assembly, inspection hours)?

## Turn 6 - User Simulator

The only upper bounds are the resource constraints (manufacturing, assembly, inspection hours).

## Turn 7 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables:**
- x_A = number of Type A motorcycles produced per week (non-negative integer)
- x_B = number of Type B motorcycles produced per week (non-negative integer)

**Objective:**
- Maximize total weekly profit = (650·x_A + 725·x_B) − (12·(20·x_A + 0·x_B) + 8·(5·x_A + 7·x_B) + 10·(3·x_A + 6·x_B))
- Simplified: Maximize (650·x_A + 725·x_B) − (240·x_A + 40·x_A + 30·x_A + 56·x_B + 48·x_B)
- = Maximize (650·x_A + 725·x_B) − (310·x_A + 104·x_B)
- = Maximize 340·x_A + 621·x_B

**Constraints:**
1. Manufacturing time: 20·x_A + 0·x_B ≤ 120
2. Assembly time: 5·x_A + 7·x_B ≤ 80
3. Inspection time: 3·x_A + 6·x_B ≤ 40
4. Minimum Type A production: x_A ≥ 5
5. Minimum profit: 340·x_A + 621·x_B ≥ 3000
6. Integrality: x_A, x_B ∈ ℤ₊ (non-negative integers)

**Key confirmations from the client:**
- Profit = revenue minus process costs on hours actually used (not full capacity).
- Production quantities must be whole units.
- Type B's 0 manufacturing hours is correct.
- The 3000 yuan profit is a hard constraint (not just a target).
- The objective is to maximize weekly profit.
- No demand caps or storage limits beyond the resource constraints.
- Overtime is not allowed (resource caps are strict upper bounds).