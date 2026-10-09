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


# Atomic Question Map

Q1 (turn 1): What should the course plan optimize for — for example, minimizing the total number of courses taken, maximizing coverage of categories, or meeting requirements while respecting course preferences?
Q2 (turn 2): What are the exact minimum course requirements for each category — Mathematics, Operations Research, and Computer Science?
Q3 (turn 3): Can Computer Programming be taken in the same term as Computer Simulation or Data Structures, or must it be completed before taking those courses?
Q4 (turn 4): Can a single course that belongs to multiple categories count toward the minimum requirement of each of those categories at the same time?
Q5 (turn 5): Must Computer Programming be completed before taking Computer Simulation or Data Structures, or can it be taken in the same term?
Q6 (turn 6): If the prerequisite timing rule remains unconfirmed, should the model treat the prerequisite as a simple inclusion rule — if Computer Simulation or Data Structures is selected, then Computer Programming must also be selected — without requiring it to be completed in an earlier term?
Q7 (turn 7): Is there a maximum number of courses the student can take in total or per term?
Q8 (turn 8): Is the course plan for a single term, or must it assign selected courses across multiple terms?
Q9 (turn 9): Should the course plan be modeled as a single-term selection of courses, with no term assignment or sequencing?
Q10 (turn 10): Can a selected course be counted only once toward a given category's minimum requirement, or can the same course be counted multiple times toward that same category?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What should the course plan optimize for — for example, minimizing the total number of courses taken, maximizing coverage of categories, or meeting requirements while respecting course preferences?

## Turn 1 - User Simulator

Minimize the total number of courses the student has to take while still meeting all the category and prerequisite requirements.

## Turn 2 - Generic Agent

QUESTION: What are the exact minimum course requirements for each category — Mathematics, Operations Research, and Computer Science?

## Turn 2 - User Simulator

At least two courses must be selected for each of those three requirements: Mathematics, Operations Research, and Computer Science.

## Turn 3 - Generic Agent

QUESTION: Can Computer Programming be taken in the same term as Computer Simulation or Data Structures, or must it be completed before taking those courses?

## Turn 3 - User Simulator

The information I have only says that taking Computer Simulation requires taking Computer Programming, and taking Data Structures requires taking Computer Programming. It doesn’t specify whether Computer Programming must be completed before, or can be taken in the same term. That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Can a single course that belongs to multiple categories count toward the minimum requirement of each of those categories at the same time?

## Turn 4 - User Simulator

Yes. A single course that belongs to multiple categories can simultaneously fulfill the requirement of all those categories.

## Turn 5 - Generic Agent

QUESTION: Must Computer Programming be completed before taking Computer Simulation or Data Structures, or can it be taken in the same term?

## Turn 5 - User Simulator

That point still needs internal confirmation. The information I have only states that taking Computer Simulation requires taking Computer Programming, and taking Data Structures requires taking Computer Programming; it does not specify whether Computer Programming must be completed before, or can be taken in the same term.

## Turn 6 - Generic Agent

QUESTION: If the prerequisite timing rule remains unconfirmed, should the model treat the prerequisite as a simple inclusion rule — if Computer Simulation or Data Structures is selected, then Computer Programming must also be selected — without requiring it to be completed in an earlier term?

## Turn 6 - User Simulator

Yes, treat it as a simple inclusion rule: if Computer Simulation or Data Structures is selected, then Computer Programming must also be selected, without requiring an earlier term.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum number of courses the student can take in total or per term?

## Turn 7 - User Simulator

No maximum total or per-term course limit was provided.

## Turn 8 - Generic Agent

QUESTION: Is the course plan for a single term, or must it assign selected courses across multiple terms?

## Turn 8 - User Simulator

The request is for planning a course selection; it does not specify assigning courses across multiple terms.

## Turn 9 - Generic Agent

QUESTION: Should the course plan be modeled as a single-term selection of courses, with no term assignment or sequencing?

## Turn 9 - User Simulator

Yes. Model it as a single-term selection of courses, with no term assignment or sequencing.

## Turn 10 - Generic Agent

QUESTION: Can a selected course be counted only once toward a given category's minimum requirement, or can the same course be counted multiple times toward that same category?

## Turn 10 - User Simulator

A selected course should be counted once toward a given category’s minimum requirement; it can count toward multiple different categories if it belongs to them, but not multiple times toward the same category.

## Turn 11 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.950

Confidence rationale: The request is sufficiently specified for a unique formulation. The objective is to minimize the total number of selected courses. Each of the three categories — Mathematics, Operations Research, and Computer Science — requires at least two selected courses. A course may count toward multiple different categories it belongs to, but only once per category. Prerequisites are modeled as inclusion constraints: selecting Computer Simulation or Data Structures requires selecting Computer Programming. The plan is a single-term selection with no term assignment, sequencing, or course-load limits.

Summary: Minimize the number of selected courses subject to: at least two courses from each of Mathematics, Operations Research, and Computer Science; a selected course counts toward every category it belongs to but only once per category; if Computer Simulation is selected then Computer Programming must be selected; if Data Structures is selected then Computer Programming must be selected; single-term selection with no term assignment, sequencing, or maximum course limit.