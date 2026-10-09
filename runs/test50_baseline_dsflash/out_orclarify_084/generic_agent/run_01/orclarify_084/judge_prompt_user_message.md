# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U8, U11, U12, U14, U2, U3, U4, U5, U7, U10, U13
I need help recruiting new employees for my team, with the number of selected candidates not exceeding 3 and at least 2 new employees hired. Total payment to selected candidates cannot exceed the budget of $35,000, and their total work experience must be at least 12 years. Additionally, at most one of candidate A and E can be selected.

Salary requirements: Candidate A: $8100, Candidate B: $20000, Candidate C: $21000, Candidate D: $3000, Candidate E: $8000.

Candidate degrees: A: Bachelor's, B: Master's, C: Doctoral, D: No degree, E: No degree.

Candidate work experience: A: 3 years, B: 10 years, C: 4 years, D: 3 years, E: 7 years.

Maximum number of new employees: 3.

Budget: $35,000.

Minimum total work experience: 12 years.

Minimum number of new employees: 2.

## Problem units
- U1 (context): I need help recruiting new employees for my team.
- U2 (data): Salary requirements: Candidate A: $8100, Candidate B: $20000, Candidate C: $21000, Candidate D: $3000, Candidate E: $8000.
- U3 (data): Candidate degrees: A: Bachelor's, B: Master's, C: Doctoral, D: No degree, E: No degree.
- U4 (data): Candidate work experience: A: 3 years, B: 10 years, C: 4 years, D: 3 years, E: 7 years.
- U5 (data): Maximum number of new employees: 3.
- U6 (constraint): The number of selected candidates cannot exceed 3.
- U7 (data): Budget: $35,000.
- U8 (constraint): Total payment to selected candidates cannot exceed the budget of $35,000.
- U9 (constraint): Select at least one candidate with a Master's or Doctoral degree.
- U10 (data): Minimum total work experience: 12 years.
- U11 (constraint): Total work experience of selected candidates must be at least 12 years.
- U12 (constraint): At most one of candidate A and E can be selected.
- U13 (data): Minimum number of new employees: 2.
- U14 (constraint): Hire at least 2 new employees.
- U15 (objective): Minimize total salary paid to selected candidates.

## Hidden slot scoring rules
## H1: advanced_degree_requirement
- Severity: P1
- Severity reason: Without this qualification constraint, the model may select only low-cost candidates without advanced degrees, leading to a solution that is business-invalid; the optimization problem remains otherwise well-defined, so it is an important clarification gap.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must mention a minimum requirement for advanced degrees (Master's or Doctoral) or inquire about educational qualification constraints.
- Reference acceptable questions:
  - Do we have any educational requirements for the hires, like needing someone with an advanced degree?
  - Is it mandatory to include at least one person with a Master's or PhD?
- Failure modes:
  - Assuming no minimum degree requirement and selecting only candidates without advanced degrees
  - Overlooking the need for at least one Master's or Doctoral hire

## H2: minimize_total_salary_objective
- Severity: P0
- Severity reason: Without a stated objective, the problem lacks a clear goal; a modeling agent cannot formulate an optimization model without inventing the objective, making the task ill-posed.
- Problem unit ID: U15
- Semantic hit rule: The agent's question must ask about the optimization goal or objective, specifically whether the goal is to minimize total salary, or inquire about what to optimize.
- Reference acceptable questions:
  - What is the objective of this hiring decision? Are we trying to minimize total salary costs?
  - Is the goal to minimize the total salaries paid, or something else?
- Failure modes:
  - Assuming a different objective such as minimizing the number of hires or maximizing total work experience
  - Treating the problem as a pure feasibility problem without asking for the objective


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Which candidate attributes matter for your hiring decision beyond the constraints you listed—for example, do you want to prioritize certain degrees, experience levels, or salary efficiency when choosing among feasible sets?

## Turn 1 - User Simulator

Yes, at least one of the selected candidates must hold a Master's or a Doctoral degree.

## Turn 2 - Generic Agent

QUESTION: Do you want me to recommend the single best set of candidates based on some objective (such as lowest total salary or highest total experience), or simply identify all feasible sets that satisfy your constraints?

## Turn 2 - User Simulator

We want to keep the total salaries as low as possible. So the goal is to minimize the sum of salaries for the people we hire.

## Turn 3 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of your request:

**Goal:** Select new employees to minimize total salary.

**Decision:** Which candidates to hire.

**Constraints:**
- Select at most 3 candidates (maximum 3).
- Hire at least 2 candidates (minimum 2).
- Total salary must not exceed $35,000.
- Total work experience must be at least 12 years.
- At most one of Candidate A and Candidate E can be selected.
- At least one selected candidate must hold a Master's or Doctoral degree.

**Candidate data:**

| Candidate | Salary | Degree | Experience |
|-----------|--------|--------|------------|
| A | $8,100 | Bachelor's | 3 yrs |
| B | $20,000 | Master's | 10 yrs |
| C | $21,000 | Doctoral | 4 yrs |
| D | $3,000 | No degree | 3 yrs |
| E | $8,000 | No degree | 7 yrs |

**Objective:** Minimize total salary of the selected candidates.

Let me now work through the feasible combinations.

**Step 1 — Identify the degree constraint.** At least one selected candidate must be B (Master's) or C (Doctoral). So every valid set must include B or C (or both).

**Step 2 — Enumerate feasible sets of size 2 or 3.**

Since B costs $20,000 and C costs $21,000, and the budget is $35,000, any set containing C cannot contain B (20,000 + 21,000 = 41,000 > 35,000). Also, a set containing C can only add candidates whose salaries keep the total ≤ $35,000.

Let me check the cheapest options first, since we minimize salary.

**Sets of size 2:**
- Must include B or C.
- {B, D}: salary 20,000 + 3,000 = 23,000; experience 10 + 3 = 13 ≥ 12 ✓; A/E constraint not triggered ✓. **Feasible.**
- {B, E}: salary 20,000 + 8,000 = 28,000; experience 10 + 7 = 17 ✓; A/E constraint: only E, fine ✓. **Feasible.**
- {B, A}: salary 20,000 + 8,100 = 28,100; experience 10 + 3 = 13 ✓; A/E constraint: only A, fine ✓. **Feasible.**
- {C, D}: salary 21,000 + 3,000 = 24,000; experience 4 + 3 = 7 < 12 ✗. Not feasible.
- {C, E}: salary 21,000 + 8,000 = 29,000; experience 4 + 7 = 11 < 12 ✗. Not feasible.
- {C, A}: salary 21,000 + 8,100 = 29,100; experience 4 + 3 = 7 < 12 ✗. Not feasible.

So among size-2 sets, the cheapest feasible is **{B, D} at $23,000**.

**Sets of size 3:**
- Any size-3 set has salary at least the three cheapest candidates. The three cheapest are D ($3,000), E ($8,000), A ($8,100) = $19,100, but that set has no Master's/Doctoral → invalid.
- To include B or C, the cheapest size-3 set would be {B, D, E} = 20,000 + 3,000 + 8,000 = $31,000, or {B, D, A} = 20,000 + 3,000 + 8,100 = $31,100, or {C, D, E} = 21,000 + 3,000 + 8,000 = $32,000, etc.
- All size-3 feasible sets cost at least $31,000, which is more than $23,000.

**Step 3 — Compare.** The minimum-salary feasible set is **{B, D}** at **$23,000**.

**Final recommendation:**

Hire **Candidate B** and **Candidate D**.

- Total salary: $20,000 + $3,000 = **$23,000** (within the $35,000 budget)
- Total experience: 10 + 3 = **13 years** (meets the 12-year minimum)
- Number hired: **2** (meets the 2–3 range)
- Degree requirement: B holds a Master's ✓
- A/E constraint: neither A nor E selected ✓

This is the lowest-cost feasible selection. If you'd prefer to hire 3 people (for example, to add more capacity), the cheapest valid 3-person option would be {B, D, E} at $31,000, but that costs $8,000 more than the recommended set.