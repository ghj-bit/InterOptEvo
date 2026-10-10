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

QUESTION: Is the objective to minimize the total weekly labor cost (sum of each student's hours multiplied by their hourly wage), or is there a different goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hours multiplied by their hourly wage.

## Turn 2 - Generic Agent

QUESTION: Are the decision variables the number of hours each student works on each day, and are these variables continuous (allowing fractional hours) or must they be integers?

## Turn 2 - User Simulator

The decision variables are the number of hours each student works on each day. These variables must be integers.

## Turn 3 - Generic Agent

QUESTION: Is the requirement that exactly one student is on duty at all times during the 8:00 AM to 10:00 PM window equivalent to requiring that the sum of all students' hours on any given day equals exactly 14 hours?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Are the weekly minimum hour requirements (8 hours for undergraduates and 7 hours for graduates) hard constraints that must be strictly satisfied, or are they soft targets that can be violated with a penalty?

## Turn 4 - User Simulator

They are hard constraints that must be strictly satisfied.

## Turn 5 - Generic Agent

QUESTION: Are the maximum daily hours in Table 5-9 hard constraints that must be strictly respected, or are they soft targets that can be exceeded with a penalty?

## Turn 5 - User Simulator

They are hard constraints that must be strictly respected.

## Turn 6 - Generic Agent

QUESTION: Which student IDs correspond to undergraduate students and which correspond to graduate students?

## Turn 6 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the specific undergraduate/graduate classification is not available, should I assume that all six students are undergraduates requiring at least 8 hours per week, or should I assume a different split such as students 1-3 being undergraduates and students 4-6 being graduates?

## Turn 7 - User Simulator

I cannot confirm either assumption. The specific undergraduate/graduate classification for each student still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are there any additional constraints or requirements not yet mentioned, such as limits on the number of days a student can work per week, requirements for specific students to be available on specific days, or rules about consecutive days off?

## Turn 8 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 9 - Generic Agent

QUESTION: Does the constraint that each student can work no more than 2 shifts per week mean that a student can only be assigned to work on at most 2 distinct days out of the 5 days (Monday through Friday)?

## Turn 9 - User Simulator

Yes, that is correct.

## Turn 10 - Generic Agent

QUESTION: Does the constraint that no more than 3 students can be scheduled for duty each day mean that on any given day, at most 3 students can have a positive number of hours assigned?

## Turn 10 - User Simulator

Yes, that is correct.

## Turn 11 - Generic Agent

QUESTION: Is the "no more than 2 shifts per week" constraint a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 11 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 12 - Generic Agent

QUESTION: Is the "no more than 3 students per day" constraint a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 12 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Minimize total weekly labor cost (sum of hours worked by each student multiplied by their hourly wage).
2.  **Decision Variables:** Integer hours worked by each student on each day (Monday–Friday).
3.  **Coverage Constraint:** The sum of hours worked by all students on any given day must equal exactly 14 hours (8:00 AM to 10:00 PM).
4.  **Daily Max Hours:** Each student's hours on a specific day cannot exceed the maximum specified in Table 5-9. This is a hard constraint.
5.  **Weekly Min Hours:** Each student must work at least a minimum number of hours per week. This is a hard constraint.
    *   *Note:* The specific minimum (8 hours for undergrads, 7 hours for grads) depends on the student's classification.
6.  **Max Days per Week:** Each student can work on at most 2 distinct days per week. This is a hard constraint.
7.  **Max Students per Day:** On any given day, at most 3 students can have a positive number of hours assigned. This is a hard constraint.
8.  **Data:** Wages and daily maximum hours are provided in Table 5-9 for 6 students over 5 days.

**Open Assumptions:**
1.  **Student Classification:** The specific classification of each student as undergraduate or graduate is **not confirmed**.
    *   *Impact:* This determines whether the weekly minimum for a specific student is 8 hours or 7 hours.
    *   *Action:* The model formulation will include a parameter $minHours_i$ for each student $i$. To solve the model, you must provide the value for each student (either 8 or 7). If you cannot provide this, the model cannot be solved to a specific optimal schedule, but the structure is ready.

**Model Structure Summary:**
*   **Sets:** Students $i \in \{1..6\}$, Days $d \in \{Mon..Fri\}$.
*   **Parameters:**
    *   $wage_i$: Hourly wage for student $i$.
    *   $maxHrs_{i,d}$: Maximum hours student $i$ can work on day $d$ (from Table 5-9).
    *   $minHrs_i$: Minimum weekly hours for student $i$ (8 or 7, pending classification).
    *   $TotalDailyHrs = 14$.
*   **Variables:**
    *   $x_{i,d} \in \mathbb{Z}_{\ge 0}$: Hours student $i$ works on day $d$.
    *   $y_{i,d} \in \{0, 1\}$: Binary variable indicating if student $i$ works on day $d$ (1 if $x_{i,d} > 0$, 0 otherwise).
*   **Objective:** Minimize $\sum_{i} \sum_{d} wage_i \cdot x_{i,d}$.
*   **Constraints:**
    1.  **Daily Coverage:** $\sum_{i} x_{i,d} = 14$ for all $d$.
    2.  **Daily Max Hours:** $x_{i,d} \le maxHrs_{i,d}$ for all $i, d$.
    3.  **Weekly Min Hours:** $\sum_{d} x_{i,d} \ge minHrs_i$ for all $i$.
    4.  **Max Days per Week:** $\sum_{d} y_{i,d} \le 2$ for all $i$.
    5.  **Max Students per Day:** $\sum_{i} y_{i,d} \le 3$ for all $d$.
    6.  **Linking Constraint:** $x_{i,d} \le M \cdot y_{i,d}$ for all $i, d$ (where $M$ is a large constant, e.g., 14, to ensure $y_{i,d}=1$ if $x_{i,d}>0$).