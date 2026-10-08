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

QUESTION: When some units of a model are processed in Process II during overtime, does the overtime premium apply to the entire weekly output of that model, or only to the units that actually exceed the 70-hour regular capacity?

## Turn 1 - User Simulator

The overtime premium applies only to the units that actually exceed the 70-hour regular capacity.

## Turn 2 - Generic Agent

QUESTION: For the units processed in Process II during overtime, is the profit per unit the overtime figure (280 yuan for A, 425 yuan for B) replacing the regular profit, or is it the regular profit plus an additional overtime premium?

## Turn 2 - User Simulator

The overtime figures (280 yuan for A, 425 yuan for B) replace the regular profit for those specific units.

## Turn 3 - Generic Agent

QUESTION: Is the 150 hours for Process I a hard requirement that must be met exactly (so the plan is infeasible if it can't be hit), or is it a target that should be met if possible but the plan can deviate from it?

## Turn 3 - User Simulator

The 150 hours for Process I is a hard requirement that must be met exactly.

## Turn 4 - Generic Agent

QUESTION: What is the goal of the production plan — for example, minimize total production cost, maximize total profit, or something else — given that profit must be at least 10,000 yuan?

## Turn 4 - User Simulator

The goal is to maximize total profit.

## Turn 5 - Generic Agent

QUESTION: Are there any upper limits on how many units of Model A and Model B can be produced per week (e.g., demand caps or machine limits), or can production of each model be any nonnegative amount?

## Turn 5 - User Simulator

There are no upper limits on the number of units of Model A or Model B that can be produced per week.

## Turn 6 - Generic Agent

QUESTION: Can the number of units produced per week for each model be fractional, or must they be whole numbers?

## Turn 6 - User Simulator

The number of units produced per week for each model must be whole numbers.

## Turn 7 - Generic Agent

QUESTION: Is there a limit on how many hours of overtime can be used in Process II per week, or can overtime hours be unlimited as long as the regular 70 hours are used first?

## Turn 7 - User Simulator

The overtime on Process II is limited to 30 hours per week.

## Turn 8 - Generic Agent

QUESTION: When Process II uses overtime hours, is the regular 70-hour capacity always fully used first, or can the plan choose to use fewer than 70 regular hours and shift some units to overtime?

## Turn 8 - User Simulator

The regular 70-hour capacity is always fully used first.

## Turn 9 - Generic Agent

QUESTION: Since the regular 70 hours of Process II must be fully used, is that a hard requirement (the plan is infeasible if it can't be met), or is it simply the rule that regular hours are consumed before overtime, with no obligation to fill all 70 hours?

## Turn 9 - User Simulator

It is simply the rule that regular hours are consumed before overtime, with no obligation to fill all 70 hours.

## Turn 10 - Generic Agent

QUESTION: Is the 10,000 yuan weekly profit a hard minimum (the plan is infeasible if profit falls below it), or is it a target that should be met if possible?

## Turn 10 - User Simulator

The 10,000 yuan weekly profit is a hard minimum.

## Turn 11 - Generic Agent

QUESTION: For the overtime units in Process II, do they still consume Process I time at the same rate (4 hours for A, 6 hours for B) as regular units, or is Process I time different for overtime units?

## Turn 11 - User Simulator

Overtime units in Process II still consume Process I time at the same rate (4 hours for A, 6 hours for B) as regular units.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on how many units can be processed in Process I per week beyond the exact 150-hour requirement, or is the 150 hours the only constraint on Process I?

## Turn 12 - User Simulator

The 150 hours is the only constraint on Process I.

## Turn 13 - Generic Agent

QUESTION: Is there any cost associated with using overtime hours in Process II, or is the only effect of overtime the reduced profit per unit (280 for A, 425 for B)?

## Turn 13 - User Simulator

The only effect of overtime is the reduced profit per unit (280 for A, 425 for B).

## Turn 14 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two microcomputer models, A and B, produced in whole (integer) units per week, with no upper bound on units.
- **Objective:** Maximize total weekly profit.
- **Profit:** Regular units earn 300 yuan (A) and 450 yuan (B). Units processed in Process II during overtime earn 280 yuan (A) and 425 yuan (B) instead — the overtime figure replaces the regular profit for those specific units only.
- **Process I:** 4 hours/unit for A, 6 hours/unit for B. Total Process I time must be **exactly 150 hours** per week (hard requirement). This is the only constraint on Process I.
- **Process II:** 3 hours/unit for A, 2 hours/unit for B. Regular capacity is 70 hours/week; overtime capacity is an additional 30 hours/week (so up to 100 hours total). Regular hours are consumed before overtime, but there is no obligation to fill all 70 regular hours.
- **Overtime units** still consume Process I time at the same rate as regular units.
- **Profit constraint:** Total weekly profit must be **at least 10,000 yuan** (hard minimum).
- **No other costs or constraints** are present.