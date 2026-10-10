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

QUESTION: What is the objective of the scheduling plan — are we minimizing total weekly labor cost, or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost. This is calculated as the sum of each student's hourly wage multiplied by their total hours worked during the week.

## Turn 2 - Generic Agent

QUESTION: How many hours per day must be covered by a student on duty, given that the lab is open from 8:00 AM to 10:00 PM?

## Turn 2 - User Simulator

14 hours per day.

## Turn 3 - Generic Agent

QUESTION: Are the maximum daily hours in Table 5-9 hard upper bounds that a student cannot exceed on any given day, or are they soft targets that can be violated at some cost?

## Turn 3 - User Simulator

They are hard upper bounds. A student cannot exceed the maximum hours specified in Table 5-9 on any given day.

## Turn 4 - Generic Agent

QUESTION: Are the minimum weekly hours (8 for undergraduates, 7 for graduates) hard lower bounds that must be met, or are they soft targets that can be violated at some penalty?

## Turn 4 - User Simulator

They are hard lower bounds that must be met.

## Turn 5 - Generic Agent

QUESTION: Which student IDs in the table are undergraduates and which are graduate students?

## Turn 5 - User Simulator

I need to confirm internally which specific student IDs are undergraduates and which are graduate students.

## Turn 6 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be whole numbers of hours?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Besides the minimum weekly hours, maximum daily hours, and one-student-on-duty requirement, are there any other constraints such as maximum consecutive days worked, required days off, or limits on how many days per week a student can work?

## Turn 7 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 8 - Generic Agent

QUESTION: Does the "no more than 2 shifts per week" constraint mean a student can work on at most 2 different days per week, or does it mean a student can work at most 2 separate duty blocks per day?

## Turn 8 - User Simulator

It means a student can work on at most 2 different days per week.

## Turn 9 - Generic Agent

QUESTION: Does the "no more than 3 different students can be scheduled for duty on any single day" constraint mean that at most 3 students can have non-zero hours on a given day, or does it mean something else?

## Turn 9 - User Simulator

It means that at most 3 students can have non-zero hours on a given day.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about, such as specific days certain students cannot work, or any preferences about which students should be scheduled together?

## Turn 10 - User Simulator

No, there are no other constraints or requirements beyond what has already been discussed.

## Turn 11 - Generic Agent

QUESTION: Can a student work fractional hours (e.g., 2.5 hours) on a given day, or must all hours be whole numbers?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are the lab open hours the same every day from Monday to Friday, or do they vary by day?

## Turn 12 - User Simulator

The lab operates from 8:00 AM to 10:00 PM every day from Monday to Friday.

## Turn 13 - Generic Agent

QUESTION: Can a student work fractional hours (e.g., 2.5 hours) on a given day, or must all hours be whole numbers?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Minimize total weekly labor cost, calculated as the sum of each student's hourly wage multiplied by their total hours worked during the week. *(Confirmed)*

2. **Decision Variables:** Hours worked by each student on each day (Monday through Friday). *(Confirmed)*

3. **Variable Domain:** Continuous (fractional hours allowed). *(Assumed — user has not confirmed whether hours must be whole numbers)*

4. **Constraints:**
   - **One student on duty:** Exactly one student must be on duty during open hours each day. *(Confirmed)*
   - **Daily coverage:** 14 hours per day must be covered (8:00 AM to 10:00 PM). *(Confirmed)*
   - **Minimum weekly hours:** Each undergraduate must work at least 8 hours per week; each graduate student must work at least 7 hours per week. *(Confirmed as hard lower bounds)*
   - **Maximum daily hours:** Each student's hours on a given day cannot exceed the maximum specified in Table 5-9. *(Confirmed as hard upper bounds)*
   - **Maximum days per week:** Each student can work on at most 2 different days per week. *(Confirmed)*
   - **Maximum students per day:** At most 3 different students can have non-zero hours on any single day. *(Confirmed)*

5. **Data:**
   - Table 5-9 provides hourly wages and maximum daily hours for 6 students across Monday to Friday. *(Confirmed)*
   - Lab operates from 8:00 AM to 10:00 PM every day from Monday to Friday. *(Confirmed)*

**Open Assumptions:**

1. **Student classification:** Which student IDs are undergraduates and which are graduate students is not confirmed. This affects the minimum weekly hours constraint (8 hours for undergraduates, 7 hours for graduates).

2. **Variable domain:** Whether hours must be whole numbers or can be fractional is not confirmed. The model assumes continuous variables (fractional hours allowed).