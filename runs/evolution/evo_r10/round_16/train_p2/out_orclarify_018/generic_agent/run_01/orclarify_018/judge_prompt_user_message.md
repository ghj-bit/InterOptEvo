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

QUESTION: The brief says to minimize overtime, but it doesn't define what overtime is or how it relates to the 110 weekly production hours — is the 110 hours the regular (non-overtime) capacity, with any production beyond it counted as overtime to be minimized, or is 110 hours the total available time including overtime?

## Turn 1 - User Simulator

The 110 hours is the regular (non-overtime) capacity. Any production time beyond those 110 hours is counted as overtime, which we want to minimize.

## Turn 2 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1000 m/h, which already exceeds the 110 regular hours — so overtime is unavoidable. Is there any upper limit on how much overtime can be used per week, or is overtime unlimited and we simply minimize its amount?

## Turn 2 - User Simulator

There is an upper limit: overtime should not exceed 10 hours per week.

## Turn 3 - Generic Agent

QUESTION: The brief mentions two shifts — does the 110 regular hours already include both shifts (i.e., it's the total regular capacity across the week), or is 110 hours per shift, and does the number of shifts impose any additional constraint on the production plan?

## Turn 3 - User Simulator

The 110 hours is the total regular capacity across the week, including both shifts. The number of shifts does not impose any additional constraint on the production plan.

## Turn 4 - Generic Agent

QUESTION: The brief says at least 70,000 m of curtain and 45,000 m of clothing "must be sold" — is production allowed to exceed these minimums (with the extra units also sold), or must production be exactly equal to the minimum sales amounts?

## Turn 4 - User Simulator

Production is allowed to exceed these minimums. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are minimum weekly sales requirements, not exact targets.

## Turn 5 - Generic Agent

QUESTION: The brief lists profit per meter for both fabrics, but the stated goal is to minimize overtime — is profit part of the objective at all (for example, maximize profit subject to minimizing overtime, or a weighted combination), or is profit just background information and the sole objective is to minimize overtime hours?

## Turn 5 - User Simulator

Profit is just background information. The sole objective is to minimize overtime hours.

## Turn 6 - Generic Agent

QUESTION: Since production can exceed the minimums and overtime is capped at 10 hours (so total capacity is at most 120 hours = 120,000 m), is there any limit on how much extra fabric beyond the minimums can be produced and sold, or is the only upper bound the 120 hours of total available time?

## Turn 6 - User Simulator

The only upper bound is the 120 hours of total available time (110 regular + 10 overtime). There are no other limits on how much extra fabric can be produced and sold beyond that capacity.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Weekly production (and sales) of curtain fabric (meters) and clothing fabric (meters), plus overtime hours used.
- **Capacity:** 110 regular hours per week (total across both shifts; shifts impose no extra constraint). Overtime may be added, capped at 10 hours, so total available time ≤ 120 hours.
- **Production rate:** 1000 meters per hour for both fabrics (shared capacity).
- **Minimum sales requirements:** curtain fabric ≥ 70,000 m/week; clothing fabric ≥ 45,000 m/week. Production may exceed these minimums.
- **Upper bound on production:** only the total time capacity (≤ 120 hours → ≤ 120,000 m total across both fabrics). No other limits.
- **Objective:** Minimize overtime hours used. Profit figures (2.5 yuan/m curtain, 1.5 yuan/m clothing) are background information only and do not enter the objective.
- **Feasibility note:** The minimums alone require 115,000 m = 115 hours, so at least 5 hours of overtime is unavoidable; the model will find the minimum overtime consistent with meeting the minimums and the capacity cap.