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

QUESTION: Is the 3000 yuan weekly profit target a hard minimum constraint that the plan must satisfy, or is it a target you want to maximize?

## Turn 1 - User Simulator

It is a hard minimum constraint. The plan must achieve at least 3000 yuan in weekly profit.

## Turn 2 - Generic Agent

QUESTION: Is the objective to minimize total weekly cost, or is the goal simply to find any feasible plan that meets the profit and production constraints?

## Turn 2 - User Simulator

The goal is to maximize weekly profit.

## Turn 3 - Generic Agent

QUESTION: Is the "at least 5 units of Type A" requirement a hard minimum constraint that must be met every week, or is it a soft target that can be relaxed if needed?

## Turn 3 - User Simulator

It is a hard minimum constraint that must be met every week.

## Turn 4 - Generic Agent

QUESTION: Are the production quantities for Type A and Type B required to be whole numbers (integers), or can they be fractional values?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: For the profit calculation, is the "process cost" applied to the total hours used in each department (manufacturing, assembly, inspection), or is it a fixed cost per unit produced regardless of hours?

## Turn 5 - User Simulator

The process cost is applied to the total hours used in each department.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as maximum production limits per type, minimum production for Type B, or dependencies between the two types?

## Turn 6 - User Simulator

No, there are no other constraints or requirements beyond those already mentioned.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total weekly profit.
2.  **Decision Variables:** Weekly production quantity of Type A motorcycles ($x_A$) and Type B motorcycles ($x_B$).
3.  **Variable Domain:** Non-negative. *Assumption: Quantities are continuous (not necessarily integers), as integrality was not confirmed.*
4.  **Profit Calculation:**
    *   Revenue: $650 x_A + 725 x_B$.
    *   Cost: Calculated as (Total Manufacturing Hours $\times$ 12) + (Total Assembly Hours $\times$ 8) + (Total Inspection Hours $\times$ 10).
    *   Profit = Revenue - Total Process Cost.
5.  **Constraints:**
    *   **Minimum Profit:** Total weekly profit $\ge$ 3000 yuan (Hard constraint).
    *   **Minimum Type A Production:** $x_A \ge$ 5 (Hard constraint).
    *   **Manufacturing Time:** $20 x_A + 0 x_B \le$ 120 hours.
    *   **Assembly Time:** $5 x_A + 7 x_B \le$ 80 hours.
    *   **Inspection Time:** $3 x_A + 6 x_B \le$ 40 hours.
    *   **No Overtime:** Implicitly covered by the time caps above.
6.  **Other Requirements:** None.

**Explicit Assumptions:**
*   Production quantities ($x_A, x_B$) are treated as continuous variables. If integer production is required, the model would need to be adjusted to an Integer Linear Program.