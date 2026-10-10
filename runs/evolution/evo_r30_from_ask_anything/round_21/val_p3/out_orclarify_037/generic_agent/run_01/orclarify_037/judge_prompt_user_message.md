# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U5, U8, U9, U2
I need help creating a weekly production plan for two types of microcomputers in a factory, where both types require the same two production processes. The goal is to maximize total weekly profit, subject to at least 10 units of Model A being produced per week and the weekly production time for Process II being fully utilized, with potential overtime if necessary.

| Process | Model A (hours/unit) | Model B (hours/unit) | Maximum Weekly Processing Capacity (hours) |
| :---: | :---: | :---: | :---: |
| I | 4 | 6 | 150 |
| II | 3 | 2 | 70 |
| Profit ($ per unit) | 300 | 450 |  |

## Problem units
- U1 (context): I need help creating a weekly production plan for two types of microcomputers in a factory.
- U2 (data): | Process | Model A (hours/unit) | Model B (hours/unit) | Maximum Weekly Processing Capacity (hours) |
| :---: | :---: | :---: | :---: |
| I | 4 | 6 | 150 |
| II | 3 | 2 | 70 |
| Profit ($ per unit) | 300 | 450 |  |
- U3 (objective): Maximize total weekly profit.
- U4 (constraint): Total weekly profit must be at least $10,000.
- U5 (constraint): At least 10 units of Model A must be produced per week.
- U6 (constraint): At least 15 units of Model B must be produced per week.
- U7 (constraint): The weekly production time for Process I must be exactly 150 hours.
- U8 (constraint): The weekly production time for Process II should be fully utilized, with potential overtime if necessary.
- U9 (assumption): Both types of microcomputers require the same two production processes.

## Hidden slot scoring rules
## H1: minimum_profit_target
- Severity: P2
- Severity reason: The omission leaves the model as a still‑coherent pure profit maximization problem; the lower bound is a business target, not a structural necessity.
- Problem unit ID: U4
- Semantic hit rule: The Agent’s question must explicitly ask about a minimum profit requirement or a lower bound of $10,000 on weekly profit.
- Reference acceptable questions:
  - Is there a requirement that the total weekly profit must be at least $10,000?
  - Do we have a minimum profit target of $10,000 per week that must be met?
- Failure modes:
  - Assuming no minimum profit constraint is required
  - Assuming the objective is only to maximize profit without a lower bound

## H2: min_production_model_B
- Severity: P2
- Severity reason: Without this detail the model remains a valid production planning problem; the minimum quantity for Model B is a contractual preference, not a formulation‑critical gap.
- Problem unit ID: U6
- Semantic hit rule: The Agent’s question must ask about the minimum production quantity of Model B, specifically at least 15 units per week.
- Reference acceptable questions:
  - Do we have to produce at least 15 units of Model B every week?
  - Is there a contractual requirement for a minimum of 15 units of Model B per week?
- Failure modes:
  - Assuming that there is no minimum production requirement for Model B
  - Forgetting the contractual obligation for Model B

## H3: exact_process_I_time
- Severity: P2
- Severity reason: The model still works with a ≤150 capacity constraint; the exact‑150 requirement is an extra operational target, not a fatal modeling defect.
- Problem unit ID: U7
- Semantic hit rule: The Agent’s question must ask whether Process I time must be exactly 150 hours (i.e., an equality), not merely a capacity upper bound.
- Reference acceptable questions:
  - Must we use exactly 150 hours of Process I each week, not just up to 150?
  - Is it a hard requirement that Process I time equals 150 hours every week?
- Failure modes:
  - Assuming that Process I time is limited to at most 150 hours, not exactly 150
  - Treating the requirement as a simple capacity constraint


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the 70-hour maximum weekly capacity for Process II a hard ceiling that cannot be exceeded, or is it a baseline that can be expanded through overtime at an additional cost?

## Turn 1 - User Simulator

The 70-hour figure is a baseline that can be expanded through overtime if necessary. It is not a hard ceiling.

## Turn 2 - Generic Agent

QUESTION: What is the hourly cost of overtime for Process II that should be subtracted from the profit of each unit produced during those extra hours?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the 150-hour maximum weekly capacity for Process I a hard ceiling that cannot be exceeded, or is it also expandable through overtime?

## Turn 3 - User Simulator

The 150-hour capacity for Process I is a hard ceiling that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the requirement to produce at least 10 units of Model A per week a hard constraint that must be strictly satisfied, or is it a soft target that can be violated if it improves total profit?

## Turn 4 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities for Model A and Model B required to be whole numbers, or can they be fractional values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model B, or can the factory produce any non-negative quantity of Model B as long as the process capacities are respected?

## Turn 6 - User Simulator

There is no maximum weekly production limit for Model B.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model A, or can the factory produce any quantity of Model A above the 10-unit minimum as long as the process capacities are respected?

## Turn 7 - User Simulator

There is no maximum weekly production limit for Model A.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum number of overtime hours that can be scheduled for Process II per week, or is the overtime capacity unlimited?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements for the weekly production plan, such as minimum production levels for Model B, labor availability limits, or material shortages, that are not mentioned in the initial brief?

## Turn 9 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 10 - Generic Agent

QUESTION: Is the contractual requirement to produce at least 15 units of Model B per week a hard constraint that must be strictly satisfied, or is it a soft target that can be violated if it improves total profit?

## Turn 10 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total weekly profit.
2.  **Decision Variables:** Weekly production quantities for Model A ($x_A$) and Model B ($x_B$).
3.  **Profit Coefficients:** Model A yields \$300 per unit; Model B yields \$450 per unit.
4.  **Process I Constraint:** Hard ceiling of 150 hours. Usage is $4x_A + 6x_B \le 150$.
5.  **Process II Constraint:** Baseline capacity is 70 hours, but it is expandable via overtime. The constraint is not a hard ceiling at 70 hours.
6.  **Model A Minimum:** Hard constraint of at least 10 units ($x_A \ge 10$).
7.  **Model B Minimum:** Hard constraint of at least 15 units ($x_B \ge 15$).
8.  **Upper Bounds:** No maximum production limits for either model.
9.  **Non-negativity:** Production quantities must be non-negative.

**Open Assumptions (due to lack of confirmed data):**
1.  **Overtime Cost for Process II:** The hourly cost of overtime for Process II is unknown. I will assume the overtime cost is zero (i.e., overtime hours are free) or that the "fully utilized" phrasing implies we simply need to ensure the 70 hours are used, but since it's not a hard ceiling, the binding constraint for Process II is effectively non-existent unless an overtime cost is provided. *Note: If overtime has a cost, the objective function or constraint needs adjustment. Without a cost, Process II does not limit production.*
2.  **Integrality:** It is unconfirmed whether production quantities must be integers. I will assume continuous variables for the initial formulation, but integer constraints can be added if required.
3.  **Overtime Limit:** It is unconfirmed if there is a maximum limit on overtime hours for Process II. I will assume unlimited overtime capacity for Process II.

**Formulation Note:**
Since Process II is not a hard ceiling and overtime cost is unknown/assumed zero, Process II will likely not be the binding constraint. The model will be driven by the Process I capacity (150 hours) and the minimum production requirements.