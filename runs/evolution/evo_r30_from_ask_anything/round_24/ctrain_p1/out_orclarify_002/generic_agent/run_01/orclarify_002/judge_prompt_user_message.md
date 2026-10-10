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

QUESTION: What is the number of trained pilots that each fighter jet allocated to training produces in a given year?

## Turn 1 - User Simulator

Each fighter jet allocated to training produces 5 trained pilots in a given year.

## Turn 2 - Generic Agent

QUESTION: Is the number of fighter jets allocated to training in each year a decision variable you can choose freely, or is it fixed by some external requirement?

## Turn 2 - User Simulator

The number of fighter jets allocated to training in each year is a decision variable that can be chosen freely, subject to the constraint that some fighter jets each year must be allocated exclusively for pilot training.

## Turn 3 - Generic Agent

QUESTION: What is the minimum number of fighter jets that must be allocated to training in each year?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: If the minimum number of fighter jets allocated to training each year is not confirmed, should I treat it as zero (meaning no mandatory minimum, so the allocation can be any non-negative integer up to the annual production)?

## Turn 4 - User Simulator

No, that is not correct. The business requirement states that "some fighter jets each year must be allocated exclusively for pilot training." This implies a mandatory minimum greater than zero, but the exact number is not specified in the available facts.

## Turn 5 - Generic Agent

QUESTION: Should I treat the mandatory minimum number of fighter jets allocated to training each year as exactly 1, or is there a specific integer value greater than 1 that applies?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the exact minimum is unconfirmed, should I proceed with the assumption that at least 1 fighter jet must be allocated to training in each year, or would you prefer I leave this as an open parameter in the final formulation?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Should I treat the minimum number of fighter jets allocated to training in each year as a fixed parameter M (where M ≥ 1) that you will specify later, rather than assuming a specific value?

## Turn 7 - User Simulator

Yes, treat the minimum number of fighter jets allocated to training in each year as a fixed parameter M (where M ≥ 1) that will be specified later.

## Turn 8 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn only from that year's production, or can jets produced in a previous year also be allocated to training in a later year?

## Turn 8 - User Simulator

The fighter jets allocated to training in a given year are drawn only from that year's production.

## Turn 9 - Generic Agent

QUESTION: Is the number of fighter jets allocated to training in each year required to be an integer, or can it be a continuous value?

## Turn 9 - User Simulator

The number of fighter jets allocated to training in each year must be an integer.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints on the allocation of fighter jets to training, such as a maximum number that can be allocated in a given year?

## Turn 10 - User Simulator

No, there are no other constraints on the allocation of fighter jets to training beyond the minimum parameter M and the fact that the allocation cannot exceed that year's production.

## Turn 11 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots available by the end of year 2, or is there a different goal such as meeting a specific pilot target?

## Turn 11 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 12 - Generic Agent

QUESTION: Do the trained pilots produced in year 1 remain available and count toward the total at the end of year 2, or do they expire or get reassigned such that only year 2 pilots count?

## Turn 12 - User Simulator

The trained pilots produced in year 1 remain available and count toward the total at the end of year 2.

## Turn 13 - Generic Agent

QUESTION: Are there any other requirements or constraints not yet discussed, such as a minimum number of fighter jets that must remain available for operational use after training allocation?

## Turn 13 - User Simulator

No, there are no other requirements or constraints not yet discussed.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Decision Variables:** Let \( x_1 \) and \( x_2 \) be the number of fighter jets allocated to training in year 1 and year 2, respectively. Both are non-negative integers.
- **Production Limits:**
  - Year 1 production: \( a_1 = 10 \)
  - Year 2 production: \( a_2 = 15 \)
- **Constraints:**
  - \( x_1 \leq 10 \) (cannot allocate more jets to training than produced in year 1)
  - \( x_2 \leq 15 \) (cannot allocate more jets to training than produced in year 2)
  - \( x_1 \geq M \) (minimum allocation in year 1, where \( M \geq 1 \) is a parameter to be specified)
  - \( x_2 \geq M \) (minimum allocation in year 2, where \( M \geq 1 \) is a parameter to be specified)
- **Pilot Production:** Each fighter jet allocated to training produces 5 trained pilots in that year.
- **Pilot Accumulation:** Pilots produced in year 1 remain available and count toward the total at the end of year 2.
- **Objective Function:** Maximize \( 5x_1 + 5x_2 \)
- **No Other Constraints:** No operational reserve requirements, no maximum allocation limits beyond production, no other exclusivity or interaction rules.

**Open Assumption:**
- The parameter \( M \) (minimum number of fighter jets allocated to training each year) is treated as a fixed parameter to be specified later, with the only known bound being \( M \geq 1 \).