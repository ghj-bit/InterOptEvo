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

QUESTION: When you say Process II's weekly production time must be "fully utilized," do you mean the total time spent on Process II must be exactly 70 hours (i.e., 3A + 2B = 70), or at least 70 hours (i.e., 3A + 2B ≥ 70, with overtime allowed beyond 70)?

## Turn 1 - User Simulator

It means at least 70 hours, with overtime allowed beyond 70.

## Turn 2 - Generic Agent

QUESTION: You mentioned "potential overtime if necessary" — is overtime allowed on both Process I and Process II, or only on Process II?

## Turn 2 - User Simulator

Overtime is only allowed on Process II.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum limit on how many overtime hours can be used on Process II, or can it exceed 70 hours without bound?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the overtime cap on Process II is still being confirmed internally, should I model Process II as having no upper bound on overtime (i.e., 3A + 2B ≥ 70 with no ceiling), or would you prefer I leave a placeholder parameter for the overtime cap so you can fill in the number once it's confirmed?

## Turn 4 - User Simulator

Please leave a placeholder parameter for the overtime cap so I can fill in the number once it's confirmed.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum limit on how many units of Model B can be produced per week, or is Model B production unbounded (subject only to the process constraints)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the Model B cap is still being confirmed, should I leave a placeholder parameter for the maximum weekly units of Model B (with the constraint B ≤ that parameter), or should I model Model B as unbounded for now?

## Turn 6 - User Simulator

Please leave a placeholder parameter for the maximum weekly units of Model B.

## Turn 7 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since integrality is still being confirmed, should I model the production quantities as continuous (allowing fractional units) for now, or as integer variables?

## Turn 8 - User Simulator

Please model the production quantities as integer variables.

## Turn 9 - Generic Agent

QUESTION: Is there a minimum production requirement for Model B per week, or is the only minimum constraint the 10 units of Model A?

## Turn 9 - User Simulator

Yes, there is a minimum production requirement for Model B: at least 15 units per week.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum limit on how many units of Model A can be produced per week, or is Model A production unbounded (subject only to the process constraints)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Since the Model A cap is still being confirmed, should I leave a placeholder parameter for the maximum weekly units of Model A (with the constraint A ≤ that parameter), or should I model Model A as unbounded for now?

## Turn 11 - User Simulator

Please leave a placeholder parameter for the maximum weekly units of Model A.

## Turn 12 - Generic Agent

QUESTION: Is there any additional constraint on Process I beyond the 150-hour maximum capacity, such as a minimum utilization requirement?

## Turn 12 - User Simulator

Yes, the weekly production time for Process I must be exactly 150 hours.

## Turn 13 - Generic Agent

QUESTION: Is there any cost associated with overtime hours on Process II that should be subtracted from the profit in the objective function, or is the profit per unit simply $300 for Model A and $450 for Model B regardless of whether overtime is used?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the overtime cost is still being confirmed, should I leave a placeholder parameter for the overtime cost per hour on Process II (to be subtracted from total profit in the objective), or should I model the objective as simply 300A + 450B with no overtime cost deduction for now?

## Turn 14 - User Simulator

Please leave a placeholder parameter for the overtime cost per hour on Process II.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as labor availability, raw material limits, or demand caps, that would affect the weekly production plan?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Since other potential constraints are still being confirmed, should I leave a placeholder section in the model for additional constraints (such as labor availability, raw material limits, or demand caps) that you can fill in once they're confirmed, or should I proceed with only the constraints we've discussed so far?

## Turn 16 - User Simulator

Please leave a placeholder section in the model for additional constraints.

## Turn 17 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision Variables:**
- A = number of units of Model A produced per week (integer)
- B = number of units of Model B produced per week (integer)

**Objective:**
- Maximize total weekly profit: 300A + 450B − (overtime_cost_per_hour × overtime_hours_on_Process_II)
- Where overtime_hours_on_Process_II = max(0, 3A + 2B − 70)
- Placeholder parameter: `overtime_cost_per_hour` (to be filled in once confirmed)

**Constraints:**
1. Process I must be exactly fully utilized: 4A + 6B = 150
2. Process II must be at least fully utilized: 3A + 2B ≥ 70
3. Process II overtime cap: 3A + 2B ≤ 70 + `overtime_cap_hours` (placeholder parameter, to be filled in once confirmed)
4. Minimum Model A production: A ≥ 10
5. Minimum Model B production: B ≥ 15
6. Maximum Model A production: A ≤ `max_A` (placeholder parameter, to be filled in once confirmed)
7. Maximum Model B production: B ≤ `max_B` (placeholder parameter, to be filled in once confirmed)
8. Placeholder section for additional constraints (labor availability, raw material limits, demand caps, etc.) to be filled in once confirmed

**Parameters (given):**
- Process I: 4 hrs/unit for A, 6 hrs/unit for B, exactly 150 hrs/week
- Process II: 3 hrs/unit for A, 2 hrs/unit for B, at least 70 hrs/week, overtime allowed only on Process II
- Profit: $300/unit for A, $450/unit for B

**Variables are integer (whole units).**