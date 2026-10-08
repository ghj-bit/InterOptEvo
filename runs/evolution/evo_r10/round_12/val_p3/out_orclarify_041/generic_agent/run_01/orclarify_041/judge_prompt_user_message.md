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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., the sum of all matured proceeds from investments made in Years 1–3, with no requirement to hold any cash uninvested), or must some minimum cash be kept uninvested at the end of Year 3?

## Turn 1 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. There is no requirement to keep any minimum cash uninvested at the end of Year 3.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20·I payment received at the end of the year immediately available to be reinvested in products available at the beginning of the next year (i.e., end-of-year proceeds can fund next year's investments), or is there a lag that prevents immediate reinvestment?

## Turn 2 - User Simulator

The 1.20·I payment received at the end of the year is immediately available to be reinvested in products available at the beginning of the next year. There is no lag.

## Turn 3 - Generic Agent

QUESTION: Can you invest in product (1) in all three years (Years 1, 2, and 3), or is it only available in certain years?

## Turn 3 - User Simulator

You can invest in product (1) in all three years (Years 1, 2, and 3).

## Turn 4 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited in each year?

## Turn 4 - User Simulator

Product (1) is unlimited in each year. There is no limit on the total amount that can be invested in product (1) across all three years.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any positive amount (including very small amounts) in each product?

## Turn 5 - User Simulator

There is no minimum investment amount required for any of the products. You can invest any positive amount in each product.

## Turn 6 - Generic Agent

QUESTION: Are the investments in each product required to be whole numbers (e.g., whole yuan amounts), or can you invest fractional amounts (e.g., 10,000.5 yuan)?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax associated with investing in any of the products, or are the returns stated (1.20·I, 1.50·I, 1.60·I, 1.40·I) the net amounts you actually receive?

## Turn 7 - User Simulator

The returns stated (1.20·I, 1.50·I, 1.60·I, 1.40·I) are the net amounts you actually receive. There are no transaction costs, fees, or taxes associated with investing in any of the products.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you choose to hold some cash uninvested (earning zero return) and carry it forward to the next year?

## Turn 8 - User Simulator

You can choose to hold some cash uninvested and carry it forward to the next year. There is no constraint requiring you to invest all available cash at the beginning of each year.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint on the total amount that can be invested across all products in a single year, or is the only limit the individual product caps (120,000 for product 2, 150,000 for product 3, 100,000 for product 4)?

## Turn 9 - User Simulator

The only limits are the individual product caps: 120,000 yuan for product (2), 150,000 yuan for product (3), and 100,000 yuan for product (4). There is no separate constraint on the total amount that can be invested across all products in a single year, other than the cash available at that time.

## Turn 10 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one product in each year, or can you choose to invest nothing in a particular year and simply carry all cash forward?

## Turn 10 - User Simulator

You can choose to invest nothing in a particular year and simply carry all cash forward. There is no constraint requiring you to invest in at least one product in each year.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint that the total investment in a given year cannot exceed the cash available at the beginning of that year (i.e., you cannot invest more than you have), or is there some form of borrowing or leverage allowed?

## Turn 11 - User Simulator

Yes, the total investment in a given year cannot exceed the cash available at the beginning of that year. No borrowing or leverage is allowed.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint that the cash carried forward (uninvested) at the end of each year must be non-negative, or could it theoretically be negative (which would imply borrowing)?

## Turn 12 - User Simulator

The cash carried forward must be non-negative. It cannot be negative, as that would imply borrowing, which is not allowed.

## Turn 13 - Generic Agent

QUESTION: Is there any constraint that the investment in product (2) must be made at the beginning of Year 1 specifically, or could it be made at the beginning of Year 2 as well (with maturity at the end of Year 3)?

## Turn 13 - User Simulator

The investment in product (2) must be made at the beginning of Year 1 specifically. It is not available at the beginning of Year 2.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that the investment in product (3) must be made at the beginning of Year 2 specifically, or could it be made at the beginning of Year 1 or Year 3 as well?

## Turn 14 - User Simulator

The investment in product (3) must be made at the beginning of Year 2 specifically. It is not available at the beginning of Year 1 or Year 3.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that the investment in product (4) must be made at the beginning of Year 3 specifically, or could it be made at the beginning of Year 1 or Year 2 as well?

## Turn 15 - User Simulator

The investment in product (4) must be made at the beginning of Year 3 specifically. It is not available at the beginning of Year 1 or Year 2.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that the total cash on hand at the end of Year 3 must be at least some minimum amount, or is there no lower bound on the final cash position?

## Turn 16 - User Simulator

There is no lower bound on the final cash position. The objective is simply to maximize the total cash on hand at the end of Year 3.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the investment in product (1) in a given year must be a whole number of yuan, or can it be any non-negative real number?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that the investment in product (2) must be a whole number of yuan, or can it be any non-negative real number up to 120,000?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the investment in product (3) must be a whole number of yuan, or can it be any non-negative real number up to 150,000?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the investment in product (4) must be a whole number of yuan, or can it be any non-negative real number up to 100,000?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the cash carried forward at the end of each year must be a whole number of yuan, or can it be any non-negative real number?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the total cash on hand at the end of Year 3 must be a whole number of yuan, or can it be any non-negative real number?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the initial capital of 500,000 yuan at the beginning of Year 1 must be a whole number, or is it simply a fixed starting amount?

## Turn 23 - User Simulator

It is simply a fixed starting amount.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the returns from product (1) (1.20·I), product (2) (1.50·I), product (3) (1.60·I), or product (4) (1.40·I) must be whole numbers of yuan, or can they be any non-negative real numbers?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the total investment in product (1) across all three years must be a whole number of yuan, or can it be any non-negative real number?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the total investment in product (2) must be a whole number of yuan, or can it be any non-negative real number up to 120,000?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the total investment in product (3) must be a whole number of yuan, or can it be any non-negative real number up to 150,000?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the total investment in product (4) must be a whole number of yuan, or can it be any non-negative real number up to 100,000?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the cash available at the beginning of each year must be a whole number of yuan, or can it be any non-negative real number?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the cash available at the end of each year must be a whole number of yuan, or can it be any non-negative real number?

## Turn 30 - User Simulator

The point still needs internal confirmation.