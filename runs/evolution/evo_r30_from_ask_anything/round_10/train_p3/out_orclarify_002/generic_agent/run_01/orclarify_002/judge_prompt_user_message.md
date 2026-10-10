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

QUESTION: Is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training in that year, or is there a different conversion rate or delay between jets allocated and pilots actually trained?

## Turn 1 - User Simulator

There is a different conversion rate. Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Do the 5 pilots trained by a jet in a given year become available in that same year, or do they become available in the following year?

## Turn 2 - User Simulator

The 5 pilots trained by a jet in a given year become available in that same year.

## Turn 3 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that year's production, or can jets produced in previous years be carried over and used for training in later years?

## Turn 3 - User Simulator

The fighter jets allocated to training in a given year are drawn from that year's production.

## Turn 4 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to training each year, or is the allocation to training a free decision variable that can be zero?

## Turn 4 - User Simulator

The allocation to training is a free decision variable that can be zero.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to training in a given year, or is the only upper bound the total production available that year?

## Turn 5 - User Simulator

The only upper bound is the total production available that year.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots available by the end of year 2, or is there a specific target number of pilots that must be met?

## Turn 6 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements on the fighter jet production and training setup that I should be aware of, such as minimum production levels, budget limits, or restrictions on how many jets can be used for other purposes?

## Turn 7 - User Simulator

No, there are no other constraints or requirements beyond those already discussed.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total number of trained pilots available by the end of year 2. *(Confirmed)*
2. **Decision Variables:** Let $x_1$ and $x_2$ be the number of fighter jets allocated to training in year 1 and year 2, respectively. *(Confirmed)*
3. **Variable Domain:** $x_1$ and $x_2$ are non-negative integers (since you cannot allocate a fraction of a jet). *(Assumed: integrality is standard for discrete physical assets like jets, though not explicitly stated. If fractional jets were allowed, the math would be identical but the interpretation would differ.)*
4. **Constraints:**
   - Year 1: $x_1 \le 10$ (Production in year 1 is 10). *(Confirmed)*
   - Year 2: $x_2 \le 15$ (Production in year 2 is 15). *(Confirmed)*
   - No carry-over: Jets allocated in year 1 cannot be used in year 2; each year's allocation is drawn only from that year's production. *(Confirmed)*
   - No minimum allocation: $x_1 \ge 0$, $x_2 \ge 0$. *(Confirmed)*
   - No other constraints. *(Confirmed)*
5. **Objective Function:** Total pilots = $5x_1 + 5x_2$. Each training jet produces 5 pilots in the same year. *(Confirmed)*
6. **Quantity Interpretation:**
   - $a_1 = 10$: Total production in year 1. *(Confirmed)*
   - $a_2 = 15$: Total production in year 2. *(Confirmed)*
   - 5: Pilots per training jet per year. *(Confirmed)*

**Solution:**

Since the objective is to maximize $5x_1 + 5x_2$ subject to $x_1 \le 10$ and $x_2 \le 15$, the optimal solution is to allocate the maximum possible number of jets to training in both years.

- $x_1 = 10$
- $x_2 = 15$

Total trained pilots = $5(10) + 5(15) = 50 + 75 = 125$.

**Answer:** The maximum number of trained pilots available by the end of year 2 is **125**.