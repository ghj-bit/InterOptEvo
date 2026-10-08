# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U2
I need help planning production. A product consists of three components produced by four workshops, each with a limited number of production hours, and the total number of hours allocated by each workshop to the three components must not exceed its production capacity.

Table 1.4

| Workshop | Production Capacity (hours) | Production Rate (units/hour) |   |   |
| :------: | :-------------------------: | :--------------------------: | - | - |
|          |                             | Component 1 | Component 2  | Component 3 |
|    A     |           100               |      10      |      15     |      5      |
|    B     |           150               |      15      |      10     |      5      |
|    C     |           80                |      20      |      5      |      10     |
|    D     |           200               |      10      |      15     |      20     |

## Problem units
- U1 (context): I need help planning production. A product consists of three components produced by four workshops, each with a limited number of production hours.
- U2 (data): Table 1.4

| Workshop | Production Capacity (hours) | Production Rate (units/hour) |   |   |
| :------: | :-------------------------: | :--------------------------: | - | - |
|          |                             | Component 1 | Component 2  | Component 3 |
|    A     |           100               |      10      |      15     |      5      |
|    B     |           150               |      15      |      10     |      5      |
|    C     |           80                |      20      |      5      |      10     |
|    D     |           200               |      10      |      15     |      20     |
- U3 (objective): Maximize the number of completed products.
- U4 (constraint): The total number of hours allocated by each workshop to the three components must not exceed its production capacity.

## Hidden slot scoring rules
## H1: unknown_objective
- Severity: P0
- Severity reason: Without the objective, the problem is ill-posed. The agent cannot formulate a linear program because there is no function to optimize, making the entire model meaningless.
- Problem unit ID: U3
- Semantic hit rule: The agent must ask a question that explicitly inquires about the optimization objective, such as what to maximize or minimize, and the response must indicate it is about the number of completed products.
- Reference acceptable questions:
  - What is the goal of the optimization? Are we trying to maximize the number of complete products assembled from the three components?
  - Could you clarify the objective? Is it to maximize the total number of products that can be fully assembled?
- Failure modes:
  - Assuming the objective is to maximize total component production (e.g., sum of all components produced) without considering assembly into complete products.
  - Assuming the objective is to minimize production time or cost.
  - Assuming the objective is to maximize any of the components individually.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective of this production plan — for example, maximizing the number of complete products that can be assembled, minimizing total production hours used, or something else — and over what time horizon (e.g., a single period) does it apply?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled. Each product requires one unit of each of the three components. The plan applies to a single period.

## Turn 2 - Generic Agent

QUESTION: Are the production rates in the table (e.g., Workshop A produces 10 units/hour of Component 1) the same for every workshop-component pair, meaning each workshop can produce any component at the listed rate, or does each workshop only produce specific components?

## Turn 2 - User Simulator

Each workshop can produce any of the three components at the specific rate listed for that workshop-component pair in the table.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities of each component required to be whole numbers (integer units), or can they be fractional?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a minimum or target number of complete products that must be produced, or is the only requirement to maximize the number of complete products subject to the workshop capacity limits?

## Turn 4 - User Simulator

The only requirement is to maximize the number of complete products subject to the workshop capacity limits.

## Turn 5 - Generic Agent

QUESTION: If a workshop has leftover hours after allocating to the three components, is that simply allowed (i.e., hours need not be fully used), or is there any penalty or requirement to use all available hours?

## Turn 5 - User Simulator

Leftover hours are simply allowed. There is no penalty or requirement to use all available hours.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum production requirements for each component (e.g., at least X units of Component 1 must be produced), or can a component's production be zero if it doesn't help maximize complete products?

## Turn 6 - User Simulator

There are no minimum production requirements for each component. A component's production can be zero if it does not help maximize complete products.

## Turn 7 - Generic Agent

QUESTION: Regarding the production quantities, should they be treated as continuous (fractional units allowed) or must they be whole numbers (integer units)?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many units of a single component a given workshop can produce in the period, other than the total hours capacity constraint?

## Turn 8 - User Simulator

No, there is no limit on how many units of a single component a given workshop can produce other than the total hours capacity constraint.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements I haven't asked about yet, such as setup times, sequencing, or demand limits on the final products?

## Turn 9 - User Simulator

No, there are no other constraints or requirements beyond the workshop capacity limits and the objective to maximize the number of complete products.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the number of complete products assembled in a single period. Each complete product requires exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3.

- **Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of units produced. The number of complete products is determined by the minimum of the total available units of the three components.

- **Production rates (units/hour):**
  - Workshop A: C1=10, C2=15, C3=5; capacity=100 hours
  - Workshop B: C1=15, C2=10, C3=5; capacity=150 hours
  - Workshop C: C1=20, C2=5, C3=10; capacity=80 hours
  - Workshop D: C1=10, C2=15, C3=20; capacity=200 hours

- **Constraints:**
  - For each workshop, the total hours allocated to the three components must not exceed its production capacity.
  - No minimum production requirements for any component.
  - No per-component-per-workshop upper bound beyond the hours capacity.
  - Leftover hours are allowed (no requirement to fully utilize capacity).
  - No setup times, sequencing, or demand limits.

- **Integrality:** The client deferred confirmation on whether production quantities must be whole numbers. I will model with continuous (fractional) variables as the default, noting that if integer values are required, the model can be adjusted accordingly.