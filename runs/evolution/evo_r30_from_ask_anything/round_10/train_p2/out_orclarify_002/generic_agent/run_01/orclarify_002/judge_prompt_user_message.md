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

QUESTION: Is the number of fighter jets allocated to training in each year a decision variable you can choose freely, or is it fixed by some external requirement?

## Turn 2 - User Simulator

The number of fighter jets allocated to training in each year is a decision variable that can be chosen freely, subject to the constraint that some fighter jets each year must be allocated exclusively for pilot training.

## Turn 3 - Generic Agent

QUESTION: What is the minimum number of fighter jets that must be allocated to training in each year?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to training in each year, or is the only upper bound the total production available that year?

## Turn 4 - User Simulator

The only upper bound is the total production available that year.

## Turn 5 - Generic Agent

QUESTION: Are the fighter jets allocated to training in year 1 and year 2 independent decisions, or does the allocation in one year affect the availability of jets in the other year?

## Turn 5 - User Simulator

The allocation in year 1 and year 2 are independent decisions.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots by the end of year 2, or is there a specific target number of trained pilots that must be met?

## Turn 6 - User Simulator

The objective is to maximize the total number of trained pilots by the end of year 2.

## Turn 7 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year consumed (i.e., no longer available for other uses after that year), or do they remain in the fleet after the training year?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the decision variables for the number of jets allocated to training in each year required to be whole numbers, or can they be fractional?

## Turn 8 - User Simulator

The decision variables for the number of jets allocated to training in each year are required to be whole numbers.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed facts:**
- Annual fighter jet production: 10 in year 1, 15 in year 2.
- Each fighter jet allocated to training produces 5 trained pilots per year.
- The number of jets allocated to training in each year is a decision variable.
- The only upper bound on jets allocated to training in a given year is the total production available that year.
- Allocations in year 1 and year 2 are independent decisions.
- The objective is to maximize the total number of trained pilots by the end of year 2.
- Decision variables must be whole numbers (integer).

**Assumptions (unconfirmed):**
- The minimum number of fighter jets that must be allocated to training in each year is unknown. I assume there is no minimum requirement beyond zero (i.e., at least 0 jets must be allocated to training each year).
- Whether jets allocated to training are consumed or remain in the fleet after the training year is unconfirmed. I assume they are consumed (not available for other uses after the training year), which does not affect the pilot count calculation since the objective is solely to maximize trained pilots.

**Formulation:**
- Decision variables: x1 = number of jets allocated to training in year 1 (integer, 0 ≤ x1 ≤ 10); x2 = number of jets allocated to training in year 2 (integer, 0 ≤ x2 ≤ 15).
- Objective: Maximize 5x1 + 5x2.
- Constraints: x1 ≤ 10, x2 ≤ 15, x1 and x2 are non-negative integers.

**Solution:**
To maximize 5x1 + 5x2, set x1 = 10 and x2 = 15.
Total trained pilots = 5(10) + 5(15) = 50 + 75 = **125**.