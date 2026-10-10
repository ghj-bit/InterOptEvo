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

QUESTION: Is the lab open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday through Friday, or are there specific open hours on certain days that differ from this range?

## Turn 1 - User Simulator

The lab is open for the full 14 hours, from 8:00 AM to 10:00 PM, every day from Monday through Friday.

## Turn 2 - Generic Agent

QUESTION: Is the objective to minimize the total weekly labor cost (sum of wage times hours worked for all students), or is there a different goal such as maximizing fairness or minimizing total hours worked?

## Turn 2 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage times their total hours worked that week.

## Turn 3 - Generic Agent

QUESTION: Are the maximum duty hours in Table 5-9 (e.g., Student 1 has 6 hours on Monday) hard upper limits that cannot be exceeded, or are they soft targets that can be violated with a penalty?

## Turn 3 - User Simulator

The maximum duty hours in Table 5-9 are hard upper limits that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Are the minimum weekly hours (8 hours for undergraduates, 7 hours for graduates) hard lower bounds that must be met, or are they soft targets that can be missed with a penalty?

## Turn 4 - User Simulator

The minimum weekly hours are hard lower bounds that must be met.

## Turn 5 - Generic Agent

QUESTION: Which students are undergraduates and which are graduates, since the minimum weekly hours differ between the two groups?

## Turn 5 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is unconfirmed, should I assume all six students are undergraduates requiring at least 8 hours per week, or should I assume all six are graduates requiring at least 7 hours per week?

## Turn 6 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the decision variable the number of hours each student works on each day (continuous values allowed), or must hours be assigned in discrete blocks such as whole hours or half-hours?

## Turn 7 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is the requirement for "one and only one student on duty" a hard constraint that must be satisfied for every hour of the 14-hour operating window each day, or is it a soft target that can be violated with a penalty?

## Turn 8 - User Simulator

The requirement for one and only one student on duty is a hard constraint that must be satisfied for every hour of the 14-hour operating window each day.

## Turn 9 - Generic Agent

QUESTION: Can a student work multiple non-consecutive blocks of time on the same day (e.g., 2 hours in the morning and 3 hours in the afternoon), or must their daily hours be a single continuous block?

## Turn 9 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or requirements for the scheduling plan that have not been mentioned, such as maximum consecutive days worked, required days off, or preferences for specific students on specific days?

## Turn 10 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 11 - Generic Agent

QUESTION: Does "no more than 2 shifts per week" mean a student can be assigned to work on at most 2 distinct days out of the 5 operating days, or does it mean something else?

## Turn 11 - User Simulator

It means a student can be assigned to work on at most 2 distinct days out of the 5 operating days.

## Turn 12 - Generic Agent

QUESTION: Does "no more than 3 students can be scheduled for duty each day" mean that at most 3 students can have any hours assigned on a given day, or does it mean that at most 3 students can be on duty at any single hour?

## Turn 12 - User Simulator

It means that at most 3 students can have any hours assigned on a given day.

## Turn 13 - Generic Agent

QUESTION: Is there a maximum number of hours any single student can work in total per week, or is the only weekly limit the minimum hours requirement?

## Turn 13 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there a maximum number of hours any single student can work in total per week, or is the only weekly limit the minimum hours requirement?

## Turn 14 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Minimize total weekly labor cost (sum of wage × hours for all students).
2.  **Operating Hours:** The lab is open 14 hours/day (8:00 AM – 10:00 PM) from Monday to Friday.
3.  **Coverage Constraint:** Exactly one student must be on duty for every hour of the 14-hour window each day.
4.  **Daily Max Hours:** Each student’s hours on a specific day cannot exceed the values in Table 5-9 (hard upper limits).
5.  **Weekly Min Hours:** Each student must work at least a minimum number of hours per week (hard lower bound).
6.  **Max Days Worked:** Each student can work on at most 2 distinct days per week.
7.  **Max Students per Day:** At most 3 students can have any hours assigned on a given day.

**Assumptions (due to lack of confirmation):**
1.  **Student Classification:** It is assumed that **all six students are undergraduates**, requiring a minimum of **8 hours** per week. (If any are graduates, their minimum would be 7 hours, but without classification, the stricter 8-hour bound is applied to all to ensure feasibility for both groups if the distinction is later clarified, or this assumption should be updated if the user provides the split).
2.  **Variable Domain:** Hours are treated as **continuous** variables (e.g., a student can work 3.5 hours).
3.  **Shift Continuity:** A student’s daily hours can be **non-consecutive** (e.g., split shifts are allowed).
4.  **Weekly Max Hours:** There is **no maximum** total weekly hours limit beyond the sum of the daily maximums in Table 5-9.