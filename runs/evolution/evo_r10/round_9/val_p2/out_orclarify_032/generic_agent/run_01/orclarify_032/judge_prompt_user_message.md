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

QUESTION: What is the objective of this production plan — for example, maximize the total number of complete products (each requiring one of each component), maximize total component output, or minimize total production hours — and is there a demand or minimum quantity of complete products that must be met?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products. Each product requires one unit of each of the three components. There is no demand or minimum quantity of complete products that must be met.

## Turn 2 - Generic Agent

QUESTION: Are there any limits on how many units of each component can be produced (such as maximum demand per component, storage capacity, or a cap on total units), or can each component be produced in unlimited quantities as long as workshop hours are available?

## Turn 2 - User Simulator

There are no limits on how many units of each component can be produced. Components can be produced in unlimited quantities as long as workshop hours are available.

## Turn 3 - Generic Agent

QUESTION: Can a single workshop split its available hours across multiple components (i.e., divide its capacity among the three components as needed), or is each workshop dedicated to producing only one specific component?

## Turn 3 - User Simulator

A single workshop can split its available hours across multiple components. Each workshop can divide its capacity among the three components as needed.

## Turn 4 - Generic Agent

QUESTION: Are the production rates in the table (units per hour) constant regardless of how many hours a workshop allocates to a component, and can a workshop produce a fractional number of units of a component (e.g., 2.5 units), or must component output be in whole units?

## Turn 4 - User Simulator

The production rates in the table are constant regardless of how many hours a workshop allocates to a component. A workshop can produce a fractional number of units of a component.

## Turn 5 - Generic Agent

QUESTION: Are the workshop production capacities (100, 150, 80, 200 hours) hard upper limits that must not be exceeded, or are they targets that could potentially be exceeded if needed?

## Turn 5 - User Simulator

The workshop production capacities are hard upper limits that must not be exceeded.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the number of completed products, where each completed product requires exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3.
- **Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of hours allocated to that component. These are continuous, non-negative variables (fractional hours and fractional units are allowed).
- **Production rates:** Constant, as given in the table (units per hour):
  - Workshop A: 10 (C1), 15 (C2), 5 (C3)
  - Workshop B: 15 (C1), 10 (C2), 5 (C3)
  - Workshop C: 20 (C1), 5 (C2), 10 (C3)
  - Workshop D: 10 (C1), 15 (C2), 20 (C3)
- **Capacity constraints:** Each workshop's total hours allocated across the three components must not exceed its capacity (A: 100, B: 150, C: 80, D: 200). These are hard upper limits.
- **Workshop flexibility:** Each workshop can split its hours arbitrarily among the three components.
- **No other limits:** No demand, no minimum production, no per-component caps, no storage limits. Components can be produced in unlimited quantities subject only to workshop hours.
- **Completion coupling:** The number of completed products equals the minimum of the total units produced of Component 1, Component 2, and Component 3.