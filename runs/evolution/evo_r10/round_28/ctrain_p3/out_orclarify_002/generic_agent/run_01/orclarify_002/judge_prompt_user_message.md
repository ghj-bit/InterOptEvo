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

QUESTION: How many trained pilots does one fighter jet produce in a single year of training?

## Turn 2 - User Simulator

One fighter jet produces 5 trained pilots in a single year of training.

## Turn 3 - Generic Agent

QUESTION: In year 2, how many of the 15 newly produced fighter jets must be allocated exclusively for pilot training?

## Turn 3 - User Simulator

The number of fighter jets that must be allocated exclusively for pilot training in year 2 is not specified in the information I have. That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Do the fighter jets allocated for training in year 1 remain available to train pilots again in year 2, or are they used up after one year of training?

## Turn 4 - User Simulator

The fighter jets allocated for training in year 1 remain available to train pilots again in year 2.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced in a year, other than the number of training jets available (i.e., is the only constraint that each training jet produces at most 5 pilots per year)?

## Turn 5 - User Simulator

Yes, the only constraint is that each training jet produces at most 5 pilots per year.

## Turn 6 - Generic Agent

QUESTION: When you say "determine the total number of trained pilots available by the end of year 2," do you mean the maximum total pilots that can be trained over the two years combined (i.e., pilots trained in year 1 plus pilots trained in year 2)?

## Turn 6 - User Simulator

Yes, I mean the maximum total pilots that can be trained over the two years combined (i.e., pilots trained in year 1 plus pilots trained in year 2).

## Turn 7 - Generic Agent

QUESTION: Since the number of training jets in each year is not yet confirmed, is there any rule or formula that determines how many of the newly produced jets each year must go to training (for example, a fixed fraction of that year's production, or a fixed number)?

## Turn 7 - User Simulator

No, there is no rule or formula that determines how many of the newly produced jets each year must go to training. That point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the jets produced in year 1 (the 10 jets) available to be allocated for training in year 2, or can only the jets produced in year 2 be used for training in year 2?

## Turn 8 - User Simulator

The jets produced in year 1 are available to be allocated for training in year 2.

## Turn 9 - Generic Agent

QUESTION: Since the number of training jets each year is not yet confirmed, is the goal to maximize the total pilots trained by choosing how many jets to allocate to training each year (i.e., the allocation is a decision we make), or is the allocation fixed by some external requirement we just don't know yet?

## Turn 9 - User Simulator

The allocation is a decision we make to maximize the total pilots trained.

## Turn 10 - Generic Agent

QUESTION: Are there any other uses for the fighter jets besides pilot training (for example, combat deployment), or are all jets free to be allocated to training if that maximizes pilot output?

## Turn 10 - User Simulator

There are other uses for the fighter jets besides pilot training, such as combat deployment.

## Turn 11 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be kept available for combat deployment each year, and if so, what is that minimum?

## Turn 11 - User Simulator

The minimum number of fighter jets that must be kept available for combat deployment each year is not specified in the information I have. That point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Do the jets allocated to combat deployment in year 1 remain available for use (either combat or training) in year 2, or are they consumed/retired after year 1?

## Turn 12 - User Simulator

The jets allocated to combat deployment in year 1 remain available for use in year 2.

## Turn 13 - Generic Agent

QUESTION: Since the minimum combat deployment requirement is not yet confirmed, is there any other constraint that limits how many jets can be allocated to training in a given year (for example, a cap on the number of training jets, or a requirement that a certain number of jets must be in combat)?

## Turn 13 - User Simulator

No, there is no other constraint that limits how many jets can be allocated to training in a given year.

## Turn 14 - Generic Agent

QUESTION: If all jets can be allocated to training and there is no confirmed minimum combat requirement, does that mean the maximum total pilots trained by the end of year 2 is simply all 25 jets (10 from year 1 + 15 from year 2) each training for the full two years, giving 25 × 5 × 2 = 250 pilots?

## Turn 14 - User Simulator

No, that is not correct. The 15 jets produced in year 2 are not available to train in year 1. Therefore, the 10 jets from year 1 can train in both year 1 and year 2, but the 15 jets from year 2 can only train in year 2.

## Turn 15 - Generic Agent

QUESTION: If all jets can be allocated to training and there is no confirmed minimum combat requirement, does that mean the maximum total pilots trained by the end of year 2 is (10 jets training in year 1 + 10 jets training in year 2 + 15 jets training in year 2) × 5 pilots per jet per year = 175 pilots?

## Turn 15 - User Simulator

Yes, that is correct.

## Turn 16 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Production:** 10 jets produced in year 1, 15 jets produced in year 2.
- **Training capacity:** Each jet allocated to training produces at most 5 trained pilots per year.
- **Jet availability:** Jets produced in year 1 are available for training in both year 1 and year 2. Jets produced in year 2 are available for training only in year 2.
- **Jet persistence:** Jets are not consumed; they remain available across years.
- **Allocation decision:** We choose how many jets to allocate to training each year to maximize total pilots trained.
- **Other uses:** Jets can also be used for combat deployment, but no minimum combat requirement or other constraint on training allocation has been confirmed.
- **Objective:** Maximize the total number of trained pilots produced over the two years combined.
- **Result:** With no binding constraint limiting training allocation, all available jets are allocated to training each year:
  - Year 1: 10 jets × 5 pilots = 50 pilots
  - Year 2: (10 + 15) jets × 5 pilots = 125 pilots
  - **Total: 175 trained pilots by the end of year 2.**