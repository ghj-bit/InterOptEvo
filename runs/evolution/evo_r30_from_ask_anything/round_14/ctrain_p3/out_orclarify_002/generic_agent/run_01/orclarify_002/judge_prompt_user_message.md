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

QUESTION: Are the annual fighter jet production figures of 10 in year 1 and 15 in year 2 the total jets produced each year, from which some must be set aside for training, or are they the number of jets available for operational use after training jets have already been removed?

## Turn 1 - User Simulator

They are the total jets produced each year. From those totals, some must be set aside for training.

## Turn 2 - Generic Agent

QUESTION: How many fighter jets must be allocated exclusively for pilot training in each year, and is that number a fixed count per year, a fixed fraction of that year's production, or a variable we are free to choose?

## Turn 2 - User Simulator

The number of jets allocated for training is a variable we are free to choose each year.

## Turn 3 - Generic Agent

QUESTION: How many trained pilots does one training jet produce per year, and is that output a fixed number per training jet or does it depend on other factors?

## Turn 3 - User Simulator

One training jet produces 5 trained pilots per year. That output is a fixed number per training jet.

## Turn 4 - Generic Agent

QUESTION: Are the trained pilots produced in a given year available immediately in that same year, or do they only become available in the following year?

## Turn 4 - User Simulator

The trained pilots produced in a given year are available immediately in that same year.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how many of the total jets produced in a given year can be allocated to training, or can we allocate all of that year's production to training if we choose?

## Turn 5 - User Simulator

There is no limit stated; we can allocate all of that year's production to training if we choose.

## Turn 6 - Generic Agent

QUESTION: Are the training jets allocated in a given year reusable for training in subsequent years, or are they consumed (retired) after one year of training?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the purpose of this model, should we assume that a training jet allocated in year 1 can also be used for training in year 2, or should we assume each training jet is used for training in only one year and then retired?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the reusability of training jets across years is unconfirmed, should we proceed by assuming each training jet is used for training in only one year and then retired, so that the number of training jets in each year is chosen independently from that year's production?

## Turn 8 - User Simulator

Yes, proceed by assuming each training jet is used for training in only one year and then retired, so that the number of training jets in each year is chosen independently from that year's production.

## Turn 9 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots available by the end of year 2, or is there a specific target number of pilots we need to meet?

## Turn 9 - User Simulator

The goal is to maximize the total number of trained pilots available by the end of year 2.

## Turn 10 - Generic Agent

QUESTION: Are the trained pilots produced in year 1 still available and counted in the total at the end of year 2, or do they leave the system after year 1 so only year 2's pilots count?

## Turn 10 - User Simulator

The trained pilots produced in year 1 are still available and counted in the total at the end of year 2.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or requirements on the allocation of jets to training or to operational use that the brief does not mention, such as a minimum number of jets that must remain for operational use each year?

## Turn 11 - User Simulator

No, there are no other constraints or requirements on the allocation of jets to training or to operational use beyond what has been discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize the total number of trained pilots available by the end of year 2. (Confirmed)
- Decision variables: The number of jets allocated to training in year 1 (t1) and in year 2 (t2). (Confirmed)
- Variable domain: t1 and t2 are non-negative quantities chosen from each year's production. (Confirmed)
- Production: Total jets produced are 10 in year 1 and 15 in year 2. These are the totals from which training jets are drawn. (Confirmed)
- Training output: Each training jet produces 5 trained pilots in the year it is used. (Confirmed)
- Pilot availability: Pilots produced in a given year are available immediately in that year. (Confirmed)
- Pilot accumulation: Pilots produced in year 1 remain available and are counted in the total at the end of year 2. (Confirmed)
- Training jet lifecycle: Each training jet is used for training in only one year and then retired; the training allocation in each year is chosen independently from that year's production. (Assumed, per user instruction to proceed this way pending internal confirmation)
- Allocation limits: There is no stated limit on the fraction of a year's production that can be allocated to training; all of a year's production could be allocated to training. (Confirmed)
- Other constraints: No additional constraints on operational use or other requirements. (Confirmed)

Open assumptions:
- Training jets are single-year use and retired after one year of training (not reusable across years). This was not internally confirmed and is carried as an explicit assumption.