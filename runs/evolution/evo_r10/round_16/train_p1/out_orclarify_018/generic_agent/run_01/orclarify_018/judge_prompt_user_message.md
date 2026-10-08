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

QUESTION: The brief says to minimize overtime, but also lists a profit per meter for each fabric — is the goal to minimize overtime hours (with the 70,000 m and 45,000 m sales minimums as hard constraints), or to maximize total profit subject to some overtime limit?

## Turn 1 - User Simulator

The goal is to minimize overtime hours. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are hard constraints. The profit figures are not part of the optimization objective.

## Turn 2 - Generic Agent

QUESTION: The brief states weekly production time is 110 hours, but 70,000 m + 45,000 m at 1000 m/hour requires 115 hours — so is the 110 hours the regular (non-overtime) time available, with overtime being the extra hours needed beyond 110, or is 110 hours the total time including any overtime?

## Turn 2 - User Simulator

The 110 hours is the regular (non-overtime) time available. Overtime is the extra hours needed beyond 110.

## Turn 3 - Generic Agent

QUESTION: The brief mentions the factory operates two shifts — does this two-shift structure affect the model in any way (for example, a per-shift capacity limit, a shift-specific overtime rule, or a requirement to split production across shifts), or is it just background information and the only time limit that matters is the 110 regular hours plus overtime?

## Turn 3 - User Simulator

It is just background information. The only time limit that matters is the 110 regular hours plus overtime.

## Turn 4 - Generic Agent

QUESTION: Is there any upper limit on how much overtime can be scheduled per week (for example, a maximum number of overtime hours or a cap on total weekly hours), or can overtime be as large as needed to meet the sales minimums?

## Turn 4 - User Simulator

Yes, overtime should not exceed 10 hours per week.

## Turn 5 - Generic Agent

QUESTION: Since the sales minimums (70,000 m + 45,000 m) require 115 hours but only 120 hours are available (110 regular + 10 overtime), can the factory produce more than the minimum sales amounts of each fabric, or must production be exactly equal to the minimum sales quantities?

## Turn 5 - User Simulator

Production must be exactly equal to the minimum sales quantities.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize overtime hours.
- **Decision variables:**
  - Overtime hours (continuous, non-negative, capped at 10 hours/week).
  - Production of curtain fabric (meters) and clothing fabric (meters).
- **Constraints:**
  - Curtain fabric production = exactly 70,000 meters (hard constraint).
  - Clothing fabric production = exactly 45,000 meters (hard constraint).
  - Total production time = (70,000 + 45,000) / 1000 = 115 hours.
  - Regular time available = 110 hours.
  - Overtime = total production time − regular time = 115 − 110 = 5 hours.
  - Overtime ≤ 10 hours/week.
- **Not part of the model:** Profit figures (2.5 yuan/m for curtain, 1.5 yuan/m for clothing), two-shift structure.
- **Result:** The minimum overtime is 5 hours, which is within the 10-hour cap, so the problem is feasible.