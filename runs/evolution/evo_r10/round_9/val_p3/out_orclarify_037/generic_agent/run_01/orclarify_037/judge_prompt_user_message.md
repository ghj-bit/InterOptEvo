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

QUESTION: When you say Process II's weekly production time must be "fully utilized," do you mean the total hours used on Process II must be exactly 70 (i.e., the 70-hour capacity is a hard equality that must be met, with overtime allowed only if the other constraints make 70 hours impossible), or do you mean Process II must be used at least up to its 70-hour capacity (i.e., ≥70 hours, with overtime permitted to exceed 70 if needed)?

## Turn 1 - User Simulator

I mean Process II must be used at least up to its 70-hour capacity (i.e., ≥70 hours, with overtime permitted to exceed 70 if needed).

## Turn 2 - Generic Agent

QUESTION: You mentioned overtime is possible for Process II if necessary — is there a maximum overtime limit (in hours) that Process II can exceed its 70-hour capacity, or can it run for any number of hours beyond 70 with no upper bound?

## Turn 2 - User Simulator

There is no maximum overtime limit; Process II can run for any number of hours beyond 70 with no upper bound.

## Turn 3 - Generic Agent

QUESTION: Is Process I's 150-hour weekly capacity a hard upper limit that cannot be exceeded (no overtime allowed for Process I), or can Process I also run overtime beyond 150 hours?

## Turn 3 - User Simulator

Process I's 150-hour weekly capacity is a hard upper limit that cannot be exceeded; no overtime is allowed for Process I.

## Turn 4 - Generic Agent

QUESTION: The requirement is "at least 10 units of Model A per week" — is 10 a hard minimum (i.e., Model A production must be ≥10, with no upper limit on Model A), or is there also a maximum number of Model A units that can be produced per week?

## Turn 4 - User Simulator

10 is a hard minimum; Model A production must be ≥10, with no upper limit on Model A.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional (e.g., 12.5 units)?

## Turn 5 - User Simulator

The production quantities of Model A and Model B are required to be whole numbers (integer units).

## Turn 6 - Generic Agent

QUESTION: Is there any minimum production requirement for Model B (e.g., at least some number of units per week), or can Model B production be zero if that maximizes profit?

## Turn 6 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on the total number of units (Model A + Model B combined) that can be produced per week, or is the only constraint on total output the Process I capacity of 150 hours?

## Turn 7 - User Simulator

There is no upper limit on the total number of units (Model A + Model B combined) other than the Process I capacity of 150 hours.

## Turn 8 - Generic Agent

QUESTION: Since Process II can run overtime with no upper bound, is there any additional cost associated with overtime hours on Process II (e.g., a per-hour overtime premium that reduces profit), or is the profit per unit ($300 for A, $450 for B) already net of any overtime costs?

## Turn 8 - User Simulator

The profit per unit ($300 for A, $450 for B) is already net of any overtime costs.

## Turn 9 - Generic Agent

QUESTION: Is there any other constraint or requirement I should be aware of that isn't already covered — for example, a maximum on Model B production, a minimum total output, or any other business rule that would affect the plan?

## Turn 9 - User Simulator

Yes, the total weekly profit must be at least $10,000.

## Turn 10 - Generic Agent

QUESTION: Is the $10,000 minimum weekly profit a hard constraint (i.e., the plan is infeasible if profit falls below $10,000), or is it a target that should be met if possible but the model should still maximize profit regardless?

## Turn 10 - User Simulator

The $10,000 minimum weekly profit is a hard constraint; the plan is infeasible if profit falls below $10,000.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision Variables:**
- x_A = number of Model A units produced per week (integer, ≥ 0)
- x_B = number of Model B units produced per week (integer, ≥ 0)

**Objective:**
- Maximize total weekly profit: 300·x_A + 450·x_B

**Constraints:**
1. Process I capacity (hard upper limit, no overtime): 4·x_A + 6·x_B ≤ 150
2. Process II minimum utilization (overtime allowed, no upper bound): 3·x_A + 2·x_B ≥ 70
3. Model A minimum: x_A ≥ 10
4. Model B minimum (contractual): x_B ≥ 15
5. Minimum profit (hard constraint): 300·x_A + 450·x_B ≥ 10,000
6. Integrality: x_A and x_B are non-negative integers

**Notes:**
- Process II has no upper bound (overtime unlimited, no additional cost).
- Process I has a strict 150-hour cap with no overtime.
- No upper limits on x_A or x_B beyond what the constraints imply.
- Profit figures are net of all costs including any overtime.