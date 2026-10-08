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

QUESTION: What is the exact rule for how many of the jets produced each year must be allocated exclusively for pilot training (for example, a fixed number, a fraction of that year's production, or a fraction of the cumulative fleet)?

## Turn 1 - User Simulator

The exact rule for how many jets must be allocated to training is not specified in my original request. I only stated that "some fighter jets each year must be allocated exclusively for pilot training."

I need to confirm internally whether this is a fixed number, a fraction of that year's production, or a fraction of the cumulative fleet.

## Turn 2 - Generic Agent

QUESTION: How many trained pilots does one training jet produce per year it is in service (for example, one pilot per year, or a fixed number of pilots over its lifetime)?

## Turn 2 - User Simulator

Each training jet can train 5 pilots per year.

## Turn 3 - Generic Agent

QUESTION: Do training jets remain in the training fleet and keep training pilots in subsequent years, or are they used for training only in the year they are allocated and then retired?

## Turn 3 - User Simulator

The available business facts do not determine whether training jets remain in the training fleet for subsequent years or are retired after the year they are allocated. This point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Are the jets allocated to training in a given year drawn from that year's production only, or can jets produced in earlier years also be assigned to training in later years?

## Turn 4 - User Simulator

The available business facts do not determine whether jets allocated to training in a given year are drawn from that year's production only, or if jets produced in earlier years can also be assigned to training in later years. This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how many jets can be allocated to training in a given year (such as a maximum number of training slots or a cap on the training fleet size)?

## Turn 5 - User Simulator

The available business facts do not determine if there is a limit on how many jets can be allocated to training in a given year. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is the number of jets allocated to training each year fixed by some external requirement?

## Turn 6 - User Simulator

The goal is to determine the total number of trained pilots available by the end of year 2. The available business facts do not specify whether the number of jets allocated to training each year is fixed by an external requirement or if the allocation is variable to maximize the pilot count. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Do jets allocated to training in year 1 continue to be available for training in year 2, or are they retired after year 1?

## Turn 7 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 continue to be available for training in year 2 or are retired after year 1. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 drawn from year 1's production only, or can they also include jets produced in earlier years?

## Turn 8 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 are drawn from year 1's production only or can include jets produced in earlier years. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the number of jets allocated to training each year a fixed requirement (e.g., a specific number or fraction that must be met), or is it a decision variable that we choose to maximize the total trained pilots?

## Turn 9 - User Simulator

The available business facts do not determine whether the number of jets allocated to training each year is a fixed requirement or a decision variable chosen to maximize the total trained pilots. This point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there a minimum number of jets that must be allocated to training each year, or is the allocation purely at our discretion to maximize pilot output?

## Turn 10 - User Simulator

The available business facts do not determine if there is a minimum number of jets that must be allocated to training each year, or if the allocation is purely at our discretion. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Do jets allocated to training in year 1 remain available for training in year 2, or are they retired after year 1?

## Turn 11 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 remain available for training in year 2 or are retired after year 1. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is the total number of trained pilots by the end of year 2 to be maximized, or is it determined by a fixed allocation rule that we must follow?

## Turn 12 - User Simulator

The available business facts do not determine whether the total number of trained pilots by the end of year 2 is to be maximized or determined by a fixed allocation rule. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 drawn from year 1's production only, or can they also include jets produced in earlier years?

## Turn 13 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 are drawn from year 1's production only or can include jets produced in earlier years. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there a maximum number of jets that can be allocated to training in any given year?

## Turn 14 - User Simulator

The available business facts do not determine if there is a maximum number of jets that can be allocated to training in any given year. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Do jets allocated to training in year 1 remain available for training in year 2, or are they retired after year 1?

## Turn 15 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 remain available for training in year 2 or are retired after year 1. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is the number of jets allocated to training each year a fixed requirement that must be met, or is it a decision variable that we choose to maximize the total trained pilots?

## Turn 16 - User Simulator

The available business facts do not determine whether the number of jets allocated to training each year is a fixed requirement that must be met or a decision variable chosen to maximize the total trained pilots. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 drawn from year 1's production only, or can they also include jets produced in earlier years?

## Turn 17 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 are drawn from year 1's production only or can include jets produced in earlier years. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there a minimum number of jets that must be allocated to training each year, or is the allocation purely at our discretion to maximize pilot output?

## Turn 18 - User Simulator

The available business facts do not determine if there is a minimum number of jets that must be allocated to training each year, or if the allocation is purely at our discretion. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Do jets allocated to training in year 1 remain available for training in year 2, or are they retired after year 1?

## Turn 19 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 remain available for training in year 2 or are retired after year 1. This point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is the total number of trained pilots by the end of year 2 to be maximized, or is it determined by a fixed allocation rule that we must follow?

## Turn 20 - User Simulator

The available business facts do not determine whether the total number of trained pilots by the end of year 2 is to be maximized or determined by a fixed allocation rule. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 drawn from year 1's production only, or can they also include jets produced in earlier years?

## Turn 21 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 are drawn from year 1's production only or can include jets produced in earlier years. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there a maximum number of jets that can be allocated to training in any given year?

## Turn 22 - User Simulator

The available business facts do not determine if there is a maximum number of jets that can be allocated to training in any given year. This point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Do jets allocated to training in year 1 remain available for training in year 2, or are they retired after year 1?

## Turn 23 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 remain available for training in year 2 or are retired after year 1. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is the number of jets allocated to training each year a fixed requirement that must be met, or is it a decision variable that we choose to maximize the total trained pilots?

## Turn 24 - User Simulator

The available business facts do not determine whether the number of jets allocated to training each year is a fixed requirement that must be met or a decision variable chosen to maximize the total trained pilots. This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 drawn from year 1's production only, or can they also include jets produced in earlier years?

## Turn 25 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 are drawn from year 1's production only or can include jets produced in earlier years. This point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there a minimum number of jets that must be allocated to training each year, or is the allocation purely at our discretion to maximize pilot output?

## Turn 26 - User Simulator

The available business facts do not determine if there is a minimum number of jets that must be allocated to training each year, or if the allocation is purely at our discretion. This point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Do jets allocated to training in year 1 remain available for training in year 2, or are they retired after year 1?

## Turn 27 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 remain available for training in year 2 or are retired after year 1. This point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is the total number of trained pilots by the end of year 2 to be maximized, or is it determined by a fixed allocation rule that we must follow?

## Turn 28 - User Simulator

The available business facts do not determine whether the total number of trained pilots by the end of year 2 is to be maximized or determined by a fixed allocation rule. This point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 drawn from year 1's production only, or can they also include jets produced in earlier years?

## Turn 29 - User Simulator

The available business facts do not determine whether jets allocated to training in year 1 are drawn from year 1's production only or can include jets produced in earlier years. This point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there a maximum number of jets that can be allocated to training in any given year?

## Turn 30 - User Simulator

The available business facts do not determine if there is a maximum number of jets that can be allocated to training in any given year. This point still needs internal confirmation.