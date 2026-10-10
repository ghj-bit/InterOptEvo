# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U2
I need help determining the number of trained pilots that can be provided by a fighter jet production and training setup, where some fighter jets each year must be allocated exclusively for pilot training. Specifically, determine the total number of trained pilots available by the end of year 2.

Annual fighter jet production: a1 = 10, a2 = 15.

## Problem units
- U1 (context): I need help determining the number of trained pilots that can be provided by a fighter jet production and training setup.
- U2 (data): Annual fighter jet production: a1 = 10, a2 = 15.
- U3 (constraint): Each training jet can train 5 pilots per year.
- U4 (constraint): Each trained pilot can operate one combat jet in subsequent years.
- U5 (constraint): Some fighter jets each year must be allocated exclusively for pilot training.
- U6 (assumption): Training starts in year 1 and continues for 2 years.
- U7 (objective): Determine the total number of trained pilots available by the end of year 2.

## Hidden slot scoring rules
## H1: training_capacity_per_jet
- Severity: P0
- Severity reason: Without the per-jet training capacity, it is impossible to calculate the number of pilots trained per year, which is essential to achieving the objective. The model would be completely indeterminate.
- Problem unit ID: U3
- Semantic hit rule: The agent's question must explicitly ask about the per-year pilot training capacity of each training jet.
- Reference acceptable questions:
  - How many pilots can each training jet train per year?
  - What is the training capacity of a single jet in terms of pilots?
- Failure modes:
  - Assuming each jet can train 1 pilot per year
  - Assuming unlimited training capacity per jet
  - Assuming training capacity is proportional to jet age or type

## H2: pilot_to_combat_jet_mapping
- Severity: P2
- Severity reason: Without this information, the number of trained pilots available for air defense could be misinterpreted, but a reasonable model would still treat trained pilots as directly contributing. The missing unit clarifies the one-to-one mapping, but the total count of trained pilots remains the same. Omitting this does not prevent computing the number of trained pilots, so it is a low-impact detail.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must ask about the relationship between trained pilots and combat jets, specifically the number of jets a pilot can operate.
- Reference acceptable questions:
  - How many combat jets can a trained pilot operate?
  - Is there a limit on how many jets a pilot can handle?
- Failure modes:
  - Assuming each pilot can operate multiple combat jets
  - Assuming pilots need further training before operating any combat jet
  - Assuming the pilot-to-jet ratio depends on jet type

## H3: training_duration_and_start
- Severity: P1
- Severity reason: The start year and duration of training are not completely determined from the objective alone, and without them, the model might incorrectly set the training timeline, leading to a wrong total. A responsible agent should clarify the exact training period.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must mention the start year or the duration of the training program.
- Reference acceptable questions:
  - When does the training program start?
  - How many years does the training last?
- Failure modes:
  - Assuming training has already started before year 1
  - Assuming training lasts only 1 year
  - Assuming training continues indefinitely


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are the annual fighter jet production figures of 10 in year 1 and 15 in year 2 the total jets produced each year, with some of those jets then allocated to training, or are they the number of jets available for operational use after training jets have already been set aside?

## Turn 1 - User Simulator

They are the total jets produced each year. Some of those jets are then allocated to training.

## Turn 2 - Generic Agent

QUESTION: How many trained pilots does one training jet produce per year, and is that number the same in both year 1 and year 2?

## Turn 2 - User Simulator

One training jet produces 5 trained pilots per year. That number is the same in both year 1 and year 2.

## Turn 3 - Generic Agent

QUESTION: Is there a minimum number of training jets that must be allocated each year, and if so, what is that minimum for year 1 and year 2?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum number of training jets that can be allocated each year, or is the only limit that the number of training jets cannot exceed the total jets produced that year?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are the training jets allocated in a given year reusable for training in the following year, or are they consumed and must be replaced by newly produced jets each year?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are the trained pilots produced in year 1 still available and counted in the total at the end of year 2, or does the "total number of trained pilots available by the end of year 2" refer only to the pilots trained during year 2?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a fixed allocation rule that determines how many jets are assigned to training each year?

## Turn 7 - User Simulator

The goal is to maximize the total number of trained pilots by the end of year 2.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints on the allocation of jets to training, such as a requirement that a certain number of jets must remain available for operational use each year?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the training jets allocated in a given year reusable for training in the following year, or are they consumed and must be replaced by newly produced jets each year?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Production:** Total fighter jets produced are 10 in Year 1 and 15 in Year 2.
2.  **Training Rate:** Each training jet produces 5 trained pilots per year. This rate is constant across both years.
3.  **Objective:** Maximize the total number of trained pilots available by the end of Year 2.
4.  **Allocation:** Some fraction of the total jets produced each year is allocated exclusively for pilot training.

**Assumptions (due to lack of confirmation):**
1.  **No Minimum Training Jets:** There is no minimum number of training jets required each year.
2.  **No Maximum Training Jets:** There is no maximum number of training jets allowed other than the total production limit (i.e., all produced jets can be allocated to training if it maximizes the objective).
3.  **No Carryover/Reusability:** Training jets are not reusable across years. The jets allocated to training in Year 1 are distinct from those in Year 2. The production figures represent the total available pool for that specific year's allocation.
4.  **Cumulative Count:** The "total number of trained pilots available by the end of year 2" is the cumulative sum of pilots trained in Year 1 and Year 2.
5.  **No Operational Constraints:** There are no constraints requiring a minimum number of jets to remain for operational use; the only constraint is that the number of training jets cannot exceed the total production for that year.

**Model Formulation:**
Let $x_1$ be the number of training jets in Year 1.
Let $x_2$ be the number of training jets in Year 2.

**Objective:**
Maximize $Z = 5x_1 + 5x_2$

**Constraints:**
1.  $0 \le x_1 \le 10$ (Training jets in Year 1 cannot exceed production)
2.  $0 \le x_2 \le 15$ (Training jets in Year 2 cannot exceed production)
3.  $x_1, x_2$ are non-negative integers (assuming discrete jets)

**Solution:**
To maximize $Z$, we set $x_1$ and $x_2$ to their maximum possible values.
$x_1 = 10$
$x_2 = 15$

$Z = 5(10) + 5(15) = 50 + 75 = 125$

**Total trained pilots by end of Year 2: 125**