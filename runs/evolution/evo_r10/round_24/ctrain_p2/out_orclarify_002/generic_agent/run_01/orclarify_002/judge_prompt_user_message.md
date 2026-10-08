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

QUESTION: In this setup, is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training that year (i.e., one pilot trained per training jet), or is there a different conversion rate between training jets and trained pilots?

## Turn 1 - User Simulator

There is a different conversion rate. Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: When a fighter jet is allocated to pilot training in a given year, is it used for training only in that single year, or does it remain in the training pool and continue training pilots in subsequent years as well?

## Turn 2 - User Simulator

A fighter jet allocated to training in a given year is used for training only in that single year.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a given year can be allocated to training (for example, a maximum fraction or number), or can any number of that year's production be assigned to training as long as the total does not exceed that year's production?

## Turn 3 - User Simulator

There is no specific limit mentioned. Any number of that year's production can be assigned to training, as long as the total does not exceed that year's production.

## Turn 4 - Generic Agent

QUESTION: Are the jets allocated to training in a given year drawn only from that same year's production, or can jets produced in an earlier year (and not used for training then) be carried over and used for training in a later year?

## Turn 4 - User Simulator

The available business facts do not determine whether jets produced in an earlier year can be carried over and used for training in a later year. This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Since the carry-over point is still open, let me confirm the objective: is the goal to maximize the total number of trained pilots available by the end of year 2, or is there a fixed requirement (such as a minimum number of pilots) that the setup must meet?

## Turn 5 - User Simulator

The goal is to maximize the total number of trained pilots available by the end of year 2.

## Turn 6 - Generic Agent

QUESTION: When a jet is not allocated to training in a given year, what happens to it — is it simply unused/idle for that year, or does it serve some other purpose (such as operational deployment) that would count as a separate use of the jet?

## Turn 6 - User Simulator

The available business facts do not determine what happens to jets not allocated to training. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the carry-over question is still open, let me ask it in a simpler form: can a jet produced in year 1 be held and then used for training in year 2, or must each year's training jets come only from that same year's production?

## Turn 7 - User Simulator

The available business facts do not determine whether a jet produced in year 1 can be held and used for training in year 2. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the carry-over point remains open, let me confirm the horizon: does the setup operate for exactly two years (year 1 and year 2), with no production or training occurring before year 1 or after year 2?

## Turn 8 - User Simulator

Yes, the setup operates for exactly two years (year 1 and year 2), with no production or training occurring before year 1 or after year 2.

## Turn 9 - Generic Agent

QUESTION: Since the carry-over point remains open, let me ask it one final time in the most direct form: is a jet produced in year 1 available to be used for training in year 2, or is each year's training allocation restricted to only that year's newly produced jets?

## Turn 9 - User Simulator

The available business facts do not determine whether a jet produced in year 1 is available to be used for training in year 2. This point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Since the carry-over point remains open, let me confirm one last detail: are the production figures a1 = 10 (year 1) and a2 = 15 (year 2) fixed and given, or are they themselves decision variables that could be adjusted?

## Turn 10 - User Simulator

The production figures a1 = 10 (year 1) and a2 = 15 (year 2) are fixed and given.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the total number of trained pilots available by the end of year 2.

**Parameters:**
- Annual fighter jet production: a1 = 10 (year 1), a2 = 15 (year 2). These are fixed.
- Conversion rate: each training jet trains 5 pilots per year.
- Horizon: exactly two years (year 1 and year 2); no activity before or after.

**Decision variables:**
- t1 = number of jets allocated to training in year 1 (0 ≤ t1 ≤ 10)
- t2 = number of jets allocated to training in year 2 (0 ≤ t2 ≤ 15)

**Constraints:**
- t1 ≤ a1 = 10 (training jets in year 1 cannot exceed year 1 production)
- t2 ≤ a2 = 15 (training jets in year 2 cannot exceed year 2 production)
- No explicit limit on the fraction of production that can go to training.

**Objective function:**
Maximize 5·t1 + 5·t2

**Open items (parked, not resolved by the client):**
- Whether jets produced in year 1 can be carried over and used for training in year 2 (the client indicated this is undetermined). I will model the conservative reading: each year's training allocation is drawn only from that year's production. If carry-over is later confirmed, the constraint t2 ≤ a2 would be relaxed to t2 ≤ a2 + (a1 − t1).
- What happens to jets not allocated to training (idle vs. other use). This does not affect the pilot count, so it does not change the model.

**Solution under the conservative (no carry-over) reading:**
Since the objective is to maximize 5·t1 + 5·t2 with no other constraints binding, the optimum is t1 = 10, t2 = 15, giving a maximum of 5·10 + 5·15 = 125 trained pilots by the end of year 2.