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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, so 14 duty-hours are needed each day. However, the sum of the daily maximum hours in Table 5-9 is only 13 for Monday, 18 for Tuesday, 12 for Wednesday, 16 for Thursday, and 16 for Friday — so Monday and Wednesday cannot reach 14 hours. Does the lab actually need coverage for the full 8:00 AM–10:00 PM window every day, or is the daily open window shorter (and if so, how many hours per day must be covered)?

## Turn 1 - User Simulator

The lab does need coverage for the full 8:00 AM to 10:00 PM window every day. That is 14 hours per day.

## Turn 2 - Generic Agent

QUESTION: Since the full 14-hour window is required but the daily maximum-hour sums in Table 5-9 are only 13 (Monday) and 12 (Wednesday), the schedule as stated cannot be feasible. Which of these readings should I use: (a) the daily maximums in Table 5-9 are correct and the lab may be closed for the uncovered hours on those days; (b) the daily maximums are correct and I should treat the problem as infeasible and report that; or (c) the daily maximums should be read as minimums or are otherwise adjustable, so I should maximize coverage subject to the weekly minimums?

## Turn 2 - User Simulator

The daily maximums in Table 5-9 are correct. The lab must be covered for the full 14 hours every day. The problem as stated is infeasible.

## Turn 3 - Generic Agent

QUESTION: Since the problem is infeasible as stated, what should the final deliverable be: (a) a formal proof/report demonstrating infeasibility (e.g., showing the daily maximum-hour sums fall short of 14 on Monday and Wednesday); (b) a model that minimizes the uncovered hours per day (so the shortfall is made explicit and minimized) while still respecting the weekly minimums and daily maximums; or (c) a model that relaxes the "exactly one on duty" rule to "at most one on duty" and minimizes total labor cost, reporting the resulting coverage gaps?

## Turn 3 - User Simulator

The final deliverable should be (a) a formal proof/report demonstrating infeasibility.

## Turn 4 - Generic Agent

QUESTION: For the infeasibility proof, should I demonstrate it using only the daily maximum-hour sums (i.e., Monday's sum of 13 and Wednesday's sum of 12 are each less than the required 14 hours), or should I also verify that no other constraint (weekly minimums, wage, etc.) independently causes infeasibility?

## Turn 4 - User Simulator

Demonstrate it using only the daily maximum-hour sums.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Setting:** A university computer lab is open 8:00 AM–10:00 PM (14 hours) each day, Monday through Friday. Exactly one student worker must be on duty at all times during open hours, so 14 duty-hours are required per day.
- **Workers:** 6 students (IDs 1–6), each with an hourly wage and per-day maximum duty hours as given in Table 5-9.
- **Constraints as stated:**
  - Exactly one student on duty at all times → 14 hours of coverage required each day.
  - Each undergraduate must work at least 8 hours/week; each graduate at least 7 hours/week.
  - Each student's hours on a given day cannot exceed the daily maximum in Table 5-9.
- **Key finding (confirmed by the client):** The problem is infeasible. The sum of the daily maximum hours across all students is:
  - Monday: 6+0+4+5+3+0 = 13 < 14
  - Tuesday: 0+8+8+5+0+6 = 27 ≥ 14
  - Wednesday: 6+9+3+6+5+0 = 29 ≥ 14
  - Thursday: 0+6+0+0+8+6 = 20 ≥ 14
  - Friday: 7+0+5+4+0+5 = 21 ≥ 14

  Since Monday's total available capacity (13 hours) is less than the 14 hours required, no feasible schedule exists.

- **Deliverable:** A formal proof/report demonstrating infeasibility using only the daily maximum-hour sums (specifically, Monday's sum of 13 < 14). No optimization model is needed; the report will show that the coverage requirement cannot be met on Monday regardless of how hours are allocated among students.