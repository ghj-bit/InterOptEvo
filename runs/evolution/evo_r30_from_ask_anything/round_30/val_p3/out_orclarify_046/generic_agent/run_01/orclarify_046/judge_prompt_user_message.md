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

QUESTION: Is the objective of this scheduling plan to minimize the total weekly labor cost, or is there a different primary goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The primary goal is to minimize the total weekly labor cost.

## Turn 2 - Generic Agent

QUESTION: Are the decision variables representing the number of hours each student works on each day, or are they binary variables indicating whether a student is on duty during specific time slots within the day?

## Turn 2 - User Simulator

The decision variables represent the number of hours each student works on each day.

## Turn 3 - Generic Agent

QUESTION: Are the daily working hours for each student required to be integer values, or can they be fractional values?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Should the daily working hours for each student be restricted to integer values, or are fractional hours acceptable in the schedule?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the duty schedule, such as limits on the number of days a student can work per week, requirements for consecutive days off, or restrictions on which students can work on specific days?

## Turn 5 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 6 - Generic Agent

QUESTION: Does the constraint that each student can work no more than 2 shifts per week mean that a student can be scheduled on at most 2 distinct days out of the 5 operating days?

## Turn 6 - User Simulator

Yes, a student can be scheduled on at most 2 distinct days out of the 5 operating days.

## Turn 7 - Generic Agent

QUESTION: Does the constraint that no more than 3 different students can be scheduled for duty on any single day mean that at most 3 students can have non-zero hours on that day, or does it refer to something else?

## Turn 7 - User Simulator

Yes, it means that at most 3 students can have non-zero hours on that day.

## Turn 8 - Generic Agent

QUESTION: Does the requirement that there must be one and only one student on duty during open hours mean that the total hours worked by all students on any given day must exactly equal the total number of operating hours for that day?

## Turn 8 - User Simulator

Yes, the total hours worked by all students on any given day must exactly equal the total number of operating hours for that day.

## Turn 9 - Generic Agent

QUESTION: Are the maximum daily hours specified in Table 5-9 hard upper bounds that must not be exceeded, or are they soft targets that can be violated with a penalty?

## Turn 9 - User Simulator

They are hard upper bounds that must not be exceeded.

## Turn 10 - Generic Agent

QUESTION: Are the minimum weekly hours of 8 for undergraduates and 7 for graduates hard lower bounds that must be met, or are they soft targets that can be violated with a penalty?

## Turn 10 - User Simulator

They are hard lower bounds that must be met.

## Turn 11 - Generic Agent

QUESTION: Are all six students in Table 5-9 undergraduate students, or are some of them graduate students?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are students 1 through 6 all undergraduate students, or are some of them graduate students?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is the lab open for the full 14 hours (8:00 AM to 10:00 PM) on all five days from Monday to Friday?

## Turn 13 - User Simulator

Yes, the lab is open for the full 14 hours (8:00 AM to 10:00 PM) on all five days from Monday to Friday.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total weekly labor cost.
2.  **Decision Variables:** $x_{i,d}$ represents the number of hours student $i$ works on day $d$ (where $d \in \{Mon, Tue, Wed, Thu, Fri\}$).
3.  **Variable Domain:** The variables are continuous and non-negative. (Note: Integrality was not confirmed; assumed continuous for now, but if integer hours are required, the model can be adjusted to Integer Linear Programming).
4.  **Operating Hours:** The lab is open for 14 hours each day (8:00 AM to 10:00 PM) from Monday to Friday.
5.  **Coverage Constraint:** For each day $d$, the sum of hours worked by all students must exactly equal 14 hours.
    *   $\sum_{i=1}^{6} x_{i,d} = 14$ for all $d$.
6.  **Daily Maximum Hours:** For each student $i$ and day $d$, $x_{i,d}$ cannot exceed the maximum hours specified in Table 5-9.
    *   $x_{i,d} \le MaxHours_{i,d}$ (from Table 5-9).
    *   Note: If $MaxHours_{i,d} = 0$, then $x_{i,d} = 0$.
7.  **Weekly Minimum Hours:**
    *   **Assumption:** Since the classification of students as undergraduate or graduate was not confirmed, I am assuming **all students are undergraduates** and must work at least 8 hours per week. If some are graduates, their minimum would be 7 hours.
    *   $\sum_{d} x_{i,d} \ge 8$ for all $i$ (assuming all are undergrads).
8.  **Maximum Days Worked:** Each student can work on at most 2 distinct days per week.
    *   This requires binary variables $y_{i,d}$ indicating if student $i$ works on day $d$.
    *   $\sum_{d} y_{i,d} \le 2$ for all $i$.
    *   $x_{i,d} \le M \cdot y_{i,d}$ (where $M$ is a large number, e.g., 14).
9.  **Maximum Students Per Day:** No more than 3 different students can be scheduled on any single day.
    *   $\sum_{i} y_{i,d} \le 3$ for all $d$.
10. **Wages:** The cost is calculated as $\sum_{i,d} Wage_i \cdot x_{i,d}$.

**Open Assumptions:**
*   **Student Classification:** All students are assumed to be undergraduates (minimum 8 hours/week). If any are graduates, their minimum is 7 hours/week.
*   **Integrality:** Hours are assumed to be continuous. If integer hours are required, the model should be treated as a Mixed Integer Linear Program (MILP) with integer constraints on $x_{i,d}$.