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

QUESTION: For Process II, should the model allow overtime beyond the 70-hour regular capacity (with an associated overtime cost or rate), or is the 70-hour limit a hard ceiling that must be exactly met with no overtime permitted?

## Turn 1 - User Simulator

The 70-hour limit is not a hard ceiling. We need the model to allow overtime beyond the 70-hour regular capacity for Process II if necessary to meet production requirements.

## Turn 2 - Generic Agent

QUESTION: When Process II runs overtime beyond 70 hours, is there an overtime cost (or a reduced profit rate) that should be subtracted from profit, and if so, what is the overtime rate per hour?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum limit on how many overtime hours Process II can run beyond the 70-hour regular capacity, or can it run unlimited overtime?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: For Model A, is the "at least 10 units per week" a strict minimum that must be met every week, or is it a soft target that can be relaxed if doing so would increase total profit?

## Turn 4 - User Simulator

It is a strict minimum that must be met every week.

## Turn 5 - Generic Agent

QUESTION: Should the weekly production quantities of Model A and Model B be whole numbers (integer units), or can they be treated as continuous values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the 150-hour maximum for Process I a hard ceiling that production cannot exceed, or can Process I also run overtime beyond 150 hours if needed?

## Turn 6 - User Simulator

The 150-hour limit for Process I is a hard ceiling that production cannot exceed.

## Turn 7 - Generic Agent

QUESTION: The brief says Process II's weekly production time must be "fully utilized" — does this mean the model must use at least 70 hours of Process II (i.e., the 70 regular hours are mandatory, with overtime on top if needed), or does it simply mean Process II should be used up to its capacity as a natural result of maximizing profit?

## Turn 7 - User Simulator

The 70 regular hours are mandatory. The model must use at least 70 hours of Process II, with overtime on top if needed.

## Turn 8 - Generic Agent

QUESTION: Are there any minimum production requirements for Model B, or can Model B production be zero if that maximizes profit?

## Turn 8 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 9 - Generic Agent

QUESTION: Can the weekly production quantities of Model A and Model B be treated as continuous values, or must they be whole numbers?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on the total number of units (Model A plus Model B) that can be produced in a week, or is the only constraint on total output the two process capacities?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about that aren't covered in the table or the brief, such as demand limits, raw material constraints, or labor restrictions?

## Turn 11 - User Simulator

Yes, there are two additional requirements:

1. Total weekly profit must be at least $10,000.
2. The weekly production time for Process I must be exactly 150 hours, not just up to 150.

## Turn 12 - Generic Agent

QUESTION: Is the $10,000 minimum weekly profit a hard constraint that must be satisfied, or is it a target that the model should aim for but can be relaxed if infeasible?

## Turn 12 - User Simulator

Yes, the $10,000 minimum weekly profit is a hard constraint that must be satisfied.

## Turn 13 - Generic Agent

QUESTION: Since Process II overtime cost is still pending internal confirmation, should I model overtime as a free extension of Process II capacity (i.e., no additional cost deducted from profit) for now, or would you prefer I leave the overtime cost as a parameter to be filled in later?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the overtime hours on Process II, should I treat them as having zero additional cost (i.e., overtime hours are free) in the model, so that the only effect of overtime is that Process II can exceed 70 hours?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Should the production quantities of Model A and Model B be modeled as continuous (allowing fractional units) or as integers (whole units only)?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is there a maximum number of overtime hours that Process II can run beyond the 70-hour regular capacity, or is overtime unlimited?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Should I treat the production quantities of Model A and Model B as continuous (fractional units allowed) in the model, since the integer question has been deferred?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any upper limit on the number of units of Model A or Model B that can be produced per week, or is the only cap on each model's output the process capacity constraints?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Are there any other business rules, constraints, or requirements I should include in the model that we haven't discussed yet?

## Turn 19 - User Simulator

No, I believe we have covered all the business rules, constraints, and requirements.

## Turn 20 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Objective:** Maximize total weekly profit = 300·A + 450·B, where A and B are the weekly production quantities of Model A and Model B.

**Decision variables:**
- A = weekly units of Model A (continuous, non-negative)
- B = weekly units of Model B (continuous, non-negative)
- OT = overtime hours on Process II (continuous, non-negative)

**Constraints:**

1. **Process I capacity (hard ceiling, exactly 150 hours):**
   4A + 6B = 150

2. **Process II (at least 70 regular hours mandatory, overtime allowed on top):**
   3A + 2B ≥ 70
   (Overtime hours OT = 3A + 2B − 70, with no cost deducted from profit — overtime cost is pending internal confirmation and is treated as zero for now.)

3. **Minimum Model A production (strict):**
   A ≥ 10

4. **Minimum Model B production (contractual, strict):**
   B ≥ 15

5. **Minimum weekly profit (hard constraint):**
   300A + 450B ≥ 10,000

**Notes on deferred items (to be confirmed internally):**
- Overtime cost/rate for Process II (currently modeled as zero cost)
- Maximum overtime hours for Process II (currently modeled as unlimited)
- Whether A and B should be integers (currently modeled as continuous)
- Whether there is a total output cap (currently no cap beyond process capacities)

The model is a linear program. With the Process I constraint binding at exactly 150 hours and the minimums on A and B, the feasible region is well-defined, and the profit-maximizing solution can be found directly.