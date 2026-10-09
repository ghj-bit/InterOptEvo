# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U5, U2
I need help creating a staffing plan for a 24-hour bus service, where the objective is to minimize the total number of drivers and crew members needed, and during each time period, the number of drivers and crew members on duty must be at least the required number specified in the table.

Required number of drivers and crew members per time period:
| Shift | Time | Required number |
|-------|------|-----------------|
| 1 | 6:00 ~ 10:00 | 60 |
| 2 | 10:00 ~ 14:00 | 70 |
| 3 | 14:00 ~ 18:00 | 60 |
| 4 | 18:00 ~ 22:00 | 50 |
| 5 | 22:00 ~ 2:00 | 20 |
| 6 | 2:00 ~ 6:00 | 30 |

## Problem units
- U1 (context): I need help creating a staffing plan for a 24-hour bus service.
- U2 (data): Required number of drivers and crew members per time period:
| Shift | Time | Required number |
|-------|------|-----------------|
| 1 | 6:00 ~ 10:00 | 60 |
| 2 | 10:00 ~ 14:00 | 70 |
| 3 | 14:00 ~ 18:00 | 60 |
| 4 | 18:00 ~ 22:00 | 50 |
| 5 | 22:00 ~ 2:00 | 20 |
| 6 | 2:00 ~ 6:00 | 30 |
- U3 (assumption): Drivers and crew members start their shifts at the beginning of each time period and work continuously for 8 hours.
- U4 (objective): Minimize the total number of drivers and crew members needed.
- U5 (constraint): During each time period, the number of drivers and crew members on duty must be at least the required number specified in the table.

## Hidden slot scoring rules
## H1: eight_hour_shift_start_rule
- Severity: P0
- Severity reason: Without knowing shift duration and start times, the decision variables and constraints that link staffing across periods are undefined, making the problem ill-posed and impossible to model responsibly.
- Problem unit ID: U3
- Semantic hit rule: The agent must ask about the length of a shift and/or when shifts begin, or explicitly inquire about the work pattern described as 8-hour continuous shifts starting at the period boundaries.
- Reference acceptable questions:
  - How long are the shifts, and when do they begin?
  - Do all drivers work exactly 8-hour shifts starting at the beginning of each time period?
- Failure modes:
  - Assuming shift lengths are flexible or unconstrained
  - Assuming drivers can start work at any time within a period, not necessarily at the period start
  - Assuming shift duration is not explicitly 8 hours continuous


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When a driver starts a shift at a given time, how many consecutive 4-hour periods do they work (for example, does a driver starting at 6:00 work only the 6:00–10:00 period, or do they work 6:00–10:00 and 10:00–14:00, or longer)?

## Turn 1 - User Simulator

They work two consecutive 4-hour periods. For example, a driver starting at 6:00 works the 6:00–10:00 period and the 10:00–14:00 period.

## Turn 2 - Generic Agent

QUESTION: Are drivers allowed to start a shift at any of the six period boundaries (6:00, 10:00, 14:00, 18:00, 22:00, 2:00), or are there restrictions on which start times are permitted?

## Turn 2 - User Simulator

Drivers can start a shift at any of the six period boundaries.

## Turn 3 - Generic Agent

QUESTION: When a driver's two-period shift crosses midnight (for example, starting at 22:00 and covering 22:00–2:00 and 2:00–6:00), is that treated as a single continuous shift within the same planning day, or does it count as two separate shifts on different days?

## Turn 3 - User Simulator

It is treated as a single continuous shift within the same planning day.

## Turn 4 - Generic Agent

QUESTION: Is the staffing plan a single-day plan that repeats identically every day, or do you need a multi-day plan where shifts can span across days?

## Turn 4 - User Simulator

It is a single-day plan that repeats identically every day.

## Turn 5 - Generic Agent

QUESTION: Are the required numbers (60, 70, 60, 50, 20, 30) minimums that must be met or exceeded in each period, or must they be met exactly?

## Turn 5 - User Simulator

They are minimums that must be met or exceeded in each period.

## Turn 6 - Generic Agent

QUESTION: Are the decision variables (number of drivers starting at each of the six boundaries) required to be whole numbers, or can they be fractional?

## Turn 6 - User Simulator

They must be whole numbers.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total number of drivers available, or is the only objective to minimize the total number of drivers needed?

## Turn 7 - User Simulator

There is no limit on the total number of drivers available. The only objective is to minimize the total number of drivers needed.

## Turn 8 - Generic Agent

QUESTION: When you say "minimize the total number of drivers needed," do you mean minimizing the sum of drivers starting at all six boundaries (i.e., total shift-starts per day), or minimizing the maximum number of drivers on duty at any single time?

## Turn 8 - User Simulator

It means minimizing the sum of drivers starting at all six boundaries (i.e., total shift-starts per day).

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** Single day, 24 hours, divided into 6 consecutive 4-hour periods (6:00–10:00, 10:00–14:00, 14:00–18:00, 18:00–22:00, 22:00–2:00, 2:00–6:00). The plan repeats identically every day.

- **Decision variables:** Six non-negative integer variables, one per period boundary (6:00, 10:00, 14:00, 18:00, 22:00, 2:00), representing the number of drivers starting a shift at that time.

- **Shift structure:** Each driver works exactly two consecutive 4-hour periods. A driver starting at boundary *i* covers period *i* and period *i+1* (wrapping around midnight, e.g., a 22:00 start covers 22:00–2:00 and 2:00–6:00).

- **Constraints:** For each of the six periods, the sum of drivers whose two-period shift covers that period must be at least the required number (60, 70, 60, 50, 20, 30 respectively). These are minimums, not exact targets.

- **Objective:** Minimize the sum of all six decision variables (total shift-starts per day).

- **No upper bound** on the number of drivers available.