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

QUESTION: What is the objective of this decision — are you maximizing total profit (revenue from selling the animals minus feed costs), and if so, is the feed cost a one-time cost per animal or a recurring daily cost that should be multiplied by some number of days?

## Turn 1 - User Simulator

Yes, the objective is to maximize total profit, where profit is the selling price minus the feed cost for each animal. The feed cost is a one-time cost per animal, not a recurring daily cost.

## Turn 2 - Generic Agent

QUESTION: Should the number of cows, sheep, and chickens be whole numbers (integers), or can they be fractional values?

## Turn 2 - User Simulator

The number of cows, sheep, and chickens must be whole numbers.

## Turn 3 - Generic Agent

QUESTION: The manure constraint says "total manure produced per day cannot exceed 800 units," but the manure production rates are given per animal per day. Since the animals are raised (not just passing through), does the 800-unit daily manure limit apply to the steady-state total of all animals you keep, meaning the constraint is simply 10·cows + 5·sheep + 3·chickens ≤ 800?

## Turn 3 - User Simulator

Yes, the 800-unit daily manure limit applies to the steady-state total of all animals kept, so the constraint is 10·cows + 5·sheep + 3·chickens ≤ 800.

## Turn 4 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total profit, where profit per animal = selling price − feed cost (one-time cost per animal):
- Cow: $500 − $100 = $400
- Sheep: $200 − $80 = $120
- Chicken: $8 − $5 = $3

**Decision variables:**
- Cows (c), Sheep (s), Chickens (k) — all non-negative integers.

**Constraints:**
1. Manure: 10c + 5s + 3k ≤ 800 (steady-state daily manure, units/day)
2. Chickens: k ≤ 50
3. Cows: c ≥ 10
4. Sheep: s ≥ 20
5. Total animals: c + s + k ≤ 100

**No other constraints or costs apply.** The feed cost is a one-time per-animal cost, not recurring.