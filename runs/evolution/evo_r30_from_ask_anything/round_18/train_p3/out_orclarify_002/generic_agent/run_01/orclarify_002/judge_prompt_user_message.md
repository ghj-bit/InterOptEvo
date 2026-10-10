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

QUESTION: Is the total number of fighter jets available for allocation in each year exactly equal to that year's production (10 in year 1 and 15 in year 2), or do jets produced in year 1 carry over and remain available for allocation in year 2?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Are the 10 jets produced in year 1 available to be allocated for training in year 2 as well, or are they consumed or unavailable after year 1?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to training in any given year, or can all jets produced in that year be allocated to training?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to training in each year, or is it permissible to allocate zero jets to training in a given year?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any other requirements or constraints on the allocation of fighter jets to training that I should be aware of, such as limits on total training capacity or dependencies between years?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Production:** Year 1 production is 10 jets; Year 2 production is 15 jets.
2.  **Training Output:** Each fighter jet allocated to training produces 5 trained pilots per year.
3.  **Objective:** Determine the total number of trained pilots available by the end of year 2.

**Assumptions (due to lack of confirmation):**
1.  **No Carryover:** Jets produced in Year 1 are not available for allocation in Year 2. Each year's allocation is limited strictly to that year's production.
2.  **No Capacity Limits:** There is no maximum limit on the number of jets that can be allocated to training in any given year (i.e., all produced jets can be allocated to training if desired).
3.  **No Minimums:** There is no minimum requirement to allocate jets to training (allocation can be zero).
4.  **No Other Constraints:** There are no other hidden constraints, dependencies, or capacity limits affecting the allocation.

**Model Formulation:**
Let $x_1$ be the number of jets allocated to training in Year 1.
Let $x_2$ be the number of jets allocated to training in Year 2.

**Objective:** Maximize Total Pilots $Z = 5x_1 + 5x_2$

**Constraints:**
1.  $0 \le x_1 \le 10$ (Year 1 production limit)
2.  $0 \le x_2 \le 15$ (Year 2 production limit)
3.  $x_1, x_2$ are non-negative integers (assuming discrete jets)

**Solution:**
To maximize the number of trained pilots, we allocate the maximum possible number of jets to training in both years.
*   $x_1 = 10$
*   $x_2 = 15$

Total Pilits = $5(10) + 5(15) = 50 + 75 = 125$.

**Answer:** The maximum number of trained pilots available by the end of year 2 is **125**.