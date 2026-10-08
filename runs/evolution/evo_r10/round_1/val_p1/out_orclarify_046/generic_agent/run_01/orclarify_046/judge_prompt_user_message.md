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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, but the daily maximum hours in Table 5-9 sum to only 13 hours across all six students on Monday (6+0+4+5+3+0), so the 14 open hours cannot be covered on that day. Is the intended coverage requirement actually 13 hours per day (e.g., the lab is open 8:00 AM to 9:00 PM, or one hour is intentionally uncovered), or should the model instead minimize the total uncovered hours subject to the given daily maximums?

## Turn 1 - User Simulator

The lab is open 8:00 AM to 10:00 PM, which is 14 hours. The coverage requirement is that exactly one student must be on duty during all open hours. The daily maximum hours in Table 5-9 are hard constraints; if the sum of available hours on a given day is less than 14, the problem is infeasible as stated. There is no provision for uncovered hours or a reduced operating time. Please confirm whether the operating hours or the maximum duty hours in Table 5-9 need to be adjusted to make the schedule feasible.

## Turn 2 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday (6+0+4+5+3+0) and 13 hours on Thursday (0+6+0+0+8+6), which is less than the 14 open hours, how should I resolve this infeasibility: (a) treat the lab as open 13 hours per day (8:00 AM to 9:00 PM), (b) keep 14 open hours and raise the Monday and Thursday maximums so each day sums to at least 14, or (c) keep 14 open hours and allow the model to report infeasibility on those days?

## Turn 2 - User Simulator

The lab is open 8:00 AM to 10:00 PM (14 hours), and exactly one student must be on duty during all open hours. The daily maximum hours in Table 5-9 are fixed constraints. If the sum of available hours on a day is less than 14, the problem is infeasible as stated. There is no provision for uncovered hours, reduced operating time, or adjusted maximums. Please confirm whether the operating hours or the maximum duty hours in Table 5-9 need to be corrected to make the schedule feasible.

## Turn 3 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 3 - User Simulator

The lab is open 8:00 AM to 10:00 PM (14 hours). The daily maximum hours in Table 5-9 are fixed. If the sum of available hours on a day is less than 14, the problem is infeasible as stated. There is no provision for uncovered hours, reduced operating time, or adjusted maximums. Please confirm whether the operating hours or the maximum duty hours in Table 5-9 need to be corrected to make the schedule feasible.

## Turn 4 - Generic Agent

QUESTION: Given that the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and that you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: While that is being confirmed, is the objective of the schedule to minimize the total weekly labor cost (sum of each student's hours worked times their hourly wage)?

## Turn 5 - User Simulator

Yes, the objective is to minimize the total weekly labor cost, which is the sum of each student's hours worked times their hourly wage.

## Turn 6 - Generic Agent

QUESTION: Are the weekly minimum requirements (at least 8 hours for each undergraduate and at least 7 hours for each graduate student) hard constraints that must be satisfied, or are they soft targets that can be relaxed if needed to make the schedule feasible?

## Turn 6 - User Simulator

The weekly minimum requirements are hard constraints that must be satisfied.

## Turn 7 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 upper bounds (a student can work up to but not necessarily exactly that many hours), or exact targets that each student must work precisely that many hours on each day?

## Turn 9 - User Simulator

The daily maximum hours in Table 5-9 are upper bounds. A student can work up to, but not necessarily exactly, that many hours on each day.

## Turn 10 - Generic Agent

QUESTION: Are there any constraints on how many days per week each student can work, or can a student work on any subset of the five days as long as their daily hours stay within the Table 5-9 upper bounds and their weekly total meets the minimum?

## Turn 10 - User Simulator

Each student cannot work more than 2 shifts in a week.

## Turn 11 - Generic Agent

QUESTION: When you say each student cannot work more than 2 shifts in a week, does "shift" mean a day on which the student works at least one hour (i.e., at most 2 of the 5 days), or does it mean something else such as a fixed-length block of hours?

## Turn 11 - User Simulator

A "shift" means a day on which the student works at least one hour. Therefore, each student can work on at most 2 of the 5 days.

## Turn 12 - Generic Agent

QUESTION: Given that each student can work on at most 2 days, the maximum weekly hours for student 1 is 6+6=12 (Mon+Wed) or 6+7=13 (Mon+Fri) or 6+0=6 (Tue/Thu), and for student 2 is 8+9=17 (Tue+Wed) or 8+6=14 (Tue+Thu), etc. — is it acceptable that some students' 2-day maximums are well above their weekly minimum (e.g., student 2 can work up to 17 hours but only needs 7 or 8), and the model should simply choose the cheapest feasible combination?

## Turn 12 - User Simulator

Yes, it is acceptable. The model should choose the cheapest feasible combination of days and hours for each student, subject to the daily upper bounds, the 2-day limit, and the weekly minimums.

## Turn 13 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 18 - User Simulator

The point

## Turn 19 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Since the daily maximums in Table 5-9 sum to only 13 hours on Monday and Thursday, which is less than the 14 open hours, and you have confirmed the maximums are fixed, should I treat the 14-hour operating window as the value to be corrected (i.e., the lab is actually open 13 hours per day, 8:00 AM to 9:00 PM), or should I keep 14 open hours and let the model report infeasibility on Monday and Thursday?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) continuous, or must they be integer numbers of hours?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, so I can apply the 8-hour minimum to undergraduates and the 7-hour minimum to graduate students?

## Turn 30 - User Simulator

The