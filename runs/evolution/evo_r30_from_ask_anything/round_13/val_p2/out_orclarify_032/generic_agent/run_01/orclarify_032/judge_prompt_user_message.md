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

QUESTION: What is the objective of this production plan: maximize total profit, maximize total units produced, or minimize total production cost?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Is the production rate in the table the number of component units produced per hour, or is it the number of hours required to produce one unit?

## Turn 2 - User Simulator

The production rate is the number of component units produced per hour.

## Turn 3 - Generic Agent

QUESTION: How many units of each component are required to assemble one completed product?

## Turn 3 - User Simulator

One unit of each of the three components is required to assemble one completed product.

## Turn 4 - Generic Agent

QUESTION: Can a workshop produce all three components, or is each workshop restricted to producing only specific components?

## Turn 4 - User Simulator

Each workshop can produce all three components.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or requirements for the production plan, such as minimum production levels, demand limits, or setup times?

## Turn 5 - User Simulator

No, the only constraint is that the total number of hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the number of completed products.
2.  **Product Composition:** One completed product requires exactly 1 unit of Component 1, 1 unit of Component 2, and 1 unit of Component 3.
3.  **Decision Variables:** The number of hours allocated by each of the four workshops (A, B, C, D) to each of the three components (1, 2, 3).
4.  **Variable Domain:** Continuous, non-negative hours. (Assumption: Production can be fractional; if integer units are required, the model would need integer constraints on the final component counts, but typically hours are continuous in LP formulations).
5.  **Production Rates:** The table values represent the number of component units produced per hour.
    *   Workshop A: 10 units/hr (C1), 15 units/hr (C2), 5 units/hr (C3)
    *   Workshop B: 15 units/hr (C1), 10 units/hr (C2), 5 units/hr (C3)
    *   Workshop C: 20 units/hr (C1), 5 units/hr (C2), 10 units/hr (C3)
    *   Workshop D: 10 units/hr (C1), 15 units/hr (C2), 20 units/hr (C3)
6.  **Constraints:**
    *   **Capacity:** For each workshop, the sum of hours allocated to all three components must not exceed the workshop's total production capacity.
        *   Workshop A: $\le 100$ hours
        *   Workshop B: $\le 150$ hours
        *   Workshop C: $\le 80$ hours
        *   Workshop D: $\le 200$ hours
    *   **Balance:** The total units of Component 1 produced must equal the total units of Component 2 produced, which must equal the total units of Component 3 produced (since 1:1:1 ratio is required for a completed product).
7.  **Assumptions:**
    *   There are no demand limits or minimum production requirements.
    *   There are no setup times or fixed costs.
    *   Workshops can produce any combination of the three components.
    *   Production hours are continuous variables.