# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U10, U11, U12, U13, U14, U2, U3, U4, U5, U6, U7, U8, U9
I need help deciding how many cows, sheep, and chickens to raise for a farm, while ensuring that total manure produced per day cannot exceed 800 units, the number of chickens raised must be at most 50, the number of cows raised must be at least 10, the number of sheep raised must be at least 20, and the total number of animals (cows + sheep + chickens) cannot exceed 100.

Selling prices: cow $500, sheep $200, chicken $8.

Feed costs per animal: cow $100, sheep $80, chicken $5.

Manure production per animal per day: cow 10 units, sheep 5 units, chicken 3 units.

Manure handling capacity: 800 units per day.

Maximum number of chickens allowed: 50.

Minimum number of cows required: 10.

Minimum number of sheep required: 20.

Maximum total number of animals: 100.

## Problem units
- U1 (context): I need help deciding how many cows, sheep, and chickens to raise for a farm.
- U2 (data): Selling prices: cow $500, sheep $200, chicken $8.
- U3 (data): Feed costs per animal: cow $100, sheep $80, chicken $5.
- U4 (data): Manure production per animal per day: cow 10 units, sheep 5 units, chicken 3 units.
- U5 (data): Manure handling capacity: 800 units per day.
- U6 (data): Maximum number of chickens allowed: 50.
- U7 (data): Minimum number of cows required: 10.
- U8 (data): Minimum number of sheep required: 20.
- U9 (data): Maximum total number of animals: 100.
- U10 (constraint): Total manure produced per day cannot exceed 800 units.
- U11 (constraint): Number of chickens raised must be at most 50.
- U12 (constraint): Number of cows raised must be at least 10.
- U13 (constraint): Number of sheep raised must be at least 20.
- U14 (constraint): Total number of animals (cows + sheep + chickens) cannot exceed 100.
- U15 (objective): Maximize total profit, where profit is the difference between the selling price and the feed cost for all animals raised.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without the objective, the agent cannot formulate any optimization model, making the problem ill-posed.
- Problem unit ID: U15
- Semantic hit rule: The agent must explicitly ask about the optimization objective (maximize profit) and/or how profit is defined (difference between selling price and feed cost).
- Reference acceptable questions:
  - What is the objective we are trying to achieve? Is it to maximize profit?
  - How is profit calculated? Is it just the selling price minus the feed cost per animal?
- Failure modes:
  - Assuming the objective is to maximize revenue only (ignoring feed costs).
  - Assuming profit is defined as selling price minus some arbitrary operation cost not specified.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the goal to maximize the total daily profit (total selling revenue minus total feed costs) for the animals you raise?

## Turn 1 - User Simulator

Yes, the goal is to maximize the total profit, which is the selling price for each animal minus its feed cost, across all animals raised.

## Turn 2 - Generic Agent

QUESTION: Are the selling prices and feed costs you provided meant to be applied once per animal as a one-time value, or are they daily rates that apply every day the animals are kept?

## Turn 2 - User Simulator

The selling prices and feed costs are one-time values per animal.

## Turn 3 - Generic Agent

QUESTION: Are the numbers of cows, sheep, and chickens you choose required to be whole numbers (integers), or can they be fractional values?

## Turn 3 - User Simulator

The numbers of cows, sheep, and chickens must be whole numbers.

## Turn 4 - Generic Agent

QUESTION: Are there any additional requirements or constraints beyond the manure limit, chicken maximum, cow minimum, sheep minimum, and total animal maximum that I should include in the model?

## Turn 4 - User Simulator

No, there are no additional requirements or constraints beyond those listed.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total profit, where profit per animal is selling price minus feed cost (cow: $500 - $100 = $400; sheep: $200 - $80 = $120; chicken: $8 - $5 = $3). Confirmed.
- Decision variables: Number of cows, sheep, and chickens to raise. Confirmed.
- Variable domain: All three variables must be non-negative integers. Confirmed.
- Constraints:
  - Total manure produced per day ≤ 800 units (cow: 10, sheep: 5, chicken: 3). Confirmed.
  - Number of chickens ≤ 50. Confirmed.
  - Number of cows ≥ 10. Confirmed.
  - Number of sheep ≥ 20. Confirmed.
  - Total number of animals (cows + sheep + chickens) ≤ 100. Confirmed.
- No additional constraints exist. Confirmed.
- Selling prices and feed costs are one-time values per animal, not daily rates. Confirmed.

No open assumptions remain. All formulation-critical facts are confirmed.