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

QUESTION: The lab is open 14 hours a day (8:00–22:00) but the daily maximum hours in Table 5-9 sum to far less than 14 for most days, so I need to know how the "one and only one student on duty" requirement is meant to work: is the lab actually staffed for only part of the day (i.e., there is a specific set of open hours each day, which I should treat as the coverage requirement), or is the lab open the full 8:00–22:00 every day and the student on duty may simply be off-duty for part of that span?

## Turn 1 - User Simulator

The lab is open the full 8:00–22:00 every day, and the student on duty must cover the entire 14-hour span. The "one and only one student on duty" requirement means that for every hour within that 14-hour window, exactly one student is assigned to be on duty.

## Turn 2 - Generic Agent

QUESTION: Since each student's maximum daily hours (from Table 5-9) are far below 14, a single student cannot cover the whole day, so I need to clarify the coverage rule: does "exactly one student on duty for every hour" mean that at each hour exactly one student is working (so the 14 hours are split among different students, each within their daily cap), or does it mean exactly one student is designated "on duty" for the entire day (which would be infeasible given the caps)?

## Turn 2 - User Simulator

At each hour, exactly one student is working. The 14 hours are split among different students, each within their daily cap.

## Turn 3 - Generic Agent

QUESTION: The daily maximum hours in Table 5-9 sum to only 18 hours across all six students on Monday, but the lab needs 14 hours of coverage that day, and on Wednesday the sum is only 22 hours for 14 hours needed — so coverage is feasible, but I need to confirm the objective: is the goal to minimize the total weekly labor cost (sum of wage × hours worked for each student), subject to the coverage, minimum-hours, and daily-cap constraints?

## Turn 3 - User Simulator

Yes, the goal is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week, subject to the coverage, minimum-hours, and daily-cap constraints.

## Turn 4 - Generic Agent

QUESTION: For the minimum weekly hours requirement (at least 8 hours for undergraduates, at least 7 for graduates), I need to know which students are undergraduates and which are graduates — can you tell me the classification of each of the six students (IDs 1–6)?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is still pending, I need to know how to handle the minimum-hours requirement in the meantime: should I treat all six students as having the same minimum weekly hours (and if so, which value — 8 or 7), or should I set up the model with a placeholder minimum for each student that you can fill in once the classification is confirmed?

## Turn 5 - User Simulator

Set up the model with a placeholder minimum for each student that I can fill in once the classification is confirmed.

## Turn 6 - Generic Agent

QUESTION: For the daily coverage, I need to confirm the time granularity: are the 14 hours (8:00–22:00) divided into 14 one-hour slots (8–9, 9–10, …, 21–22), and is each student's hours worked in a day simply the count of one-hour slots they are assigned that day (so hours are whole numbers)?

## Turn 6 - User Simulator

Yes, the 14 hours are divided into 14 one-hour slots, and each student's hours worked in a day is the count of one-hour slots they are assigned that day, so hours are whole numbers.

## Turn 7 - Generic Agent

QUESTION: I need to confirm the daily-cap interpretation: does a value of 0 in Table 5-9 (for example, Student 1 on Tuesday) mean that student is completely unavailable and cannot be assigned any slot that day, while a positive value means they can be assigned up to that many one-hour slots?

## Turn 7 - User Simulator

Yes, a value of 0 means that student is completely unavailable and cannot be assigned any slot that day, while a positive value means they can be assigned up to that many one-hour slots.

## Turn 8 - Generic Agent

QUESTION: I need to confirm the coverage feasibility on each day: the sum of daily caps is 18 (Mon), 29 (Tue), 22 (Wed), 20 (Thu), 21 (Fri), all ≥ 14, so coverage is feasible — but I want to confirm there is no additional constraint such as a student not being allowed to work consecutive slots, or a maximum number of days per week a student can work, beyond what is already stated?

## Turn 8 - User Simulator

There is no additional constraint such as a student not being allowed to work consecutive slots, or a maximum number of days per week a student can work, beyond what is already stated.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Setting:** A university computer lab is open every day Monday–Friday, 8:00–22:00, i.e., 14 one-hour slots per day (8–9, 9–10, …, 21–22).
- **Workers:** Six students (IDs 1–6), each with an hourly wage and a per-day maximum number of one-hour slots they may work (Table 5-9). A value of 0 means the student is unavailable that day; a positive value is an upper bound on slots that day.
- **Coverage constraint:** For every one-hour slot on every day, exactly one student is assigned (so 14 student-slots per day, 70 total per week).
- **Minimum weekly hours:** Each student must work at least a minimum number of hours per week. The undergraduate/graduate classification (which determines whether the minimum is 8 or 7) is still pending, so the model uses a placeholder minimum `minHours[i]` for each student i, to be filled in once confirmed.
- **Daily cap:** Each student's slots on a given day ≤ the corresponding Table 5-9 value.
- **No other constraints:** No restrictions on consecutive slots, no max days per week, nothing beyond the above.
- **Objective:** Minimize total weekly labor cost = Σ (wage[i] × total hours worked by student i that week).
- **Variables:** Integer (whole-number) slot assignments; a student's daily hours = count of slots assigned that day.

I will now formulate the model accordingly.