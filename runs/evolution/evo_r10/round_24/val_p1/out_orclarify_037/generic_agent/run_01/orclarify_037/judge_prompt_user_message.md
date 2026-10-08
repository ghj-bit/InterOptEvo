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

QUESTION: When you say Process II's weekly production time must be "fully utilized," do you mean the 70 regular hours must be completely used up (i.e., the Process II constraint is binding at exactly 70 hours), or that it simply cannot exceed 70 regular hours and any extra production is allowed via overtime at some cost?

## Turn 1 - User Simulator

It means the 70 regular hours must be completely used up. The Process II constraint is binding at exactly 70 hours.

## Turn 2 - Generic Agent

QUESTION: You mentioned "potential overtime if necessary" — does overtime apply to Process I, Process II, both, or neither?

## Turn 2 - User Simulator

Overtime applies to Process II.

## Turn 3 - Generic Agent

QUESTION: Since Process II must be fully utilized at exactly 70 hours, in what situation would overtime on Process II ever be needed — is overtime actually part of the plan, or was that just a general note and the model should simply use the 70-hour capacity with no overtime?

## Turn 3 - User Simulator

The model should simply use the 70-hour capacity with no overtime.

## Turn 4 - Generic Agent

QUESTION: For Process I, is the 150-hour maximum weekly capacity a hard limit that production cannot exceed, or can it also be exceeded (e.g., via overtime) if needed?

## Turn 4 - User Simulator

The 150-hour capacity for Process I is a hard limit that production cannot exceed.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on how many units of Model B can be produced per week, or is Model B only limited by the Process I and Process II capacities?

## Turn 6 - User Simulator

Model B is only limited by the Process I and Process II capacities.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on how many units of Model A can be produced per week, or is Model A only limited by the Process I and Process II capacities (with the 10-unit minimum as its only lower bound)?

## Turn 7 - User Simulator

Model A is only limited by the Process I and Process II capacities, with the 10-unit minimum as its only lower bound.

## Turn 8 - Generic Agent

QUESTION: Since the production quantities still need internal confirmation on whether they must be whole numbers, should I proceed with the model assuming fractional units are allowed (continuous variables), or would you prefer I wait for that confirmation before finalizing?

## Turn 8 - User Simulator

Please proceed with the model assuming fractional units are allowed (continuous variables).

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables (continuous, non-negative):**
- x_A = weekly units of Model A
- x_B = weekly units of Model B

**Objective:** Maximize total weekly profit = 300·x_A + 450·x_B

**Constraints:**
1. Process I capacity (hard limit): 4·x_A + 6·x_B ≤ 150 hours
2. Process II fully utilized (binding, no overtime): 3·x_A + 2·x_B = 70 hours
3. Minimum Model A production: x_A ≥ 10
4. Non-negativity: x_A ≥ 0, x_B ≥ 0

**Confirmed details:**
- Process II must be used up exactly at 70 hours (equality, not inequality); no overtime.
- Process I is a hard ceiling at 150 hours; no overtime.
- No upper bound on either model beyond the two process capacities.
- Model A's only lower bound is the 10-unit minimum.
- Fractional (continuous) units are allowed.

I will now formulate and solve this linear program.