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

QUESTION: In year 1, how many of the 10 newly produced fighter jets must be allocated exclusively for pilot training?

## Turn 1 - User Simulator

The number of fighter jets that must be allocated exclusively for pilot training in year 1 is not specified in the information I have. That point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: How many trained pilots does one fighter jet produce per year when it is allocated exclusively for pilot training?

## Turn 2 - User Simulator

One fighter jet allocated exclusively for pilot training produces 5 trained pilots per year.

## Turn 3 - Generic Agent

QUESTION: Do the fighter jets allocated for training in year 1 remain available for training in year 2 as well, or are they used only in the year they are allocated?

## Turn 3 - User Simulator

The fighter jets allocated for training in year 1 remain available for training in year 2 as well.

## Turn 4 - Generic Agent

QUESTION: In year 2, are the 15 newly produced fighter jets also subject to a requirement that some of them must be allocated exclusively for pilot training, and if so, how many?

## Turn 4 - User Simulator

The number of the 15 newly produced fighter jets in year 2 that must be allocated exclusively for pilot training is not specified in the information I have. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are the 10 fighter jets produced in year 1 (including any allocated for training) still available and counted in year 2, or does only the year-2 production of 15 jets matter for year 2?

## Turn 5 - User Simulator

The 10 fighter jets produced in year 1 are still available and counted in year 2.

## Turn 6 - Generic Agent

QUESTION: Do the 5 trained pilots produced by a training jet in a given year carry over and accumulate into the total trained pilots available by the end of year 2, or does only the pilots produced in year 2 count toward that total?

## Turn 6 - User Simulator

The 5 trained pilots produced by a training jet in a given year carry over and accumulate into the total trained pilots available by the end of year 2.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how many of the available fighter jets can be allocated to training in a given year, or can all available jets be used for training if desired?

## Turn 7 - User Simulator

There is no limit on how many of the available fighter jets can be allocated to training in a given year; all available jets can be used for training if desired.

## Turn 8 - Generic Agent

QUESTION: Since the number of jets that must be allocated to training in year 1 and year 2 is not yet confirmed, should the model treat the number of training jets in each year as a decision variable to be chosen (e.g., to maximize trained pilots), or is it a fixed requirement that will be provided later?

## Turn 8 - User Simulator

The number of training jets in each year is a decision variable to be chosen to maximize trained pilots.

## Turn 9 - Generic Agent

QUESTION: When a fighter jet is allocated to training in a given year, is it still available to be allocated to training in the following year, or does allocating it to training in one year remove it from the pool for the next year?

## Turn 9 - User Simulator

A fighter jet allocated to training in a given year is still available to be allocated to training in the following year.

## Turn 10 - Generic Agent

QUESTION: Is there any other use or requirement for fighter jets besides pilot training that would reduce the number available for training, or are all available jets free to be allocated to training?

## Turn 10 - User Simulator

There is no other use or requirement for fighter jets besides pilot training that would reduce the number available for training; all available jets are free to be allocated to training.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Production:** Year 1 produces 10 fighter jets (a1 = 10); year 2 produces 15 fighter jets (a2 = 15).
- **Jet availability:** Jets produced in year 1 remain available in year 2. A jet allocated to training in one year remains available for training in the following year.
- **Training allocation:** The number of jets allocated to training in each year is a decision variable. There is no upper limit — all available jets can be allocated to training if desired. There is no other use or requirement for jets besides training.
- **Pilot output:** Each jet allocated to training in a given year produces 5 trained pilots that year.
- **Accumulation:** Trained pilots produced in a given year carry over and accumulate into the total available by the end of year 2.
- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Unspecified (parked):** The exact "must be allocated" minimums for training in year 1 and year 2 were not provided; since allocation is a free decision variable with no other competing use, the optimal choice is to allocate all available jets to training in both years.

**Model:**
- Decision variables: x1 = number of jets allocated to training in year 1; x2 = number of jets allocated to training in year 2.
- Constraints:
  - x1 ≤ 10 (only year-1 production is available in year 1)
  - x2 ≤ 10 + 15 = 25 (year-1 jets carry over plus year-2 production)
  - x1, x2 ≥ 0
- Objective: Maximize 5·x1 + 5·x2 (pilots from year 1 and year 2 both accumulate).

**Optimal solution:** x1 = 10, x2 = 25. Total trained pilots by end of year 2 = 5·10 + 5·25 = 50 + 125 = **175**.