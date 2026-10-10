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

QUESTION: Is the number of trained pilots produced in a given year equal to the number of fighter jets allocated to training in that same year, or does each training jet produce a different number of pilots (for example, multiple pilots per jet or a fixed rate)?

## Turn 1 - User Simulator

Each training jet produces a fixed number of pilots per year. Specifically, each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: Is the number of fighter jets allocated to training in a given year a decision variable you can choose freely (subject to constraints), or is it fixed by some rule such as a specific fraction or percentage of that year's production?

## Turn 2 - User Simulator

The number of fighter jets allocated to training in a given year is a decision variable that can be chosen freely, subject to the constraint that some fighter jets each year must be allocated exclusively for pilot training.

## Turn 3 - Generic Agent

QUESTION: What is the minimum number of fighter jets that must be allocated to training in each year, or is there a specific lower bound (such as a fixed number or a percentage of production) that defines the "some" requirement?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum number of fighter jets that can be allocated to training in each year, or is the only upper bound the total production available in that year?

## Turn 4 - User Simulator

The only upper bound is the total production available in that year.

## Turn 5 - Generic Agent

QUESTION: Do the fighter jets allocated to training in year 1 remain available for training in year 2, or is the training allocation in each year drawn only from that year's new production?

## Turn 5 - User Simulator

The training allocation in each year is drawn only from that year's new production.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total number of trained pilots available by the end of year 2, or is there a specific target number of pilots that must be met?

## Turn 6 - User Simulator

The objective is to maximize the total number of trained pilots available by the end of year 2.

## Turn 7 - Generic Agent

QUESTION: Are the number of training jets allocated in each year required to be whole numbers (integers), or can they be fractional values?

## Turn 7 - User Simulator

The number of training jets allocated in each year must be whole numbers (integers).

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the total number of trained pilots available by the end of year 2.
2.  **Decision Variables:** Let $x_1$ and $x_2$ be the number of fighter jets allocated to training in year 1 and year 2, respectively.
3.  **Variable Domain:** $x_1$ and $x_2$ are non-negative integers.
4.  **Production Data:**
    *   Year 1 production ($a_1$) = 10 jets.
    *   Year 2 production ($a_2$) = 15 jets.
5.  **Training Rate:** Each training jet produces 5 pilots per year.
6.  **Constraints:**
    *   Upper bound: $x_1 \le 10$ and $x_2 \le 15$ (allocation cannot exceed production).
    *   Lower bound: The requirement that "some" jets must be allocated to training is **unconfirmed**. I am assuming there is no minimum lower bound other than $x_1 \ge 0$ and $x_2 \ge 0$ (i.e., it is permissible to allocate zero jets to training if that maximizes the objective, though logically if the goal is to maximize pilots, we would allocate as many as possible).
    *   Independence: Training allocations in each year are drawn only from that year's new production (no carry-over of jets).

**Assumptions:**
*   **Minimum Training Allocation:** The specific lower bound for "some fighter jets" was not confirmed. I assume the lower bound is 0. If there is a strict minimum (e.g., at least 1 jet per year), the model would need that constraint added. However, since the objective is to *maximize* pilots, the optimal solution will naturally push $x_1$ and $x_2$ to their maximum possible values regardless of a small lower bound, unless the lower bound is negative (which is impossible). Thus, the maximum solution is likely robust to this assumption.

**Formulation:**
Maximize $Z = 5x_1 + 5x_2$
Subject to:
$x_1 \le 10$
$x_2 \le 15$
$x_1, x_2 \in \mathbb{Z}_{\ge 0}$

**Solution:**
To maximize $Z$, we set $x_1$ and $x_2$ to their maximum values.
$x_1 = 10$
$x_2 = 15$
Total Pilots $Z = 5(10) + 5(15) = 50 + 75 = 125$.

The maximum number of trained pilots available by the end of year 2 is **125**.