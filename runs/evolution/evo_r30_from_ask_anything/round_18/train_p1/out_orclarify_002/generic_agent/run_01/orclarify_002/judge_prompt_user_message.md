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

QUESTION: Is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training that year, or is there a different conversion rate or training duration that affects how many pilots are available by the end of year 2?

## Turn 1 - User Simulator

There is a different conversion rate. Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Are the 5 pilots trained by a training jet in a given year available immediately at the end of that same year, or do they require an additional year of training before they are counted as available?

## Turn 2 - User Simulator

The 5 pilots trained by a training jet in a given year are available at the end of that same year.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on the number of fighter jets that can be allocated to training in any given year, or can any number of the produced jets be assigned to training as long as the total does not exceed that year's production?

## Turn 3 - User Simulator

There is no stated limit on the number of fighter jets that can be allocated to training in any given year, other than the total not exceeding that year's production.

## Turn 4 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year reusable for training in subsequent years, or are they consumed or removed from the pool after one year of training?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: If the training jets are not reusable, does the number of trained pilots available by the end of year 2 equal the sum of pilots trained in year 1 plus pilots trained in year 2, or are pilots trained in year 1 no longer counted as available by the end of year 2?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to training in each year, or is it permissible to allocate zero jets to training in a given year?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots available by the end of year 2, or is there a specific target number of pilots that must be met?

## Turn 7 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 8 - Generic Agent

QUESTION: Are the fighter jets produced in year 1 available for allocation to training in year 2, or is each year's production only available for allocation in that same year?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the fighter jets produced in year 1 available for allocation to training in year 2, or is each year's production only available for allocation in that same year?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2.  **Production:** Year 1 production ($a_1$) is 10 jets; Year 2 production ($a_2$) is 15 jets.
3.  **Conversion Rate:** Each training jet trains 5 pilots per year.
4.  **Availability Timing:** Pilots trained in a given year are available at the end of that same year.
5.  **Training Capacity Constraint:** The number of jets allocated to training in a given year cannot exceed that year's production.

**Explicit Assumptions (due to lack of confirmation):**
1.  **Jet Reusability:** It is assumed that training jets are **not** reusable across years. A jet allocated to training in Year 1 is not available for training in Year 2. (If they were reusable, the model would change significantly, but given the "production and training setup" context and the lack of confirmation, non-reusability is the standard interpretation for annual production allocation problems unless stated otherwise).
2.  **Production Availability:** It is assumed that each year's production is **only** available for allocation in that same year. Jets produced in Year 1 cannot be held back to be used for training in Year 2.
3.  **Minimum Training Allocation:** It is assumed there is **no minimum** requirement to allocate jets to training. The decision variable (number of jets allocated to training) can be zero.
4.  **Pilot Accumulation:** It is assumed that pilots trained in Year 1 remain available and are counted in the total at the end of Year 2. The objective is the cumulative total of pilots trained in Year 1 and Year 2.

**Model Formulation:**
Let $x_1$ be the number of jets allocated to training in Year 1.
Let $x_2$ be the number of jets allocated to training in Year 2.

**Objective Function:**
Maximize $Z = 5x_1 + 5x_2$

**Constraints:**
1.  $0 \le x_1 \le 10$ (Year 1 production limit)
2.  $0 \le x_2 \le 15$ (Year 2 production limit)
3.  $x_1, x_2$ are non-negative integers (assuming discrete jets).

**Solution:**
To maximize $Z$, we should allocate the maximum possible number of jets to training in both years.
$x_1 = 10$
$x_2 = 15$

Total Pilots = $5(10) + 5(15) = 50 + 75 = 125$.

**Final Answer:**
The maximum number of trained pilots available by the end of year 2 is **125**.