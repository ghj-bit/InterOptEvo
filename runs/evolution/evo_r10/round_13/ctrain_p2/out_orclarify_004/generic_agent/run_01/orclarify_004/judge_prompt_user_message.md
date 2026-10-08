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

QUESTION: What is the objective of this decision — are you trying to maximize total profit (selling revenue minus feed cost), maximize total selling revenue, or something else?

## Turn 1 - User Simulator

We want to maximize the total profit. Profit is simply the selling price we get for each animal minus the feed cost for that animal.

## Turn 2 - Generic Agent

QUESTION: Are the numbers of cows, sheep, and chickens required to be whole numbers (you can't raise a fraction of an animal), or is it acceptable to treat them as continuous values?

## Turn 2 - User Simulator

The numbers of cows, sheep, and chickens must be whole numbers.

## Turn 3 - Generic Agent

QUESTION: Is the feed cost a one-time cost per animal, or is it a recurring daily cost that should be multiplied by the number of days the animals are kept?

## Turn 3 - User Simulator

The feed cost is a one-time cost per animal.

## Turn 4 - Generic Agent

QUESTION: Is the manure constraint a daily limit (800 units per day) that applies continuously while the animals are on the farm, or is it a one-time total limit for the entire period?

## Turn 4 - User Simulator

The manure constraint is a daily limit of 800 units per day.

## Turn 5 - Generic Agent

QUESTION: Is there a minimum number of chickens required, or can the number of chickens be zero?

## Turn 5 - User Simulator

There is no minimum number of chickens required. The number of chickens can be zero.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum number of cows or sheep allowed, or are they only bounded below (cows ≥ 10, sheep ≥ 20) and by the total animal cap of 100?

## Turn 6 - User Simulator

There are no specific maximum numbers for cows or sheep. They are only bounded below (cows ≥ 10, sheep ≥ 20) and by the total animal cap of 100.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables (all non-negative integers):**
- C = number of cows
- S = number of sheep
- K = number of chickens

**Objective:** Maximize total profit = (500 − 100)·C + (200 − 80)·S + (8 − 5)·K = 400C + 120S + 3K

**Constraints:**
1. Manure (daily): 10C + 5S + 3K ≤ 800
2. Chickens cap: K ≤ 50
3. Cows floor: C ≥ 10
4. Sheep floor: S ≥ 20
5. Total animals: C + S + K ≤ 100
6. Integrality: C, S, K ∈ ℤ₊ (non-negative integers)

**Notes:**
- Feed cost is one-time per animal (not multiplied by days).
- Manure is a per-day rate; the constraint simply caps the daily total at 800.
- No upper bound on cows or sheep beyond the total-animal cap.
- Chickens can be zero (no lower bound).