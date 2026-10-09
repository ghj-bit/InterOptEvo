# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U8, U9, U10, U12, U2, U3, U4, U5, U6
I need help deciding whether to hire some of the five candidates for our R&D team, where the total salary paid to hired candidates cannot exceed the budget, the number of hired candidates cannot exceed the maximum number of new hires, the total skill level of hired candidates must be at least 8, and the total project management experience of hired candidates must be at least 8 years, with the objective to minimize the total salary paid to hired candidates.

Candidate data:
| Candidate | Salary | Skill Level | Project Management Experience (years) |
|-----------|--------|-------------|----------------------------------------|
| F         | 12000  | 2           | 1                                      |
| G         | 15000  | 3           | 2                                      |
| H         | 18000  | 4           | 2                                      |
| I         | 5000   | 1           | 5                                      |
| J         | 10000  | 2           | 4                                      |

Budget: $40,000

Maximum number of new hires: 4

Minimum required total skill level: 8

Minimum required total project management experience (years): 8

## Problem units
- U1 (context): I need help deciding whether to hire some of the five candidates for our R&D team.
- U2 (data): Candidate data:
| Candidate | Salary | Skill Level | Project Management Experience (years) |
|-----------|--------|-------------|----------------------------------------|
| F         | 12000  | 2           | 1                                      |
| G         | 15000  | 3           | 2                                      |
| H         | 18000  | 4           | 2                                      |
| I         | 5000   | 1           | 5                                      |
| J         | 10000  | 2           | 4                                      |
- U3 (data): Budget: $40,000
- U4 (data): Maximum number of new hires: 4
- U5 (data): Minimum required total skill level: 8
- U6 (data): Minimum required total project management experience (years): 8
- U7 (constraint): Total salary paid to hired candidates cannot exceed the budget.
- U8 (constraint): The number of hired candidates cannot exceed the maximum number of new hires.
- U9 (constraint): The total skill level of hired candidates must be at least 8.
- U10 (constraint): The total project management experience of hired candidates must be at least 8 years.
- U11 (constraint): At most one of candidates G and J can be hired.
- U12 (objective): Minimize the total salary paid to hired candidates.

## Hidden slot scoring rules
## H1: at_most_one_of_G_and_J
- Severity: P2
- Severity reason: Without this constraint, the problem remains a coherent optimization problem with budget, skill, experience, and headcount limits. Omitting it simply expands the feasible set but does not make modeling impossible or materially incorrect; it is a specific business preference.
- Problem unit ID: U11
- Semantic hit rule: The Agent's question must explicitly mention the limitation on hiring both G and J, or ask whether only one of them can be hired.
- Reference acceptable questions:
  - Is there any restriction on hiring both G and J, or can we hire them both?
  - Should we include a condition that we can't hire both G and J together because of their similar backgrounds?
- Failure modes:
  - Silently assuming both G and J can be hired without any mutual exclusion constraint.
  - Assuming there is no restriction on hiring candidates with similar backgrounds.


# Full Transcript

## Turn 1 - Generic Agent

```json
{
  "action": "ASK",
  "question": "How should the hiring decision treat each candidate?",
  "options": [
    {
      "id": "A",
      "text": "Each candidate can be hired at most once, so the choice is simply hire or not hire."
    },
    {
      "id": "B",
      "text": "A candidate can be hired multiple times if that helps meet the team requirements."
    },
    {
      "id": "C",
      "text": "A candidate can be hired partially, such as for a fraction of their salary and contribution."
    }
  ],
  "allow_other": true
}
```

Question:
How should the hiring decision treat each candidate?

Options:
A. Each candidate can be hired at most once, so the choice is simply hire or not hire.
B. A candidate can be hired multiple times if that helps meet the team requirements.
C. A candidate can be hired partially, such as for a fraction of their salary and contribution.
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
  "action": "READY_TO_MODEL",
  "summary": "Confirmed: choose a subset of the five candidates F, G, H, I, J to hire, with each candidate hired at most once. Minimize total salary. Constraints: total salary <= $40,000; number hired <= 4; total skill >= 8; total project management experience >= 8 years. All candidate data and parameter values are given. No remaining material assumptions."
}
```

Confirmed: choose a subset of the five candidates F, G, H, I, J to hire, with each candidate hired at most once. Minimize total salary. Constraints: total salary <= $40,000; number hired <= 4; total skill >= 8; total project management experience >= 8 years. All candidate data and parameter values are given. No remaining material assumptions.