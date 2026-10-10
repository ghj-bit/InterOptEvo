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

QUESTION: What is the specific objective of this production plan, such as maximizing total profit, maximizing total units produced, or minimizing total production cost?

## Turn 1 - User Simulator

The specific objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Are the production rates in the table (e.g., 10 units/hour for Component 1 in Workshop A) the number of units produced per hour, or are they the hours required to produce one unit?

## Turn 2 - User Simulator

The production rates are the number of units produced per hour.

## Turn 3 - Generic Agent

QUESTION: Is there a specific demand or maximum limit for the total number of completed products that can be sold or used?

## Turn 3 - User Simulator

There is no specific demand or maximum limit for the total number of completed products.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum production requirements for each component or workshop that must be met regardless of the total product count?

## Turn 4 - User Simulator

No, there are no minimum production requirements for each component or workshop.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or requirements, such as fixed setup costs, labor availability limits, or specific ratios between components, that are not already captured by the workshop capacity and production rates?

## Turn 5 - User Simulator

No, there are no other constraints or requirements beyond the workshop capacity limits and the production rates already provided.

## Turn 6 - Generic Agent

READY_TO_MODEL
I have gathered all necessary information to formulate the production planning model. Here is the summary of the confirmed understanding:

**Objective:**
*   **Maximize** the total number of completed products.
*   A "completed product" consists of exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3.

**Decision Variables:**
*   Let $x_{ij}$ be the number of hours allocated by Workshop $i$ to produce Component $j$.
*   Workshops $i \in \{A, B, C, D\}$.
*   Components $j \in \{1, 2, 3\}$.
*   All variables are continuous and non-negative.

**Parameters (Confirmed):**
*   **Production Capacities (Hours):**
    *   Workshop A: 100 hours
    *   Workshop B: 150 hours
    *   Workshop C: 80 hours
    *   Workshop D: 200 hours
*   **Production Rates (Units per Hour):**
    *   Workshop A: Comp 1 = 10, Comp 2 = 15, Comp 3 = 5
    *   Workshop B: Comp 1 = 15, Comp 2 = 10, Comp 3 = 5
    *   Workshop C: Comp 1 = 20, Comp 2 = 5, Comp 3 = 10
    *   Workshop D: Comp 1 = 10, Comp 2 = 15, Comp 3 = 20

**Constraints:**
1.  **Workshop Capacity Constraints:** For each workshop $i$, the sum of hours allocated to all three components must not exceed its total capacity.
    *   $\sum_{j=1}^{3} x_{ij} \leq \text{Capacity}_i$
2.  **Product Balance Constraints:** The number of completed products is limited by the minimum of the total units produced for each component type. To maximize completed products $P$, we require:
    *   Total Units of Component 1 $\geq P$
    *   Total Units of Component 2 $\geq P$
    *   Total Units of Component 3 $\geq P$
    *   Where Total Units of Component $j = \sum_{i \in \{A,B,C,D\}} (\text{Rate}_{ij} \times x_{ij})$

**Assumptions:**
*   There are no minimum production requirements for any component or workshop.
*   There are no upper bounds on the number of completed products (demand is unlimited).
*   There are no other constraints (e.g., setup costs, labor limits, or specific ratios) beyond those specified.
*   Production rates are constant and linear.