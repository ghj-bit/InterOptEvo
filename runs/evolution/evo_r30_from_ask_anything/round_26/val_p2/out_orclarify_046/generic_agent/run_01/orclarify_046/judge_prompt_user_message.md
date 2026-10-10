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

QUESTION: What is the objective of the scheduling plan — are we minimizing total weekly labor cost, or is there a different goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost. This is calculated as the sum of each student's hourly wage multiplied by their total hours worked during the week.

## Turn 2 - Generic Agent

QUESTION: Are the maximum duty hours in Table 5-9 expressed in hours (e.g., 6 means 6 hours), or do they represent something else like a number of time slots?

## Turn 2 - User Simulator

The maximum duty hours in Table 5-9 are expressed in hours. For example, a value of 6 means the student can work up to 6 hours on that day.

## Turn 3 - Generic Agent

QUESTION: Is the lab open for the full 14 hours every day from Monday through Friday, or are there specific open hours that differ by day?

## Turn 3 - User Simulator

The lab is open for the full 14 hours every day from Monday through Friday, from 8:00 AM to 10:00 PM.

## Turn 4 - Generic Agent

QUESTION: Can a student work a maximum of 14 hours in a single day if their Table 5-9 value allows it, or is there a separate daily cap below 14 hours?

## Turn 4 - User Simulator

The only daily cap is the maximum duty hours specified in Table 5-9 for each student on that day. There is no separate daily cap below 14 hours.

## Turn 5 - Generic Agent

QUESTION: Are the minimum weekly hours (8 for undergraduates, 7 for graduates) hard constraints that must be met, or are they soft targets that can be relaxed if needed?

## Turn 5 - User Simulator

The minimum weekly hours are hard constraints that must be met.

## Turn 6 - Generic Agent

QUESTION: Which students in the table are undergraduates and which are graduate students?

## Turn 6 - User Simulator

I don't have that information. The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is unconfirmed, should I treat all six students as having the same minimum weekly requirement, and if so, which minimum (8 hours or 7 hours) should apply to everyone?

## Turn 7 - User Simulator

Since the classification is unconfirmed, please treat all six students as having the same minimum weekly requirement of 8 hours.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements for the schedule that are not mentioned in the brief, such as limits on how many days per week a student can work, required days off, or restrictions on which students can work together?

## Turn 8 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 9 - Generic Agent

QUESTION: When you say each student can work no more than 2 shifts per week, does a "shift" mean a single continuous block of hours on one day, or does it mean one day of work regardless of how many hours are worked that day?

## Turn 9 - User Simulator

A "shift" means one day of work, regardless of how many hours are worked that day.

## Turn 10 - Generic Agent

QUESTION: Is the constraint that no more than 3 different students can be scheduled on any single day a hard constraint that must be strictly satisfied, or is it a soft target that can be exceeded if necessary?

## Turn 10 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 11 - Generic Agent

QUESTION: Can a student's duty hours on a given day be split into multiple non-contiguous blocks, or must their hours on a day form one continuous block?

## Turn 11 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Since the continuity of duty hours within a day is unconfirmed, should I assume that a student's hours on a given day must form one continuous block, or can they be split into multiple non-contiguous blocks?

## Turn 12 - User Simulator

Since the continuity of duty hours within a day is unconfirmed, please assume that a student's hours on a given day must form one continuous block.

## Turn 13 - Generic Agent

QUESTION: Are the decision variables for hours worked by each student on each day continuous (allowing fractional hours like 2.5 hours) or must they be integer values?

## Turn 13 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the granularity of hours is unconfirmed, should I assume that hours worked by each student on each day must be whole numbers, or can they be fractional values?

## Turn 14 - User Simulator

Since the granularity of hours is unconfirmed, please assume that hours worked by each student on each day must be whole numbers.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or requirements for the schedule that are not mentioned in the brief, such as limits on how many consecutive days a student can work, or restrictions on which specific days a student can or cannot work?

## Turn 15 - User Simulator

No, there are no other constraints or requirements beyond those already discussed.

## Turn 16 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Minimize total weekly labor cost, calculated as the sum of each student's hourly wage multiplied by their total hours worked during the week.
- **Decision Variables:** For each student (1–6) and each day (Monday–Friday), the number of hours that student works on that day. These variables are non-negative integers.
- **Lab Hours:** The lab is open 14 hours per day (8:00 AM to 10:00 PM) from Monday through Friday.
- **Coverage Constraint:** Exactly one student must be on duty at all times during open hours, meaning the sum of hours worked by all students on any given day must equal 14.
- **Daily Maximum Hours:** Each student's hours on a given day cannot exceed the maximum specified in Table 5-9 for that student and day.
- **Minimum Weekly Hours:** Each student must work at least 8 hours per week (applied uniformly to all six students, as the undergraduate/graduate classification was unconfirmed).
- **Maximum Shifts Per Week:** Each student can work on no more than 2 days per week (a "shift" is defined as one day of work, regardless of hours).
- **Maximum Students Per Day:** No more than 3 different students can be scheduled for duty on any single day.
- **Continuity:** A student's hours on a given day must form one continuous block.
- **Wages:** As specified in Table 5-9 (Student 1: 10.0, Student 2: 10.0, Student 3: 9.9, Student 4: 9.8, Student 5: 10.8, Student 6: 11.3 CNY/h).

**Explicit Assumptions:**

- All six students are treated as having the same minimum weekly requirement of 8 hours, since the undergraduate/graduate classification was not provided.
- A student's hours on a given day must form one continuous block, as confirmed by the user.
- Hours worked by each student on each day must be whole numbers, as confirmed by the user.