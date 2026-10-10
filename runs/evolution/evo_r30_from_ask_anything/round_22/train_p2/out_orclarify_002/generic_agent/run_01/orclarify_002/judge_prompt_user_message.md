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

QUESTION: What is the number of trained pilots that a single fighter jet can produce in one year when it is allocated exclusively for pilot training?

## Turn 1 - User Simulator

A single fighter jet allocated exclusively for pilot training can train 5 pilots in one year.

## Turn 2 - Generic Agent

QUESTION: Are the fighter jets produced in year 1 available for pilot training in year 2, or does each year's production only serve that same year's training needs?

## Turn 2 - User Simulator

The fighter jets produced in year 1 are available for pilot training in year 2.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on the total number of fighter jets that can be allocated to pilot training in any given year, or can all available jets be used for training?

## Turn 3 - User Simulator

There is no stated limit on the total number of fighter jets that can be allocated to pilot training in any given year; all available jets can be used for training.

## Turn 4 - Generic Agent

QUESTION: Do the fighter jets produced in year 2 also carry over to year 3 or beyond, or is the analysis strictly limited to years 1 and 2 with no carryover past year 2?

## Turn 4 - User Simulator

The analysis is strictly limited to years 1 and 2 with no carryover past year 2.

## Turn 5 - Generic Agent

QUESTION: Are the fighter jets produced in year 1 available for training in year 1 itself, or do they only become available starting in year 2?

## Turn 5 - User Simulator

The fighter jets produced in year 1 are available for training in year 1 itself.

## Turn 6 - Generic Agent

QUESTION: Are the fighter jets produced in year 2 available for training in year 2 itself, or do they only become available starting in year 3?

## Turn 6 - User Simulator

The fighter jets produced in year 2 are available for training in year 2 itself.

## Turn 7 - Generic Agent

QUESTION: Is the total number of trained pilots available by the end of year 2 the sum of pilots trained in year 1 plus pilots trained in year 2, or does the term "available" refer only to pilots trained in year 2?

## Turn 7 - User Simulator

The total number of trained pilots available by the end of year 2 is the sum of pilots trained in year 1 plus pilots trained in year 2.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed facts:**
- Annual fighter jet production: year 1 = 10 jets, year 2 = 15 jets.
- Each fighter jet allocated exclusively to pilot training produces 5 trained pilots per year.
- Fighter jets produced in year 1 are available for training in year 1 and carry over to year 2.
- Fighter jets produced in year 2 are available for training in year 2.
- There is no limit on the number of jets that can be allocated to training in any year; all available jets can be used.
- The analysis is strictly limited to years 1 and 2 with no carryover past year 2.
- The total number of trained pilots available by the end of year 2 is the sum of pilots trained in year 1 plus pilots trained in year 2.

**Assumptions (none required):** All formulation-critical facts were confirmed by the user.

**Model summary:**
- Decision variables: Let x1 = number of jets allocated to training in year 1, x2 = number of jets allocated to training in year 2.
- Objective: Maximize total trained pilots = 5*x1 + 5*x2.
- Constraints:
  - x1 ≤ 10 (only year 1 production available in year 1)
  - x2 ≤ 10 + 15 = 25 (year 1 jets carry over plus year 2 production available in year 2)
  - x1, x2 ≥ 0
- Since all available jets can be used and there is no other constraint, the optimal allocation is x1 = 10 and x2 = 25.
- Total trained pilots by end of year 2 = 5*10 + 5*25 = 50 + 125 = 175.