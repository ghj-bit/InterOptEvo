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

QUESTION: What is the number of fighter jets that must be allocated exclusively for pilot training each year?

## Turn 1 - User Simulator

The number of fighter jets allocated exclusively for pilot training each year is not specified in the information I have. That point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: How many trained pilots does each fighter jet allocated to training produce per year?

## Turn 2 - User Simulator

Each fighter jet allocated to training produces 5 trained pilots per year.

## Turn 3 - Generic Agent

QUESTION: Do the fighter jets allocated to training in a given year remain available for training in subsequent years, or are they only used for training in the year they are allocated?

## Turn 3 - User Simulator

The fighter jets allocated to training in a given year remain available for training in subsequent years.

## Turn 4 - Generic Agent

QUESTION: Are the training jets allocated in year 1 and year 2 drawn from that year's production only, or can jets produced in earlier years also be allocated to training in later years?

## Turn 4 - User Simulator

The training jets allocated in year 1 and year 2 are drawn from that year's production only.

## Turn 5 - Generic Agent

QUESTION: Do the training jets allocated in year 1 continue to produce pilots in year 2 as well, or does each training jet only produce pilots in the single year it is allocated?

## Turn 5 - User Simulator

The training jets allocated in year 1 continue to produce pilots in year 2 as well.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a given year can be allocated to training, or can all of that year's production be allocated to training?

## Turn 6 - User Simulator

There is no limit on how many of the jets produced in a given year can be allocated to training; all of that year's production can be allocated to training.

## Turn 7 - Generic Agent

QUESTION: Are the trained pilots produced in year 1 still counted as "available" by the end of year 2, or does "available by the end of year 2" mean only the pilots produced in year 2?

## Turn 7 - User Simulator

The trained pilots produced in year 1 are still counted as "available" by the end of year 2.

## Turn 8 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots available by the end of year 2, or is there a fixed number of training jets that must be allocated each year (i.e., the allocation is predetermined rather than a decision)?

## Turn 8 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Production:** Year 1 produces a1 = 10 fighter jets; Year 2 produces a2 = 15 fighter jets.
- **Decision:** Each year, choose how many of that year's newly produced jets to allocate to training (0 up to the full production of that year).
- **Training capacity:** Each training jet produces 5 trained pilots per year.
- **Persistence:** A training jet allocated in year 1 continues to produce pilots in year 2 as well.
- **No carryover of jets:** Training jets in year 2 can only come from year 2's production (not from year 1's jets).
- **Objective:** Maximize the total number of trained pilots available by the end of year 2 (cumulative: pilots produced in year 1 + pilots produced in year 2).
- **No upper bound** on the number of jets allocated to training beyond the year's production.

The model is a simple two-period allocation:
- Let x1 = number of year-1 jets allocated to training (0 ≤ x1 ≤ 10).
- Let x2 = number of year-2 jets allocated to training (0 ≤ x2 ≤ 15).
- Pilots in year 1: 5·x1.
- Pilots in year 2: 5·x1 + 5·x2 (year-1 jets persist, plus new year-2 jets).
- Total pilots by end of year 2: 5·x1 + 5·x1 + 5·x2 = 10·x1 + 5·x2.
- Maximize 10·x1 + 5·x2 subject to 0 ≤ x1 ≤ 10, 0 ≤ x2 ≤ 15.

Optimal solution: x1 = 10, x2 = 15, giving a maximum of 10·10 + 5·15 = 175 trained pilots by the end of year 2.