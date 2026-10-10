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

QUESTION: Is the objective to minimize the total weekly labor cost (sum of wage times hours for all students), or is there a different primary goal such as maximizing fairness or minimizing total hours worked?

## Turn 2 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked during the week.

## Turn 3 - Generic Agent

QUESTION: Are the maximum daily hours in Table 5-9 hard upper limits that cannot be exceeded, or are they soft targets that can be violated with a penalty?

## Turn 3 - User Simulator

The maximum daily hours in Table 5-9 are hard upper limits that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Are the minimum weekly hours (8 for undergraduates, 7 for graduates) hard lower bounds that must be met exactly or at least, or are they soft targets that can be violated with a penalty?

## Turn 4 - User Simulator

The minimum weekly hours are hard lower bounds that must be met at least.

## Turn 5 - Generic Agent

QUESTION: Which student IDs in the table are undergraduates and which are graduate students?

## Turn 5 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are the decision variables for student hours continuous (allowing fractional hours like 2.5 hours) or must they be integer values (whole hours only)?

## Turn 6 - User Simulator

I don't have that information in the supplied business facts. The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any additional constraints or requirements not mentioned in the brief, such as limits on the number of days a student can work, requirements for specific students to cover certain time slots, or restrictions on consecutive days off?

## Turn 7 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 8 - Generic Agent

QUESTION: Does the constraint "each student can work no more than 2 shifts per week" mean that a student can be scheduled on at most 2 distinct days out of the 5 days (Monday-Friday), or does it mean something else?

## Turn 8 - User Simulator

It means a student can be scheduled on at most 2 distinct days out of the 5 days (Monday–Friday).

## Turn 9 - Generic Agent

QUESTION: Does the constraint "no more than 3 different students can be scheduled for duty on any single day" mean that at most 3 students can have non-zero hours on a given day, or does it mean something else?

## Turn 9 - User Simulator

It means that at most 3 students can have non-zero hours on a given day.

## Turn 10 - Generic Agent

QUESTION: Is the constraint "no more than 3 different students can be scheduled for duty on any single day" a hard limit that cannot be exceeded, or is it a soft target that can be violated with a penalty?

## Turn 10 - User Simulator

It is a hard limit that cannot be exceeded.

## Turn 11 - Generic Agent

QUESTION: Is the constraint "each student can work no more than 2 shifts per week" a hard limit that cannot be exceeded, or is it a soft target that can be violated with a penalty?

## Turn 11 - User Simulator

It is a hard limit that cannot be exceeded.

## Turn 12 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as specific time slot coverage requirements, minimum hours per shift, or restrictions on which students can work together?

## Turn 12 - User Simulator

No, there are no other constraints or requirements beyond those already discussed.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total weekly labor cost, calculated as the sum of (hourly wage × hours worked) for all students.
2.  **Time Horizon:** Monday through Friday, 5 days total.
3.  **Daily Operation:** The lab is open 14 hours each day (8:00 AM to 10:00 PM).
4.  **Coverage Requirement:** Exactly one student must be on duty for the entire 14-hour duration each day. This implies that for each day, the sum of hours worked by all students must equal 14.
5.  **Decision Variables:** Let $x_{i,d}$ be the number of hours student $i$ works on day $d$.
    *   *Assumption:* Hours are continuous (fractional hours allowed).
6.  **Student Classification:**
    *   *Assumption:* Since the specific undergraduate/graduate status was not provided, I will assume all students are subject to the same minimum weekly hours constraint for the sake of formulation, or you will need to specify which IDs are which. However, based on the prompt's distinction, I will treat the minimums as:
        *   Undergraduates: $\ge 8$ hours/week.
        *   Graduates: $\ge 7$ hours/week.
        *   *Note:* Without knowing who is who, I cannot apply the specific 8 vs 7 distinction. I will assume for the model structure that you will map the IDs to these categories. If forced to choose, I will assume all are undergraduates (8 hours) as the stricter constraint, or you must provide the mapping. *Correction:* I will list this as an open assumption.
7.  **Constraints:**
    *   **Daily Coverage:** For each day $d \in \{Mon, Tue, Wed, Thu, Fri\}$, $\sum_{i=1}^{6} x_{i,d} = 14$.
    *   **Daily Max Hours:** For each student $i$ and day $d$, $x_{i,d} \le M_{i,d}$, where $M_{i,d}$ is the value from Table 5-9.
    *   **Weekly Min Hours:**
        *   If student $i$ is an undergraduate: $\sum_{d} x_{i,d} \ge 8$.
        *   If student $i$ is a graduate: $\sum_{d} x_{i,d} \ge 7$.
    *   **Max Days Worked:** Each student can work on at most 2 distinct days. This requires binary variables $y_{i,d}$ indicating if student $i$ works on day $d$.
        *   $\sum_{d} y_{i,d} \le 2$ for all $i$.
        *   $x_{i,d} \le M_{i,d} \cdot y_{i,d}$ (If $y_{i,d}=0$, then $x_{i,d}=0$).
    *   **Max Students Per Day:** At most 3 students can work on any single day.
        *   $\sum_{i} y_{i,d} \le 3$ for all $d$.
    *   **Non-negativity:** $x_{i,d} \ge 0$.

**Open Assumptions:**
1.  **Student Classification:** It is assumed that the user will provide the mapping of which Student IDs are undergraduates (min 8 hrs) and which are graduates (min 7 hrs). If not provided, the model cannot strictly enforce the different minimums.
2.  **Variable Domain:** It is assumed that hours ($x_{i,d}$) are continuous variables. If integer hours are required, the model would need to be adjusted to an Integer Linear Program (ILP) with integer constraints on $x_{i,d}$.