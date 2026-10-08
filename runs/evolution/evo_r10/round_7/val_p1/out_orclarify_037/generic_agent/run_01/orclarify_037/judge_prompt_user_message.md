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

QUESTION: When you say the weekly production time for Process II must be "fully utilized," do you mean the total Process II hours used must be exactly 70 (so any unused time is forbidden), or at least 70 (so overtime beyond 70 is allowed but going below 70 is not)?

## Turn 1 - User Simulator

It means at least 70 hours. We must use the full 70-hour capacity, but if necessary, we can go beyond 70 hours with overtime.

## Turn 2 - Generic Agent

QUESTION: For Process I, is the 150-hour maximum a hard cap that cannot be exceeded (no overtime allowed), or can Process I also run overtime beyond 150 hours?

## Turn 2 - User Simulator

The 150 hours for Process I is a hard cap. It cannot be exceeded; no overtime is allowed for Process I.

## Turn 3 - Generic Agent

QUESTION: If Process II runs overtime beyond 70 hours, is there a maximum limit on how many overtime hours are allowed, or can it run for any number of hours beyond 70?

## Turn 3 - User Simulator

There is no maximum limit on overtime hours for Process II. It can run for any number of hours beyond 70 if necessary.

## Turn 4 - Generic Agent

QUESTION: Is there any cost associated with the overtime hours on Process II that should be subtracted from profit, or is the overtime free (i.e., the per-unit profits of $300 for Model A and $450 for Model B remain unchanged regardless of how much overtime is used)?

## Turn 4 - User Simulator

The overtime is free. The per-unit profits of $300 for Model A and $450 for Model B remain unchanged regardless of how much overtime is used on Process II.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 5 - User Simulator

The weekly production quantities must be whole numbers.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on how many units of Model B can be produced per week, or is Model B unbounded above (subject only to the Process I and Process II constraints)?

## Turn 6 - User Simulator

There is no upper limit on the number of units of Model B that can be produced per week, other than the Process I and Process II constraints.

## Turn 7 - Generic Agent

QUESTION: Is there any minimum production requirement for Model B, or can the weekly production of Model B be zero?

## Turn 7 - User Simulator

There is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the number of units of Model A that can be produced per week, or is Model A unbounded above (subject only to the Process I and Process II constraints and the minimum of 10)?

## Turn 8 - User Simulator

There is no upper limit on the number of units of Model A that can be produced per week, other than the Process I and Process II constraints and the minimum of 10 units.

## Turn 9 - Generic Agent

QUESTION: Is there any demand limit on how many units of either model can be sold per week, or can the factory produce and sell any quantity up to the production constraints?

## Turn 9 - User Simulator

There is no demand limit. The factory can produce and sell any quantity up to the production constraints.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about, such as labor limits, raw material limits, or minimum/maximum production for either model beyond what we've already discussed?

## Turn 10 - User Simulator

No, there are no other constraints or requirements beyond what we have already discussed.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables:**
- x_A = number of Model A units produced per week (integer, ≥ 0)
- x_B = number of Model B units produced per week (integer, ≥ 0)

**Objective:**
- Maximize total weekly profit = 300·x_A + 450·x_B

**Constraints:**
1. Process I capacity (hard cap, no overtime): 4·x_A + 6·x_B ≤ 150
2. Process II minimum utilization (overtime allowed, no upper bound): 3·x_A + 2·x_B ≥ 70
3. Minimum Model A production: x_A ≥ 10
4. Minimum Model B production (contractual): x_B ≥ 15
5. Integrality: x_A and x_B must be non-negative integers

**Confirmed details:**
- Process I: 150 hours is a strict upper bound; no overtime permitted.
- Process II: must use at least 70 hours; overtime beyond 70 is permitted with no upper limit and no additional cost.
- Per-unit profits ($300 for A, $450 for B) are constant regardless of overtime usage.
- No demand limits, no raw material limits, no labor limits, and no other constraints.
- No upper bounds on production quantities beyond the process constraints.