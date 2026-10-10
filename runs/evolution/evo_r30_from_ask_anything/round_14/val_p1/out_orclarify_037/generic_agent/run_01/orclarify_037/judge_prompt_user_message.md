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

QUESTION: Is the 70-hour maximum weekly capacity for Process II a hard ceiling that must not be exceeded, or is it a regular-time limit that can be exceeded through overtime (with overtime hours subject to their own separate maximum)?

## Turn 1 - User Simulator

The 70-hour figure is a regular-time limit. It can be exceeded through overtime. Overtime hours are subject to their own separate maximum, but that specific overtime maximum is not provided in the current request.

## Turn 2 - Generic Agent

QUESTION: What is the maximum number of overtime hours allowed per week for Process II?

## Turn 2 - User Simulator

The specific maximum number of overtime hours allowed per week for Process II still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the 150-hour maximum weekly capacity for Process I a hard ceiling that must not be exceeded, or is it a regular-time limit that can also be exceeded through overtime?

## Turn 3 - User Simulator

The 150-hour capacity for Process I is a hard ceiling that must not be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the requirement that at least 10 units of Model A be produced per week a hard minimum that must be met, or is it a soft target that can be relaxed if doing so would increase total profit?

## Turn 4 - User Simulator

It is a hard minimum that must be met.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the requirement that Process II's weekly production time be "fully utilized" a hard constraint that must be met exactly, or is it a soft target that can be relaxed if doing so would increase total profit?

## Turn 6 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 7 - Generic Agent

QUESTION: Are the profit figures of $300 per unit for Model A and $450 per unit for Model B the correct per-unit values to use in the objective function, or do they represent something else such as a per-batch or per-period total?

## Turn 7 - User Simulator

They are the correct per-unit values to use in the objective function.

## Turn 8 - Generic Agent

QUESTION: Are the processing times of 4 hours per unit for Model A and 6 hours per unit for Model B in Process I the correct per-unit values to use in the Process I capacity constraint?

## Turn 8 - User Simulator

Yes, those are the correct per-unit values to use in the Process I capacity constraint.

## Turn 9 - Generic Agent

QUESTION: Are the processing times of 3 hours per unit for Model A and 2 hours per unit for Model B in Process II the correct per-unit values to use in the Process II utilization constraint?

## Turn 9 - User Simulator

Yes, those are the correct per-unit values to use in the Process II utilization constraint.

## Turn 10 - Generic Agent

QUESTION: Are there any additional requirements or constraints beyond the ones already discussed, such as a maximum production limit for either model, a minimum production requirement for Model B, or any other business rules that should be included in the plan?

## Turn 10 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 11 - Generic Agent

QUESTION: Is the contractual requirement to produce at least 15 units of Model B each week a hard minimum that must be met, or is it a soft target that can be relaxed if doing so would increase total profit?

## Turn 11 - User Simulator

It is a hard minimum that must be met.

## Turn 12 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model A, or can Model A be produced in any quantity up to what the process capacities allow?

## Turn 12 - User Simulator

There is no maximum weekly production limit for Model A beyond what the process capacities allow.

## Turn 13 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model B, or can Model B be produced in any quantity up to what the process capacities allow?

## Turn 13 - User Simulator

There is no maximum weekly production limit for Model B beyond what the process capacities allow.

## Turn 14 - Generic Agent

QUESTION: Are there any other business rules, dependencies, or constraints that should be included in the weekly production plan beyond the ones already discussed?

## Turn 14 - User Simulator

No, there are no other business rules, dependencies, or constraints beyond the ones already discussed.

## Turn 15 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of the weekly production plan for Model A and Model B microcomputers:

**Objective**
- Maximize total weekly profit.
- Profit is $300 per unit of Model A and $450 per unit of Model B (confirmed per-unit values).

**Decision Variables**
- Weekly production quantity of Model A (units).
- Weekly production quantity of Model B (units).
- Weekly overtime hours used in Process II (hours).
- Domain: The integrality of the production quantities (whole units vs. continuous) is still pending internal confirmation and is flagged as an open assumption.

**Constraints**
1. Process I capacity (hard ceiling): 4 hours/unit for Model A and 6 hours/unit for Model B, with a maximum of 150 hours per week. This is a hard ceiling that must not be exceeded.
2. Process II utilization (hard equality): 3 hours/unit for Model A and 2 hours/unit for Model B. The total regular-time hours (70) plus overtime hours must equal the total processing time required. This is a hard constraint that must be met exactly.
3. Process II overtime limit: Overtime hours are subject to a separate maximum, but that specific maximum is not yet confirmed and is flagged as an open assumption.
4. Model A minimum (hard floor): At least 10 units of Model A must be produced per week.
5. Model B minimum (hard floor): At least 15 units of Model B must be produced per week (contractual requirement).
6. No maximum production limits for either model beyond what the process capacities allow.
7. No other business rules, dependencies, or constraints.

**Open Assumptions**
- The maximum number of overtime hours allowed per week for Process II is not yet confirmed.
- Whether the production quantities must be whole numbers (integer) or can be continuous is not yet confirmed.