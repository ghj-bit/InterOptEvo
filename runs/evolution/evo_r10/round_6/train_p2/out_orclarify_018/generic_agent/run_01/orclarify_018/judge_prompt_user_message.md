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

QUESTION: Is the 110 hours the total available production time per week (i.e., the maximum), and is overtime any production beyond this 110 hours that you want to minimize?

## Turn 1 - User Simulator

Yes, the 110 hours is the total regular production time available per week. Overtime is any production beyond these 110 hours, and we want to minimize it.

## Turn 2 - Generic Agent

QUESTION: Is the 1000 meters per hour production rate the same for both fabrics regardless of which shift is running, and can the two fabrics be produced in the same hour (i.e., is the 1000 m/h a shared capacity that must be split between them)?

## Turn 2 - User Simulator

Yes, the 1000 meters per hour rate is the same for both fabrics on both shifts. The 1000 m/h is a shared capacity that must be split between the two fabrics.

## Turn 3 - Generic Agent

QUESTION: Do the minimum sales requirements (70,000 m curtain, 45,000 m clothing) have to be met exactly by the production within the week, or can you produce more than the minimum and sell the extra (with the extra also earning profit)?

## Turn 3 - User Simulator

The minimum sales requirements are minimums, not exact targets. We can produce and sell more than the minimums, and the extra production also earns profit.

## Turn 4 - Generic Agent

QUESTION: Since producing more than the minimums earns profit, is there any upper limit on how much of each fabric can be produced or sold per week (e.g., a maximum demand or a maximum production capacity beyond the 110 regular hours plus overtime)?

## Turn 4 - User Simulator

There is no upper limit on production or sales beyond the available production time (110 regular hours plus overtime).

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how much overtime can be used per week, or is overtime unlimited as long as it is minimized?

## Turn 5 - User Simulator

There is a limit: overtime should not exceed 10 hours per week.

## Turn 6 - Generic Agent

QUESTION: Is the objective to minimize overtime only, or is it to maximize profit with overtime minimized as a secondary goal (i.e., lexicographic: first maximize profit, then among profit-maximizing plans minimize overtime)?

## Turn 6 - User Simulator

The objective is to minimize overtime as much as possible.

## Turn 7 - Generic Agent

QUESTION: Is the 10-hour overtime limit a hard cap (overtime must be ≤ 10 hours), or is it a soft target that can be exceeded if needed to meet the minimum sales?

## Turn 7 - User Simulator

It is a hard cap: overtime must not exceed 10 hours per week.

## Turn 8 - Generic Agent

QUESTION: Is the 110 regular hours a hard cap on regular production time (i.e., you cannot use more than 110 regular hours, and any production beyond 110 hours counts as overtime), or is 110 hours just the baseline and you could also choose to use fewer regular hours?

## Turn 8 - User Simulator

The 110 hours is the total regular production time available per week. We aim to fully use these 110 hours. Any production beyond 110 hours counts as overtime.

## Turn 9 - Generic Agent

QUESTION: Since you aim to fully use the 110 regular hours and overtime is minimized, is the model's decision simply how to split the 110 regular hours (plus up to 10 overtime hours) between curtain and clothing fabric to meet the minimums, with overtime being whatever is needed beyond 110 hours?

## Turn 9 - User Simulator

Yes, that is correct. The decision is how to split the 110 regular hours (plus up to 10 overtime hours) between curtain and clothing fabric to meet the minimums, with overtime being whatever is needed beyond 110 hours.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Production capacity:** Shared rate of 1000 meters per hour, same on both shifts, split between the two fabrics.
- **Regular time:** 110 hours per week, to be fully used.
- **Overtime:** Any production beyond 110 hours; hard cap of 10 hours per week (so total production time ≤ 120 hours).
- **Minimum sales (production) requirements:**
  - Curtain fabric: at least 70,000 meters per week.
  - Clothing fabric: at least 45,000 meters per week.
- **No upper limit** on production/sales beyond the available time (110 regular + up to 10 overtime hours).
- **Profit:** Curtain 2.5 yuan/meter; clothing 1.5 yuan/meter (extra production beyond minimums also earns profit, but profit is not the objective).
- **Objective:** Minimize overtime (i.e., minimize total production time beyond 110 hours), subject to meeting the minimums and the 10-hour overtime cap.
- **Decision variables:** How to split the 110 regular hours (and up to 10 overtime hours) between curtain and clothing fabric.

Note: 70,000 + 45,000 = 115,000 meters minimum total, at 1000 m/h that's 115 hours, which exceeds the 110 regular hours, so at least 5 hours of overtime is required to meet both minimums. The model will confirm the exact minimum overtime and the optimal split.