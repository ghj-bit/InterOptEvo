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

QUESTION: What is the specific objective of this production plan, such as maximizing total profit, minimizing total cost, or meeting a specific demand target?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum production requirements for each individual component, or can the production of any component be zero?

## Turn 2 - User Simulator

There are no minimum production requirements for any individual component.

## Turn 3 - Generic Agent

QUESTION: Is the production rate constant regardless of the number of units produced, meaning there are no setup times or batch size constraints?

## Turn 3 - User Simulator

Yes, the production rate is constant regardless of the number of units produced.

## Turn 4 - Generic Agent

QUESTION: Can the production quantities for each component be fractional, or must they be whole numbers?

## Turn 4 - User Simulator

The production quantities can be fractional.

## Turn 5 - Generic Agent

READY_TO_MODEL
I have gathered all the necessary details to formulate the production planning model. Here is the confirmed understanding:

**Objective:**
Maximize the number of completed products. Since each product consists of exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3, the number of completed products is determined by the minimum of the total production quantities of the three components.

**Decision Variables:**
Let $x_{ij}$ be the number of units of Component $j$ produced by Workshop $i$, where $i \in \{A, B, C, D\}$ and $j \in \{1, 2, 3\}$.
Let $P$ be the number of completed products.

**Constraints:**
1.  **Workshop Capacity Constraints:** The total hours used by each workshop must not exceed its capacity.
    *   Workshop A: $\frac{x_{A1}}{10} + \frac{x_{A2}}{15} + \frac{x_{A3}}{5} \le 100$
    *   Workshop B: $\frac{x_{B1}}{15} + \frac{x_{B2}}{10} + \frac{x_{B3}}{5} \le 150$
    *   Workshop C: $\frac{x_{C1}}{20} + \frac{x_{C2}}{5} + \frac{x_{C3}}{10} \le 80$
    *   Workshop D: $\frac{x_{D1}}{10} + \frac{x_{D2}}{15} + \frac{x_{D3}}{20} \le 200$

2.  **Product Assembly Constraints:** The number of completed products $P$ cannot exceed the total production of any single component.
    *   $P \le \sum_{i \in \{A,B,C,D\}} x_{i1}$
    *   $P \le \sum_{i \in \{A,B,C,D\}} x_{i2}$
    *   $P \le \sum_{i \in \{A,B,C,D\}} x_{i3}$

3.  **Non-negativity:**
    *   $x_{ij} \ge 0$ for all $i, j$
    *   $P \ge 0$

**Assumptions:**
*   Production rates are constant.
*   Fractional production quantities are allowed.
*   There are no minimum production requirements for individual components.