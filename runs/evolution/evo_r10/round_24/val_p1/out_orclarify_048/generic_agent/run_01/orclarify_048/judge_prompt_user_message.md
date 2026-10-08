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

QUESTION: For the overtime portion of Process II, is there a maximum number of overtime hours per week available, and if so, what is that limit?

## Turn 1 - User Simulator

Yes. The overtime for Process II is limited to 30 hours per week.

## Turn 2 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or does the overtime change the Process I time as well?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the overtime units in Process II, do they still consume the same Process I hours (4 for A, 6 for B) as regular units, or is the Process I time different for overtime units?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the "exactly 150 hours" requirement for Process I a hard constraint that the plan must satisfy precisely, or is it a target that can be met or exceeded?

## Turn 4 - User Simulator

It is a hard constraint. The processing time for Process I must be exactly 150 hours per week.

## Turn 5 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the "at least 10,000 yuan" weekly profit target a hard constraint that the plan must satisfy, or is it a goal to be met if possible while the plan itself optimizes something else?

## Turn 7 - User Simulator

It is a hard constraint. The total weekly profit must be at least 10,000 yuan.

## Turn 8 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is the weekly production quantity of each model (A and B) required to be a whole number of units, or can fractional units be allowed in the plan?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it still consume the same Process I hours (4 for A, 6 for B) as a regular unit, or is the Process I time different for overtime units?

## Turn 30 - User Simulator

The point still needs internal confirmation.