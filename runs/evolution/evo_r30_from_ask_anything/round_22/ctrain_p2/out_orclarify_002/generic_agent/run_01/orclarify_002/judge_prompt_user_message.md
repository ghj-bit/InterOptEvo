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

QUESTION: Are the annual fighter jet production figures of 10 in year 1 and 15 in year 2 the total number of jets produced in each year, or do they represent the number of jets available for allocation after accounting for any other uses?

## Turn 1 - User Simulator

They are the total number of fighter jets produced in each year.

## Turn 2 - Generic Agent

QUESTION: How many fighter jets are required to train one pilot in a single year?

## Turn 2 - User Simulator

One training jet is required to train 5 pilots in a single year.

## Turn 3 - Generic Agent

QUESTION: Does a fighter jet allocated to pilot training in year 1 remain available for training in year 2, or is it consumed or retired after its training year?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: If a fighter jet allocated to pilot training in year 1 is not consumed, does it become available for other uses in year 2, or does it remain exclusively dedicated to training for the entire planning horizon?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum limit on the number of fighter jets that can be allocated to pilot training in any given year, or can all produced jets be allocated to training if desired?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any other uses or requirements for the fighter jets besides pilot training that must be satisfied before jets can be allocated to training?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a specific target number of pilots that must be met?

## Turn 7 - User Simulator

The goal is to determine the total number of trained pilots available by the end of year 2.

## Turn 8 - Generic Agent

QUESTION: Does a fighter jet allocated to training in year 1 remain available for training in year 2, or is it consumed or retired after its training year?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any other uses or requirements for the fighter jets besides pilot training that must be satisfied before jets can be allocated to training?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Production:** Total fighter jet production is 10 in Year 1 and 15 in Year 2.
2.  **Training Rate:** One training jet can train 5 pilots in a single year.
3.  **Objective:** Determine the total number of trained pilots available by the end of Year 2.

**Explicit Assumptions (due to lack of confirmation):**
1.  **Jet Lifespan/Availability:** It is assumed that a fighter jet allocated to training in Year 1 remains available for training in Year 2 (i.e., jets are not consumed or retired after one year of training).
2.  **Allocation Constraints:** It is assumed there are no other mandatory uses for the jets (e.g., combat deployment, reserve) and no maximum limit on the number of jets that can be allocated to training in any given year. Therefore, all produced jets can be allocated to training.
3.  **Cumulative Count:** It is assumed that "total number of trained pilots available by the end of year 2" refers to the cumulative sum of pilots trained in Year 1 and Year 2.

**Formulation:**
Let $x_1$ be the number of jets allocated to training in Year 1.
Let $x_2$ be the number of jets allocated to training in Year 2.

Given the assumptions:
*   $x_1 \le 10$ (Production in Year 1)
*   $x_2 \le 10 + 15 = 25$ (Cumulative production available in Year 2, assuming Year 1 jets carry over)
*   To maximize pilots, we allocate all available jets to training.
    *   $x_1 = 10$
    *   $x_2 = 25$

Pilots trained in Year 1: $10 \text{ jets} \times 5 \text{ pilots/jet} = 50 \text{ pilots}$.
Pilots trained in Year 2: $25 \text{ jets} \times 5 \text{ pilots/jet} = 125 \text{ pilots}$.

**Total Trained Pilots by End of Year 2:** $50 + 125 = 175$.