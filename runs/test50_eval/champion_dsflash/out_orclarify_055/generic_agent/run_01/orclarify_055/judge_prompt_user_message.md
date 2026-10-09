# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U7, U8, U9, U2
I need help planning a course selection for a master's student in Operations Research, where at least two courses must be selected that satisfy the Computer Science requirement, and a single course that belongs to multiple categories can simultaneously fulfill the requirement of all those categories. Additionally, taking Computer Simulation requires taking Computer Programming, and taking Data Structures requires taking Computer Programming.

Courses and their category memberships:
- Calculus: Mathematics
- Operations Research: Operations Research, Mathematics
- Data Structures: Computer Science, Mathematics
- Management Statistics: Mathematics, Operations Research
- Computer Simulation: Computer Science, Operations Research
- Computer Programming: Computer Science
- Forecasting: Operations Research, Mathematics

## Problem units
- U1 (context): I need help planning a course selection for a master's student in Operations Research.
- U2 (data): Courses and their category memberships:
- Calculus: Mathematics
- Operations Research: Operations Research, Mathematics
- Data Structures: Computer Science, Mathematics
- Management Statistics: Mathematics, Operations Research
- Computer Simulation: Computer Science, Operations Research
- Computer Programming: Computer Science
- Forecasting: Operations Research, Mathematics
- U3 (objective): Minimize the total number of courses selected.
- U4 (constraint): At least two courses must be selected that satisfy the Mathematics requirement.
- U5 (constraint): At least two courses must be selected that satisfy the Operations Research requirement.
- U6 (constraint): At least two courses must be selected that satisfy the Computer Science requirement.
- U7 (constraint): A single course that belongs to multiple categories can simultaneously fulfill the requirement of all those categories.
- U8 (constraint): Taking Computer Simulation requires taking Computer Programming.
- U9 (constraint): Taking Data Structures requires taking Computer Programming.
- U10 (constraint): Taking Management Statistics requires taking Calculus.
- U11 (constraint): Taking Forecasting requires taking Management Statistics.

## Hidden slot scoring rules
## H1: unknown_objective_minimize_courses
- Severity: P0
- Severity reason: Without an explicit objective, the optimization problem is ill‑defined; the agent cannot know what to optimize and may assume a different or even opposite goal, making any model meaningless.
- Problem unit ID: U3
- Semantic hit rule: The agent's question must ask about the optimization goal being to minimize the total number of courses selected.
- Reference acceptable questions:
  - What are we trying to achieve? Minimize the number of courses?
  - Is the goal to find the smallest possible set of courses that meets the requirements?
- Failure modes:
  - Assuming the goal is simply to find any feasible course selection
  - Assuming we want to maximize something else like course variety or credit hours

## H2: unknown_mathematics_course_count
- Severity: P1
- Severity reason: The exact number of required mathematics courses (at least two) is a critical parameter; without it the feasible region is incorrectly defined and the optimal course set will almost certainly be wrong.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must explicitly ask about the required number or minimum number of courses that satisfy the Mathematics requirement.
- Reference acceptable questions:
  - How many mathematics courses does the student need to take?
  - Is there a minimum number of math courses that must be included?
- Failure modes:
  - Assuming only one mathematics course is needed
  - Assuming the requirement is exactly two, not at least two, or any other arbitrary number

## H3: unknown_operations_research_course_count
- Severity: P1
- Severity reason: The exact number of required operations research courses (at least two) is essential to define the feasible set; omitting it leads to an incorrect model and suboptimal selection.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must specifically ask about the required number of courses for the Operations Research category.
- Reference acceptable questions:
  - How many operations research courses are required?
  - Do we need at least two courses that satisfy the OR requirement?
- Failure modes:
  - Assuming one OR course is sufficient
  - Assuming the OR requirement is optional or can be satisfied with fewer courses

## H4: unknown_prerequisite_management_statistics
- Severity: P1
- Severity reason: The prerequisite constraint linking Management Statistics to Calculus is a structural rule; ignoring it allows infeasible schedules and makes the resulting model invalid for the real academic programme.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must inquire about whether Management Statistics has a prerequisite and/or explicitly mention Calculus as a requirement.
- Reference acceptable questions:
  - Does Management Statistics have any prerequisite courses?
  - Can the student take Management Statistics without having taken Calculus?
- Failure modes:
  - Assuming Management Statistics has no prerequisites
  - Assuming Calculus is optional or not required before Management Statistics

## H5: unknown_prerequisite_forecasting
- Severity: P1
- Severity reason: The Forecasting prerequisite (Management Statistics) is necessary to correctly define feasibility; omitting it can lead to a course plan that violates the real enrolment rules.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask about prerequisites for Forecasting and/or mention that Management Statistics is needed before Forecasting.
- Reference acceptable questions:
  - Does Forecasting depend on any other course?
  - Is Management Statistics a prerequisite for Forecasting?
- Failure modes:
  - Assuming Forecasting can be taken independently
  - Assuming only Calculus is a prerequisite for Forecasting


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective of the course selection — for example, minimize the number of courses taken, or is there a fixed total number of courses to select?

## Turn 1 - User Simulator

The objective is to minimize the total number of courses the student has to take while still meeting all the category and prerequisite requirements.

## Turn 2 - Generic Agent

QUESTION: Besides the Computer Science requirement of at least two courses, are there any other category requirements (e.g., a minimum number of Mathematics or Operations Research courses) that must be met?

## Turn 2 - User Simulator

Yes. The student must also take at least two courses that count toward the Mathematics requirement and at least two courses that meet the Operations Research requirement.

## Turn 3 - Generic Agent

QUESTION: For the prerequisite rules — "taking Computer Simulation requires taking Computer Programming" and "taking Data Structures requires taking Computer Programming" — do these mean that if the student selects the dependent course, they must also select Computer Programming (i.e., Computer Programming must be in the chosen set)?

## Turn 3 - User Simulator

Yes, if the student selects Computer Simulation or Data Structures, they must also select Computer Programming.

## Turn 4 - Generic Agent

QUESTION: Can a single course be counted toward more than one of the three category requirements at the same time (e.g., Data Structures counting toward both Computer Science and Mathematics), or must the required courses for each category be distinct?

## Turn 4 - User Simulator

Yes, a single course that belongs to multiple categories can simultaneously fulfill the requirement of all those categories.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on the total number of courses the student may take, or any other constraint (such as a maximum per category) that I should account for?

## Turn 5 - User Simulator

No, there is no limit on the total number of courses the student may take, nor are there any maximum per category constraints.

## Turn 6 - Generic Agent

QUESTION: Must the student take at least one course overall, or is selecting zero courses acceptable if it somehow met the requirements (which it cannot here)?

## Turn 6 - User Simulator

No, selecting zero courses is not acceptable. The student must take at least two courses for each of the Mathematics, Operations Research, and Computer Science requirements.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Minimize the total number of courses selected.
- **Category requirements (each at least 2 courses):**
  - Computer Science
  - Mathematics
  - Operations Research
- **Overlap allowed:** A course belonging to multiple categories counts toward all of them simultaneously.
- **Prerequisites (one-way):** Selecting Computer Simulation requires Computer Programming; selecting Data Structures requires Computer Programming. So Computer Programming must be in the chosen set if either dependent course is chosen.
- **No other limits:** No cap on total courses, no per-category maximums, no minimum beyond the category requirements.

Course category memberships:
- Calculus: Mathematics
- Operations Research: Operations Research, Mathematics
- Data Structures: Computer Science, Mathematics
- Management Statistics: Mathematics, Operations Research
- Computer Simulation: Computer Science, Operations Research
- Computer Programming: Computer Science
- Forecasting: Operations Research, Mathematics

Model: binary variable per course; minimize the sum; constraints enforce ≥2 in each of the three categories (counting overlaps); prerequisite implications link Computer Simulation → Computer Programming and Data Structures → Computer Programming.