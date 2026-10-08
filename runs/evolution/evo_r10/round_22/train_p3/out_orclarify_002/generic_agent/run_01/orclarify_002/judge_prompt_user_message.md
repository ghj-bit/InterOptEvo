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

QUESTION: How many trained pilots does one fighter jet produce per year when it is allocated to pilot training?

## Turn 2 - User Simulator

One fighter jet allocated to pilot training produces 5 trained pilots per year.

## Turn 3 - Generic Agent

QUESTION: Do the fighter jets allocated to training in year 1 remain available for training in year 2 as well, or are they used only in the year they are allocated?

## Turn 3 - User Simulator

The fighter jets allocated to training in year 1 remain available for training in year 2 as well.

## Turn 4 - Generic Agent

QUESTION: In year 2, how many of the 15 newly produced fighter jets must be allocated exclusively for pilot training?

## Turn 4 - User Simulator

The number of fighter jets that must be allocated exclusively for pilot training in year 2 is not specified in the information I have. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are there any limits on how many fighter jets can be allocated to training in a given year, or can any number of the available jets be assigned to training?

## Turn 5 - User Simulator

There are no limits on how many fighter jets can be allocated to training in a given year; any number of the available jets can be assigned to training.

## Turn 6 - Generic Agent

QUESTION: Since the number of jets allocated to training each year is not fixed, should the model choose the allocation that maximizes the total number of trained pilots by the end of year 2?

## Turn 6 - User Simulator

Yes, the model should choose the allocation that maximizes the total number of trained pilots by the end of year 2.

## Turn 7 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero?

## Turn 7 - User Simulator

The fleet starts at zero at the start of year 1.

## Turn 8 - Generic Agent

QUESTION: Do the jets allocated to training in year 1 continue producing pilots in year 2 at the same rate of 5 pilots per jet per year?

## Turn 8 - User Simulator

Yes, the jets allocated to training in year 1 continue producing pilots in year 2 at the same rate of 5 pilots per jet per year.

## Turn 9 - Generic Agent

QUESTION: Do the newly produced jets in year 2 (the 15 jets) also produce pilots in year 2 if allocated to training, or do they only start producing pilots in year 3?

## Turn 9 - User Simulator

The newly produced jets in year 2 also produce pilots in year 2 if allocated to training.

## Turn 10 - Generic Agent

QUESTION: Are the trained pilots produced in year 1 and year 2 both counted in the total, or only the pilots produced in year 2?

## Turn 10 - User Simulator

Both the trained pilots produced in year 1 and year 2 are counted in the total.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or costs associated with allocating jets to training, such as maintenance costs or a minimum number of jets that must remain in operational (non-training) status?

## Turn 11 - User Simulator

There are no other constraints or costs associated with allocating jets to training, such as maintenance costs or a minimum number of jets that must remain in operational status.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Horizon:** 2 years (year 1 and year 2).
- **Production:** 10 jets produced in year 1, 15 jets produced in year 2.
- **Initial fleet:** 0 jets at the start of year 1.
- **Training allocation:**
  - Any number of available jets can be allocated to training each year (no upper or lower bound on the allocation).
  - The number of jets allocated to training in each year is a decision variable (not fixed).
  - Jets allocated to training in year 1 remain available for training in year 2.
  - Newly produced jets in year 2 can also be allocated to training in year 2.
- **Pilot production rate:** Each jet allocated to training produces 5 trained pilots per year.
- **Pilot counting:** Pilots produced in both year 1 and year 2 are counted in the total.
- **No other constraints:** No maintenance costs, no minimum operational fleet requirement, no other costs or limits.

**Model summary:**
- Decision variables: x1 = number of jets allocated to training in year 1 (from the 10 produced), x2 = number of additional jets allocated to training in year 2 (from the 15 produced in year 2).
- Jets in training in year 1: x1
- Jets in training in year 2: x1 + x2 (year 1 jets carry over, plus new year 2 jets)
- Pilots in year 1: 5 * x1
- Pilots in year 2: 5 * (x1 + x2)
- Total pilots: 5*x1 + 5*(x1 + x2) = 10*x1 + 5*x2
- Constraints: 0 ≤ x1 ≤ 10, 0 ≤ x2 ≤ 15
- Optimal solution: x1 = 10, x2 = 15 → Total pilots = 10*10 + 5*15 = 100 + 75 = **175 trained pilots**.