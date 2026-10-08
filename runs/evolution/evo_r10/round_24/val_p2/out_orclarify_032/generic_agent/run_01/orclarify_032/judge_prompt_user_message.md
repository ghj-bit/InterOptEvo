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

QUESTION: What is the objective of this production plan — for example, maximize the total number of complete products (limited by the smallest component count), maximize total component output, or minimize total production hours used?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products. Each product requires one unit of each of the three components, so the goal is to produce the components in a balanced way to assemble as many complete products as possible.

## Turn 2 - Generic Agent

QUESTION: Is there a demand limit on how many complete products you can sell or use, or is the only limit the workshops' production capacities (i.e., produce as many complete products as the capacities allow)?

## Turn 2 - User Simulator

The only limit is the workshops' production capacities. There is no demand limit; the goal is to produce as many complete products as the capacities allow.

## Turn 3 - Generic Agent

QUESTION: Can a workshop split its hours across all three components (producing fractional amounts of each), or must each workshop be dedicated to producing only one component?

## Turn 3 - User Simulator

A workshop can split its hours across all three components.

## Turn 4 - Generic Agent

QUESTION: Do the production rates mean that, for example, workshop A produces 10 units of Component 1 per hour (so 100 hours yields up to 1000 units of Component 1), i.e., the rate is units of that component per hour of that workshop?

## Turn 4 - User Simulator

Yes, the production rates mean that, for example, workshop A produces 10 units of Component 1 per hour.

## Turn 5 - Generic Agent

QUESTION: Can the number of units of each component produced be fractional, or must they be whole numbers (integers)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: If a workshop produces more of one component than the number of complete products assembled, is that extra component simply left over (unused), or must production be balanced so no component is produced in excess?

## Turn 6 - User Simulator

The extra component is simply left over (unused).

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or costs I should account for — such as a minimum production requirement for any component, a fixed setup cost per workshop, or a limit on how many workshops can be used — or is the model fully described by the four workshops' hour capacities and the production rates?

## Turn 7 - User Simulator

The model is fully described by the four workshops' hour capacities and the production rates. There are no other constraints or costs to account for.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the number of complete products assembled, where each product requires exactly one unit of each of the three components.
- **Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of hours allocated to that component.
- **Capacity constraints:** For each workshop, the sum of hours allocated to the three components must not exceed its production capacity (A: 100, B: 150, C: 80, D: 200 hours).
- **Production:** A workshop can split its hours across all three components. The number of units of a component produced by a workshop equals its hours on that component times the corresponding production rate (e.g., workshop A produces 10 units of Component 1 per hour).
- **Assembly:** The number of complete products is limited by the smallest total component count across the three components (each product uses one of each).
- **Leftover:** Any component produced in excess of the assembled products is simply left over (unused); no balancing or no-excess requirement.
- **No other constraints:** No demand limit, no minimum production, no setup costs, no limit on the number of workshops used.
- **Integrality:** Whether component units must be whole numbers is still pending internal confirmation; I will note this as an open item and can provide both a continuous and an integer version if needed.