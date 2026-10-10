# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U9, U11, U2, U3, U4, U6, U8
I need help creating an investment plan over the next three years, with the objective to maximize total principal plus interest at the end of Year 3. However, investment in product (2) cannot exceed 120,000 yuan, investment in product (3) cannot exceed 150,000 yuan, and investment in product (4) cannot exceed 100,000 yuan.

Initial capital at beginning of Year 1: 500,000 yuan.

Investment projects:
(1) A 1-year product available at the beginning of each year (Years 1–3). If you invest I at the start of a year, you receive 1.20·I at that year’s end. Unlimited capacity.
(2) A 2-year product available only at the beginning of Year 1; it matures at the end of Year 2 and pays 1.50·I. Investment in this product is capped at 120,000 yuan.
(3) A same-year product available at the beginning of Year 2, maturing at the end of Year 2, and paying 1.60·I. Investment is capped at 150,000 yuan.
(4) A 1-year product available at the beginning of Year 3, maturing at the end of Year 3, and paying 1.40·I. Investment is capped at 100,000 yuan.

Maximum allowable investment for project (2): 120,000 yuan.

Maximum allowable investment for project (3): 150,000 yuan.

Maximum allowable investment for project (4): 100,000 yuan.

## Problem units
- U1 (context): I need help creating an investment plan over the next three years that maximizes my total wealth at the end.
- U2 (data): Initial capital at beginning of Year 1: 500,000 yuan.
- U3 (data): Investment projects:
(1) A 1-year product available at the beginning of each year (Years 1–3). If you invest I at the start of a year, you receive 1.20·I at that year’s end. Unlimited capacity.
(2) A 2-year product available only at the beginning of Year 1; it matures at the end of Year 2 and pays 1.50·I. Investment in this product is capped at 120,000 yuan.
(3) A same-year product available at the beginning of Year 2, maturing at the end of Year 2, and paying 1.60·I. Investment is capped at 150,000 yuan.
(4) A 1-year product available at the beginning of Year 3, maturing at the end of Year 3, and paying 1.40·I. Investment is capped at 100,000 yuan.
- U4 (data): Maximum allowable investment for project (2): 120,000 yuan.
- U5 (constraint): Investment in product (2) cannot exceed 120,000 yuan.
- U6 (data): Maximum allowable investment for project (3): 150,000 yuan.
- U7 (constraint): Investment in product (3) cannot exceed 150,000 yuan.
- U8 (data): Maximum allowable investment for project (4): 100,000 yuan.
- U9 (constraint): Investment in product (4) cannot exceed 100,000 yuan.
- U10 (constraint): No borrowing allowed; decisions are made at the beginnings of Years 1–3 using only currently available cash (initial capital and proceeds from matured investments).
- U11 (objective): Maximize total principal plus interest at the end of Year 3.

## Hidden slot scoring rules
## H1: no_borrowing_cash_only
- Severity: P1
- Severity reason: Without this constraint, the agent may assume borrowing is allowed, leading to a materially incorrect cash-flow model that overestimates available funds and yields an investment plan different from the intended problem.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must explicitly ask about whether borrowing is allowed, or about the restriction that only cash on hand (initial capital and matured proceeds) can be used for investments.
- Reference acceptable questions:
  - Is borrowing allowed, or can we only use the cash we already have?
  - Are we permitted to take out loans, or must we invest strictly from the initial capital and any returns we receive?
- Failure modes:
  - Assuming unlimited borrowing is possible at zero interest
  - Assuming the agent can carry a negative cash balance to invest more


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or can you also invest funds that are returned from maturing projects in subsequent years?

## Turn 1 - User Simulator

The 500,000 yuan is the only source of funds available at the beginning of Year 1. In subsequent years, you can also invest funds returned from projects that have already matured.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the investment amount at the beginning of each year (Years 1, 2, and 3) a separate decision variable that can be chosen independently for each year, subject to the funds available at that time?

## Turn 2 - User Simulator

Yes, the investment amount in product (1) is a separate decision for the beginning of each year (Years 1, 2, and 3), subject to the funds available at that time.

## Turn 3 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan, such as minimum investment amounts, mandatory diversification, or restrictions on how funds can be carried over between years?

## Turn 3 - User Simulator

No, there are no minimum investment amounts, mandatory diversification requirements, or restrictions on carrying over funds between years. The only constraints are the maximum investment caps for products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 4 - Generic Agent

QUESTION: When you say you cannot borrow money, does this mean that the total amount invested at the beginning of any year cannot exceed the total funds available at that time (initial capital plus returns from matured projects), or is there a specific limit on how much cash you must hold back?

## Turn 4 - User Simulator

It means the total amount invested at the beginning of any year cannot exceed the total funds available at that time. There is no specific limit on how much cash you must hold back.

## Turn 5 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total wealth (principal plus interest) at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Funding Rule:** No borrowing allowed. The total investment at the beginning of any year cannot exceed the funds available at that time (initial capital plus returns from projects maturing at the end of the previous year). Uninvested cash carries over to the next year.
5.  **Investment Products & Decision Variables:**
    *   **Product (1):** 1-year term. Available at the beginning of Years 1, 2, and 3.
        *   Decision variables: $x_{1,1}$ (invested at start of Y1), $x_{1,2}$ (invested at start of Y2), $x_{1,3}$ (invested at start of Y3).
        *   Return: 1.20 times the investment amount at the end of the respective year.
        *   Constraint: No upper bound (unlimited capacity).
    *   **Product (2):** 2-year term. Available only at the beginning of Year 1.
        *   Decision variable: $x_2$ (invested at start of Y1).
        *   Return: 1.50 times the investment amount at the end of Year 2.
        *   Constraint: $x_2 \le 120,000$.
    *   **Product (3):** Same-year term. Available only at the beginning of Year 2.
        *   Decision variable: $x_3$ (invested at start of Y2).
        *   Return: 1.60 times the investment amount at the end of Year 2.
        *   Constraint: $x_3 \le 150,000$.
    *   **Product (4):** 1-year term. Available only at the beginning of Year 3.
        *   Decision variable: $x_4$ (invested at start of Y3).
        *   Return: 1.40 times the investment amount at the end of Year 3.
        *   Constraint: $x_4 \le 100,000$.
6.  **Variable Domains:** All investment variables are non-negative continuous variables.
7.  **Cash Flow Constraints:**
    *   **Start of Year 1:** $x_{1,1} + x_2 \le 500,000$.
    *   **Start of Year 2:** Funds available = Uninvested cash from Y1 + Return from $x_{1,1}$ (matures end of Y1).
        *   $x_{1,2} + x_3 \le (500,000 - x_{1,1} - x_2) + 1.20 \cdot x_{1,1}$.
    *   **Start of Year 3:** Funds available = Uninvested cash from Y2 + Return from $x_{1,2}$ (matures end of Y2) + Return from $x_2$ (matures end of Y2) + Return from $x_3$ (matures end of Y2).
        *   $x_{1,3} + x_4 \le \text{Uninvested}_{Y2} + 1.20 \cdot x_{1,2} + 1.50 \cdot x_2 + 1.60 \cdot x_3$.
        *   (Note: Uninvested cash from Y2 is the residual from the Year 2 constraint).
8.  **Final Wealth Calculation:**
    *   Total Wealth at End of Year 3 = Uninvested cash from Y3 + Return from $x_{1,3}$ + Return from $x_4$.
    *   $W = \text{Uninvested}_{Y3} + 1.20 \cdot x_{1,3} + 1.40 \cdot x_4$.

**Assumptions:**
*   All investments are made at the very beginning of the year and returns are received at the very end of the maturity year.
*   There are no transaction costs or taxes.
*   Cash can be held indefinitely without interest (implied by "no specific limit on how much cash you must hold back" and standard LP formulation unless stated otherwise).