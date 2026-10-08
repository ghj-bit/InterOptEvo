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

QUESTION: For Process II, should the model require that regular-time capacity (70 hours) be used up exactly, with any additional production allowed only through overtime that is charged at some overtime rate, or is it acceptable for Process II to simply run at or below 70 hours with no overtime at all?

## Turn 1 - User Simulator

Process II must be fully utilized. If the production plan requires more than 70 hours, overtime is allowed.

## Turn 2 - Generic Agent

QUESTION: When overtime is used on Process II, is there a maximum number of overtime hours allowed per week, or can overtime be unlimited?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For Process I, is the 150-hour weekly capacity a hard ceiling that cannot be exceeded, or can Process I also run overtime if needed?

## Turn 3 - User Simulator

Process I must run for exactly 150 hours per week.

## Turn 4 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" requirement a floor (10 or more is fine), or must Model A be produced at exactly 10 units?

## Turn 4 - User Simulator

It is a floor; 10 or more units of Model A per week is fine.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on how many units of Model B can be produced per week, or is Model B unbounded above (subject only to the process capacities)?

## Turn 6 - User Simulator

There is no upper limit on Model B production per week, other than the process capacities.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on how many units of Model A can be produced per week, or is Model A unbounded above (subject only to the process capacities and the 10-unit floor)?

## Turn 7 - User Simulator

There is no upper limit on Model A production per week, other than the process capacities and the 10-unit floor.

## Turn 8 - Generic Agent

QUESTION: Since Process I must run for exactly 150 hours, if the production plan uses fewer than 150 hours of Process I, should the model allow "idle" time to fill the gap (i.e., the machine runs but produces nothing), or must the 150 hours be fully consumed by actual production of Model A and Model B only?

## Turn 8 - User Simulator

The 150 hours must be fully consumed by actual production of Model A and Model B only.

## Turn 9 - Generic Agent

QUESTION: Since Process II must be fully utilized, if the production plan uses fewer than 70 hours of Process II, should the model allow "idle" time to fill the gap (i.e., the machine runs but produces nothing), or must the 70 hours be fully consumed by actual production of Model A and Model B only?

## Turn 9 - User Simulator

The 70 hours must be fully consumed by actual production of Model A and Model B only.

## Turn 10 - Generic Agent

QUESTION: When overtime is used on Process II, is the overtime charged at a different (higher) hourly cost that reduces profit, or does overtime simply extend capacity at no extra cost?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or business rules I should know about that are not captured in the table or your earlier answers, such as minimum production for Model B, demand limits, or setup requirements?

## Turn 11 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 12 - Generic Agent

QUESTION: Is the "at least 15 units of Model B per week" requirement a floor (15 or more is fine), or must Model B be produced at exactly 15 units?

## Turn 12 - User Simulator

It is a floor; 15 or more units of Model B per week is fine.

## Turn 13 - Generic Agent

QUESTION: Are there any other constraints or business rules I should know about that are not yet captured, such as demand limits, setup requirements, or labor restrictions?

## Turn 13 - User Simulator

Yes, the total weekly profit must be at least $10,000.

## Turn 14 - Generic Agent

QUESTION: Is the $10,000 minimum weekly profit a hard constraint that the plan must satisfy, or is it a target that the model should aim for but can be relaxed if infeasible?

## Turn 14 - User Simulator

It is a hard constraint; the plan must satisfy the $10,000 minimum weekly profit.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or business rules I should know about that are not yet captured in our discussion?

## Turn 15 - User Simulator

No, there are no other constraints or business rules beyond those already discussed.

## Turn 16 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables**
- x_A = weekly units of Model A produced
- x_B = weekly units of Model B produced
- (Overtime on Process II is allowed if needed; the overtime cap and overtime cost are still pending internal confirmation, so I will model overtime as an unbounded, zero-extra-cost extension of Process II capacity unless you later confirm otherwise.)

**Objective**
- Maximize total weekly profit = 300·x_A + 450·x_B

**Constraints**
1. Process I: 4·x_A + 6·x_B = 150 (must run exactly 150 hours, fully consumed by actual production of A and B only — no idle time)
2. Process II: 3·x_A + 2·x_B ≥ 70 (must be fully utilized; if the plan needs more than 70 hours, overtime is allowed)
3. Model A floor: x_A ≥ 10
4. Model B floor: x_B ≥ 15 (contractual)
5. Minimum profit: 300·x_A + 450·x_B ≥ 10,000 (hard constraint)
6. Non-negativity: x_A, x_B ≥ 0
7. No upper bounds on x_A or x_B beyond the process capacities and the floors above.

**Open items (parked, pending internal confirmation)**
- Whether overtime on Process II has a maximum cap.
- Whether overtime on Process II carries an extra cost that reduces profit.
- Whether x_A and x_B must be integers.

I will proceed with the model treating overtime as unbounded and cost-free, and quantities as continuous, unless those items are confirmed otherwise.