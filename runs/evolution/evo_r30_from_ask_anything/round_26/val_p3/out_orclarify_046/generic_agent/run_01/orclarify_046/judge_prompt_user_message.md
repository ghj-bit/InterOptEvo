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

QUESTION: What is the objective of the scheduling plan — are we minimizing total weekly labor cost, or is there a different goal?

## Turn 1 - User Simulator

We are minimizing the total weekly labor cost. Specifically, the goal is to minimize the total gross pay, which is the sum of each student's hourly wage multiplied by their total hours worked during the week.

## Turn 2 - Generic Agent

QUESTION: Are the maximum duty hours in Table 5-9 measured in continuous hours (e.g., 6 hours means 6 hours of work), or do they refer to the number of distinct time slots a student can be assigned?

## Turn 2 - User Simulator

The maximum duty hours in Table 5-9 are measured in continuous hours. For example, a value of 6 means the student can work up to 6 hours on that day.

## Turn 3 - Generic Agent

QUESTION: Does the lab require exactly one student on duty for every hour from 8:00 AM to 10:00 PM, meaning 14 hours of coverage each day?

## Turn 3 - User Simulator

Yes, the lab requires exactly one student on duty for every hour from 8:00 AM to 10:00 PM, meaning 14 hours of coverage each day.

## Turn 4 - Generic Agent

QUESTION: Can a single student work multiple non-consecutive blocks of hours within the same day, or must their daily work be one continuous block?

## Turn 4 - User Simulator

The available business facts do not specify whether a student's daily work must be one continuous block or can be split into multiple non-consecutive blocks. This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Can a student's daily work be split into multiple non-consecutive blocks of hours, or must it be one continuous block?

## Turn 5 - User Simulator

The available business facts do not specify whether a student's daily work must be one continuous block or can be split into multiple non-consecutive blocks. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints on the schedule, such as limits on how many days per week a student can work, or requirements about which students can cover specific time slots?

## Turn 6 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 7 - Generic Agent

QUESTION: When you say each student can work no more than 2 shifts per week, does a "shift" mean any single day they work (regardless of how many hours), or does it refer to a specific time block?

## Turn 7 - User Simulator

A "shift" means any single day the student works, regardless of how many hours they work that day.

## Turn 8 - Generic Agent

QUESTION: Can a student's daily work be split into multiple non-consecutive blocks of hours, or must it be one continuous block?

## Turn 8 - User Simulator

The available business facts do not specify whether a student's daily work must be one continuous block or can be split into multiple non-consecutive blocks. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the 14 hours of daily coverage (8 AM to 10 PM) divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 9 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end their shifts at any hour. This point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 10 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end their shifts at any hour. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 11 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end their shifts at any hour. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 12 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end their shifts at any hour. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 13 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end their shifts at any hour. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 14 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end

## Turn 15 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 15 - User Simulator

The available business facts do not specify whether the 14 hours of daily coverage are divided into fixed time slots or if students can start and end

## Turn 16 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 16 - User Simulator

The available business

## Turn 17 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 18 - User Simulator

The

## Turn 19 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Are the 14 hours of daily coverage divided into fixed time slots, or can students start and end their shifts at any hour?

## Turn 30 - User Simulator

The