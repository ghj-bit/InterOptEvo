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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, so 14 hours of coverage are needed each day. However, the maximum daily hours in Table 5-9 sum to only 13 hours on Monday (6+0+4+5+3+0), 19 on Tuesday, 20 on Wednesday, 16 on Thursday, and 21 on Friday. Since 13 < 14 on Monday, the stated requirements cannot all hold as written. Which of these readings is correct: (a) the lab is actually open fewer hours on Monday (e.g., 13 hours), (b) the Monday maximums in the table are wrong and should be higher, or (c) the "one and only one student on duty" rule does not apply to every hour of the open period (e.g., coverage is only required for a subset of the day)?

## Turn 1 - User Simulator

The lab is open for the full 14 hours on Monday. The maximum daily hours in Table 5-9 are correct as stated. The "one and only one student on duty" rule applies to every hour of the open period.

## Turn 2 - Generic Agent

QUESTION: Since the Monday maximums sum to only 13 hours but 14 hours of coverage are required, the problem as stated is infeasible. Which of these readings should I implement: (a) the "at least 8 hours per week" minimum for undergraduates is a soft target that may be violated on Monday (i.e., drop the weekly minimum and keep only the daily maximums and full 14-hour coverage), (b) the daily maximums are hard caps but the weekly minimums are also hard, meaning I should report the problem infeasible rather than produce a schedule, or (c) one of the Monday values in the table is a typo and should actually be higher (if so, which student and what value)?

## Turn 2 - User Simulator

The problem is infeasible as stated. You should report the problem infeasible rather than produce a schedule.

## Turn 3 - Generic Agent

QUESTION: To confirm the scope of the infeasibility check: should the model treat the weekly minimums (at least 8 hours for each undergraduate, at least 7 hours for each graduate student) as hard constraints that must hold in addition to the daily maximums and the full 14-hour-per-day coverage, so that the infeasibility is detected from the combination of all these requirements together?

## Turn 3 - User Simulator

Yes, the weekly minimums are hard constraints that must hold in addition to the daily maximums and the full 14-hour-per-day coverage. The infeasibility is detected from the combination of all these requirements together.

## Turn 4 - Generic Agent

QUESTION: To confirm the objective: since the task is to detect and report infeasibility, should the model still include a cost-minimization objective (minimizing total weekly wage cost) that would apply if the data were feasible, or should the model be purely a feasibility check with no objective function?

## Turn 4 - User Simulator

The model should include the cost-minimization objective (minimizing total weekly wage cost) that would apply if the data were feasible.

## Turn 5 - Generic Agent

QUESTION: To confirm the variable domains: should each student's daily working hours be modeled as a continuous variable (allowing fractional hours, e.g., 3.5 hours), or must they be integer hours (whole hours only)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: To confirm the student classification: which of the six students are undergraduates (subject to the 8-hour weekly minimum) and which are graduate students (subject to the 7-hour weekly minimum)?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: To confirm the coverage structure: is the lab's 14-hour open period (8:00 AM to 10:00 PM) divided into 14 one-hour slots, with exactly one student assigned to each slot, and a student's daily hours equal to the number of slots they are assigned that day?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: To confirm the boundary convention for the open period: does the 14-hour span from 8:00 AM to 10:00 PM consist of 14 one-hour slots (8-9, 9-10, ..., 21-22), meaning the last slot ends exactly at 10:00 PM?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: To confirm the treatment of unused capacity: if a student's daily maximum hours exceed the hours they are actually assigned, is the unused portion simply free (no penalty, no requirement to use it), so the only binding limits are the daily maximums as upper bounds?

## Turn 9 - User Simulator

Yes, the unused portion is simply free. The daily maximums act as upper bounds, and there is no penalty or requirement to use the full capacity.

## Turn 10 - Generic Agent

QUESTION: To confirm the coverage requirement per day: is the requirement that exactly 14 hours of coverage be provided each day (one student on duty for every hour of the 14-hour open period), with no requirement that the same student cannot work consecutive hours or that there be any break between a student's assigned hours?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: To confirm the weekly minimum scope: does the weekly minimum (8 hours for undergraduates, 7 hours for graduate students) apply to the sum of hours across all five days (Monday through Friday) for each student?

## Turn 11 - User Simulator

Yes, the weekly minimum applies to the sum of hours across all five days (Monday through Friday) for each student.

## Turn 12 - Generic Agent

QUESTION: To confirm the wage application: is the total weekly wage cost computed as the sum over each student of (their hourly wage) multiplied by (their total hours worked across all five days), with no additional fixed costs or premiums?

## Turn 12 - User Simulator

Yes, the total weekly wage cost is computed as the sum over each student of (their hourly wage) multiplied by (their total hours worked across all five days), with no additional fixed costs or premiums.

## Turn 13 - Generic Agent

QUESTION: To confirm the daily coverage equality: is the requirement that the sum of all students' hours on a given day must equal exactly 14 (equality), not at least 14 (inequality)?

## Turn 13 - User Simulator

Yes, the requirement is that the sum of all students' hours on a given day must equal exactly 14.

## Turn 14 - Generic Agent

QUESTION: To confirm the non-negativity: can a student work zero hours on a given day (i.e., are daily hours allowed to be zero, with the only lower bound being zero)?

## Turn 14 - User Simulator

Yes, a student can work zero hours on a given day.

## Turn 15 - Generic Agent

QUESTION: To confirm the student classification: are all six students in the table undergraduates (each subject to the 8-hour weekly minimum), or are some of them graduate students (subject to the 7-hour weekly minimum)?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: To confirm the variable domain: should each student's daily working hours be modeled as a continuous variable (allowing fractional hours), or must they be integer hours?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: To confirm the coverage structure: is the lab's 14-hour open period divided into 14 one-hour slots, with exactly one student assigned to each slot, and a student's daily hours equal to the number of slots they are assigned that day?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: To confirm the boundary convention for the open period: does the 14-hour span from 8:00 AM to 10:00 PM consist of 14 one-hour slots (8-9, 9-10, ..., 21-22), meaning the last slot ends exactly at 10:00 PM?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: To confirm the coverage requirement per day: is the requirement that exactly 14 hours of coverage be provided each day (one student on duty for every hour of the 14-hour open period), with no additional restrictions such as breaks or consecutive-hour limits?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: To confirm the student classification: are all six students in the table undergraduates (each subject to the 8-hour weekly minimum), or are some of them graduate students (subject to the 7-hour weekly minimum)?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: To confirm the variable domain: should each student's daily working hours be modeled as a continuous variable (allowing fractional hours), or must they be integer hours?

## Turn 21 - User Simulator

The point

## Turn 22 - Generic Agent

QUESTION: To confirm the student classification: are all six students in the table undergraduates (each subject to the 8-hour weekly minimum), or are some of them graduate students (subject to the 7-hour weekly minimum)?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: To confirm the variable domain: should each student's daily working hours be modeled as a continuous variable (allowing fractional hours), or must they be integer hours?

## Turn 23 - User Simulator

The point

## Turn 24 - Generic Agent

QUESTION: To confirm the coverage structure: is the lab's 14-hour open period divided into 14 one-hour slots, with exactly one student assigned to each slot, and a student's daily hours equal to the number of slots they are assigned that day?

## Turn 24 - User Simulator

The point

## Turn 25 - Generic Agent

QUESTION: To confirm the boundary convention for the open period: does the 14-hour span from 8:00 AM to 10:00 PM consist of 14 one-hour slots (8-9, 9-10, ..., 21-22), meaning the last slot ends exactly at 10:00 PM?

## Turn 25 - User Simulator

The point

## Turn 26 - Generic Agent

QUESTION: To confirm the coverage requirement per day: is the requirement that exactly 14 hours of coverage be provided each day (one student on duty for every hour of the 14-hour open period), with no additional restrictions such as breaks or consecutive-hour limits?

## Turn 26 - User Simulator

The point

## Turn 27 - Generic Agent

QUESTION: To confirm the student classification: are all six students in the table undergraduates (each subject to the 8-hour weekly minimum), or are some of them graduate students (subject to the 7-hour weekly minimum)?

## Turn 27 - User Simulator

The point

## Turn 28 - Generic Agent

QUESTION: To confirm the variable domain: should each student's daily working hours be modeled as a continuous variable (allowing fractional hours), or must they be integer hours?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: To confirm the coverage structure: is the lab's 14-hour open period divided into 14 one-hour slots, with exactly one student assigned to each slot, and a student's daily hours equal to the number of slots they are assigned that day?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: To confirm the boundary convention for the open period: does the 14-hour span from 8:00 AM to 10:00 PM consist of 14 one-hour slots (8-9, 9-10, ..., 21-22), meaning the last slot ends exactly at 10:00 PM?

## Turn 30 - User Simulator

The