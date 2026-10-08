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

QUESTION: What is the exact rule linking jets allocated to training in a given year to the number of pilots trained that year — for example, does each training jet train exactly one pilot per year, or is there a different rate or a fixed number of pilots per training jet?

## Turn 1 - User Simulator

Each training jet trains exactly 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Are the jets allocated to training in a given year drawn from that same year's production, or can jets produced in earlier years be carried over and used for training in later years?

## Turn 2 - User Simulator

Jets allocated to training in a given year are drawn from that same year's production.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a year can be allocated to training — for example, a maximum fraction or number that must be reserved for training, or a minimum that must be allocated?

## Turn 3 - User Simulator

There is no stated limit on how many of the jets produced in a year can be allocated to training.

## Turn 4 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years, or are they consumed/retired after that year's training?

## Turn 4 - User Simulator

Jets allocated to training in a given year remain available for training in later years.

## Turn 5 - Generic Agent

QUESTION: Since training jets remain available in later years, do they continue to train 5 pilots each in every subsequent year they are in service, or do they train pilots only in the year they were allocated?

## Turn 5 - User Simulator

Training jets continue to train 5 pilots each in every subsequent year they are in service.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the total number of training jets that can be in service at once — for example, a maximum fleet size for training, or a cap on how many jets can be allocated to training in total across both years?

## Turn 6 - User Simulator

There is no stated limit on the total number of training jets that can be in service at once.

## Turn 7 - Generic Agent

QUESTION: When you say "total number of trained pilots available by the end of year 2," do you mean the cumulative total of all pilots trained across both years (year 1 plus year 2), or only the pilots trained in year 2?

## Turn 7 - User Simulator

It means the cumulative total of all pilots trained across both years (year 1 plus year 2).

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements I should be aware of — for example, a minimum number of jets that must be allocated to training each year, or any other business rules that affect the allocation decision?

## Turn 8 - User Simulator

No, there are no other constraints or requirements beyond what has already been discussed.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Production:** Year 1 produces a1 = 10 jets; Year 2 produces a2 = 15 jets.
- **Training allocation:** In each year, some number of that year's newly produced jets can be allocated to training. There is no upper or lower bound on how many can be allocated (including the possibility of allocating all or none).
- **Training jets persist:** Once a jet is allocated to training, it remains in the training fleet in all subsequent years.
- **Training rate:** Each training jet trains exactly 5 pilots per year, in every year it is in service.
- **Objective:** Maximize the cumulative total number of pilots trained across Year 1 and Year 2 (i.e., pilots trained in Year 1 plus pilots trained in Year 2).
- **No other constraints** apply.

**Model:**

Decision variables:
- x1 = number of Year 1 jets allocated to training (0 ≤ x1 ≤ 10, integer)
- x2 = number of Year 2 jets allocated to training (0 ≤ x2 ≤ 15, integer)

Pilots trained:
- Year 1: 5 · x1
- Year 2: 5 · (x1 + x2)  (Year 1 training jets persist into Year 2)

Objective: Maximize 5·x1 + 5·(x1 + x2) = 10·x1 + 5·x2

Constraints:
- 0 ≤ x1 ≤ 10
- 0 ≤ x2 ≤ 15
- x1, x2 integers

**Optimal solution:** x1 = 10, x2 = 15

- Year 1 pilots: 5 × 10 = 50
- Year 2 pilots: 5 × (10 + 15) = 125
- **Total trained pilots by end of Year 2: 175**