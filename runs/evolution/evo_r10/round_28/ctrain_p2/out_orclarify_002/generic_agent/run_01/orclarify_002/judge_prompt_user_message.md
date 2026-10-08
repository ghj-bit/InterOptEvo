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

QUESTION: Are the 15 jets produced in year 2 also eligible to be allocated to training in year 2, or are they only available starting in year 3?

## Turn 4 - User Simulator

The 15 jets produced in year 2 are eligible to be allocated to training in year 2.

## Turn 5 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to training each year, and if so, what is that minimum for year 1 and year 2?

## Turn 5 - User Simulator

The minimum number of fighter jets that must be allocated to training each year is not specified in the information I have. That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to training in any given year, or can all available jets be used for training?

## Turn 6 - User Simulator

There is no maximum number of fighter jets that can be allocated to training in any given year; all available jets can be used for training.

## Turn 7 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start empty and only the newly produced jets are available?

## Turn 7 - User Simulator

The fleet starts empty at the beginning of year 1; only the newly produced jets are available.

## Turn 8 - Generic Agent

QUESTION: Since the minimum number of jets that must be allocated to training each year is still unconfirmed, should I assume that the number of jets allocated to training in each year is a free decision variable (i.e., we choose how many to allocate, with no lower bound other than zero)?

## Turn 8 - User Simulator

Yes, the number of jets allocated to training in each year is a free decision variable, with no lower bound other than zero.

## Turn 9 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a specific target number of trained pilots that must be met?

## Turn 9 - User Simulator

The goal is to maximize the total number of trained pilots by the end of year 2.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Fleet start:** Empty at the beginning of year 1; only newly produced jets are available.
- **Production:** 10 jets in year 1, 15 jets in year 2.
- **Training capacity:** Each jet allocated to training produces 5 trained pilots per year.
- **Jet persistence:** Jets allocated to training in year 1 remain available for training in year 2.
- **Year-2 jets:** The 15 jets produced in year 2 are eligible for training in year 2.
- **Allocation decision:** The number of jets allocated to training each year is a free decision variable with no lower bound other than zero and no upper bound other than the number of available jets.
- **Objective:** Maximize the total number of trained pilots by the end of year 2.

**Model:**

Let:
- x1 = number of jets allocated to training in year 1 (0 ≤ x1 ≤ 10)
- x2 = number of jets allocated to training in year 2 (0 ≤ x2 ≤ 10 + 15 = 25)

Note: In year 2, the available jets are the 10 from year 1 (all still in the fleet) plus the 15 newly produced, so up to 25 jets can be allocated.

Objective: Maximize 5·x1 + 5·x2

Constraints:
- 0 ≤ x1 ≤ 10
- 0 ≤ x2 ≤ 25

Since the objective is to maximize and there is no cost or trade-off to allocating jets to training, the optimal solution is:
- x1 = 10
- x2 = 25

Total trained pilots by end of year 2 = 5(10) + 5(25) = 50 + 125 = **175 trained pilots**.