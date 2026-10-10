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

QUESTION: When you say the total weekly profit must be at least 10,000 yuan, is that a hard minimum constraint that the plan must satisfy, or is it the objective you want to maximize?

## Turn 1 - User Simulator

It is a hard minimum constraint. The plan must achieve at least 10,000 yuan in total weekly profit.

## Turn 2 - Generic Agent

QUESTION: What is the objective of this production plan: are you trying to minimize total weekly production cost, maximize total weekly profit, or simply find any feasible production quantity that satisfies all the stated constraints?

## Turn 2 - User Simulator

The objective is to find any feasible production quantity that satisfies all the stated constraints.

## Turn 3 - Generic Agent

QUESTION: For the overtime profit figures you provided (Model A 280 yuan, Model B 425 yuan), are these the total profit per unit when produced during overtime, or are they the additional profit per unit on top of the regular profit?

## Turn 3 - User Simulator

These are the total profit per unit when produced during overtime.

## Turn 4 - Generic Agent

QUESTION: What is the maximum number of overtime hours available per week for Process II?

## Turn 4 - User Simulator

The maximum overtime hours available per week for Process II is 30 hours.

## Turn 5 - Generic Agent

QUESTION: For the Process I constraint, is the requirement that the total processing time must be exactly 150 hours per week, or is 150 hours the maximum capacity that cannot be exceeded?

## Turn 5 - User Simulator

The requirement is that the total processing time for Process I must be exactly 150 hours per week.

## Turn 6 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model A or Model B, or can each model be produced in any non-negative quantity as long as the process constraints are met?

## Turn 7 - User Simulator

There is no maximum weekly production limit for Model A or Model B. They can be produced in any non-negative quantity as long as the process constraints are met.

## Turn 8 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Find any feasible production quantity that satisfies all stated constraints. (Confirmed)
2. **Decision Variables:** Weekly production quantities for Model A and Model B. (Confirmed)
3. **Variable Domain:** Non-negative quantities. (Confirmed)
4. **Process I Constraint:** Total processing time for Process I must be exactly 150 hours per week. (Confirmed)
   - Model A uses 4 hours/unit, Model B uses 6 hours/unit.
5. **Process II Regular Constraint:** Total regular processing time for Process II must not exceed 70 hours per week. (Confirmed)
   - Model A uses 3 hours/unit, Model B uses 2 hours/unit.
6. **Process II Overtime Constraint:** Maximum overtime hours available per week for Process II is 30 hours. (Confirmed)
7. **Profit Constraint:** Total weekly profit must be at least 10,000 yuan. (Confirmed)
   - Regular profit: Model A 300 yuan/unit, Model B 450 yuan/unit.
   - Overtime profit: Model A 280 yuan/unit, Model B 425 yuan/unit (total profit per unit when produced during overtime). (Confirmed)
8. **Production Limits:** No maximum weekly production limit for Model A or Model B. (Confirmed)

**Open Assumptions:**

1. **Integrality:** It is assumed that production quantities can be fractional (continuous) since the user could not confirm whether whole numbers are required. (Assumed)
2. **Overtime Allocation Logic:** It is assumed that units produced beyond the 70-hour regular capacity in Process II are produced during overtime, and the overtime profit figures apply to those units. The total Process II time (regular + overtime) cannot exceed 70 + 30 = 100 hours. (Assumed)
3. **Profit Calculation:** It is assumed that the total weekly profit is calculated as the sum of regular profit for units produced within regular capacity plus overtime profit for units produced during overtime. (Assumed)