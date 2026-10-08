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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours), but the daily maximum hours in Table 5-9 are at most 9 per student, so no single student can cover the whole day. Does "one and only one student on duty" mean exactly one student is assigned to each 1-hour slot (so 14 students total per day, possibly different students in different slots), or does it mean exactly one student is on duty for the entire 14-hour stretch each day?

## Turn 1 - User Simulator

It means exactly one student is on duty for the entire 14-hour stretch each day.

## Turn 2 - Generic Agent

QUESTION: Since no student can work 14 hours in a day (max is 9), the lab cannot have exactly one student on duty for the full 14-hour stretch. Does the lab actually need coverage for all 14 hours, or is the required daily coverage shorter (e.g., a specific number of hours per day that one student can cover)?

## Turn 2 - User Simulator

The lab needs coverage for all 14 hours, from 8:00 AM to 10:00 PM.

## Turn 3 - Generic Agent

QUESTION: Since no single student can work 14 hours in a day, the "one student on duty for the entire 14-hour stretch" requirement is infeasible. Which of these readings should I implement: (A) exactly one student is on duty in each 1-hour slot, with different students allowed in different slots (so 14 student-slots per day), or (B) exactly one student is on duty per day but only for a subset of the 14 hours, with the remaining hours uncovered?

## Turn 3 - User Simulator

The requirement is that exactly one student is on duty in each 1-hour slot, with different students allowed in different slots.

## Turn 4 - Generic Agent

QUESTION: The objective is to minimize total weekly labor cost (sum of wage × hours worked across all students and slots), correct?

## Turn 4 - User Simulator

Yes, the objective is to minimize total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 5 - Generic Agent

QUESTION: The minimum weekly hours (8 for undergraduates, 7 for graduates) are hard constraints that must be met exactly or exceeded, and the model must find a feasible schedule satisfying them, correct?

## Turn 5 - User Simulator

Yes, the minimum weekly hours are hard constraints that must be met or exceeded.

## Turn 6 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students?

## Turn 6 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the undergraduate/graduate split is not yet confirmed, for now should I treat all six students as undergraduates (each requiring at least 8 hours per week) as a placeholder, or would you prefer I treat all six as graduate students (each requiring at least 7 hours per week) as the placeholder?

## Turn 7 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: The daily maximum hours in Table 5-9 are hard upper bounds on how many of the 14 hourly slots a given student can be assigned on that day, correct?

## Turn 8 - User Simulator

Yes, the daily maximum hours in Table 5-9 are hard upper bounds on how many of the 14 hourly slots a given student can be assigned on that day.

## Turn 9 - Generic Agent

QUESTION: A student can be assigned to at most one slot per hour (i.e., a student cannot be on duty in two different slots at the same time), which is naturally satisfied since each slot has exactly one student, but can a student be assigned to consecutive slots (e.g., both 8-9 AM and 9-10 AM) on the same day?

## Turn 9 - User Simulator

Yes, a student can be assigned to consecutive slots on the same day.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how many total hours a student can work across the whole week (beyond the daily maximums and the minimum weekly hours), or is the only weekly constraint the minimum (8 or 7 hours)?

## Turn 10 - User Simulator

There is no additional weekly maximum hours constraint beyond the daily maximums and the minimum weekly hours.

## Turn 11 - Generic Agent

QUESTION: The schedule only covers Monday through Friday (5 days), with no weekend shifts, correct?

## Turn 11 - User Simulator

Yes, the schedule only covers Monday through Friday.

## Turn 12 - Generic Agent

QUESTION: The undergraduate/graduate split is still pending internal confirmation. As a placeholder for now, should I treat all six students as undergraduates (each requiring at least 8 hours per week)?

## Turn 12 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: As a final placeholder for the pending undergraduate/graduate split, should I treat all six students as undergraduates (each requiring at least 8 hours per week) so I can proceed with modeling?

## Turn 13 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 14 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Scope:** One-week duty schedule for a university computer lab, Monday through Friday only (no weekends).
- **Operating hours:** 8:00 AM to 10:00 PM each day = 14 one-hour slots per day (slots 1–14).
- **Coverage rule:** Exactly one student is on duty in each 1-hour slot. Different students may be assigned to different slots on the same day. A student may be assigned to consecutive slots.
- **Decision variables:** For each student i and each day d and each slot t, a binary variable x[i,d,t] = 1 if student i is on duty in slot t on day d.
- **Objective:** Minimize total weekly labor cost = Σ (wage_i × total hours worked by student i over the week).
- **Daily maximum constraint:** For each student i and day d, the number of slots assigned to i on day d ≤ the daily maximum from Table 5-9 (a hard upper bound).
- **Minimum weekly hours constraint:** Each student must work at least a minimum number of hours per week. The undergraduate/graduate split (8 hours for undergrads, 7 hours for grads) is **pending internal confirmation**; as a placeholder I will treat all six students as undergraduates requiring at least 8 hours per week. This is a hard constraint (must be met or exceeded).
- **No other weekly maximum** beyond the daily caps and the minimum.
- **Wages:** As given in Table 5-9 (CNY/hour).

The only open item is the undergraduate/graduate classification, which will be incorporated once confirmed.