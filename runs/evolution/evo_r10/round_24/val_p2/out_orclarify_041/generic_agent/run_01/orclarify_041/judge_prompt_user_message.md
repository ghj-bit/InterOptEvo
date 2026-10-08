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

QUESTION: At the end of Year 3, do you want to count only the proceeds from investments that mature by then (i.e., product 1 invested in Year 3, product 4, and any cash carried over), or should the value of any still-unmatured investments (such as product 2, which matures at the end of Year 2, so none remain) also be included — and more importantly, is any cash left uninvested at the end of Year 3 simply added to the total at face value?

## Turn 1 - User Simulator

Yes. At the end of Year 3, the total is the sum of:

1.  Proceeds from all investments that mature by the end of Year 3 (including Product 1 invested in Year 3, Product 4, and any other matured products).
2.  Any cash left uninvested at the end of Year 3, added at face value.

Since Product 2 matures at the end of Year 2, there are no still-unmatured investments remaining at the end of Year 3 to value.

## Turn 2 - Generic Agent

QUESTION: When you say "any cash left uninvested at the end of Year 3, added at face value," does that mean cash can simply sit idle with no return (i.e., 1.00 multiplier), or is there a minimum return or penalty for uninvested cash that I should account for?

## Turn 2 - User Simulator

Cash left uninvested at the end of Year 3 is added at face value, meaning it has a 1.00 multiplier. There is no minimum return or penalty for uninvested cash.

## Turn 3 - Generic Agent

QUESTION: For the cash flow constraints, when you say "initial capital at beginning of Year 1: 500,000 yuan," does this mean the total amount available to invest at the start of Year 1 is exactly 500,000 (i.e., you must allocate all of it across products and/or leave it as idle cash), or is it a maximum you can choose to invest less than?

## Turn 3 - User Simulator

The 500,000 yuan is the total amount available to invest at the start of Year 1. You can choose to invest less than the full amount, leaving the remainder as idle cash. You cannot invest more than 500,000 yuan at the start of Year 1.

## Turn 4 - Generic Agent

QUESTION: At the beginning of Year 2, the cash available to invest (in Product 1 Year 2 and Product 3) comes from the proceeds of Product 1 invested in Year 1 plus any idle cash carried over from Year 1. Is that correct, or is there any other source of cash at the start of Year 2?

## Turn 4 - User Simulator

Yes, that is correct. At the beginning of Year 2, the cash available to invest comes from:

1.  Proceeds from Product 1 invested in Year 1.
2.  Any idle cash carried over from Year 1.

There are no other sources of cash at the start of Year 2.

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 3, the cash available to invest (in Product 1 Year 3 and Product 4) comes from the proceeds of Product 1 invested in Year 2, the proceeds of Product 3, the proceeds of Product 2, plus any idle cash carried over from Year 2. Is that correct, or is there any other source of cash at the start of Year 3?

## Turn 5 - User Simulator

Yes, that is correct. At the beginning of Year 3, the cash available to invest comes from:

1.  Proceeds from Product 1 invested in Year 2.
2.  Proceeds from Product 3.
3.  Proceeds from Product 2.
4.  Any idle cash carried over from Year 2.

There are no other sources of cash at the start of Year 3.

## Turn 6 - Generic Agent

QUESTION: Can you invest in Product 1 in all three years (Year 1, Year 2, and Year 3) simultaneously, meaning you could have Product 1 investments maturing at the end of Year 1, end of Year 2, and end of Year 3 all at once?

## Turn 6 - User Simulator

Yes, you can invest in Product 1 in all three years. This means you could have Product 1 investments maturing at the end of Year 1, end of Year 2, and end of Year 3.

## Turn 7 - Generic Agent

QUESTION: Are there any minimum investment amounts for any of the products, or can you invest any non-negative amount (including zero) in each product?

## Turn 7 - User Simulator

You can invest any non-negative amount (including zero) in each product. There are no minimum investment amounts.

## Turn 8 - Generic Agent

QUESTION: Are the investment amounts required to be in whole yuan (integer values), or can they be any continuous non-negative real number?

## Turn 8 - User Simulator

The investment amounts can be any continuous non-negative real number. They do not need to be in whole yuan.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint that limits the total amount you can invest in Product 1 across all three years combined, or is it truly unlimited in each year with no aggregate cap?

## Turn 9 - User Simulator

Product 1 is truly unlimited in each year with no aggregate cap. The only limit on how much you can invest in Product 1 in any given year is the cash available to you at the beginning of that year.

## Turn 10 - Generic Agent

QUESTION: Is there any constraint on the total amount of cash that can be carried over as idle cash from one year to the next, or can any amount of uninvested cash simply roll forward to the next year?

## Turn 10 - User Simulator

There is no constraint on the total amount of cash that can be carried over as idle cash. Any amount of uninvested cash simply rolls forward to the next year.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you choose to leave some cash idle in any year (not just Year 3)?

## Turn 11 - User Simulator

You can choose to leave some cash idle in any year. There is no constraint requiring you to invest all available cash at the beginning of each year.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint on the total amount you can invest across all products in a single year (i.e., a per-year budget cap beyond the cash available), or is the only per-year limit the cash you actually have at the start of that year?

## Turn 12 - User Simulator

The only per-year limit is the cash you actually have at the start of that year. There is no additional per-year budget cap beyond the available cash.

## Turn 13 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 2 must be made entirely at the beginning of Year 1 (i.e., you cannot split it across multiple time points), or could you theoretically invest in it at different times?

## Turn 13 - User Simulator

Product 2 is available only at the beginning of Year 1. Therefore, the total investment in Product 2 must be made entirely at the beginning of Year 1.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 3 must be made entirely at the beginning of Year 2 (i.e., you cannot split it across multiple time points), or could you theoretically invest in it at different times?

## Turn 14 - User Simulator

Product 3 is available only at the beginning of Year 2. Therefore, the total investment in Product 3 must be made entirely at the beginning of Year 2.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 4 must be made entirely at the beginning of Year 3 (i.e., you cannot split it across multiple time points), or could you theoretically invest in it at different times?

## Turn 15 - User Simulator

Product 4 is available only at the beginning of Year 3. Therefore, the total investment in Product 4 must be made entirely at the beginning of Year 3.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in a given year must be made entirely at the beginning of that year (i.e., you cannot invest in it mid-year or at multiple time points within the year)?

## Turn 16 - User Simulator

Yes, investment in Product 1 for a given year must be made entirely at the beginning of that year.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 across all three years combined cannot exceed some aggregate limit, or is it truly unlimited in each year with no aggregate cap?

## Turn 17 - User Simulator

Product 1 is truly unlimited in each year with no aggregate cap.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 2, Product 3, and Product 4 combined cannot exceed some aggregate limit, or are their caps independent of each other?

## Turn 18 - User Simulator

The caps for Product 2, Product 3, and Product 4 are independent of each other. There is no aggregate limit on their combined investment.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000, or can it sum to less than 500,000 (with the remainder simply not existing)?

## Turn 19 - User Simulator

The total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000. The remainder does not simply not exist; it is carried forward as idle cash.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 2 and Product 3, plus any idle cash at the beginning of Year 2, must sum to exactly the cash available at the start of Year 2 (i.e., proceeds from Product 1 Year 1 plus idle cash from Year 1), or can it sum to less than that?

## Turn 20 - User Simulator

The total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3 (i.e., proceeds from Product 1 Year 2, Product 3, Product 2, plus idle cash from Year 2), or can it sum to less than that?

## Turn 21 - User Simulator

The total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000, or can it sum to less than 500,000 (with the remainder simply not existing)?

## Turn 22 - User Simulator

The total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2, or can it sum to less than that?

## Turn 23 - User Simulator

The total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3, or can it sum to less than that?

## Turn 24 - User Simulator

The total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000, or can it sum to less than 500,000 (with the remainder simply not existing)?

## Turn 25 - User Simulator

The total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2, or can it sum to less than that?

## Turn 26 - User Simulator

The total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3, or can it sum to less than that?

## Turn 27 - User Simulator

The total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000, or can it sum to less than 500,000 (with the remainder simply not existing)?

## Turn 28 - User Simulator

The total investment in Product 1 in Year 1, Product 2, and any idle cash at the beginning of Year 1 must sum to exactly 500,000.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2, or can it sum to less than that?

## Turn 29 - User Simulator

The total investment in Product 1 in Year 2, Product 3, and any idle cash at the beginning of Year 2 must sum to exactly the cash available at the start of Year 2.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3, or can it sum to less than that?

## Turn 30 - User Simulator

The total investment in Product 1 in Year 3, Product 4, and any idle cash at the beginning of Year 3 must sum to exactly the cash available at the start of Year 3.