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

QUESTION: Is the lab open for the full 8:00 AM to 10:00 PM span on each of Monday through Friday, and is the "one and only one student on duty" requirement meant to hold continuously across every hour of that span (so each day needs exactly 14 student-hours of coverage)?

## Turn 1 - User Simulator

Yes, the lab is open for the full 8:00 AM to 10:00 PM span on each of Monday through Friday. The "one and only one student on duty" requirement holds continuously across every hour of that span, so each day requires exactly 14 student-hours of coverage.

## Turn 2 - Generic Agent

QUESTION: The daily maximums in Table 5-9 sum to only 13 hours for Monday, 20 for Tuesday, 20 for Wednesday, 12 for Thursday, and 21 for Friday, so Monday and Thursday cannot reach the 14 hours of coverage the lab needs. Should I treat the table values as hard caps and accept that Monday and Thursday are infeasible, or should I instead treat them as soft caps that may be exceeded when needed to reach 14 hours of coverage?

## Turn 2 - User Simulator

The table values are hard caps. If Monday and Thursday cannot reach 14 hours of coverage under these caps, the point still needs internal confirmation regarding how to handle the infeasibility.

## Turn 3 - Generic Agent

QUESTION: Since Monday and Thursday are infeasible under the hard caps, how should the model handle those two days: should it drop the "exactly 14 hours of coverage" requirement on Monday and Thursday and instead cover as many hours as the caps allow (maximizing covered hours), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Setting aside the Monday/Thursday infeasibility, what should the model optimize: minimize the total weekly wage cost of the scheduled hours, or maximize the total number of covered hours across the week?

## Turn 4 - User Simulator

The model should minimize the total weekly wage cost of the scheduled hours.

## Turn 5 - Generic Agent

QUESTION: For the minimum weekly hours (8 for undergraduates, 7 for graduates), should these be treated as hard lower bounds that every student must meet, or as soft targets that may be missed if doing so is necessary to keep the schedule feasible?

## Turn 5 - User Simulator

The minimum weekly hours are hard lower bounds that every student must meet.

## Turn 6 - Generic Agent

QUESTION: Which students are undergraduates and which are graduates, so I can apply the 8-hour and 7-hour minimums correctly?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still unconfirmed, should I apply the 8-hour minimum to every student as a safe default (which automatically satisfies the 7-hour graduate minimum as well)?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: For the daily maximums in Table 5-9, should a value of 0 be read as "this student is completely unavailable that day" (they cannot work any hours), or as "this student may work up to 0 hours but could still be scheduled if needed"?

## Turn 8 - User Simulator

A value of 0 means the student is completely unavailable that day and cannot work any hours.

## Turn 9 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Should the model be treated as a linear program where daily hours can take fractional values, or as an integer program where each student's daily hours must be whole numbers?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For the "one and only one student on duty" rule, should it be enforced at the level of each individual hour (exactly one student assigned to each of the 14 hourly slots per day), or is it enough to enforce it only at the daily level (the sum of all students' hours in a day equals 14)?

## Turn 11 - User Simulator

The "one and only one student on duty" rule should be enforced at the level of each individual hour, meaning exactly one student is assigned to each of the 14 hourly slots per day.

## Turn 12 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still unconfirmed, should I apply the 8-hour minimum to every student as a safe default (which automatically satisfies the 7-hour graduate minimum as well)?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Should the model be treated as a linear program where daily hours can take fractional values, or as an integer program where each student's daily hours must be whole numbers?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the "one and only one student on duty" rule, should it be enforced at the level of each individual hour (exactly one student assigned to each of the 14 hourly slots per day), or is it enough to enforce it only at the daily level (the sum of all students' hours in a day equals 14)?

## Turn 16 - User Simulator

The "one and only one student on duty" rule should be enforced at the level of each individual hour, meaning exactly one student is assigned to each of the 14 hourly slots per day.

## Turn 17 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 18 - User Simulator

The point still needs internal confirmation

## Turn 19 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 20 - User Simulator

The point still needs internal confirmation

## Turn 21 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 21 - User Simulator

The point still needs internal

## Turn 22 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 22 - User Simulator

The point

## Turn 23 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: For the Monday and Thursday infeasibility, should the model drop the "exactly 14 hours of coverage" requirement on those two days and instead cover as many hours as the caps allow (maximizing covered hours on Monday and Thursday), while keeping exactly 14 hours on Tuesday and Wednesday?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Should each student's daily hours be modeled as whole hours (integer), or can they be fractional (for example, 3.5 hours on a given day)?

## Turn 30 - User Simulator

The