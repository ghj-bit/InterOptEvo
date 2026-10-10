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

QUESTION: Are the annual production figures a1 = 10 and a2 = 15 the total number of fighter jets produced in year 1 and year 2 respectively, or do they represent some other quantity such as the number of jets available for allocation after accounting for prior commitments?

## Turn 1 - User Simulator

They are the total number of fighter jets produced in year 1 and year 2, respectively.

## Turn 2 - Generic Agent

QUESTION: How many fighter jets must be allocated exclusively for pilot training in each year, and is that number a fixed count, a percentage of that year's production, or a variable we are choosing to optimize?

## Turn 2 - User Simulator

The number of fighter jets allocated exclusively for pilot training in each year is a variable we are choosing to optimize.

## Turn 3 - Generic Agent

QUESTION: What is the objective we are optimizing, and in which direction: are we maximizing the total number of trained pilots available by the end of year 2, or is there a different goal such as minimizing the number of jets used for training while meeting a pilot requirement?

## Turn 3 - User Simulator

We are maximizing the total number of trained pilots available by the end of year 2.

## Turn 4 - Generic Agent

QUESTION: How many trained pilots does one fighter jet allocated to training produce in a given year, and is that rate the same in year 1 and year 2 or does it differ between the two years?

## Turn 4 - User Simulator

One fighter jet allocated to training produces 5 trained pilots in a given year. That rate is the same in year 1 and year 2.

## Turn 5 - Generic Agent

QUESTION: Do the trained pilots produced in year 1 carry over and remain available by the end of year 2, or does "trained pilots available by the end of year 2" count only the pilots produced in year 2?

## Turn 5 - User Simulator

The trained pilots produced in year 1 carry over and remain available by the end of year 2.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum or maximum limits on the number of fighter jets that can be allocated to training in each year, or can we allocate anywhere from zero up to the full production of that year?

## Turn 6 - User Simulator

There are no minimum or maximum limits on the number of fighter jets that can be allocated to training in each year, other than the total production available that year.

## Turn 7 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year consumed (i.e., no longer available for other uses in later years), or do they remain in the fleet after being used for training?

## Turn 7 - User Simulator

The fighter jets allocated to training in a given year remain in the fleet after being used for training.

## Turn 8 - Generic Agent

QUESTION: Are there any other uses or requirements for the fighter jets besides pilot training that would limit how many can be allocated to training, or is the only constraint the total production available each year?

## Turn 8 - User Simulator

The only constraint is the total production available each year.

## Turn 9 - Generic Agent

QUESTION: Is the number of fighter jets allocated to training in each year required to be a whole number (integer), or can it be a fractional value?

## Turn 9 - User Simulator

The number of fighter jets allocated to training in each year must be a whole number (integer).

## Turn 10 - Generic Agent

QUESTION: Is there any requirement that the number of jets allocated to training in year 1 and year 2 must be equal, or can they differ from year to year?

## Turn 10 - User Simulator

The number of jets allocated to training in year 1 and year 2 can differ from year to year.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize the total number of trained pilots available by the end of year 2.
- Decision variables: Let x1 = number of fighter jets allocated to training in year 1, x2 = number of fighter jets allocated to training in year 2.
- Variable domain: x1 and x2 are non-negative integers.
- Constraints:
  - x1 ≤ 10 (year 1 production)
  - x2 ≤ 15 (year 2 production)
- Pilot production: Each jet allocated to training produces 5 trained pilots in that year.
- Carry-over: Pilots produced in year 1 remain available by the end of year 2.
- Objective function: Maximize 5*x1 + 5*x2.
- No other constraints, minimums, maximums, or coupling between years.
- Jets used for training remain in the fleet afterward (no consumption effect on future years).

Solution: Since the objective is to maximize 5*x1 + 5*x2 subject only to x1 ≤ 10 and x2 ≤ 15, the optimal solution is x1 = 10 and x2 = 15, yielding a total of 5*(10 + 15) = 125 trained pilots available by the end of year 2.