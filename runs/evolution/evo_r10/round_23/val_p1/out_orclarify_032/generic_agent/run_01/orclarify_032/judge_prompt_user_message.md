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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products that can be assembled, minimize total production cost, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled.

## Turn 2 - Generic Agent

QUESTION: Is there a demand limit or target number of complete products to produce, or should the plan simply produce as many complete products as the workshop capacities allow?

## Turn 2 - User Simulator

There is no demand limit or target number. The plan should produce as many complete products as the workshop capacities allow.

## Turn 3 - Generic Agent

QUESTION: Each complete product requires exactly one unit of each of the three components, correct?

## Turn 3 - User Simulator

Yes, each complete product requires exactly one unit of each of the three components.

## Turn 4 - Generic Agent

QUESTION: If a workshop produces more of one component than is needed for the complete products, is that excess simply wasted (i.e., only the matched minimum across components counts), or is there some other treatment for leftover components?

## Turn 4 - User Simulator

The excess is simply wasted; only the matched minimum across the three components counts toward the number of complete products.

## Turn 5 - Generic Agent

QUESTION: Can a single workshop produce more than one of the three components simultaneously (i.e., split its available hours across multiple components), or is each workshop dedicated to producing only one component?

## Turn 5 - User Simulator

A single workshop can split its available hours across multiple components.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as minimum production quantities per component, setup times, or costs associated with production?

## Turn 6 - User Simulator

No, there are no other constraints or considerations. The only constraint is that the total hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the number of complete products assembled.
- **Product structure:** Each complete product requires exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3.
- **Workshops:** Four workshops (A, B, C, D), each with a fixed production capacity in hours.
- **Production rates:** Each workshop has a specific production rate (units/hour) for each of the three components, as given in the table.
- **Flexibility:** A workshop can split its available hours across any combination of the three components.
- **Constraint:** For each workshop, the total hours allocated to all three components must not exceed its production capacity.
- **Excess handling:** Any component produced in excess of the matched minimum is wasted; only the minimum of the three total component outputs determines the number of complete products.
- **No other constraints:** No demand limits, no minimum production quantities, no setup times, no costs.

The model will have decision variables for the hours each workshop allocates to each component, constraints enforcing capacity limits per workshop, and an objective that maximizes the number of complete products (the minimum of the total units produced across the three components).