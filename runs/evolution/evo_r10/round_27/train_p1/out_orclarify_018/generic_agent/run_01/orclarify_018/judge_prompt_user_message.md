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

QUESTION: Is the 110 hours the total weekly production time available across both shifts combined (i.e., the sum of hours worked on shift 1 and shift 2 cannot exceed 110), or is it the regular-time capacity per shift with overtime being any additional hours beyond that?

## Turn 1 - User Simulator

The 110 hours is the total weekly production time available across both shifts combined.

## Turn 2 - Generic Agent

QUESTION: How is overtime defined and measured in this factory — is it any production hour beyond a certain regular-time threshold (and if so, what is that threshold), or is overtime a separate resource (e.g., extra workers or extra hours) that you want to minimize in addition to the 110 hours?

## Turn 2 - User Simulator

Overtime is any production hour beyond the 110 hours of regular weekly production time.

## Turn 3 - Generic Agent

QUESTION: Since the minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1,000 m/hour, which exceeds the 110 regular hours, is overtime allowed and is there any upper limit on how many overtime hours can be used per week?

## Turn 3 - User Simulator

Yes, overtime is allowed. The upper limit is 10 hours per week.

## Turn 4 - Generic Agent

QUESTION: You mentioned the factory operates two shifts — does the shift structure impose any constraint on the model (for example, a maximum number of hours per shift, or a requirement that production be split between the two shifts), or is the only relevant limit the 110 regular hours plus up to 10 overtime hours per week?

## Turn 4 - User Simulator

The only relevant limit is the 110 regular hours plus up to 10 overtime hours per week.

## Turn 5 - Generic Agent

QUESTION: You said the goal is to minimize overtime "as much as possible" — is overtime the sole objective (i.e., minimize total overtime hours, with the sales minimums as hard constraints), or should profit also play a role (for example, minimize overtime first, then maximize profit among plans with the same overtime, or maximize profit subject to some overtime cap)?

## Turn 5 - User Simulator

Overtime is the sole objective. The goal is to minimize total overtime hours, with the sales minimums as hard constraints.

## Turn 6 - Generic Agent

QUESTION: The brief says at least 70,000 m of curtain and 45,000 m of clothing "must be sold" — is production exactly equal to these sales (i.e., no inventory, no leftover fabric carried over), so that producing more than the minimums is pointless and the model should treat production = sales?

## Turn 6 - User Simulator

Yes, production equals sales. There is no inventory or leftover fabric carried over, so producing more than the minimums is pointless.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much of the 110 regular hours (or the 10 overtime hours) can be allocated to each fabric type, or can the full 120 hours be split freely between curtain and clothing production in any proportion?

## Turn 7 - User Simulator

The full 120 hours can be split freely between curtain and clothing production in any proportion.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Hours allocated to curtain production (h_c) and hours allocated to clothing production (h_l), plus overtime hours (OT).
- **Production rate:** 1,000 meters per hour for both fabrics.
- **Sales/production equality:** Production = sales, no inventory. So curtain production = 1,000·h_c meters, clothing production = 1,000·h_l meters.
- **Hard constraints (minimum sales):**
  - Curtain: 1,000·h_c ≥ 70,000 → h_c ≥ 70
  - Clothing: 1,000·h_l ≥ 45,000 → h_l ≥ 45
- **Capacity:** Regular time = 110 hours total; overtime allowed up to 10 hours. Total production hours h_c + h_l ≤ 110 + OT, with 0 ≤ OT ≤ 10.
- **Objective:** Minimize OT (total overtime hours). Profit figures (2.5 and 1.5 yuan/meter) are not used in the objective.
- **Shift structure:** No additional constraints beyond the 110 + 10 hour limits.
- **Free allocation:** Hours can be split between the two fabrics in any proportion.

Note: The minimums require 70 + 45 = 115 hours, so at least 5 hours of overtime are unavoidable; the model will confirm the minimum feasible OT.