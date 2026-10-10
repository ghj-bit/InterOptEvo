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

QUESTION: Are the annual fighter jet production figures of 10 in year 1 and 15 in year 2 the total jets produced each year, with some of them then allocated to training, or are they the number of jets available for training after other allocations have already been made?

## Turn 1 - User Simulator

They are the total jets produced each year. Some of those produced jets are then allocated exclusively for pilot training.

## Turn 2 - Generic Agent

QUESTION: What is the maximum number of jets that can be allocated to pilot training in each year, or is there a specific rule (such as a fixed number, a percentage of production, or a limit based on available training slots) that determines how many jets are assigned to training each year?

## Turn 2 - User Simulator

There is no fixed number, percentage, or specific rule stated in the original request that determines how many jets are assigned to training each year. The only constraint is that "some fighter jets each year must be allocated exclusively for pilot training."

## Turn 3 - Generic Agent

QUESTION: How many trained pilots does one fighter jet produce per year when it is allocated to training, and is this rate the same in year 1 and year 2?

## Turn 3 - User Simulator

Each training jet can train 5 pilots per year. This rate is the same in year 1 and year 2.

## Turn 4 - Generic Agent

QUESTION: Can a jet allocated to training in year 1 continue to be used for training in year 2, or must each year's training jets be drawn exclusively from that year's new production?

## Turn 4 - User Simulator

I need to confirm this internally. The available business facts do not specify whether a jet allocated to training in year 1 can continue to be used for training in year 2, or if training jets must be drawn exclusively from that year's new production.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum limit on the total number of jets that can be allocated to training in any single year, or can all jets produced in a given year be allocated to training if desired?

## Turn 5 - User Simulator

There is no maximum limit stated. The only constraint is that "some fighter jets each year must be allocated exclusively for pilot training."

## Turn 6 - Generic Agent

QUESTION: Does the requirement that "some fighter jets each year must be allocated exclusively for pilot training" mean that at least one jet must be allocated to training in each year, or is it simply a descriptive statement that training allocation is part of the process without imposing a minimum?

## Turn 6 - User Simulator

It means that at least one jet must be allocated to training in each year.

## Turn 7 - Generic Agent

QUESTION: Are the number of jets allocated to training in each year required to be whole numbers, or can fractional jets be allocated?

## Turn 7 - User Simulator

The number of jets allocated to training in each year must be whole numbers.

## Turn 8 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots available by the end of year 2, or is there a specific target number of pilots that needs to be met?

## Turn 8 - User Simulator

The goal is to maximize the total number of trained pilots available by the end of year 2.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Production:** Total fighter jet production is 10 in Year 1 and 15 in Year 2.
2.  **Training Rate:** Each jet allocated to training produces 5 trained pilots per year.
3.  **Minimum Allocation:** At least 1 jet must be allocated to training in each year.
4.  **Variable Domain:** The number of jets allocated to training in each year must be a non-negative integer.
5.  **Objective:** Maximize the total number of trained pilots available by the end of Year 2.
6.  **No Upper Limit:** There is no stated maximum limit on the number of jets that can be allocated to training in any given year (other than the total production available).

**Assumptions (Unresolved Points):**
1.  **Jet Carry-over:** It is assumed that jets allocated to training in Year 1 **cannot** be reused for training in Year 2. Training jets must be drawn exclusively from that year's new production. (This was flagged as unconfirmed by the user).
    *   *Impact:* If jets *can* carry over, the model would allow Year 1 training jets to contribute to Year 2 pilot output, potentially increasing the total. Under the assumption that they cannot, Year 1 and Year 2 training allocations are independent.
2.  **Availability of Jets for Training:** It is assumed that all jets produced in a given year are available for allocation to training, subject only to the integer and minimum constraints. There are no other competing uses for the jets that would reduce the pool available for training.

**Model Formulation (based on assumptions):**
Let $x_1$ be the number of jets allocated to training in Year 1.
Let $x_2$ be the number of jets allocated to training in Year 2.

**Objective:**
Maximize $Z = 5x_1 + 5x_2$

**Constraints:**
1.  $x_1 \le 10$ (Cannot train with more jets than produced in Year 1)
2.  $x_2 \le 15$ (Cannot train with more jets than produced in Year 2)
3.  $x_1 \ge 1$ (At least one jet in Year 1)
4.  $x_2 \ge 1$ (At least one jet in Year 2)
5.  $x_1, x_2 \in \mathbb{Z}_{\ge 0}$ (Integer values)

**Solution:**
To maximize $Z$, we set $x_1$ and $x_2$ to their maximum possible values.
$x_1 = 10$
$x_2 = 15$

Total Trained Pilots = $5(10) + 5(15) = 50 + 75 = 125$.