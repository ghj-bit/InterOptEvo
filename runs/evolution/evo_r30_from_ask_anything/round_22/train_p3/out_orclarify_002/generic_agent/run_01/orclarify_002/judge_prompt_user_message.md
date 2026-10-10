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

QUESTION: What is the number of trained pilots that a single fighter jet can produce when it is allocated exclusively for pilot training in a given year?

## Turn 1 - User Simulator

A single fighter jet allocated exclusively for pilot training can train 5 pilots in a given year.

## Turn 2 - Generic Agent

QUESTION: Are the fighter jets produced in year 1 available for pilot training in year 1, or do they only become available for training starting in year 2?

## Turn 2 - User Simulator

The fighter jets produced in year 1 are available for pilot training in year 1.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on the number of fighter jets that can be allocated for pilot training in each year, or can any number of the available jets be used for training?

## Turn 3 - User Simulator

There is no stated limit on the number of fighter jets that can be allocated for pilot training in each year; any number of the available jets can be used for training.

## Turn 4 - Generic Agent

QUESTION: Do the fighter jets allocated for pilot training in a given year remain available for training in subsequent years, or are they consumed and no longer available after that year?

## Turn 4 - User Simulator

The fighter jets allocated for pilot training in a given year remain available for training in subsequent years.

## Turn 5 - Generic Agent

QUESTION: Are the fighter jets produced in year 2 available for pilot training in year 2, or do they only become available for training starting in year 3?

## Turn 5 - User Simulator

The fighter jets produced in year 2 are available for pilot training in year 2.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or requirements that limit how many fighter jets can be allocated for pilot training in each year, such as a minimum number of jets that must be reserved for operational use?

## Turn 6 - User Simulator

There are no other constraints or requirements that limit how many fighter jets can be allocated for pilot training in each year, such as a minimum number of jets that must be reserved for operational use.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2. **Decision Variables:** The number of fighter jets allocated for pilot training in year 1 ($x_1$) and year 2 ($x_2$).
3. **Variable Domain:** $x_1$ and $x_2$ are non-negative integers (since jets are discrete units).
4. **Production Data:**
   - Year 1 production: $a_1 = 10$ jets.
   - Year 2 production: $a_2 = 15$ jets.
5. **Availability Rules:**
   - Jets produced in a given year are available for training in that same year.
   - Jets allocated for training in a given year remain available for training in subsequent years (they are not consumed).
6. **Training Rate:** Each fighter jet allocated for training in a given year trains 5 pilots in that year.
7. **Constraints:**
   - There are no limits on the number of jets that can be allocated for training.
   - There are no minimum operational requirements or other constraints limiting training allocation.
   - The only implicit constraint is that you cannot allocate more jets for training than are available (i.e., $x_1 \le 10$ and $x_2 \le 10 + 15 = 25$, assuming all year 1 jets are available in year 2).

**Formulation:**

Let $x_1$ be the number of jets allocated for training in year 1.
Let $x_2$ be the number of jets allocated for training in year 2.

**Objective:**
Maximize $Z = 5x_1 + 5x_2$

**Subject to:**
1. $x_1 \le 10$ (Jets available in year 1)
2. $x_2 \le 10 + 15 = 25$ (Jets available in year 2: 10 from year 1 + 15 from year 2)
3. $x_1, x_2 \ge 0$ and integer.

**Solution:**
Since there are no other constraints, we maximize $x_1$ and $x_2$ to their upper bounds.
$x_1 = 10$
$x_2 = 25$

Total trained pilots by end of year 2:
$Z = 5(10) + 5(25) = 50 + 125 = 175$

**Final Answer:** The total number of trained pilots available by the end of year 2 is **175**.