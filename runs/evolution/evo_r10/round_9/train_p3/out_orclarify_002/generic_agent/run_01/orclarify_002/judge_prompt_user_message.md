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

QUESTION: What is the exact rule for how many trained pilots a single fighter jet produces when it is allocated to training in a given year (for example, a fixed number of pilots per jet per year, or a rate that depends on something else)?

## Turn 1 - User Simulator

Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: When a jet is allocated to training in a year, does it train 5 pilots in that same year only, or does it continue training pilots in subsequent years as well (i.e., is the allocation a per-year flow or a standing assignment)?

## Turn 2 - User Simulator

The allocation is a per-year flow. A jet allocated to training in a given year trains 5 pilots in that same year only.

## Turn 3 - Generic Agent

QUESTION: Are the jets produced in a given year available to be allocated to training in that same year, or do they only become available starting the following year?

## Turn 3 - User Simulator

The jets produced in a given year are available to be allocated to training in that same year.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a year can be allocated to training (for example, a maximum fraction or number), or can all jets produced in a year be allocated to training if that is optimal?

## Turn 4 - User Simulator

There is no stated limit on how many of the jets produced in a year can be allocated to training. All jets produced in a year can be allocated to training if that is optimal.

## Turn 5 - Generic Agent

QUESTION: Is there any requirement that some jets must be kept for other purposes (e.g., operational/combat use), or is the only goal to maximize the total number of trained pilots by the end of year 2 with no other constraints?

## Turn 5 - User Simulator

The only goal is to maximize the total number of trained pilots by the end of year 2. There is no requirement that some jets must be kept for other purposes.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Production:** 10 jets produced in year 1 (a1 = 10), 15 jets produced in year 2 (a2 = 15).
- **Availability:** Jets produced in a given year are available for allocation in that same year.
- **Training rule:** Each jet allocated to training in a given year trains exactly 5 pilots in that same year only (per-year flow, no carryover effect).
- **Allocation variable:** For each year, a non-negative integer (or continuous, since 5×integer is linear) number of jets allocated to training, bounded above by that year's production.
- **No other constraints:** No minimum operational reserve, no cap on training allocation, no other uses for jets.
- **Horizon:** 2 years.

The model is straightforward: allocate all 10 jets in year 1 and all 15 jets in year 2 to training, yielding 10×5 + 15×5 = 50 + 75 = **125 trained pilots** by the end of year 2.