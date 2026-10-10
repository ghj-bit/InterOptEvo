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

QUESTION: What is the total number of hours the lab is open each day that a student must be on duty, for example is it the full 14 hours from 8:00 AM to 10:00 PM every day?

## Turn 1 - User Simulator

Yes, the lab is open for the full 14 hours each day, from 8:00 AM to 10:00 PM, and a student must be on duty for the entire duration.

## Turn 2 - Generic Agent

QUESTION: Are the maximum duty hours in Table 5-9 the only upper limits on how many hours a student can work on a given day, or are there also minimum hours a student must work on a day if they are scheduled at all?

## Turn 2 - User Simulator

The maximum duty hours in Table 5-9 are the only upper limits on how many hours a student can work on a given day. There are no minimum hours a student must work on a specific day if they are scheduled.

## Turn 3 - Generic Agent

QUESTION: Is the goal of the scheduling plan to minimize the total weekly wage cost paid to the students, or is there a different objective such as maximizing fairness or minimizing the number of students used?

## Turn 3 - User Simulator

The goal is to minimize the total weekly wage cost paid to the students.

## Turn 4 - Generic Agent

QUESTION: Are the weekly minimum requirements of at least 8 hours for each undergraduate and at least 7 hours for each graduate student hard constraints that must be satisfied for every student, or are they targets that can be violated if necessary?

## Turn 4 - User Simulator

They are hard constraints that must be satisfied for every student.

## Turn 5 - Generic Agent

QUESTION: Which of the six students in Table 5-9 are undergraduates and which are graduate students?

## Turn 5 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the undergraduate versus graduate classification is not provided, should I assume all six students are undergraduates requiring at least 8 hours per week, or should I treat the classification as an open assumption to be flagged in the final summary?

## Turn 6 - User Simulator

Treat the classification as an open assumption to be flagged in the final summary.

## Turn 7 - Generic Agent

QUESTION: Are the working hours for each student on each day required to be whole numbers of hours, or can they be fractional values?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Should I assume that working hours for each student on each day must be whole numbers, or can they be fractional values?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements for the duty scheduling plan that I have not yet covered, such as limits on consecutive days worked or specific days off?

## Turn 9 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 10 - Generic Agent

QUESTION: Does the constraint that each student can work no more than 2 shifts per week mean that a student can be on duty on at most 2 different days out of the 5 days, or does it mean something else?

## Turn 10 - User Simulator

It means a student can be on duty on at most 2 different days out of the 5 days.

## Turn 11 - Generic Agent

QUESTION: Does the constraint that no more than 3 different students can be scheduled for duty on any single day mean that at most 3 students can have non-zero hours on that day, or does it refer to something else?

## Turn 11 - User Simulator

It means that at most 3 students can have non-zero hours on that day.

## Turn 12 - Generic Agent

QUESTION: Are there any other constraints or requirements for the duty scheduling plan that I have not yet covered?

## Turn 12 - User Simulator

No, all constraints and requirements have been covered.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize the total weekly wage cost.
2.  **Decision Variables:** Let $x_{i,d}$ be the number of hours student $i$ works on day $d$ (where $i \in \{1, \dots, 6\}$ and $d \in \{\text{Mon}, \dots, \text{Fri}\}$).
3.  **Time Horizon:** Monday through Friday.
4.  **Daily Coverage Constraint:** The lab is open for 14 hours each day (8:00 AM to 10:00 PM). Exactly one student must be on duty for the entire duration. This implies that for each day $d$, the sum of hours worked by all students must equal 14: $\sum_{i=1}^{6} x_{i,d} = 14$.
5.  **Daily Maximum Hours Constraint:** For each student $i$ and day $d$, $x_{i,d} \le M_{i,d}$, where $M_{i,d}$ is the value from Table 5-9.
6.  **Weekly Minimum Hours Constraint:**
    *   Undergraduates: $\sum_{d} x_{i,d} \ge 8$.
    *   Graduate Students: $\sum_{d} x_{i,d} \ge 7$.
    *   *Note:* The specific classification of which students are undergraduates vs. graduates is **not provided**.
7.  **Shift Limit Constraint:** Each student can work on at most 2 different days per week. This implies that for each student $i$, the number of days $d$ where $x_{i,d} > 0$ is $\le 2$.
8.  **Daily Student Limit Constraint:** On any single day $d$, at most 3 different students can have non-zero hours. This implies that for each day $d$, the number of students $i$ where $x_{i,d} > 0$ is $\le 3$.
9.  **Wages:** The hourly wage for each student is given in Table 5-9.

**Open Assumptions:**

1.  **Student Classification:** It is assumed that the distinction between undergraduate and graduate students is unknown. To proceed with a model, one would typically need to assign a classification to each student. Without this, the weekly minimum constraints cannot be fully specified. A common assumption in such missing-data scenarios might be to treat all as one category (e.g., all undergrads requiring 8 hours) or to parameterize the minimums, but this is an **open assumption** that needs resolution for a specific numerical solution.
2.  **Integrality of Hours:** It is assumed that working hours $x_{i,d}$ can be continuous (fractional) values, as no explicit integrality constraint was confirmed. If hours must be integers, the model would change to an Integer Linear Program.
3.  **Feasibility:** The combination of constraints (14 hours/day coverage, max 3 students/day, max 2 days/student, daily max hours) may make the problem infeasible for certain student classifications or if the daily max hours are too low. For example, if a student has a max of 0 hours on a day, they cannot work that day. The model will determine if a feasible schedule exists.