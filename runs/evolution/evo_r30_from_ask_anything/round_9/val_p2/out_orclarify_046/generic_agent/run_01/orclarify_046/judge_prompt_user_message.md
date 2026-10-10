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

QUESTION: Are the maximum duty hours in Table 5-9 expressed in hours (e.g., 6 means 6 hours) or in some other unit like 30-minute slots?

## Turn 2 - User Simulator

The maximum duty hours in Table 5-9 are expressed in hours.

## Turn 3 - Generic Agent

QUESTION: Is the lab open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday to Friday, or are there specific open hours that differ by day?

## Turn 3 - User Simulator

The lab is open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday to Friday.

## Turn 4 - Generic Agent

QUESTION: Can a student work multiple non-contiguous shifts on the same day, or must their working hours on a given day form a single continuous block?

## Turn 4 - User Simulator

I don't have a specific rule on whether a student's working hours on a given day must form a single continuous block or can be split into multiple non-contiguous shifts. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum number of days per week that any single student is allowed to work?

## Turn 5 - User Simulator

No, there is no maximum number of days per week that any single student is allowed to work.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or requirements for the scheduling plan that are not mentioned in the brief, such as minimum days off, specific days a student cannot work, or preferences for certain students to work on certain days?

## Turn 6 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 7 - Generic Agent

QUESTION: Does the constraint "Each student can work no more than 2 shifts per week" mean that a student can work on at most 2 different days per week, or does it mean something else?

## Turn 7 - User Simulator

It means a student can work on at most 2 different days per week.

## Turn 8 - Generic Agent

QUESTION: Does the constraint "No more than 3 students can be scheduled for duty each day" mean that at most 3 students can be assigned to work on any given day, or does it mean something else?

## Turn 8 - User Simulator

It means that at most 3 students can be assigned to work on any given day.

## Turn 9 - Generic Agent

QUESTION: Can a student work a partial hour (e.g., 2.5 hours) on a given day, or must their working hours on each day be whole numbers?

## Turn 9 - User Simulator

I don't have a specific rule on whether a student's working hours on a given day must be whole numbers or can be partial hours. That point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum number of hours any single student can work in total per week, or is the only weekly limit the minimum requirement (8 hours for undergraduates, 7 hours for graduates)?

## Turn 10 - User Simulator

The only weekly limit is the minimum requirement: 8 hours for undergraduates and 7 hours for graduates. There is no maximum total weekly hours per student beyond the daily maximums in Table 5-9 and the 2-shifts-per-week limit.

## Turn 11 - Generic Agent

QUESTION: Which students are undergraduates and which are graduates, so that the correct minimum weekly hours (8 or 7) can be applied to each?

## Turn 11 - User Simulator

I don't have the specific breakdown of which students are undergraduates and which are graduates. That point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are there any other constraints or requirements for the scheduling plan that are not mentioned in the brief, such as specific days a student cannot work, preferences for certain students to work on certain days, or any other rules?

## Turn 12 - User Simulator

No, there are no other constraints or requirements beyond what has already been discussed.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective**: Minimize total weekly labor cost (sum of wage × hours for all students).
2. **Decision Variables**: Hours worked by each student on each day (Monday–Friday).
3. **Variable Domain**: Continuous non-negative hours (assumed, since partial hours were not confirmed as disallowed).
4. **Constraints**:
   - **Coverage**: Exactly one student on duty at all times during open hours (8:00 AM–10:00 PM, 14 hours/day, Mon–Fri). This implies the sum of hours worked by all students on any given day must equal 14.
   - **Daily Maximums**: Each student’s hours on a given day cannot exceed the values in Table 5-9.
   - **Weekly Minimums**: Each undergraduate must work at least 8 hours/week; each graduate must work at least 7 hours/week.
   - **Shift Limit**: Each student can work on at most 2 different days per week.
   - **Daily Student Limit**: At most 3 students can be assigned to work on any given day.
5. **Data**:
   - Wages and daily maximum hours are as given in Table 5-9.
   - Lab is open 14 hours/day, Monday through Friday.

**Open Assumptions:**

1. **Student Classification**: It is assumed that all 6 students are undergraduates (requiring 8 hours/week minimum). If any are graduates, their minimum would be 7 hours/week. This needs confirmation.
2. **Partial Hours**: It is assumed that students can work partial hours (e.g., 2.5 hours) on a given day. If whole hours only are required, the model would need integer constraints.
3. **Shift Continuity**: It is assumed that a student’s hours on a given day can be split into non-contiguous shifts. If a single continuous block is required, additional constraints would be needed.

## Turn 13 - User Simulator

The understanding is correct, with one correction:

- **Student Classification**: I still do not have the specific breakdown of which students are undergraduates and which are graduates. This point still needs internal confirmation.

The other open assumptions (partial hours allowed, non-contiguous shifts allowed) are acceptable as stated.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective**: Minimize total weekly labor cost.
2.  **Decision Variables**: Let $x_{i,d}$ be the number of hours student $i$ works on day $d$ (where $i \in \{1..6\}$ and $d \in \{Mon..Fri\}$).
3.  **Variable Domain**: Continuous, non-negative real numbers.
4.  **Constraints**:
    *   **Daily Coverage**: For each day $d$, $\sum_{i=1}^{6} x_{i,d} = 14$ (since the lab is open 14 hours and exactly one student is on duty at all times).
    *   **Daily Maximums**: $x_{i,d} \le M_{i,d}$ for all $i, d$, where $M_{i,d}$ is the value from Table 5-9.
    *   **Shift Limit (Days Worked)**: Each student can work on at most 2 days per week. This requires binary variables $y_{i,d}$ indicating if student $i$ works on day $d$, with $\sum_{d} y_{i,d} \le 2$ for all $i$, and $x_{i,d} \le M_{i,d} \cdot y_{i,d}$.
    *   **Daily Student Limit**: At most 3 students can be scheduled on any given day. This requires $\sum_{i=1}^{6} y_{i,d} \le 3$ for all $d$.
    *   **Weekly Minimums**:
        *   For each undergraduate $i$: $\sum_{d} x_{i,d} \ge 8$.
        *   For each graduate $i$: $\sum_{d} x_{i,d} \ge 7$.
5.  **Data**:
    *   Wages: $w_i$ as per Table 5-9.
    *   Daily Max Hours: $M_{i,d}$ as per Table 5-9.
    *   Open Hours: 14 hours/day, Monday–Friday.

**Open Assumptions:**

1.  **Student Classification**: The specific classification of students 1–6 as undergraduate or graduate is **unknown**. The model formulation will include a parameter $minHours_i$ which is 8 for undergraduates and 7 for graduates. This parameter must be set before solving.
2.  **Partial Hours**: Students can work partial hours (continuous variables).
3.  **Shift Continuity**: A student's hours on a given day can be non-contiguous (no continuity constraint required).