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

QUESTION: Is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training in that same year, or does each training jet produce a different number of pilots (for example, multiple pilots per jet or a fixed pilot output per jet)?

## Turn 1 - User Simulator

Each training jet produces a fixed number of pilots per year. Specifically, each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Are the training jets allocated in year 1 still available to train pilots in year 2, or must new training jets be allocated from the year 2 production to continue training?

## Turn 2 - User Simulator

The training jets allocated in year 1 are still available to train pilots in year 2.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum limit on the number of fighter jets that can be allocated to training in any given year, or can all of that year's production be allocated to training if desired?

## Turn 3 - User Simulator

There is no maximum limit on the number of fighter jets that can be allocated to training in any given year. All of that year's production can be allocated to training if desired.

## Turn 4 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to training in each year, or can zero jets be allocated to training in a given year?

## Turn 4 - User Simulator

There is no minimum number of fighter jets that must be allocated to training in each year. Zero jets can be allocated to training in a given year.

## Turn 5 - Generic Agent

QUESTION: Are there any other requirements or constraints on the allocation of fighter jets to training that I should know about, such as a requirement to reserve some jets for operational use or a limit on the total number of training jets that can be maintained over the two years?

## Turn 5 - User Simulator

No, there are no other requirements or constraints on the allocation of fighter jets to training.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2. **Decision Variables:**
   - $x_1$: Number of fighter jets allocated to training in year 1.
   - $x_2$: Number of fighter jets allocated to training in year 2.
3. **Variable Domain:**
   - $x_1$ and $x_2$ are non-negative integers (since you cannot allocate a fraction of a jet).
4. **Constraints:**
   - Year 1 production limit: $x_1 \le 10$
   - Year 2 production limit: $x_2 \le 15$
   - No minimum allocation required ($x_1 \ge 0, x_2 \ge 0$).
   - No other constraints (no operational reserve, no maintenance limit).
5. **Accounting and Flow:**
   - Training jets allocated in year 1 remain available for training in year 2.
   - Each training jet produces 5 pilots per year.
   - Total pilots from year 1 jets: $5 \times x_1$ (produced in year 1) + $5 \times x_1$ (produced in year 2) = $10 x_1$.
   - Total pilots from year 2 jets: $5 \times x_2$ (produced in year 2).
   - Total pilots by end of year 2: $10 x_1 + 5 x_2$.
6. **Solution:**
   - To maximize $10 x_1 + 5 x_2$ subject to $x_1 \le 10$ and $x_2 \le 15$:
   - Set $x_1 = 10$ and $x_2 = 15$.
   - Total pilots = $10(10) + 5(15) = 100 + 75 = 175$.

**Final Answer:** The maximum number of trained pilots available by the end of year 2 is **175**.