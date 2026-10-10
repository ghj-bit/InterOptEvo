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

QUESTION: What is the primary objective of the production plan, such as maximizing total profit, minimizing total cost, or meeting specific demand targets for each component?

## Turn 1 - User Simulator

The primary objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Are there specific minimum demand requirements for each of the three components that must be met, or is the only constraint that the number of completed products is limited by the smallest quantity of any single component produced?

## Turn 2 - User Simulator

There are no specific minimum demand requirements for each component. The number of completed products is limited by the smallest quantity of any single component produced, since each product requires one unit of each of the three components.

## Turn 3 - Generic Agent

QUESTION: Are there any other constraints on the production plan, such as maximum production limits for specific components or workshops, or are the only constraints the workshop hour capacities and the requirement that each completed product uses one unit of each component?

## Turn 3 - User Simulator

The only constraints are the workshop hour capacities and the requirement that each completed product uses one unit of each component.

## Turn 4 - Generic Agent

READY_TO_MODEL
I understand you want to maximize the number of completed products, where each product requires one unit of Component 1, one unit of Component 2, and one unit of Component 3. The production is distributed across four workshops (A, B, C, D), each with a fixed capacity in hours. The number of units of a specific component produced by a workshop is determined by the hours allocated to that component multiplied by the workshop's production rate for that component. The total hours allocated by each workshop to all three components cannot exceed its capacity. There are no other constraints, such as minimum demands or maximum production limits. The goal is to find the allocation of hours to components in each workshop that maximizes the minimum of the total quantities produced for the three components.