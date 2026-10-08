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

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products that can be assembled, or minimize total production hours used?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled.

## Turn 2 - Generic Agent

QUESTION: For each component, is the total number of units produced the sum of the units made in all four workshops (i.e., each workshop can produce any of the three components, and their outputs are pooled together)?

## Turn 2 - User Simulator

Yes, each workshop can produce any of the three components, and the total units for each component are the sum of the units made across all four workshops.

## Turn 3 - Generic Agent

QUESTION: To assemble one complete product, how many units of each component are required — is it one unit of Component 1, one unit of Component 2, and one unit of Component 3?

## Turn 3 - User Simulator

Yes, one complete product requires one unit of Component 1, one unit of Component 2, and one unit of Component 3.

## Turn 4 - Generic Agent

QUESTION: Are the production quantities for each component at each workshop required to be whole numbers (integer units), or can they be fractional?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: If a workshop has leftover capacity that isn't used for any component, is that simply allowed (no penalty), or is there some requirement or cost associated with unused hours?

## Turn 5 - User Simulator

Unused hours are simply allowed; there is no penalty or cost associated with them.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum production requirement for each component or for the total number of complete products, or is the only goal to maximize complete products subject to the capacity limits?

## Turn 6 - User Simulator

There are no minimum production requirements. The only goal is to maximize the number of complete products subject to the workshop capacity limits.

## Turn 7 - Generic Agent

QUESTION: Regarding the production rates in the table — for example, Workshop A producing Component 1 at 10 units/hour — does this mean that if Workshop A spends H hours on Component 1, it produces 10×H units of Component 1?

## Turn 7 - User Simulator

Yes, if Workshop A spends H hours on Component 1, it produces 10×H units of Component 1.

## Turn 8 - Generic Agent

QUESTION: Are the production quantities (units of each component) required to be whole numbers, or can they be fractional?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Since the integrality question is still pending, as a fallback: should I model the production quantities as continuous (allowing fractional units) in the final formulation, and note that integrality can be added later if confirmed?

## Turn 9 - User Simulator

Yes, model the production quantities as continuous (allowing fractional units) for now, and note that integrality can be added later if confirmed.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the number of complete products assembled.
- **Product structure:** One complete product requires exactly 1 unit of Component 1, 1 unit of Component 2, and 1 unit of Component 3.
- **Decision variables:** For each workshop (A, B, C, D) and each component (1, 2, 3), the number of hours allocated to that component. Continuous, non-negative.
- **Production:** If workshop w spends H hours on component c, it produces (rate_wc × H) units of component c, where rate_wc is the production rate from the table.
- **Capacity constraints:** For each workshop, the sum of hours allocated to all three components ≤ its production capacity (A: 100, B: 150, C: 80, D: 200).
- **Assembly constraint:** The number of complete products ≤ total units of Component 1, ≤ total units of Component 2, and ≤ total units of Component 3 (where total units of each component is the sum across all four workshops).
- **Unused hours:** Allowed, no penalty.
- **No minimum production requirements.**
- **Integrality:** Modeled as continuous for now; integrality can be added later if confirmed.