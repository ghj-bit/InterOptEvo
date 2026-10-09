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

QUESTION: What is the maximum number of new hires you are allowed to make?

## Turn 1 - User Simulator

The maximum number of new hires is 4.

## Turn 2 - Generic Agent

QUESTION: What is the total salary budget you cannot exceed?

## Turn 2 - User Simulator

The total salary budget is $40,000.

## Turn 3 - Generic Agent

QUESTION: Is the minimum required total skill level for the hired candidates 8?

## Turn 3 - User Simulator

Yes, the minimum required total skill level is 8.

## Turn 4 - Generic Agent

QUESTION: Is the minimum required total project management experience for the hired candidates 8 years?

## Turn 4 - User Simulator

Yes, the minimum required total project management experience is 8 years.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:
- Choose any subset of the five candidates (F, G, H, I, J) to hire.
- Total salary of hired candidates must not exceed $40,000.
- Number of hired candidates must not exceed 4.
- Total skill level of hired candidates must be at least 8.
- Total project management experience of hired candidates must be at least 8 years.
- Objective: minimize total salary paid to hired candidates.

Candidate data:

| Candidate | Salary | Skill | PM Experience |
|-----------|--------|-------|---------------|
| F | 12000 | 2 | 1 |
| G | 15000 | 3 | 2 |
| H | 18000 | 4 | 2 |
| I | 5000 | 1 | 5 |
| J | 10000 | 2 | 4 |

Let me solve this.

We need skill ≥ 8 and PM experience ≥ 8, minimizing salary.

Let me evaluate combinations. Total skill across all five = 2+3+4+1+2 = 12. Total PM = 1+2+2+5+4 = 14.

We need to find the cheapest subset meeting both thresholds.

Let me check the cheapest candidates first. I (5000, skill 1, PM 5) and J (10000, skill 2, PM 4) are cheap. I+J: skill 3, PM 9. Skill too low.

We need skill ≥ 8. Let's think about which candidates give good skill per dollar.

Let me enumerate promising subsets.

Cheapest salaries: I=5000, J=10000, F=12000, G=15000, H=18000.

Try to reach skill 8 with low cost.

- H (skill 4) + G (skill 3) = skill 7, need 1 more → add I (skill 1): H+G+I = skill 8, PM = 2+2+5 = 9. Salary = 18000+15000+5000 = 38000. Feasible.
- H + F + J: skill 4+2+2 = 8, PM = 2+1+4 = 7. PM too low.
- H + G + J: skill 4+3+2 = 9, PM = 2+2+4 = 8. Salary = 18000+15000+10000 = 43000. Over budget.
- H + F + I + J: skill 4+2+1+2 = 9, PM = 2+1+5+4 = 12. Salary = 18000+12000+5000+10000 = 45000. Over budget.
- G + F + J + I: skill 3+2+2+1 = 8, PM = 2+1+4+5 = 12. Salary = 15000+12000+10000+5000 = 42000. Over budget.
- G + F + J: skill 3+2+2 = 7. Too low.
- G + F + I + ... need skill 8: G+F+I = 6, need 2 more → J: G+F+I+J = 8, salary 42000 (over).
- H + J + I: skill 4+2+1 = 7. Too low.
- H + J + I + F: skill 9, PM 12, salary 45000 (over).
- H + G + I = 38000 (found above), skill 8, PM 9. Feasible.
- H + G + F: skill 9, PM 5. PM too low.
- H + G + J: 43000 over budget.
- G + J + I + F: 42000 over.
- H + F + I: skill 7. Too low.
- H + F + J: PM 7 too low.
- H + I + J + G: skill 10, PM 13, salary 48000 over.

Let me check 4-candidate options within budget:
- I+J+F+G = 42000 over.
- I+J+F+H = 45000 over.
- I+J+G+H = 48000 over.
- I+F+G+H = 50000 over.
- J+F+G+H = 55000 over.

So 4-candidate options all exceed budget except maybe none. Let's verify cheapest 4: I+J+F+G = 5000+10000+12000+15000 = 42000 > 40000. So no 4-candidate subset is feasible.

3-candidate options:
- H+G+I = 38000, skill 8, PM 9 ✓
- H+G+J = 43000 over
- H+F+I = 35000, skill 7 ✗
- H+F+J = 40000, skill 8, PM 7 ✗
- H+I+J = 33000, skill 7 ✗
- G+F+I = 32000, skill 6 ✗
- G+F+J = 37000, skill 7 ✗
- G+I+J = 30000, skill 6 ✗
- F+I+J = 27000, skill 5 ✗
- H+G+F = 45000 over

2-candidate options: max skill H+G = 7 < 8. So none.

So the only feasible 3-candidate option is H+G+I at 38000. But wait, let me double-check whether any 3-candidate subset with skill ≥8 and PM ≥8 exists cheaper.

We need skill ≥ 8 with 3 candidates. Max skills: H(4), G(3), F(2), J(2), I(1). To get 8 with 3: H+G+I=8, H+G+J=9, H+F+J=8, H+G+F=9. Also H+F+J=8 (PM 7 ✗). H+G+F=9 (PM 5 ✗). H+G+J=9 (PM 8 ✓ but 43000 over). H+G+I=8 (PM 9 ✓, 38000).

So among 3-candidate, H+G+I is the only feasible within budget.

Now check if any 4-candidate subset is feasible within budget — we showed cheapest 4 is 42000 > 40000, so no.

Therefore the minimum salary feasible solution is H + G + I = $38,000.

Wait — but is there possibly a 3-candidate solution cheaper than 38000 that I missed? Let me list all 3-candidate subsets with salary ≤ 40000 and check:
- I+J+F = 27000, skill 5 ✗
- I+J+G = 30000, skill 6 ✗
- I+J+H = 33000, skill 7 ✗
- I+F+G = 32000, skill 6 ✗
- I+F+H = 35000, skill 7 ✗
- I+G+H = 38000, skill 8, PM 9 ✓
- J+F+G = 37000, skill 7 ✗
- J+F+H = 40000, skill 8, PM 7 ✗
- J+G+H = 43000 over
- F+G+H = 45000 over

So indeed only I+G+H works among 3-candidate subsets.

Final answer: Hire candidates G, H, and I.

- Total salary: 15000 + 18000 + 5000 = $38,000 (≤ $40,000 ✓)
- Number hired: 3 (≤ 4 ✓)
- Total skill: 3 + 4 + 1 = 8 (≥ 8 ✓)
- Total PM experience: 2 + 2 + 5 = 9 (≥ 8 ✓)

This is the minimum possible salary, since no 4-candidate subset fits the budget and no cheaper 3-candidate subset meets both thresholds.