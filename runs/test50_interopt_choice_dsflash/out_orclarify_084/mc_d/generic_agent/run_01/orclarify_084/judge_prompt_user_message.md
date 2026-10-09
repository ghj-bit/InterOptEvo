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

```json
{
  "action": "ASK",
  "question": "Are the budget, experience, and headcount limits strict requirements or can they be relaxed with penalties?",
  "options": [
    {
      "id": "A",
      "text": "All stated limits are strict and cannot be violated."
    },
    {
      "id": "B",
      "text": "The budget can be exceeded with a penalty, but other limits are strict."
    },
    {
      "id": "C",
      "text": "The experience requirement can be missed with a penalty, but other limits are strict."
    }
  ],
  "allow_other": true
}
```

Question:
Are the budget, experience, and headcount limits strict requirements or can they be relaxed with penalties?

Options:
A. All stated limits are strict and cannot be violated.
B. The budget can be exceeded with a penalty, but other limits are strict.
C. The experience requirement can be missed with a penalty, but other limits are strict.
D. None of the above — I'd like to explain in my own words.

## Turn 1 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 2 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Is there a specific objective for choosing among feasible candidate sets, or is any feasible set acceptable?",
  "options": [
    {
      "id": "A",
      "text": "Any feasible set is acceptable; there is no additional objective."
    },
    {
      "id": "B",
      "text": "Minimize total salary paid to selected candidates."
    },
    {
      "id": "C",
      "text": "Maximize total work experience of selected candidates."
    }
  ],
  "allow_other": true
}
```

Question:
Is there a specific objective for choosing among feasible candidate sets, or is any feasible set acceptable?

Options:
A. Any feasible set is acceptable; there is no additional objective.
B. Minimize total salary paid to selected candidates.
C. Maximize total work experience of selected candidates.
D. None of the above — I'd like to explain in my own words.

## Turn 2 - User Simulator

```json
{
  "choice": "B"
}
```

Business user selected option B.

## Turn 3 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Does the selected team need to satisfy any minimum education or degree requirement?",
  "options": [
    {
      "id": "A",
      "text": "No degree requirement applies; candidates are eligible regardless of degree."
    },
    {
      "id": "B",
      "text": "At least one selected candidate must hold a Bachelor's degree or higher."
    },
    {
      "id": "C",
      "text": "At least one selected candidate must hold a Master's degree or higher."
    }
  ],
  "allow_other": true
}
```

Question:
Does the selected team need to satisfy any minimum education or degree requirement?

Options:
A. No degree requirement applies; candidates are eligible regardless of degree.
B. At least one selected candidate must hold a Bachelor's degree or higher.
C. At least one selected candidate must hold a Master's degree or higher.
D. None of the above — I'd like to explain in my own words.

## Turn 3 - User Simulator

```json
{
  "choice": "C"
}
```

Business user selected option C.

## Turn 4 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Are there any other eligibility rules for candidates beyond the stated salary, degree, experience, and A/E conflict constraints?",
  "options": [
    {
      "id": "A",
      "text": "No other eligibility rules apply."
    },
    {
      "id": "B",
      "text": "Candidates must be currently authorized to work in the country."
    },
    {
      "id": "C",
      "text": "Candidates must have at least a Bachelor's degree."
    }
  ],
  "allow_other": true
}
```

Question:
Are there any other eligibility rules for candidates beyond the stated salary, degree, experience, and A/E conflict constraints?

Options:
A. No other eligibility rules apply.
B. Candidates must be currently authorized to work in the country.
C. Candidates must have at least a Bachelor's degree.
D. None of the above — I'd like to explain in my own words.

## Turn 4 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 5 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Are there any other candidate compatibility, exclusion, or must-include relationships beyond the stated A/E restriction?",
  "options": [
    {
      "id": "A",
      "text": "No other compatibility, exclusion, or must-include relationships exist."
    },
    {
      "id": "B",
      "text": "Some candidates must be selected together as a pair."
    },
    {
      "id": "C",
      "text": "Some candidates cannot be selected together beyond the A/E restriction."
    }
  ],
  "allow_other": true
}
```

Question:
Are there any other candidate compatibility, exclusion, or must-include relationships beyond the stated A/E restriction?

Options:
A. No other compatibility, exclusion, or must-include relationships exist.
B. Some candidates must be selected together as a pair.
C. Some candidates cannot be selected together beyond the A/E restriction.
D. None of the above — I'd like to explain in my own words.

## Turn 5 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 6 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Does the team need to satisfy any eligibility rule beyond salary, experience, and the A/E restriction, such as a required degree level or excluding no-degree candidates?",
  "options": [
    {
      "id": "A",
      "text": "No additional eligibility rule applies beyond the stated constraints."
    },
    {
      "id": "B",
      "text": "Candidates with no degree are not eligible for selection."
    },
    {
      "id": "C",
      "text": "At least one selected candidate must hold a Bachelor's degree or higher."
    }
  ],
  "allow_other": true
}
```

Question:
Does the team need to satisfy any eligibility rule beyond salary, experience, and the A/E restriction, such as a required degree level or excluding no-degree candidates?

Options:
A. No additional eligibility rule applies beyond the stated constraints.
B. Candidates with no degree are not eligible for selection.
C. At least one selected candidate must hold a Bachelor's degree or higher.
D. None of the above — I'd like to explain in my own words.

## Turn 6 - User Simulator

```json
{
  "choice": "D",
  "comment": "There is an additional eligibility rule: at least one selected candidate must hold a Master's or Doctoral degree."
}
```

Business user response: none of the offered options match. There is an additional eligibility rule: at least one selected candidate must hold a Master's or Doctoral degree.

## Turn 7 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Is the requirement that at least one selected candidate hold a Master's or Doctoral degree the only additional eligibility rule beyond salary, experience, and the A/E restriction?",
  "options": [
    {
      "id": "A",
      "text": "Yes, that is the only additional eligibility rule."
    },
    {
      "id": "B",
      "text": "No, there is also a rule excluding candidates with no degree."
    },
    {
      "id": "C",
      "text": "No, there is also a rule requiring at least one Bachelor's degree holder."
    }
  ],
  "allow_other": true
}
```

Question:
Is the requirement that at least one selected candidate hold a Master's or Doctoral degree the only additional eligibility rule beyond salary, experience, and the A/E restriction?

Options:
A. Yes, that is the only additional eligibility rule.
B. No, there is also a rule excluding candidates with no degree.
C. No, there is also a rule requiring at least one Bachelor's degree holder.
D. None of the above — I'd like to explain in my own words.

## Turn 7 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 8 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Does the restriction between candidates A and E only prevent selecting both together, or does it also create other selection relationships?",
  "options": [
    {
      "id": "A",
      "text": "It only prevents selecting both A and E together; no other relationship exists."
    },
    {
      "id": "B",
      "text": "It also means that if A is selected, E must be selected, or vice versa."
    },
    {
      "id": "C",
      "text": "It also means that selecting A or E forces some other candidate to be selected or excluded."
    }
  ],
  "allow_other": true
}
```

Question:
Does the restriction between candidates A and E only prevent selecting both together, or does it also create other selection relationships?

Options:
A. It only prevents selecting both A and E together; no other relationship exists.
B. It also means that if A is selected, E must be selected, or vice versa.
C. It also means that selecting A or E forces some other candidate to be selected or excluded.
D. None of the above — I'd like to explain in my own words.

## Turn 8 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 9 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "Confirmed: select 2 to 3 candidates from A, B, C, D, E to minimize total salary, subject to a $35,000 salary budget, at least 12 total years of experience, at most one of A and E, and at least one selected candidate holding a Master's or Doctoral degree. All limits are strict, and no other eligibility or compatibility rules apply. Remaining minor assumption: the problem is a one-time selection with no additional timing or grouping structure."
}
```

Confirmed: select 2 to 3 candidates from A, B, C, D, E to minimize total salary, subject to a $35,000 salary budget, at least 12 total years of experience, at most one of A and E, and at least one selected candidate holding a Master's or Doctoral degree. All limits are strict, and no other eligibility or compatibility rules apply. Remaining minor assumption: the problem is a one-time selection with no additional timing or grouping structure.