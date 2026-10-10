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

QUESTION: Is the lab's open hours (8:00 AM to 10:00 PM) a single continuous block of 14 hours each day, or are there breaks or sub-periods during the day that affect how duty hours are counted?

## Turn 1 - User Simulator

The lab's open hours from 8:00 AM to 10:00 PM are a single continuous block of 14 hours each day. There are no breaks or sub-periods that affect how duty hours are counted.

## Turn 2 - Generic Agent

QUESTION: Is the objective to minimize the total weekly labor cost (sum of wage times hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 2 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked during the week.

## Turn 3 - Generic Agent

QUESTION: Are the decision variables continuous (allowing fractional hours like 2.5 hours) or must they be integer values (whole hours only)?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Should the scheduling model allow fractional hours (e.g., 2.5 hours) or require whole-hour increments for each student's daily duty?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the "one and only one student on duty" requirement a strict constraint that exactly one student must be assigned to cover the entire 14-hour block each day, or is it a soft target that allows for some flexibility in coverage?

## Turn 5 - User Simulator

It is a strict constraint: exactly one student must be on duty during open hours.

## Turn 6 - Generic Agent

QUESTION: Does the "exactly one student on duty" constraint mean that one student works the full 14-hour block each day, or does it mean that the sum of hours worked by all students on a given day must equal exactly 14 hours (allowing multiple students to split the day)?

## Turn 6 - User Simulator

It means that the sum of hours worked by all students on a given day must equal exactly 14 hours, allowing multiple students to split the day.

## Turn 7 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 hard upper bounds that cannot be exceeded, or are they soft targets that can be violated with a penalty?

## Turn 7 - User Simulator

They are hard upper bounds that cannot be exceeded.

## Turn 8 - Generic Agent

QUESTION: Are the weekly minimum hours (8 hours for undergraduates, 7 hours for graduates) hard lower bounds that must be met, or are they soft targets that can be violated with a penalty?

## Turn 8 - User Simulator

They are hard lower bounds that must be met.

## Turn 9 - Generic Agent

QUESTION: Which students in the table are undergraduates and which are graduate students, so that the correct weekly minimum (8 hours or 7 hours) can be applied to each?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are all six students in the table undergraduates, all six are graduate students, or is there a specific split between the two groups?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is the lab open only on Monday through Friday, or are there additional days (such as weekends) that require coverage?

## Turn 11 - User Simulator

The lab is open only on Monday through Friday.

## Turn 12 - Generic Agent

QUESTION: Are there any constraints on the number of days per week a student can work, or can a student work on any subset of the five days as long as their daily hours do not exceed the table limits and their weekly total meets the minimum?

## Turn 12 - User Simulator

There is a constraint: each student can work no more than 2 shifts per week.

## Turn 13 - Generic Agent

QUESTION: Does the "no more than 2 shifts per week" constraint mean a student can work on at most 2 distinct days, or does it mean a student can work at most 2 total shifts regardless of how many days they span?

## Turn 13 - User Simulator

It means a student can work on at most 2 distinct days per week.

## Turn 14 - Generic Agent

QUESTION: Is the "at most 2 distinct days per week" constraint a hard limit that cannot be exceeded, or is it a soft target that can be violated with a penalty?

## Turn 14 - User Simulator

It is a hard limit that cannot be exceeded.

## Turn 15 - Generic Agent

QUESTION: Are the decision variables continuous (allowing fractional hours like 2.5 hours) or must they be integer values (whole hours only)?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Are the decision variables continuous (allowing fractional hours like 2.5 hours) or must they be integer values (whole hours only)?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is the "at most 2 distinct days per week" constraint applied to all students, or only to specific groups such as undergraduates or graduate students?

## Turn 17 - User Simulator

It is applied to all students.

## Turn 18 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total weekly labor cost (sum of wage × hours for all students).
2.  **Time Horizon:** Monday through Friday only.
3.  **Daily Coverage:** The lab is open 8:00 AM to 10:00 PM (14 hours) each day. The sum of hours worked by all students on any given day must equal exactly 14 hours.
4.  **Decision Variables:** Let $x_{i,d}$ be the hours student $i$ works on day $d$.
5.  **Variable Domain:** **Assumed Continuous.** (The user did not confirm integrality; fractional hours are allowed unless specified otherwise in standard LP formulations for this type of problem).
6.  **Daily Maximum Constraints:** For each student $i$ and day $d$, $x_{i,d} \leq M_{i,d}$, where $M_{i,d}$ is the value from Table 5-9. These are hard upper bounds.
7.  **Weekly Minimum Constraints:**
    *   **Assumed Grouping:** Since the user did not specify which students are undergraduates vs. graduates, it is **assumed** that all students are subject to the same minimum, or that the distinction does not change the model structure if we apply the stricter minimum (8 hours) to all, or the looser (7 hours) to all. *However, typically in such problems, if not specified, one might assume a split or apply the minimum to all. Given the ambiguity, I will list this as an open assumption.*
    *   **Constraint Form:** For each student $i$, $\sum_{d=1}^{5} x_{i,d} \geq L_i$, where $L_i$ is 8 if undergraduate, 7 if graduate.
8.  **Shift Limit Constraint:** Each student can work on at most 2 distinct days per week. This is a hard constraint. This requires binary variables $y_{i,d}$ indicating if student $i$ works on day $d$, with $\sum_{d} y_{i,d} \leq 2$ and $x_{i,d} \leq M_{i,d} y_{i,d}$.
9.  **Non-negativity:** $x_{i,d} \geq 0$.

**Open Assumptions:**
1.  **Variable Domain:** Assumed continuous (fractional hours allowed).
2.  **Student Classification:** It is assumed that the weekly minimum hours (8 vs 7) apply based on a classification that was not provided. If the classification is unknown, the model cannot be fully instantiated without knowing which students get 8h and which get 7h. *Note: If the user intended all to be the same, the minimum would be uniform. If mixed, the specific IDs are needed.*
3.  **Feasibility:** It is assumed that a feasible solution exists given the hard constraints (14h/day coverage, max 2 days/student, daily caps, weekly mins).