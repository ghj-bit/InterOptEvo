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

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times — does this mean the 14 hours each day are divided into 14 one-hour slots, and each student's daily hours must be an integer number of these slots?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Since the slot structure is still being confirmed internally, may I proceed on the assumption that each day is divided into 14 one-hour slots (8:00–9:00, 9:00–10:00, …, 21:00–22:00) and each student's daily hours are whole numbers of slots?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Setting the slot question aside for now, do the weekly minimums (8 hours for undergraduates, 7 hours for graduates) apply to every student individually, or only to students who are actually scheduled to work at least once that week?

## Turn 4 - User Simulator

The weekly minimums apply to every student individually.

## Turn 5 - Generic Agent

QUESTION: Which of the six students are undergraduates and which are graduate students, so I can apply the 8-hour and 7-hour weekly minimums to the right people?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: While the undergraduate/graduate split is being confirmed, is there any other rule about which students may work on which days — for example, must a student's daily hours be zero on days where Table 5-9 shows 0, or can a student work on any day up to the listed maximum?

## Turn 6 - User Simulator

A student's daily hours must be zero on days where Table 5-9 shows 0.

## Turn 7 - Generic Agent

QUESTION: The lab needs exactly one student on duty for all 14 hours each day, so the sum of all students' hours on any given day must equal 14 — is that correct, or could the lab be understaffed on some days?

## Turn 7 - User Simulator

Yes, the sum of all students' hours on any given day must equal 14.

## Turn 8 - Generic Agent

QUESTION: Are the daily hours each student works required to be whole numbers (e.g., 3 hours, not 2.5 hours), or can a student work fractional hours within a day?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Do the six students have any other restrictions beyond what is in Table 5-9 — for example, a limit on how many days per week a student can work, or a requirement that a student's hours on a given day must be contiguous (one block) rather than split across the day?

## Turn 9 - User Simulator

Each student cannot work more than 2 shifts in a week.

## Turn 10 - Generic Agent

QUESTION: When you say a student cannot work more than 2 shifts in a week, does "shift" mean a single contiguous block of hours on one day (so a student could work, say, 3 hours Monday and 4 hours Wednesday = 2 shifts), or does it mean a student can be on duty on at most 2 different days per week?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: While the shift definition is being confirmed, is there a maximum total number of hours any single student can work in a week, beyond the daily caps in Table 5-9?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there any requirement that a student's hours on a given day must form one contiguous block (e.g., 10:00–13:00), or can a student's hours on the same day be split into separate periods (e.g., 8:00–10:00 and 14:00–16:00)?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Since several operational details are still being confirmed internally, may I proceed with the following working assumptions for the model: (1) each day is 14 one-hour slots, (2) daily hours are whole numbers, (3) a student's hours on a day form one contiguous block, and (4) "at most 2 shifts per week" means at most 2 days per week — and you will flag any of these that turn out to be wrong?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any requirement about which specific hours within the 8:00 AM to 10:00 PM window a student must cover — for example, must the first hour (8:00–9:00) and last hour (21:00–22:00) always be covered, or can any student work any hour as long as exactly one student is present each hour?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or preferences I should know about that are not yet captured — such as a preference for spreading hours evenly across students, a requirement that at least one graduate student be on duty at all times, or a cap on total weekly labor cost?

## Turn 15 - User Simulator

No, there are no other constraints or preferences beyond what has already been discussed.

## Turn 16 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the duty scheduling problem:

**Setting**
- A university computer lab is open Monday–Friday, 8:00 AM to 10:00 PM (14 hours per day, 70 hours per week).
- Exactly one student must be on duty at all times, so the sum of all students' hours on each day must equal 14.

**Workers**
- Six students (IDs 1–6), each with an hourly wage and per-day maximum hours as given in Table 5-9.
- A student's daily hours must be zero on any day where Table 5-9 shows 0.

**Objective**
- Minimize total weekly labor cost = Σ (wage_i × total hours worked by student i that week).

**Constraints**
1. **Daily coverage:** For each of the 5 days, the sum of all students' hours equals exactly 14.
2. **Daily caps:** Each student's hours on a given day ≤ the value in Table 5-9 (and = 0 where the table shows 0).
3. **Weekly minimums:** Each undergraduate works ≥ 8 hours/week; each graduate student works ≥ 7 hours/week. (The undergraduate/graduate classification for each of the six students is still pending internal confirmation; I will parameterize it so it can be plugged in.)
4. **Shift limit:** Each student works at most 2 shifts per week. (The precise definition of "shift" — contiguous block vs. distinct day — is pending confirmation; I will model it as at most 2 days per week as the working assumption.)
5. **Integrality / slot structure:** Daily hours are assumed to be whole numbers of one-hour slots (pending confirmation).

**Items still pending internal confirmation (to be parameterized):**
- Undergraduate vs. graduate status of each student.
- Exact definition of "shift" (contiguous block vs. day).
- Whether hours are integer (slot-based) or can be fractional.
- Whether a student's hours on a day must be contiguous.

I will build the model with these as clearly-marked parameters/assumptions so the confirmed values can be dropped in without restructuring.