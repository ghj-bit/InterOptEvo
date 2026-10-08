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

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) with exactly one student on duty at all times — does this mean the single on-duty student works the entire 14-hour stretch each day, or are there multiple duty shifts per day (e.g., morning and evening) where different students can cover different time blocks?

## Turn 2 - User Simulator

There are multiple duty shifts per day, and different students can cover different time blocks.

## Turn 3 - Generic Agent

QUESTION: How many duty shifts are there per day, and what are their time boundaries (for example, 8:00–12:00 and 12:00–18:00 and 18:00–22:00)?

## Turn 3 - User Simulator

I don't have the specific number of shifts per day or their exact time boundaries. That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the exact shift boundaries are still being confirmed internally, for now should I model the day as a set of discrete shifts where each shift has a known duration (in hours) and exactly one student is assigned to each shift, with the total hours per day summing to 14 — and treat the number of shifts and their durations as parameters you will provide later?

## Turn 4 - User Simulator

Yes, that is a reasonable way to model it for now. Treat the number of shifts and their durations as parameters to be provided later, with the constraint that the total hours per day sum to 14 and exactly one student is assigned to each shift.

## Turn 5 - Generic Agent

QUESTION: The daily maximum hours in Table 5-9 (e.g., Student 1 can work at most 6 hours on Monday) — does this cap apply to the total hours a student works across all shifts on that day, meaning a student can be assigned to multiple shifts on the same day as long as their combined hours don't exceed the cap?

## Turn 5 - User Simulator

Yes, the daily maximum hours in Table 5-9 apply to the total hours a student works across all shifts on that day. A student can be assigned to multiple shifts on the same day as long as their combined hours do not exceed the cap.

## Turn 6 - Generic Agent

QUESTION: The weekly minimum hours (8 hours for undergraduates, 7 hours for graduates) — are all six students in the table undergraduates, or are some of them graduate students? If some are graduates, which student IDs are graduate students?

## Turn 6 - User Simulator

I don't have the information on which specific student IDs are graduate students versus undergraduates. That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is still pending, should I model this by treating each student's weekly minimum hours as a parameter (8 for undergrads, 7 for grads) that you will confirm later, rather than hard-coding a specific split?

## Turn 7 - User Simulator

Yes, that is a reasonable approach. Treat each student's weekly minimum hours as a parameter to be confirmed later, rather than hard-coding a specific split.

## Turn 8 - Generic Agent

QUESTION: If a student's daily maximum hours in Table 5-9 is 0 (for example, Student 1 on Tuesday), does that mean the student is completely unavailable for any shift on that day, or could they still be assigned a shift of zero hours?

## Turn 8 - User Simulator

A daily maximum of 0 means the student is completely unavailable for any shift on that day.

## Turn 9 - Generic Agent

QUESTION: Are there any constraints on how many consecutive days a student can work, or any requirement that a student must have at least one day off per week?

## Turn 9 - User Simulator

I don't have any information about constraints on consecutive working days or mandatory days off. That point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Since consecutive-day and day-off constraints are still pending, should I proceed without them for now (i.e., a student can work on any subset of the five days as long as the daily caps and weekly minimum are met), and add such constraints later if they are confirmed?

## Turn 10 - User Simulator

Yes, proceed without them for now. A student can work on any subset of the five days as long as the daily caps and weekly minimum are met. Add such constraints later if they are confirmed.

## Turn 11 - Generic Agent

QUESTION: Can the same student be assigned to two different shifts on the same day, or is each student limited to at most one shift per day?

## Turn 11 - User Simulator

The same student can be assigned to two different shifts on the same day, as long as their combined hours do not exceed the daily maximum in Table 5-9.

## Turn 12 - Generic Agent

QUESTION: Is there any upper limit on the total number of hours a single student can work in a week, beyond the daily caps in Table 5-9?

## Turn 12 - User Simulator

I don't have any information about an upper limit on total weekly hours beyond the daily caps in Table 5-9. That point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Since a weekly upper cap is still pending, should I proceed with only the daily caps as the upper bound on each student's hours, and add a weekly cap later if one is confirmed?

## Turn 13 - User Simulator

Yes, proceed with only the daily caps as the upper bound on each student's hours for now. Add a weekly cap later if one is confirmed.

## Turn 14 - Generic Agent

QUESTION: Are there any constraints on which students can cover which shifts — for example, must a graduate student be on duty during certain hours, or can any available student cover any shift?

## Turn 14 - User Simulator

I don't have any information about constraints on which students can cover which shifts. That point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Since shift-specific eligibility constraints are still pending, should I proceed with the assumption that any student who is available (daily cap > 0) can be assigned to any shift on that day, and add eligibility restrictions later if they are confirmed?

## Turn 15 - User Simulator

Yes, proceed with the assumption that any student who is available (daily cap > 0) can be assigned to any shift on that day. Add eligibility restrictions later if they are confirmed.

## Turn 16 - Generic Agent

QUESTION: Is the lab open every day from Monday through Friday, or are there other days (e.g., Saturday, Sunday) that also require coverage?

## Turn 16 - User Simulator

The lab is open Monday through Friday only.

## Turn 17 - Generic Agent

QUESTION: Is there any requirement that the same student cannot be assigned to two shifts that are adjacent (back-to-back) on the same day, or is there no such restriction?

## Turn 17 - User Simulator

I don't have any information about restrictions on adjacent or back-to-back shifts. That point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Since adjacent-shift restrictions are still pending, should I proceed without them for now (i.e., a student can work back-to-back shifts on the same day as long as the daily cap is not exceeded), and add such a constraint later if it is confirmed?

## Turn 18 - User Simulator

Yes, proceed without them for now. A student can work back-to-back shifts on the same day as long as the daily cap is not exceeded. Add such a constraint later if it is confirmed.

## Turn 19 - Generic Agent

QUESTION: When you say "one and only one student on duty during open hours," does this mean exactly one student is assigned to each individual shift (so the lab is always covered by exactly one person), or could there be periods where no student is assigned as long as the total coverage hours per day equal 14?

## Turn 19 - User Simulator

Exactly one student is assigned to each individual shift, so the lab is always covered by exactly one person.

## Turn 20 - Generic Agent

QUESTION: Are the shifts of equal duration, or can different shifts on the same day have different durations (for example, a 4-hour morning shift and a 2-hour evening shift)?

## Turn 20 - User Simulator

I don't have information on whether shifts are of equal duration or can vary. That point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Since shift durations are still pending, should I model each shift as having a parameterized duration (in hours) that you will provide later, with the constraint that the sum of all shift durations on a given day equals 14 hours?

## Turn 21 - User Simulator

Yes, model each shift as having a parameterized duration (in hours) to be provided later, with the constraint that the sum of all shift durations on a given day equals 14 hours.

## Turn 22 - Generic Agent

QUESTION: Is there any requirement that a student's total hours worked in a week must be an integer number of hours, or can hours be fractional (for example, if a shift is 1.5 hours long)?

## Turn 22 - User Simulator

I don't have any information about whether hours must be integers or can be fractional. That point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Since integrality of hours is still pending, should I proceed with the assumption that hours can be fractional (i.e., a student's total weekly hours need not be a whole number), and add an integrality constraint later if one is confirmed?

## Turn 23 - User Simulator

Yes, proceed with the assumption that hours can be fractional. Add an integrality constraint later if one is confirmed.

## Turn 24 - Generic Agent

QUESTION: Is there any requirement that the total number of shifts per day must be the same across all five days (Monday through Friday), or can different days have different numbers of shifts?

## Turn 24 - User Simulator

I don't have any information about whether the number of shifts per day must be the same across all five days. That point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Since the number of shifts per day is still pending, should I model the number of shifts as a parameter that can differ from day to day (i.e., Monday could have 3 shifts while Tuesday has 4), with each day's shifts summing to 14 hours?

## Turn 25 - User Simulator

Yes, model the number of shifts as a parameter that can differ from day to day, with each day's shifts summing to 14 hours.

## Turn 26 - Generic Agent

QUESTION: Is there any requirement that a student must be assigned to at least one shift on a given day if they are available (daily cap > 0), or can an available student simply not be assigned to any shift that day?

## Turn 26 - User Simulator

I don't have any information about whether an available student must be assigned to at least one shift on a given day. That point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Since the requirement for available students to work at least one shift per day is still pending, should I proceed without it (i.e., an available student may or may not be assigned to any shift on a given day, as long as the weekly minimum is met), and add such a constraint later if it is confirmed?

## Turn 27 - User Simulator

Yes, proceed without it. An available student may or may not be assigned to any shift on a given day, as long as the weekly minimum is met.

## Turn 28 - Generic Agent

QUESTION: Is there any requirement that the total number of students on duty across the week must be balanced in some way (for example, each student must work roughly the same number of shifts), or is the only fairness-related constraint the weekly minimum hours?

## Turn 28 - User Simulator

I don't have any information about balancing the total number of students on duty across the week or any fairness-related constraints beyond the weekly minimum hours. That point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Since fairness or balancing constraints beyond the weekly minimum are still pending, should I proceed with only the weekly minimum hours as the sole per-student lower-bound constraint, and add any balancing or fairness constraints later if they are confirmed?

## Turn 29 - User Simulator

Yes, proceed with only the weekly minimum hours as the sole per-student lower-bound constraint. Add any balancing or fairness constraints later if they are confirmed.

## Turn 30 - Generic Agent

QUESTION: Is there any requirement that a student cannot work on a day where their daily cap is 0, even if they are assigned to a shift of zero hours on that day?

## Turn 30 - User Simulator

Yes, a student cannot work on a day where their daily cap is 0.