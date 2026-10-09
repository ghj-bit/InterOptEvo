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

QUESTION: Is the maximum number of new hires (4) a hard upper bound that must be respected, or is it a soft target that could be exceeded if needed to meet the skill and experience minimums?

## Turn 1 - User Simulator

It is a hard upper bound. We cannot hire more than four candidates.

## Turn 2 - Generic Agent

QUESTION: Is the $40,000 budget a hard upper bound on total salary, or is it a soft target that could be exceeded if needed to meet the skill and experience minimums?

## Turn 2 - User Simulator

It is a hard upper bound. The total salary paid to hired candidates cannot exceed $40,000.

## Turn 3 - Generic Agent

QUESTION: Are the minimum total skill level (8) and minimum total project management experience (8 years) both hard lower bounds that must be met, or are they soft targets that could be relaxed if needed?

## Turn 3 - User Simulator

They are both hard lower bounds. The total skill level of hired candidates must be at least 8, and the total project management experience must be at least 8 years.

## Turn 4 - Generic Agent

QUESTION: Is the objective to minimize total salary paid to hired candidates, or is there another objective (e.g., maximize total skill level, maximize total experience, or some combination)?

## Turn 4 - User Simulator

The objective is to minimize the total salary paid to hired candidates.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as candidate availability, team composition requirements, or any other business rules that might affect the hiring decision?

## Turn 5 - User Simulator

Yes. At most one of candidates G and J can be hired.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as candidate availability, team composition requirements, or any other business rules that might affect the hiring decision?

## Turn 6 - User Simulator

No, there are no other constraints or considerations.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:** Binary variable for each of the five candidates (F, G, H, I, J), indicating whether they are hired (1) or not (0).

**Objective:** Minimize total salary paid to hired candidates.

**Constraints:**
1. **Budget (hard upper bound):** Total salary of hired candidates ≤ $40,000.
2. **Maximum hires (hard upper bound):** Number of hired candidates ≤ 4.
3. **Minimum skill level (hard lower bound):** Total skill level of hired candidates ≥ 8.
4. **Minimum project management experience (hard lower bound):** Total PM experience of hired candidates ≥ 8 years.
5. **Mutual exclusion:** At most one of candidates G and J can be hired.

**Candidate data:**
| Candidate | Salary | Skill Level | PM Experience (years) |
|-----------|--------|-------------|----------------------|
| F         | 12,000 | 2           | 1                    |
| G         | 15,000 | 3           | 2                    |
| H         | 18,000 | 4           | 2                    |
| I         | 5,000  | 1           | 5                    |
| J         | 10,000 | 2           | 4                    |

This is a binary integer programming problem with five binary decision variables and five linear constraints.