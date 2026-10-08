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

QUESTION: What is the objective of this farm plan — are you maximizing total profit (selling revenue minus feed costs) per animal, and is the feed cost a one-time cost per animal or a recurring daily cost that should be multiplied by some number of days?

## Turn 1 - User Simulator

The objective is to maximize total profit, where profit is the selling price minus the feed cost for all animals raised. The feed cost is a one-time cost per animal, not a recurring daily cost.

## Turn 2 - Generic Agent

QUESTION: Are the numbers of cows, sheep, and chickens required to be whole numbers (integers), or can they be treated as continuous values?

## Turn 2 - User Simulator

The numbers of cows, sheep, and chickens must be whole numbers (integers).

## Turn 3 - Generic Agent

QUESTION: Is there any upper limit on the number of cows or sheep, or are they only bounded below (cows ≥ 10, sheep ≥ 20) and by the total-animal cap of 100?

## Turn 3 - User Simulator

There are no specific upper limits on the number of cows or sheep other than the total-animal cap of 100.

## Turn 4 - Generic Agent

QUESTION: The manure constraint is stated as "total manure produced per day cannot exceed 800 units" — is this a hard constraint that must be satisfied, or is there a penalty/cost for exceeding it that should be included in the objective?

## Turn 4 - User Simulator

The manure constraint is a hard constraint that must be satisfied.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total profit = (500·cows + 200·sheep + 8·chickens) − (100·cows + 80·sheep + 5·chickens), where feed cost is a one-time cost per animal.

**Decision variables:**
- cows, sheep, chickens — non-negative integers

**Constraints:**
1. Manure (hard constraint): 10·cows + 5·sheep + 3·chickens ≤ 800
2. Chickens upper bound: chickens ≤ 50
3. Cows lower bound: cows ≥ 10
4. Sheep lower bound: sheep ≥ 20
5. Total animals: cows + sheep + chickens ≤ 100

**No other upper bounds** on cows or sheep beyond the total-animal cap. All constraints are hard (no penalties).