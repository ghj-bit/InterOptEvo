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

QUESTION: What is the objective of this production plan — for example, maximize the total number of complete products produced, minimize the total production cost, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Is there a required demand or minimum number of completed products that must be met, or is there no demand constraint and we simply produce as many complete products as the workshops allow?

## Turn 2 - User Simulator

There is no demand constraint or minimum number of completed products that must be met. We simply produce as many complete products as the workshops allow.

## Turn 3 - Generic Agent

QUESTION: How many units of each component are needed to assemble one complete product — is it one unit of each of the three components per product, or are the ratios different?

## Turn 3 - User Simulator

One complete product requires one unit of each of the three components.

## Turn 4 - Generic Agent

QUESTION: Can a workshop split its production hours across multiple components (i.e., produce some of component 1 and some of component 2 in the same workshop), or must each workshop be dedicated to producing only one component?

## Turn 4 - User Simulator

A workshop can split its production hours across multiple components.

## Turn 5 - Generic Agent

QUESTION: Are the production rates in the table constant regardless of how many hours a workshop spends on a component (i.e., no setup time or learning curve), so that units produced equals hours times the rate?

## Turn 5 - User Simulator

Yes, the production rates are constant. Units produced equals hours times the rate.

## Turn 6 - Generic Agent

QUESTION: Do the component quantities have to be whole numbers (integer units), or can they be fractional?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: If a workshop has leftover hours that cannot be used to produce a full additional unit of any component, is that leftover time simply unused (free), or does it incur a cost or penalty?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the production hours allocated to each component by a workshop required to be whole numbers, or can they be any non-negative fractional amount?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on the total number of units of each component that can be produced (such as a maximum output per component), or is the only limit on each component the total hours available across the four workshops?

## Turn 9 - User Simulator

The only limit on each component is the total hours available across the four workshops.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or considerations I should account for, such as minimum production levels per workshop, sequencing requirements, or quality constraints?

## Turn 10 - User Simulator

No, there are no other constraints or considerations. The only constraint is that the total number of hours allocated by each workshop to the three components must not exceed its production capacity.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the number of complete products produced.
- **Product structure:** One complete product requires exactly one unit of each of the three components (component 1, component 2, component 3).
- **Workshops:** Four workshops (A, B, C, D), each with a fixed production capacity in hours:
  - A: 100 hours
  - B: 150 hours
  - C: 80 hours
  - D: 200 hours
- **Production rates (units per hour):**
  - Workshop A: 10 (comp 1), 15 (comp 2), 5 (comp 3)
  - Workshop B: 15 (comp 1), 10 (comp 2), 5 (comp 3)
  - Workshop C: 20 (comp 1), 5 (comp 2), 10 (comp 3)
  - Workshop D: 10 (comp 1), 15 (comp 2), 20 (comp 3)
- **Allocation:** Each workshop can split its hours freely across the three components; units produced = hours × rate (constant rates, no setup time).
- **Constraints:** For each workshop, the sum of hours allocated to the three components must not exceed its capacity. No demand, no minimums, no per-component caps, no other constraints.
- **Completeness:** The number of complete products is limited by the scarcest component (each product needs one of each).
- **Integrality / leftover-time treatment:** Left for internal confirmation; I will model hours and units as continuous (non-negative) variables, which is the standard reading for a capacity-allocation problem, and note that integrality can be added if required.