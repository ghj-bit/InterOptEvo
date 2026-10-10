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

QUESTION: What is the objective of this production plan — are we maximizing total units of a finished product, maximizing profit, or meeting a specific demand target?

## Turn 1 - User Simulator

We are maximizing the number of completed products. Each product requires one unit of each of the three components, so the goal is to produce the components in a balanced way to assemble as many complete products as possible.

## Turn 2 - Generic Agent

QUESTION: Are the production rates in the table (e.g., 10 units/hour for Component 1 in Workshop A) the number of units produced per hour, or the number of hours required to produce one unit?

## Turn 2 - User Simulator

The production rates in the table are the number of units produced per hour.

## Turn 3 - Generic Agent

QUESTION: Are there any other constraints or requirements beyond the workshop capacity limits, such as minimum production quantities, setup times, or limits on how many workshops can produce a specific component?

## Turn 3 - User Simulator

No, the only constraint is that the total number of hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 4 - Generic Agent

QUESTION: Can a single workshop produce multiple different components simultaneously, or is each workshop dedicated to producing only one component at a time?

## Turn 4 - User Simulator

A single workshop can produce multiple different components. The constraint is simply that the total hours allocated by each workshop to all three components combined must not exceed its production capacity.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities for each component required to be whole numbers, or can they be fractional?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Should the production quantities be treated as continuous values (allowing fractions) or must they be integers?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the number of completed products.
2.  **Product Definition:** Each completed product requires exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3.
3.  **Decision Variables:** The number of units of each component (1, 2, and 3) produced by each workshop (A, B, C, and D).
4.  **Production Rates:** The values in the table represent units produced per hour.
5.  **Constraints:**
    *   For each workshop, the sum of hours allocated to all three components must not exceed the workshop's total production capacity.
    *   Hours allocated to a specific component = (Units of that component produced) / (Production rate for that component in that workshop).
    *   Workshops can produce multiple components simultaneously; the only limit is the total hours.
    *   There are no other constraints (no minimums, setup times, or exclusivity rules).

**Assumptions (Unconfirmed):**
1.  **Variable Domain:** It is assumed that production quantities can be **continuous** (fractional units are allowed). If integer constraints are required, the model would need to be adjusted to an Integer Linear Program.
2.  **Non-negativity:** It is assumed that production quantities cannot be negative (standard assumption).

**Model Formulation:**

Let $x_{ij}$ be the number of units of component $j$ produced by workshop $i$.
Let $P_i$ be the production capacity (hours) of workshop $i$.
Let $r_{ij}$ be the production rate (units/hour) of component $j$ in workshop $i$.

**Objective Function:**
Maximize $Z$, where $Z$ is the number of completed products.
Since each product requires 1 unit of each component, $Z$ is limited by the total production of each component type.
$Z \le \sum_{i} x_{i1}$
$Z \le \sum_{i} x_{i2}$
$Z \le \sum_{i} x_{i3}$
Maximize $Z$

**Constraints:**
For each workshop $i \in \{A, B, C, D\}$:
$\frac{x_{i1}}{r_{i1}} + \frac{x_{i2}}{r_{i2}} + \frac{x_{i3}}{r_{i3}} \le P_i$

Specifically:
*   **Workshop A:** $\frac{x_{A1}}{10} + \frac{x_{A2}}{15} + \frac{x_{A3}}{5} \le 100$
*   **Workshop B:** $\frac{x_{B1}}{15} + \frac{x_{B2}}{10} + \frac{x_{B3}}{5} \le 150$
*   **Workshop C:** $\frac{x_{C1}}{20} + \frac{x_{C2}}{5} + \frac{x_{C3}}{10} \le 80$
*   **Workshop D:** $\frac{x_{D1}}{10} + \frac{x_{D2}}{15} + \frac{x_{D3}}{20} \le 200$

**Non-negativity:**
$x_{ij} \ge 0$ for all $i, j$.
$Z \ge 0$.