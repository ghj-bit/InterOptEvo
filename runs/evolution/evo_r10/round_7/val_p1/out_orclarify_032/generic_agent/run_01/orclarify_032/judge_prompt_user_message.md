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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products (each requiring one unit of each of the three components), or maximize total profit given some per-component or per-product value?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products. Each product requires one unit of each of the three components.

## Turn 2 - Generic Agent

QUESTION: Are the production rates in the table (e.g., Workshop A makes 10 units/hour of Component 1) the number of units produced per hour, meaning the hours needed for a component equals its units divided by that rate?

## Turn 2 - User Simulator

Yes, the production rates are the number of units produced per hour. The hours needed for a component equals its units divided by that rate.

## Turn 3 - Generic Agent

QUESTION: Can a workshop split its available hours across all three components (i.e., produce any mix of the three components within its capacity), or is each workshop dedicated to producing only one specific component?

## Turn 3 - User Simulator

A workshop can split its available hours across all three components. Each workshop can produce any mix of the three components within its capacity.

## Turn 4 - Generic Agent

QUESTION: Do the component quantities have to be whole numbers (integer units), or can they be fractional?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how many units of each component can be produced (such as a maximum demand or a storage cap), or is the only limit the workshops' total production hours?

## Turn 5 - User Simulator

The only limit is the workshops' total production hours.

## Turn 6 - Generic Agent

QUESTION: If a workshop has leftover hours that it does not use for any component, is that simply allowed (unused hours are free), or is there any penalty or requirement to use all available hours?

## Turn 6 - User Simulator

Unused hours are simply allowed. There is no penalty or requirement to use all available hours.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize the number of complete products, where each product requires exactly one unit of each of the three components.
- **Production:** Four workshops (A, B, C, D), each with a fixed capacity in hours (A=100, B=150, C=80, D=200). Each workshop can produce any mix of the three components, splitting its hours freely among them.
- **Rates:** The table gives units produced per hour for each workshop-component pair (e.g., A makes 10 units/hour of Component 1). Hours consumed for a component = units produced ÷ that workshop's rate for that component.
- **Capacity constraint:** For each workshop, the sum of hours spent on the three components must not exceed its capacity.
- **No other limits:** There are no demand caps, storage limits, or per-component maximums; the only binding limits are the workshops' hours.
- **Unused hours:** Allowed, with no penalty or requirement to use all hours.
- **Integrality:** Whether component quantities must be whole numbers is still pending internal confirmation; I will treat them as continuous by default and note that an integer version is a straightforward variant.

The model will therefore have decision variables for the number of units of each component produced at each workshop, a capacity constraint per workshop, and an objective maximizing the minimum of the three total component outputs (the number of complete products).