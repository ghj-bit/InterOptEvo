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

QUESTION: When you say the factory operates two shifts with a total of 110 hours of production time per week, is 110 hours the total available time across both shifts combined, or is it the available time per shift (making 220 hours total)?

## Turn 1 - User Simulator

110 hours is the total available time across both shifts combined.

## Turn 2 - Generic Agent

QUESTION: You mentioned minimizing overtime as the goal, but the 110 hours is described as the total available production time. Is there a separate regular-time limit (for example, 80 hours) such that any production beyond that limit counts as overtime, or is the 110-hour figure itself the regular-time capacity with overtime defined as any additional hours beyond 110?

## Turn 2 - User Simulator

The 110-hour figure is the regular-time capacity. Overtime is any additional hours beyond 110.

## Turn 3 - Generic Agent

QUESTION: The minimum sales requirements (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1,000 m/hour, which already exceeds the 110-hour regular capacity. Is the plan required to meet these minimum sales exactly, or is it allowed to produce and sell more than the minimums (for example, to use the extra overtime hours profitably)?

## Turn 3 - User Simulator

The plan must meet at least the minimum sales requirements. It is allowed to produce and sell more than the minimums.

## Turn 4 - Generic Agent

QUESTION: You listed profit per meter for both fabrics, but your stated goal is minimizing overtime. Is the objective purely to minimize overtime hours (with profit being irrelevant to the decision), or should the plan balance profit against overtime (for example, by maximizing profit minus an overtime cost, or by minimizing overtime only among plans that achieve a target profit)?

## Turn 4 - User Simulator

The objective is purely to minimize overtime hours. Profit is not part of the decision criteria.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum limit on how many overtime hours can be used per week, or is overtime allowed to be any non-negative amount needed to meet the minimum sales requirements?

## Turn 5 - User Simulator

There is a maximum limit of 10 overtime hours per week.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the total production or sales of each fabric type per week (for example, a maximum number of meters that can be produced or sold), or can the factory produce and sell unlimited quantities of each fabric as long as the minimums are met and the 10-hour overtime cap is respected?

## Turn 6 - User Simulator

There is no maximum limit on the total production or sales of each fabric type per week. The factory can produce and sell unlimited quantities of each fabric as long as the minimums are met and the 10-hour overtime cap is respected.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize overtime hours per week. Profit is not part of the decision criteria.
- **Decision variables:**
  - Hours allocated to curtain fabric production (continuous, non-negative).
  - Hours allocated to clothing fabric production (continuous, non-negative).
  - Overtime hours (continuous, non-negative, capped at 10).
- **Production capacity:**
  - Regular-time capacity: 110 hours total per week (across both shifts combined).
  - Overtime: any hours beyond 110, with a maximum of 10 overtime hours per week.
  - Total available production time: up to 120 hours per week.
- **Production rate:** 1,000 meters per hour for both fabric types.
- **Minimum sales requirements (floors):**
  - Curtain fabric: at least 70,000 meters per week.
  - Clothing fabric: at least 45,000 meters per week.
- **No upper bounds** on production or sales of either fabric type.
- **Feasibility note:** The minimums require 115,000 meters total, which at 1,000 m/hour requires 115 hours. Since regular capacity is 110 hours, at least 5 overtime hours are required. The 10-hour overtime cap is not binding for feasibility (5 ≤ 10).
- **Assumptions (none critical):** No other constraints (e.g., labor, materials, machine availability) beyond the time-based capacity and minimum sales floors.

The model is a simple linear program: minimize overtime hours subject to meeting the minimum meter requirements within the 110 + overtime hour budget, with overtime ≤ 10.