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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products you can assemble, minimize total production hours used, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products you can assemble.

## Turn 2 - Generic Agent

QUESTION: Is there a demand or target number of complete products that must be met, or is there no upper limit on how many products you want to produce?

## Turn 2 - User Simulator

There is no demand or target number that must be met, and there is no upper limit on how many products we want to produce.

## Turn 3 - Generic Agent

QUESTION: Does each complete product require exactly one unit of each of the three components, or are the component quantities per product different?

## Turn 3 - User Simulator

Each complete product requires exactly one unit of each of the three components.

## Turn 4 - Generic Agent

QUESTION: Can a single workshop produce all three components, or is each workshop restricted to producing only one specific component?

## Turn 4 - User Simulator

A single workshop can produce all three components.

## Turn 5 - Generic Agent

QUESTION: Are the production rates in the table fixed for each workshop-component pair, or can a workshop choose to produce a component at a different rate?

## Turn 5 - User Simulator

The production rates in the table are fixed for each workshop-component pair.

## Turn 6 - Generic Agent

QUESTION: Are the production capacities in the table hard limits that must not be exceeded, or are they soft limits that can be exceeded at some cost?

## Turn 6 - User Simulator

The production capacities in the table are hard limits that must not be exceeded.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total number of units of each component that can be produced, or is the only constraint the workshop capacity?

## Turn 7 - User Simulator

The only constraint is the workshop capacity.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or considerations I should know about, such as minimum production requirements, setup times, or component storage limits?

## Turn 8 - User Simulator

No, there are no other constraints or considerations.

## Turn 9 - Generic Agent

READY_TO_MODEL

I understand the problem as follows:

- **Objective**: Maximize the number of complete products that can be assembled.
- **Product structure**: Each complete product requires exactly one unit of each of the three components.
- **Workshops**: Four workshops (A, B, C, D), each with a fixed production capacity in hours.
- **Production rates**: Fixed rates (units/hour) for each workshop-component pair, as given in the table.
- **Constraints**:
  - Each workshop's total hours allocated to the three components must not exceed its production capacity (hard limit).
  - No other constraints (no demand targets, no minimum production, no setup times, no storage limits).
- **Decision variables**: The number of hours each workshop allocates to each component (or equivalently, the number of units of each component produced by each workshop).
- **Key relationship**: The number of complete products is limited by the minimum of the total units produced of each of the three components (since one unit of each is needed per product).