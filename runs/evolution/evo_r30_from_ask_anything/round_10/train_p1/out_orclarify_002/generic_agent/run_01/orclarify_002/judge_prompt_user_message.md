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

QUESTION: What is the number of trained pilots produced per fighter jet allocated to training in each year?

## Turn 1 - User Simulator

Each fighter jet allocated to training produces 5 trained pilots per year.

## Turn 2 - Generic Agent

QUESTION: Is the number of fighter jets allocated to training in each year a decision variable that you want to choose to maximize the total number of trained pilots, or is it a fixed quantity that is already determined?

## Turn 2 - User Simulator

The number of fighter jets allocated to training in each year is a decision variable that I want to choose to maximize the total number of trained pilots.

## Turn 3 - Generic Agent

QUESTION: Are there any limits on the number of fighter jets that can be allocated to training in each year, such as a maximum number of jets available for training or a minimum number of jets that must be reserved for other purposes?

## Turn 3 - User Simulator

The only limit is that the number of jets allocated to training in a given year cannot exceed the total fighter jets produced that year. There is no minimum number of jets that must be reserved for other purposes.

## Turn 4 - Generic Agent

QUESTION: Do the fighter jets allocated to training in year 1 remain available for training in year 2, or are they consumed or retired after year 1?

## Turn 4 - User Simulator

The fighter jets allocated to training in year 1 remain available for training in year 2.

## Turn 5 - Generic Agent

QUESTION: Do the fighter jets allocated to training in year 1 produce trained pilots in both year 1 and year 2, or do they only produce pilots in the year they are first allocated to training?

## Turn 5 - User Simulator

The fighter jets allocated to training in year 1 produce trained pilots in both year 1 and year 2.

## Turn 6 - Generic Agent

QUESTION: Do the fighter jets allocated to training in year 2 also produce trained pilots in year 2, or do they only start producing pilots in year 3?

## Turn 6 - User Simulator

The fighter jets allocated to training in year 2 produce trained pilots in year 2.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements on the allocation of fighter jets to training that I should be aware of, such as a maximum total number of jets that can be in training at any time or a requirement that a certain number of jets must be available for operational use?

## Turn 7 - User Simulator

No, there are no other constraints or requirements on the allocation of fighter jets to training beyond what has already been discussed.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2. **Decision Variables:**
   - $x_1$: Number of fighter jets allocated to training in year 1.
   - $x_2$: Number of fighter jets allocated to training in year 2.
3. **Variable Domain:** $x_1$ and $x_2$ are non-negative integers (since you cannot allocate a fraction of a jet).
4. **Constraints:**
   - $x_1 \le 10$ (Jets allocated to training in year 1 cannot exceed year 1 production).
   - $x_2 \le 15$ (Jets allocated to training in year 2 cannot exceed year 2 production).
   - No other constraints (no minimum operational reserve, no capacity limit on total training jets).
5. **Quantity Interpretation:**
   - Each jet allocated to training produces 5 trained pilots per year.
   - Jets allocated in year 1 produce pilots in both year 1 and year 2.
   - Jets allocated in year 2 produce pilots in year 2.
6. **Accounting and Flow:**
   - Jets allocated in year 1 remain available and continue to produce pilots in year 2.
   - Jets allocated in year 2 are added to the training fleet for year 2.
7. **Objective Function Formulation:**
   - Pilots from year 1 allocation: $5 \times x_1$ (in year 1) + $5 \times x_1$ (in year 2) = $10 x_1$.
   - Pilots from year 2 allocation: $5 \times x_2$ (in year 2).
   - Total pilots by end of year 2: $10 x_1 + 5 x_2$.

**Assumptions:**
- None. All critical facts were confirmed by the user.