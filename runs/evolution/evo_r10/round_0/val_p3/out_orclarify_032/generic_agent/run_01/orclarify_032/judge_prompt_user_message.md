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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products (each requiring one unit of each component), maximize total component output, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products. Each product requires one unit of each of the three components, so the goal is to produce the components in a balanced way to assemble as many complete products as possible.

## Turn 2 - Generic Agent

QUESTION: Can a workshop produce more than one component type simultaneously (i.e., split its hours across components), or must each workshop be dedicated to producing only a single component?

## Turn 2 - User Simulator

A workshop can split its hours across the three components. The only requirement is that the total hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities of each component required to be whole numbers (integer units), or can they be fractional?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the integrality point is still being confirmed internally, should I proceed by modeling the component quantities as continuous (allowing fractional units) for now, so the plan can be adjusted later if whole numbers turn out to be required?

## Turn 4 - User Simulator

Yes, proceed by modeling the component quantities as continuous for now.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize the number of complete products, where each product requires exactly one unit of each of the three components. The number of complete products equals the minimum of the three total component outputs.
- **Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of hours allocated to that component.
- **Production rates (units/hour):**
  - Workshop A: 10 (C1), 15 (C2), 5 (C3)
  - Workshop B: 15 (C1), 10 (C2), 5 (C3)
  - Workshop C: 20 (C1), 5 (C2), 10 (C3)
  - Workshop D: 10 (C1), 15 (C2), 20 (C3)
- **Capacity constraints:** For each workshop, the sum of hours allocated to the three components must not exceed its capacity (A: 100, B: 150, C: 80, D: 200).
- **Splitting allowed:** A workshop may divide its hours across any combination of the three components.
- **Integrality:** Component quantities are modeled as continuous (fractional units allowed) for now; this can be tightened to integers later if required.
- **Balancing:** The objective is to balance the three component outputs so that the minimum of the three totals is maximized.