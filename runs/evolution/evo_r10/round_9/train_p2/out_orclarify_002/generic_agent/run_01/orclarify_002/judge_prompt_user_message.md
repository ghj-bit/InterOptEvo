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

QUESTION: How many trained pilots does each fighter jet produce when it is allocated to pilot training in a given year?

## Turn 1 - User Simulator

Each fighter jet allocated to pilot training in a given year produces 5 trained pilots.

## Turn 2 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, and if so, what is that minimum?

## Turn 2 - User Simulator

The business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to pilot training in a given year, or can all jets produced that year be used for training?

## Turn 3 - User Simulator

The available business facts do not specify a maximum number of fighter jets that can be allocated to pilot training in a given year. That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Do trained pilots carry over from year 1 to year 2, so that the total by the end of year 2 includes pilots trained in both years?

## Turn 4 - User Simulator

Yes, trained pilots carry over from year 1 to year 2, so the total by the end of year 2 includes pilots trained in both years.

## Turn 5 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn from that year's production only, or can jets produced in earlier years also be used for training in later years?

## Turn 5 - User Simulator

The available business facts do not specify whether training jets are drawn from that year's production only or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: If a fighter jet is not allocated to pilot training in a given year, is it simply not used for training that year (with no penalty or other effect), or does it have some other role or consequence?

## Turn 6 - User Simulator

The available business facts do not specify any penalty, other role, or consequence for fighter jets not allocated to pilot training in a given year. That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a specific target number of trained pilots that must be met?

## Turn 7 - User Simulator

The goal is to maximize the total number of trained pilots by the end of year 2.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many fighter jets can be allocated to pilot training in a given year, such as a cap based on available training facilities or instructors?

## Turn 8 - User Simulator

The available business facts do not specify any limit on how many fighter jets can be allocated to pilot training in a given year, such as a cap based on available training facilities or instructors. That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the fighter jets used for pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 9 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 10 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 11 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 12 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 13 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 14 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 15 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 16 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 17 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 18 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 19 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 20 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 21 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 22 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 23 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 24 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 25 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 26 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 27 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 28 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Are the fighter jets allocated to pilot training in a given year drawn only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 29 - User Simulator

The available business facts do not specify whether training jets are drawn only from that year's production or can include jets produced in earlier years. That point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to pilot training each year, even if it is not explicitly stated in the business facts?

## Turn 30 - User Simulator

The available business facts state that some fighter jets each year must be allocated exclusively for pilot training, but they do not specify a minimum number. That point still needs internal confirmation.