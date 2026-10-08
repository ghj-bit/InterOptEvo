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

QUESTION: The brief says to minimize overtime, but also gives profit per meter and minimum sales — is the true objective to minimize total overtime hours (with the 70,000 m and 45,000 m sales as hard constraints), or to maximize profit subject to some overtime limit, or to minimize overtime only after meeting the sales minimums?

## Turn 1 - User Simulator

The true objective is to minimize total overtime hours. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are hard constraints that must be met.

## Turn 2 - Generic Agent

QUESTION: The brief states weekly production time is 110 hours and the factory operates two shifts — is 110 hours the total regular (non-overtime) time available per week across both shifts, with any production beyond it counted as overtime, or is 110 hours the total time including overtime?

## Turn 2 - User Simulator

110 hours is the total regular (non-overtime) time available per week across both shifts. Any production beyond it is counted as overtime.

## Turn 3 - Generic Agent

QUESTION: The production rate is 1000 meters per hour for both fabrics — is this rate per machine, per shift, or for the whole factory, and can the factory produce both fabrics simultaneously (sharing the 110 hours) or must time be allocated exclusively to one fabric at a time?

## Turn 3 - User Simulator

The 1000 meters per hour rate is for the whole factory. The factory must allocate time exclusively to one fabric at a time; it cannot produce both fabrics simultaneously.

## Turn 4 - Generic Agent

QUESTION: Since the factory must allocate time exclusively to one fabric at a time, is the production schedule a single continuous block per fabric (e.g., all curtain time first, then all clothing time), or can the factory switch back and forth between fabrics within the week?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Overtime is to be minimized — is there any upper limit or cost on overtime hours, or is overtime simply an unbounded resource that can be used as much as needed as long as it is minimized?

## Turn 5 - User Simulator

There is an upper limit: overtime should not exceed 10 hours per week.

## Turn 6 - Generic Agent

QUESTION: The minimum sales are 70,000 m of curtain and 45,000 m of clothing — must the factory produce exactly these amounts, or can it produce more than the minimums (with the extra production either sold or left as leftover inventory)?

## Turn 6 - User Simulator

The factory can produce more than the minimums. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are minimums that must be met, not exact targets.

## Turn 7 - Generic Agent

QUESTION: If the factory produces more than the minimums, what happens to the extra fabric — is it all sold (so production equals sales), or can some be left as leftover inventory that is not sold?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: The 110 regular hours are split across two shifts — is there any per-shift limit on how many hours can be worked, or can all 110 regular hours (and any overtime) be concentrated in a single shift?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: The overtime cap is 10 hours per week — is this 10 hours a total across both shifts, or is it 10 hours per shift (i.e., up to 20 hours total)?

## Turn 9 - User Simulator

The 10 hours is a total across both shifts.

## Turn 10 - Generic Agent

QUESTION: The brief mentions profit per meter (2.5 yuan for curtain, 1.5 yuan for clothing) — since the objective is to minimize overtime, is profit completely irrelevant to the model, or should it play any role (e.g., as a secondary objective or a minimum profit constraint)?

## Turn 10 - User Simulator

Profit is completely irrelevant to the model. The objective is solely to minimize overtime, subject to the production and sales constraints.

## Turn 11 - Generic Agent

QUESTION: To confirm the feasibility picture: with 110 regular hours plus up to 10 overtime hours (120 hours total) at 1000 m/hour, the factory can produce at most 120,000 meters total, while the minimums alone require 115,000 meters (115 hours) — so the minimum overtime needed is 5 hours. Is that understanding correct, i.e., the model should simply find the minimum overtime (5 hours) to meet the minimums, with no incentive to produce beyond them?

## Turn 11 - User Simulator

Yes, that understanding is correct. The model should find the minimum overtime (5 hours) to meet the minimums, with no incentive to produce beyond them.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize total overtime hours per week.
- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Production:** The whole factory produces at 1000 meters/hour, allocating time exclusively to one fabric at a time (no simultaneous production).
- **Regular time:** 110 hours per week total (across two shifts) is available as regular (non-overtime) time.
- **Overtime:** Any production time beyond the 110 regular hours is overtime, capped at 10 hours per week total (across both shifts).
- **Hard constraints (minimums):** At least 70,000 meters of curtain fabric and at least 45,000 meters of clothing fabric must be produced/sold per week.
- **Production beyond minimums:** Permitted but not incentivized; the model has no reason to produce beyond the minimums since the objective is to minimize overtime.
- **Profit:** Irrelevant to the model (2.5 yuan/m curtain, 1.5 yuan/m clothing are not used).
- **Feasibility check confirmed by client:** Minimums require 115 hours of production (70 + 45), so minimum overtime = 115 − 110 = 5 hours, which is within the 10-hour cap.
- **Parked (internal confirmation pending, not load-bearing for the core model):** whether the schedule is one continuous block per fabric or can switch back and forth; whether extra production is all sold or can be leftover inventory; whether there is a per-shift hour limit. None of these change the minimum-overtime optimum of 5 hours, so they do not affect the submitted model.

The model is a small linear program: decide regular hours allocated to each fabric (h_c, h_l) and overtime hours (o_c, o_l), minimize o_c + o_l, subject to 1000·(h_c + o_c) ≥ 70,000, 1000·(h_l + o_l) ≥ 45,000, h_c + h_l ≤ 110, o_c + o_l ≤ 10, and all variables ≥ 0.