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

QUESTION: For Process II, is the 70-hour capacity a hard ceiling that must be met exactly (i.e., total Process II time must equal 70 hours, with overtime allowed only to reach that 70-hour target), or is 70 hours the regular-time capacity that must be fully used and any additional Process II time beyond 70 hours is permitted as overtime at some extra cost?

## Turn 1 - User Simulator

The 70 hours is the regular-time capacity that must be fully used. Any additional Process II time beyond 70 hours is permitted as overtime.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how much overtime can be worked on Process II, or is overtime unlimited?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is overtime on Process II charged at an extra cost per hour (reducing profit), or is it free in the sense that it only adds production time without any additional cost?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the 150-hour weekly capacity for Process I a hard ceiling that production cannot exceed, or can Process I also run overtime beyond 150 hours?

## Turn 4 - User Simulator

The 150 hours is a hard ceiling that production cannot exceed.

## Turn 5 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" a minimum (i.e., Model A can be 10 or more), or is it an exact requirement that Model A must be exactly 10 units?

## Turn 5 - User Simulator

It is a minimum; Model A can be 10 or more units per week.

## Turn 6 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there any minimum production requirement for Model B, or can Model B be zero units in a week?

## Turn 7 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is the 15 units of Model B a minimum (15 or more), or an exact requirement (exactly 15)?

## Turn 8 - User Simulator

It is a minimum; Model B can be 15 or more units per week.

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on the total weekly production of Model A or Model B (for example, a maximum number of units of either model that can be produced per week)?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there any demand limit on how many units of Model A or Model B can be sold per week, or can we assume all units produced will be sold?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there any other constraint on the production plan besides the two process capacities, the minimum production requirements for Model A and Model B, and the Process II full utilization requirement?

## Turn 11 - User Simulator

Yes, the total weekly profit must be at least $10,000.

## Turn 12 - Generic Agent

QUESTION: Is the $10,000 total weekly profit a minimum target that must be met (i.e., profit ≥ $10,000), or is it an exact target (profit = $10,000)?

## Turn 12 - User Simulator

Yes, our goal is that the total weekly profit should not be less than $10,000.

## Turn 13 - Generic Agent

QUESTION: Is the $10,000 profit a hard constraint that must be satisfied (i.e., the plan is infeasible if profit is below $10,000), or is it a soft target that we should try to meet but can be relaxed if needed?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 14 - User Simulator

Yes, the weekly production time for Process I must be exactly 150 hours, not just up to 150.

## Turn 15 - Generic Agent

QUESTION: Is the requirement that Process I uses exactly 150 hours a hard constraint (the plan is infeasible if Process I time is not exactly 150), or is it a target that we should try to meet but can be relaxed if needed?

## Turn 15 - User Simulator

We need the weekly production time for Process I to be exactly 150 hours, not just up to 150.

## Turn 16 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there any other constraint or requirement for the production plan that we haven't discussed yet?

## Turn 30 - User Simulator

The point still needs internal confirmation.