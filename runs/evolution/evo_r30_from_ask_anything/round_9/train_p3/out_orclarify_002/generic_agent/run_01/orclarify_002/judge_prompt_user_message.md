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

QUESTION: Is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training in that year, or is there a different conversion rate or training duration that affects how many pilots are available by the end of year 2?

## Turn 1 - User Simulator

There is a different conversion rate. Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Do the 5 pilots trained by a jet in a given year become available immediately in that same year, or do they only become available in the following year?

## Turn 2 - User Simulator

The 5 pilots trained by a jet in a given year become available in the following year.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on how many fighter jets can be allocated to training in each year, or can any number of the produced jets be assigned to training?

## Turn 3 - User Simulator

There is no stated limit on how many fighter jets can be allocated to training in each year.

## Turn 4 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year consumed (i.e., no longer available for future years), or do they remain in the fleet and can be used for training in multiple years?

## Turn 4 - User Simulator

The fighter jets allocated to training remain in the fleet and can be used for training in multiple years.

## Turn 5 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots available by the end of year 2, or is there a specific allocation plan you want to evaluate?

## Turn 5 - User Simulator

The goal is to maximize the total number of trained pilots available by the end of year 2.

## Turn 6 - Generic Agent

QUESTION: Are there any other uses or requirements for the fighter jets besides pilot training that would limit how many can be allocated to training in each year?

## Turn 6 - User Simulator

No, there are no other uses or requirements for the fighter jets besides pilot training that would limit how many can be allocated to training in each year.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2. **Decision Variables:** The number of fighter jets allocated to training in year 1 (x1) and year 2 (x2).
3. **Variable Domain:** x1 and x2 are non-negative integers (number of jets).
4. **Production Data:**
   - Year 1 production: a1 = 10 jets
   - Year 2 production: a2 = 15 jets
5. **Training Conversion Rate:** Each training jet trains 5 pilots per year.
6. **Pilot Availability Timing:** Pilots trained in year t become available in year t+1.
   - Pilots trained in year 1 become available in year 2.
   - Pilots trained in year 2 become available in year 3 (not counted in the end-of-year-2 total).
7. **Jet Fleet Dynamics:** Jets allocated to training remain in the fleet and can be reused in subsequent years.
8. **Constraints:**
   - x1 ≤ 10 (cannot allocate more jets to training in year 1 than are produced)
   - x2 ≤ 10 + 15 = 25 (cannot allocate more jets to training in year 2 than the cumulative fleet available: 10 from year 1 + 15 from year 2)
   - No other constraints on jet allocation.
9. **Objective Function:** Maximize 5 * x1 (only year 1 training contributes to pilots available by end of year 2, since year 2 training produces pilots available in year 3).

**Key Insight:** Since only pilots trained in year 1 are available by the end of year 2, the optimal strategy is to allocate all 10 year-1 jets to training, yielding 50 trained pilots available by the end of year 2. The year-2 allocation does not affect the end-of-year-2 pilot count.