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

QUESTION: At the end of Year 3, do you require all funds to be in cash (i.e., no money may remain tied up in any investment still maturing after Year 3), or is it acceptable to hold investments that mature later as long as their value at the end of Year 3 is counted?

## Turn 1 - User Simulator

All funds must be in cash at the end of Year 3. No money may remain tied up in any investment that matures after Year 3.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum amount that must be kept in cash (uninvested) at the beginning of each year, or can 100% of available cash be invested each year?

## Turn 2 - User Simulator

There is no minimum cash requirement. 100% of available cash can be invested at the beginning of each year.

## Turn 3 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year — is the 1.20 return the same in all three years (Years 1, 2, and 3), or does the rate differ by year?

## Turn 3 - User Simulator

The 1.20 return is the same in all three years (Years 1, 2, and 3).

## Turn 4 - Generic Agent

QUESTION: Can you invest in product (1) at the beginning of Year 3, even though it matures at the end of Year 3 (i.e., it's a 1-year product starting in Year 3 and ending in Year 3)?

## Turn 4 - User Simulator

Yes, you can invest in product (1) at the beginning of Year 3. It matures at the end of Year 3.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total cash at the end of Year 3.
- **Initial capital:** 500,000 yuan at the beginning of Year 1.
- **All funds must be in cash at the end of Year 3** (no investments maturing after Year 3).
- **No minimum cash requirement** — 100% of available cash can be invested each year.

**Investment products:**

| Product | Type | Available | Matures | Return | Cap |
|---------|------|-----------|---------|--------|-----|
| (1) | 1-year | Beginning of Years 1, 2, 3 | End of same year | 1.20×I | Unlimited |
| (2) | 2-year | Beginning of Year 1 only | End of Year 2 | 1.50×I | 120,000 |
| (3) | Same-year | Beginning of Year 2 only | End of Year 2 | 1.60×I | 150,000 |
| (4) | 1-year | Beginning of Year 3 only | End of Year 3 | 1.40×I | 100,000 |

**Key structural points:**
- Product (1) can be purchased in all three years with the same 1.20 return.
- Product (2) ties up capital for 2 years (Year 1 → Year 2).
- Product (3) is a same-year product in Year 2 (beginning → end of Year 2).
- Product (4) is a 1-year product in Year 3 (beginning → end of Year 3).
- Cash flows must balance at the beginning of each year: available cash = prior year's maturing investments + uninvested cash.
- At the end of Year 3, all investments mature and cash is collected.