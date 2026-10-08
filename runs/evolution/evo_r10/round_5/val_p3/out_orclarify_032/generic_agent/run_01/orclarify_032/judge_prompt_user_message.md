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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products that can be assembled, minimize total production hours used, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled.

## Turn 2 - Generic Agent

QUESTION: Is there a required demand or minimum number of complete products that must be produced, or is the only goal to produce as many as the workshop capacities allow?

## Turn 2 - User Simulator

There is no required demand or minimum number of complete products. The only goal is to produce as many complete products as the workshop capacities allow.

## Turn 3 - Generic Agent

QUESTION: For each workshop, is the production rate for a component fixed (i.e., the workshop always produces that component at the listed units/hour), or can the rate vary within some range?

## Turn 3 - User Simulator

The production rate for each component at each workshop is fixed at the listed units/hour.

## Turn 4 - Generic Agent

QUESTION: Can a single workshop split its available hours among the three components (e.g., Workshop A spends 40 hours on Component 1 and 60 hours on Component 2), or is each workshop dedicated to producing only one component?

## Turn 4 - User Simulator

A single workshop can split its available hours among the three components.

## Turn 5 - Generic Agent

QUESTION: Are the production hours allocated to each component at each workshop required to be whole numbers, or can they be fractional (e.g., 12.5 hours)?

## Turn 5 - User Simulator

The production hours allocated to each component at each workshop can be fractional.

## Turn 6 - Generic Agent

QUESTION: When a workshop produces a component, must the number of units produced be a whole number, or can it be fractional (e.g., 12.5 units of Component 1)?

## Turn 6 - User Simulator

The number of units produced can be fractional.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how many units of each component can be produced (e.g., a maximum per component), or is the only limit the workshop capacity?

## Turn 7 - User Simulator

The only limit is the workshop capacity.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about, such as minimum production levels for any component, setup times, or costs?

## Turn 8 - User Simulator

No, there are no other constraints or requirements. The only constraint is that the total number of hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 9 - Generic Agent

READY_TO_MODEL

I have confirmed the following understanding:

**Objective:** Maximize the number of complete products that can be assembled.

**Decision Variables:**
- For each workshop (A, B, C, D) and each component (1, 2, 3), the number of hours allocated to produce that component at that workshop.
- These variables are continuous and non-negative (fractional hours are allowed).

**Constraints:**
- For each workshop, the sum of hours allocated to all three components must not exceed the workshop's production capacity.
- The number of units of each component produced is determined by: (hours allocated) × (production rate for that component at that workshop).
- The number of complete products is limited by the minimum of the total units produced across all workshops for each of the three components.

**Data:**
- Workshop capacities: A=100, B=150, C=80, D=200 hours
- Production rates (units/hour):
  - Workshop A: Component 1=10, Component 2=15, Component 3=5
  - Workshop B: Component 1=15, Component 2=10, Component 3=5
  - Workshop C: Component 1=20, Component 2=5, Component 3=10
  - Workshop D: Component 1=10, Component 2=15, Component 3=20

**No other constraints:** No minimum production levels, no setup times, no costs, no demand requirements, no integrality requirements.