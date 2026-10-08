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

QUESTION: At the end of Year 3, do you want to maximize the total cash on hand (i.e., the sum of all matured proceeds from investments made in Years 1–3, with no requirement to hold any cash uninvested), or is there a minimum amount of cash that must be kept liquid at the end of Year 3?

## Turn 1 - User Simulator

I want to maximize the total cash on hand at the end of Year 3. There is no minimum amount of cash that must be kept liquid.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), which is available at the beginning of each year, can the proceeds from a product that matures at the end of Year 1 be reinvested in product (1) at the beginning of Year 2, and similarly can proceeds maturing at the end of Year 2 be reinvested in product (1) at the beginning of Year 3?

## Turn 2 - User Simulator

Yes, proceeds from investments that mature at the end of a year can be reinvested in product (1) at the beginning of the following year.

## Turn 3 - Generic Agent

QUESTION: Can the proceeds from product (2), which matures at the end of Year 2, be reinvested in product (4) at the beginning of Year 3?

## Turn 3 - User Simulator

Yes, the proceeds from product (2) can be reinvested in product (4) at the beginning of Year 3.

## Turn 4 - Generic Agent

QUESTION: Can the proceeds from product (3), which matures at the end of Year 2, be reinvested in product (4) at the beginning of Year 3?

## Turn 4 - User Simulator

Yes, the proceeds from product (3) can be reinvested in product (4) at the beginning of Year 3.

## Turn 5 - Generic Agent

QUESTION: Can the proceeds from product (1) that mature at the end of Year 2 be reinvested in product (4) at the beginning of Year 3?

## Turn 5 - User Simulator

Yes, the proceeds from product (1) that mature at the end of Year 2 can be reinvested in product (4) at the beginning of Year 3.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how much can be invested in product (1) in any given year, or is it truly unlimited as stated?

## Turn 6 - User Simulator

Product (1) is truly unlimited; there is no cap on how much can be invested in it in any given year.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in both product (1) and product (2) simultaneously, splitting the initial 500,000 yuan between them?

## Turn 7 - User Simulator

Yes, at the beginning of Year 1, you can invest in both product (1) and product (2) simultaneously, splitting the initial 500,000 yuan between them.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in both product (1) and product (3) simultaneously, splitting the available cash between them?

## Turn 8 - User Simulator

Yes, at the beginning of Year 2, you can invest in both product (1) and product (3) simultaneously, splitting the available cash between them.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in both product (1) and product (4) simultaneously, splitting the available cash between them?

## Turn 9 - User Simulator

Yes, at the beginning of Year 3, you can invest in both product (1) and product (4) simultaneously, splitting the available cash between them.

## Turn 10 - Generic Agent

QUESTION: Is there any requirement that all available cash at the beginning of each year must be fully invested, or is it permissible to hold some cash uninvested (earning no return) at the beginning of a year?

## Turn 10 - User Simulator

It is permissible to hold some cash uninvested at the beginning of a year. There is no requirement that all available cash must be fully invested.

## Turn 11 - Generic Agent

QUESTION: Can cash that is held uninvested at the beginning of a year simply carry over to the end of that year (and thus be available for investment at the beginning of the next year) without any penalty or loss?

## Turn 11 - User Simulator

Yes, cash held uninvested at the beginning of a year carries over to the end of that year without any penalty or loss, and is available for investment at the beginning of the next year.

## Turn 12 - Generic Agent

QUESTION: Is there any borrowing or leverage allowed, or must all investments in each year be funded solely by the initial capital and the proceeds from previously matured investments?

## Turn 12 - User Simulator

No borrowing or leverage is allowed. All investments in each year must be funded solely by the initial capital and the proceeds from previously matured investments.

## Turn 13 - Generic Agent

QUESTION: Are the investment amounts required to be whole numbers (e.g., whole yuan), or can they be any non-negative real number?

## Turn 13 - User Simulator

The investment amounts can be any non-negative real number.

## Turn 14 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**
1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at the end of that year. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, returns 1.50×I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, returns 1.60×I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, returns 1.40×I. Capped at 100,000 yuan.

**Key rules confirmed:**
- At the beginning of Year 1: can split cash between Product (1) and Product (2).
- At the beginning of Year 2: can split cash between Product (1) and Product (3).
- At the beginning of Year 3: can split cash between Product (1) and Product (4).
- Proceeds from any product maturing at the end of a year can be reinvested in any product available at the beginning of the next year.
- Cash may be held uninvested (carries over with no penalty or loss).
- No borrowing or leverage; all investments funded by initial capital and prior proceeds.
- Investment amounts are non-negative real numbers.
- No minimum cash requirement at the end of Year 3.