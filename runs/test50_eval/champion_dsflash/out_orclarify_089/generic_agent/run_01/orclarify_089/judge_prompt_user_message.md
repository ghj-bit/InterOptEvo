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

QUESTION: Is the storage limit of 4 kg for product A a hard cap on how much A can be stored, or is it a cap on how much A can be produced per week?

## Turn 1 - User Simulator

It is a hard cap on how much product A can be stored per week.

## Turn 2 - Generic Agent

QUESTION: Does the storage space constraint apply to product B as well, or only to product A?

## Turn 2 - User Simulator

The storage space constraint applies only to product A.

## Turn 3 - Generic Agent

QUESTION: Since product A takes four times the storage space of product B, is there a total storage capacity limit that both products share, or is the only storage limit the 4 kg cap on product A?

## Turn 3 - User Simulator

The only storage limit is the 4 kg cap on product A.

## Turn 4 - Generic Agent

QUESTION: Can the production quantities of A and B be fractional (any real number of kg), or must they be whole kilograms?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum production requirement for either product, or can either product be zero in a given week?

## Turn 5 - User Simulator

There is a minimum production requirement: we must produce at least three times as much product B as product A each week.

## Turn 6 - Generic Agent

QUESTION: Does "at least three times as much product B as product A" mean B ≥ 3A in kilograms?

## Turn 6 - User Simulator

Yes, B ≥ 3A in kilograms.

## Turn 7 - Generic Agent

QUESTION: Is the goal to maximize total weekly profit, with no other objective such as minimizing time or storage?

## Turn 7 - User Simulator

Yes, the goal is to maximize total weekly profit.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** weekly production quantities of product A and product B, in kilograms. Whether these must be whole kilograms is still pending internal confirmation; I will model them as continuous (fractional kg allowed) unless told otherwise.
- **Objective:** maximize total weekly profit = 30·A + 10·B (profit per kg: A £30, B £10).
- **Production time constraint:** 6·A + 3·B ≤ 40 hours per week.
- **Storage constraint:** A ≤ 4 kg per week. This is a hard cap on how much A is stored per week, and it applies only to product A. There is no shared total-storage limit and no storage limit on B.
- **Minimum production requirement:** B ≥ 3·A (in kilograms).
- **Non-negativity:** A ≥ 0, B ≥ 0; either product may be zero subject to the minimum-ratio rule.

Model:

maximize  30A + 10B
subject to
  6A + 3B ≤ 40
  A ≤ 4
  B ≥ 3A
  A ≥ 0, B ≥ 0

One open item: whether A and B must be integer kilograms (pending internal confirmation). I have modeled them as continuous.