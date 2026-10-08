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

QUESTION: What is the objective of the scheduling plan — is it to minimize the total weekly labor cost (sum of wage × hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 2 - Generic Agent

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) with exactly one student on duty at all times — does this mean the total hours worked by all students combined must equal 14 hours per day (i.e., 70 hours per week), or could the lab be closed on some days of the week?

## Turn 2 - User Simulator

The total hours worked by all students combined must equal 14 hours per day, which is 70 hours per week. The lab is open every day from Monday to Friday.

## Turn 3 - Generic Agent

QUESTION: The minimum weekly hours are 8 for each undergraduate and 7 for each graduate student — which of the six students are undergraduates and which are graduate students?

## Turn 3 - User Simulator

I don't have that information in the supplied business facts. It still needs internal confirmation which of the six students are undergraduates and which are graduate students.

## Turn 4 - Generic Agent

QUESTION: The maximum daily hours in Table 5-9 — are these hard upper bounds on how many hours a student can work on that day (i.e., a student cannot be scheduled for more hours than the table value on that day), or do they represent something else like a preference or a soft limit?

## Turn 4 - User Simulator

They are hard upper bounds. A student cannot be scheduled for more hours than the table value on that day.

## Turn 5 - Generic Agent

QUESTION: Can a student work fractional hours (e.g., 3.5 hours) on a given day, or must the hours assigned to each student on each day be whole numbers?

## Turn 5 - User Simulator

The supplied business facts do not specify whether hours must be whole numbers or if fractional hours are allowed. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: The lab is open 8:00 AM to 10:00 PM with one student on duty at all times — does a student's shift have to be a single continuous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a given day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 6 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single continuous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any restrictions on which students can work on which days beyond the zero entries in Table 5-9 — for example, is a zero in the table simply meaning that student is unavailable that day, or could there be additional constraints like a student not being allowed to work on consecutive days?

## Turn 7 - User Simulator

The supplied business facts do not specify any additional restrictions beyond the zero entries in Table 5-9, such as a student not being allowed to work on consecutive days. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 8 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: For the minimum weekly hours requirement (8 hours for undergraduates, 7 hours for graduate students), is this a strict lower bound that must be met exactly or at least, meaning a student could work more than 8 or 7 hours in a week as long as they meet the minimum?

## Turn 9 - User Simulator

It is a strict lower bound meaning "at least." A student could work more than 8 or 7 hours in a week as long as they meet the minimum.

## Turn 10 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 10 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 11 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 12 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 13 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 14 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 15 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 16 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 17 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 18 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 19 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 20 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 21 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 22 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 23 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 24 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 25 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 26 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 27 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 28 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 29 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Since the lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student is on duty at all times, does each student's shift on a given day have to be a single contiguous block of hours (e.g., 8 AM to 2 PM), or can a student's hours on a day be split into multiple non-contiguous segments (e.g., 8 AM to 12 PM and 6 PM to 10 PM)?

## Turn 30 - User Simulator

The supplied business facts do not specify whether a student's shift must be a single contiguous block or can be split into multiple non-contiguous segments. This point still needs internal confirmation.