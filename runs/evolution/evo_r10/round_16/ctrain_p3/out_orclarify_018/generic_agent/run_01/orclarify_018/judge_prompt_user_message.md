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

QUESTION: The brief says to minimize overtime, but also lists profit per meter for each fabric — should the plan's objective be to minimize overtime hours (with the 70,000 m and 45,000 m sales as hard minimums), or to maximize total profit subject to some overtime limit, or to minimize overtime only after profit is maximized?

## Turn 1 - User Simulator

The objective is to minimize overtime hours. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are hard minimums. The profit figures are not part of the optimization objective.

## Turn 2 - Generic Agent

QUESTION: The brief states weekly production time is 110 hours, but 70,000 m + 45,000 m at 1,000 m/h requires 115 hours — so at least 5 hours of overtime is unavoidable. Is 110 hours the regular (non-overtime) time available, with overtime being any hours beyond 110, and is there any upper limit on how much overtime can be worked?

## Turn 2 - User Simulator

Yes, 110 hours is the regular (non-overtime) time available. Overtime is any hours beyond 110. There is an upper limit: overtime should not exceed 10 hours per week.

## Turn 3 - Generic Agent

QUESTION: The brief mentions the factory operates two shifts — does this two-shift structure impose any constraint on the model (for example, a per-shift hour cap, a shift-specific production rate, or a requirement that production be split between shifts), or is it just background information and the only time constraints are the 110 regular hours plus up to 10 overtime hours?

## Turn 3 - User Simulator

The two-shift structure is just background information. The only time constraints are the 110 regular hours plus up to 10 overtime hours.

## Turn 4 - Generic Agent

QUESTION: The production rate is 1,000 meters per hour for both fabrics — is this a shared rate, meaning the factory can produce at most 1,000 meters per hour in total across both fabrics combined (so producing both simultaneously doesn't double output), or can each fabric be produced at 1,000 meters per hour independently?

## Turn 4 - User Simulator

It is a shared rate. The factory can produce at most 1,000 meters per hour in total across both fabrics combined.

## Turn 5 - Generic Agent

QUESTION: Since the minimums (70,000 m + 45,000 m = 115,000 m) already require 115 hours, which exceeds the 110 regular hours, the plan must use at least 5 overtime hours. Is it acceptable for the factory to produce more than the minimums (e.g., extra curtain or clothing fabric) as long as total production time stays within 120 hours, or should production be exactly the minimums with no extra fabric produced?

## Turn 5 - User Simulator

Production should be exactly the minimums with no extra fabric produced.

## Turn 6 - Generic Agent

QUESTION: Since production is fixed at exactly 70,000 m of curtain fabric and 45,000 m of clothing fabric, the total time is fixed at 115 hours, meaning overtime is always exactly 5 hours regardless of any decision. Is there any flexibility I'm missing — for example, can the factory choose to produce some of the required fabric in regular time versus overtime, or is the overtime amount simply a fixed 5 hours with no real decision to make?

## Turn 6 - User Simulator

The overtime amount is simply a fixed 5 hours with no real decision to make.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize overtime hours.
- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Hard minimums (production = sales, exactly):**
  - Curtain fabric: 70,000 meters per week
  - Clothing fabric: 45,000 meters per week
- **Production rate:** Shared rate of 1,000 meters per hour total across both fabrics combined.
- **Time:**
  - Regular (non-overtime) time available: 110 hours per week
  - Overtime: any hours beyond 110, capped at 10 hours per week
- **Two shifts:** Background information only; no per-shift constraints.
- **Profit figures (2.5 yuan/m curtain, 1.5 yuan/m clothing):** Not part of the objective; informational only.
- **No extra production:** Production is exactly the minimums; no surplus fabric.

**Resulting model:**
- Total production = 70,000 + 45,000 = 115,000 meters
- Total time required = 115,000 / 1,000 = 115 hours
- Regular time used = 110 hours
- Overtime = 115 − 110 = **5 hours** (within the 10-hour cap)

The overtime is fixed at 5 hours with no decision variables affecting it. The model is essentially a feasibility check confirming that the minimums are achievable within the time budget (115 ≤ 110 + 10 = 120), and the minimum overtime is 5 hours.