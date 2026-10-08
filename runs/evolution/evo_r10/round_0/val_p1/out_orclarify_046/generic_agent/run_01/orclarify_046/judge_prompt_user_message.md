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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours), but the daily maximum hours in Table 5-9 are at most 9, so no single student can cover the whole day — does "one and only one student on duty" mean exactly one student is assigned to each hour slot (so 14 different students must be scheduled per day, one per hour), or does it mean exactly one student is on duty for the entire day (which would make the problem infeasible as stated)?

## Turn 1 - User Simulator

It means exactly one student is on duty for each hour slot. So, for each of the 14 hours the lab is open, one student is assigned to cover that specific hour.

## Turn 2 - Generic Agent

QUESTION: The weekly minimums (8 hours for undergraduates, 7 for graduates) are stated per student, but the table doesn't say which students are undergraduates and which are graduates — can you tell me which of students 1–6 are undergraduates and which are graduates?

## Turn 2 - User Simulator

Students 1, 2, and 3 are undergraduates. Students 4, 5, and 6 are graduates.

## Turn 3 - Generic Agent

QUESTION: The objective is to minimize total weekly wage cost, right?

## Turn 3 - User Simulator

Yes, the objective is to minimize the total weekly wage cost.

## Turn 4 - Generic Agent

QUESTION: A student's daily hours are capped by Table 5-9, but is there also a per-day minimum (e.g., if a student works on a given day they must work at least some number of hours), or can a student work any number of hours from 0 up to that day's maximum?

## Turn 4 - User Simulator

There is no per-day minimum. A student can work any number of hours from 0 up to that day's maximum specified in Table 5-9.

## Turn 5 - Generic Agent

QUESTION: Can a student's hours on a given day be any integer number of hours from 0 up to that day's maximum (e.g., student 1 could work 3 hours on Monday), or must a student either work the full maximum for that day or not work at all?

## Turn 5 - User Simulator

A student's hours on a given day can be any integer number of hours from 0 up to that day's maximum.

## Turn 6 - Generic Agent

QUESTION: Since exactly one student covers each of the 14 hours per day, the total hours worked per day is 14 — is there any additional constraint that a student cannot work two consecutive hours (i.e., must have a break between shifts), or can a student cover any set of hours up to their daily maximum including consecutive ones?

## Turn 6 - User Simulator

There is no constraint requiring a break between hours. A student can cover any set of hours up to their daily maximum, including consecutive ones.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how many days per week a single student can work, or can a student work on all five days (Monday through Friday) as long as their daily hours stay within the Table 5-9 caps and their weekly total meets the minimum?

## Turn 7 - User Simulator

There is a limit: each student can work no more than 2 shifts per week.

## Turn 8 - Generic Agent

QUESTION: When you say each student can work no more than 2 shifts per week, does "shift" mean a day on which the student works at least one hour (so a student can work on at most 2 of the 5 days), or does it mean something else?

## Turn 8 - User Simulator

"Shift" means a day on which the student works at least one hour. So a student can work on at most 2 of the 5 days.

## Turn 9 - Generic Agent

QUESTION: With each student limited to at most 2 days per week, the maximum total weekly hours is 6 students × 2 days × 9 max hours = 108 hours, but the lab needs 14 hours/day × 5 days = 70 hours — is there any other constraint I'm missing, or is the problem simply to find the minimum-cost assignment satisfying all the stated constraints (one student per hour, daily caps, weekly minimums, max 2 days per student)?

## Turn 9 - User Simulator

There is one additional constraint: no more than 3 different students can be scheduled for duty on any single day.

## Turn 10 - Generic Agent

QUESTION: With at most 3 students per day and each student capped at 9 hours max, the maximum hours 3 students can cover in one day is at most 27, but we need exactly 14 — is the "no more than 3 different students per day" constraint a hard requirement, or is it a soft preference that can be relaxed if needed for feasibility?

## Turn 10 - User Simulator

It is a hard requirement.

## Turn 11 - Generic Agent

QUESTION: Since each student can work at most 2 days per week and at most 3 students can work per day, the maximum total weekly hours is 6 students × 2 days × 9 hours = 108, but we need 70 hours total — is there any flexibility in the weekly minimums (8 hours for undergrads, 7 for grads) that could be relaxed if the problem turns out infeasible, or are those also hard requirements?

## Turn 11 - User Simulator

The weekly minimums are hard requirements.

## Turn 12 - Generic Agent

QUESTION: I want to confirm the full set of constraints before I model: (1) exactly one student per hour slot, 14 hours/day × 5 days; (2) each student's daily hours ≤ Table 5-9 cap; (3) undergrads (1,2,3) ≥ 8 hrs/week, grads (4,5,6) ≥ 7 hrs/week; (4) each student works at most 2 days/week; (5) at most 3 different students per day; (6) minimize total wage cost. Is that the complete list, or is there anything else?

## Turn 12 - User Simulator

That is the complete list of constraints and the objective.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Setting:** A university computer lab open 8:00 AM–10:00 PM (14 hour-slots) on Monday–Friday. Exactly one student is assigned to each hour-slot.
- **Students:** 6 students. Students 1, 2, 3 are undergraduates; students 4, 5, 6 are graduates.
- **Decision variables:** For each student, each day, and each of the 14 hour-slots, whether that student covers that slot (binary). Equivalently, integer hours per student per day.
- **Constraints:**
  1. **Coverage:** For each day and each of the 14 hour-slots, exactly one student is assigned.
  2. **Daily caps:** Each student's hours on a given day ≤ the maximum in Table 5-9 (e.g., student 1: Mon ≤ 6, Tue ≤ 0, Wed ≤ 6, Thu ≤ 0, Fri ≤ 7).
  3. **Weekly minimums:** Students 1–3 (undergrads) work ≥ 8 hours/week; students 4–6 (grads) work ≥ 7 hours/week.
  4. **Max days per student:** Each student works on at most 2 of the 5 days (a "shift" = a day with ≥ 1 hour).
  5. **Max students per day:** At most 3 different students are scheduled on any single day.
  6. **No per-day minimum:** A student can work 0 up to the daily cap on any day.
  7. **No break constraint:** A student may cover consecutive hours.
- **Objective:** Minimize total weekly wage cost (wage per hour × hours worked, summed over all students and days).
- **All constraints are hard requirements.**