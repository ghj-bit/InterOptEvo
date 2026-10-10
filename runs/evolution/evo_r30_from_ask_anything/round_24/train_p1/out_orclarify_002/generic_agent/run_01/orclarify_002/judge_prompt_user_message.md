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

QUESTION: What is the number of trained pilots that a single fighter jet can produce when allocated exclusively for pilot training in a given year?

## Turn 1 - User Simulator

A single fighter jet allocated exclusively for pilot training can train 5 pilots in a given year.

## Turn 2 - Generic Agent

QUESTION: Are the fighter jets allocated for pilot training in a given year drawn from that year's production, or can they also include jets produced in previous years?

## Turn 2 - User Simulator

The fighter jets allocated for pilot training in a given year are drawn from that year's production.

## Turn 3 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated for pilot training each year, or can the allocation be zero?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated for pilot training in a given year, or is the only limit the total production available that year?

## Turn 4 - User Simulator

The only limit is the total production available that year.

## Turn 5 - Generic Agent

QUESTION: Are the trained pilots produced in year 1 still available and counted in the total at the end of year 2, or do they expire or leave after their training year?

## Turn 5 - User Simulator

The trained pilots produced in year 1 are still available and counted in the total at the end of year 2.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots available by the end of year 2, or is there a fixed allocation rule that determines how many jets are assigned to training each year?

## Turn 6 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed facts:**
- Annual fighter jet production: Year 1 = 10, Year 2 = 15.
- Fighter jets allocated for training in a given year are drawn exclusively from that year's production.
- Each fighter jet allocated to training produces 5 trained pilots in that year.
- Trained pilots accumulate; pilots trained in Year 1 remain available and are counted in the total at the end of Year 2.
- The only constraint on the number of jets allocated to training in a given year is the total production available that year (i.e., allocation cannot exceed production).
- The objective is to maximize the total number of trained pilots available by the end of Year 2.

**Assumptions:**
- There is no minimum number of jets that must be allocated to training each year (allocation can be zero).
- There are no other constraints on jet allocation (e.g., no requirement to reserve jets for operational use, no exclusivity rules beyond the training allocation itself).
- Jets not allocated to training are simply not used for pilot production and do not affect the pilot count.

**Model Formulation:**

Let \( x_1 \) = number of jets allocated to training in Year 1.
Let \( x_2 \) = number of jets allocated to training in Year 2.

**Objective:**
Maximize \( Z = 5x_1 + 5x_2 \)

**Constraints:**
- \( x_1 \leq 10 \)
- \( x_2 \leq 15 \)
- \( x_1 \geq 0 \)
- \( x_2 \geq 0 \)

**Solution:**
Since the objective is to maximize pilot output and there are no other constraints limiting allocation, the optimal solution is to allocate all available jets to training in both years:
- \( x_1 = 10 \)
- \( x_2 = 15 \)

Total trained pilots by end of Year 2:
\( Z = 5(10) + 5(15) = 50 + 75 = 125 \)

**Answer: 125 trained pilots.**