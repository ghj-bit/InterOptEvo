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

QUESTION: At the end of Year 3, can you still hold any money that has not been invested in any product (i.e., cash sitting idle with no return), or must all available funds be allocated to one of the listed products?

## Turn 1 - User Simulator

You can hold uninvested cash at the end of Year 3. There is no requirement that all available funds must be allocated to one of the listed products.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), which is available at the beginning of each year, can you invest in it multiple times within the same year (for example, investing some at the start of Year 1 and then again at the start of Year 2 with proceeds from Year 1), or is there a limit on how many times you can invest in product (1) across the three years?

## Turn 2 - User Simulator

You can invest in product (1) at the beginning of each year (Years 1, 2, and 3). There is no limit on the number of times you can invest in it across the three years, other than the availability of cash at the start of each year.

## Turn 3 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of a year, does the return (1.20·I) become available as cash at the end of that same year, which you can then use to invest in products available at the beginning of the next year?

## Turn 3 - User Simulator

Yes, the return from product (1) becomes available as cash at the end of that year, which you can then use to invest in products available at the beginning of the next year.

## Turn 4 - Generic Agent

QUESTION: For product (2), which is a 2-year product available only at the beginning of Year 1 and matures at the end of Year 2, does the return (1.50·I) become available as cash at the end of Year 2, which you can then use to invest in products available at the beginning of Year 3?

## Turn 4 - User Simulator

Yes, the return from product (2) becomes available as cash at the end of Year 2, which you can then use to invest in products available at the beginning of Year 3.

## Turn 5 - Generic Agent

QUESTION: For product (3), which is a same-year product available at the beginning of Year 2 and matures at the end of Year 2, does the return (1.60·I) become available as cash at the end of Year 2, which you can then use to invest in products available at the beginning of Year 3?

## Turn 5 - User Simulator

Yes, the return from product (3) becomes available as cash at the end of Year 2, which you can then use to invest in products available at the beginning of Year 3.

## Turn 6 - Generic Agent

QUESTION: For product (4), which is a 1-year product available at the beginning of Year 3 and matures at the end of Year 3, does the return (1.40·I) become available as cash at the end of Year 3, and does this count toward the total principal plus interest at the end of Year 3?

## Turn 6 - User Simulator

Yes, the return from product (4) becomes available as cash at the end of Year 3, and it counts toward the total principal plus interest at the end of Year 3.

## Turn 7 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any amount (including zero) in each product?

## Turn 7 - User Simulator

There is no minimum investment amount required for any of the products. You can invest any amount, including zero, in each product.

## Turn 8 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integers), or can they be any continuous value (including fractions of a yuan)?

## Turn 8 - User Simulator

The investment amounts can be any continuous value, including fractions of a yuan. They do not need to be whole numbers.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint on the total amount you can invest across all products in a given year, or is the only limit the cash available at the beginning of that year?

## Turn 9 - User Simulator

The only limit is the cash available at the beginning of that year. There is no separate constraint on the total amount you can invest across all products in a given year.

## Turn 10 - Generic Agent

QUESTION: At the beginning of Year 1, you have 500,000 yuan. Can you invest in both product (1) and product (2) at the beginning of Year 1, as long as the total investment does not exceed 500,000 yuan?

## Turn 10 - User Simulator

Yes, you can invest in both product (1) and product (2) at the beginning of Year 1, as long as the total investment does not exceed 500,000 yuan.

## Turn 11 - Generic Agent

QUESTION: At the beginning of Year 2, the cash available is the sum of returns from product (1) invested in Year 1 and any uninvested cash from Year 1. Can you invest in both product (1) and product (3) at the beginning of Year 2, as long as the total investment does not exceed the cash available at the beginning of Year 2?

## Turn 11 - User Simulator

Yes, you can invest in both product (1) and product (3) at the beginning of Year 2, as long as the total investment does not exceed the cash available at the beginning of Year 2.

## Turn 12 - Generic Agent

QUESTION: At the beginning of Year 3, the cash available is the sum of returns from product (1) invested in Year 2, product (2) invested in Year 1, product (3) invested in Year 2, and any uninvested cash from Year 2. Can you invest in both product (1) and product (4) at the beginning of Year 3, as long as the total investment does not exceed the cash available at the beginning of Year 3?

## Turn 12 - User Simulator

Yes, you can invest in both product (1) and product (4) at the beginning of Year 3, as long as the total investment does not exceed the cash available at the beginning of Year 3.

## Turn 13 - Generic Agent

QUESTION: Is there any constraint that requires you to invest at least some minimum amount in product (1) in each year, or can you choose to invest zero in product (1) in any given year?

## Turn 13 - User Simulator

You can choose to invest zero in product (1) in any given year. There is no minimum investment requirement.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that requires you to invest at least some minimum amount in product (2), product (3), or product (4), or can you choose to invest zero in any of these products?

## Turn 14 - User Simulator

You can choose to invest zero in any of these products. There is no minimum investment requirement for product (2), product (3), or product (4).

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one product in each year, or can you choose to invest zero in all products in a given year and simply carry forward the cash?

## Turn 15 - User Simulator

You can choose to invest zero in all products in a given year and simply carry forward the cash. There is no requirement to invest in at least one product in each year.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that limits how much you can invest in product (1) in a given year, or is product (1) truly unlimited in capacity as stated?

## Turn 16 - User Simulator

Product (1) is truly unlimited in capacity. There is no constraint limiting how much you can invest in product (1) in a given year, other than the cash available at the beginning of that year.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you choose to hold some cash uninvested and carry it forward to the next year?

## Turn 17 - User Simulator

You can choose to hold some cash uninvested and carry it forward to the next year. There is no requirement to invest all available cash at the beginning of each year.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (2) at the beginning of Year 1, or can you choose to invest zero in product (2) and instead invest all your cash in product (1) at the beginning of Year 1?

## Turn 18 - User Simulator

You can choose to invest zero in product (2) and instead invest all your cash in product (1) at the beginning of Year 1. There is no requirement to invest in product (2).

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (3) at the beginning of Year 2, or can you choose to invest zero in product (3) and instead invest all your available cash in product (1) at the beginning of Year 2?

## Turn 19 - User Simulator

You can choose to invest zero in product (3) and instead invest all your available cash in product (1) at the beginning of Year 2. There is no requirement to invest in product (3).

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (4) at the beginning of Year 3, or can you choose to invest zero in product (4) and instead invest all your available cash in product (1) at the beginning of Year 3?

## Turn 20 - User Simulator

You can choose to invest zero in product (4) and instead invest all your available cash in product (1) at the beginning of Year 3. There is no requirement to invest in product (4).

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (1) at the beginning of Year 1, or can you choose to invest zero in product (1) at the beginning of Year 1 and instead invest all your cash in product (2)?

## Turn 21 - User Simulator

You can choose to invest zero in product (1) at the beginning of Year 1 and instead invest all your cash in product (2), subject to the 120,000 yuan cap on product (2).

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (1) at the beginning of Year 2, or can you choose to invest zero in product (1) at the beginning of Year 2 and instead invest all your available cash in product (3)?

## Turn 22 - User Simulator

You can choose to invest zero in product (1) at the beginning of Year 2 and instead invest all your available cash in product (3), subject to the 150,000 yuan cap on product (3).

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (1) at the beginning of Year 3, or can you choose to invest zero in product (1) at the beginning of Year 3 and instead invest all your available cash in product (4)?

## Turn 23 - User Simulator

You can choose to invest zero in product (1) at the beginning of Year 3 and instead invest all your available cash in product (4), subject to the 100,000 yuan cap on product (4).

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (1) at the beginning of Year 1, Year 2, or Year 3, or can you choose to invest zero in product (1) in all three years?

## Turn 24 - User Simulator

You can choose to invest zero in product (1) in all three years. There is no requirement to invest in product (1) in any specific year.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one of the products (1), (2), (3), or (4) at the beginning of Year 1, or can you choose to invest zero in all products at the beginning of Year 1 and simply carry forward the 500,000 yuan cash to Year 2?

## Turn 25 - User Simulator

You can choose to invest zero in all products at the beginning of Year 1 and simply carry forward the 500,000 yuan cash to Year 2.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one of the products (1), (3), or (4) at the beginning of Year 2, or can you choose to invest zero in all products at the beginning of Year 2 and simply carry forward the cash to Year 3?

## Turn 26 - User Simulator

You can choose to invest zero in all products at the beginning of Year 2 and simply carry forward the cash to Year 3.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one of the products (1) or (4) at the beginning of Year 3, or can you choose to invest zero in all products at the beginning of Year 3 and simply carry forward the cash to the end of Year 3?

## Turn 27 - User Simulator

You can choose to invest zero in all products at the beginning of Year 3 and simply carry forward the cash to the end of Year 3.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (2) at the beginning of Year 1, product (3) at the beginning of Year 2, or product (4) at the beginning of Year 3, or can you choose to invest zero in all of these products?

## Turn 28 - User Simulator

You can choose to invest zero in all of these products. There is no requirement to invest in product (2), product (3), or product (4).

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one product in at least one year, or can you choose to invest zero in all products in all three years and simply carry forward the 500,000 yuan cash to the end of Year 3?

## Turn 29 - User Simulator

You can choose to invest zero in all products in all three years and simply carry forward the 500,000 yuan cash to the end of Year 3.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in product (1) at the beginning of Year 1, Year 2, or Year 3, or can you choose to invest zero in product (1) in all three years and instead invest in other products or carry forward cash?

## Turn 30 - User Simulator

You can choose to invest zero in product (1) in all three years and instead invest in other products or carry forward cash.