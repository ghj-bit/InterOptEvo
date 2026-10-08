# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U5, U6, U9, U2, U3
I need help creating a duty scheduling plan for a university computer lab with undergraduate and graduate student workers, where there must be one and only one student on duty during open hours. Each undergraduate must work at least 8 hours per week, and each graduate student must work at least 7 hours per week. Additionally, for each student, their working hours on a given day cannot exceed the maximum hours specified in Table 5-9.

Table 5-9: Hourly wage and maximum duty hours from Monday to Friday for each student.

| Student ID | Wage (CNY/h) | Monday | Tuesday | Wednesday | Thursday | Friday |
|------------|--------------|--------|---------|-----------|----------|--------|
| 1          | 10.0         | 6      | 0       | 6         | 0        | 7      |
| 2          | 10.0         | 0      | 8       | 9         | 6        | 0      |
| 3          | 9.9          | 4      | 8       | 3         | 0        | 5      |
| 4          | 9.8          | 5      | 5       | 6         | 0        | 4      |
| 5          | 10.8         | 3      | 0       | 5         | 8        | 0      |
| 6          | 11.3         | 0      | 6       | 0         | 6        | 5      |

The lab operates from 8:00 AM to 10:00 PM.

## Problem units
- U1 (context): I need help creating a duty scheduling plan for a university computer lab with undergraduate and graduate student workers.
- U2 (data): Table 5-9: Hourly wage and maximum duty hours from Monday to Friday for each student.

| Student ID | Wage (CNY/h) | Monday | Tuesday | Wednesday | Thursday | Friday |
|------------|--------------|--------|---------|-----------|----------|--------|
| 1          | 10.0         | 6      | 0       | 6         | 0        | 7      |
| 2          | 10.0         | 0      | 8       | 9         | 6        | 0      |
| 3          | 9.9          | 4      | 8       | 3         | 0        | 5      |
| 4          | 9.8          | 5      | 5       | 6         | 0        | 4      |
| 5          | 10.8         | 3      | 0       | 5         | 8        | 0      |
| 6          | 11.3         | 0      | 6       | 0         | 6        | 5      |
- U3 (data): The lab operates from 8:00 AM to 10:00 PM.
- U4 (constraint): There must be one and only one student on duty during open hours.
- U5 (constraint): Each undergraduate must work at least 8 hours per week.
- U6 (constraint): Each graduate student must work at least 7 hours per week.
- U7 (constraint): Each student can work no more than 2 shifts per week.
- U8 (constraint): No more than 3 students can be scheduled for duty each day.
- U9 (constraint): For each student, their working hours on a given day cannot exceed the maximum hours specified in Table 5-9.
- U10 (objective): Minimize total gross pay (sum over all students of hourly wage multiplied by total hours worked during the week).

## Hidden slot scoring rules
## H1: max_shifts_per_week
- Severity: P1
- Severity reason: Without this constraint, the agent can still formulate a valid scheduling model using daily hour limits and coverage constraints, but the model would be under‑constrained and might assign a student to work on more than 2 distinct days, violating the intended business rule. The agent should clarify this before finalizing.
- Problem unit ID: U7
- Semantic hit rule: The Agent's question must ask about a limit on the number of shifts or working days per student per week.
- Reference acceptable questions:
  - Is there a limit on how many different days a student can work?
  - Can a student be scheduled on more than two days of the week?
- Failure modes:
  - Assuming there is no limit on the number of days a student can work, possibly scheduling a student across all 5 days
  - Assuming a 'shift' is the same as a day and not considering distinct time blocks

## H2: max_students_per_day
- Severity: P1
- Severity reason: Missing this constraint leads to a schedule that could assign more than three distinct students on any day, which might be a labor rule the problem intends. The agent can still build a coherent model without it, but the resulting schedule would not comply with the full specification, so clarification is needed for accuracy.
- Problem unit ID: U8
- Semantic hit rule: The Agent's question must inquire about a daily limit on the count of distinct students assigned to duty.
- Reference acceptable questions:
  - Is there a limit on the number of different students who can work on the same day?
  - Can I schedule all six students on a single day if their individual hours allow?
- Failure modes:
  - Assuming any number of students can be used per day as long as only one is on duty at a time
  - Overlooking the distinct-student-per-day cap and scheduling 4 or more students on one day

## H3: objective_minimize_gross_pay
- Severity: P0
- Severity reason: Without an explicit objective, the optimization problem is ill‑posed. The agent cannot build a meaningful model without knowing what to minimize or maximize. The objective must be clarified before modeling.
- Problem unit ID: U10
- Semantic hit rule: The Agent's question must explicitly ask about the optimization goal (objective), such as minimizing total cost or gross pay.
- Reference acceptable questions:
  - What is the objective of the optimization? Should we minimize total cost?
  - Are we trying to minimize the total wage payout?
- Failure modes:
  - Assuming the objective is to minimize the number of students used or total hours worked, rather than gross pay
  - Proceeding with a feasibility-only formulation without any objective


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, but the daily maximum hours in Table 5-9 sum to only 13 hours on Monday (6+0+4+5+3+0), so the stated requirements cannot all be met as written — could you clarify how to resolve this, for example by (a) treating the table values as the actual available hours and allowing the lab to be unstaffed for the remaining hour(s) each day, (b) treating the table values as upper bounds that may be exceeded up to the 14 open hours, or (c) some other reading you intended?

## Turn 1 - User Simulator

The table values are strict upper bounds on the hours each student can work on that specific day. They cannot be exceeded.

Because the sum of these maximums is less than the 14 open hours on some days, the lab will be unstaffed for the remaining hours. Please proceed with the assumption that the lab is unstaffed for any hours not covered by the scheduled students, while strictly adhering to the daily maximums in Table 5-9.

## Turn 2 - Generic Agent

QUESTION: You mentioned "one and only one student on duty during open hours" — since the lab will be unstaffed for some hours, does the "only one" rule mean that in any hour that IS staffed, exactly one student works (no two students simultaneously), and the objective is to minimize total weekly labor cost subject to the weekly minimums (8h undergrad / 7h grad) and the daily caps?

## Turn 2 - User Simulator

Yes, that is correct. In any hour that is staffed, exactly one student works. No two students work simultaneously. The goal is to minimize total weekly labor cost while meeting the weekly minimums and respecting the daily caps.

## Turn 3 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergrads and the 7-hour minimum to grads?

## Turn 3 - User Simulator

Students 1, 2, and 3 are undergraduates. Students 4, 5, and 6 are graduate students.

## Turn 4 - Generic Agent

QUESTION: Are the weekly minimums (8 hours for undergrads, 7 hours for grads) hard requirements that must be met for every student, or are they soft targets that may be relaxed (e.g., with a penalty) if infeasible?

## Turn 4 - User Simulator

They are hard requirements. Every undergraduate must work at least 8 hours per week, and every graduate student must work at least 7 hours per week.

## Turn 5 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 also hard upper bounds that must never be exceeded, or are they soft limits that could be relaxed with a penalty if needed?

## Turn 5 - User Simulator

They are hard upper bounds. No student may work more than the specified maximum hours on any given day.

## Turn 6 - Generic Agent

QUESTION: Are the working hours for each student on each day required to be whole numbers (integer hours), or can they be fractional (e.g., 2.5 hours)?

## Turn 6 - User Simulator

The working hours must be whole numbers.

## Turn 7 - Generic Agent

QUESTION: Is the objective purely to minimize total weekly labor cost (sum of wage × hours for all students), with no other considerations such as fairness, preference for certain students, or penalties for unstaffed hours?

## Turn 7 - User Simulator

Yes, the objective is purely to minimize total weekly labor cost. There are no other considerations such as fairness, student preferences, or penalties for unstaffed hours.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Setting:** A university computer lab open 8:00 AM–10:00 PM (14 hours/day), Monday–Friday.
- **Staffing rule:** In any hour that is staffed, exactly one student works (no two students simultaneously). The lab may be unstaffed for hours not covered.
- **Students:** 6 students. Students 1, 2, 3 are undergraduates; students 4, 5, 6 are graduate students.
- **Wages (CNY/h):** Student 1: 10.0, Student 2: 10.0, Student 3: 9.9, Student 4: 9.8, Student 5: 10.8, Student 6: 11.3.
- **Daily maximum hours (hard upper bounds, integer):** As given in Table 5-9.
- **Weekly minimums (hard lower bounds):** Each undergraduate (1, 2, 3) must work at least 8 hours per week; each graduate student (4, 5, 6) must work at least 7 hours per week.
- **Integrality:** All working hours are non-negative integers.
- **Objective:** Minimize total weekly labor cost = Σ (wage_i × total hours_i) over all students.
- **No other constraints:** No fairness, no preferences, no penalty for unstaffed hours.