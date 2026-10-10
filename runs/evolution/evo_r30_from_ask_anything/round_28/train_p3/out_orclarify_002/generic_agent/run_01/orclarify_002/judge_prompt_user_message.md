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

QUESTION: Are the annual fighter jet production figures a1 = 10 and a2 = 15 the total number of jets produced in each year, or do they represent the number of jets available for allocation after accounting for any other uses?

## Turn 1 - User Simulator

They are the total number of jets produced in each year.

## Turn 2 - Generic Agent

QUESTION: How many of the jets produced in each year must be allocated exclusively for pilot training, and is this number a fixed count, a percentage of production, or a variable we need to determine?

## Turn 2 - User Simulator

The number of jets allocated exclusively for pilot training is a variable we need to determine.

## Turn 3 - Generic Agent

QUESTION: What is the objective of the model, is it to maximize the total number of trained pilots available by the end of year 2, or is there a different goal such as minimizing the number of jets allocated to training?

## Turn 3 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 4 - Generic Agent

QUESTION: How many trained pilots does one fighter jet produce per year when allocated exclusively for pilot training, and is this rate constant across both years?

## Turn 4 - User Simulator

Each training jet can train 5 pilots per year, and this rate is constant across both years.

## Turn 5 - Generic Agent

QUESTION: Are the jets allocated for training in year 1 still available for training in year 2, or are they consumed or retired after year 1?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Do the training jets allocated in year 1 remain available for training in year 2, or are they retired after year 1 such that only year 2 production can be allocated for training in year 2?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any constraints on the number of jets that can be allocated for training in each year, such as a maximum percentage of production or a minimum number of jets that must be reserved for other purposes?

## Turn 7 - User Simulator

There are no constraints on the number of jets that can be allocated for training in each year, such as a maximum percentage of production or a minimum number of jets that must be reserved for other purposes.

## Turn 8 - Generic Agent

QUESTION: Are the jets allocated for training in year 1 still available for training in year 2, or are they retired after year 1 such that only year 2 production can be allocated for training in year 2?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2.  **Production Data:** Total fighter jet production is 10 in Year 1 ($a_1 = 10$) and 15 in Year 2 ($a_2 = 15$).
3.  **Training Rate:** Each jet allocated exclusively for training produces 5 trained pilots per year.
4.  **Decision Variables:** The number of jets allocated to training in Year 1 ($x_1$) and Year 2 ($x_2$) are variables to be determined.
5.  **Constraints:** There are no explicit upper or lower bounds on the number of jets allocated to training other than the total production available in each year.
6.  **Variable Domain:** The number of jets allocated to training must be non-negative integers (since you cannot allocate a fraction of a jet).

**Explicit Assumptions:**
1.  **Jet Lifespan/Availability:** It is assumed that jets allocated for training in Year 1 are **retired or unavailable** for training in Year 2. This means the pool of jets available for training in Year 2 consists only of the jets produced in Year 2. (Note: This was left unconfirmed by the user, but is the standard interpretation for "annual production" problems where assets are not explicitly stated to carry over. If jets *do* carry over, the model changes significantly.)
2.  **Independence of Training:** The training output of a jet in a given year depends only on that jet being allocated in that specific year.

**Model Formulation:**

Let $x_1$ be the number of jets allocated to training in Year 1.
Let $x_2$ be the number of jets allocated to training in Year 2.

**Objective Function:**
Maximize $Z = 5x_1 + 5x_2$

**Subject to:**
1.  $x_1 \le 10$ (Year 1 production limit)
2.  $x_2 \le 15$ (Year 2 production limit)
3.  $x_1, x_2 \ge 0$ and integer

**Solution:**
Since the objective is to maximize the number of pilots and there are no other constraints limiting the allocation of jets to training (e.g., no requirement to keep jets for combat or other uses), the optimal strategy is to allocate **all** available jets to training in both years.

*   $x_1 = 10$
*   $x_2 = 15$

**Total Trained Pilots by End of Year 2:**
$Z = 5(10) + 5(15) = 50 + 75 = 125$

**Answer:** The maximum number of trained pilots available by the end of year 2 is **125**.