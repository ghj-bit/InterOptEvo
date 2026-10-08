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

QUESTION: What is the objective of this production plan — for example, maximizing the number of complete products that can be assembled, minimizing the total production hours used, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled.

## Turn 2 - Generic Agent

QUESTION: For each component, can it be produced in any combination of the four workshops (with each workshop's hours on that component limited by its capacity), or is each component assigned to exactly one workshop?

## Turn 2 - User Simulator

Each component can be produced in any combination of the four workshops, subject to each workshop’s capacity limit.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many units of each component can be produced (such as demand or storage limits), or is the only limit the workshops' production hours?

## Turn 3 - User Simulator

The only limit is the workshops' production hours.

## Turn 4 - Generic Agent

QUESTION: Are the production rates in the table (units per hour) fixed constants, so that the number of units produced equals the hours allocated times the rate, and can the number of units produced be fractional or must it be whole units?

## Turn 4 - User Simulator

The production rates are fixed constants, and the number of units produced equals the hours allocated times the rate. The number of units produced can be fractional.

## Turn 5 - Generic Agent

QUESTION: Since a complete product needs one unit of each of the three components, is the number of complete products equal to the minimum of the three total component outputs, and can leftover (excess) components be produced freely without any penalty?

## Turn 5 - User Simulator

Yes, the number of complete products is equal to the minimum of the three total component outputs, and leftover components can be produced freely without any penalty.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize the number of complete products assembled, where one complete product requires one unit of each of the three components.
- **Production:** Each of the three components can be produced in any combination of the four workshops (A, B, C, D).
- **Rates:** Production rates (units/hour) are fixed constants as given in the table:
  - A: capacity 100 h; rates 10 (C1), 15 (C2), 5 (C3)
  - B: capacity 150 h; rates 15 (C1), 10 (C2), 5 (C3)
  - C: capacity 80 h; rates 20 (C1), 5 (C2), 10 (C3)
  - D: capacity 200 h; rates 10 (C1), 15 (C2), 20 (C3)
- **Output:** Units produced = hours allocated × rate; units may be fractional.
- **Capacity:** For each workshop, the sum of hours allocated to the three components must not exceed its production capacity.
- **No other limits:** No demand, storage, or per-component caps; the only constraint is workshop hours.
- **Objective measure:** Complete products = min(total C1, total C2, total C3); excess components are free (no penalty).

Model sketch: variables x_{w,c} = hours workshop w spends on component c (continuous, ≥ 0); capacity constraints Σ_c x_{w,c} ≤ cap_w; component outputs O_c = Σ_w rate_{w,c}·x_{w,c}; maximize P subject to P ≤ O_1, P ≤ O_2, P ≤ O_3.