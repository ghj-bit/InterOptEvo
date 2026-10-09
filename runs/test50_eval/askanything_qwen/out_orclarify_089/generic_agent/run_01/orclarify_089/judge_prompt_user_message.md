# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U9, U2, U3, U4, U5, U6
I need help planning production for liquid products A and B, where total production time must not exceed 40 hours per week and the amount of product A stored per week cannot exceed 4 kilograms.

Profit per kg: product A £30, product B £10.

Production time per kg: product A 6 hours, product B 3 hours.

Maximum weekly production hours: 40 hours.

Storage space required for product A is four times that of product B.

Maximum storage of product A: 4 kg per week.

## Problem units
- U1 (context): I need help planning production for liquid products A and B.
- U2 (data): Profit per kg: product A £30, product B £10.
- U3 (data): Production time per kg: product A 6 hours, product B 3 hours.
- U4 (data): Maximum weekly production hours: 40 hours.
- U5 (data): Storage space required for product A is four times that of product B.
- U6 (data): Maximum storage of product A: 4 kg per week.
- U7 (constraint): Total production time must not exceed 40 hours per week.
- U8 (constraint): Output of product B must be at least three times the output of product A.
- U9 (constraint): The amount of product A stored per week cannot exceed 4 kilograms.

## Hidden slot scoring rules
## H1: minimum_ratio_productB_toA
- Severity: P1
- Severity reason: Without this demand ratio requirement, the agent would formulate a model missing a key business constraint, leading to a materially different and likely invalid optimal plan. The model would be coherent but not reflect the intended problem.
- Problem unit ID: U8
- Semantic hit rule: The agent's question must explicitly mention a demand constraint, a minimum output ratio, or that product B must be at least three times product A.
- Reference acceptable questions:
  - Is there any minimum requirement for how much B we must produce relative to A?
  - Do we need to satisfy a specific ratio between the outputs of product A and product B?
- Failure modes:
  - Assuming no market demand constraint between products A and B.
  - Assuming only that demand must be met but not a specific proportion (e.g., assuming any mix is allowed).


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is there a maximum weekly storage limit for product B, or is its storage effectively unlimited?

## Turn 1 - User Simulator

There is no maximum weekly storage limit specified for product B.

## Turn 2 - Generic Agent

QUESTION: Is there a maximum weekly production limit for product B, or is its production only constrained by the available production hours?

## Turn 2 - User Simulator

There is no maximum weekly production limit specified for product B.

## Turn 3 - Generic Agent

QUESTION: Is there a minimum weekly production requirement for either product A or product B?

## Turn 3 - User Simulator

There is no minimum weekly production requirement for either product A or product B.

## Turn 4 - Generic Agent

QUESTION: Are the production times and storage constraints applied to the total weekly production quantities, or are there separate daily or batch-level constraints?

## Turn 4 - User Simulator

The production times and storage constraints are applied to the total weekly production quantities.

## Turn 5 - Generic Agent

READY_TO_MODEL

I understand you want to maximize weekly profit from producing liquid products A and B.

Let:
- x = kilograms of product A produced per week
- y = kilograms of product B produced per week

Objective:
- Maximize profit = 30x + 10y

Constraints:
- Production time: 6x + 3y ≤ 40 hours
- Storage for product A: x ≤ 4 kg
- Non-negativity: x ≥ 0, y ≥ 0

Note: The statement that "storage space required for product A is four times that of product B" does not create an additional constraint because there is no total storage capacity limit given, and product B has no individual storage limit. The only binding storage constraint is the 4 kg maximum for product A.