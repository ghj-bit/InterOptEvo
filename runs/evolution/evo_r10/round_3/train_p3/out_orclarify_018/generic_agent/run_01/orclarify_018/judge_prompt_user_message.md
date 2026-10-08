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

QUESTION: What is the primary objective of the production plan — is it to minimize overtime hours (with the 70,000 m and 45,000 m sales minimums as hard constraints), or to maximize total weekly profit (with overtime minimized only as a secondary/tie-breaking goal)?

## Turn 1 - User Simulator

The primary objective is to minimize overtime hours. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric sales minimums are hard constraints.

## Turn 2 - Generic Agent

QUESTION: The brief says the factory operates two shifts with 110 hours of weekly production time — is 110 hours the total regular (non-overtime) capacity available across both shifts, with any production beyond 110 hours counted as overtime to be minimized?

## Turn 2 - User Simulator

Yes, 110 hours is the total regular (non-overtime) capacity available across both shifts. Any production beyond 110 hours is counted as overtime.

## Turn 3 - Generic Agent

QUESTION: Is there any upper limit on how much overtime hours can be used per week, or is overtime unlimited (only penalized in the objective)?

## Turn 3 - User Simulator

There is an upper limit. Overtime should not exceed 10 hours per week.

## Turn 4 - Generic Agent

QUESTION: Is the production rate of 1000 meters per hour the same for both fabrics regardless of which shift (regular or overtime) is used, so that total weekly production capacity is simply (110 + overtime) × 1000 meters?

## Turn 4 - User Simulator

Yes, the production rate is 1000 meters per hour for both fabrics, regardless of whether it is regular or overtime time.

## Turn 5 - Generic Agent

QUESTION: The brief lists a profit per meter for each fabric, but since the objective is minimizing overtime, is profit completely irrelevant to the model, or should it play some role (e.g., a minimum weekly profit target, or a secondary objective after overtime is minimized)?

## Turn 5 - User Simulator

Profit is completely irrelevant to the model.

## Turn 6 - Generic Agent

QUESTION: Is there any maximum production limit per fabric per week (i.e., can the factory produce more than the 70,000 m and 45,000 m minimums if it wants to, or are those also the maximums)?

## Turn 6 - User Simulator

There is no maximum production limit per fabric. The 70,000 meters and 45,000 meters are minimums only.

## Turn 7 - Generic Agent

QUESTION: Is there any constraint linking the two shifts — for example, must both shifts run the same number of hours, or can the factory allocate regular hours freely between the two shifts as long as the total regular time does not exceed 110 hours?

## Turn 7 - User Simulator

I don't have specific information about constraints linking the two shifts. That point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the two shifts have no distinguishing constraints and the production rate is identical, can I treat the factory as having a single pool of 110 regular hours plus up to 10 overtime hours (total capacity 120 hours × 1000 m/h = 120,000 m), with the only decision being how many meters of each fabric to produce?

## Turn 8 - User Simulator

Yes, you can treat the factory as having a single pool of 110 regular hours plus up to 10 overtime hours. The only decision is how many meters of each fabric to produce.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Weekly production (in meters) of curtain fabric and clothing fabric. Both are continuous, non-negative, with no upper bound.
- **Hard constraints:**
  - Curtain fabric production ≥ 70,000 meters.
  - Clothing fabric production ≥ 45,000 meters.
  - Total production time (curtain + clothing meters ÷ 1000 m/h) ≤ 120 hours (110 regular + 10 overtime).
- **Objective:** Minimize overtime hours, where overtime = max(0, total production hours − 110).
- **Parameters:**
  - Production rate: 1000 meters per hour (same for both fabrics, same for regular and overtime).
  - Regular capacity: 110 hours/week.
  - Overtime cap: 10 hours/week.
  - Profit figures are irrelevant to the model.
- **No other constraints** (no shift-linking rules, no per-fabric maximums, no demand upper bounds).

The model is a small linear program: minimize overtime subject to the two sales minimums and the total capacity ceiling.