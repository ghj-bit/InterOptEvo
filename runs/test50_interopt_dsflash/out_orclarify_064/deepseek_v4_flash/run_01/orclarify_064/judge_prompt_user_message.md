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


# Atomic Question Map

Q1 (turn 1): Can each candidate be hired at most once?
Q2 (turn 1): Is it allowed to hire fewer than the maximum number of candidates?
Q3 (turn 2): Are the minimum total skill level of 8 and minimum total project management experience of 8 years hard requirements that must be met, or can they be relaxed if no feasible set of hires satisfies them?
Q4 (turn 3): Should the total skill level and total project management experience be calculated as simple sums of the hired candidates' individual values?
Q5 (turn 4): Are the $40,000 budget and the maximum of 4 new hires hard limits that must never be exceeded, or can either be relaxed if needed?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Can each candidate be hired at most once, and is it allowed to hire fewer than the maximum number of candidates?

## Turn 1 - User Simulator

Each candidate can be hired at most once, and yes, it is allowed to hire fewer than the maximum number of candidates.

## Turn 2 - Generic Agent

QUESTION: Are the minimum total skill level of 8 and minimum total project management experience of 8 years hard requirements that must be met, or can they be relaxed if no feasible set of hires satisfies them?

## Turn 2 - User Simulator

They are hard requirements that must be met.

## Turn 3 - Generic Agent

QUESTION: Should the total skill level and total project management experience be calculated as simple sums of the hired candidates' individual values?

## Turn 3 - User Simulator

Yes, they should be calculated as simple sums of the hired candidates' individual values.

## Turn 4 - Generic Agent

QUESTION: Are the $40,000 budget and the maximum of 4 new hires hard limits that must never be exceeded, or can either be relaxed if needed?

## Turn 4 - User Simulator

They are hard limits that must never be exceeded.

## Turn 5 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.950

Confidence rationale: The request is sufficiently specified for a unique binary optimization formulation. Each candidate is a binary hire/no-hire decision, each candidate can be hired at most once, hiring fewer than the maximum is allowed, the budget and maximum-hires limits are hard upper bounds, the skill and project-management requirements are hard lower bounds computed as simple sums, and the objective is to minimize total salary.

Summary: Choose a subset of the five candidates to hire, with binary variables indicating whether each candidate is hired. Each candidate can be hired at most once. Constraints: total salary of hired candidates must not exceed $40,000; number hired must not exceed 4; total skill level of hired candidates must be at least 8; total project management experience of hired candidates must be at least 8 years. Objective: minimize total salary paid to hired candidates.