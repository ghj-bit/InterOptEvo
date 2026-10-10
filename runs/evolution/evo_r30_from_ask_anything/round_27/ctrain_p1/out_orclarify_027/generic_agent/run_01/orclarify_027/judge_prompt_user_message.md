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

QUESTION: Is the goal to maximize total profit, where profit is calculated as total revenue from selling all produced units minus total raw material costs minus total operating costs?

## Turn 1 - User Simulator

Yes, that is correct. The goal is to maximize total profit, calculated as total revenue from selling all produced units minus total raw material costs minus total operating costs.

## Turn 2 - Generic Agent

QUESTION: Are the "Operating Costs at Full Capacity" figures fixed costs that are incurred in full whenever any production is assigned to that machine, or are they variable costs that scale proportionally with the fraction of machine hours actually used?

## Turn 2 - User Simulator

They are fixed costs. If you use a machine at all during the planning period, you must pay that entire amount.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities for each product required to be whole numbers, or can they be fractional values?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Are the production quantities for each product required to be whole numbers, or can they be fractional values?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are the "Effective Machine Hours" limits for each machine hard ceilings that must not be exceeded, or are they soft targets that can be violated with a penalty?

## Turn 5 - User Simulator

They are hard ceilings that must not be exceeded.

## Turn 6 - Generic Agent

QUESTION: Is there a minimum demand or required production quantity for any of the three products that must be met, or is the production quantity for each product free to be zero if it is not profitable?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements, such as minimum production levels, maximum production limits, or dependencies between products, that are not mentioned in the table?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is the planning horizon a single period where all production is completed and sold within that period, or does it span multiple periods with inventory carry-over?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the planning horizon a single period where all production is completed and sold within that period, or does it span multiple periods with inventory carry-over?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total profit.
2.  **Profit Calculation:** Total Revenue (Unit Price × Quantity) - Total Raw Material Cost (Raw Material Cost/Unit × Quantity) - Total Operating Costs.
3.  **Operating Costs:** Fixed costs. If a machine is used at all (i.e., total processing time assigned > 0), the full "Operating Costs at Full Capacity" amount is incurred. If a machine is not used, the cost is 0.
4.  **Machine Capacity Constraints:** The "Effective Machine Hours" are hard ceilings. The total processing time assigned to each machine must not exceed this limit.
5.  **Routing Constraints:**
    *   **Product I:** Procedure A can be on A1 or A2. Procedure B can be on B1, B2, or B3.
    *   **Product II:** Procedure A can be on A1 or A2. Procedure B must be on B1.
    *   **Product III:** Procedure A must be on A2. Procedure B must be on B2.
6.  **Processing Times:** The values in the table (e.g., 5 for Product I on A1) represent the processing time (hours) required per unit of product on that specific machine for that specific procedure.

**Assumptions (due to lack of confirmation):**
1.  **Variable Domain:** Production quantities are assumed to be **continuous** (fractional values allowed). *Note: If whole numbers are required, the model becomes a Mixed Integer Linear Program (MILP) instead of a Linear Program (LP).*
2.  **Demand/Production Limits:** There are **no minimum production requirements** and **no maximum production limits** other than those imposed by machine capacity and the non-negativity constraint. Production can be zero if not profitable.
3.  **Planning Horizon:** This is a **single-period** problem. There is no inventory carry-over, and all produced units are assumed to be sold.
4.  **Sales:** All produced units can be sold at the stated unit prices. There are no demand caps.
5.  **Procedure Independence:** The choice of machine for Procedure A is independent of the choice of machine for Procedure B for the same product unit (except where routing constraints force a specific machine). The total time on a machine is the sum of times for all products processed on it for both procedures (if applicable). *Correction: The table lists times per procedure. A machine only performs one procedure (A machines do A, B machines do B). So A1/A2 only handle Procedure A, and B1/B2/B3 only handle Procedure B.*

**Model Structure Summary:**
*   **Decision Variables:**
    *   $x_{i,j}$: Quantity of Product $i$ processed on Machine $j$ for Procedure A (where applicable).
    *   $y_{i,k}$: Quantity of Product $i$ processed on Machine $k$ for Procedure B (where applicable).
    *   $z_j$: Binary variable indicating if Machine $j$ is used (1 if used, 0 otherwise).
*   **Objective Function:** Maximize $\sum (\text{Price}_i - \text{RM Cost}_i) \times Q_i - \sum (\text{Fixed Cost}_j \times z_j)$, where $Q_i$ is total production of Product $i$.
*   **Constraints:**
    *   Flow balance: Total quantity of Product $i$ processed in Procedure A must equal total quantity processed in Procedure B (and equals total production $Q_i$).
    *   Capacity: $\sum (\text{Time}_{i,j} \times x_{i,j}) \le \text{Capacity}_j$ for all A machines.
    *   Capacity: $\sum (\text{Time}_{i,k} \times y_{i,k}) \le \text{Capacity}_k$ for all B machines.
    *   Fixed Cost Linkage: $x_{i,j} \le M \cdot z_j$ and $y_{i,k} \le M \cdot z_k$ (Big-M constraints to ensure $z_j=1$ if any production occurs on machine $j$).
    *   Non-negativity: $x, y \ge 0$.
    *   Binary: $z \in \{0, 1\}$.