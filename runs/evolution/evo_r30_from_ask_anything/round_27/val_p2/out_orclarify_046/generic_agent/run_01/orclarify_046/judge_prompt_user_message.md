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

QUESTION: What is the objective of the scheduling plan: minimize total weekly labor cost, minimize total hours worked, or something else?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost.

## Turn 2 - Generic Agent

QUESTION: Are the student duty hours on each day required to be whole numbers of hours, or can they be fractional values?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the daily maximum hours in Table 5-9, does a value of 0 mean the student is completely unavailable on that day, or does it mean they can work up to 0 hours (i.e., unavailable)?

## Turn 3 - User Simulator

A value of 0 means the student is completely unavailable on that day.

## Turn 4 - Generic Agent

QUESTION: Does the lab require exactly one student on duty for every hour from 8:00 AM to 10:00 PM, or is it sufficient to have at least one student on duty during open hours?

## Turn 4 - User Simulator

The lab requires exactly one student on duty for every hour from 8:00 AM to 10:00 PM.

## Turn 5 - Generic Agent

QUESTION: Can a student work multiple non-consecutive blocks of hours on the same day, or must their daily duty be a single continuous block?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are the minimum weekly hours (8 for undergraduates, 7 for graduates) hard constraints that must be met, or are they soft targets that can be violated with a penalty?

## Turn 6 - User Simulator

They are hard constraints that must be met.

## Turn 7 - Generic Agent

QUESTION: Which students in the table are undergraduates and which are graduate students?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum number of hours any single student can work in total per week, or is the only weekly limit the minimum requirement?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements for the scheduling plan, such as limits on consecutive days worked, specific days off, or restrictions on which students can work together?

## Turn 9 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 10 - Generic Agent

QUESTION: Does the constraint "each student can work no more than 2 shifts per week" mean that a student can be scheduled on at most 2 different days per week, or does it mean something else?

## Turn 10 - User Simulator

It means a student can be scheduled on at most 2 different days per week.

## Turn 11 - Generic Agent

QUESTION: Does the constraint "no more than 3 different students can be scheduled for duty on any single day" mean that at most 3 students can have non-zero hours on that day, or does it refer to something else?

## Turn 11 - User Simulator

It means that at most 3 students can have non-zero hours on that day.

## Turn 12 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 hard constraints that must not be exceeded, or are they soft targets?

## Turn 12 - User Simulator

They are hard constraints that must not be exceeded.

## Turn 13 - Generic Agent

QUESTION: Are the student duty hours on each day required to be whole numbers of hours, or can they be fractional values?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Can a student work multiple non-consecutive blocks of hours on the same day, or must their daily duty be a single continuous block?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Which students in the table are undergraduates and which are graduate students?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is there a maximum number of hours any single student can work in total per week, or is the only weekly limit the minimum requirement?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1. **Objective:** Minimize total weekly labor cost.
2. **Operating Hours:** The lab is open from 8:00 AM to 10:00 PM (14 hours) every day from Monday to Friday.
3. **Coverage Requirement:** Exactly one student must be on duty for every hour during open hours.
4. **Student Availability:** A value of 0 in Table 5-9 indicates the student is completely unavailable on that day.
5. **Daily Hour Limits:** The maximum hours per day for each student (Table 5-9) are hard constraints.
6. **Weekly Minimums:** Each undergraduate must work at least 8 hours per week, and each graduate student must work at least 7 hours per week. These are hard constraints.
7. **Shift Limit:** Each student can be scheduled on at most 2 different days per week.
8. **Daily Student Limit:** No more than 3 different students can have non-zero hours on any single day.

**Assumptions (due to lack of confirmation):**
1. **Student Classification:** It is assumed that Students 1, 2, and 3 are undergraduates (minimum 8 hours/week) and Students 4, 5, and 6 are graduate students (minimum 7 hours/week). *Note: This is a guess based on typical ordering; please verify.*
2. **Hour Granularity:** It is assumed that duty hours must be integer values (whole hours).
3. **Continuity:** It is assumed that a student's duty on a given day must be a single continuous block of hours (no split shifts).
4. **Weekly Maximum:** It is assumed there is no explicit maximum weekly hours constraint other than the sum of the daily maximums and the 2-day limit.

**Model Structure:**
- **Decision Variables:** $x_{i,d,h}$ is a binary variable indicating if student $i$ is on duty at hour $h$ on day $d$. Alternatively, $y_{i,d}$ can represent the number of hours student $i$ works on day $d$, with constraints ensuring coverage. Given the "exactly one" constraint per hour, a binary assignment per hour-slot is the most precise formulation.
- **Indices:**
  - $i \in \{1, ..., 6\}$ (Students)
  - $d \in \{Mon, Tue, Wed, Thu, Fri\}$ (Days)
  - $h \in \{1, ..., 14\}$ (Hours, representing 8:00-9:00, ..., 21:00-22:00)
- **Objective:** $\min \sum_{i,d,h} w_i \cdot x_{i,d,h}$
- **Constraints:**
  1. **Coverage:** $\sum_{i} x_{i,d,h} = 1$ for all $d, h$.
  2. **Availability:** $x_{i,d,h} = 0$ if MaxHours$_{i,d} = 0$.
  3. **Daily Max Hours:** $\sum_{h} x_{i,d,h} \le \text{MaxHours}_{i,d}$ for all $i, d$.
  4. **Weekly Min Hours:** $\sum_{d,h} x_{i,d,h} \ge 8$ for undergraduates; $\ge 7$ for graduates.
  5. **Max Days per Student:** $\sum_{h} x_{i,d,h} \le M \cdot z_{i,d}$ where $z_{i,d}$ is binary (1 if student $i$ works on day $d$), and $\sum_{d} z_{i,d} \le 2$. (Or simply: if $\sum_{h} x_{i,d,h} > 0$, count as 1 day).
  6. **Max Students per Day:** $\sum_{i} z_{i,d} \le 3$ for all $d$.