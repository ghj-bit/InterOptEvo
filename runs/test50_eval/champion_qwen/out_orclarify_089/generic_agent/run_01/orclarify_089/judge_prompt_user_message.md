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

QUESTION: Is the 4 kg limit on product A a cap on the amount produced each week, or a cap on the amount carried over into storage at the end of the week (with the rest sold immediately)?

## Turn 1 - User Simulator

It is a cap on the amount carried over into storage at the end of the week.

## Turn 2 - Generic Agent

QUESTION: Is there any demand limit on how much of products A and B can be sold each week, or can you sell everything you produce?

## Turn 2 - User Simulator

There is no demand limit on how much of products A and B can be sold each week. We can sell everything we produce.

## Turn 3 - Generic Agent

QUESTION: Is the 40-hour limit a cap on total production time per week, or is it a fixed amount of production time that must be fully used?

## Turn 3 - User Simulator

It is a cap on total production time per week.

## Turn 4 - Generic Agent

QUESTION: Is there any storage limit on product B, or can any amount of B be carried over into storage?

## Turn 4 - User Simulator

There is no storage limit on product B.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how much of product B can be produced per week, other than the 40-hour production cap?

## Turn 5 - User Simulator

No, there is no limit on how much of product B can be produced per week other than the 40-hour production cap.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit from production, or is there another goal such as minimizing production time or meeting a target output?

## Turn 6 - User Simulator

The objective is to maximize total weekly profit from production.

## Turn 7 - Generic Agent

QUESTION: Is the 4 kg storage cap on product A the only storage constraint, or is there also a total storage space limit that applies to both A and B combined?

## Turn 7 - User Simulator

The 4 kg storage cap on product A is the only storage constraint.

## Turn 8 - Generic Agent

QUESTION: Is the 4 kg storage cap on product A a weekly limit that resets each week, or is it a cumulative limit over a longer planning horizon?

## Turn 8 - User Simulator

It is a weekly limit that resets each week.

## Turn 9 - Generic Agent

QUESTION: Is the 40-hour production cap also a weekly limit that resets each week, or is it a cumulative limit over a longer planning horizon?

## Turn 9 - User Simulator

It is a weekly limit that resets each week.

## Turn 10 - Generic Agent

QUESTION: Is the production plan for a single week, or do you need a multi-week plan where decisions in one week affect the next?

## Turn 10 - User Simulator

It is a single-week plan.

## Turn 11 - Generic Agent

QUESTION: Is there any minimum production requirement for either product A or product B, or can you produce zero of either?

## Turn 11 - User Simulator

There is a minimum production requirement: we must produce at least three times as much product B as product A each week.

## Turn 12 - Generic Agent

QUESTION: Is the minimum production requirement that product B must be at least three times product A, or is it that product A must be at least three times product B?

## Turn 12 - User Simulator

It is that product B must be at least three times product A.

## Turn 13 - Generic Agent

QUESTION: Is the "at least three times as much product B as product A" requirement based on kilograms produced, or on production hours used?

## Turn 13 - User Simulator

It is based on kilograms produced.

## Turn 14 - Generic Agent

QUESTION: Is there any other constraint or requirement I haven't asked about yet, such as a minimum production level for either product, a maximum production level for either product, or any other business rule?

## Turn 14 - User Simulator

No, there are no other constraints or requirements.

## Turn 15 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** A and B, measured in kg.
- **Objective:** Maximize total weekly profit = 30·A + 10·B (£).
- **Decision variables:** kg of A produced (A) and kg of B produced (B) in the week.
- **Production time cap:** 6·A + 3·B ≤ 40 hours (weekly cap, not a fixed usage).
- **Storage cap on A:** amount of A carried over into storage at end of week ≤ 4 kg (weekly, resets each week). Since everything produced can be sold and there is no demand limit, the carried-over amount is a choice up to what is produced; the binding interpretation is that at most 4 kg of A may be held in storage at week end.
- **Storage on B:** no limit.
- **Ratio requirement:** B ≥ 3·A (based on kg produced).
- **No demand limits, no minimum production levels, no other constraints.**
- **Single-week plan.**

Note: The brief's statement that "storage space required for product A is four times that of product B" does not create an additional constraint, since the only storage limit is the 4 kg cap on A and there is no total storage space limit.