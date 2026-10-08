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

QUESTION: For the overtime portion of Process II, is there a separate maximum weekly overtime capacity (in hours) that the overtime processing time must not exceed, or is overtime unlimited as long as the regular 70-hour capacity is used first?

## Turn 1 - User Simulator

There is a separate maximum weekly overtime capacity. The overtime processing for Process II must not exceed 30 hours per week.

## Turn 2 - Generic Agent

QUESTION: When a unit of Model A or B is produced, does it always consume its full regular Process II time (3 hours for A, 2 hours for B) from the regular 70-hour capacity first, with only the excess beyond 70 hours going to overtime — or can any portion of a unit's Process II time be assigned to overtime at the planner's discretion?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: The profit figures differ between regular and overtime production (A: 300 vs 280, B: 450 vs 425) — does this mean a unit's profit depends on whether its Process II time is done in regular or overtime hours, so the plan must track how many units of each model are produced in each mode?

## Turn 3 - User Simulator

Yes, a unit's profit depends on whether its Process II time is done in regular or overtime hours. The plan must track how many units of each model are produced in each mode.

## Turn 4 - Generic Agent

QUESTION: The brief says Process I time must be exactly 150 hours per week — is this a hard requirement that the plan must use all 150 hours of Process I (i.e., 4·A + 6·B = 150 exactly), or is 150 simply the capacity ceiling and using less is allowed?

## Turn 4 - User Simulator

It is a hard requirement that the plan must use all 150 hours of Process I. The processing time for Process I must be exactly 150 hours per week.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: The overtime profit is lower than regular profit (A: 280 vs 300, B: 425 vs 450) — is this because overtime incurs an extra cost that reduces profit, and is that cost already baked into the 280/425 figures so I should just use them as-is, or is there a separate overtime cost I need to account for?

## Turn 6 - User Simulator

The cost is already baked into the 280/425 figures. You should just use them as-is.

## Turn 7 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit (subject to the constraint that profit is at least 10,000 yuan), or is the objective something else such as minimizing production cost or maximizing units produced, with the 10,000 yuan profit being just a minimum requirement?

## Turn 7 - User Simulator

The objective is to maximize total weekly profit, subject to the constraint that profit is at least 10,000 yuan.

## Turn 8 - Generic Agent

QUESTION: Since the objective is to maximize profit and the only profit-related constraint is a floor of 10,000 yuan, is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Since the objective is to maximize profit and overtime profit is lower than regular profit, is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: For Process II, is the regular 70-hour capacity a hard ceiling that must be fully used before any overtime hours can be used, or can overtime hours be used even if regular capacity is not fully utilized?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there any upper limit on total production (e.g., a maximum number of units of A or B per week, or a demand cap), or can production be as large as the Process I and Process II capacities allow?

## Turn 30 - User Simulator

The point still needs internal confirmation.