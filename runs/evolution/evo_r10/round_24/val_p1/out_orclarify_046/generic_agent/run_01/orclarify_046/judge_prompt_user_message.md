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

QUESTION: The lab is open 14 hours a day (8:00–22:00) and exactly one student must be on duty at all times, so 14 person-hours are needed each day. But the sum of the daily maximum hours in Table 5-9 is only 12 on Monday, 18 on Tuesday, 14 on Wednesday, 12 on Thursday, and 21 on Friday — so Monday and Thursday cannot be fully covered. How should the model handle this: (a) treat the table as the true availability and allow the lab to be understaffed on some hours (minimizing total wage cost subject to the minimum-hour requirements), (b) treat the table as a cap but allow students to work beyond it if needed to guarantee full 14-hour coverage every day, or (c) something else, such as reducing the required coverage on those days?

## Turn 1 - User Simulator

The table in Table 5-9 represents the true maximum availability for each student on each day. The model should treat these values as hard caps.

Therefore, the correct approach is (a): treat the table as the true availability and allow the lab to be understaffed on some hours. The goal is to minimize total wage cost subject to the minimum-hour requirements, accepting that full 14-hour coverage may not be possible on days where the total available hours are insufficient.

## Turn 2 - Generic Agent

QUESTION: You confirmed the table values are hard caps and that understaffing is allowed. Now, regarding the minimum-hour requirements: each undergraduate must work at least 8 hours per week and each graduate at least 7 hours per week. Are these minimums hard constraints that the schedule must satisfy (meaning the model is infeasible if they can't be met), or are they soft targets that we try to meet but can relax if the availability caps make it impossible?

## Turn 2 - User Simulator

The minimum-hour requirements are hard constraints. The schedule must satisfy them. If the availability caps make it impossible to meet these minimums, the model is infeasible.

## Turn 3 - Generic Agent

QUESTION: The table lists 6 students but doesn't say which are undergraduates and which are graduates. Could you tell me which student IDs are undergraduates (minimum 8 hours/week) and which are graduates (minimum 7 hours/week)?

## Turn 3 - User Simulator

I don't have that information in the provided business facts. The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the undergraduate/graduate classification isn't available, how should the model handle the minimum-hour requirement: should I apply the 8-hour minimum to all students, the 7-hour minimum to all students, or introduce a binary classification variable for each student (undergraduate vs. graduate) so the model can decide which minimum applies to whom?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Setting aside the undergraduate/graduate classification for now, I need to clarify the coverage requirement. You said the lab must have one and only one student on duty during open hours, but also that understaffing is allowed on days where total availability is insufficient. So the model's objective is to minimize total wage cost while satisfying the minimum-hour constraints, and the "one student on duty" rule means that at any given hour, at most one student can be assigned (not exactly one)?

## Turn 5 - User Simulator

The "one student on duty" rule means that at any given hour, at most one student can be assigned. The model should minimize total wage cost while satisfying the minimum-hour constraints, accepting that some hours may remain uncovered if total availability is insufficient.

## Turn 6 - Generic Agent

QUESTION: Regarding the objective function: you want to minimize total weekly wage cost. Since the minimum-hour requirements are hard constraints and the daily caps are hard caps, the model will assign each student their minimum required hours (or as close as the caps allow) at the lowest possible cost. Is the objective simply to minimize the sum of (hours assigned × hourly wage) across all students and all days, with no other cost or penalty terms?

## Turn 6 - User Simulator

Yes, the objective is simply to minimize the sum of (hours assigned × hourly wage) across all students and all days, with no other cost or penalty terms.

## Turn 7 - Generic Agent

QUESTION: Going back to the undergraduate/graduate classification: since you don't have that information, should I model the minimum-hour requirement as a single uniform minimum of 7 hours per week for all students (the lower of the two thresholds), or would you prefer I parameterize it so you can plug in the correct minimum for each student once the classification is confirmed?

## Turn 7 - User Simulator

I would prefer you parameterize it so I can plug in the correct minimum for each student once the classification is confirmed.

## Turn 8 - Generic Agent

QUESTION: One more clarification on the structure: the lab is open 14 hours each day (8:00–22:00), and the table gives maximum hours per student per day. Should I model the assignment at the hour level (i.e., decide which student covers each of the 14 hours on each day, with the constraint that at most one student is assigned per hour and each student's total assigned hours that day don't exceed their cap), or is it sufficient to model at the day level (i.e., decide how many hours each student works on each day, with the constraint that the sum of hours across all students on a given day doesn't exceed 14)?

## Turn 8 - User Simulator

It is sufficient to model at the day level. Decide how many hours each student works on each day, with the constraint that the sum of hours across all students on a given day doesn't exceed 14.

## Turn 9 - Generic Agent

QUESTION: Regarding the daily coverage constraint: you said the sum of hours across all students on a given day doesn't exceed 14. Is there also a lower bound on daily coverage (e.g., the lab must be open for at least some minimum number of hours each day), or is it purely an upper bound of 14 with no minimum daily coverage requirement?

## Turn 9 - User Simulator

It is purely an upper bound of 14 with no minimum daily coverage requirement.

## Turn 10 - Generic Agent

QUESTION: One final check: the decision variables are the number of hours each student works on each day (6 students × 5 days = 30 variables). The constraints are: (1) each student's hours on a given day ≤ their cap from Table 5-9, (2) sum of all students' hours on a given day ≤ 14, (3) each student's total weekly hours ≥ their parameterized minimum (7 or 8 depending on classification), and (4) all variables ≥ 0. Is that the complete set of constraints, or are there any additional rules I should include (e.g., a student cannot work on a day where their cap is 0, maximum consecutive days, etc.)?

## Turn 10 - User Simulator

There are two additional rules to include:

1.  Each student can work no more than 2 shifts per week.
2.  No more than 3 students can be scheduled for duty each day.

## Turn 11 - Generic Agent

QUESTION: Regarding the "no more than 2 shifts per week" rule: does a "shift" mean any day on which a student works at least 1 hour (i.e., a student can work at most 2 out of the 5 days), or does it mean something else, such as a fixed time block?

## Turn 11 - User Simulator

A "shift" means any day on which a student works at least 1 hour. A student can work at most 2 out of the 5 days.

## Turn 12 - Generic Agent

QUESTION: Regarding the "no more than 3 students can be scheduled for duty each day" rule: does this mean that on any given day, at most 3 students can have a positive number of hours assigned (i.e., at most 3 students are "on duty" that day), or does it mean something else?

## Turn 12 - User Simulator

It means that on any given day, at most 3 students can have a positive number of hours assigned.

## Turn 13 - Generic Agent

QUESTION: One last check on the "at most 2 shifts per week" rule combined with the minimum-hour requirements: if a student can work at most 2 days per week, and their minimum is 8 hours per week, then they need to average 4 hours per working day. Looking at the caps in Table 5-9, some students have very low caps on certain days (e.g., Student 1 has caps of 6, 0, 6, 0, 7 — so they can only work Monday, Wednesday, or Friday). Does the model simply need to find any feasible assignment satisfying all constraints, or should it also try to maximize total coverage hours (i.e., fill as many of the 14 daily slots as possible) as a secondary objective?

## Turn 13 - User Simulator

The model simply needs to find any feasible assignment satisfying all constraints. There is no secondary objective to maximize total coverage hours.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the duty scheduling problem:

**Problem:** Assign hours to 6 student workers across 5 days (Monday–Friday) for a university computer lab.

**Decision Variables:**
- x[i][d] = number of hours student i works on day d (continuous, ≥ 0), for i = 1..6 and d = Mon..Fri (30 variables total).

**Objective:**
- Minimize total weekly wage cost: Σ (x[i][d] × wage[i]) over all students and days.

**Constraints:**
1. **Daily caps (hard):** x[i][d] ≤ cap[i][d] from Table 5-9 for each student and day.
2. **Daily coverage upper bound:** Σ_i x[i][d] ≤ 14 for each day d (no minimum daily coverage).
3. **Minimum weekly hours (hard, parameterized):** Σ_d x[i][d] ≥ min_hours[i] for each student, where min_hours[i] is 8 for undergraduates and 7 for graduates (to be parameterized since classification is pending).
4. **At most 2 shifts per week:** For each student, the number of days on which x[i][d] > 0 is at most 2 (requires binary auxiliary variables y[i][d] with x[i][d] ≤ M·y[i][d] and Σ_d y[i][d] ≤ 2).
5. **At most 3 students per day:** For each day d, the number of students with x[i][d] > 0 is at most 3 (uses the same y[i][d] variables: Σ_i y[i][d] ≤ 3).
6. **Non-negativity:** x[i][d] ≥ 0.

**Parameters (from Table 5-9):**
- Wages: [10.0, 10.0, 9.9, 9.8, 10.8, 11.3] CNY/h
- Caps: as given in the table (0 means the student is unavailable that day).

**Notes:**
- The model is a mixed-integer linear program (MILP) due to the binary shift variables.
- If the minimum-hour constraints cannot be satisfied given the caps and shift limits, the model is infeasible.
- The undergraduate/graduate classification (and thus min_hours[i]) is to be parameterized for later input.