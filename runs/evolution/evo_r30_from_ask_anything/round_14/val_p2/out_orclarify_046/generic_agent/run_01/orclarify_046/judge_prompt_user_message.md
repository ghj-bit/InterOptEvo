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

QUESTION: What is the objective of the scheduling plan — are we minimizing total weekly labor cost, minimizing total hours worked, or something else?

## Turn 1 - User Simulator

We are minimizing the total weekly labor cost. That is the sum of each student's hourly wage multiplied by their total hours worked during the week.

## Turn 2 - Generic Agent

QUESTION: The lab is open from 8:00 AM to 10:00 PM, which is 14 hours per day. Does "one and only one student on duty" mean that exactly one student must be assigned to work the entire 14-hour block each day, or are the 14 hours divided into smaller shifts (e.g., 2-hour or 4-hour blocks) where different students can cover different blocks?

## Turn 2 - User Simulator

The 14 hours are divided into smaller shifts. Different students can cover different blocks, but at any given time, exactly one student must be on duty.

## Turn 3 - Generic Agent

QUESTION: What is the length of each shift block — for example, are the 14 hours divided into 7 two-hour shifts, 2 seven-hour shifts, or some other configuration?

## Turn 3 - User Simulator

I need to confirm the exact shift block length internally.

## Turn 4 - Generic Agent

QUESTION: Since the exact shift block length is unconfirmed, I will proceed with the assumption that the 14 hours are divided into 14 one-hour slots, and a student can work any subset of those slots subject to their daily maximum. Is that assumption acceptable, or would you prefer I use a different granularity?

## Turn 4 - User Simulator

That assumption is acceptable.

## Turn 5 - Generic Agent

QUESTION: Are there any constraints on how many consecutive hours a student can work in a single day, or can a student work any combination of the 14 one-hour slots as long as the total does not exceed their daily maximum?

## Turn 5 - User Simulator

A student can work any combination of the 14 one-hour slots as long as the total does not exceed their daily maximum.

## Turn 6 - Generic Agent

QUESTION: The table shows maximum hours for Monday through Friday only. Does the lab operate on weekends (Saturday and Sunday), or is the scheduling period strictly Monday through Friday?

## Turn 6 - User Simulator

The scheduling period is strictly Monday through Friday.

## Turn 7 - Generic Agent

QUESTION: The minimum weekly hours are stated as "at least 8 hours per week" for undergraduates and "at least 7 hours per week" for graduates. Are these minimums hard constraints that must be strictly satisfied, or are they soft targets that can be violated if necessary?

## Turn 7 - User Simulator

They are hard constraints that must be strictly satisfied.

## Turn 8 - Generic Agent

QUESTION: Are there any upper bounds on the total weekly hours a student can work, or is the only weekly limit the minimum (8 hours for undergrads, 7 hours for graduates)?

## Turn 8 - User Simulator

There is an upper bound: each student cannot work more than 2 shifts in a week.

## Turn 9 - Generic Agent

QUESTION: You mentioned a limit of 2 shifts per week, but we previously established that the 14 hours are divided into 14 one-hour slots. Does "2 shifts" mean a student can work on at most 2 different days per week, or does it mean something else?

## Turn 9 - User Simulator

It means a student can work on at most 2 different days per week.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or requirements I have not yet covered, such as restrictions on which students can work together, mandatory days off, or preferences for specific students on specific days?

## Turn 10 - User Simulator

Yes, there is one more constraint: no more than 3 different students can be scheduled for duty in a single day.

## Turn 11 - Generic Agent

QUESTION: Are there any restrictions on which students are classified as undergraduates versus graduates, or can I assume that the classification is fixed and known for each student ID?

## Turn 11 - User Simulator

The classification is fixed and known for each student ID.

## Turn 12 - Generic Agent

QUESTION: Can you provide the specific classification (undergraduate or graduate) for each of the six student IDs listed in the table?

## Turn 12 - User Simulator

I need to confirm the specific classification for each student ID internally.

## Turn 13 - Generic Agent

QUESTION: Since the specific classification for each student ID is unconfirmed, I will proceed with the assumption that the classification is a fixed input parameter that will be provided when the model is implemented. Is that acceptable, or would you prefer I make a specific assumption about which students are undergraduates versus graduates?

## Turn 13 - User Simulator

That is acceptable.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Minimize total weekly labor cost, calculated as the sum of each student's hourly wage multiplied by their total hours worked over the week.

2. **Scheduling Period:** Monday through Friday only (5 days).

3. **Lab Hours:** 8:00 AM to 10:00 PM each day, totaling 14 hours per day.

4. **Shift Granularity:** The 14 hours per day are divided into 14 one-hour slots. A student can work any combination of these slots subject to their daily maximum.

5. **Coverage Constraint:** At every one-hour slot, exactly one student must be on duty.

6. **Student Classification:** Each student is either an undergraduate or a graduate. This classification is a fixed input parameter to be provided at implementation time.

7. **Minimum Weekly Hours (Hard Constraints):**
   - Each undergraduate must work at least 8 hours per week.
   - Each graduate must work at least 7 hours per week.

8. **Daily Maximum Hours (Hard Constraints):** Each student's hours on a given day cannot exceed the maximum specified in Table 5-9 for that day.

9. **Weekly Day Limit (Hard Constraint):** Each student can work on at most 2 different days per week.

10. **Daily Student Limit (Hard Constraint):** No more than 3 different students can be scheduled for duty in a single day.

11. **Wages:** As specified in Table 5-9 (ranging from 9.8 to 11.3 CNY/hour).

**Assumptions:**

- The specific undergraduate/graduate classification for each student ID will be provided as an input parameter when the model is implemented.
- There are no other constraints beyond those listed above (no consecutive-hour restrictions, no mandatory days off, no student-specific day preferences, no mutual exclusivity rules beyond those stated).