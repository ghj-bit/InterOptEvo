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

QUESTION: Is the goal to minimize total overtime hours (with the 110 hours being regular time and any production beyond it counting as overtime), or is the goal to minimize the number of overtime shifts worked?

## Turn 1 - User Simulator

The goal is to minimize total overtime hours. The 110 hours are regular time, and any production beyond that counts as overtime hours.

## Turn 2 - Generic Agent

QUESTION: Is there a maximum limit on how many overtime hours can be worked per week, or is overtime unlimited as long as it is minimized?

## Turn 2 - User Simulator

There is a maximum limit of 10 overtime hours per week.

## Turn 3 - Generic Agent

QUESTION: The 110 regular hours plus up to 10 overtime hours gives at most 120 production hours, i.e. at most 120,000 meters total, while the minimum sales require 115,000 meters — so the minimums are feasible. Is the 110 hours a shared total across both fabrics (i.e., the two fabrics compete for the same 110 regular hours), or does each fabric have its own 110 hours?

## Turn 3 - User Simulator

The 110 hours is a shared total across both fabrics. The two fabrics compete for the same 110 regular hours.

## Turn 4 - Generic Agent

QUESTION: Is the 10-hour overtime limit also a shared total across both fabrics (i.e., total overtime for both fabrics combined cannot exceed 10 hours), or does each fabric get its own 10 hours of overtime?

## Turn 4 - User Simulator

The 10-hour overtime limit is a shared total across both fabrics. Total overtime for both fabrics combined cannot exceed 10 hours.

## Turn 5 - Generic Agent

QUESTION: Is the production rate of 1000 meters per hour the same for both fabrics regardless of which shift is being worked, or does the rate differ between the two shifts?

## Turn 5 - User Simulator

The production rate of 1000 meters per hour is the same for both fabrics regardless of which shift is being worked.

## Turn 6 - Generic Agent

QUESTION: The two shifts are mentioned but the 110 hours and 10 overtime hours are given as weekly totals — do the two shifts impose any additional constraint (such as a per-shift hour cap or a requirement that production be split between shifts), or are the shifts just descriptive and the only hour limits are the 110 regular and 10 overtime weekly totals?

## Turn 6 - User Simulator

The shifts are just descriptive. The only hour limits are the 110 regular and 10 overtime weekly totals.

## Turn 7 - Generic Agent

QUESTION: The minimum sales of 70,000 meters of curtain fabric and 45,000 meters of clothing fabric must be met — is production allowed to exceed these minimums (i.e., produce and sell more than the minimums), or must production be exactly equal to the minimums?

## Turn 7 - User Simulator

Production is allowed to exceed these minimums.

## Turn 8 - Generic Agent

QUESTION: Since the objective is to minimize overtime hours, and the minimum sales (115,000 meters) already require 115 production hours (110 regular + 5 overtime), is there any reason to produce beyond the minimums — for example, is profit maximization a secondary goal, or is the plan simply to meet the minimums with the least overtime and produce nothing extra?

## Turn 8 - User Simulator

The plan is simply to meet the minimums with the least overtime and produce nothing extra.

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on how much of each fabric can be produced per week (such as a maximum production capacity per fabric), or are the only production limits the shared 110 regular hours and 10 overtime hours?

## Turn 9 - User Simulator

The only production limits are the shared 110 regular hours and 10 overtime hours.

## Turn 10 - Generic Agent

QUESTION: Since the minimums (115,000 meters) already require 115 hours, which is 5 hours over the 110 regular hours, the plan will necessarily use 5 overtime hours — is that acceptable, or is there a way to reduce the required production (for example, can some of the minimum sales be met from existing inventory rather than new production)?

## Turn 10 - User Simulator

No, the minimum sales must be met from new production.

## Turn 11 - Generic Agent

QUESTION: Is there any cost or penalty associated with overtime hours (such as a per-hour overtime wage premium), or is the objective purely to minimize the total number of overtime hours without any monetary cost attached?

## Turn 11 - User Simulator

The objective is purely to minimize the total number of overtime hours without any monetary cost attached.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Facility**: A textile factory producing two fabrics — curtain fabric and clothing fabric. Two shifts exist but are purely descriptive; they impose no additional constraints.

- **Decision variables**: Weekly production (in meters) of curtain fabric and clothing fabric. Both are continuous, non-negative quantities.

- **Production capacity**:
  - Regular time: 110 hours per week, shared across both fabrics.
  - Overtime: up to 10 hours per week, shared across both fabrics.
  - Production rate: 1000 meters per hour for both fabrics, same on both shifts.
  - Total available production: at most 120 hours × 1000 = 120,000 meters.

- **Minimum sales (must be met from new production, no inventory)**:
  - Curtain fabric: at least 70,000 meters per week.
  - Clothing fabric: at least 45,000 meters per week.
  - Production may exceed these minimums, but the plan is to produce nothing extra.

- **Objective**: Minimize total overtime hours used (overtime = total production hours beyond the 110 regular hours). No monetary cost is attached to overtime; it is purely a minimization of hours.

- **No other limits**: No per-fabric capacity caps, no per-shift caps, no inventory, no demand upper bounds.

- **Feasibility note**: The minimums require 115,000 meters = 115 hours, which is 5 hours over the 110 regular hours, so at least 5 overtime hours are unavoidable. The overtime cap of 10 hours is not binding.

- **Profit figures** (curtain 2.5 yuan/m, clothing 1.5 yuan/m) are provided but do not enter the objective, since the goal is overtime minimization, not profit maximization.