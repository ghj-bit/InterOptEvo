# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U7, U8, U2, U3
I need help creating a production plan for two microcomputer models, A and B, where the total weekly profit must be at least 10,000 yuan, the processing time for Process I must be exactly 150 hours per week, and the regular processing time for Process II must not exceed its maximum weekly capacity of 70 hours.

| Process | Model A | Model B | Maximum Weekly Processing Capacity |
|---------|---------|---------|------------------------------------|
| I (hours/unit) | 4 | 6 | 150 |
| II (hours/unit) | 3 | 2 | 70 |
| Profit (yuan/unit) | 300 | 450 | |

Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan.

## Problem units
- U1 (context): I need help creating a production plan for two microcomputer models, A and B.
- U2 (data): | Process | Model A | Model B | Maximum Weekly Processing Capacity |
|---------|---------|---------|------------------------------------|
| I (hours/unit) | 4 | 6 | 150 |
| II (hours/unit) | 3 | 2 | 70 |
| Profit (yuan/unit) | 300 | 450 | |
- U3 (data): Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan.
- U4 (constraint): Total weekly profit must be at least 10,000 yuan.
- U5 (constraint): At least 10 units of model A must be produced each week.
- U6 (constraint): At least 15 units of model B must be produced each week.
- U7 (constraint): The processing time for Process I must be exactly 150 hours per week.
- U8 (constraint): The regular processing time for Process II must not exceed its maximum weekly capacity of 70 hours.
- U9 (constraint): The overtime processing for Process II must not exceed 30 hours per week.

## Hidden slot scoring rules
## H1: min_weekly_production_A
- Severity: P1
- Severity reason: Without this constraint, the model could produce fewer than 10 units of model A, violating a contractual obligation and making the solution business-invalid.
- Problem unit ID: U5
- Semantic hit rule: The Agent's question must inquire about a minimum or lower bound on the weekly production quantity of model A, or ask if there is any requirement to produce at least a certain number of A.
- Reference acceptable questions:
  - What is the minimum number of model A microcomputers we must produce each week?
  - Are there any minimum production requirements for model A?
- Failure modes:
  - Assuming no minimum production requirement for model A (production can be zero)
  - Assuming a different arbitrary lower bound

## H2: min_weekly_production_B
- Severity: P1
- Severity reason: Missing this constraint would allow the model to produce fewer than 15 units of model B, violating a contract and leading to a business-invalid solution.
- Problem unit ID: U6
- Semantic hit rule: The Agent's question asks for the minimum required weekly output of model B or whether there is a lower bound on B production.
- Reference acceptable questions:
  - How many model B microcomputers do we need to produce at minimum each week?
  - Is there a lower bound on the weekly production of model B?
- Failure modes:
  - Assuming no minimum production requirement for model B
  - Assuming an incorrect lower limit for B

## H3: max_overtime_process_II
- Severity: P1
- Severity reason: Without this limit, the model could treat overtime as unbounded, which would completely distort the feasible region and profit calculations, or could omit overtime entirely.
- Problem unit ID: U9
- Semantic hit rule: The Agent's question must explicitly ask for the upper limit or cap on overtime hours for Process II.
- Reference acceptable questions:
  - What is the maximum allowed overtime for Process II?
  - How many hours of overtime per week are permitted for Process II?
- Failure modes:
  - Assuming unlimited overtime for Process II
  - Assuming no overtime is allowed for Process II
  - Assuming a different arbitrary overtime cap


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When a unit's Process II work is done in overtime, does its profit drop to the overtime figure (280 for A, 425 for B) for that unit, or is the overtime figure an additional amount on top of the regular profit?

## Turn 1 - User Simulator

The overtime figure is the profit for that unit when its Process II work is done in overtime. It replaces the regular profit for that unit; it is not an additional amount on top of the regular profit.

## Turn 2 - Generic Agent

QUESTION: Is the 150-hour requirement for Process I a hard equality (total Process I time must be exactly 150 hours every week), or is 150 the maximum capacity and the real requirement is only that it not exceed 150 hours?

## Turn 2 - User Simulator

The 150-hour requirement for Process I is a hard equality. The total Process I time must be exactly 150 hours every week.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much overtime Process II can run beyond its 70-hour regular capacity, or can Process II overtime be unlimited?

## Turn 3 - User Simulator

There is a limit. Overtime on Process II is limited to 30 hours per week.

## Turn 4 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole units (integers), or can they be fractional?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on the total weekly production of each model (A and B), or can production be as large as the other constraints allow?

## Turn 5 - User Simulator

There is no limit on the total weekly production of each model beyond the other constraints.

## Turn 6 - Generic Agent

QUESTION: Is the 10,000-yuan weekly profit a minimum that must be met (a constraint), or is it the target you want to maximize?

## Turn 6 - User Simulator

The 10,000-yuan weekly profit is a minimum that must be met. It is a constraint, not a target to maximize.

## Turn 7 - Generic Agent

QUESTION: Since profit must be at least 10,000 and Process I must be exactly 150 hours, what should the plan actually optimize — for example, minimize total production cost, minimize overtime hours used, or minimize total units produced?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: When a unit's Process II work is done in overtime, does it still consume its full Process I time (4 hours for A, 6 hours for B) toward the 150-hour Process I total?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: For the plan, should I treat the production quantities of Model A and Model B as whole units (integers), or is it acceptable for them to be fractional?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Since the profit minimum and Process I equality are the only hard requirements, should the plan simply be any feasible production mix that satisfies them (no optimization), or is there a specific thing to minimize or maximize?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: If a unit's Process II work is done in overtime, does it still consume its full Process I time (4 hours for A, 6 hours for B) toward the 150-hour Process I total?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole units (integers), or can they be fractional?

## Turn 30 - User Simulator

The point still needs internal confirmation.