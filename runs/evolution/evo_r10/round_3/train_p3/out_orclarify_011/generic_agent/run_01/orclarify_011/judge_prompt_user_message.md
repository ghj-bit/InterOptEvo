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

QUESTION: For the profit target of at least 3000 yuan per week, should profit be computed as total selling revenue minus the total process cost (i.e., subtracting 12 yuan per manufacturing hour, 8 yuan per assembly hour, and 10 yuan per inspection hour actually used), or is it simply total selling revenue with no cost deduction?

## Turn 1 - User Simulator

Profit should be computed as total selling revenue minus the total process cost. That means you subtract 12 yuan per manufacturing hour, 8 yuan per assembly hour, and 10 yuan per inspection hour actually used.

## Turn 2 - Generic Agent

QUESTION: Should the weekly production quantities of Type A and Type B be required to be whole numbers (integer units), or can they be fractional values?

## Turn 2 - User Simulator

The weekly production quantities of Type A and Type B must be whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: The brief says "total weekly profit should be at least 3000 yuan" — is this a hard constraint that the plan must satisfy (i.e., infeasible if profit < 3000), or is 3000 yuan a target to maximize (i.e., maximize profit, with 3000 being a minimum acceptable level)?

## Turn 3 - User Simulator

The 3000 yuan is a hard constraint. The plan must achieve at least 3000 yuan in weekly profit; if profit is less than 3000, the plan is infeasible.

## Turn 4 - Generic Agent

QUESTION: Since the 3000 yuan profit is a hard constraint and there is no stated objective to maximize, what should the plan actually optimize — for example, minimize total production cost, minimize total hours used, minimize total units produced, or is any feasible plan (satisfying all constraints) acceptable?

## Turn 4 - User Simulator

The plan should maximize weekly profit. Additionally, we want to minimize idle time for each process, with weights proportional to the corresponding hourly cost.

## Turn 5 - Generic Agent

QUESTION: For the secondary objective of minimizing idle time weighted by hourly cost, should this be a lexicographic objective (first maximize profit, then among all max-profit plans minimize weighted idle time), or should it be a single combined objective where profit and weighted idle time are added together with some trade-off weight?

## Turn 5 - User Simulator

It should be a lexicographic objective: first maximize profit, then among all max-profit plans minimize weighted idle time.

## Turn 6 - Generic Agent

QUESTION: For the weighted idle time minimization, should the idle time for each process be computed as (capacity − hours actually used), i.e., manufacturing idle = 120 − 20·xA, assembly idle = 80 − (5·xA + 7·xB), inspection idle = 40 − (3·xA + 6·xB), with weights 12, 8, 10 respectively?

## Turn 6 - User Simulator

Yes, that is correct. Idle time for each process is capacity minus hours actually used, and the weights are 12 for manufacturing, 8 for assembly, and 10 for inspection.

## Turn 7 - Generic Agent

QUESTION: Regarding the "at least 5 units of Type A must be produced each week" constraint — is this a strict lower bound (xA ≥ 5), and is there any upper limit on how many units of Type A or Type B can be produced per week beyond what the capacity constraints already imply?

## Turn 7 - User Simulator

Yes, it is a strict lower bound: at least 5 units of Type A must be produced each week. There is no additional upper limit on Type A or Type B beyond what the capacity constraints already imply.

## Turn 8 - Generic Agent

QUESTION: You mentioned "overtime is not allowed" — does this simply mean the three capacity constraints (manufacturing ≤ 120, assembly ≤ 80, inspection ≤ 40) are the only time limits, or is there an additional constraint such as a maximum number of hours any single worker can work per week that I should account for?

## Turn 8 - User Simulator

"Overtime is not allowed" simply means the three capacity constraints are the only time limits: manufacturing ≤ 120 hours, assembly ≤ 80 hours, and inspection ≤ 40 hours. There is no additional per-worker hour limit to account for.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision Variables:**
- xA = weekly production quantity of Type A (non-negative integer)
- xB = weekly production quantity of Type B (non-negative integer)

**Objective (Lexicographic):**
1. **Primary:** Maximize weekly profit = (650·xA + 725·xB) − [12·(20·xA) + 8·(5·xA + 7·xB) + 10·(3·xA + 6·xB)]
2. **Secondary (among all max-profit solutions):** Minimize weighted idle time = 12·(120 − 20·xA) + 8·(80 − 5·xA − 7·xB) + 10·(40 − 3·xA − 6·xB)

**Constraints:**
- Profit ≥ 3000 (hard constraint)
- xA ≥ 5 (minimum Type A production)
- Manufacturing: 20·xA ≤ 120
- Assembly: 5·xA + 7·xB ≤ 80
- Inspection: 3·xA + 6·xB ≤ 40
- xA, xB ∈ ℤ₊ (non-negative integers)

**Notes:**
- "Overtime not allowed" is fully captured by the three capacity constraints.
- No additional upper bounds on xA or xB beyond capacity.
- Profit = revenue − process cost (12 yuan/hr manufacturing, 8 yuan/hr assembly, 10 yuan/hr inspection).