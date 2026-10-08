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

QUESTION: When Process II runs beyond its 70-hour regular capacity, is the overtime work limited to a maximum number of extra hours per week, or can it be any amount as long as the overtime profit rates (280 yuan for A, 425 yuan for B) apply to the units processed in that overtime?

## Turn 1 - User Simulator

The overtime work is limited to a maximum of 30 extra hours per week.

## Turn 2 - Generic Agent

QUESTION: For the units processed during Process II overtime, is the profit per unit reduced to the overtime rate (280 yuan for A, 425 yuan for B) for those specific units, while units processed within the regular 70 hours keep the full profit (300 yuan for A, 450 yuan for B)?

## Turn 2 - User Simulator

Yes, that is correct. Units processed during Process II overtime earn the reduced overtime profit rates (280 yuan for A, 425 yuan for B), while units processed within the regular 70 hours keep the full profit (300 yuan for A, 450 yuan for B).

## Turn 3 - Generic Agent

QUESTION: The brief says Process I time must be exactly 150 hours per week, which equals its maximum capacity. Is the goal to find a feasible production plan that satisfies all these requirements (profit at least 10,000 yuan, Process I exactly 150 hours, Process II regular time at most 70 hours, overtime at most 30 hours), or is there an additional objective to optimize, such as minimizing total production cost or maximizing total profit?

## Turn 3 - User Simulator

The goal is to find a feasible production plan that satisfies all the requirements: total weekly profit at least 10,000 yuan, Process I exactly 150 hours, Process II regular time at most 70 hours, and overtime at most 30 hours. There is no additional objective to optimize, such as minimizing cost or maximizing profit.

## Turn 4 - Generic Agent

QUESTION: For the units processed during Process II overtime, do they still consume the full regular Process I time per unit (4 hours for A, 6 hours for B) toward the exactly-150-hour Process I requirement, or does overtime affect Process I time as well?

## Turn 4 - User Simulator

The overtime affects only Process II. Units processed during Process II overtime still consume the full regular Process I time per unit (4 hours for A, 6 hours for B) toward the exactly-150-hour Process I requirement.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: When Process II runs overtime, are the overtime hours allocated to specific units (so each unit is either fully processed in regular time or fully in overtime), or can a single unit's Process II time be split between regular and overtime?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the Process II regular capacity of 70 hours, is the constraint that the total regular Process II time (3 hours per A unit plus 2 hours per B unit, for units processed in regular time) must be at most 70 hours, with any remaining units processed in overtime up to the 30-hour overtime limit?

## Turn 7 - User Simulator

Yes, that is correct. The total regular Process II time for units processed in regular time must be at most 70 hours, with any remaining units processed in overtime up to the 30-hour overtime limit.

## Turn 8 - Generic Agent

QUESTION: If a unit is processed during Process II overtime, does it still count toward the total weekly profit at the reduced overtime rate (280 yuan for A, 425 yuan for B), and does the total weekly profit of at least 10,000 yuan include both regular and overtime unit profits combined?

## Turn 8 - User Simulator

Yes, units processed during Process II overtime count toward the total weekly profit at the reduced overtime rate (280 yuan for A, 425 yuan for B), and the total weekly profit of at least 10,000 yuan includes both regular and overtime unit profits combined.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:**
- x_A: number of Model A units produced per week
- x_B: number of Model B units produced per week
- a_reg, b_reg: units of A and B processed in Process II regular time
- a_ot, b_ot: units of A and B processed in Process II overtime
- (a_reg + a_ot = x_A, b_reg + b_ot = x_B)

**Constraints:**
1. Process I exactly 150 hours: 4·x_A + 6·x_B = 150 (overtime does not affect Process I)
2. Process II regular time ≤ 70 hours: 3·a_reg + 2·b_reg ≤ 70
3. Process II overtime time ≤ 30 hours: 3·a_ot + 2·b_ot ≤ 30
4. Total weekly profit ≥ 10,000 yuan: 300·a_reg + 450·b_reg + 280·a_ot + 425·b_ot ≥ 10,000
5. Non-negativity: all variables ≥ 0

**Objective:** Feasibility only — find any production plan satisfying all constraints. No optimization objective.

**Deferred items (not yet confirmed):**
- Whether x_A and x_B must be integers (whole units) or can be fractional.
- Whether a single unit's Process II time can be split between regular and overtime, or each unit must be entirely in one category.

These two items are pending internal confirmation and do not change the structure of the model; they only affect the integrality and splitting assumptions on the variables.