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

QUESTION: Is the lab's open hours (8:00 AM to 10:00 PM) divided into discrete time slots (e.g., hourly blocks) for scheduling, and if so, how many such slots are there per day?

## Turn 1 - User Simulator

The lab's open hours are not divided into discrete time slots. The scheduling is based on continuous hours, where a student can work any number of hours up to their daily maximum, as long as the total hours for the day are covered by exactly one student on duty.

## Turn 2 - Generic Agent

QUESTION: Since exactly one student is on duty for the entire 14-hour open period each day, does the "maximum duty hours" in Table 5-9 represent a hard upper limit on how many of those 14 hours a specific student can work on that day, meaning if a student's max is less than 14, they simply cannot be assigned to cover the full day?

## Turn 2 - User Simulator

Yes, the "maximum duty hours" in Table 5-9 represent a hard upper limit on how many hours a specific student can work on that day. If a student's maximum is less than 14, they cannot be assigned to cover the full day alone.

## Turn 3 - Generic Agent

QUESTION: Since the lab is open for 14 hours daily but no student has a maximum daily limit of 14 hours or more, how is the requirement for "one and only one student on duty" satisfied if a single student cannot cover the entire 14-hour period?

## Turn 3 - User Simulator

The requirement for "one and only one student on duty" means that at any given moment during the 14-hour open period, exactly one student is present. It does not mean that a single student must work the entire 14 hours continuously. Multiple students can work different portions of the day, as long as their shifts do not overlap and their individual daily hours do not exceed their maximums from Table 5-9.

## Turn 4 - Generic Agent

QUESTION: Are the shifts for each student on a given day required to be contiguous (i.e., one single block of time), or can a student's daily hours be split into multiple non-contiguous blocks as long as they do not overlap with other students' shifts?

## Turn 4 - User Simulator

The shifts for each student on a given day are required to be contiguous (one single block of time).

## Turn 5 - Generic Agent

QUESTION: Is the primary objective of this scheduling plan to minimize the total weekly labor cost (sum of hours worked multiplied by hourly wage for all students), or is there a different goal such as maximizing fairness or minimizing the number of students used?

## Turn 5 - User Simulator

The primary objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 6 - Generic Agent

QUESTION: Are there any constraints on the number of days per week each student is allowed to work, or can a student work on any subset of the five days (Monday through Friday) as long as their daily and weekly hour limits are met?

## Turn 6 - User Simulator

There is a constraint that each student cannot work more than 2 shifts in a week.

## Turn 7 - Generic Agent

QUESTION: Does the constraint that each student cannot work more than 2 shifts in a week apply to all students, or are there specific students who are exempt from this limit?

## Turn 7 - User Simulator

The constraint that each student cannot work more than 2 shifts in a week applies to all students.

## Turn 8 - Generic Agent

QUESTION: Are there any constraints on the specific days of the week a student can work, such as requiring a rest day between shifts or prohibiting work on certain days, or can a student work on any two days of the week as long as the daily hour limits are respected?

## Turn 8 - User Simulator

There are no constraints on the specific days of the week a student can work, such as requiring a rest day between shifts or prohibiting work on certain days. A student can work on any two days of the week as long as the daily hour limits are respected.

## Turn 9 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the scheduling plan that have not been mentioned yet, such as minimum or maximum total hours per student per week beyond the stated minimums, or specific preferences for shift start or end times?

## Turn 9 - User Simulator

There is one additional constraint: no more than 3 students can be scheduled for duty each day.

## Turn 10 - Generic Agent

QUESTION: Is the constraint that no more than 3 students can be scheduled for duty each day a hard limit, meaning it is strictly forbidden to have 4 or more students working on the same day, or is it a soft target that can be violated if necessary to meet the other requirements?

## Turn 10 - User Simulator

It is a hard limit. It is strictly forbidden to have 4 or more students working on the same day.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective**: Minimize total weekly labor cost, calculated as the sum of (hours worked × hourly wage) for all students.
2.  **Time Horizon**: Monday through Friday.
3.  **Daily Operation**: The lab is open for 14 hours each day (8:00 AM to 10:00 PM).
4.  **Coverage Requirement**: The total hours worked by all students on any given day must sum to exactly 14 hours.
5.  **Shift Structure**:
    *   Each student's shift on a given day is a single contiguous block of time.
    *   Shifts for different students on the same day must not overlap.
    *   Since shifts are contiguous and non-overlapping, and must cover the full 14 hours, the schedule for each day is a partition of the 14-hour interval into contiguous segments assigned to specific students.
6.  **Student Constraints**:
    *   **Weekly Minimums**: Each undergraduate must work at least 8 hours per week. Each graduate student must work at least 7 hours per week. *(Note: The brief does not specify which students are undergraduates and which are graduates. This is a critical missing piece of information.)*
    *   **Daily Maximums**: A student's hours on a specific day cannot exceed the value in Table 5-9 for that day.
    *   **Weekly Shift Limit**: Each student can work on at most 2 days per week.
    *   **Daily Student Limit**: No more than 3 students can be scheduled on any single day.
7.  **Data**:
    *   Wages and daily maximum hours are provided in Table 5-9 for 6 students.

**Open Assumptions / Missing Information:**

1.  **Student Classification**: The brief states minimums for "undergraduate" and "graduate" students but does not specify which of the 6 students (IDs 1-6) fall into which category. This is required to apply the correct weekly minimum constraint (8 hours vs. 7 hours) to each student.
2.  **Shift Timing**: While the model needs to ensure shifts are contiguous and non-overlapping, the specific start and end times of each shift are decision variables. The model will determine the sequence of students and the duration of their shifts to cover the 14 hours.

**Clarification Needed Before Final Formulation:**
Which students (IDs 1-6) are undergraduates and which are graduates?

## Turn 11 - User Simulator

Students 1, 2, and 3 are undergraduates. Students 4, 5, and 6 are graduates.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective**: Minimize total weekly labor cost, calculated as the sum of (hours worked × hourly wage) for all students.
2.  **Time Horizon**: Monday through Friday.
3.  **Daily Operation**: The lab is open for 14 hours each day (8:00 AM to 10:00 PM).
4.  **Coverage Requirement**: The total hours worked by all students on any given day must sum to exactly 14 hours.
5.  **Shift Structure**:
    *   Each student's shift on a given day is a single contiguous block of time.
    *   Shifts for different students on the same day must not overlap.
    *   The schedule for each day is a partition of the 14-hour interval into contiguous segments assigned to specific students.
6.  **Student Classification**:
    *   **Undergraduates**: Students 1, 2, and 3.
    *   **Graduates**: Students 4, 5, and 6.
7.  **Student Constraints**:
    *   **Weekly Minimums**:
        *   Undergraduates (1, 2, 3) must work at least 8 hours per week.
        *   Graduates (4, 5, 6) must work at least 7 hours per week.
    *   **Daily Maximums**: A student's hours on a specific day cannot exceed the value in Table 5-9 for that day.
    *   **Weekly Shift Limit**: Each student can work on at most 2 days per week.
    *   **Daily Student Limit**: No more than 3 students can be scheduled on any single day.
8.  **Data**:
    *   Wages and daily maximum hours are provided in Table 5-9 for 6 students.

**Open Assumptions:**

None. All formulation-critical facts have been confirmed.