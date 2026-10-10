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

QUESTION: Are the 10 and 15 fighter jets produced in years 1 and 2 available for pilot training in the same year they are produced, or do they become available for training only in the following year?

## Turn 2 - User Simulator

The 10 and 15 fighter jets produced in years 1 and 2 are available for pilot training in the same year they are produced.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum limit on the number of fighter jets that can be allocated to pilot training in any given year, or can all jets produced in that year be used for training?

## Turn 3 - User Simulator

There is no maximum limit on the number of fighter jets that can be allocated to pilot training in any given year; all jets produced in that year can be used for training.

## Turn 4 - Generic Agent

QUESTION: Do the fighter jets used for training in year 1 remain available for training in year 2, or are they consumed or retired after one year of training use?

## Turn 4 - User Simulator

The fighter jets used for training in year 1 remain available for training in year 2.

## Turn 5 - Generic Agent

QUESTION: Are there any other requirements or constraints on the allocation of fighter jets to pilot training, such as a minimum number of jets that must be reserved for other purposes like combat or maintenance?

## Turn 5 - User Simulator

There are no other requirements or constraints on the allocation of fighter jets to pilot training, such as a minimum number of jets that must be reserved for other purposes like combat or maintenance.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2. **Production:**
   - Year 1: 10 fighter jets produced.
   - Year 2: 15 fighter jets produced.
3. **Training Capacity:**
   - Each fighter jet allocated to training produces 5 pilots per year.
4. **Availability:**
   - Jets are available for training in the same year they are produced.
   - Jets used for training in Year 1 remain available for training in Year 2 (they are not consumed or retired).
5. **Constraints:**
   - No maximum limit on the number of jets allocated to training.
   - No minimum number of jets reserved for other purposes.
   - All produced jets can be allocated to training.

**Calculation:**

- **Year 1:**
  - Jets available for training: 10 (produced in Year 1).
  - Pilots trained in Year 1: $10 \text{ jets} \times 5 \text{ pilots/jet} = 50 \text{ pilots}$.

- **Year 2:**
  - Jets available for training: 10 (from Year 1) + 15 (produced in Year 2) = 25 jets.
  - Pilots trained in Year 2: $25 \text{ jets} \times 5 \text{ pilots/jet} = 125 \text{ pilots}$.

- **Total Trained Pilots by End of Year 2:**
  - $50 \text{ (Year 1)} + 125 \text{ (Year 2)} = 175 \text{ pilots}$.

**Final Answer:**
The total number of trained pilots available by the end of year 2 is **175**.