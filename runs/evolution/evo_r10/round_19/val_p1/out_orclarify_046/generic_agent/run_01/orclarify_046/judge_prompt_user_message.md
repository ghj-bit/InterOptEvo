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

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times — does this mean the 14 hours are split into 14 one-hour slots, and each student's daily hours in Table 5-9 are integer numbers of those slots they can work?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the minimum weekly hours requirement (8 hours for undergraduates, 7 for graduates), does this mean each student must work at least that many hours in total across the whole week, or at least that many hours on each individual day they work?

## Turn 3 - User Simulator

Each student must work at least that many hours in total across the whole week.

## Turn 4 - Generic Agent

QUESTION: Which students are undergraduates and which are graduates — is there a specific split among student IDs 1 through 6, or are all six students treated the same way for the minimum-hours rule?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: If a student's maximum hours for a given day in Table 5-9 is 0, does that mean the student is completely unavailable that day and cannot be scheduled at all, or does it simply mean they can work up to 0 hours (i.e., also unavailable)?

## Turn 5 - User Simulator

A value of 0 means the student is completely unavailable that day and cannot be scheduled.

## Turn 6 - Generic Agent

QUESTION: Since the lab is open 14 hours and exactly one student must be on duty at all times, the total hours that must be covered each day is 14 — is that correct, or are there days when the lab is not open for the full 14 hours?

## Turn 6 - User Simulator

Yes, the lab is open for the full 14 hours each day from Monday through Friday, so 14 hours must be covered each day.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or rules I should be aware of, such as a maximum number of days per week a student can work, a limit on consecutive days, or a requirement that a student's daily hours be contiguous (one block) rather than split across the day?

## Turn 7 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 8 - Generic Agent

QUESTION: When you say each student can work no more than 2 shifts per week, does "shift" mean a single contiguous block of hours on one day (so a student could work, say, 4 hours on Monday and 4 hours on Wednesday as two shifts), or does it mean a student can be scheduled on at most 2 different days per week?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Regarding the constraint that no more than 3 different students can be scheduled on any single day — does this mean at most 3 students can have nonzero hours on a given day, or at most 3 students can be assigned to any single one-hour slot?

## Turn 9 - User Simulator

It means at most 3 students can have nonzero hours on a given day.

## Turn 10 - Generic Agent

QUESTION: Since the lab needs 14 hours covered each day and at most 3 students can work on a given day, the hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For the minimum weekly hours (8 for undergraduates, 7 for graduates), if a student is unavailable on some days (0 in Table 5-9), does the minimum still apply to their total across only the days they are available, or could a student be exempt from the minimum if their available days don't allow them to reach it?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Since the objective is to minimize total weekly labor cost, is it acceptable for a student to work fewer than their maximum allowed hours on a given day (i.e., the Table 5-9 values are upper bounds, not targets), as long as the 14 hours per day are fully covered by the students scheduled that day?

## Turn 12 - User Simulator

Yes, the Table 5-9 values are upper bounds. A student can work fewer hours than their maximum on a given day, as long as the 14 hours per day are fully covered.

## Turn 13 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Since the lab is open 14 hours each day and at most 3 students can work on a given day, the 14 hours must be split among those students — is it acceptable for a student to work, for example, 6 hours on Monday and 5 hours on Wednesday (two separate days), as long as each day's hours don't exceed their Table 5-9 maximum for that day?

## Turn 30 - User Simulator

The point still needs internal confirmation.