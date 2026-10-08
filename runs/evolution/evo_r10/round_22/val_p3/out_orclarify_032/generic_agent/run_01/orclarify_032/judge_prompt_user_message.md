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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products (each requiring one of each component) that can be produced, minimize total production hours used, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products. Each product requires one unit of each of the three components, so the goal is to produce the components in a balanced way to assemble as many complete products as possible.

## Turn 2 - Generic Agent

QUESTION: Are there any demand limits or minimum production requirements for the components, or is the only constraint the workshop capacity (i.e., we can produce as many components as the workshops allow, up to what's needed for complete products)?

## Turn 2 - User Simulator

The only constraint is the workshop capacity. There are no demand limits or minimum production requirements for the components.

## Turn 3 - Generic Agent

QUESTION: Can a workshop split its available hours across multiple components (e.g., Workshop A uses 40 hours on Component 1 and 60 hours on Component 2), or must each workshop dedicate all its hours to a single component?

## Turn 3 - User Simulator

A workshop can split its available hours across multiple components.

## Turn 4 - Generic Agent

QUESTION: Are the production rates constant regardless of how many hours a workshop spends on a component (i.e., linear: units = rate × hours), or are there any setup times, batch requirements, or other nonlinear effects I should account for?

## Turn 4 - User Simulator

The production rates are constant. Units produced equal the rate multiplied by the hours spent. There are no setup times, batch requirements, or other nonlinear effects.

## Turn 5 - Generic Agent

QUESTION: Do the hours spent on each component need to be whole numbers, or can they be fractional (e.g., 12.5 hours)?

## Turn 5 - User Simulator

The hours spent on each component can be fractional.

## Turn 6 - Generic Agent

QUESTION: Do the final number of complete products need to be a whole number, or is it acceptable for the model to report a fractional value (e.g., 123.4 products)?

## Turn 6 - User Simulator

The final number of complete products needs to be a whole number.

## Turn 7 - Generic Agent

QUESTION: If the model produces, say, 123.4 complete products, should I round down to 123 (i.e., only count fully assembled products), or is there any other way you'd like the final integer value determined?

## Turn 7 - User Simulator

Round down to 123. Only count fully assembled products.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or considerations I should account for — such as labor availability, raw material limits, or a time horizon — or is the model fully defined by the four workshop capacities, the production rates, and the requirement that each complete product uses one unit of each component?

## Turn 8 - User Simulator

No, there are no other constraints or considerations. The model is fully defined by the four workshop capacities, the production rates, and the requirement that each complete product uses one unit of each component.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the number of complete products (each requiring exactly one unit of Component 1, one unit of Component 2, and one unit of Component 3). The final answer must be a whole number (round down).

**Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of hours allocated. Hours can be fractional.

**Parameters:**
- Workshop capacities: A = 100 hrs, B = 150 hrs, C = 80 hrs, D = 200 hrs
- Production rates (units/hour):
  - Workshop A: C1 = 10, C2 = 15, C3 = 5
  - Workshop B: C1 = 15, C2 = 10, C3 = 5
  - Workshop C: C1 = 20, C2 = 5, C3 = 10
  - Workshop D: C1 = 10, C2 = 15, C3 = 20

**Constraints:**
1. For each workshop, the sum of hours allocated to the three components ≤ its capacity.
2. For each component, total units produced across all workshops ≥ number of complete products (so that enough of each component exists to assemble the products).
3. Number of complete products is a non-negative integer.

**No other constraints:** No demand limits, no minimum production, no setup times, no batch requirements, no raw material limits, no time horizon. Production is linear (units = rate × hours). Workshops can split hours freely across components.