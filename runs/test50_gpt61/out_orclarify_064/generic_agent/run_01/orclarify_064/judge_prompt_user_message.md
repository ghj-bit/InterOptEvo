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

READY_TO_MODEL

Confirmed understanding: each candidate is either hired or not hired, with fixed salary. The selection must satisfy:

- Salary no more than $40,000
- No more than 4 hires
- Total skill level at least 8
- Total project management experience at least 8 years
- Minimize total salary

## Recommended hires

Hire **G, H, and I**:

| Candidate | Salary | Skill | Experience |
|---|---:|---:|---:|
| G | $15,000 | 3 | 2 |
| H | $18,000 | 4 | 2 |
| I | $5,000 | 1 | 5 |
| **Total** | **$38,000** | **8** | **9** |

This selection:

- Uses 3 of the 4 available hire slots
- Meets the minimum skill requirement exactly
- Exceeds the experience requirement by 1 year
- Stays $2,000 under budget

**Minimum total salary: $38,000.** No lower-cost combination satisfies both the skill and experience requirements.