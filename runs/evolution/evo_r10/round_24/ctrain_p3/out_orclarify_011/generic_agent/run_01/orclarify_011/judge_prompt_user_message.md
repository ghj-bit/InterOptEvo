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

QUESTION: For the profit target of at least 3000 yuan per week, should profit be calculated as total selling revenue minus the process costs (manufacturing, assembly, inspection) for the hours actually used, or is there a different profit definition you have in mind (for example, a fixed per-unit profit margin that already accounts for all costs)?

## Turn 1 - User Simulator

Profit should be calculated as total selling revenue minus the process costs (manufacturing, assembly, inspection) for the hours actually used.

## Turn 2 - Generic Agent

QUESTION: The table shows Type B requires 0 hours of manufacturing per unit — should I treat this as Type B genuinely needing no manufacturing time (so the 120-hour manufacturing limit only constrains Type A), or is 0 a placeholder and Type B actually uses some manufacturing hours that you can provide?

## Turn 2 - User Simulator

Type B genuinely needs no manufacturing time.

## Turn 3 - Generic Agent

QUESTION: The brief says "at least 5 units of Type A must be produced each week" — should Type A and Type B production quantities be required to be whole numbers (integer units), or is it acceptable for the plan to specify fractional units (e.g., 5.5 units of Type A)?

## Turn 3 - User Simulator

Production quantities must be whole numbers.

## Turn 4 - Generic Agent

QUESTION: The brief says total weekly profit should be "at least 3000 yuan" — is 3000 yuan a minimum profit requirement (a constraint the plan must satisfy), or is the goal to maximize total weekly profit subject to the resource limits, with 3000 yuan just being a target you expect to reach?

## Turn 4 - User Simulator

3000 yuan is a minimum profit requirement that the plan must satisfy.

## Turn 5 - Generic Agent

QUESTION: Since profit must be at least 3000 yuan and the resource limits cap how much can be produced, is the goal to find any feasible plan that meets all the requirements, or should the plan maximize total weekly profit subject to all the constraints (with 3000 yuan as a lower bound that must also hold)?

## Turn 5 - User Simulator

The plan should maximize total weekly profit subject to all the constraints, with 3000 yuan as a lower bound that must also hold.

## Turn 6 - Generic Agent

QUESTION: Are there any upper limits on how many units of Type A or Type B can be produced per week (for example, demand caps or maximum production capacities), or are the only limits on production quantities the three resource constraints (120 manufacturing, 80 assembly, 40 inspection hours) plus the minimum of 5 Type A units?

## Turn 6 - User Simulator

The only limits on production quantities are the three resource constraints (120 manufacturing, 80 assembly, 40 inspection hours) plus the minimum of 5 Type A units.

## Turn 7 - Generic Agent

QUESTION: The process costs are given per hour (12 yuan/hour for manufacturing, 8 yuan/hour for assembly, 10 yuan/hour for inspection) — should these costs be charged only for the hours actually used by the units produced, or should they be charged for the full weekly capacity (i.e., 120, 80, and 40 hours) regardless of how much is actually used?

## Turn 7 - User Simulator

These costs should be charged only for the hours actually used by the units produced.

## Turn 8 - Generic Agent

QUESTION: The brief says "overtime is not allowed" — does this simply mean the three resource limits (120, 80, 40 hours) are hard caps that cannot be exceeded, or is there an additional standard-hours baseline (e.g., regular shift hours) that must be met exactly, with the caps being the regular-hours limit?

## Turn 8 - User Simulator

It simply means the three resource limits (120, 80, 40 hours) are hard caps that cannot be exceeded.

## Turn 9 - Generic Agent

QUESTION: If a resource (e.g., manufacturing) is not fully used in the optimal plan, is that acceptable — i.e., the 120/80/40 hour figures are maximums that don't have to be fully consumed, or must each resource be used up to its full capacity?

## Turn 9 - User Simulator

The 120/80/40 hour figures are maximums that don't have to be fully consumed.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** x_A = number of Type A units, x_B = number of Type B units, both non-negative integers (whole units).
- **Objective:** Maximize total weekly profit.
- **Profit definition:** Total selling revenue minus process costs for hours actually used.
  - Revenue: 650·x_A + 725·x_B
  - Manufacturing cost: 12 yuan/hour × 20·x_A hours
  - Assembly cost: 8 yuan/hour × (5·x_A + 7·x_B) hours
  - Inspection cost: 10 yuan/hour × (3·x_A + 6·x_B) hours
  - Profit = (650·x_A + 725·x_B) − [12·(20·x_A) + 8·(5·x_A + 7·x_B) + 10·(3·x_A + 6·x_B)]
- **Constraints:**
  1. Manufacturing: 20·x_A ≤ 120 (Type B uses 0 manufacturing hours — confirmed genuine)
  2. Assembly: 5·x_A + 7·x_B ≤ 80
  3. Inspection: 3·x_A + 6·x_B ≤ 40
  4. Minimum Type A: x_A ≥ 5
  5. Minimum profit: Profit ≥ 3000 yuan
  6. Non-negativity and integrality: x_A, x_B ∈ ℤ₊
- **No other limits:** No demand caps, no upper bounds beyond the resource constraints.
- **Resource limits are hard caps** (overtime not allowed) but need not be fully consumed.
- **Process costs charged only on hours actually used**, not on full capacity.