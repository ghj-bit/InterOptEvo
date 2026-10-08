# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U12, U13, U14, U2, U3, U4, U5, U6, U7, U8, U9
I need help creating a production plan for a textile factory where at least 70,000 meters of curtain fabric and 45,000 meters of clothing fabric must be sold per week, while minimizing overtime as much as possible.

The factory produces two types of fabrics: clothing fabric and curtain fabric.

The factory operates two shifts.

Weekly production time is 110 hours.

Production rate for both fabrics: 1000 meters per hour.

Minimum weekly sales of curtain fabric: 70,000 meters.

Profit for curtain fabric: 2.5 yuan per meter.

Minimum weekly sales of clothing fabric: 45,000 meters.

Profit for clothing fabric: 1.5 yuan per meter.

## Problem units
- U1 (context): I need help creating a production plan for a textile factory.
- U2 (data): The factory produces two types of fabrics: clothing fabric and curtain fabric.
- U3 (data): The factory operates two shifts.
- U4 (data): Weekly production time is 110 hours.
- U5 (data): Production rate for both fabrics: 1000 meters per hour.
- U6 (data): Minimum weekly sales of curtain fabric: 70,000 meters.
- U7 (data): Profit for curtain fabric: 2.5 yuan per meter.
- U8 (data): Minimum weekly sales of clothing fabric: 45,000 meters.
- U9 (data): Profit for clothing fabric: 1.5 yuan per meter.
- U10 (constraint): Weekly production time must fully utilize the 110 hours.
- U11 (constraint): Overtime should not exceed 10 hours per week.
- U12 (constraint): At least 70,000 meters of curtain fabric must be sold per week.
- U13 (constraint): At least 45,000 meters of clothing fabric must be sold per week.
- U14 (objective): Minimize overtime as much as possible.

## Hidden slot scoring rules
## H1: unclear_production_time_goal
- Severity: P0
- Severity reason: Without knowing that this is a goal with a specific priority and not a hard equality constraint, the model will incorrectly enforce exactly 110 hours of production time, conflicting with other objectives and missing the preemptive goal-programming structure.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must ask whether the 110-hours utilization is a hard constraint or a soft goal, and/or inquire about its priority relative to the other listed objectives.
- Reference acceptable questions:
  - Is the requirement to fully use 110 hours a strict constraint, or a target that can be over-/under‑achieved?
  - Should the goal of fully utilizing 110 hours be treated as an objective with a certain priority over the other objectives?
- Failure modes:
  - Assuming that weekly production time must equal exactly 110 hours as a rigid constraint.
  - Assuming that fully utilizing 110 hours has higher priority than the overtime-related goals without asking.

## H2: unclear_overtime_limit_goal
- Severity: P0
- Severity reason: Without clarification, the agent may treat the overtime limit as a hard constraint instead of a prioritized goal, leading to a model that cannot correctly trade off overtime against other objectives and misrepresents the real problem structure.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask about the nature of the 10-hour overtime rule (strict constraint vs. soft target) and/or its priority in the overall objective hierarchy.
- Reference acceptable questions:
  - Is the 10-hour overtime limit a strict upper bound, or is it another goal that we try to meet as closely as possible?
  - What is the priority of keeping overtime under 10 hours compared to the other objectives like minimizing overtime?
- Failure modes:
  - Assuming the 10-hour overtime limit is a rigid constraint that cannot be violated under any circumstances.
  - Assuming the overtime limit has equal weight to minimizing overtime without inquiring about preemptive priorities.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the 110 hours the total weekly production time available across both shifts combined, or is it the time available per shift (i.e., 220 hours total per week)?

## Turn 1 - User Simulator

The 110 hours is the total weekly production time available across both shifts combined.

## Turn 2 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1000 m/h, but only 110 hours are available — so the requirements cannot both be met. Which should take priority: meeting the minimum sales targets (allowing overtime to cover the shortfall), or strictly limiting production to 110 hours (accepting that some minimum sales will not be met)?

## Turn 2 - User Simulator

The minimum sales targets must be met. Overtime should be used to cover the shortfall, keeping it under 10 hours per week if possible.

## Turn 3 - Generic Agent

QUESTION: You mentioned "minimizing overtime as much as possible" and "keeping it under 10 hours per week if possible" — should overtime be treated as a hard cap of 10 hours per week (i.e., at most 10 hours of overtime allowed), or as a soft target where overtime beyond 10 hours is permitted but penalized in the objective?

## Turn 3 - User Simulator

Overtime should be treated as a soft target. Overtime beyond 10 hours is permitted but should be minimized as much as possible.

## Turn 4 - Generic Agent

QUESTION: The brief mentions profit per meter for both fabrics, but the stated goal is minimizing overtime. Should the objective be purely minimizing overtime hours, or should it also incorporate profit (for example, maximizing profit subject to overtime being minimized, or a weighted combination of both)?

## Turn 4 - User Simulator

The objective is purely minimizing overtime hours.

## Turn 5 - Generic Agent

QUESTION: Since the minimum sales targets (115,000 m total) require 115 hours but only 110 hours are available, overtime is unavoidable. Is there any upper limit on total overtime hours per week (e.g., a maximum of 10 hours, 20 hours, or no cap at all)?

## Turn 5 - User Simulator

There is no hard upper limit on total overtime hours per week. Overtime beyond 10 hours is permitted, but it should be minimized as much as possible.

## Turn 6 - Generic Agent

QUESTION: The brief mentions two shifts — does the 110 hours of regular time split evenly between the two shifts (55 hours each), or is the shift structure irrelevant to the model as long as total regular time is 110 hours?

## Turn 6 - User Simulator

The shift structure is irrelevant to the model as long as the total regular time is 110 hours.

## Turn 7 - Generic Agent

QUESTION: Can the factory produce more than the minimum sales targets (i.e., produce extra curtain or clothing fabric beyond 70,000 m and 45,000 m respectively), or must production be exactly equal to the minimum sales amounts?

## Turn 7 - User Simulator

Production can be more than the minimum sales targets.

## Turn 8 - Generic Agent

QUESTION: Since the objective is purely minimizing overtime and production can exceed the minimums, producing extra fabric would only add more hours (and thus more overtime) without any benefit. Should I assume the factory will never produce beyond the minimum sales targets, or is there a reason extra production might be desired (e.g., inventory for future weeks)?

## Turn 8 - User Simulator

Assume the factory will never produce beyond the minimum sales targets.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Minimize total overtime hours per week.

**Decision variables:**
- Regular time allocated to curtain fabric (hours)
- Regular time allocated to clothing fabric (hours)
- Overtime time allocated to curtain fabric (hours)
- Overtime time allocated to clothing fabric (hours)

**Parameters:**
- Total regular time available: 110 hours/week
- Production rate: 1,000 meters/hour (same for both fabrics)
- Minimum curtain fabric sales: 70,000 meters/week
- Minimum clothing fabric sales: 45,000 meters/week
- No hard upper limit on overtime hours
- Shift structure is irrelevant; only total regular time matters
- Production will not exceed the minimum sales targets

**Constraints:**
1. Total regular time used (curtain + clothing) ≤ 110 hours
2. Curtain fabric produced ≥ 70,000 meters (i.e., curtain regular time + curtain overtime time ≥ 70 hours)
3. Clothing fabric produced ≥ 45,000 meters (i.e., clothing regular time + clothing overtime time ≥ 45 hours)
4. All time variables ≥ 0

**Key observation:** Total required production is 115,000 m = 115 hours, but only 110 hours of regular time are available, so at least 5 hours of overtime is unavoidable. The model will allocate the 110 regular hours between the two fabrics to minimize total overtime.

**Note:** Profit figures (2.5 yuan/m for curtain, 1.5 yuan/m for clothing) are provided in the brief but do not enter the model since the objective is purely minimizing overtime.