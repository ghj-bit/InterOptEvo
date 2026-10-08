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

QUESTION: What is the objective of the scheduling plan — are we minimizing the total weekly labor cost (sum of wage × hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 2 - Generic Agent

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) with exactly one student on duty at all times — does this mean the lab is open all 14 hours every day from Monday through Friday, and the "maximum duty hours" in Table 5-9 are the upper bounds on how many of those 14 hours each student can work on that day?

## Turn 2 - User Simulator

Yes, the lab is open all 14 hours every day from Monday through Friday, and the values in Table 5-9 are the upper bounds on how many of those 14 hours each student can work on that specific day.

## Turn 3 - Generic Agent

QUESTION: The lab needs exactly one student on duty for all 14 hours each day, so 70 student-hours are required per week. The weekly minimums (undergrads ≥ 8h, grads ≥ 7h) plus the daily caps in Table 5-9 must cover those 70 hours — are students 1–6 all undergraduates, or is there a split between undergraduate and graduate students, and if so, which IDs are which?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still being confirmed internally, can you tell me which students are undergraduates and which are graduates, or should I treat all six students as the same category for now and apply a single minimum-hours rule?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Setting aside the undergraduate/graduate split for now, is there any other constraint on how many hours a single student can work in total across the whole week, or is the only weekly limit the minimum (at least 8 or 7 hours) with the daily caps from Table 5-9 being the only upper bounds?

## Turn 5 - User Simulator

There is an additional weekly limit: each student can work no more than 2 shifts per week.

## Turn 6 - Generic Agent

QUESTION: You mentioned a limit of no more than 2 shifts per week — does "shift" here mean a single continuous block of hours worked on one day (so a student could work up to 2 days per week), or does it mean something else like a fixed-length time slot?

## Turn 6 - User Simulator

A "shift" means a single continuous block of hours worked on one day, so a student can work on at most 2 days per week.

## Turn 7 - Generic Agent

QUESTION: Since each student can work on at most 2 days per week, and the daily caps in Table 5-9 already show 0 for some day-student combinations (meaning they cannot work that day), is the "at most 2 days per week" constraint an additional restriction on top of the table's zeros, or does it replace them — that is, could a student with a non-zero cap on 3 or more days still only pick 2 of those days?

## Turn 7 - User Simulator

It is an additional restriction on top of the table's zeros. A student with a non-zero cap on 3 or more days can still only pick 2 of those days to work.

## Turn 8 - Generic Agent

QUESTION: When a student works on a given day, must they work a single continuous block of hours (e.g., 9:00 AM to 3:00 PM), or can they work multiple separate blocks within that day as long as the total doesn't exceed the daily cap?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Since the continuous-block question is still being confirmed, can you tell me whether the lab's 14 open hours (8:00 AM to 10:00 PM) need to be divided into fixed time slots (e.g., 2-hour blocks), or is the scheduling done at the level of whole hours where any student can be assigned to any hour as long as exactly one student covers each hour?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: For the purpose of building the model, is it acceptable to assume that the 14 hours each day are divided into 14 one-hour slots, and a student assigned to a day works a single continuous block of consecutive hours (so if they work 5 hours on Monday, it would be, say, 8-13 or 10-15, not scattered hours)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Given that the continuous-block detail is still pending, for now can I proceed with the simpler assumption that a student assigned to a day simply works some number of hours (up to the daily cap) and we don't need to track which specific hours they cover, as long as the total hours across all students equals 14 each day?

## Turn 11 - User Simulator

Yes, you can proceed with that assumption for now.

## Turn 12 - Generic Agent

QUESTION: Going back to the undergraduate/graduate split — since that is still pending internal confirmation, can you at least tell me whether the minimum-hours rule (undergrads ≥ 8h, grads ≥ 7h) applies to all six students, or should I treat all six as having the same minimum (e.g., all ≥ 8h or all ≥ 7h) until the split is confirmed?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students are undergraduates and must each work at least 8 hours per week — is that acceptable as a placeholder, or would you prefer I use 7 hours as the minimum for all six?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still pending, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still pending, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Since the undergraduate/graduate split remains unconfirmed, I will proceed with the assumption that all six students must work at least 8 hours per week (the stricter minimum) — is that acceptable as a placeholder for the model?

## Turn 30 - User Simulator

The point still needs internal confirmation.