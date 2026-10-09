# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U8, U9, U10, U11, U13, U2, U3, U4, U5, U6, U7
I need help deciding how many tables, chairs, and bookshelves to produce, where the total warehouse space occupied by the products cannot exceed 500 square meters, at least 10 tables and at least 20 bookshelves must be produced, and the total number of items produced cannot exceed 200. Profit for each product is the selling price minus the manufacturing cost.

Selling prices: table $200, chair $50, bookshelf $150.

Manufacturing costs: table $120, chair $20, bookshelf $90.

Space occupancy: table 5 sq m, chair 2 sq m, bookshelf 3 sq m.

Total available warehouse space: 500 sq m.

Minimum required production: tables 10, bookshelves 20.

Total production capacity: 200 items.

## Problem units
- U1 (context): I need help deciding how many tables, chairs, and bookshelves to produce.
- U2 (data): Selling prices: table $200, chair $50, bookshelf $150.
- U3 (data): Manufacturing costs: table $120, chair $20, bookshelf $90.
- U4 (data): Space occupancy: table 5 sq m, chair 2 sq m, bookshelf 3 sq m.
- U5 (data): Total available warehouse space: 500 sq m.
- U6 (data): Minimum required production: tables 10, bookshelves 20.
- U7 (data): Total production capacity: 200 items.
- U8 (constraint): The total warehouse space occupied by the products cannot exceed 500 square meters.
- U9 (constraint): At least 10 tables must be produced.
- U10 (constraint): At least 20 bookshelves must be produced.
- U11 (constraint): The total number of items produced cannot exceed 200.
- U12 (objective): Maximize total profit.
- U13 (assumption): Profit for each product is the selling price minus the manufacturing cost.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without specifying the objective, the modeling agent cannot formulate an optimization model; the problem would be ill-posed and the agent would not know what to optimize.
- Problem unit ID: U12
- Semantic hit rule: The agent's question must explicitly ask about the objective or goal of the production problem, such as maximizing profit, minimizing cost, or some other metric.
- Reference acceptable questions:
  - What is the objective we are trying to achieve? Are we maximizing profit?
  - What should be our goal when deciding production quantities?
- Failure modes:
  - Assuming the objective is to minimize total manufacturing cost
  - Assuming the goal is to maximize total revenue
  - Assuming no objective and just producing to meet minimum requirements


# Atomic Question Map

(No detector-counted atomic questions.)

# Full Transcript

## Turn 1 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 1.000

Confidence rationale: The request explicitly defines the decision variables (production quantities for tables, chairs, and bookshelves), the objective function (maximizing total profit calculated from provided selling prices and manufacturing costs), and all constraints (warehouse space limit, minimum production requirements for specific items, and total production capacity). All necessary parameters are provided, and no silent assumptions are required to define the feasible region or operational logic.

Summary: Maximize total profit by determining the production quantities of tables, chairs, and bookshelves. Profit per unit is $80 for tables, $30 for chairs, and $60 for bookshelves. Constraints include: total space usage (5x + 2y + 3z) <= 500 sq m, total items (x + y + z) <= 200, minimum tables (x) >= 10, and minimum bookshelves (z) >= 20. All variables are non-negative integers.