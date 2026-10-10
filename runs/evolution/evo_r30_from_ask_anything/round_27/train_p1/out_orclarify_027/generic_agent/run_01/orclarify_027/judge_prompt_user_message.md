# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U5, U6, U7, U8, U2
I need help arranging a production plan for my factory. Each product must be processed through both procedure A and procedure B, and the total processing time assigned to each machine must not exceed its effective machine hours. Product I can be processed on any equipment for procedure A (A1, A2) and any equipment for procedure B (B1, B2, B3). Product II can be processed on any A equipment (A1, A2), but only on B1 for procedure B. Product III can only be processed on A2 for procedure A and on B2 for procedure B.

Table 1-4
| Equipment  | Product I | Product II | Product III | Effective Machine Hours | Operating Costs at Full Capacity (Yuan) |
|------------|-----------|------------|-------------|--------------------------|------------------------------------------|
| A1         | 5         | 10         |             | 6000                     | 300                                      |
| A2         | 7         | 9          | 12          | 10000                    | 321                                      |
| B1         | 6         | 8          |             | 4000                     | 250                                      |
| B2         | 4         |            | 11          | 7000                     | 783                                      |
| B3         | 7         |            |             | 4000                     | 200                                      |
| Raw Material Cost (Yuan/Unit) | 0.25 | 0.35       | 0.50       |                          |                                          |
| Unit Price (Yuan/Unit)        | 1.25 | 2.00       | 2.80       |                          |                                          |

## Problem units
- U1 (context): I need help arranging a production plan for my factory.
- U2 (data): Table 1-4
| Equipment  | Product I | Product II | Product III | Effective Machine Hours | Operating Costs at Full Capacity (Yuan) |
|------------|-----------|------------|-------------|--------------------------|------------------------------------------|
| A1         | 5         | 10         |             | 6000                     | 300                                      |
| A2         | 7         | 9          | 12          | 10000                    | 321                                      |
| B1         | 6         | 8          |             | 4000                     | 250                                      |
| B2         | 4         |            | 11          | 7000                     | 783                                      |
| B3         | 7         |            |             | 4000                     | 200                                      |
| Raw Material Cost (Yuan/Unit) | 0.25 | 0.35       | 0.50       |                          |                                          |
| Unit Price (Yuan/Unit)        | 1.25 | 2.00       | 2.80       |                          |                                          |
- U3 (objective): Maximize the factory's profit.
- U4 (constraint): Each product must be processed through both procedure A and procedure B.
- U5 (constraint): The total processing time assigned to each machine must not exceed its effective machine hours.
- U6 (constraint): Product I can be processed on any equipment for procedure A (A1, A2) and any equipment for procedure B (B1, B2, B3).
- U7 (constraint): Product II can be processed on any A equipment (A1, A2), but only on B1 for procedure B.
- U8 (constraint): Product III can only be processed on A2 for procedure A and on B2 for procedure B.

## Hidden slot scoring rules
## H1: operating_cost_treatment
- Severity: P1
- Severity reason: Without clarifying how the 'operating costs at full capacity' should be included in profit (fixed charge or variable cost), the agent will likely make an arbitrary assumption that materially misstates profit and may lead to incorrect production decisions.
- Problem unit ID: U3
- Semantic hit rule: The Agent's question must explicitly ask how to include the 'Operating Costs at Full Capacity' in profit, specifically referencing whether these are fixed costs or variable costs, or requesting clarification on cost allocation.
- Reference acceptable questions:
  - How should the operating costs at full capacity be incorporated into the profit calculation? Are they fixed charges if a machine is used, or should I compute an hourly cost?
  - Do the operating costs at full capacity represent a fixed cost that must be paid if a machine runs at all, or are they proportional to actual machine usage?
- Failure modes:
  - Assuming the operating costs are variable and dividing them by effective hours to get an hourly cost without clarification
  - Assuming the operating costs are fixed and subtracting them only if the machine is fully utilized
  - Omitting operating costs entirely from the profit calculation


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the objective to maximize total profit (revenue minus raw material costs minus operating costs), or is there a different goal such as maximizing total units produced or minimizing total cost?

## Turn 1 - User Simulator

The objective is to maximize total profit. That means revenue minus raw material costs minus operating costs.

## Turn 2 - Generic Agent

QUESTION: Are the "Operating Costs at Full Capacity" values fixed costs that are incurred if any production is assigned to that machine, or are they variable costs that scale proportionally with the fraction of machine hours actually used?

## Turn 2 - User Simulator

They are fixed costs. If you use a machine at all during the planning period, you must pay that entire amount.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities for each product required to be whole numbers (integers), or can they be fractional values?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Are the effective machine hours (6000, 10000, 4000, 7000, 4000) the total available hours for the entire planning period, or are they the available hours per day or per week?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are there any minimum production requirements or maximum sales limits for each product that must be met or respected in the plan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or requirements for the production plan that have not been mentioned yet, such as minimum production levels, maximum sales limits, or dependencies between products?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are the processing times in the table (e.g., 5, 10, 7) measured in minutes per unit, or are they measured in hours per unit?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the processing times in the table (e.g., 5, 10, 7) measured in minutes per unit, or are they measured in hours per unit?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total profit, defined as Total Revenue minus Total Raw Material Costs minus Total Operating Costs.
2.  **Process Structure:** Each product must undergo both Procedure A and Procedure B.
3.  **Routing Constraints:**
    *   **Product I:** Procedure A on A1 or A2; Procedure B on B1, B2, or B3.
    *   **Product II:** Procedure A on A1 or A2; Procedure B on B1 only.
    *   **Product III:** Procedure A on A2 only; Procedure B on B2 only.
4.  **Capacity Constraints:** The total processing time assigned to each machine must not exceed its effective machine hours.
5.  **Operating Costs:** These are fixed costs. If any production is assigned to a machine, the full "Operating Cost at Full Capacity" is incurred. If no production is assigned, the cost is zero.
6.  **Raw Material Costs:** Variable costs per unit (Product I: 0.25, Product II: 0.35, Product III: 0.50).
7.  **Unit Prices:** Revenue per unit (Product I: 1.25, Product II: 2.00, Product III: 2.80).

**Assumptions (due to lack of confirmation):**
1.  **Variable Domain:** Production quantities are assumed to be **continuous** (fractional units allowed). If integer constraints are required, the model will need to be adjusted to an Integer Linear Program.
2.  **Time Units:** The processing times in the table (e.g., 5, 10) are assumed to be in the **same unit** as the "Effective Machine Hours" (e.g., if hours are in hours, processing times are in hours; if hours are in minutes, processing times are in minutes). The ratio between them is consistent.
3.  **Planning Period:** The "Effective Machine Hours" represent the total available capacity for the **entire planning period** considered in the model.
4.  **No Other Constraints:** There are no minimum production requirements, maximum sales limits, or other dependencies between products beyond the routing and capacity constraints specified.
5.  **Cost Linearity:** Raw material costs and revenue are linear with respect to the number of units produced.