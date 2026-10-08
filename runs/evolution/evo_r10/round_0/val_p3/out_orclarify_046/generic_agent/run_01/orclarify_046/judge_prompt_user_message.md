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

QUESTION: What is the objective of the scheduling plan — is it to minimize the total weekly labor cost (sum of wage × hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 2 - Generic Agent

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times — does this mean the 14 hours are divided into 14 one-hour slots, and each student's daily hours must be an integer number of these slots (i.e., a student works whole hours only, not fractions of an hour)?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Since the hourly-slot question is still being confirmed, may I proceed on the assumption that the 14 open hours are divided into 14 one-hour slots and each student's daily hours must be a whole number of slots (integer hours), with the constraint that exactly one student is assigned to each slot?

## Turn 3 - User Simulator

Yes, you may proceed on that assumption.

## Turn 4 - Generic Agent

QUESTION: The weekly minimums are 8 hours for undergraduates and 7 hours for graduates — are students 1–3 undergraduates and students 4–6 graduates, or is the undergraduate/graduate split different?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still being confirmed, may I proceed on the assumption that students 1–3 are undergraduates (minimum 8 hours/week) and students 4–6 are graduates (minimum 7 hours/week)?

## Turn 5 - User Simulator

Yes, you may proceed on that assumption.

## Turn 6 - Generic Agent

QUESTION: For the daily maximum hours in Table 5-9, a value of 0 (e.g., student 1 on Tuesday) means that student is completely unavailable on that day and cannot be assigned any slot, correct?

## Turn 6 - User Simulator

Yes, a value of 0 means that student is completely unavailable on that day and cannot be assigned any slot.

## Turn 7 - Generic Agent

QUESTION: Is there any additional constraint that a student cannot work on consecutive days, or that a student must have at least one day off per week, beyond the daily maximums already given in Table 5-9?

## Turn 7 - User Simulator

No, there is no additional constraint requiring a day off or prohibiting consecutive work days beyond the daily maximums in Table 5-9.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Setting:** A university computer lab is open Monday–Friday, 8:00 AM–10:00 PM = 14 one-hour slots per day, 70 slots per week.
- **Staff:** 6 students. Students 1–3 are undergraduates; students 4–6 are graduates.
- **Coverage:** Exactly one student is assigned to each of the 70 one-hour slots (one and only one on duty at all times).
- **Decision variables:** For each student and each day, the number of one-hour slots (integer, 0–14) that student works.
- **Daily availability / max hours:** A student's hours on a given day cannot exceed the value in Table 5-9; a value of 0 means the student is unavailable that day.
- **Weekly minimums:** Each undergraduate (students 1–3) works at least 8 hours per week; each graduate (students 4–6) works at least 7 hours per week.
- **No other restrictions:** No day-off or consecutive-day constraints beyond the daily maximums.
- **Objective:** Minimize total weekly labor cost = Σ (student's hourly wage × total hours worked that week).

Wages (CNY/h): student 1 = 10.0, student 2 = 10.0, student 3 = 9.9, student 4 = 9.8, student 5 = 10.8, student 6 = 11.3.

I will now formulate this as an integer linear program.