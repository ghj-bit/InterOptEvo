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

QUESTION: What is the exact rule linking jets allocated to training in a given year to the number of pilots trained in that year (for example, how many trained pilots does one training jet produce per year, and does a jet used for training in year 1 also train pilots in year 2)?

## Turn 1 - User Simulator

Each training jet trains 5 pilots per year. A jet allocated to training in year 1 also trains pilots in year 2, as training continues for both years.

## Turn 2 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 and year 2 drawn from the same pool of production (i.e., a jet produced in year 1 can be used for training in both year 1 and year 2, while a jet produced in year 2 can only be used for training in year 2), or is there a separate production allocation for each year's training needs?

## Turn 2 - User Simulator

The jets allocated to training in year 1 and year 2 are drawn from the same pool of production. A jet produced in year 1 can be used for training in both year 1 and year 2, while a jet produced in year 2 can only be used for training in year 2.

## Turn 3 - Generic Agent

QUESTION: Is there any requirement that a minimum number of jets must be kept available for non-training purposes (e.g., operational deployment) in each year, or can all produced jets be allocated to training if that maximizes the number of trained pilots?

## Turn 3 - User Simulator

There is no requirement that a minimum number of jets must be kept available for non-training purposes. All produced jets can be allocated to training if that maximizes the number of trained pilots.

## Turn 4 - Generic Agent

QUESTION: When you say "determine the total number of trained pilots available by the end of year 2," do you mean the cumulative total of all pilots trained across both years (i.e., pilots trained in year 1 plus pilots trained in year 2), or only the pilots trained in year 2?

## Turn 4 - User Simulator

I mean the cumulative total of all pilots trained across both years (i.e., pilots trained in year 1 plus pilots trained in year 2).

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Production:** a1 = 10 jets in year 1, a2 = 15 jets in year 2.
- **Training allocation:** A jet produced in year 1 can be allocated to training in both year 1 and year 2. A jet produced in year 2 can only be allocated to training in year 2.
- **Training output:** Each training jet trains 5 pilots per year.
- **No minimum operational requirement:** All produced jets may be allocated to training.
- **Objective:** Maximize the cumulative total number of trained pilots across both years (pilots trained in year 1 + pilots trained in year 2).
- **Decision variables:**
  - x1: number of year-1 jets allocated to training in year 1 (and thus also in year 2), 0 ≤ x1 ≤ 10.
  - x2: number of year-2 jets allocated to training in year 2, 0 ≤ x2 ≤ 15.
- **Objective function:** Maximize 5·x1 + 5·x1 + 5·x2 = 10·x1 + 5·x2.
- **Constraints:** 0 ≤ x1 ≤ 10, 0 ≤ x2 ≤ 15.
- **Answer:** Since all coefficients are positive, the optimum is x1 = 10, x2 = 15, giving a cumulative total of 10·10 + 5·15 = 100 + 75 = **175 trained pilots** by the end of year 2.