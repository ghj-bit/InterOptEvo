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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products (each requiring one of each component) that can be assembled, maximize total profit given some per-unit values, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled. Each complete product requires one unit of Component 1, one unit of Component 2, and one unit of Component 3.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum production requirements or demand targets for the components or complete products, or is the only constraint the workshop capacity (i.e., we simply produce as much as we can within the available hours)?

## Turn 2 - User Simulator

There are no minimum production requirements or demand targets. The only constraint is that the total hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 3 - Generic Agent

QUESTION: Can a workshop produce all three components, or is each workshop restricted to producing only certain components (i.e., are all 12 workshop-component combinations allowed)?

## Turn 3 - User Simulator

All 12 workshop-component combinations are allowed. Each of the four workshops can produce all three components.

## Turn 4 - Generic Agent

QUESTION: Can the number of units produced by each workshop for each component be any non-negative real number, or must they be whole numbers (integers)?

## Turn 4 - User Simulator

The number of units produced by each workshop for each component can be any non-negative real number.

## Turn 5 - Generic Agent

QUESTION: When computing the number of complete products, is it simply the minimum of the total units of Component 1, Component 2, and Component 3 produced across all workshops (i.e., we can only assemble as many complete products as the scarcest component allows)?

## Turn 5 - User Simulator

Yes, the number of complete products is the minimum of the total units of Component 1, Component 2, and Component 3 produced across all workshops.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many complete products can be assembled or sold, or is there no upper bound on the number of complete products we can produce (other than what the workshop capacities allow)?

## Turn 6 - User Simulator

There is no upper bound on the number of complete products other than what the workshop capacities allow.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as setup times, minimum batch sizes, or any other business rules that would affect the production plan?

## Turn 7 - User Simulator

No, there are no other constraints or considerations. The only constraint is that the total hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Objective:** Maximize the number of complete products that can be assembled.
- **Complete product definition:** Each complete product requires exactly 1 unit of Component 1, 1 unit of Component 2, and 1 unit of Component 3.
- **Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of units produced (non-negative real numbers).
- **Production rates:** Each workshop has a specific production rate (units/hour) for each component, as given in the table.
- **Constraints:** For each workshop, the total hours spent producing all three components must not exceed that workshop's production capacity (hours).
  - Workshop A: 100 hours
  - Workshop B: 150 hours
  - Workshop C: 80 hours
  - Workshop D: 200 hours
- **Complete products:** The number of complete products is the minimum of the total units of Component 1, Component 2, and Component 3 produced across all workshops.
- **No other constraints:** No minimum production requirements, no demand targets, no upper bounds on complete products, no setup times, no batch size requirements, and all 12 workshop-component combinations are allowed.