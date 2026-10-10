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

QUESTION: Is the lab open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday through Friday, or are there specific open hours that differ by day?

## Turn 1 - User Simulator

The lab is open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday through Friday.

## Turn 2 - Generic Agent

QUESTION: The maximum daily hours in Table 5-9 sum to less than 14 hours for every student (e.g., Student 1 maxes at 6+0+6+0+7=19 total, but no single day exceeds 7), so no single student can cover all 14 hours in a day; does "one and only one student on duty" mean exactly one student is assigned to the lab for the entire 14-hour block each day, or can the 14 hours be split among multiple students as long as only one is present at any given time?

## Turn 2 - User Simulator

The 14 hours can be split among multiple students as long as only one is present at any given time.

## Turn 3 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 hard caps that a student cannot exceed, or are they soft targets that can be violated with a penalty?

## Turn 3 - User Simulator

The daily maximum hours in Table 5-9 are hard caps that a student cannot exceed.

## Turn 4 - Generic Agent

QUESTION: Is the objective to minimize total weekly labor cost (sum of wage × hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 4 - User Simulator

The objective is to minimize total weekly labor cost, which is the sum of each student's hourly wage times their total hours worked that week.

## Turn 5 - Generic Agent

QUESTION: Are the weekly minimums (8 hours for undergraduates, 7 hours for graduates) hard constraints that must be met, or are they soft targets that can be violated with a penalty?

## Turn 5 - User Simulator

The weekly minimums are hard constraints that must be met.

## Turn 6 - Generic Agent

QUESTION: Which student IDs are undergraduates and which are graduates?

## Turn 6 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is not confirmed, should I assume all six students are undergraduates (requiring at least 8 hours each per week), or is there a different split you would like me to use?

## Turn 7 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the decision variables continuous (allowing fractional hours like 2.5 hours) or must they be integer (whole hours only)?

## Turn 8 - User Simulator

I don't have that information in the supplied business facts. That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any additional requirements beyond those stated, such as minimum consecutive hours per shift, maximum consecutive days worked, or restrictions on which students can work on the same day?

## Turn 9 - User Simulator

Yes, there are two additional requirements:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 10 - Generic Agent

QUESTION: Does "no more than 2 shifts per week" mean a student can work on at most 2 distinct days out of the 5, or does it mean something else like at most 2 separate time blocks per day?

## Turn 10 - User Simulator

It means a student can work on at most 2 distinct days out of the 5.

## Turn 11 - Generic Agent

QUESTION: Does "no more than 3 students can be scheduled for duty each day" mean at most 3 students can have any hours assigned on a given day, or does it mean at most 3 students can be on duty at any single point in time?

## Turn 11 - User Simulator

It means at most 3 students can have any hours assigned on a given day.

## Turn 12 - Generic Agent

QUESTION: Are there any other constraints or requirements I should be aware of that are not yet covered?

## Turn 12 - User Simulator

No, there are no other constraints or requirements beyond those already covered.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1. **Objective:** Minimize total weekly labor cost (sum of wage × hours for all students).
2. **Time Horizon:** Monday through Friday, 14 hours per day (8:00 AM to 10:00 PM).
3. **Coverage Constraint:** Exactly one student must be on duty at any given time, so total hours assigned per day must equal 14.
4. **Daily Max Hours:** The values in Table 5-9 are hard caps on hours per student per day.
5. **Weekly Minimums:** Hard constraints. Undergraduates must work ≥ 8 hours/week; Graduates must work ≥ 7 hours/week.
6. **Shift Limit:** Each student can work on at most 2 distinct days per week.
7. **Daily Student Limit:** At most 3 students can have any hours assigned on a given day.
8. **No Other Constraints:** No additional requirements beyond those listed.

**Assumptions (Unconfirmed):**
1. **Student Classification:** It is assumed all six students are undergraduates, so each must work at least 8 hours per week. (If any are graduates, their minimum would be 7 hours instead.)
2. **Variable Domain:** It is assumed hours can be fractional (continuous variables), not restricted to whole hours.

**Model Structure Summary:**
- **Decision Variables:** $x_{i,d}$ = hours student $i$ works on day $d$ (continuous, non-negative).
- **Objective:** Minimize $\sum_{i=1}^{6} \sum_{d=1}^{5} w_i \cdot x_{i,d}$
- **Constraints:**
  - $\sum_{i=1}^{6} x_{i,d} = 14$ for each day $d$ (coverage).
  - $x_{i,d} \leq M_{i,d}$ for all $i, d$ (daily max from Table 5-9).
  - $\sum_{d=1}^{5} x_{i,d} \geq 8$ for all $i$ (weekly min, assuming all undergrads).
  - $\sum_{d=1}^{5} y_{i,d} \leq 2$ for all $i$, where $y_{i,d}$ is a binary indicator that student $i$ works on day $d$ (shift limit).
  - $x_{i,d} \leq 14 \cdot y_{i,d}$ (linking constraint).
  - $\sum_{i=1}^{6} y_{i,d} \leq 3$ for each day $d$ (daily student limit).