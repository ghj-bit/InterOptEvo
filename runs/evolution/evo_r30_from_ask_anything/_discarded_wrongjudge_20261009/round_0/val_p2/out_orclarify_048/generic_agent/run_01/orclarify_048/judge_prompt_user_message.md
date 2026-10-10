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

QUESTION: What is the maximum number of units of Model A that can be produced per week

## Turn 1 - User Simulator

I don't have a stated maximum production limit for Model A in the current request. The only constraint I can confirm for Model A is the minimum of at least 10 units per week.

## Turn 2 - Generic Agent

QUESTION: What is the minimum number of units of Model B

## Turn 2 - User Simulator

At least 15 units of Model B must be produced each week.

## Turn 3 - Generic Agent

QUESTION: Is the "exactly 150 hours" requirement for Process

## Turn 3 - User Simulator

Yes, the processing time for Process I must be exactly 150 hours per week.

## Turn 4 - Generic Agent

QUESTION: Can production in Process II exceed the 70-hour regular capacity

## Turn 4 - User Simulator

Yes, production in Process II can exceed the 70-hour regular capacity through overtime, but the overtime is limited to 30 hours per week.

## Turn 5 - Generic Agent

QUESTION: Is the 30-hour overtime limit for Process II

## Turn 5 - User Simulator

Yes, the overtime processing for Process II must not exceed 30 hours per week.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints

## Turn 6 - User Simulator

Yes, there are two minimum production requirements:
- At least 10 units of Model A must be produced each week.
- At least 15 units of Model B must be produced each week.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Decision variables: weekly production quantities of Model A (A) and Model B (B), assumed to be non-negative integers.
- Objective: Maximize total weekly profit.
- Profit structure:
  - Regular Process II capacity is 70 hours.
  - Overtime in Process II is allowed up to 30 hours per week.
  - If total Process II time exceeds 70 hours, the units produced during the overtime portion earn reduced profit: Model A 280 yuan/unit, Model B 425 yuan/unit.
  - Units produced within the first 70 hours of Process II earn regular profit: Model A 300 yuan/unit, Model B 450 yuan/unit.
- Constraints:
  - Process I time must be exactly 150 hours: 4A + 6B = 150.
  - Process II regular time cannot exceed 70 hours: 3A + 2B ≤ 70 + overtime, where overtime ≤ 30, so total Process II time ≤ 100 hours.
  - Minimum production: A ≥ 10, B ≥ 15.
  - Total weekly profit must be at least 10,000 yuan.

The plan will determine the optimal integer values of A and B that satisfy all constraints and maximize profit, accounting for the split between regular and overtime profit rates in Process II.