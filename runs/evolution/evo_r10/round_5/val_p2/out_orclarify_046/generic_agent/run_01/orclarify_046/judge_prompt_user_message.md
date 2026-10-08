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

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) with exactly one student on duty at all times — does this mean the 14 hours of coverage each day must be split among students in whole-hour blocks (e.g., a student works 3 consecutive hours), or can a student's shift be any combination of hours as long as the total per day matches the coverage?

## Turn 2 - User Simulator

The 14 hours of coverage each day must be split among students in whole-hour blocks.

## Turn 3 - Generic Agent

QUESTION: When a student works a whole-hour block on a given day, must their hours that day be consecutive (one single shift), or can a student work multiple separate blocks on the same day (e.g., 2 hours in the morning and 3 hours in the evening)?

## Turn 3 - User Simulator

I need to confirm this internally.

## Turn 4 - Generic Agent

QUESTION: The table gives a maximum number of hours per student per day — is this maximum a hard cap (the student cannot work more than that many hours that day), or is it a target that should be met exactly?

## Turn 4 - User Simulator

It is a hard cap; the student cannot work more than that many hours that day.

## Turn 5 - Generic Agent

QUESTION: The minimum weekly hours (8 for undergraduates, 7 for graduates) — are these hard lower bounds that must be satisfied in every feasible schedule, or are they soft targets that can be relaxed if needed?

## Turn 5 - User Simulator

They are hard lower bounds that must be satisfied in every feasible schedule.

## Turn 6 - Generic Agent

QUESTION: Which of the six students are undergraduates and which are graduate students, so I can apply the correct minimum weekly hours (8 vs 7) to each?

## Turn 6 - User Simulator

I need to confirm this internally.

## Turn 7 - Generic Agent

QUESTION: The lab is open 8:00 AM to 10:00 PM every day Monday through Friday — is the lab open on all five days, or are there days when it is closed?

## Turn 7 - User Simulator

The lab is open on all five days, Monday through Friday.

## Turn 8 - Generic Agent

QUESTION: Since the lab needs 14 hours of coverage each day and the maximum daily hours per student are given in the table, is it acceptable for a student whose maximum is 0 on a particular day to simply not work at all that day?

## Turn 8 - User Simulator

Yes, a student whose maximum is 0 on a particular day simply does not work that day.

## Turn 9 - Generic Agent

QUESTION: The 14 hours of daily coverage must be split among students in whole-hour blocks — is there any constraint on which specific hours of the day a student can work (e.g., a student cannot work past 10 PM, or must work within certain time windows), or can any student cover any whole hour from 8 AM to 10 PM as long as their daily total doesn't exceed their cap?

## Turn 9 - User Simulator

Any student can cover any whole hour from 8 AM to 10 PM as long as their daily total doesn't exceed their cap.

## Turn 10 - Generic Agent

QUESTION: The minimum weekly hours (8 for undergraduates, 7 for graduates) — do these apply to the total hours worked across all five days combined, or is there also a per-day minimum?

## Turn 10 - User Simulator

They apply to the total hours worked across all five days combined.

## Turn 11 - Generic Agent

QUESTION: Are there any constraints on the total number of hours a student can work across the entire week (a weekly cap), or is the only weekly constraint the minimum (8 or 7 hours)?

## Turn 11 - User Simulator

There is no weekly cap beyond the daily maximums in the table. The only weekly constraint is the minimum (8 or 7 hours).

## Turn 12 - Generic Agent

QUESTION: The model will assign each student a number of whole hours per day (0 up to their daily cap), with the sum across all students equaling 14 each day. Is the decision variable simply "how many hours does each student work on each day" (an integer from 0 to their cap), with no further structure needed about which specific hours they cover?

## Turn 12 - User Simulator

Yes, the decision variable is simply how many hours each student works on each day, an integer from 0 to their cap, with no further structure needed about which specific hours they cover.

## Turn 13 - Generic Agent

QUESTION: Regarding the undergraduate vs. graduate classification — since you need to confirm this internally, would it be acceptable for me to proceed with the model using a parameter (e.g., a list specifying which students are undergrads and which are grads) that can be filled in later, rather than hard-coding a specific assignment?

## Turn 13 - User Simulator

Yes, that is acceptable.

## Turn 14 - Generic Agent

QUESTION: Regarding the consecutive-shift question you deferred earlier — for the purpose of this model, is it acceptable to proceed with the assumption that a student's hours on a given day do NOT need to be consecutive (i.e., they can work any combination of whole hours up to their daily cap), since the decision variable is just the total hours per day?

## Turn 14 - User Simulator

Yes, that is acceptable.

## Turn 15 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Minimize total weekly labor cost = sum over all students of (hourly wage × total hours worked that week).

**Decision variables:** For each student i (1–6) and each day d (Mon–Fri), an integer variable x(i,d) representing the number of whole hours student i works on day d.

**Constraints:**

1. **Daily coverage:** For each day d, the sum of x(i,d) over all students i must equal exactly 14 (the lab is open 8 AM–10 PM, 14 hours, with exactly one student on duty at all times).

2. **Daily caps:** For each student i and day d, x(i,d) ≤ cap(i,d), where cap(i,d) is the value from Table 5-9. If cap is 0, the student does not work that day.

3. **Non-negativity and integrality:** x(i,d) ≥ 0 and integer for all i, d.

4. **Weekly minimums:** For each student i, the sum of x(i,d) over all five days must be at least 8 if student i is an undergraduate, or at least 7 if student i is a graduate student. (The specific undergraduate/graduate classification is a parameter to be filled in.)

**Parameters:**
- Wages: Student 1: 10.0, Student 2: 10.0, Student 3: 9.9, Student 4: 9.8, Student 5: 10.8, Student 6: 11.3 (CNY/hour).
- Daily caps as given in Table 5-9.
- Lab open Monday through Friday, 14 hours per day.
- No weekly cap beyond the daily maximums.
- No consecutive-shift requirement; hours per day are just a total count.
- Any student can cover any hour of the day.

**Model class:** Integer Linear Program (ILP).