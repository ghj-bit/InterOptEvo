## Turn 1 - Generic Agent

QUESTION: At the end of Year 3, do you want the objective to count only the cash that has actually matured by then (i.e., proceeds from products that paid out by end of Year 3), or should any money still tied up in an unfinished investment also be counted at its face value?

## Turn 1 - User Simulator

The objective should count only the cash that has actually matured by the end of Year 3. All investments in this plan mature by the end of Year 3, so there is no money tied up in unfinished investments at that point.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), which is available at the beginning of each of Years 1, 2, and 3, is the amount you can invest in a given year limited only by the cash you have available at the start of that year, or is there also a separate per-year cap on how much can be put into product (1)?

## Turn 2 - User Simulator

The amount you can invest in product (1) in a given year is limited only by the cash you have available at the start of that year. There is no separate per-year cap on product (1).

## Turn 3 - Generic Agent

QUESTION: When you invest in product (1) at the start of a year and it pays out at that year's end, is that payout cash immediately available to invest in products at the start of the following year, or does it stay separate and only count toward the final Year 3 total?

## Turn 3 - User Simulator

The payout cash is immediately available to invest at the start of the following year.

## Turn 4 - Generic Agent

QUESTION: At the start of each year, is it required that all available cash be invested (i.e., no cash can be held idle), or is it allowed to leave some cash uninvested and carry it forward?

## Turn 4 - User Simulator

It is allowed to leave some cash uninvested and carry it forward.

## Turn 5 - Generic Agent

QUESTION: If cash is left uninvested and carried forward to the next year, does it earn any interest, or does it simply carry over at face value (1.00 times the amount)?

## Turn 5 - User Simulator

It simply carries over at face value (1.00 times the amount).

## Turn 6 - Generic Agent

QUESTION: For product (2), the 2-year product available only at the beginning of Year 1 that matures at the end of Year 2 — is the 120,000 yuan cap on the total amount invested in product (2) over the whole plan, or is it a cap that applies to the single investment made at the beginning of Year 1?

## Turn 6 - User Simulator

It is a cap on the single investment made at the beginning of Year 1.

## Turn 7 - Generic Agent

QUESTION: For product (3), the same-year product available at the beginning of Year 2 that matures at the end of Year 2 — is the 150,000 yuan cap on the single investment made at the beginning of Year 2, or is it a cap on the total amount that can be invested in product (3) over the whole plan?

## Turn 7 - User Simulator

It is a cap on the single investment made at the beginning of Year 2.

## Turn 8 - Generic Agent

QUESTION: For product (4), the 1-year product available at the beginning of Year 3 that matures at the end of Year 3 — is the 100,000 yuan cap on the single investment made at the beginning of Year 3, or is it a cap on the total amount that can be invested in product (4) over the whole plan?

## Turn 8 - User Simulator

It is a cap on the single investment made at the beginning of Year 3.

## Turn 9 - Generic Agent

QUESTION: Are the investment amounts in each product required to be whole yuan amounts (integer), or can they be any fractional amount?

## Turn 9 - User Simulator

They can be any fractional amount.

## Turn 10 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any positive amount (including very small ones) in each product?

## Turn 10 - User Simulator

There is no minimum investment amount. You can invest any positive amount in each product.

## Turn 11 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in both product (1) and product (2) simultaneously, as long as the total does not exceed the 500,000 yuan available?

## Turn 11 - User Simulator

Yes, you can invest in both product (1) and product (2) simultaneously at the beginning of Year 1, as long as the total does not exceed the 500,000 yuan available.

## Turn 12 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in both product (1) and product (3) simultaneously, as long as the total does not exceed the cash available at that time?

## Turn 12 - User Simulator

Yes, you can invest in both product (1) and product (3) simultaneously at the beginning of Year 2, as long as the total does not exceed the cash available at that time.

## Turn 13 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in both product (1) and product (4) simultaneously, as long as the total does not exceed the cash available at that time?

## Turn 13 - User Simulator

Yes, you can invest in both product (1) and product (4) simultaneously at the beginning of Year 3, as long as the total does not exceed the cash available at that time.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that limits the total amount you can invest across all products in a single year, other than the cash available at the start of that year?

## Turn 14 - User Simulator

No, there is no constraint limiting the total amount you can invest across all products in a single year other than the cash available at the start of that year.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that the total amount invested across all years and all products cannot exceed the initial 500,000 yuan, or is the only limit the cash flow constraint (you can only invest what you have available at the start of each year)?

## Turn 15 - User Simulator

The only limit is the cash flow constraint: you can only invest what you have available at the start of each year.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) across all three years (Year 1, Year 2, and Year 3) cannot exceed some limit, or is product (1) truly unlimited in total across the three years?

## Turn 16 - User Simulator

Product (1) is truly unlimited in total across the three years.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (2) plus product (3) plus product (4) combined cannot exceed some limit, or are the only caps the individual ones you already specified (120,000 for product 2, 150,000 for product 3, 100,000 for product 4)?

## Turn 17 - User Simulator

The only caps are the individual ones: 120,000 for product (2), 150,000 for product (3), and 100,000 for product (4).

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) in Year 1 plus the amount invested in product (2) in Year 1 cannot exceed 500,000 yuan, or is the only constraint that the total investment at the start of Year 1 cannot exceed the 500,000 yuan available?

## Turn 18 - User Simulator

The only constraint is that the total investment at the start of Year 1 cannot exceed the 500,000 yuan available.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) in Year 2 plus the amount invested in product (3) in Year 2 cannot exceed the cash available at the start of Year 2, or is the only constraint that the total investment at the start of Year 2 cannot exceed the cash available at that time?

## Turn 19 - User Simulator

The only constraint is that the total investment at the start of Year 2 cannot exceed the cash available at that time.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) in Year 3 plus the amount invested in product (4) in Year 3 cannot exceed the cash available at the start of Year 3, or is the only constraint that the total investment at the start of Year 3 cannot exceed the cash available at that time?

## Turn 20 - User Simulator

The only constraint is that the total investment at the start of Year 3 cannot exceed the cash available at that time.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the cash available at the start of Year 2 must be at least some minimum amount, or can it be any non-negative amount?

## Turn 21 - User Simulator

It can be any non-negative amount.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the cash available at the start of Year 3 must be at least some minimum amount, or can it be any non-negative amount?

## Turn 22 - User Simulator

It can be any non-negative amount.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the final total (principal plus interest) at the end of Year 3 must be at least some minimum amount, or is the objective simply to maximize it without any lower bound?

## Turn 23 - User Simulator

The objective is simply to maximize it without any lower bound.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the amount invested in product (1) in Year 1 must be at least some minimum amount, or can it be any non-negative amount?

## Turn 24 - User Simulator

It can be any non-negative amount.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the amount invested in product (2) must be at least some minimum amount, or can it be any non-negative amount up to the 120,000 yuan cap?

## Turn 25 - User Simulator

It can be any non-negative amount up to the 120,000 yuan cap.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the amount invested in product (3) must be at least some minimum amount, or can it be any non-negative amount up to the 150,000 yuan cap?

## Turn 26 - User Simulator

It can be any non-negative amount up to the 150,000 yuan cap.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the amount invested in product (4) must be at least some minimum amount, or can it be any non-negative amount up to the 100,000 yuan cap?

## Turn 27 - User Simulator

It can be any non-negative amount up to the 100,000 yuan cap.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the amount invested in product (1) in Year 2 must be at least some minimum amount, or can it be any non-negative amount?

## Turn 28 - User Simulator

It can be any non-negative amount.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the amount invested in product (1) in Year 3 must be at least some minimum amount, or can it be any non-negative amount?

## Turn 29 - User Simulator

It can be any non-negative amount.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the cash carried forward from Year 1 to Year 2 must be at least some minimum amount, or can it be any non-negative amount?

## Turn 30 - User Simulator

It can be any non-negative amount.