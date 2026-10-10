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

QUESTION: When you say "investment in product (2) cannot exceed 120,000 yuan," do you mean the total amount invested in product (2) across all years combined cannot exceed 120,000 yuan, or is the 120,000 yuan cap applied to the investment made in any single year (though product 2 is only available in Year 1)?

## Turn 1 - User Simulator

The 120,000 yuan cap applies to the total amount invested in product (2). Since product (2) is only available at the beginning of Year 1, this means the single investment made at the start of Year 1 cannot exceed 120,000 yuan.

## Turn 2 - Generic Agent

QUESTION: For product (3), which is available only at the beginning of Year 2, does the 150,000 yuan cap apply to the single investment made at the start of Year 2, or is there a possibility of multiple investments in product (3) across different periods that would sum to a total cap of 150,000 yuan?

## Turn 2 - User Simulator

The 150,000 yuan cap applies to the single investment made at the beginning of Year 2. Product (3) is only available at that time, so there is only one opportunity to invest in it.

## Turn 3 - Generic Agent

QUESTION: For product (4), which is available only at the beginning of Year 3, does the 100,000 yuan cap apply to the single investment made at the start of Year 3, or is there a possibility of multiple investments in product (4) across different periods that would sum to a total cap of 100,000 yuan?

## Turn 3 - User Simulator

The 100,000 yuan cap applies to the single investment made at the beginning of Year 3. Product (4) is only available at that time, so there is only one opportunity to invest in it.

## Turn 4 - Generic Agent

QUESTION: Are there any additional requirements or constraints beyond the caps on products (2), (3), and (4) that I should be aware of, such as minimum investment amounts, mandatory allocations to specific products, or restrictions on how funds can be carried over between years?

## Turn 4 - User Simulator

There are no minimum investment amounts or mandatory allocations to specific products. You can carry over funds between years, but you cannot borrow money. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 5 - Generic Agent

QUESTION: When you say you can carry over funds between years, does this mean that any cash not invested at the end of a year automatically rolls over to the beginning of the next year and is available for investment then, or is there a specific mechanism or constraint on how uninvested cash is handled between periods?

## Turn 5 - User Simulator

Any cash not invested at the end of a year automatically rolls over to the beginning of the next year and is available for investment then.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the amount you can invest in product (1) in any given year, or is it truly unlimited as stated?

## Turn 6 - User Simulator

Product (1) has no investment limit; it is truly unlimited.

## Turn 7 - Generic Agent

QUESTION: Are all investment amounts required to be non-negative, meaning you cannot have a negative investment in any product in any year?

## Turn 7 - User Simulator

Yes, all investment amounts must be non-negative.

## Turn 8 - Generic Agent

QUESTION: Are the investment amounts required to be integer values (whole yuan amounts), or can they be any non-negative real number?

## Turn 8 - User Simulator

The investment amounts can be any non-negative real number; they do not need to be whole yuan amounts.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total principal plus interest at the end of Year 3.

**Time Horizon:** 3 years (Year 1, Year 2, Year 3).

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Decision Variables:**
- I1_t: Investment in product (1) at the beginning of year t, for t = 1, 2, 3.
- I2_1: Investment in product (2) at the beginning of Year 1.
- I3_2: Investment in product (3) at the beginning of Year 2.
- I4_3: Investment in product (4) at the beginning of Year 3.

**Variable Domains:** All investment variables are non-negative continuous real numbers.

**Investment Products and Returns:**
1. Product (1): 1-year product available at the beginning of each year (Years 1–3). Returns 1.20·I at the end of that year. Unlimited capacity.
2. Product (2): 2-year product available only at the beginning of Year 1. Matures at the end of Year 2, returns 1.50·I. Cap: I2_1 ≤ 120,000.
3. Product (3): Same-year product available only at the beginning of Year 2. Matures at the end of Year 2, returns 1.60·I. Cap: I3_2 ≤ 150,000.
4. Product (4): 1-year product available only at the beginning of Year 3. Matures at the end of Year 3, returns 1.40·I. Cap: I4_3 ≤ 100,000.

**Cash Flow Constraints:**
- Beginning of Year 1: Available cash = 500,000. Constraint: I1_1 + I2_1 ≤ 500,000.
- Beginning of Year 2: Available cash = 1.20·I1_1 + 1.50·I2_1 (proceeds from Year 1 product (1) and product (2) maturing at end of Year 2... wait, product (2) matures at end of Year 2, so it is not available at the beginning of Year 2). Correction: Available cash at beginning of Year 2 = 1.20·I1_1 (from product (1) invested in Year 1). Product (2) matures at end of Year 2, so its proceeds are available at the beginning of Year 3. Constraint: I1_2 + I3_2 ≤ 1.20·I1_1.
- Beginning of Year 3: Available cash = 1.20·I1_2 + 1.50·I2_1 + 1.60·I3_2 (proceeds from product (1) invested in Year 2, product (2) maturing at end of Year 2, and product (3) maturing at end of Year 2). Constraint: I1_3 + I4_3 ≤ 1.20·I1_2 + 1.50·I2_1 + 1.60·I3_2.

**Objective Function:** Maximize 1.20·I1_3 + 1.40·I4_3 (total value at end of Year 3 from investments made in Year 3).

**Assumptions:** None. All facts were confirmed by the user.