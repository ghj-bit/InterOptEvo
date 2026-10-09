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

QUESTION: Should the minimum total skill level of 8 and minimum total project management experience of 8 years be treated as hard constraints that must be satisfied, or is it acceptable to hire no one (or fewer) if those thresholds cannot be met within the budget and hire limit?

## Turn 1 - User Simulator

They are hard constraints. The total skill level of hired candidates must be at least 8, and the total project management experience of hired candidates must be at least 8 years.

## Turn 2 - Generic Agent

QUESTION: Is there any requirement on the minimum number of candidates to hire, or is hiring zero candidates allowed as long as the skill and experience thresholds are met?

## Turn 2 - User Simulator

There is no minimum number of candidates to hire. Hiring zero candidates is allowed as long as the skill and experience thresholds are met.

## Turn 3 - Generic Agent

QUESTION: Since the skill and experience thresholds are hard constraints, hiring zero candidates would violate them — so effectively at least one candidate must be hired. Is that the correct reading?

## Turn 3 - User Simulator

Yes, that is the correct reading. Since the skill and experience thresholds are hard constraints, hiring zero candidates would violate them, so at least one candidate must be hired.

## Turn 4 - Generic Agent

QUESTION: Is the objective purely to minimize total salary, with no secondary preference (for example, preferring more hires or higher skill when salaries tie)?

## Turn 4 - User Simulator

Yes, the objective is purely to minimize the total salary paid to hired candidates. There is no secondary preference.

## Turn 5 - Generic Agent

QUESTION: Are the salary figures monthly or annual, and does the budget of $40,000 apply to the same time period as those salaries?

## Turn 5 - User Simulator

The salary figures are annual, and the budget of $40,000 applies to the same annual time period.

## Turn 6 - Generic Agent

QUESTION: Are the skill level and project management experience values additive across hired candidates (i.e., totals are simple sums), or is there any other aggregation rule?

## Turn 6 - User Simulator

Yes, the skill level and project management experience values are additive across hired candidates. The totals are simple sums.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision:** Binary hire/no-hire for each of the five candidates F, G, H, I, J.
- **Objective:** Minimize total annual salary of hired candidates.
- **Constraints (all hard):**
  1. Total salary of hired candidates ≤ $40,000 (annual).
  2. Number of hired candidates ≤ 4.
  3. Total skill level of hired candidates ≥ 8 (additive sum).
  4. Total project management experience of hired candidates ≥ 8 years (additive sum).
- **No minimum number of hires**, but since constraints 3 and 4 are hard, at least one candidate must be hired (zero hires is infeasible).
- **No secondary preference** on ties.
- **Aggregation:** Skill and experience totals are simple sums.

Candidate data (salary, skill, PM experience):
- F: 12000, 2, 1
- G: 15000, 3, 2
- H: 18000, 4, 2
- I: 5000, 1, 5
- J: 10000, 2, 4

Model formulation:

Let \(x_c \in \{0,1\}\) for \(c \in \{F,G,H,I,J\}\).

\[
\min \sum_c \text{salary}_c \, x_c
\]

subject to:
\[
\sum_c \text{salary}_c \, x_c \le 40000
\]
\[
\sum_c x_c \le 4
\]
\[
\sum_c \text{skill}_c \, x_c \ge 8
\]
\[
\sum_c \text{pmexp}_c \, x_c \ge 8
\]
\[
x_c \in \{0,1\}
\]

I will now solve this model.