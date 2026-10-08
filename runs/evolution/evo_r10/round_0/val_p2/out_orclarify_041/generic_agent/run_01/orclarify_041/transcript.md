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