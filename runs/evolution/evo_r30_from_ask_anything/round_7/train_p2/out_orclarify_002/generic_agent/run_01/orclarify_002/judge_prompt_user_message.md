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

QUESTION: What is the number of fighter jets required to train one pilot during a single year?

## Turn 1 - User Simulator

One training jet is required to train five pilots in a single year, so the number of fighter jets required to train one pilot during a single year is 1/5 of a jet.

## Turn 2 - Generic Agent

QUESTION: Are the fighter jets allocated for training in a given year drawn exclusively from that year's production, or can jets produced in previous years be carried over and used for training in later years?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: If jets produced in previous years can be carried over, are they available for training in later years, or are they only available for other purposes?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Are the fighter jets produced in a given year available for pilot training in that same year, or do they become available for training only in the following year?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a fixed allocation of jets to training that determines the pilot count?

## Turn 5 - User Simulator

The goal is to maximize the total number of trained pilots by the end of year 2.

## Turn 6 - Generic Agent

QUESTION: Are there any other uses or constraints on the fighter jets besides pilot training, such as operational deployment or maintenance requirements that would reduce the number available for training?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Can fighter jets produced in year 1 be used for pilot training in year 2, or are they restricted to training only in the year they are produced?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is the total number of trained pilots by the end of year 2 calculated as the sum of pilots trained in year 1 and pilots trained in year 2, or does it refer only to pilots trained in year 2?

## Turn 8 - User Simulator

The total number of trained pilots by the end of year 2 is the sum of pilots trained in year 1 and pilots trained in year 2.

## Turn 9 - Generic Agent

QUESTION: Are there any limits on the number of pilots that can be trained in a single year, such as instructor availability or training facility capacity, other than the number of training jets allocated?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the fighter jets allocated for training in a given year drawn exclusively from that year's production, or can jets produced in previous years be carried over and used for training in later years?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2.  **Time Horizon:** 2 years (Year 1 and Year 2).
3.  **Production:**
    *   Year 1 production ($a_1$) = 10 jets.
    *   Year 2 production ($a_2$) = 15 jets.
4.  **Training Rate:** 1 training jet can train 5 pilots in a single year (or 1 pilot requires 1/5 of a jet-year).
5.  **Pilot Count Definition:** The total number of trained pilots by the end of year 2 is the sum of pilots trained in Year 1 and pilots trained in Year 2.

**Open Assumptions (due to lack of confirmation):**
1.  **Jet Availability for Training:** It is assumed that jets produced in a given year are available for training in that same year.
2.  **Carry-over of Jets:** It is assumed that jets produced in Year 1 can be carried over and used for training in Year 2. (If this is false, the model changes significantly, but given the "maximization" goal and lack of other constraints, assuming maximum availability is the standard interpretation for this type of resource allocation problem unless restricted).
3.  **Other Constraints:** It is assumed there are no other constraints on the number of pilots that can be trained (e.g., instructor limits, facility capacity) other than the number of training jets allocated.
4.  **Other Uses:** It is assumed there are no mandatory allocations of jets to other uses (e.g., operational deployment) that would reduce the pool available for training. All produced jets are available for training allocation.

**Model Formulation:**
Let $x_1$ be the number of jets allocated to training in Year 1.
Let $x_2$ be the number of jets allocated to training in Year 2.

**Objective:**
Maximize $Z = 5x_1 + 5x_2$

**Constraints:**
1.  **Year 1 Availability:** $x_1 \le a_1 = 10$
2.  **Year 2 Availability:** $x_1 + x_2 \le a_1 + a_2 = 25$ (Assuming carry-over is allowed and all jets are available for training).
    *   *Note:* If carry-over is NOT allowed, the constraint would be $x_2 \le a_2 = 15$. However, since the user did not confirm restrictions, the maximization logic implies using all available resources. If jets can be carried over, the total pool for Year 2 is the remaining jets from Year 1 plus Year 2 production.
    *   Actually, a simpler way to view this with carry-over: The total number of jets available over the 2 years is $10 + 15 = 25$. Since we want to maximize pilots, and there are no other constraints, we would allocate all 25 jets to training across the two years.
    *   Wait, the training happens *in* a year. A jet allocated in Year 1 trains 5 pilots in Year 1. A jet allocated in Year 2 trains 5 pilots in Year 2.
    *   If carry-over is allowed, we can use any of the 25 jets in either year.
    *   Max pilots = $5 \times (\text{Total Jets Allocated to Training})$.
    *   Since there are no other constraints, we allocate all 25 jets to training.
    *   Total Pilots = $5 \times 25 = 125$.

    *Alternative interpretation if no carry-over:*
    *   Year 1: Max 10 jets -> 50 pilots.
    *   Year 2: Max 15 jets -> 75 pilots.
    *   Total: 125 pilots.

    In both cases (with or without carry-over, assuming all jets are used for training), the maximum number of pilots is 125, because the total number of jet-years available is 25 in both scenarios (10 in Y1 + 15 in Y2). The carry-over question only matters if there were a constraint on *when* jets could be used or if some jets had to be reserved for other purposes. Since we are maximizing and have no other constraints, all jets will be used for training in the year they are available (or carried over if that helps, but since the rate is constant, it doesn't change the total count).

    Therefore, the solution is robust to the carry-over assumption as long as all jets can be used for training.

**Final Answer:**
The maximum number of trained pilots available by the end of year 2 is **125**.