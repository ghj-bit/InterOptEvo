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

QUESTION: In your setup, is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training that year (i.e., one pilot trained per training jet), or is there a different conversion rate between training jets and pilots?

## Turn 1 - User Simulator

There is a different conversion rate. Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: When you say each training jet can train 5 pilots per year, does that mean a jet allocated to training in year 1 produces 5 pilots in year 1 AND can also produce 5 pilots in year 2 (i.e., the same jet trains pilots in both years), or does a jet allocated to training in year 1 only produce pilots in year 1 and a separate allocation is needed for year 2?

## Turn 2 - User Simulator

A jet allocated to training in year 1 only produces pilots in year 1. A separate allocation is needed for year 2.

## Turn 3 - Generic Agent

QUESTION: Are there any constraints on how many of the jets produced in a given year must be allocated to training versus other uses (e.g., a minimum or maximum number of jets that must go to training, or a requirement that some jets be reserved for operational/combat use)?

## Turn 3 - User Simulator

There are no specific minimum or maximum constraints on the number of jets allocated to training. The only requirement is that some fighter jets each year must be allocated exclusively for pilot training.

## Turn 4 - Generic Agent

QUESTION: You mentioned that "some fighter jets each year must be allocated exclusively for pilot training" — does "some" mean at least 1 jet per year must go to training, or is there a specific minimum number of jets that must be allocated to training each year?

## Turn 4 - User Simulator

"Some" means at least 1 jet per year must be allocated to training.

## Turn 5 - Generic Agent

QUESTION: Are the jets produced in year 1 available for allocation in year 2 as well (i.e., can year 1 jets be used for training in year 2), or are jets only available for allocation in the year they are produced?

## Turn 5 - User Simulator

Jets are only available for allocation in the year they are produced.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on the number of pilots that can be trained in a given year (e.g., a cap on total pilots per year), or is the only limit the number of training jets allocated that year multiplied by 5?

## Turn 6 - User Simulator

The only limit is the number of training jets allocated that year multiplied by 5.

## Turn 7 - Generic Agent

QUESTION: When you say "determine the total number of trained pilots available by the end of year 2," do you want the maximum possible number of trained pilots (i.e., an optimization where we maximize pilot output), or is there a specific target number of pilots to achieve?

## Turn 7 - User Simulator

I want the maximum possible number of trained pilots.

## Turn 8 - Generic Agent

QUESTION: Are there any other uses for the jets besides training (e.g., operational/combat deployment), and if so, is there any requirement that a certain number of jets must be allocated to those other uses each year?

## Turn 8 - User Simulator

There are no requirements that a certain number of jets must be allocated to other uses each year.

## Turn 9 - Generic Agent

QUESTION: Just to confirm my understanding of the full picture: in each year, you produce a1=10 (year 1) or a2=15 (year 2) jets, you allocate some number of those jets to training (at least 1), each training jet produces 5 pilots that year, and the remaining jets are simply not used for training. The objective is to maximize total pilots over the two years. Is that correct, or is there any additional constraint or nuance I'm missing?

## Turn 9 - User Simulator

Yes, that is correct.

## Turn 10 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the total number of trained pilots available by the end of year 2.

**Parameters:**
- Year 1 production: a1 = 10 jets
- Year 2 production: a2 = 15 jets
- Conversion rate: 1 training jet → 5 pilots per year
- Minimum training jets per year: 1

**Decision variables:**
- x1 = number of jets allocated to training in year 1
- x2 = number of jets allocated to training in year 2

**Constraints:**
- x1 ≤ 10 (cannot allocate more jets than produced in year 1)
- x2 ≤ 15 (cannot allocate more jets than produced in year 2)
- x1 ≥ 1 (at least 1 jet for training in year 1)
- x2 ≥ 1 (at least 1 jet for training in year 2)
- x1, x2 are non-negative integers

**Objective function:**
Maximize 5·x1 + 5·x2

**Key clarifications confirmed:**
- Jets are only available in the year they are produced (no carryover).
- A training jet produces pilots only in the year it is allocated.
- No upper cap on pilots beyond the training-jet × 5 rule.
- No minimum allocation to non-training uses.
- The goal is to maximize total pilots (not meet a target).