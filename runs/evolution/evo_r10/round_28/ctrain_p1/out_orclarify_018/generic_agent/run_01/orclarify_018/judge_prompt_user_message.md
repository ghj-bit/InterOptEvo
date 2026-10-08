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

QUESTION: The brief says to minimize overtime, but it doesn't define what overtime is or how it relates to the 110 weekly production hours — is the 110 hours the regular (non-overtime) capacity, with any production beyond it counting as overtime to be minimized, or is 110 hours the total available time including overtime, with overtime being a separate tracked quantity?

## Turn 1 - User Simulator

The 110 hours is the regular (non-overtime) capacity. Any production time beyond those 110 hours counts as overtime, which is what we want to minimize.

## Turn 2 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1,000 m/h, which already exceeds the 110 regular hours — so is producing exactly the minimum sales (115,000 m, i.e., 5 hours of overtime) the intended plan, or is there a profit target or maximum production level that would make producing more than the minimum worthwhile?

## Turn 2 - User Simulator

The intended plan is to produce exactly the minimum sales quantities: 70,000 meters of curtain fabric and 45,000 meters of clothing fabric. This results in 115 hours of production, which is 5 hours of overtime. There is no profit target or maximum production level that would make producing more than the minimum worthwhile.

## Turn 3 - Generic Agent

QUESTION: You mentioned the factory operates two shifts — does the 110 regular hours split between the two shifts in a way that matters for the model (for example, a per-shift hour cap or a per-shift production limit), or is the two-shift detail just background and the only capacity constraint is the 110 total regular hours?

## Turn 3 - User Simulator

The two-shift detail is just background. The only capacity constraint is the 110 total regular hours.

## Turn 4 - Generic Agent

QUESTION: Since the plan is fixed at exactly 70,000 m curtain and 45,000 m clothing, is the profit information (2.5 and 1.5 yuan per meter) just background context, or should the model still report the total weekly profit as part of the output?

## Turn 4 - User Simulator

The profit information is just background context. The model does not need to report the total weekly profit as part of the output.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Weekly production (in meters) of curtain fabric and clothing fabric.
- **Demand (minimum sales):** At least 70,000 m of curtain fabric and at least 45,000 m of clothing fabric must be produced/sold per week.
- **Production rate:** 1,000 meters per hour, same for both fabrics.
- **Capacity:** 110 hours of regular (non-overtime) production time per week. Any production time beyond 110 hours is overtime.
- **Objective:** Minimize overtime hours.
- **Confirmed plan:** Produce exactly the minimums — 70,000 m curtain + 45,000 m clothing = 115,000 m total, requiring 115 hours, i.e., 5 hours of overtime. No incentive to produce beyond the minimums.
- **Not modeled:** The two-shift structure (background only), and the per-meter profit figures (background only; no profit reporting needed).

The model is a small linear program: minimize overtime hours = max(0, total production hours − 110), subject to production meeting the two minimum sales quantities, with total production hours = (curtain meters + clothing meters) / 1000.