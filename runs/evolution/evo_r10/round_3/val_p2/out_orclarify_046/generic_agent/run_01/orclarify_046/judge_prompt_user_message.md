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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, so 14 person-hours are needed each day. However, the maximum daily hours in Table 5-9 sum to only 12 hours on Monday, 18 on Tuesday, 19 on Wednesday, 16 on Thursday, and 21 on Friday — so Monday's 14 hours cannot be covered by the listed maxima. Is the lab actually open for fewer hours on some days (e.g., 8:00 AM to 8:00 PM, 12 hours), or should the Table 5-9 values be treated as soft limits that may be exceeded when needed to cover the full 14 hours?

## Turn 1 - User Simulator

The lab is open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday to Friday. The values in Table 5-9 are hard limits; they cannot be exceeded.

## Turn 2 - Generic Agent

QUESTION: Since the 14 daily person-hours needed cannot be met on Monday (max 12) under the hard limits, is the "one and only one student on duty" requirement meant to apply only during a subset of the 14 hours each day (for example, a core window like 8:00 AM to 8:00 PM), with the remaining hours allowed to have no one on duty?

## Turn 2 - User Simulator

No, the "one and only one student on duty" requirement applies to the entire 14-hour operating window (8:00 AM to 10:00 PM) every day. There are no hours without a student on duty.

## Turn 3 - Generic Agent

QUESTION: Given that the hard daily limits in Table 5-9 sum to only 12 hours on Monday while 14 person-hours are required, is it possible that some students are not limited by the table on certain days — for example, that a zero in the table means the student is unavailable that day, but a non-zero value is a soft cap that can be exceeded if necessary to reach 14 hours?

## Turn 3 - User Simulator

No. The values in Table 5-9 are hard limits for all students on all days. A zero means the student is unavailable that day, and a non-zero value is the maximum number of hours that student can work that day. These limits cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Since the hard limits make Monday infeasible (max 12 hours vs. 14 required), should the model instead minimize the total labor cost while covering as many of the 14 hours per day as possible (i.e., allow some hours to go uncovered when infeasible), or should the model treat the 14-hour coverage as a hard requirement and report infeasibility for Monday?

## Turn 4 - User Simulator

The 14-hour coverage is a hard requirement. The model should treat it as such and report infeasibility for Monday if the constraints cannot be satisfied.

## Turn 5 - Generic Agent

QUESTION: The model should minimize total weekly labor cost (sum of wage × hours for each student-day), subject to the 14-hour daily coverage, the weekly minimums (8h undergrad, 7h grad), and the hard daily caps — is that the correct objective, or is there a different objective (e.g., minimize total hours, maximize fairness, etc.)?

## Turn 5 - User Simulator

Yes, the objective is to minimize total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 6 - Generic Agent

QUESTION: Which of the six students are undergraduates and which are graduate students, so I can apply the correct weekly minimum (8 hours for undergrads, 7 hours for grads)?

## Turn 6 - User Simulator

I need to confirm internally which students are undergraduates and which are graduate students.

## Turn 7 - Generic Agent

QUESTION: Are the decision variables (hours worked by each student on each day) intended to be continuous (allowing fractional hours like 2.5), or must they be integer numbers of hours?

## Turn 7 - User Simulator

The decision variables are continuous; fractional hours are allowed.

## Turn 8 - Generic Agent

QUESTION: For the weekly minimums (8 hours for undergrads, 7 hours for grads), should these be treated as hard constraints (the model must satisfy them or be infeasible), or as soft constraints that can be relaxed if needed to find a feasible schedule?

## Turn 8 - User Simulator

The weekly minimums are hard constraints.

## Turn 9 - Generic Agent

QUESTION: Since the student classification (undergrad vs. grad) is still pending your internal confirmation, should I proceed with the model using a placeholder assumption — for example, treating students 1–3 as undergraduates (8h minimum) and students 4–6 as graduate students (7h minimum) — so that you can simply swap the labels once confirmed, or would you prefer to wait until the classification is finalized before I write the model?

## Turn 9 - User Simulator

Please wait until the classification is finalized before writing the model.

## Turn 10 - Generic Agent

QUESTION: While waiting for the student classification, is there any other constraint or detail I should confirm — for example, whether a student who works on a given day must work a contiguous block of hours, or whether their hours can be split across non-adjacent time slots within the 14-hour window?

## Turn 10 - User Simulator

A student's hours on a given day must be a contiguous block.

## Turn 11 - Generic Agent

QUESTION: For the contiguous block requirement, does the start time of a student's shift need to be on the hour (e.g., 8:00, 9:00, 10:00, etc.), or can it start at any time within the 14-hour window (e.g., 8:30, 9:15)?

## Turn 11 - User Simulator

The start time of a student's shift must be on the hour.

## Turn 12 - Generic Agent

QUESTION: Since only one student is on duty at any time and each student's shift is a contiguous block starting on the hour, does this mean the 14-hour day is partitioned into consecutive on-the-hour segments, each assigned to exactly one student, with no gaps and no overlaps?

## Turn 12 - User Simulator

Yes, the 14-hour day is partitioned into consecutive on-the-hour segments, each assigned to exactly one student, with no gaps and no overlaps.

## Turn 13 - Generic Agent

QUESTION: Can a single student be assigned to two separate non-adjacent blocks on the same day (e.g., hours 8-10 and hours 14-16), or must each student's daily hours form exactly one contiguous block?

## Turn 13 - User Simulator

Each student's daily hours must form exactly one contiguous block.

## Turn 14 - Generic Agent

QUESTION: Is there a maximum number of students who can be assigned shifts on any single day, or is there no limit on how many students can work in a day as long as the 14-hour partition is satisfied?

## Turn 14 - User Simulator

No more than 3 students can be scheduled for duty on any single day.

## Turn 15 - Generic Agent

QUESTION: Is there a limit on how many days per week a single student can be scheduled (e.g., a student cannot work more than 3 days out of the 5), or can a student work on any or all 5 days as long as the daily caps and weekly minimums are satisfied?

## Turn 15 - User Simulator

Each student can work no more than 2 shifts per week.

## Turn 16 - Generic Agent

QUESTION: Does "no more than 2 shifts per week" mean each student can be assigned to at most 2 of the 5 days (i.e., work on at most 2 distinct days), or does it mean something else (e.g., at most 2 total blocks across the week, which is the same thing given one block per day)?

## Turn 16 - User Simulator

It means each student can be assigned to at most 2 of the 5 days.

## Turn 17 - Generic Agent

QUESTION: With each student limited to at most 2 days per week and at most 3 students per day, the maximum total person-hours per week is 3 × 5 × (max daily cap) — but more critically, the total available person-hours across all students is limited. Is it acceptable that the model may be infeasible on days other than Monday as well (e.g., Tuesday, Wednesday, Thursday, Friday) due to the combination of the 2-day-per-student limit, the 3-students-per-day limit, and the daily caps, and should the model simply report infeasibility for any day where coverage cannot be met?

## Turn 17 - User Simulator

Yes, the model should report infeasibility for any day where the 14-hour coverage cannot be met given all the constraints.

## Turn 18 - Generic Agent

QUESTION: I understand the student classification (undergrad vs. grad) is still pending your internal confirmation. Is there anything else you'd like to clarify or add before I proceed, or should I note the classification as the sole outstanding item and prepare the model structure so that the classification can be plugged in once confirmed?

## Turn 18 - User Simulator

The student classification is the sole outstanding item. Please prepare the model structure so that the classification can be plugged in once confirmed.

## Turn 19 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Problem:** Duty scheduling for a university computer lab, Monday–Friday, 8:00 AM–10:00 PM (14 hours/day).

**Objective:** Minimize total weekly labor cost = Σ (wage_i × total hours_i across the week).

**Decision Variables:**
- For each student i and day d: a binary variable indicating whether student i is assigned a shift on day d, and if so, the start hour (on-the-hour, from 8 to 21) and duration (integer number of hours, 1–14).
- Equivalently: the 14-hour day is partitioned into consecutive on-the-hour segments, each assigned to exactly one student. Each student's daily hours form exactly one contiguous block.
- Hours are continuous in the sense that fractional hours are allowed, but since shifts start on the hour and the day is partitioned into on-the-hour segments, each segment is 1 hour, so effectively each student's daily hours are integer (number of consecutive 1-hour segments).

**Constraints:**
1. **Coverage:** Every 1-hour segment (8–9, 9–10, …, 21–22) on each day is assigned to exactly one student. No gaps, no overlaps.
2. **Daily caps:** For each student i and day d, hours worked ≤ cap(i, d) from Table 5-9. A zero cap means the student is unavailable that day.
3. **Weekly minimums:** Each undergraduate works ≥ 8 hours/week; each graduate student works ≥ 7 hours/week. (Classification pending — to be plugged in.)
4. **Max students per day:** At most 3 students are assigned shifts on any single day.
5. **Max days per student:** Each student is assigned to at most 2 of the 5 days.
6. **Contiguity:** Each student's daily hours form exactly one contiguous block of consecutive on-the-hour segments.
7. **Hard constraints:** All of the above are hard. If infeasible on any day, the model reports infeasibility.

**Data (Table 5-9):**

| Student | Wage (CNY/h) | Mon | Tue | Wed | Thu | Fri |
|---------|-------------|-----|-----|-----|-----|-----|
| 1       | 10.0        | 6   | 0   | 6   | 0   | 7   |
| 2       | 10.0        | 0   | 8   | 9   | 6   | 0   |
| 3       | 9.9         | 4   | 8   | 3   | 0   | 5   |
| 4       | 9.8         | 5   | 5   | 6   | 0   | 4   |
| 5       | 10.8        | 3   | 0   | 5   | 8   | 0   |
| 6       | 11.3        | 0   | 6   | 0   | 6   | 5   |

**Outstanding item:** Student classification (undergrad → 8h min, grad → 7h min) to be plugged in once confirmed. The model structure will parameterize this so it can be set with a single assignment.