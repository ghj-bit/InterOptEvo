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

QUESTION: What is the objective of the scheduling plan — is it to minimize the total weekly wage cost, to maximize fairness, or something else?

## Turn 1 - User Simulator

The objective is to minimize the total weekly wage cost.

## Turn 2 - Generic Agent

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times — is the "maximum duty hours" in Table 5-9 the cap on how many of those 14 hours a student can work on that day, meaning the 14 open hours each day must be fully covered by splitting them among the students?

## Turn 2 - User Simulator

Yes, the maximum duty hours in Table 5-9 are the caps on how many of the 14 open hours a student can work on that day, and the 14 open hours each day must be fully covered by splitting them among the students.

## Turn 3 - Generic Agent

QUESTION: Are the 14 open hours each day divisible into whole 1-hour slots (so each student works an integer number of hours per day), or can a student work fractional hours within a day?

## Turn 3 - User Simulator

The available business facts do not specify whether the 14 open hours must be divided into whole 1-hour slots or if fractional hours are allowed. This point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: For the weekly minimums — must each undergraduate work at least 8 hours and each graduate at least 7 hours in total across the whole week, or is that a per-day minimum?

## Turn 4 - User Simulator

The weekly minimums are totals across the whole week: each undergraduate must work at least 8 hours per week, and each graduate student must work at least 7 hours per week.

## Turn 5 - Generic Agent

QUESTION: Which of the six students are undergraduates and which are graduate students?

## Turn 5 - User Simulator

The available business facts do not specify which of the six students are undergraduates and which are graduate students. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many hours a student can work in total across the whole week (a weekly cap), or is the only per-student limit the daily maximum from Table 5-9 plus the weekly minimum?

## Turn 6 - User Simulator

There is no weekly cap on total hours. The only per-student limits are the daily maximums from Table 5-9 and the weekly minimums (8 hours for undergraduates, 7 hours for graduate students).

## Turn 7 - Generic Agent

QUESTION: Can a student work zero hours on a day where their Table 5-9 maximum is 0, and is it allowed for a student to work fewer than their daily maximum on days where the maximum is positive (i.e., the table values are upper bounds, not required hours)?

## Turn 7 - User Simulator

Yes, a student can work zero hours on a day where their Table 5-9 maximum is 0. Also, the table values are upper bounds, not required hours, so a student is allowed to work fewer than their daily maximum on days where the maximum is positive.

## Turn 8 - Generic Agent

QUESTION: Is there any requirement that a student's hours within a day must be contiguous (one unbroken block), or can a student's hours on a given day be split into separate blocks as long as the total doesn't exceed the daily maximum?

## Turn 8 - User Simulator

The available business facts do not specify whether a student's hours within a day must be contiguous or can be split into separate blocks. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints I should know about, such as a student being unavailable on certain days beyond what Table 5-9 shows, or a requirement that the same student cannot work consecutive days?

## Turn 9 - User Simulator

There are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 10 - Generic Agent

QUESTION: When you say "no more than 2 shifts per week," does a "shift" mean a single contiguous block of hours on one day (so a student working two separate blocks on the same day counts as 2 shifts), or does it mean a student can be on duty on at most 2 different days per week?

## Turn 10 - User Simulator

A "shift" means a student can be on duty on at most 2 different days per week.

## Turn 11 - Generic Agent

QUESTION: You mentioned "no more than 3 different students can be scheduled for duty on any single day" — does this mean that on each of the 5 days, at most 3 students can have a positive number of hours, or does it mean something else?

## Turn 11 - User Simulator

Yes, it means that on each of the 5 days, at most 3 students can have a positive number of hours.

## Turn 12 - Generic Agent

QUESTION: Going back to the earlier point about whether hours within a day must be contiguous or can be split into separate blocks — since a "shift" is defined as being on duty on a given day (not a contiguous block), does that mean a student's hours on a day can be split into separate blocks, or must they still be one contiguous block?

## Turn 12 - User Simulator

The available business facts do not specify whether a student's hours within a day must be contiguous or can be split into separate blocks. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Going back to the earlier point about whether hours must be whole 1-hour slots or fractional hours are allowed — since the daily caps in Table 5-9 are all whole numbers and the lab is open 14 hours, is it safe to assume all hours are in whole 1-hour increments?

## Turn 13 - User Simulator

The available business facts do not specify whether hours must be whole 1-hour slots or if fractional hours are allowed. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Regarding the student types (undergraduate vs. graduate) — since this was deferred earlier, could you confirm which of the six students are undergraduates and which are graduate students, or should I treat all six as the same category with a single weekly minimum?

## Turn 14 - User Simulator

The available business facts do not specify which of the six students are undergraduates and which are graduate students. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Since the student types (undergraduate vs. graduate) remain unconfirmed, could you at least confirm whether the weekly minimum is 8 hours for all six students, 7 hours for all six students, or some mix that you'd like me to parameterize so you can fill in the values later?

## Turn 15 - User Simulator

The available business facts do not specify which students are undergraduates and which are graduate students, so the exact mix of 8-hour and 7-hour weekly minimums cannot be confirmed. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Since the student types remain unconfirmed, I'll parameterize the weekly minimum as a per-student value (8 for undergraduates, 7 for graduates) that you can fill in. Is there anything else about the problem structure I should clarify before I proceed to build the model?

## Turn 16 - User Simulator

No, there is nothing else to clarify. The problem structure is fully defined by the facts provided:

- 6 students, 5 days (Mon–Fri), 14 open hours per day.
- Exactly one student on duty at all times (14 hours covered each day).
- Daily maximums per student from Table 5-9 (upper bounds; 0 means unavailable).
- Each student works on at most 2 different days per week.
- At most 3 different students on duty per day.
- Weekly minimums: 8 hours for undergraduates, 7 hours for graduate students (to be parameterized per student).
- Objective: minimize total weekly wage cost.

## Turn 17 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Setting:** A university computer lab open 8:00 AM – 10:00 PM (14 hours) on Monday through Friday. Exactly one student is on duty at all times, so 14 hours must be covered each day.

- **Workers:** 6 students (IDs 1–6), each with an hourly wage and per-day maximum duty hours as given in Table 5-9. A value of 0 means the student is unavailable that day; positive values are upper bounds (the student may work fewer).

- **Decision variables:** For each student *i* and day *d*, the number of hours *x(i,d)* that student works. Hours are treated as continuous (the integrality question was deferred; the model will use continuous variables, which is the natural relaxation and will yield integer optima given the data structure).

- **Objective:** Minimize total weekly wage cost = Σᵢ Σ_d wage(i) · x(i,d).

- **Constraints:**
  1. **Full coverage:** For each day *d*, Σᵢ x(i,d) = 14.
  2. **Daily caps:** x(i,d) ≤ max(i,d) for every student-day (from Table 5-9).
  3. **At most 2 days per student:** For each student *i*, the number of days on which x(i,d) > 0 is at most 2 (modeled with binary indicators y(i,d) and x(i,d) ≤ max(i,d)·y(i,d); Σ_d y(i,d) ≤ 2).
  4. **At most 3 students per day:** For each day *d*, Σᵢ y(i,d) ≤ 3.
  5. **Weekly minimums:** For each student *i*, Σ_d x(i,d) ≥ min_hours(i), where min_hours(i) = 8 if student *i* is an undergraduate, 7 if a graduate. (The undergraduate/graduate assignment is parameterized and to be filled in by the client.)
  6. **Non-negativity:** x(i,d) ≥ 0.

- **Deferred / parameterized items:**
  - Which students are undergraduates vs. graduates (affects the 8 vs. 7 weekly minimum per student).
  - Whether hours must be whole 1-hour slots or fractional (model uses continuous; if integer is required, integrality can be added).
  - Whether a student's hours within a day must be contiguous (not modeled; if required, additional structure would be needed).

I will now formulate the optimization model based on the above.