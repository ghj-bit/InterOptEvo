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

QUESTION: Is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training in that same year, or does each training jet produce a different number of pilots (for example, multiple pilots per jet or a fixed pilot count per jet)?

## Turn 1 - User Simulator

Each training jet produces a fixed number of pilots. Specifically, each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Are the 10 and 15 fighter jets produced in years 1 and 2 available for pilot training in those same years, or is there a delay before newly produced jets can be used for training?

## Turn 2 - User Simulator

The 10 and 15 fighter jets produced in years 1 and 2 are available for pilot training in those same years.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum limit on the number of fighter jets that can be allocated to training in any given year, or can all jets produced in a year be allocated to training if desired?

## Turn 3 - User Simulator

There is no maximum limit on the number of fighter jets that can be allocated to training in any given year. All jets produced in a year can be allocated to training if desired.

## Turn 4 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year consumed (i.e., no longer available for future years), or do they remain in the fleet and can be reused for training in subsequent years?

## Turn 4 - User Simulator

The fighter jets allocated to training in a given year remain in the fleet and can be reused for training in subsequent years.

## Turn 5 - Generic Agent

QUESTION: Are there any other requirements or constraints on the allocation of fighter jets to training, such as a minimum number of jets that must be reserved for operational use or a fixed proportion that must be allocated to training each year?

## Turn 5 - User Simulator

There are no other requirements or constraints on the allocation of fighter jets to training, such as a minimum number of jets that must be reserved for operational use or a fixed proportion that must be allocated to training each year.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2. **Decision Variables:** The number of fighter jets allocated to training in year 1 ($x_1$) and year 2 ($x_2$).
3. **Variable Domain:** $x_1$ and $x_2$ are non-negative integers (since jets are discrete units).
4. **Production Data:**
   - Year 1 production: 10 jets.
   - Year 2 production: 15 jets.
5. **Availability:** Jets produced in a given year are available for training in that same year.
6. **Training Capacity:** Each training jet trains 5 pilots per year.
7. **Fleet Accumulation:** Jets allocated to training remain in the fleet and can be reused in subsequent years. Therefore, the total fleet available in year 2 is the sum of jets produced in year 1 and year 2 (assuming all are kept).
8. **Constraints:**
   - $x_1 \le 10$ (cannot allocate more jets to training in year 1 than are produced/available).
   - $x_2 \le 10 + 15 = 25$ (cannot allocate more jets to training in year 2 than are available in the cumulative fleet).
   - No minimum operational reserve or other constraints.
9. **Objective Function:** Maximize $5x_1 + 5x_2$.

**Solution:**
Since there are no constraints forcing jets out of training and the objective is to maximize pilots, we should allocate all available jets to training in both years.
- Year 1: Allocate all 10 jets. Pilots trained = $10 \times 5 = 50$.
- Year 2: The fleet consists of the 10 jets from Year 1 plus the 15 new jets from Year 2, totaling 25 jets. Allocate all 25 jets. Pilots trained = $25 \times 5 = 125$.

**Total trained pilots by end of year 2:** $50 + 125 = 175$.