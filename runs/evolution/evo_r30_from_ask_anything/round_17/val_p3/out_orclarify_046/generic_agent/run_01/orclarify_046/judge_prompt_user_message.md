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

QUESTION: Is the goal to minimize the total weekly labor cost, or is there another objective such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The goal is to minimize the total weekly labor cost.

## Turn 2 - Generic Agent

QUESTION: Are the maximum duty hours in Table 5-9 expressed in hours (e.g., 6 means 6 hours) or in some other unit like 30-minute slots?

## Turn 2 - User Simulator

The maximum duty hours in Table 5-9 are expressed in hours.

## Turn 3 - Generic Agent

QUESTION: Is the lab open for the full 14 hours from 8:00 AM to 10:00 PM every day from Monday to Friday, or are there specific open hours that differ by day?

## Turn 3 - User Simulator

The lab is open for the full 14 hours from 8:00 AM to 10:00 PM every day from Monday to Friday.

## Turn 4 - Generic Agent

QUESTION: Can a student work multiple separate shifts on the same day, or must their daily hours be a single continuous block?

## Turn 4 - User Simulator

I don't have a specific rule on whether a student's daily hours must be a single continuous block or can be split into multiple shifts. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are there any additional requirements beyond the minimum weekly hours, daily maximums, and one-student-on-duty rule, such as limits on consecutive days worked, required days off, or restrictions on which students can work together?

## Turn 5 - User Simulator

Yes, there are two additional requirements:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty in a single day.

## Turn 6 - Generic Agent

QUESTION: Does the "no more than 2 shifts per week" constraint mean each student can be assigned to at most 2 different days per week, or does it mean each student can have at most 2 separate time blocks per week even if they work on the same day?

## Turn 6 - User Simulator

The "no more than 2 shifts per week" constraint means each student can be assigned to at most 2 different days per week.

## Turn 7 - Generic Agent

QUESTION: Does the "no more than 3 different students can be scheduled for duty in a single day" constraint mean that at most 3 distinct students can have any hours assigned on that day, or does it mean that at most 3 students can be on duty at any single point in time during the day?

## Turn 7 - User Simulator

It means that at most 3 distinct students can have any hours assigned on that day.

## Turn 8 - Generic Agent

QUESTION: Can a student's daily hours be split into multiple separate time blocks within the same day, or must their daily hours be a single continuous block?

## Turn 8 - User Simulator

I don't have a specific rule on whether a student's daily hours must be a single continuous block or can be split into multiple separate time blocks within the same day. That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the decision variable for each student-day a continuous number of hours (allowing any fractional value up to the daily maximum), or must the hours be integer values?

## Turn 9 - User Simulator

I don't have a specific rule on whether the daily hours must be integer values or can be any fractional value up to the daily maximum. That point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the minimum weekly hours (8 for undergraduates, 7 for graduates) hard constraints that must be strictly met, or are they soft targets where violations are allowed but penalized in the objective function?

## Turn 10 - User Simulator

The minimum weekly hours are hard constraints that must be strictly met.

## Turn 11 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 hard constraints that cannot be exceeded, or are they soft targets where exceeding them is allowed but penalized?

## Turn 11 - User Simulator

The daily maximum hours in Table 5-9 are hard constraints that cannot be exceeded.

## Turn 12 - Generic Agent

QUESTION: Are the "no more than 2 shifts per week" and "no more than 3 different students per day" constraints hard constraints that must be strictly satisfied, or are they soft targets where violations are allowed but penalized?

## Turn 12 - User Simulator

Both the "no more than 2 shifts per week" and "no more than 3 different students per day" constraints are hard constraints that must be strictly satisfied.

## Turn 13 - Generic Agent

QUESTION: Which students in the table are undergraduates and which are graduate students?

## Turn 13 - User Simulator

I don't have the specific classification of which students are undergraduates and which are graduate students. That point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Are there any other constraints or requirements I have not yet covered, such as specific days off, maximum consecutive hours, or restrictions on which students can work on specific days?

## Turn 14 - User Simulator

No, there are no other constraints or requirements beyond what has already been covered.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total weekly labor cost.
2.  **Decision Variables:** Let $x_{i,d}$ be the number of hours student $i$ works on day $d$ (where $i \in \{1, \dots, 6\}$ and $d \in \{\text{Mon}, \dots, \text{Fri}\}$).
3.  **Variable Domain:** The domain for $x_{i,d}$ is assumed to be continuous non-negative real numbers ($x_{i,d} \ge 0$). *Assumption: Hours can be fractional.*
4.  **Constraints:**
    *   **Coverage:** For each day $d$, the sum of hours worked by all students must equal 14 hours (8:00 AM to 10:00 PM). $\sum_{i} x_{i,d} = 14$ for all $d$.
    *   **Daily Maximums:** $x_{i,d} \le M_{i,d}$ for all $i, d$, where $M_{i,d}$ is the value from Table 5-9.
    *   **Weekly Minimums:** $\sum_{d} x_{i,d} \ge 8$ for undergraduate students $i$, and $\sum_{d} x_{i,d} \ge 7$ for graduate students $i$. *Assumption: Student classification (undergrad vs. grad) is unknown; this parameter must be provided to finalize the model.*
    *   **Max Days per Week:** Each student can work on at most 2 days per week. This requires binary variables $y_{i,d} \in \{0,1\}$ indicating if student $i$ works on day $d$, with $\sum_{d} y_{i,d} \le 2$ for all $i$, and $x_{i,d} \le M_{i,d} y_{i,d}$.
    *   **Max Students per Day:** At most 3 distinct students can work on any given day. This requires $\sum_{i} y_{i,d} \le 3$ for all $d$.
5.  **Data:**
    *   Wages: $w_i$ as given in Table 5-9.
    *   Max Hours: $M_{i,d}$ as given in Table 5-9.
    *   Open Hours: 14 hours/day, Mon-Fri.

**Explicit Assumptions:**
1.  **Student Classification:** It is assumed that the user will provide which students are undergraduates (min 8 hrs) and which are graduates (min 7 hrs). Without this, the weekly minimum constraints cannot be fully specified.
2.  **Hour Granularity:** It is assumed that hours can be fractional (continuous variables). If integer hours are required, the model would need to be adjusted to an Integer Linear Program.
3.  **Shift Continuity:** It is assumed that a student's hours on a given day do not need to be a single continuous block; they can be split. However, since the coverage constraint is just a sum of hours, and there are no specific shift start/end time constraints, this assumption does not change the algebraic form of the model, only the operational interpretation.
4.  **Feasibility:** It is assumed that a feasible solution exists given the constraints. Note that with only 6 students, each working at most 2 days, and at most 3 students per day, the total capacity is limited. For example, if 3 students work on Monday, they must cover 14 hours. The max hours for any single student on Monday are at most 6 (Student 1). So 3 students can cover at most $6+0+4=10$ hours if we pick the best 3 (Student 1: 6, Student 3: 4, Student 4: 5 -> wait, Student 1 is 6, Student 3 is 4, Student 4 is 5. Sum = 15. So 3 students can cover 14 hours on Monday. But we need to check all days. This feasibility check is part of the modeling process.