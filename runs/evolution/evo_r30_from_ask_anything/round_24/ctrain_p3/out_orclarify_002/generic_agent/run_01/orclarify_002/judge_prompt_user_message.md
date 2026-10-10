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

QUESTION: How many fighter jets must be allocated exclusively for pilot training each year?

## Turn 1 - User Simulator

The number of fighter jets allocated exclusively for pilot training each year is not fixed. It is a decision variable that we need to determine as part of the optimization. The only requirement is that some jets each year must be allocated exclusively for pilot training.

## Turn 2 - Generic Agent

QUESTION: What is the objective of the optimization, such as maximizing the total number of trained pilots by the end of year 2?

## Turn 2 - User Simulator

The objective is to determine the total number of trained pilots available by the end of year 2.

## Turn 3 - Generic Agent

QUESTION: How many trained pilots does one fighter jet allocated exclusively for training produce in a single year?

## Turn 3 - User Simulator

Each training jet can train 5 pilots per year.

## Turn 4 - Generic Agent

QUESTION: Is there a minimum number of fighter jets that must be allocated to training each year, or is it sufficient that the allocation is simply greater than zero?

## Turn 4 - User Simulator

The requirement is simply that the allocation is greater than zero. There is no specific minimum number of fighter jets that must be allocated to training each year.

## Turn 5 - Generic Agent

QUESTION: Are the number of fighter jets allocated to training in each year required to be whole numbers (integers), or can they be fractional?

## Turn 5 - User Simulator

The number of fighter jets allocated to training in each year must be whole numbers (integers).

## Turn 6 - Generic Agent

QUESTION: Are the fighter jets allocated to training in year 1 and year 2 drawn from the same pool of jets, or does each year's production (10 in year 1, 15 in year 2) constitute a separate, independent pool from which training jets are chosen?

## Turn 6 - User Simulator

Each year's production constitutes a separate, independent pool from which training jets are chosen.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints on the number of jets that can be allocated to training, such as a maximum limit per year or a requirement that a certain number of jets must be reserved for operational use?

## Turn 7 - User Simulator

There are no other constraints on the number of jets that can be allocated to training, such as a maximum limit per year or a requirement that a certain number of jets must be reserved for operational use.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2.  **Decision Variables:**
    *   $x_1$: Number of fighter jets allocated to training in Year 1.
    *   $x_2$: Number of fighter jets allocated to training in Year 2.
3.  **Variable Domain:**
    *   $x_1$ and $x_2$ must be integers.
    *   $x_1 > 0$ and $x_2 > 0$ (strictly greater than zero).
4.  **Constraints:**
    *   Year 1 Production Limit: $x_1 \le 10$ (since the pool is 10 jets).
    *   Year 2 Production Limit: $x_2 \le 15$ (since the pool is 15 jets).
    *   No other constraints (no operational reserve, no cross-year dependencies).
5.  **Quantity Interpretation:**
    *   Each training jet produces 5 pilots per year.
    *   Total pilots = $5 \times x_1 + 5 \times x_2$.
6.  **Accounting/Flow:**
    *   Pools are independent per year.
    *   Pilots accumulate over the two years.

**Formulation:**
Maximize $Z = 5x_1 + 5x_2$
Subject to:
$x_1 \le 10$
$x_2 \le 15$
$x_1 \ge 1$
$x_2 \ge 1$
$x_1, x_2 \in \mathbb{Z}$

**Solution:**
To maximize the objective, we should allocate the maximum possible number of jets to training in each year, subject to the production limits and the "greater than zero" constraint (which is satisfied by the maximums).

*   Max $x_1 = 10$
*   Max $x_2 = 15$

Total Pilots = $5(10) + 5(15) = 50 + 75 = 125$.

**Final Answer:** The total number of trained pilots available by the end of year 2 is **125**.