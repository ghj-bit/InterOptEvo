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

QUESTION: At the end of Year 3, is any money that was not invested in a maturing product (i.e., cash left idle) counted at its face value in the final objective, or must all funds be placed in some product by the end of Year 3?

## Turn 1 - User Simulator

Cash left idle at the end of Year 3 is counted at its face value in the final objective. There is no requirement that all funds must be placed in a product by the end of Year 3.

## Turn 2 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year: is the amount invested in it during a given year limited only by the cash available at the start of that year, or is there also a separate per-year cap on how much can be placed in product (1)?

## Turn 2 - User Simulator

The amount invested in product (1) during a given year is limited only by the cash available at the start of that year. There is no separate per-year cap on product (1).

## Turn 3 - Generic Agent

QUESTION: Can funds be reinvested within the same year — for example, can the proceeds from a product that matures at the end of Year 2 be used to invest in product (4) at the beginning of Year 3, or are investments in a given year restricted to cash that was already on hand at the start of that year?

## Turn 3 - User Simulator

Yes, funds can be reinvested. The proceeds from a product that matures at the end of Year 2 can be used to invest in product (4) at the beginning of Year 3. Investments in a given year are not restricted to cash that was already on hand at the start of that year; they can include proceeds from investments that have already matured.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can any non-negative amount (including zero) be invested in each product?

## Turn 4 - User Simulator

There is no minimum investment amount required for any of the products. Any non-negative amount, including zero, can be invested in each product.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts in each product required to be whole numbers (integer yuan), or can they be any continuous non-negative amount?

## Turn 5 - User Simulator

The investment amounts in each product can be any continuous non-negative amount. They are not required to be whole numbers.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how much cash can be held idle (not invested) at the end of any year, or can any amount be carried forward as cash?

## Turn 6 - User Simulator

There is no limit on how much cash can be held idle at the end of any year. Any amount can be carried forward as cash.

## Turn 7 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax that reduces the amount received when a product matures, or is the full stated return (e.g., 1.20·I, 1.50·I, etc.) received with no deductions?

## Turn 7 - User Simulator

There are no transaction costs, fees, or taxes. The full stated return is received with no deductions.

## Turn 8 - Generic Agent

QUESTION: Can the initial 500,000 yuan at the beginning of Year 1 be split across multiple products simultaneously — for example, investing in both product (1) and product (2) at the start of Year 1 — or must it be allocated to only one product?

## Turn 8 - User Simulator

Yes, the initial 500,000 yuan at the beginning of Year 1 can be split across multiple products simultaneously. It does not have to be allocated to only one product.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 2, can funds be invested in both product (1) and product (3) simultaneously, or is there a restriction that only one of them can be chosen in Year 2?

## Turn 9 - User Simulator

Yes, at the beginning of Year 2, funds can be invested in both product (1) and product (3) simultaneously. There is no restriction that only one of them can be chosen in Year 2.

## Turn 10 - Generic Agent

QUESTION: At the beginning of Year 3, can funds be invested in both product (1) and product (4) simultaneously, or is there a restriction that only one of them can be chosen in Year 3?

## Turn 10 - User Simulator

Yes, at the beginning of Year 3, funds can be invested in both product (1) and product (4) simultaneously. There is no restriction that only one of them can be chosen in Year 3.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in all products at the beginning of a given year cannot exceed the total cash available at that time, or could one invest more than available cash (i.e., is borrowing allowed)?

## Turn 11 - User Simulator

No, borrowing is not allowed. The total amount invested in all products at the beginning of a given year cannot exceed the total cash available at that time.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint on the total amount of cash that can be carried forward from one year to the next, or is there a requirement that a certain minimum amount must be invested each year?

## Turn 12 - User Simulator

There is no constraint on the total amount of cash that can be carried forward from one year to the next, and there is no requirement that a certain minimum amount must be invested each year.

## Turn 13 - Generic Agent

QUESTION: Is there any constraint that the total investment across all products over the entire three-year period cannot exceed some overall budget, or is the only budget constraint the cash available at the start of each year?

## Turn 13 - User Simulator

There is no overall budget constraint across the entire three-year period. The only budget constraint is the cash available at the start of each year.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) across all three years combined cannot exceed some limit, or is product (1) truly unlimited in total over the three years?

## Turn 14 - User Simulator

There is no limit on the total amount invested in product (1) across all three years combined. Product (1) is truly unlimited in total over the three years.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (2) cannot exceed 120,000 yuan in total, or is the 120,000 yuan cap applied per investment (though product (2) is only available at the beginning of Year 1)?

## Turn 15 - User Simulator

The 120,000 yuan cap is applied to the total amount invested in product (2). Since product (2) is only available at the beginning of Year 1, this means the total investment in product (2) cannot exceed 120,000 yuan.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (3) cannot exceed 150,000 yuan in total, or is the 150,000 yuan cap applied per investment (though product (3) is only available at the beginning of Year 2)?

## Turn 16 - User Simulator

The 150,000 yuan cap is applied to the total amount invested in product (3). Since product (3) is only available at the beginning of Year 2, this means the total investment in product (3) cannot exceed 150,000 yuan.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (4) cannot exceed 100,000 yuan in total, or is the 100,000 yuan cap applied per investment (though product (4) is only available at the beginning of Year 3)?

## Turn 17 - User Simulator

The 100,000 yuan cap is applied to the total amount invested in product (4). Since product (4) is only available at the beginning of Year 3, this means the total investment in product (4) cannot exceed 100,000 yuan.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that the total amount of cash plus investments at the end of Year 3 must be at least some minimum value, or is the objective purely to maximize the total without any minimum requirement?

## Turn 18 - User Simulator

There is no minimum value requirement for the total amount of cash plus investments at the end of Year 3. The objective is purely to maximize the total without any minimum requirement.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in all products at the beginning of Year 1 cannot exceed 500,000 yuan, or can the total investment in Year 1 be less than 500,000 yuan with the remainder carried forward as cash?

## Turn 19 - User Simulator

The total amount invested in all products at the beginning of Year 1 cannot exceed 500,000 yuan. The total investment in Year 1 can be less than 500,000 yuan, with the remainder carried forward as cash.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in all products at the beginning of Year 2 cannot exceed the total cash available at the start of Year 2 (which includes cash carried forward from Year 1 plus proceeds from products maturing at the end of Year 1), or can the total investment in Year 2 be less than the available cash with the remainder carried forward?

## Turn 20 - User Simulator

The total amount invested in all products at the beginning of Year 2 cannot exceed the total cash available at the start of Year 2. The total investment in Year 2 can be less than the available cash, with the remainder carried forward.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in all products at the beginning of Year 3 cannot exceed the total cash available at the start of Year 3 (which includes cash carried forward from Year 2 plus proceeds from products maturing at the end of Year 2), or can the total investment in Year 3 be less than the available cash with the remainder carried forward?

## Turn 21 - User Simulator

The total amount invested in all products at the beginning of Year 3 cannot exceed the total cash available at the start of Year 3. The total investment in Year 3 can be less than the available cash, with the remainder carried forward.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the total amount of cash carried forward from Year 1 to Year 2 cannot exceed some limit, or can any amount of cash be carried forward?

## Turn 22 - User Simulator

There is no limit on the total amount of cash carried forward from Year 1 to Year 2. Any amount of cash can be carried forward.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the total amount of cash carried forward from Year 2 to Year 3 cannot exceed some limit, or can any amount of cash be carried forward?

## Turn 23 - User Simulator

There is no limit on the total amount of cash carried forward from Year 2 to Year 3. Any amount of cash can be carried forward.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the total amount of cash carried forward from Year 3 to the end of the planning horizon cannot exceed some limit, or can any amount of cash be carried forward to the end?

## Turn 24 - User Simulator

There is no limit on the total amount of cash carried forward from Year 3 to the end of the planning horizon. Any amount of cash can be carried forward to the end.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) at the beginning of Year 1 cannot exceed some limit, or is the only constraint on product (1) in Year 1 the cash available at the start of Year 1?

## Turn 25 - User Simulator

There is no separate limit on the total amount invested in product (1) at the beginning of Year 1. The only constraint on product (1) in Year 1 is the cash available at the start of Year 1.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) at the beginning of Year 2 cannot exceed some limit, or is the only constraint on product (1) in Year 2 the cash available at the start of Year 2?

## Turn 26 - User Simulator

There is no separate limit on the total amount invested in product (1) at the beginning of Year 2. The only constraint on product (1) in Year 2 is the cash available at the start of Year 2.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) at the beginning of Year 3 cannot exceed some limit, or is the only constraint on product (1) in Year 3 the cash available at the start of Year 3?

## Turn 27 - User Simulator

There is no separate limit on the total amount invested in product (1) at the beginning of Year 3. The only constraint on product (1) in Year 3 is the cash available at the start of Year 3.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (2) at the beginning of Year 1 cannot exceed 120,000 yuan, or is the 120,000 yuan cap on product (2) the only constraint on that product?

## Turn 28 - User Simulator

The 120,000 yuan cap is the only specific constraint on product (2). In addition, the investment in product (2) is also limited by the cash available at the start of Year 1, as with all investments.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (3) at the beginning of Year 2 cannot exceed 150,000 yuan, or is the 150,000 yuan cap on product (3) the only specific constraint on that product?

## Turn 29 - User Simulator

The 150,000 yuan cap is the only specific constraint on product (3). In addition, the investment in product (3) is also limited by the cash available at the start of Year 2, as with all investments.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (4) at the beginning of Year 3 cannot exceed 100,000 yuan, or is the 100,000 yuan cap on product (4) the only specific constraint on that product?

## Turn 30 - User Simulator

The 100,000 yuan cap is the only specific constraint on product (4). In addition, the investment in product (4) is also limited by the cash available at the start of Year 3, as with all investments.