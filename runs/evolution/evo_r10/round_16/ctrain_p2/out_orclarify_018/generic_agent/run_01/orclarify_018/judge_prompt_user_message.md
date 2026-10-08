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

QUESTION: You mention minimizing overtime as the goal, but the brief only gives a total of 110 weekly production hours without specifying how many of those are regular (non-overtime) hours — how many of the 110 hours are regular shift hours, with the remainder counted as overtime?

## Turn 1 - User Simulator

All 110 hours are regular shift hours.

## Turn 2 - Generic Agent

QUESTION: If all 110 hours are regular, then the 115,000 meters required (70,000 + 45,000) exceed the 110,000 meters that 110 hours can produce at 1000 meters/hour — so how should the shortfall be handled: is overtime allowed beyond the 110 regular hours (and if so, at what rate and any cap), or is it acceptable to sell less than the minimum for one of the fabrics?

## Turn 2 - User Simulator

Overtime is allowed beyond the 110 regular hours. It should not exceed 10 hours per week.

## Turn 3 - Generic Agent

QUESTION: With 110 regular hours plus up to 10 overtime hours, the factory can produce at most 120,000 meters, which covers the required 115,000 — so is the production plan exactly the minimum sales (70,000 curtain and 45,000 clothing), or may the factory produce and sell more than these minimums (e.g., to use up available hours or earn extra profit)?

## Turn 3 - User Simulator

The factory may produce and sell more than the minimums.

## Turn 4 - Generic Agent

QUESTION: Since the stated goal is to minimize overtime, is profit (2.5 yuan/meter for curtain, 1.5 yuan/meter for clothing) completely irrelevant to the decision, or should it play some role — for example, as a secondary objective to maximize only among plans that use the minimum overtime?

## Turn 4 - User Simulator

Profit is completely irrelevant to the decision.

## Turn 5 - Generic Agent

QUESTION: You mentioned the factory operates two shifts — does the 110 regular hours (and the 10 overtime hours) need to be split between the two shifts in any particular way, or can all production hours be treated as a single pool without any per-shift limits?

## Turn 5 - User Simulator

The 110 regular hours and the 10 overtime hours can be treated as a single pool without any per-shift limits.

## Turn 6 - Generic Agent

QUESTION: Is the 1000 meters per hour production rate the same for both fabrics regardless of how the hours are split between them, meaning any combination of curtain and clothing hours simply adds up to total meters at that rate?

## Turn 6 - User Simulator

Yes, the 1000 meters per hour production rate is the same for both fabrics.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on how much curtain fabric or clothing fabric can be produced and sold per week (beyond the total 120,000-meter capacity), or is the only constraint the total production capacity?

## Turn 7 - User Simulator

The only constraint is the total production capacity.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Minimize overtime hours used per week. Profit is irrelevant to the decision.
- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Demand (minimums to be sold per week):** at least 70,000 m of curtain fabric and at least 45,000 m of clothing fabric. Production/sales may exceed these minimums.
- **Capacity:** 110 regular hours per week plus up to 10 overtime hours per week (overtime capped at 10 h). All hours form a single pool — no per-shift split required.
- **Production rate:** 1,000 m/hour for both fabrics, identical regardless of how hours are allocated.
- **Constraints:** The only production constraint is total capacity (regular + overtime hours × 1,000 m/h). No per-fabric upper limits.
- **Objective variable:** Overtime hours (0 to 10), to be minimized.

Since the minimums alone require 115,000 m = 115 hours, and regular hours cover 110, the model will determine the minimum overtime needed (at least 5 hours) and how to allocate production between the two fabrics within the capacity.