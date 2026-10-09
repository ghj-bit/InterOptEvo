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

QUESTION: At the end of Year 3, is the objective to maximize the total cash value of all investments that have matured by that date, or should any funds that remain uninvested (cash) also be included in the final total?

## Turn 1 - User Simulator

The objective is to maximize the total cash value of all investments that have matured by the end of Year 3. Any funds that remain uninvested (cash) should also be included in that final total.

## Turn 2 - Generic Agent

QUESTION: Are there any transaction costs, taxes, or minimum investment amounts associated with any of the four products?

## Turn 2 - User Simulator

No, there are no transaction costs, taxes, or minimum investment amounts associated with any of the four products.

## Turn 3 - Generic Agent

QUESTION: Can you invest in the 1-year product (1) at the beginning of Year 3, and if so, does it mature at the end of Year 3?

## Turn 3 - User Simulator

Yes, you can invest in the 1-year product (1) at the beginning of Year 3, and it matures at the end of Year 3.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on the total amount of capital that can be invested in product (1) across all three years combined, or is it truly unlimited in each year?

## Turn 4 - User Simulator

Product (1) is unlimited in each year. There is no stated limit on the total amount invested in product (1) across all three years combined.

## Turn 5 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of your investment planning problem:

**Objective:** Maximize total cash value (matured investments + any uninvested cash) at the end of Year 3.

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Investment Products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at the end of that year. Unlimited capacity each year.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, paying 1.50×I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, paying 1.60×I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, paying 1.40×I. Capped at 100,000 yuan.

**Constraints:**
- No transaction costs, taxes, or minimum investment amounts.
- Product (2) ≤ 120,000 yuan
- Product (3) ≤ 150,000 yuan
- Product (4) ≤ 100,000 yuan
- Product (1) is unlimited in each year.
- Funds must be available at the beginning of each year to invest (i.e., you can only invest what you have on hand at that time).
- Any uninvested cash carries over to the next year and is included in the final total.

**Decision Variables (to be determined):**
- Amount invested in Product (1) at the beginning of Year 1, Year 2, and Year 3
- Amount invested in Product (2) at the beginning of Year 1
- Amount invested in Product (3) at the beginning of Year 2
- Amount invested in Product (4) at the beginning of Year 3
- Amount of cash held (uninvested) at each point in time

This is a linear programming problem that can be solved to find the optimal allocation. Would you like me to proceed with formulating and solving the model?

## Turn 5 - User Simulator

Yes, please proceed with formulating and solving the model.

## Turn 6 - Generic Agent

## Formulation and Solution

### Decision Variables

| Variable | Description |
|----------|-------------|
| $x_1$ | Amount invested in Product (1) at the beginning of Year 1 |
| $x_2$ | Amount invested in Product (2) at the beginning of Year 1 |
| $x_3$ | Amount invested in Product (1) at the beginning of Year 2 |
| $x_4$ | Amount invested in Product (3) at the beginning of Year 2 |
| $x_5$ | Amount invested in Product (1) at the beginning of Year 3 |
| $x_6$ | Amount invested in Product (4) at the beginning of Year 3 |

### Cash Flow Constraints

**Beginning of Year 1:** Total available = 500,000
$$x_1 + x_2 \leq 500{,}000$$

**Beginning of Year 2:** Available = proceeds from Product (1) Year 1 + uninvested cash from Year 1
$$x_3 + x_4 \leq 1.20\,x_1 + (500{,}000 - x_1 - x_2)$$

**Beginning of Year 3:** Available = proceeds from Product (1) Year 2 + Product (2) + Product (3) + uninvested cash from Year 2
$$x_5 + x_6 \leq 1.20\,x_3 + 1.50\,x_2 + 1.60\,x_4 + (1.20\,x_1 + 500{,}000 - x_1 - x_2 - x_3 - x_4)$$

### Capacity Constraints

$$x_2 \leq 120{,}000$$
$$x_4 \leq 150{,}000$$
$$x_6 \leq 100{,}000$$

### Non-negativity

$$x_i \geq 0 \quad \text{for all } i$$

### Objective Function

Maximize total cash at the end of Year 3:

$$\text{Maximize } Z = 1.20\,x_5 + 1.40\,x_6 + \Big[1.20\,x_3 + 1.50\,x_2 + 1.60\,x_4 + 1.20\,x_1 + 500{,}000 - x_1 - x_2 - x_3 - x_4 - x_5 - x_6\Big]$$

Simplifying:

$$Z = 1.20\,x_5 + 1.40\,x_6 + 1.20\,x_3 + 1.50\,x_2 + 1.60\,x_4 + 1.20\,x_1 + 500{,}000 - x_1 - x_2 - x_3 - x_4 - x_5 - x_6$$

$$Z = 0.20\,x_1 + 0.50\,x_2 + 0.20\,x_3 + 0.60\,x_4 + 0.20\,x_5 + 0.40\,x_6 + 500{,}000$$

### Solving the LP

Since the objective coefficients are all positive, we want to invest as much as possible in the highest-return opportunities, subject to the cash flow constraints.

**Step 1 – Year 1 allocation:**
- Product (2) has the highest "per-yuan" contribution to the final objective (0.50 per yuan invested), so invest the maximum: $x_2 = 120{,}000$.
- Remaining Year 1 cash: $500{,}000 - 120{,}000 = 380{,}000$.
- Product (1) Year 1 contributes 0.20 per yuan. Invest all remaining: $x_1 = 380{,}000$.

**Step 2 – Year 2 available funds:**
$$1.20(380{,}000) + (500{,}000 - 380{,}000 - 120{,}000) = 456{,}000 + 0 = 456{,}000$$

- Product (3) contributes 0.60 per yuan (highest in Year 2), so invest the maximum: $x_4 = 150{,}000$.
- Remaining Year 2 cash: $456{,}000 - 150{,}000 = 306{,}000$.
- Product (1) Year 2 contributes 0.20 per yuan. Invest all remaining: $x_3 = 306{,}000$.

**Step 3 – Year 3 available funds:**
$$1.20(306{,}000) + 1.50(120{,}000) + 1.60(150{,}000) + (456{,}000 - 306{,}000 - 150{,}000)$$
$$= 367{,}200 + 180{,}000 + 240{,}000 + 0 = 787{,}200$$

- Product (4) contributes 0.40 per yuan (higher than Product (1)'s 0.20), so invest the maximum: $x_6 = 100{,}000$.
- Remaining Year 3 cash: $787{,}200 - 100{,}000 = 687{,}200$.
- Product (1) Year 3 contributes 0.20 per yuan. Invest all remaining: $x_5 = 687{,}200$.

### Optimal Solution

| Variable | Amount (yuan) |
|----------|--------------|
| $x_1$ – Product (1), Year 1 | 380,000 |
| $x_2$ – Product (2), Year 1 | 120,000 |
| $x_3$ – Product (1), Year 2 | 306,000 |
| $x_4$ – Product (3), Year 2 | 150,000 |
| $x_5$ – Product (1), Year 3 | 687,200 |
| $x_6$ – Product (4), Year 3 | 100,000 |

### Final Cash at End of Year 3

$$Z = 0.20(380{,}000) + 0.50(120{,}000) + 0.20(306{,}000) + 0.60(150{,}000) + 0.20(687{,}200) + 0.40(100{,}000) + 500{,}000$$

$$= 76{,}000 + 60{,}000 + 61{,}200 + 90{,}000 + 137{,}440 + 40{,}000 + 500{,}000$$

$$\boxed{Z = 964{,}640 \text{ yuan}}$$

### Verification (Year-by-Year Cash Reconciliation)

| Time | Inflow | Outflow (Investments) | Cash Carried Forward |
|------|--------|-----------------------|---------------------|
| Beg. Year 1 | 500,000 | 380,000 + 120,000 = 500,000 | 0 |
| Beg. Year 2 | 1.20×380,000 = 456,000 | 306,000 + 150,000 = 456,000 | 0 |
| Beg. Year 3 | 1.20×306,000 + 1.50×120,