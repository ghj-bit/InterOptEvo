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

QUESTION: How many total courses must the student select for the master's program?

## Turn 1 - User Simulator

The student must select the minimum number of courses needed to satisfy all the requirements.

## Turn 2 - Generic Agent

QUESTION: Besides the Computer Science requirement of at least two courses, what other category requirements must be satisfied?

## Turn 2 - User Simulator

The student must also satisfy at least two courses for the Mathematics requirement and at least two courses for the Operations Research requirement.

## Turn 3 - Generic Agent

QUESTION: Are there any courses the student is required to take regardless of category coverage, or is the student free to choose any courses as long as the category requirements are met?

## Turn 3 - User Simulator

The student is free to choose any courses as long as the category requirements and prerequisite rules are met.

## Turn 4 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Goal: Select the minimum number of courses for a master's student in Operations Research.
- Requirements:
  - At least 2 courses satisfying the Computer Science requirement.
  - At least 2 courses satisfying the Mathematics requirement.
  - At least 2 courses satisfying the Operations Research requirement.
- A course that belongs to multiple categories counts toward all of those categories simultaneously.
- Prerequisites:
  - Computer Simulation requires Computer Programming.
  - Data Structures requires Computer Programming.
- The student may choose any courses as long as category requirements and prerequisites are met.

Course category memberships:

| Course | Categories |
|---|---|
| Calculus | Mathematics |
| Operations Research | Operations Research, Mathematics |
| Data Structures | Computer Science, Mathematics |
| Management Statistics | Mathematics, Operations Research |
| Computer Simulation | Computer Science, Operations Research |
| Computer Programming | Computer Science |
| Forecasting | Operations Research, Mathematics |

Solution:

To satisfy the Computer Science requirement with at least 2 courses, the student needs at least 2 courses from:

- Data Structures
- Computer Simulation
- Computer Programming

Because Computer Simulation and Data Structures each require Computer Programming, any selection using either of them must also include Computer Programming.

Minimum-course selection:

Choose:

1. Computer Programming — counts as Computer Science
2. Data Structures — counts as Computer Science and Mathematics
3. Management Statistics — counts as Mathematics and Operations Research
4. Forecasting — counts as Operations Research and Mathematics

Check requirements:

- Computer Science: Computer Programming + Data Structures = 2 ✅
- Mathematics: Data Structures + Management Statistics + Forecasting = 3 ✅
- Operations Research: Management Statistics + Forecasting = 2 ✅

Prerequisites:

- Data Structures requires Computer Programming: included ✅
- Computer Simulation is not selected, so its prerequisite is not triggered.

Can this be done with fewer than 4 courses?

With 3 courses, the student would need those 3 courses to cover:

- At least 2 Computer Science courses
- At least 2 Mathematics courses
- At least 2 Operations Research courses

The only courses that count as Computer Science are Computer Programming, Data Structures, and Computer Simulation.

- If Computer Programming is one of the 3, the other two must include at least one more Computer Science course. If that second Computer Science course is Data Structures or Computer Simulation, then Computer Programming is already included, so prerequisites are satisfied.
- A 3-course set would need to cover Operations Research twice as well.

Checking possible 3-course sets:

- Computer Programming + Data Structures + Management Statistics:
  - Computer Science: 2 ✅
  - Mathematics: Data Structures + Management Statistics = 2 ✅
  - Operations Research: Management Statistics only = 1 ❌

- Computer Programming + Data Structures + Forecasting:
  - Computer Science: 2 ✅
  - Mathematics: Data Structures + Forecasting = 2 ✅
  - Operations Research: Forecasting only = 1 ❌

- Computer Programming + Computer Simulation + Management Statistics:
  - Computer Science: 2 ✅
  - Mathematics: Management Statistics only = 1 ❌
  - Operations Research: Computer Simulation + Management Statistics = 2 ✅

- Computer Programming + Computer Simulation + Forecasting:
  - Computer Science: 2 ✅
  - Mathematics: Forecasting only = 1 ❌
  - Operations Research: Computer Simulation + Forecasting = 2 ✅

- Data Structures + Computer Simulation + Management Statistics:
  - Computer Science: 2 ✅
  - Mathematics: Data Structures + Management Statistics = 2 ✅
  - Operations Research: Computer Simulation + Management Statistics = 2 ✅
  - But Data Structures and Computer Simulation both require Computer Programming, which is not included ❌

- Data Structures + Computer Simulation + Forecasting:
  - Computer Science: 2 ✅
  - Mathematics: Data Structures + Forecasting = 2 ✅
  - Operations Research: Computer Simulation + Forecasting = 2 ✅
  - But Data Structures and Computer Simulation both require Computer Programming, which is not included ❌

No 3-course selection satisfies all requirements and prerequisites.

Therefore, the minimum number of courses is 4.

Recommended course selection:

1. Computer Programming
2. Data Structures
3. Management Statistics
4. Forecasting

This satisfies all category requirements and prerequisite rules with the minimum number of courses.