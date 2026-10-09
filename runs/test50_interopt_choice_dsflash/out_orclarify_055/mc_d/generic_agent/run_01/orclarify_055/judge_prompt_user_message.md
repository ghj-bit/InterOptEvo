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

```json
{
  "action": "ASK",
  "question": "What should the course plan primarily aim to achieve?",
  "options": [
    {
      "id": "A",
      "text": "Minimize the total number of courses taken while meeting all requirements"
    },
    {
      "id": "B",
      "text": "Cover as many requirement categories as possible with the selected courses"
    },
    {
      "id": "C",
      "text": "Meet a fixed target course load or credit count specified by the program"
    }
  ],
  "allow_other": true
}
```

Question:
What should the course plan primarily aim to achieve?

Options:
A. Minimize the total number of courses taken while meeting all requirements
B. Cover as many requirement categories as possible with the selected courses
C. Meet a fixed target course load or credit count specified by the program
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
  "question": "Is there a minimum or maximum total number of courses the student must take?",
  "options": [
    {
      "id": "A",
      "text": "There is no fixed total course load; the plan just needs to meet the category requirements."
    },
    {
      "id": "B",
      "text": "There is a minimum total number of courses the student must take."
    },
    {
      "id": "C",
      "text": "There is a maximum total number of courses the student may take."
    }
  ],
  "allow_other": true
}
```

Question:
Is there a minimum or maximum total number of courses the student must take?

Options:
A. There is no fixed total course load; the plan just needs to meet the category requirements.
B. There is a minimum total number of courses the student must take.
C. There is a maximum total number of courses the student may take.
D. None of the above — I'd like to explain in my own words.

## Turn 2 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 3 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Which category requirements must the course plan satisfy?",
  "options": [
    {
      "id": "A",
      "text": "Only the Computer Science requirement must be satisfied."
    },
    {
      "id": "B",
      "text": "All three categories—Computer Science, Mathematics, and Operations Research—must be satisfied."
    },
    {
      "id": "C",
      "text": "Computer Science plus at least one other category must be satisfied."
    }
  ],
  "allow_other": true
}
```

Question:
Which category requirements must the course plan satisfy?

Options:
A. Only the Computer Science requirement must be satisfied.
B. All three categories—Computer Science, Mathematics, and Operations Research—must be satisfied.
C. Computer Science plus at least one other category must be satisfied.
D. None of the above — I'd like to explain in my own words.

## Turn 3 - User Simulator

```json
{
  "choice": "B"
}
```

Business user selected option B.

## Turn 4 - Generic Agent

```json
{
  "action": "ASK",
  "question": "How many courses must satisfy the Mathematics and Operations Research requirements?",
  "options": [
    {
      "id": "A",
      "text": "At least one course must satisfy Mathematics and at least one must satisfy Operations Research."
    },
    {
      "id": "B",
      "text": "At least two courses must satisfy Mathematics and at least two must satisfy Operations Research."
    },
    {
      "id": "C",
      "text": "There is no minimum count for Mathematics or Operations Research; only Computer Science has a required count."
    }
  ],
  "allow_other": true
}
```

Question:
How many courses must satisfy the Mathematics and Operations Research requirements?

Options:
A. At least one course must satisfy Mathematics and at least one must satisfy Operations Research.
B. At least two courses must satisfy Mathematics and at least two must satisfy Operations Research.
C. There is no minimum count for Mathematics or Operations Research; only Computer Science has a required count.
D. None of the above — I'd like to explain in my own words.

## Turn 4 - User Simulator

```json
{
  "choice": "B"
}
```

Business user selected option B.

## Turn 5 - Generic Agent

```json
{
  "action": "ASK",
  "question": "When a course belongs to multiple categories, how should it count toward the minimum course requirements?",
  "options": [
    {
      "id": "A",
      "text": "It counts toward each of its categories simultaneously."
    },
    {
      "id": "B",
      "text": "It counts toward only one category, chosen by the planner."
    },
    {
      "id": "C",
      "text": "It counts toward each category but only once overall in the total course count."
    }
  ],
  "allow_other": true
}
```

Question:
When a course belongs to multiple categories, how should it count toward the minimum course requirements?

Options:
A. It counts toward each of its categories simultaneously.
B. It counts toward only one category, chosen by the planner.
C. It counts toward each category but only once overall in the total course count.
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
  "question": "When a course is taken only because it is a prerequisite (such as Computer Programming), how should it be treated in the plan?",
  "options": [
    {
      "id": "A",
      "text": "It must be included in the selected course set and counts toward the total number of courses."
    },
    {
      "id": "B",
      "text": "It must be included in the selected course set but does not count toward the total number of courses."
    },
    {
      "id": "C",
      "text": "It is assumed already completed and does not need to be included in the plan."
    }
  ],
  "allow_other": true
}
```

Question:
When a course is taken only because it is a prerequisite (such as Computer Programming), how should it be treated in the plan?

Options:
A. It must be included in the selected course set and counts toward the total number of courses.
B. It must be included in the selected course set but does not count toward the total number of courses.
C. It is assumed already completed and does not need to be included in the plan.
D. None of the above — I'd like to explain in my own words.

## Turn 6 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 7 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Must the student select courses only from the listed set, or can other courses be considered?",
  "options": [
    {
      "id": "A",
      "text": "Only the listed courses can be selected."
    },
    {
      "id": "B",
      "text": "Other courses from the program can also be selected if they fit a category."
    },
    {
      "id": "C",
      "text": "Other courses can be selected but they do not count toward category requirements."
    }
  ],
  "allow_other": true
}
```

Question:
Must the student select courses only from the listed set, or can other courses be considered?

Options:
A. Only the listed courses can be selected.
B. Other courses from the program can also be selected if they fit a category.
C. Other courses can be selected but they do not count toward category requirements.
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
  "action": "READY_TO_MODEL",
  "summary": "The student must select courses from the given list to satisfy all three category requirements: at least 2 Computer Science courses, at least 2 Mathematics courses, and at least 2 Operations Research courses. A course belonging to multiple categories counts toward each of those categories simultaneously. The objective is to minimize the total number of selected courses. Prerequisite rules apply: selecting Computer Simulation requires Computer Programming, and selecting Data Structures requires Computer Programming. Prerequisite courses are included in the selected set and count toward the total course count. Only the listed courses may be selected. Remaining minor assumption: no explicit maximum or minimum total course load beyond meeting category requirements."
}
```

The student must select courses from the given list to satisfy all three category requirements: at least 2 Computer Science courses, at least 2 Mathematics courses, and at least 2 Operations Research courses. A course belonging to multiple categories counts toward each of those categories simultaneously. The objective is to minimize the total number of selected courses. Prerequisite rules apply: selecting Computer Simulation requires Computer Programming, and selecting Data Structures requires Computer Programming. Prerequisite courses are included in the selected set and count toward the total course count. Only the listed courses may be selected. Remaining minor assumption: no explicit maximum or minimum total course load beyond meeting category requirements.