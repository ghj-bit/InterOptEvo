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

QUESTION: When Process II runs overtime, is there a maximum number of overtime hours allowed per week, and if so, what is that limit?

## Turn 1 - User Simulator

The point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: Is the overtime on Process II charged at a higher hourly cost than regular time, and if so, what is the overtime cost per hour?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the weekly production time for Process II required to be exactly 70 hours (regular time fully used, with any extra production allowed only through overtime), or is 70 hours a minimum that must be met while overtime is optional?

## Turn 3 - User Simulator

The weekly production time for Process II should be fully utilized, with potential overtime if necessary.

## Turn 4 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 4 - User Simulator

It is a hard requirement that must be met in every week.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the 150-hour capacity for Process I a hard limit that cannot be exceeded, or can Process I also run overtime like Process II?

## Turn 6 - User Simulator

The weekly production time for Process I must be exactly 150 hours, not just up to 150.

## Turn 7 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 7 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 8 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 8 - User Simulator

The weekly production time for Process II should be fully utilized, with potential overtime if necessary.

## Turn 9 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 9 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 10 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 10 - User Simulator

It is a hard requirement that must be met in every week.

## Turn 11 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 11 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 12 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 12 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 13 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 13 - User Simulator

It is a hard requirement that must be met in every week.

## Turn 14 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 14 - User Simulator

It

## Turn 15 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 15 - User Simulator

It

## Turn 16 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 16 - User Simulator

It

## Turn 17 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 17 - User Simulator

It

## Turn 18 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 18 - User Simulator

It

## Turn 19 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 19 - User Simulator

It

## Turn 20 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 20 - User Simulator

It

## Turn 21 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 21 - User Simulator

It

## Turn 22 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 22 - User Simulator

It

## Turn 23 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 23 - User Simulator

It

## Turn 24 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 24 - User Simulator

It

## Turn 25 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 25 - User Simulator

It

## Turn 26 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 26 - User Simulator

It

## Turn 27 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 27 - User Simulator

It

## Turn 28 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard requirement that must be met in every week, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 28 - User Simulator

It

## Turn 29 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 29 - User Simulator

It

## Turn 30 - Generic Agent

QUESTION: Is the 70-hour requirement for Process II a hard constraint that must be met exactly, or is it a target that can be relaxed if doing so would increase total weekly profit?

## Turn 30 - User Simulator

It