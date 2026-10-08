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

QUESTION: What is the objective of this production plan — for example, maximize total number of complete products produced, minimize total production cost, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: How are complete products assembled from the three components — does one complete product require exactly one unit of each of Component 1, Component 2, and Component 3?

## Turn 2 - User Simulator

Yes, one complete product requires exactly one unit of each of Component 1, Component 2, and Component 3.

## Turn 3 - Generic Agent

QUESTION: Can a workshop produce all three components, or is each workshop restricted to producing only certain components?

## Turn 3 - User Simulator

Each workshop can produce all three components.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum production requirements or demand targets for each component or for the final product?

## Turn 4 - User Simulator

No, there are no minimum production requirements or demand targets.

## Turn 5 - Generic Agent

QUESTION: Are there any constraints on the total number of units of each component that can be produced, such as maximum limits or availability of raw materials?

## Turn 5 - User Simulator

No, there are no constraints on the total number of units of each component beyond the workshop production capacity limits.

## Turn 6 - Generic Agent

QUESTION: Should the number of units produced of each component be restricted to whole numbers (integers), or can they be fractional?

## Turn 6 - User Simulator

The number of units produced of each component should be restricted to whole numbers (integers).

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as setup times, sequencing requirements, or quality constraints?

## Turn 7 - User Simulator

No, there are no other constraints or considerations beyond the workshop production capacity limits.

## Turn 8 - Generic Agent

READY_TO_MODEL

I have confirmed the following understanding:

1. **Objective**: Maximize the number of complete products produced.
2. **Product structure**: One complete product requires exactly one unit of each of Component 1, Component 2, and Component 3.
3. **Workshops**: Four workshops (A, B, C, D) can each produce all three components.
4. **Production rates**: Each workshop has specific production rates (units/hour) for each component, as given in the table.
5. **Capacity constraints**: Each workshop has a limited number of production hours (A: 100, B: 150, C: 80, D: 200), and the total hours allocated to all three components by each workshop must not exceed its capacity.
6. **No other constraints**: No minimum production requirements, no demand targets, no raw material limits, no setup times, no sequencing requirements, and no quality constraints.
7. **Integrality**: The number of units produced of each component must be whole numbers (integers).

The model will allocate production hours from each workshop to the three components to maximize the number of complete products, subject to the workshop capacity constraints and the requirement that complete products require one unit of each component.