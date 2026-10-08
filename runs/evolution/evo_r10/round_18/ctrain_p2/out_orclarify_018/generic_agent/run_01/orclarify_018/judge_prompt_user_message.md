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

QUESTION: The brief says to minimize overtime, but also gives profit per meter and minimum sales — should the objective be to minimize overtime hours (with the 70,000 m and 45,000 m sales as hard constraints), or to maximize profit (with overtime minimized only as a tie-breaker), or to minimize overtime only among plans that meet the minimum sales?

## Turn 1 - User Simulator

The objective is to minimize overtime hours. The minimum sales of 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are hard constraints that must be met. Profit per meter is not part of the objective function.

## Turn 2 - Generic Agent

QUESTION: The brief states weekly production time is 110 hours, but doesn't specify how much of that is regular time versus overtime — what is the regular (non-overtime) weekly production time in hours, so that overtime is the amount by which total production time exceeds regular time?

## Turn 2 - User Simulator

The regular weekly production time is 110 hours. Overtime is any production time beyond those 110 hours.

## Turn 3 - Generic Agent

QUESTION: The factory operates two shifts — does the 110 hours of regular time already include both shifts (i.e., it's the total regular production time available per week), or is 110 hours per shift (so 220 hours total regular time)?

## Turn 3 - User Simulator

The 110 hours is the total regular production time available per week, including both shifts.

## Turn 4 - Generic Agent

QUESTION: The minimum sales require 115,000 meters total, which at 1000 meters per hour needs 115 production hours — 5 hours over the 110 regular hours. Is there any upper limit on how much overtime can be worked per week, or is overtime unlimited (so the plan simply uses exactly 5 overtime hours)?

## Turn 4 - User Simulator

There is an upper limit: overtime should not exceed 10 hours per week.

## Turn 5 - Generic Agent

QUESTION: The production rate is 1000 meters per hour for both fabrics — is this a combined rate (the factory produces 1000 m/h total across both fabrics, so producing both simultaneously shares the 1000 m/h capacity), or does each fabric type have its own 1000 m/h rate (so the factory can produce up to 1000 m/h of each fabric independently)?

## Turn 5 - User Simulator

The 1000 meters per hour is a combined rate. The factory produces 1000 meters per hour total across both fabrics, so producing both simultaneously shares that capacity.

## Turn 6 - Generic Agent

QUESTION: Can the factory produce more than the minimum sales (i.e., produce extra fabric beyond 70,000 m of curtain and 45,000 m of clothing), or must production exactly equal the minimum sales amounts?

## Turn 6 - User Simulator

The factory can produce more than the minimum sales amounts. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are minimums, not exact targets.

## Turn 7 - Generic Agent

QUESTION: Since the objective is to minimize overtime and the minimum sales require 115,000 meters total (115 hours at 1000 m/h), the plan will use exactly 115 hours (5 overtime hours). Is there any reason the factory would want to produce more than the minimums — for example, is there a maximum production capacity per fabric type, or a maximum total production per week, that could bind?

## Turn 7 - User Simulator

There is no maximum production capacity per fabric type or a maximum total production per week that would bind. The only limits are the 110 hours of regular time and the 10-hour overtime cap.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize overtime hours per week.
- **Decision variables:**
  - Production of curtain fabric (meters/week), continuous, non-negative.
  - Production of clothing fabric (meters/week), continuous, non-negative.
  - Overtime hours (hours/week), continuous, non-negative.
- **Constraints:**
  - Minimum sales: curtain fabric ≥ 70,000 m; clothing fabric ≥ 45,000 m (hard constraints).
  - Production capacity: total production (curtain + clothing) ≤ 1000 × (110 + overtime), i.e., the factory produces at a combined rate of 1000 m/h, with 110 regular hours plus up to 10 overtime hours available.
  - Overtime cap: overtime ≤ 10 hours.
- **Notes:**
  - Profit per meter is not part of the objective.
  - Production can exceed the minimum sales; there is no upper bound on production beyond the time-based capacity.
  - The 110 hours is total regular time across both shifts; overtime is any time beyond 110 hours.
  - The 1000 m/h rate is shared across both fabric types (combined capacity).

The model will find the minimum overtime needed to meet the minimum sales, which is 5 hours (115,000 m ÷ 1000 m/h = 115 h; 115 − 110 = 5 h overtime), well within the 10-hour cap.