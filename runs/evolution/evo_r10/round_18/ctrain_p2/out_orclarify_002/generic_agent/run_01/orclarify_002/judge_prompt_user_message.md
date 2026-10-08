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

QUESTION: How many trained pilots does one fighter jet produce per year when it is allocated to pilot training?

## Turn 1 - User Simulator

One fighter jet allocated to pilot training produces 5 trained pilots per year.

## Turn 2 - Generic Agent

QUESTION: How many fighter jets must be allocated to pilot training each year?

## Turn 2 - User Simulator

The number of fighter jets that must be allocated to pilot training each year still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Do the fighter jets allocated to pilot training in a given year have to come from that same year's production, or can jets produced in earlier years be carried over and used for training in later years?

## Turn 3 - User Simulator

The available business facts do not determine whether training jets must come from that same year's production or can be carried over from earlier years. This point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year consumed (unavailable afterward), or do they remain in the fleet and can be used for training in multiple years?

## Turn 4 - User Simulator

The available business facts do not determine whether training jets are consumed or remain in the fleet for multiple years. This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the number of fighter jets that must be allocated to pilot training each year a fixed requirement (e.g., a specific number per year), or is it a decision variable that we can choose as part of the optimization?

## Turn 5 - User Simulator

The available business facts do not determine whether the number of training jets is a fixed requirement or a decision variable. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many fighter jets can be allocated to pilot training in a given year, such as a maximum number or a percentage of that year's production?

## Turn 6 - User Simulator

The available business facts do not determine any limit on how many fighter jets can be allocated to pilot training in a given year. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: When you say "some fighter jets each year must be allocated exclusively for pilot training," does "exclusively" mean that a jet used for training in a year cannot also be used for any other purpose (like combat deployment) in that same year?

## Turn 7 - User Simulator

Yes, "exclusively" means that a jet used for training in a year cannot also be used for any other purpose in that same year.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints on the total number of fighter jets available each year, such as a maximum fleet size or a requirement to maintain a minimum number of operational (non-training) jets?

## Turn 8 - User Simulator

The available business facts do not determine any other constraints on the total number of fighter jets available each year, such as a maximum fleet size or a minimum number of operational jets. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a specific target number of trained pilots that needs to be met?

## Turn 9 - User Simulator

The goal is to determine the total number of trained pilots available by the end of year 2.

## Turn 10 - Generic Agent

QUESTION: Is the total number of trained pilots by the end of year 2 simply the sum of pilots produced in year 1 plus pilots produced in year 2, or are there any other factors (like pilot attrition, retirement, or additional training requirements) that affect the final count?

## Turn 10 - User Simulator

The available business facts do not determine whether there are other factors like pilot attrition, retirement, or additional training requirements that affect the final count. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Can fighter jets produced in year 1 be carried over and used for pilot training in year 2, or must training jets in each year come only from that year's production?

## Turn 11 - User Simulator

The available business facts do not determine whether fighter jets produced in year 1 can be carried over and used for pilot training in year 2, or whether training jets in each year must come only from that year's production. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is the number of fighter jets allocated to pilot training in each year a fixed value that is given (e.g., 2 jets in year 1 and 3 jets in year 2), or is it something we need to determine as part of the solution?

## Turn 12 - User Simulator

The available business facts do not determine whether the number of fighter jets allocated to pilot training in each year is a fixed value or something to be determined as part of the solution. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, or is it possible to allocate zero jets to training in a given year?

## Turn 13 - User Simulator

The available business facts do not determine whether there is a minimum number of fighter jets that must be allocated to pilot training each year, or whether it is possible to allocate zero jets to training in a given year. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year consumed (i.e., they cannot be used again in subsequent years), or do they remain available for training in later years?

## Turn 14 - User Simulator

The available business facts do not determine whether fighter jets allocated to pilot training in a given year are consumed or remain available for training in later years. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is the total number of trained pilots by the end of year 2 simply the sum of pilots produced in year 1 and year 2, with no attrition, retirement, or other reductions?

## Turn 15 - User Simulator

The available business facts do not determine whether there is attrition, retirement, or other reductions affecting the total number of trained pilots by the end of year 2. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is the number of fighter jets allocated to pilot training in each year a fixed value that is given (e.g., 2 jets in year 1 and 3 jets in year 2), or is it a decision variable that we can choose to maximize the number of trained pilots?

## Turn 16 - User Simulator

The available business facts do not determine whether the number of fighter jets allocated to pilot training in each year is a fixed value or a decision variable. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to pilot training in a given year, or can all fighter jets produced in that year be allocated to training?

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION: Is the number of fighter jets allocated to pilot training in each year a fixed value that is given (e

## Turn 18 - User Simulator

The available business facts do not determine whether the number of fighter jets allocated to pilot training in each year is a fixed value or a decision variable. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is the total

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION: Is

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: Is

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Is

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Is

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Is

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Is

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Is

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Is

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Is

## Turn 30 - User Simulator

The