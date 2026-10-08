# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U2, U3
I need help planning the staffing for a 24-hour convenience store, and for each time period, the number of salespeople scheduled to work during that period must be at least the required number for that period, while each salesperson works exactly one 8-hour shift, starting at one of the specified start times (2:00, 6:00, 10:00, 14:00, 18:00, or 22:00), covering the four consecutive 2-hour periods from the start time.

Required number of salespeople per time period:
2:00-6:00: 10
6:00-10:00: 15
10:00-14:00: 25
14:00-18:00: 20
18:00-22:00: 18
22:00-2:00: 12

Shift start times: 2:00, 6:00, 10:00, 14:00, 18:00, 22:00. Shift duration: 8 hours.

## Problem units
- U1 (context): I need help planning the staffing for a 24-hour convenience store.
- U2 (data): Required number of salespeople per time period:
2:00-6:00: 10
6:00-10:00: 15
10:00-14:00: 25
14:00-18:00: 20
18:00-22:00: 18
22:00-2:00: 12
- U3 (data): Shift start times: 2:00, 6:00, 10:00, 14:00, 18:00, 22:00. Shift duration: 8 hours.
- U4 (objective): Minimize the total number of salespeople needed to meet the requirements.
- U5 (constraint): For each time period, the number of salespeople scheduled to work during that period must be at least the required number for that period.
- U6 (constraint): Each salesperson works exactly one 8-hour shift, starting at one of the specified start times (2:00, 6:00, 10:00, 14:00, 18:00, or 22:00), covering the four consecutive 2-hour periods from the start time.

## Hidden slot scoring rules
## H1: missing_minimization_objective
- Severity: P0
- Severity reason: Without the objective function, the agent cannot determine what constitutes an optimal solution; the problem is ill-posed and modeling cannot proceed meaningfuly.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must explicitly ask about the objective or goal of the staffing problem, specifically whether the aim is to minimize the total number of salespeople.
- Reference acceptable questions:
  - What are we trying to optimize here? Is the goal to minimize the total number of salespeople?
  - Just to confirm, are we minimizing the total headcount of salespeople scheduled overall?
- Failure modes:
  - Silent incorrect assumption: Assuming the objective is to minimize total labor cost rather than total number of salespeople.
  - Silent incorrect assumption: Assuming the objective is to maximize service level or employee satisfaction without clarification.
  - Silent incorrect assumption: Proceeding to build a feasible schedule without any optimization objective.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the goal to minimize the total number of salespeople scheduled across all six shifts (i.e., the sum of staff assigned to each start time), or is there a different objective such as minimizing total labor cost or keeping the total headcount as close as possible to the requirements?

## Turn 1 - User Simulator

The goal is to minimize the total number of salespeople scheduled across all six shifts.

## Turn 2 - Generic Agent

QUESTION: Should the number of salespeople assigned to each shift start time be a whole number (you can't schedule half a person), or is a fractional value acceptable in the plan?

## Turn 2 - User Simulator

The number of salespeople assigned to each shift start time must be a whole number.

## Turn 3 - Generic Agent

QUESTION: The 22:00-2:00 period spans midnight, so it is covered by the 18:00 shift (18:00-2:00) and the 22:00 shift (22:00-2:00). Does the 2:00-6:00 period at the start of the day get covered by the 22:00 shift from the previous day (22:00-6:00) and the 2:00 shift, meaning the schedule is a repeating daily cycle where the 22:00 shift carries over into the next day's early morning?

## Turn 3 - User Simulator

Yes, the schedule is a repeating daily cycle where the 22:00 shift carries over into the next day's early morning, covering the 22:00-2:00 and 2:00-6:00 periods.

## Turn 4 - Generic Agent

QUESTION: Since each salesperson works exactly one 8-hour shift per day, is it allowed for the same salesperson to work different shifts on different days (so the daily plan is independent), or must each salesperson work the same shift start time every day?

## Turn 4 - User Simulator

The daily plan is independent; the same salesperson can work different shifts on different days.

## Turn 5 - Generic Agent

QUESTION: Are there any upper limits on how many salespeople can be scheduled for a single shift start time, or is the only constraint that each period's coverage meets or exceeds its required number?

## Turn 5 - User Simulator

There are no upper limits on how many salespeople can be scheduled for a single shift start time. The only constraint is that each period's coverage meets or exceeds its required number.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Problem type:** Integer linear programming (staffing / shift scheduling).
- **Decision variables:** For each of the six shift start times (2:00, 6:00, 10:00, 14:00, 18:00, 22:00), a non-negative integer variable representing the number of salespeople starting their 8-hour shift at that time.
- **Shift coverage:** Each 8-hour shift covers the four consecutive 2-hour periods beginning at its start time. Because the schedule is a repeating daily cycle, the 22:00 shift covers the periods 22:00-2:00, 2:00-6:00, 6:00-10:00, and 10:00-14:00 (wrapping past midnight).
- **Coverage mapping (period → shifts covering it):**
  - 2:00-6:00: 22:00 shift + 2:00 shift
  - 6:00-10:00: 22:00 shift + 2:00 shift + 6:00 shift
  - 10:00-14:00: 22:00 shift + 2:00 shift + 6:00 shift + 10:00 shift
  - 14:00-18:00: 2:00 shift + 6:00 shift + 10:00 shift + 14:00 shift
  - 18:00-22:00: 6:00 shift + 10:00 shift + 14:00 shift + 18:00 shift
  - 22:00-2:00: 10:00 shift + 14:00 shift + 18:00 shift + 22:00 shift
- **Requirements (minimum coverage per period):** 2:00-6:00: 10; 6:00-10:00: 15; 10:00-14:00: 25; 14:00-18:00: 20; 18:00-22:00: 18; 22:00-2:00: 12.
- **Constraints:** For each of the six periods, the sum of the shift variables covering that period must be at least the required number for that period.
- **Objective:** Minimize the total number of salespeople scheduled, i.e., the sum of the six shift variables.
- **Domain:** All shift variables are non-negative integers.
- **No upper bounds** on any shift variable.
- **Daily independence:** The plan is for a single repeating day; no cross-day or per-person consistency constraints.