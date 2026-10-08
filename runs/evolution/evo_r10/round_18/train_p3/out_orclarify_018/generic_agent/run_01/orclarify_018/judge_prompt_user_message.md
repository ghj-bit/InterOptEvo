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

QUESTION: You mention minimizing overtime as the goal, but the brief only states a fixed 110 hours of weekly production time. Is there a separate standard (non-overtime) weekly time limit below 110 hours, so that any production time beyond that standard limit counts as overtime to be minimized?

## Turn 2 - User Simulator

The 110 hours is the standard weekly production time. Overtime is any production time beyond those 110 hours.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum cap on how much overtime the factory is allowed to work per week, or can overtime be unlimited as long as it is minimized?

## Turn 3 - User Simulator

Yes, there is a maximum cap. Overtime should not exceed 10 hours per week.

## Turn 4 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1000 m/h, which already exceeds the 110 standard hours. Is the 10-hour overtime cap a hard limit that must be respected, meaning the plan must fit within 120 total hours?

## Turn 4 - User Simulator

Yes, the 10-hour overtime cap is a hard limit. The plan must fit within 120 total hours.

## Turn 5 - Generic Agent

QUESTION: You mention the factory operates two shifts — does the two-shift structure impose any constraint on the model (for example, a per-shift time limit, or a requirement that production be split between the two shifts), or is it just background information and the only time limits that matter are the 110 standard hours plus the 10-hour overtime cap?

## Turn 5 - User Simulator

The two-shift structure is just background information. The only time limits that matter are the 110 standard hours plus the 10-hour overtime cap.

## Turn 6 - Generic Agent

QUESTION: The brief lists a profit per meter for each fabric, but the stated goal is to minimize overtime. Is profit part of the objective (for example, maximize profit subject to minimizing overtime, or a weighted combination), or is profit just background information and the sole objective is to minimize overtime hours?

## Turn 6 - User Simulator

Profit is just background information. The sole objective is to minimize overtime hours.

## Turn 7 - Generic Agent

QUESTION: Since the minimum sales requirements (115,000 m total) already force 115 hours of production, overtime is fixed at 5 hours regardless of the plan. Is producing exactly the minimum sales (70,000 m curtain and 45,000 m clothing) the intended plan, or is there any reason the factory might want to produce more than the minimums (e.g., to use up available time)?

## Turn 7 - User Simulator

Producing exactly the minimum sales (70,000 m curtain and 45,000 m clothing) is the intended plan. There is no reason to produce more than the minimums.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Weekly production (and sales) of curtain fabric (meters) and clothing fabric (meters). Continuous, non-negative.
- **Minimum sales (hard lower bounds):**
  - Curtain fabric ≥ 70,000 meters/week
  - Clothing fabric ≥ 45,000 meters/week
- **Production rate:** 1000 meters per hour, same for both fabrics.
- **Time limits:**
  - Standard weekly production time = 110 hours (total across both shifts).
  - Overtime = any production time beyond 110 hours.
  - Overtime is capped at 10 hours (hard limit), so total production time ≤ 120 hours.
- **Objective:** Minimize overtime hours (i.e., minimize total production time beyond 110 hours). Profit figures (2.5 yuan/m curtain, 1.5 yuan/m clothing) are background only and not part of the objective.
- **Two shifts:** Background information only; no per-shift constraints.
- **Intended plan:** Produce exactly the minimums (70,000 m curtain + 45,000 m clothing = 115,000 m = 115 hours), which yields 5 hours of overtime. No reason to produce beyond the minimums.

**Model summary:**
- Minimize overtime = max(0, total production hours − 110)
- Subject to:
  - Curtain production ≥ 70,000 m
  - Clothing production ≥ 45,000 m
  - (Curtain + Clothing) / 1000 ≤ 120 hours (total time cap)
  - (Curtain + Clothing) / 1000 ≥ 110 hours is not required; overtime is simply the excess over 110.

The optimal solution is to produce exactly 70,000 m curtain and 45,000 m clothing, using 115 hours, resulting in 5 hours of overtime (the minimum possible given the sales requirements).