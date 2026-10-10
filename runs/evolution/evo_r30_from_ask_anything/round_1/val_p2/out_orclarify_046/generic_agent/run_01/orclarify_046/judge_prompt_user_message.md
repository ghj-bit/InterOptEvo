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

QUESTION: What is the total number of hours the lab is open each day (for example, is it the full 14 hours from 8:00 AM to 10:00 PM every day, or are there different open hours on different days)?

## Turn 1 - User Simulator

The lab is open for the full 14 hours every day, from 8:00 AM to 10:00 PM.

## Turn 2 - Generic Agent

QUESTION: Is the lab open on all five days from Monday through Friday, or are there other days (like weekends) when it is also open and requires coverage?

## Turn 2 - User Simulator

The lab is open Monday through Friday.

## Turn 3 - Generic Agent

QUESTION: Are the students in the table divided into undergraduate and graduate groups, and if so, which specific student IDs are undergraduates and which are graduates?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the undergraduate versus graduate classification is still being confirmed internally, should I proceed by treating all six students as having the same minimum weekly requirement of 8 hours, or would you prefer I hold off on that constraint until the classification is finalized?

## Turn 4 - User Simulator

Please hold off on that constraint until the classification is finalized.

## Turn 5 - Generic Agent

QUESTION: Is the primary goal of the scheduling plan to minimize the total weekly labor cost, or is there another objective such as maximizing fairness or minimizing total hours worked?

## Turn 5 - User Simulator

The primary goal is to minimize the total weekly labor cost.

## Turn 6 - Generic Agent

QUESTION: Are the maximum duty hours listed in Table 5-9 hard upper limits that cannot be exceeded, or are they targets that can be exceeded if necessary to cover the lab hours?

## Turn 6 - User Simulator

They are hard upper limits that cannot be exceeded.

## Turn 7 - Generic Agent

QUESTION: Can a student work multiple separate shifts on the same day, or is each student limited to a single continuous block of hours per day?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the shift structure is still being confirmed, should I proceed by assuming each student can work any combination of hours up to their daily maximum, or would you prefer I hold off on modeling the daily schedule until that detail is finalized?

## Turn 8 - User Simulator

Please hold off on modeling the daily schedule until that detail is finalized.

## Turn 9 - Generic Agent

QUESTION: Is the requirement for "one and only one student on duty" meant to ensure that the lab is staffed for the entire 14-hour period every day, or is it just a constraint that no two students can be scheduled at the same time?

## Turn 9 - User Simulator

It means the lab must be staffed for the entire 14-hour period every day, with exactly one student on duty at any given time.

## Turn 10 - Generic Agent

QUESTION: Are the daily maximum hours in Table 5-9 the total hours a student can work that day, or are they the maximum length of a single continuous shift?

## Turn 10 - User Simulator

They are the total hours a student can work that day.

## Turn 11 - Generic Agent

QUESTION: Can a student work multiple separate shifts on the same day as long as their total hours do not exceed the daily maximum, or is each student limited to a single continuous block of hours per day?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Since the shift structure is still being confirmed, should I proceed by assuming each student can work any combination of hours up to their daily maximum, or would you prefer I hold off on modeling the daily schedule until that detail is finalized?

## Turn 12 - User Simulator

Please hold off on modeling the daily schedule until that detail is finalized.

## Turn 13 - Generic Agent

QUESTION: Are the working hours for each student required to be whole numbers, or can they be fractional (e.g., 0.5 hours)?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the integrality of working hours is still being confirmed, should I proceed by assuming all working hours must be whole numbers, or would you prefer I hold off on that constraint until it is finalized?

## Turn 14 - User Simulator

Please hold off on that constraint until it is finalized.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or preferences for the scheduling plan, such as limits on consecutive days worked, required days off, or fairness considerations, that I should be aware of?

## Turn 15 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 16 - Generic Agent

QUESTION: Given that the lab is open for 14 hours every day and each student can work at most 2 shifts per week, does the definition of a "shift" refer to a single continuous block of hours, or can a shift be any arbitrary set of hours within a day?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Since the definition of a "shift" is still being confirmed, should I proceed by assuming a shift is a single continuous block of hours, or would you prefer I hold off on modeling the shift count constraint until that detail is finalized?

## Turn 17 - User Simulator

Please hold off on modeling the shift count constraint until that detail is finalized.

## Turn 18 - Generic Agent

QUESTION: Are there any other constraints or preferences for the scheduling plan, such as limits on consecutive days worked, required days off, or fairness considerations, that I should be aware of?

## Turn 18 - User Simulator

No, there are no other constraints or preferences beyond what has already been discussed.

## Turn 19 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize the total weekly labor cost.
2.  **Time Horizon:** Monday through Friday.
3.  **Lab Hours:** The lab is open for 14 hours every day (8:00 AM to 10:00 PM).
4.  **Coverage Requirement:** Exactly one student must be on duty at any given time, ensuring the lab is fully staffed for the entire 14-hour period each day.
5.  **Daily Capacity:** Each student’s total working hours on a given day cannot exceed the maximum hours specified in Table 5-9. These are hard upper limits.
6.  **Student Data:**
    *   Student 1: Wage 10.0 CNY/h; Max hours: Mon 6, Tue 0, Wed 6, Thu 0, Fri 7.
    *   Student 2: Wage 10.0 CNY/h; Max hours: Mon 0, Tue 8, Wed 9, Thu 6, Fri 0.
    *   Student 3: Wage 9.9 CNY/h; Max hours: Mon 4, Tue 8, Wed 3, Thu 0, Fri 5.
    *   Student 4: Wage 9.8 CNY/h; Max hours: Mon 5, Tue 5, Wed 6, Thu 0, Fri 4.
    *   Student 5: Wage 10.8 CNY/h; Max hours: Mon 3, Tue 0, Wed 5, Thu 8, Fri 0.
    *   Student 6: Wage 11.3 CNY/h; Max hours: Mon 0, Tue 6, Wed 0, Thu 6, Fri 5.
7.  **Daily Diversity Constraint:** No more than 3 different students can be scheduled for duty on any single day.

**Open Assumptions (Held Off Pending Confirmation):**

1.  **Minimum Weekly Hours:** The specific minimum weekly hours (8 hours for undergraduates, 7 hours for graduates) are **not included** in the current model because the classification of students into undergraduate and graduate groups is pending internal confirmation.
2.  **Shift Structure:** The model does **not** currently enforce a limit on the number of shifts per week or define what constitutes a "shift" (continuous block vs. arbitrary hours), as this definition is pending internal confirmation. The model currently assumes students can work any combination of hours up to their daily maximums, subject to the "one student at a time" and "max 3 students per day" constraints.
3.  **Integrality:** The model does **not** currently enforce that working hours must be whole numbers, as this is pending internal confirmation. The model currently allows for fractional hours if necessary to meet the coverage and cost objectives.