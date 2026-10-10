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

QUESTION: What is the specific objective of the production plan, such as maximizing total profit, maximizing total units produced, or meeting a specific demand level?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum production requirements or demand constraints for each of the three components?

## Turn 2 - User Simulator

No, there are no minimum production requirements or demand constraints for the components.

## Turn 3 - Generic Agent

QUESTION: Is there a fixed ratio of components required to assemble one completed product, such as one unit of each component per product?

## Turn 3 - User Simulator

Yes, one completed product requires one unit of each of the three components.

## Turn 4 - Generic Agent

QUESTION: Are there any costs associated with producing the components or any other financial constraints to consider?

## Turn 4 - User Simulator

No, there are no costs or financial constraints to consider.

## Turn 5 - Generic Agent

READY_TO_MODEL

I have confirmed the following understanding for the production planning model:

1.  **Objective**: Maximize the number of completed products.
2.  **Product Definition**: One completed product requires exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3.
3.  **Resources**: Four workshops (A, B, C, D) with fixed production capacities (100, 150, 80, and 200 hours, respectively).
4.  **Constraints**:
    *   The total hours allocated by each workshop to produce all three components must not exceed its capacity.
    *   There are no minimum production requirements or demand constraints for individual components.
    *   There are no costs or financial constraints.
5.  **Data**: The production rates (units per hour) for each component in each workshop are as provided in the table.

The model will determine the optimal allocation of production hours across the workshops and components to maximize the minimum of the total units produced for each of the three components, as that minimum value represents the number of complete products that can be assembled.