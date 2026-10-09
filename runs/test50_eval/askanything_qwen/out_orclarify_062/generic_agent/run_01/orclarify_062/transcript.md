## Turn 1 - Generic Agent

QUESTION: Are the annual revenue figures for each restaurant the net profit after all operating expenses, or are they gross revenue from which I should subtract additional costs?

## Turn 1 - User Simulator

The annual revenue figures are the net profit after all operating expenses.

## Turn 2 - Generic Agent

QUESTION: Are the restaurant costs one-time purchase prices, or do they include recurring annual expenses?

## Turn 2 - User Simulator

The restaurant costs are one-time purchase prices.

## Turn 3 - Generic Agent

QUESTION: Can you purchase a restaurant more than once, or is each restaurant available for purchase only once?

## Turn 3 - User Simulator

Each restaurant is available for purchase only once.

## Turn 4 - Generic Agent

READY_TO_MODEL
I understand you need to select a subset of the four available restaurants to purchase, with the goal of maximizing the total annual net profit from the selected restaurants, subject to the constraint that the total one-time purchase cost does not exceed the $6 million investment budget.

Confirmed details:
- Objective: Maximize total annual net profit.
- Constraint: Total one-time purchase cost <= $6,000,000.
- Each restaurant can be purchased at most once (binary decision).
- The annual revenue figures provided are net profits.
- The cost figures are one-time purchase prices.

Data:
- Restaurant A: Profit $15,000, Cost $1,600,000
- Restaurant B: Profit $40,000, Cost $2,500,000
- Restaurant C: Profit $30,000, Cost $1,800,000
- Restaurant D: Profit $50,000, Cost $3,000,000