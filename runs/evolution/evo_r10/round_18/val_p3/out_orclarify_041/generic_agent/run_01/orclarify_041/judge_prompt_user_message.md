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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand from all investments that have matured by then, with any leftover uninvested cash simply carried over at face value (1.00) into that total?

## Turn 1 - User Simulator

Yes. The objective is to maximize the total cash on hand at the end of Year 3, which includes proceeds from all investments that have matured by then plus any uninvested cash carried over at face value.

## Turn 2 - Generic Agent

QUESTION: If you invest in the 1-year product (1) at the start of Year 3, it matures at the end of Year 3 and pays 1.20·I — is that proceeds included in the end-of-Year-3 cash total, i.e., is the Year-3 investment allowed to count toward the objective?

## Turn 2 - User Simulator

Yes, the proceeds from the 1-year product (1) invested at the start of Year 3 are included in the end-of-Year-3 cash total.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much of the available cash you may leave uninvested (i.e., carried over at face value) in any year, or is there a minimum amount that must be invested each year?

## Turn 3 - User Simulator

There is no limit on how much cash may be left uninvested, and there is no minimum amount that must be invested each year.

## Turn 4 - Generic Agent

QUESTION: Can the proceeds from an investment that matures at the end of a year be reinvested in products available at the beginning of the next year (for example, the 1.20·I received at the end of Year 1 from product (1) being available to invest at the start of Year 2)?

## Turn 4 - User Simulator

Yes, proceeds from investments that mature at the end of a year are available to invest at the beginning of the next year.

## Turn 5 - Generic Agent

QUESTION: For the 2-year product (2) invested at the start of Year 1, is the 120,000 yuan cap on the single initial investment amount, or is it a cap on the total amount that can ever be committed to product (2) across the whole plan?

## Turn 5 - User Simulator

The 120,000 yuan cap is on the single initial investment amount at the start of Year 1. Since product (2) is only available at the beginning of Year 1, this is also the total amount that can ever be committed to product (2) across the whole plan.

## Turn 6 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax deducted from the investment proceeds, or are the stated multipliers (1.20, 1.50, 1.60, 1.40) the exact net amounts received?

## Turn 6 - User Simulator

The stated multipliers (1.20, 1.50, 1.60, 1.40) are the exact net amounts received. There are no transaction costs, fees, or taxes deducted.

## Turn 7 - Generic Agent

QUESTION: Are investment amounts required to be whole yuan (integer values), or can you invest any fractional amount of yuan?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: If you invest in the 1-year product (1) at the start of Year 1, the 1.20·I received at the end of Year 1 is available at the start of Year 2 — can that cash then be invested in product (3), the same-year product available at the beginning of Year 2?

## Turn 8 - User Simulator

Yes, the cash received at the end of Year 1 from product (1) is available at the start of Year 2 and can be invested in product (3).

## Turn 9 - Generic Agent

QUESTION: Is there any restriction on investing in product (1) more than once across the three years, or can you invest in it at the start of Year 1, Year 2, and Year 3 independently with no cross-year limit?

## Turn 9 - User Simulator

There is no cross-year limit. You can invest in product (1) independently at the start of Year 1, Year 2, and Year 3, subject only to the cash available at each beginning of year.

## Turn 10 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the four products, or can you invest any positive amount (down to arbitrarily small) in each product you choose?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there any requirement that the full 500,000 yuan initial capital must be allocated (invested or held) at the start of Year 1, or can you simply hold part of it as cash from the beginning?

## Turn 11 - User Simulator

You can hold part of the initial capital as cash from the beginning. There is no requirement that the full 500,000 yuan must be invested at the start of Year 1.

## Turn 12 - Generic Agent

QUESTION: When you hold cash (uninvested) from one year to the next, does it earn any interest or return, or does it simply carry over at face value (1.00) with no growth?

## Turn 12 - User Simulator

Cash held uninvested carries over at face value (1.00) with no growth.

## Turn 13 - Generic Agent

QUESTION: Is there any upper limit on the total amount you can invest in product (1) in a single year, or is it truly unlimited as stated?

## Turn 13 - User Simulator

Yes, product (1) is truly unlimited in a single year, subject only to the cash available at the beginning of that year.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the beginning of each year (initial capital plus matured proceeds) must be fully allocated between investments and carried-over cash, i.e., can you "lose" or discard any cash, or must every yuan be either invested or held?

## Turn 14 - User Simulator

Every yuan must be either invested or held as cash. You cannot lose or discard any cash.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in all products at the beginning of a given year cannot exceed the cash available at that time, or is that simply implied by the cash-flow logic?

## Turn 15 - User Simulator

Yes, the total amount invested at the beginning of a given year cannot exceed the cash available at that time. This is implied by the cash-flow logic: you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 16 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of Year 3, which equals the sum of proceeds from all investments matured by end of Year 3 plus any uninvested cash carried over at face value (1.00).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Invest I at the start of a year → receive 1.20·I at that year's end. Unlimited capacity. No cross-year limit; can be used independently each year.

2. **Product (2):** 2-year product, available only at the beginning of Year 1. Invest I at start of Year 1 → receive 1.50·I at end of Year 2. Cap: I ≤ 120,000 yuan.

3. **Product (3):** Same-year product, available only at the beginning of Year 2. Invest I at start of Year 2 → receive 1.60·I at end of Year 2. Cap: I ≤ 150,000 yuan.

4. **Product (4):** 1-year product, available only at the beginning of Year 3. Invest I at start of Year 3 → receive 1.40·I at end of Year 3. Cap: I ≤ 100,000 yuan.

**Cash-flow rules:**
- Proceeds from investments maturing at the end of a year are available to invest at the beginning of the next year.
- Uninvested cash carries over at face value (1.00), no interest.
- Every yuan must be either invested or held as cash (no discarding).
- Total investments at the beginning of a year cannot exceed cash available at that time.
- No minimum investment amount (deferred, but not load-bearing since all returns > 1.00 make investing strictly better than holding cash).
- No transaction costs, fees, or taxes; stated multipliers are exact net returns.
- No requirement to invest the full 500,000 at the start of Year 1.

**Integrality:** Deferred (user needs internal confirmation). Since all returns exceed 1.00 and the problem is a linear program, the optimal solution will naturally allocate to the highest-return products first, and integrality is unlikely to change the optimal structure. I will model with continuous (non-negative real) variables.

**Decision variables (all ≥ 0):**
- x1₁, x1₂, x1₃: amounts invested in product (1) at start of Years 1, 2, 3
- x2: amount invested in product (2) at start of Year 1
- x3: amount invested in product (3) at start of Year 2
- x4: amount invested in product (4) at start of Year 3
- c1, c2, c3: cash held (uninvested) at the end of Years 1, 2, 3 respectively

**Constraints:**
- Year 1: x1₁ + x2 + c1 = 500,000
- Year 2: x1₂ + x3 + c2 = 1.20·x1₁ + c1
- Year 3: x1₃ + x4 + c3 = 1.20·x1₂ + 1.50·x2 + 1.60·x3 + c2
- x2 ≤ 120,000
- x3 ≤ 150,000
- x4 ≤ 100,000
- All variables ≥ 0

**Objective:** Maximize 1.20·x1₃ + 1.40·x4 + c3

This is a linear program. The optimal solution will be found by allocating to the highest-return opportunities first, subject to the caps and cash-flow timing.