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

QUESTION: When a unit is produced using overtime in Process II, does it still consume its normal Process I hours (4 for A, 6 for B) toward the 150-hour Process I total, or does overtime production bypass Process I entirely?

## Turn 1 - User Simulator

Overtime production does not bypass Process I. A unit produced using overtime in Process II still consumes its normal Process I hours (4 hours for Model A, 6 hours for Model B) toward the 150-hour Process I total.

## Turn 2 - Generic Agent

QUESTION: Is the 150-hour Process I requirement an exact equality (total Process I time must be exactly 150 hours) or a maximum capacity (total Process I time must not exceed 150 hours)?

## Turn 2 - User Simulator

It is an exact equality. The total Process I time must be exactly 150 hours per week.

## Turn 3 - Generic Agent

QUESTION: Is the 70-hour Process II limit a maximum capacity (regular Process II time must not exceed 70 hours), or is it an exact requirement (regular Process II time must be exactly 70 hours)?

## Turn 3 - User Simulator

It is a maximum capacity. The regular Process II time must not exceed 70 hours per week.

## Turn 4 - Generic Agent

QUESTION: Is the 10,000 yuan weekly profit a minimum requirement (total profit must be at least 10,000 yuan) or an exact target (total profit must be exactly 10,000 yuan)?

## Turn 4 - User Simulator

It is a minimum requirement. The total weekly profit must be at least 10,000 yuan.

## Turn 5 - Generic Agent

QUESTION: Is there a limit on how many units can be produced using overtime in Process II, or is overtime unlimited as long as the regular Process II time stays within 70 hours?

## Turn 5 - User Simulator

There is a limit. The overtime processing for Process II must not exceed 30 hours per week.

## Turn 6 - Generic Agent

QUESTION: Is the 30-hour overtime limit for Process II a maximum capacity (overtime Process II time must not exceed 30 hours) or an exact requirement (overtime Process II time must be exactly 30 hours)?

## Turn 6 - User Simulator

It is a maximum capacity. The overtime Process II time must not exceed 30 hours per week.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for each model (A and B), or is production unlimited as long as the process time constraints are satisfied?

## Turn 7 - User Simulator

There is no maximum weekly production capacity for each model. Production is unlimited as long as the process time constraints are satisfied.

## Turn 8 - Generic Agent

QUESTION: What is the objective of this production plan — are we minimizing total production cost, maximizing profit, or simply finding any feasible production plan that satisfies all the constraints?

## Turn 8 - User Simulator

The objective is to maximize profit.

## Turn 9 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers (integer units), or can they be fractional (continuous) values?

## Turn 9 - User Simulator

The production quantities for Model A and Model B must be whole numbers (integer units).

## Turn 10 - Generic Agent

QUESTION: For units produced using overtime in Process II, do they still consume their normal Process II hours (3 for A, 2 for B) toward the 70-hour regular capacity, or do they only consume overtime hours toward the 30-hour overtime limit?

## Turn 10 - User Simulator

Units produced using overtime in Process II only consume overtime hours toward the 30-hour overtime limit. They do not consume their normal Process II hours toward the 70-hour regular capacity.

## Turn 11 - Generic Agent

QUESTION: When a unit is produced using overtime in Process II, does it consume the same number of overtime hours as its regular Process II hours (3 hours for A, 2 hours for B), or are the overtime hours per unit different?

## Turn 11 - User Simulator

The overtime hours per unit are the same as the regular Process II hours: 3 hours for Model A and 2 hours for Model B.

## Turn 12 - Generic Agent

QUESTION: Can a single model (A or B) have some units produced with regular Process II time and other units produced with overtime Process II time in the same week, or must all units of a given model use the same Process II mode (all regular or all overtime)?

## Turn 12 - User Simulator

A single model can have some units produced with regular Process II time and other units produced with overtime Process II time in the same week.

## Turn 13 - Generic Agent

QUESTION: Is there any additional constraint on the total number of units produced per week (A + B combined), or is the only limit the process time constraints?

## Turn 13 - User Simulator

There is no additional constraint on the total number of units produced per week. The only limits are the process time constraints.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the production planning problem:

**Decision Variables (all non-negative integers):**
- x_A_reg: units of Model A produced with regular Process II
- x_A_ot: units of Model A produced with overtime Process II
- x_B_reg: units of Model B produced with regular Process II
- x_B_ot: units of Model B produced with overtime Process II

**Objective:** Maximize total weekly profit
- 300·x_A_reg + 280·x_A_ot + 450·x_B_reg + 425·x_B_ot

**Constraints:**
1. Process I (exact equality): 4(x_A_reg + x_A_ot) + 6(x_B_reg + x_B_ot) = 150
2. Regular Process II (≤ capacity): 3·x_A_reg + 2·x_B_reg ≤ 70
3. Overtime Process II (≤ capacity): 3·x_A_ot + 2·x_B_ot ≤ 30
4. Minimum profit (≥ requirement): 300·x_A_reg + 280·x_A_ot + 450·x_B_reg + 425·x_B_ot ≥ 10,000
5. All variables are non-negative integers

**Key clarifications confirmed:**
- Overtime units still consume normal Process I hours.
- Overtime units do NOT consume regular Process II hours; they only consume overtime hours.
- Overtime hours per unit equal regular Process II hours (3 for A, 2 for B).
- A model can be split between regular and overtime production in the same week.
- No per-model or total production caps beyond the process time constraints.
- Process I is an exact equality; Process II regular and overtime are upper bounds; profit is a lower bound.