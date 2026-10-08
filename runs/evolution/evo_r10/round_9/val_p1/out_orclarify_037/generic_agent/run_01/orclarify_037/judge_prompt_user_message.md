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

QUESTION: When you say Process II's weekly production time must be "fully utilized, with potential overtime if necessary," do you mean (1) Process II must run exactly at its 70-hour capacity with no overtime allowed, (2) Process II must run at least 70 hours and overtime beyond 70 hours is allowed at some extra cost, or (3) Process II must run at least 70 hours and overtime beyond 70 hours is allowed at no extra cost?

## Turn 1 - User Simulator

It means option (2): Process II must run at least 70 hours, and overtime beyond 70 hours is allowed at some extra cost.

## Turn 2 - Generic Agent

QUESTION: What is the overtime cost per hour for Process II, and is there any upper limit on how many overtime hours can be used in a week?

## Turn 2 - User Simulator

I need to check internally for the specific overtime cost per hour and any upper limit on overtime hours for Process II.

## Turn 3 - Generic Agent

QUESTION: Is there a minimum number of Model B units that must be produced each week, or can Model B production be zero?

## Turn 3 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 4 - Generic Agent

QUESTION: Is the 150-hour maximum weekly capacity for Process I a hard limit that cannot be exceeded (no overtime allowed on Process I), or can Process I also run overtime beyond 150 hours?

## Turn 4 - User Simulator

The 150-hour capacity for Process I is a hard limit; it cannot be exceeded.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values?

## Turn 5 - User Simulator

I need to check internally whether the weekly production quantities of Model A and Model B must be whole numbers or can be treated as continuous values.

## Turn 6 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" a hard minimum that must be met, or is it a target that can be relaxed if doing so would increase total profit?

## Turn 6 - User Simulator

It is a hard minimum that must be met.

## Turn 7 - Generic Agent

QUESTION: Is there any maximum weekly production limit (upper bound) on the number of units of Model A or Model B that can be produced, or is production only limited by the process capacities?

## Turn 7 - User Simulator

I need to check internally whether there are any maximum weekly production limits (upper bounds) on the number of units of Model A or Model B beyond the process capacities.

## Turn 8 - Generic Agent

QUESTION: When Process II runs overtime beyond 70 hours, is the overtime cost deducted from the profit (i.e., it reduces the objective), or is it just a feasibility constraint that doesn't affect the profit calculation?

## Turn 8 - User Simulator

The overtime cost is deducted from the profit; it reduces the objective.

## Turn 9 - Generic Agent

QUESTION: Is there any demand limit or market constraint on how many units of Model A or Model B can be sold per week, or can the factory produce and sell unlimited quantities as long as process capacities are respected?

## Turn 9 - User Simulator

I need to check internally whether there are any demand limits or market constraints on how many units of Model A or Model B can be sold per week.

## Turn 10 - Generic Agent

QUESTION: For the overtime on Process II, is the overtime cost a fixed hourly rate (e.g., $X per overtime hour) that applies uniformly to all overtime hours, or does it vary (e.g., different rates for different ranges of overtime hours)?

## Turn 10 - User Simulator

I need to check internally whether the overtime cost for Process II is a fixed hourly rate or varies by range of overtime hours.

## Turn 11 - Generic Agent

QUESTION: Is the 70-hour capacity for Process II the regular-time capacity, meaning that the first 70 hours are "regular" and any hours beyond 70 are "overtime," or is the 70-hour figure already inclusive of some overtime?

## Turn 11 - User Simulator

The 70-hour figure is the regular-time capacity. The first 70 hours are "regular," and any hours beyond 70 are "overtime."

## Turn 12 - Generic Agent

QUESTION: Is there any other constraint or requirement I haven't asked about that would affect the weekly production plan, such as labor availability, raw material limits, or minimum utilization requirements for Process I?

## Turn 12 - User Simulator

Yes, there is a minimum utilization requirement for Process I: the weekly production time for Process I must be exactly 150 hours, not just up to 150.

## Turn 13 - Generic Agent

QUESTION: Is the requirement that Process I runs exactly 150 hours a hard equality constraint that must be satisfied in every feasible solution, or is it a target that can be relaxed if doing so would increase total profit?

## Turn 13 - User Simulator

It is a hard equality constraint that must be satisfied in every feasible solution.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables:**
- x_A = weekly production quantity of Model A (units)
- x_B = weekly production quantity of Model B (units)
- OT = overtime hours used on Process II (hours)

**Objective:**
Maximize total weekly profit = 300·x_A + 450·x_B − (overtime cost per hour)·OT

**Constraints:**
1. Process I (hard equality, exactly 150 hours): 4·x_A + 6·x_B = 150
2. Process II (at least 70 regular hours, overtime allowed): 3·x_A + 2·x_B ≥ 70
3. Process II total hours = regular + overtime: 3·x_A + 2·x_B = 70 + OT
4. Minimum Model A: x_A ≥ 10
5. Minimum Model B (contractual): x_B ≥ 15
6. Non-negativity: x_A, x_B, OT ≥ 0

**Parameters to be confirmed internally (PARKED):**
- Overtime cost per hour for Process II (uniform rate assumed; to be confirmed)
- Upper limit on overtime hours for Process II (if any)
- Whether x_A and x_B must be integers or can be continuous
- Whether there are upper bounds on x_A or x_B beyond process capacities
- Whether there are demand/market limits on sales of Model A or Model B

**Confirmed structure:**
- Process I is a hard equality at exactly 150 hours (no overtime on Process I).
- Process II must run at least 70 hours (regular capacity); hours beyond 70 are overtime at an extra cost deducted from profit.
- The 70-hour figure is regular-time capacity; overtime is additional.
- Minimum 10 units of Model A and minimum 15 units of Model B are hard constraints.
- Overtime cost reduces the objective (it is a cost, not just a feasibility constraint).