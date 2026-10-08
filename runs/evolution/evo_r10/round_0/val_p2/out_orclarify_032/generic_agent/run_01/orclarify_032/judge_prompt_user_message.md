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

QUESTION: What is the objective of the production plan — for example, maximizing total profit (with a given profit per unit of each component), maximizing total number of finished products, or something else?

## Turn 1 - User Simulator

The objective is to maximize the number of completed products.

## Turn 2 - Generic Agent

QUESTION: Is each completed product made of exactly one unit of each of the three components (i.e., 1 of Component 1 + 1 of Component 2 + 1 of Component 3)?

## Turn 2 - User Simulator

Yes, each completed product requires exactly one unit of each of the three components.

## Turn 3 - Generic Agent

QUESTION: Can workshops produce fractional units of a component (continuous production), or must the number of units produced by each workshop for each component be a whole number?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Do the production rates in the table mean that a workshop produces that many units per hour (so hours used = units produced ÷ rate), or do they mean something else, such as the number of hours needed per unit?

## Turn 4 - User Simulator

The production rates mean that a workshop produces that many units per hour.

## Turn 5 - Generic Agent

QUESTION: Since the integer-vs-continuous point is still pending internal confirmation, should I model the production quantities as continuous (allowing fractional units) for now, or would you prefer I wait for that confirmation before finalizing?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum production requirements — for example, a required minimum number of completed products that must be delivered, or a minimum number of units of any component that must be produced?

## Turn 6 - User Simulator

No, there are no minimum production requirements.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how many units of a component a workshop can produce beyond its capacity constraint — for example, a maximum number of units per workshop per component, or a limit on the total number of completed products that can be sold?

## Turn 7 - User Simulator

No, there are no limits beyond the workshop capacity constraints.

## Turn 8 - Generic Agent

QUESTION: Since the integer-vs-continuous point is still pending, should I proceed with a continuous model (allowing fractional units) and note that it can be tightened to integer later if needed?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Product structure:** Each completed product requires exactly 1 unit of Component 1 + 1 unit of Component 2 + 1 unit of Component 3.
- **Objective:** Maximize the number of completed products.
- **Workshops:** Four workshops (A, B, C, D), each with a production capacity in hours: A=100, B=150, C=80, D=200.
- **Production rates (units/hour):**
  - A: C1=10, C2=15, C3=5
  - B: C1=15, C2=10, C3=5
  - C: C1=20, C2=5, C3=10
  - D: C1=10, C2=15, C3=20
- **Capacity constraint:** For each workshop, the total hours allocated to the three components (units produced ÷ rate) must not exceed its capacity.
- **No minimum production requirements.**
- **No additional limits** beyond workshop capacity.
- **Integrality:** Pending internal confirmation. I will model with continuous variables (allowing fractional units) and note that the model can be tightened to integer variables if whole-unit production is required.

**Model formulation:**

Decision variables:
- x_{w,c} ≥ 0: number of units of component c produced by workshop w (w ∈ {A,B,C,D}, c ∈ {1,2,3})
- P ≥ 0: number of completed products

Objective:
- Maximize P

Constraints:
- Component balance: for each component c, Σ_w x_{w,c} ≥ P (total units of each component must be at least the number of completed products)
- Workshop capacity: for each workshop w, Σ_c (x_{w,c} / rate_{w,c}) ≤ capacity_w
- Non-negativity: x_{w,c} ≥ 0, P ≥ 0

This is a linear program. If integer production is later confirmed, the x_{w,c} variables (and P) would be constrained to be integers, making it a mixed-integer linear program.