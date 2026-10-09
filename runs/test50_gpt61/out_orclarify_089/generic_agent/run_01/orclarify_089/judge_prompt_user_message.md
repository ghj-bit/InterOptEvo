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

QUESTION: Is there also a maximum total storage capacity for products A and B, or is the only storage constraint that product A cannot exceed 4 kg per week?

## Turn 1 - User Simulator

The only storage constraint is that product A cannot exceed 4 kg per week. There is no separate maximum total storage capacity for products A and B combined.

## Turn 2 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Let \(A\) be kilograms of product A produced per week.
- Let \(B\) be kilograms of product B produced per week.
- Weekly profit is \(£30A + £10B\).
- Production time is limited to 40 hours:
  \[
  6A + 3B \le 40
  \]
- Product A storage is limited to 4 kg:
  \[
  A \le 4
  \]
- Production quantities cannot be negative:
  \[
  A, B \ge 0
  \]
- There is no combined storage limit. Therefore, the statement that A requires four times the storage of B does not affect the current model.
- Assuming production quantities may be fractional kilograms.

Because product A earns £5 per production hour, while product B earns approximately £3.33 per production hour, produce as much A as permitted:

\[
A = 4
\]

This uses:

\[
6(4)=24\text{ hours}
\]

The remaining 16 hours are used for product B:

\[
B=\frac{16}{3}=5.33\text{ kg}
\]

Maximum weekly profit:

\[
30(4)+10\left(\frac{16}{3}\right)
= £173.33
\]

**Recommended weekly production:**

- Product A: **4 kg**
- Product B: **5.33 kg**
- Total production time: **40 hours**
- Maximum profit: **£173.33 per week**