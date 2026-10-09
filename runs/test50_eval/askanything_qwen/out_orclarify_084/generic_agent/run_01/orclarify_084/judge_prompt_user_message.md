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

QUESTION: What is the primary objective of this selection process, such as maximizing total work experience, minimizing total salary cost, or simply finding any valid combination that meets the constraints?

## Turn 1 - User Simulator

The primary objective is to minimize the total salary cost for the selected candidates.

## Turn 2 - Generic Agent

QUESTION: Are there any other constraints or preferences, such as requiring at least one candidate with a specific degree level, that should be included in the selection?

## Turn 2 - User Simulator

Yes, at least one of the selected candidates must hold a Master's or a Doctoral degree.

## Turn 3 - Generic Agent

READY_TO_MODEL

I have confirmed the following understanding of your recruitment problem:

**Objective:**
Minimize the total salary cost of the selected candidates.

**Candidates and Attributes:**
- **Candidate A:** Salary $8,100, Experience 3 years, Degree: Bachelor's
- **Candidate B:** Salary $20,000, Experience 10 years, Degree: Master's
- **Candidate C:** Salary $21,000, Experience 4 years, Degree: Doctoral
- **Candidate D:** Salary $3,000, Experience 3 years, Degree: No degree
- **Candidate E:** Salary $8,000, Experience 7 years, Degree: No degree

**Constraints:**
1. **Selection Count:** Select at least 2 and at most 3 candidates.
2. **Budget:** Total salary must not exceed $35,000.
3. **Experience:** Total work experience must be at least 12 years.
4. **Mutual Exclusion:** At most one of Candidate A and Candidate E can be selected.
5. **Degree Requirement:** At least one selected candidate must hold a Master's or Doctoral degree.