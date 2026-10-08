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

QUESTION: When Process II is fully utilized and overtime may be needed, is the 70-hour capacity a hard limit that must be met exactly (i.e., regular-time usage must equal 70 hours, with any additional hours beyond 70 allowed as overtime), or is 70 hours the regular-time capacity that can be exceeded by overtime up to some maximum, with overtime hours incurring an extra cost?

## Turn 1 - User Simulator

The 70 hours is the regular-time capacity. It is not a hard limit that must be met exactly. We can exceed 70 hours using overtime if necessary. There is no maximum overtime limit, and overtime hours do not incur an extra cost in our planning.

## Turn 2 - Generic Agent

QUESTION: Since overtime is unlimited and free, the "Process II fully utilized" requirement seems to be about using the regular 70 hours. Is the requirement that regular-time usage of Process II must be at least 70 hours (i.e., we must use all regular capacity, with any excess going to overtime), or is it simply that the total Process II time (regular plus overtime) must be at least 70 hours?

## Turn 2 - User Simulator

The requirement is that the total Process II time (regular plus overtime) must be at least 70 hours.

## Turn 3 - Generic Agent

QUESTION: Since overtime is unlimited and free, the "at least 70 hours" requirement on Process II is automatically satisfied by any production plan that uses at least 70 hours of Process II time. Is there any upper limit on total Process II time (regular plus overtime) that we should respect, or is Process II time effectively unbounded?

## Turn 3 - User Simulator

Process II time is effectively unbounded. There is no upper limit on total Process II time (regular plus overtime).

## Turn 4 - Generic Agent

QUESTION: Is the 150-hour capacity for Process I a hard upper limit that cannot be exceeded (no overtime allowed for Process I), or can Process I also use overtime beyond 150 hours?

## Turn 4 - User Simulator

The 150-hour capacity for Process I is a hard upper limit that cannot be exceeded. No overtime is allowed for Process I.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional values?

## Turn 5 - User Simulator

The production quantities of Model A and Model B must be whole numbers (integer units).

## Turn 6 - Generic Agent

QUESTION: Is the "at least 10 units of Model A" a strict lower bound (Model A ≥ 10), and is there any upper limit on how many units of Model A or Model B can be produced per week?

## Turn 6 - User Simulator

Yes, "at least 10 units of Model A" is a strict lower bound (Model A ≥ 10). There is no upper limit on how many units of Model A or Model B can be produced per week.

## Turn 7 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit calculated simply as 300 × (units of Model A) + 450 × (units of Model B), with no other costs, fixed charges, or secondary considerations to account for?

## Turn 7 - User Simulator

Yes, the objective is to maximize total weekly profit calculated simply as 300 × (units of Model A) + 450 × (units of Model B), with no other costs, fixed charges, or secondary considerations to account for.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** x_A = weekly units of Model A, x_B = weekly units of Model B. Both are non-negative integers.
- **Objective:** Maximize total weekly profit = 300·x_A + 450·x_B. No other costs or charges.
- **Constraints:**
  1. Process I (hard limit, no overtime): 4·x_A + 6·x_B ≤ 150 hours.
  2. Process II (regular capacity 70 hours, unlimited free overtime, so effectively unbounded): 3·x_A + 2·x_B ≥ 70 hours.
  3. Minimum Model A production: x_A ≥ 10.
  4. No upper bound on x_A or x_B beyond what the constraints imply.
- **Integrality:** x_A and x_B must be whole numbers.
- **No other constraints, costs, or secondary objectives.**