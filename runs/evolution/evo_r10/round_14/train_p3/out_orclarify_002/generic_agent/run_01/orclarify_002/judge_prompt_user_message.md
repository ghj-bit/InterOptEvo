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

QUESTION: What is the exact rule linking jets allocated to training in a given year to the number of pilots trained (for example, how many trained pilots does one training jet produce per year, and does a jet in training produce pilots in the same year it is allocated or only in the following year)?

## Turn 1 - User Simulator

One training jet produces 5 trained pilots per year. A jet allocated to training in a given year produces those pilots in that same year.

## Turn 2 - Generic Agent

QUESTION: Are the training jets allocated in a given year drawn from that year's production (a1, a2), or can jets produced in earlier years also be allocated to training in later years?

## Turn 2 - User Simulator

Training jets allocated in a given year are drawn from that year's production.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a given year may be allocated to training (for example, a maximum fraction or count), or can all of that year's production be allocated to training if that is optimal?

## Turn 3 - User Simulator

There is no stated limit on how many of the jets produced in a given year may be allocated to training.

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is the number of jets allocated to training in each year fixed by some other requirement (e.g., a minimum or exact number of training jets per year)?

## Turn 4 - User Simulator

The goal is to maximize the total number of trained pilots by the end of year 2.

## Turn 5 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in subsequent years, or are they consumed/retired after that year's training (so each year's training jets must come fresh from that year's production)?

## Turn 5 - User Simulator

Jets allocated to training in a given year remain available for training in subsequent years.

## Turn 6 - Generic Agent

QUESTION: Since jets remain available for training in subsequent years, can a jet that was allocated to training in year 1 be counted again as a training jet in year 2 (producing pilots in both years), or does each jet produce pilots in only one year total?

## Turn 6 - User Simulator

A jet allocated to training in year 1 can be counted again as a training jet in year 2, producing pilots in both years.

## Turn 7 - Generic Agent

QUESTION: When a training jet from year 1 carries over to year 2, is it still drawn from year 1's production (so year 2's training fleet can include both year 1's carried-over jets and year 2's new production), or must year 2's training jets come only from year 2's production?

## Turn 7 - User Simulator

Year 2's training fleet can include both year 1's carried-over jets and year 2's new production.

## Turn 8 - Generic Agent

QUESTION: Are there any other uses or constraints on the jets besides training (for example, a requirement that some jets be kept for combat/operational use, or a limit on total fleet size), or is the only decision how many jets to allocate to training each year?

## Turn 8 - User Simulator

There are no other uses or constraints on the jets besides training. The only decision is how many jets to allocate to training each year.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Production:** Year 1 produces a1 = 10 jets; year 2 produces a2 = 15 jets.
- **Decision:** In each year, choose how many jets to allocate to training.
- **Training rule:** One training jet produces 5 trained pilots in the year it is allocated.
- **Carryover:** A jet allocated to training in year 1 remains available and can be counted again as a training jet in year 2 (producing pilots in both years). Year 2's training fleet can include both year 1's carried-over training jets and newly allocated jets from year 2's production.
- **No limits:** There is no cap on how many jets may be allocated to training in any year, and there are no other uses or constraints on the jets.
- **Horizon:** 2 years; the total trained pilots is the sum of pilots produced in year 1 and year 2.

Since there is no limit on training allocation and no competing use, the optimal policy is to allocate every available jet to training in each year:
- Year 1: 10 jets → 10 × 5 = 50 pilots.
- Year 2: 10 (carried over) + 15 (new) = 25 jets → 25 × 5 = 125 pilots.
- **Total trained pilots by end of year 2: 175.**