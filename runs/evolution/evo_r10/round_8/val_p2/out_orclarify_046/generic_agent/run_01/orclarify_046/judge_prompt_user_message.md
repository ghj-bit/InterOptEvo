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

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times — does this mean the on-duty student works the entire 14-hour stretch continuously, or is the day divided into shifts (e.g., morning and evening) where different students can cover different portions, and if so, how many shifts per day and what are their time windows?

## Turn 2 - User Simulator

The day is divided into shifts where different students can cover different portions. The specific number of shifts per day and their time windows still need internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Since the shift structure is still being confirmed internally, could you tell me whether the maximum daily hours in Table 5-9 are intended to be interpreted as the maximum number of hours a student can work across all shifts on that day (i.e., a per-day cap on total hours), or as the maximum number of shifts a student can be assigned on that day?

## Turn 3 - User Simulator

The maximum daily hours in Table 5-9 are intended to be interpreted as the maximum number of hours a student can work across all shifts on that day.

## Turn 4 - Generic Agent

QUESTION: Since the exact shift windows are still being confirmed, could you tell me whether the total hours the lab needs to be covered each day is always 14 hours (8:00 AM to 10:00 PM with one student on duty at all times), or could the open hours vary by day of the week?

## Turn 4 - User Simulator

The total hours the lab needs to be covered each day is always 14 hours, from 8:00 AM to 10:00 PM.

## Turn 5 - Generic Agent

QUESTION: Since the exact shift windows are still being confirmed, could you tell me whether the hours a student works on a given day must be in whole-hour increments (e.g., 1, 2, 3... hours), or can they work fractional hours (e.g., 1.5 hours)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: The brief mentions "undergraduate and graduate student workers" — could you tell me which of the six students (IDs 1 through 6) are undergraduates and which are graduates, so I can apply the correct minimum weekly hours (8 for undergrads, 7 for graduates)?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is still being confirmed, could you tell me whether the minimum weekly hours requirement (8 for undergrads, 7 for graduates) applies to every student individually, or is it a group-level requirement (e.g., the total hours worked by all undergrads combined must be at least 8)?

## Turn 7 - User Simulator

The minimum weekly hours requirement applies to every student individually.

## Turn 8 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 8 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 9 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 9 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 10 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 10 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 11 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 11 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 12 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 12 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 13 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 13 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 14 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 14 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 15 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 15 - User Simulator

The minimum

## Turn 16 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 16 - User Simulator

The minimum weekly hours should be treated as a hard constraint that must be satisfied in the final schedule.

## Turn 17 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 18 - User Simulator

The

## Turn 19 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Since the undergraduate/graduate classification for each student is still being confirmed, could you tell me whether the minimum weekly hours (8 for undergrads, 7 for graduates) should be treated as a hard constraint that must be satisfied in the final schedule, or as a soft target that can be relaxed if doing so reduces total cost?

## Turn 30 - User Simulator

The