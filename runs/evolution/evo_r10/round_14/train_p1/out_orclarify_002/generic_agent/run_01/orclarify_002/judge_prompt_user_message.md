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

QUESTION: What is the exact rule for how many fighter jets each year must be allocated exclusively for pilot training — is it a fixed number, a fraction of that year's production, or some other formula?

## Turn 1 - User Simulator

The rule is not a fixed number, a fraction of that year’s production, or a specific formula. The requirement is simply that some fighter jets each year must be allocated exclusively for pilot training. The exact number to be allocated each year is not predetermined; it is part of what needs to be determined to maximize the total number of trained pilots by the end of year 2.

## Turn 2 - Generic Agent

QUESTION: How many trained pilots does one fighter jet produce per year when it is allocated to pilot training?

## Turn 2 - User Simulator

Each training jet can train 5 pilots per year.

## Turn 3 - Generic Agent

QUESTION: Do the training jets allocated in year 1 remain available for training in year 2 as well, or does each year's training allocation consist only of that year's newly produced jets?

## Turn 3 - User Simulator

The training jets allocated in year 1 remain available for training in year 2 as well.

## Turn 4 - Generic Agent

QUESTION: Are there any limits on how many of the newly produced jets in each year can be allocated to training — for example, must at least some jets be kept for other purposes (combat, reserves), or can all of a year's production be sent to training?

## Turn 4 - User Simulator

There are no limits on how many of the newly produced jets in each year can be allocated to training. All of a year's production can be sent to training.

## Turn 5 - Generic Agent

QUESTION: When a training jet trains pilots, does it train 5 pilots in each year it is in service (so a jet allocated in year 1 trains 5 in year 1 and another 5 in year 2, for 10 total), or does it train 5 pilots only in the year it is first allocated?

## Turn 5 - User Simulator

A training jet trains 5 pilots in each year it is in service. So a jet allocated in year 1 trains 5 pilots in year 1 and another 5 pilots in year 2, for 10 total.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 2 years (year 1 and year 2).
- **Production:** a1 = 10 jets in year 1, a2 = 15 jets in year 2.
- **Decision:** How many of each year's newly produced jets to allocate to pilot training (x1 in year 1, x2 in year 2).
- **Training capacity:** Each training jet trains 5 pilots per year it is in service.
- **Persistence:** Jets allocated to training in year 1 remain in training in year 2 as well (cumulative fleet).
- **No other constraints:** All of a year's production may be allocated to training; no minimum must be reserved for other purposes.
- **Objective:** Maximize the total number of trained pilots available by the end of year 2.

The total trained pilots by end of year 2 = 5·x1 (year 1) + 5·(x1 + x2) (year 2) = 10·x1 + 5·x2, subject to 0 ≤ x1 ≤ 10 and 0 ≤ x2 ≤ 15.