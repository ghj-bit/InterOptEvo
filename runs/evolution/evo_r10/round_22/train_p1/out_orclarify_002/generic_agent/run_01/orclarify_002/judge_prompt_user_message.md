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

QUESTION: In each year, is the number of jets allocated to pilot training a fixed fraction of that year's production, or is it a decision variable you can choose (subject to some constraint)?

## Turn 1 - User Simulator

It is a decision variable I can choose, subject to the constraint that some fighter jets each year must be allocated exclusively for pilot training.

## Turn 2 - Generic Agent

QUESTION: What is the exact constraint on the number of jets that must be allocated to training each year — is it a minimum (at least X), a maximum (at most X), or an exact number, and what is that number for year 1 and year 2?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: How many trained pilots does one training jet produce per year — is it a fixed number of pilots per training jet, and does a jet used for training in year 1 also produce pilots again in year 2, or is each training jet used for only one year?

## Turn 3 - User Simulator

Each training jet produces a fixed number of 5 pilots per year. A jet used for training in year 1 also produces pilots again in year 2.

## Turn 4 - Generic Agent

QUESTION: Are the training jets carried over from year 1 to year 2 (so the same jets can train in both years), or does each year's training allocation come only from that year's new production?

## Turn 4 - User Simulator

The training jets are carried over from year 1 to year 2, so the same jets can train in both years.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how many jets can be allocated to training in a given year — for example, a maximum number of training jets per year, or a maximum fraction of production that can go to training?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the total number of training jets that can be in the training fleet at the end of year 2 — for example, a maximum size of the training fleet, or a maximum total number of jets that can ever be allocated to training across both years?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are the jets allocated to training in year 1 removed from the production count (i.e., they come out of the 10 jets produced in year 1), or are training jets in addition to the production numbers?

## Turn 7 - User Simulator

The jets allocated to training in year 1 come out of the 10 jets produced in year 1.

## Turn 8 - Generic Agent

QUESTION: Do the training jets allocated in year 2 come out of the 15 jets produced in year 2, or can they also include jets that were produced in year 1 but not used for training?

## Turn 8 - User Simulator

The training jets allocated in year 2 come out of the 15 jets produced in year 2.

## Turn 9 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots by the end of year 2, or is there a specific target number of pilots you need to meet?

## Turn 9 - User Simulator

The objective is to maximize the total number of trained pilots by the end of year 2.

## Turn 10 - Generic Agent

QUESTION: Are there any other uses or constraints on the non-training jets produced each year — for example, a minimum number of jets that must be kept for operational/combat use each year, or a maximum total fleet size?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Can the number of training jets allocated in year 2 be greater than the number allocated in year 1, or is there a requirement that the training fleet size must be non-decreasing (or non-increasing) across years?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint that the number of training jets allocated in a given year must be an integer (whole number of jets), or can it be fractional?

## Turn 12 - User Simulator

The number of training jets allocated in a given year must be an integer.

## Turn 13 - Generic Agent

QUESTION: When you say "some fighter jets each year must be allocated exclusively for pilot training," does this mean there is a minimum number of jets that must go to training each year (e.g., at least 1), or is it simply that the decision variable must be non-negative (zero or more)?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Do the training jets that are carried over from year 1 to year 2 continue to produce 5 pilots per year in year 2 as well, meaning a jet allocated to training in year 1 produces 5 pilots in year 1 AND another 5 pilots in year 2 (10 total over two years)?

## Turn 14 - User Simulator

Yes, a jet allocated to training in year 1 produces 5 pilots in year 1 and another 5 pilots in year 2, for a total of 10 pilots over the two years.

## Turn 15 - Generic Agent

QUESTION: Do the training jets allocated in year 2 also produce pilots in year 2 only (5 pilots), or do they also carry over and produce pilots beyond year 2?

## Turn 15 - User Simulator

The training jets allocated in year 2 produce pilots in year 2 only (5 pilots).

## Turn 16 - Generic Agent

QUESTION: Is there any upper bound on the number of training jets that can be allocated in a given year — for example, can all 10 jets from year 1 be allocated to training, or is there a maximum fraction or number that can go to training?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Are there any other constraints or requirements I haven't asked about — for example, a minimum number of non-training (operational) jets that must be available each year, or a total budget or resource limit on the training program?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there a requirement that the number of training jets in year 2 must be at least as large as in year 1 (i.e., the training fleet cannot shrink), or can it be any non-negative integer up to the year 2 production?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Since several constraints are still pending internal confirmation, if I model the problem with only the confirmed facts (training jets are a non-negative integer decision variable, year 1 jets come from the 10 produced, year 2 jets come from the 15 produced, each training jet produces 5 pilots per year it is active, year 1 jets also produce in year 2, year 2 jets produce only in year 2, and the objective is to maximize total pilots by end of year 2), would that be acceptable as a baseline model that you can later tighten once the pending constraints are confirmed?

## Turn 19 - User Simulator

Yes, that would be acceptable as a baseline model.

## Turn 20 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the total number of trained pilots available by the end of year 2.

**Decision variables:**
- x1 = number of training jets allocated in year 1 (non-negative integer, drawn from the 10 jets produced in year 1)
- x2 = number of training jets allocated in year 2 (non-negative integer, drawn from the 15 jets produced in year 2)

**Parameters:**
- a1 = 10 (year 1 production)
- a2 = 15 (year 2 production)
- p = 5 (pilots produced per training jet per year)

**Pilot production:**
- Year 1: x1 jets each produce 5 pilots → 5·x1 pilots
- Year 2: x1 jets (carried over) each produce 5 pilots, plus x2 jets each produce 5 pilots → 5·x1 + 5·x2 pilots
- Total pilots by end of year 2: 5·x1 + 5·x1 + 5·x2 = 10·x1 + 5·x2

**Constraints (confirmed):**
- 0 ≤ x1 ≤ 10, x1 integer
- 0 ≤ x2 ≤ 15, x2 integer

**Pending (to be confirmed later, not included in baseline):**
- Minimum number of jets that must go to training each year
- Maximum number/fraction of jets that can go to training
- Any minimum operational (non-training) fleet requirement
- Any monotonicity requirement on training fleet size
- Any total fleet size or budget cap

**Baseline solution:** With no upper binding constraints beyond production, the optimum is x1 = 10, x2 = 15, yielding 10·10 + 5·15 = 175 trained pilots by the end of year 2.