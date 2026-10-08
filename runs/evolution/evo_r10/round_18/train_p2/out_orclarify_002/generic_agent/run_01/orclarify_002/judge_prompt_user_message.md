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

QUESTION: How many trained pilots does each fighter jet produce per year when it is allocated to pilot training?

## Turn 1 - User Simulator

Each fighter jet allocated to pilot training produces 5 trained pilots per year.

## Turn 2 - Generic Agent

QUESTION: How many fighter jets must be allocated to pilot training in each year — is it a fixed number, a fraction of that year's production, or a decision we choose to maximize the total trained pilots by the end of year 2?

## Turn 2 - User Simulator

It is a decision we choose to maximize the total trained pilots by the end of year 2.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a given year can be allocated to training — for example, must the jets used for training in a year come only from that year's production, or can jets produced in earlier years also be used for training in later years?

## Turn 3 - User Simulator

The jets used for training in a year must come only from that year's production.

## Turn 4 - Generic Agent

QUESTION: Are there any other uses or requirements for the jets besides pilot training — for example, must some jets be kept for combat or other purposes, or can all of a year's production be allocated to training if that maximizes trained pilots?

## Turn 4 - User Simulator

There are no other uses or requirements for the jets besides pilot training. All of a year's production can be allocated to training if that maximizes trained pilots.

## Turn 5 - Generic Agent

QUESTION: When a jet is allocated to training in a year, does it produce 5 pilots in that year only, or does it continue producing pilots in subsequent years as well?

## Turn 5 - User Simulator

A jet allocated to training in a year produces 5 pilots in that year only.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 2 years (year 1 and year 2).
- **Production:** a1 = 10 jets in year 1, a2 = 15 jets in year 2.
- **Decision:** In each year, choose how many of that year's newly produced jets to allocate to pilot training (the rest are simply unused, with no penalty or other requirement).
- **Training output:** Each jet allocated to training in a given year produces exactly 5 trained pilots in that year only (no carry-over production).
- **Constraint:** Jets used for training in a year must come from that year's production only (no reuse of earlier-year jets).
- **Objective:** Maximize the total number of trained pilots available by the end of year 2.

Since all jets can be allocated to training with no other competing use, the optimal allocation is to assign every jet to training in both years:
- Year 1: 10 jets × 5 pilots = 50 pilots
- Year 2: 15 jets × 5 pilots = 75 pilots
- **Total trained pilots by end of year 2: 125**