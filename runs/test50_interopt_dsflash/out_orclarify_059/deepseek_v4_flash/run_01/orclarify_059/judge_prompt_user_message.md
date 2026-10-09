# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U5, U6, U7, U8, U9, U10, U11, U2
I need help planning the monthly production of three candy brands using three raw materials, where for brand A candy the content of raw material A must be at least 60% and the content of raw material B must be at least 15%, for brand C candy the content of raw material A must be at most 20%, the content of raw material B must be at most 60%, and the content of raw material C must be at most 50%, and the monthly consumption of raw material A cannot exceed 2000 kg, that of raw material B cannot exceed 2500 kg, and that of raw material C cannot exceed 1200 kg.

| Item            | A               | B               | C               | Raw Material Cost (Yuan/kg) | Monthly Limit (kg) |
|:----------------|:---------------|:---------------|:---------------|:-----------------------------|:-------------------|
| A               | ≥ 60%          | ≥ 15%          |                | 2.00                        | 2000               |
| B               |                |                |                | 1.50                        | 2500               |
| C               | ≤ 20%          | ≤ 60%          | ≤ 50%          | 1.00                        | 1200               |
| Processing Fee (Yuan/kg) | 0.50         | 0.40           | 0.30           |                             |                     |
| Selling Price (Yuan/kg)   | 3.40         | 2.85           | 2.25           |                             |                     |

## Problem units
- U1 (context): I need help planning the monthly production of three candy brands using three raw materials.
- U2 (data): | Item            | A               | B               | C               | Raw Material Cost (Yuan/kg) | Monthly Limit (kg) |
|:----------------|:---------------|:---------------|:---------------|:-----------------------------|:-------------------|
| A               | ≥ 60%          | ≥ 15%          |                | 2.00                        | 2000               |
| B               |                |                |                | 1.50                        | 2500               |
| C               | ≤ 20%          | ≤ 60%          | ≤ 50%          | 1.00                        | 1200               |
| Processing Fee (Yuan/kg) | 0.50         | 0.40           | 0.30           |                             |                     |
| Selling Price (Yuan/kg)   | 3.40         | 2.85           | 2.25           |                             |                     |
- U3 (objective): Maximize the monthly profit.
- U4 (constraint): For brand A candy, the content of raw material A must be at least 60%.
- U5 (constraint): For brand A candy, the content of raw material B must be at least 15%.
- U6 (constraint): For brand C candy, the content of raw material A must be at most 20%.
- U7 (constraint): For brand C candy, the content of raw material B must be at most 60%.
- U8 (constraint): For brand C candy, the content of raw material C must be at most 50%.
- U9 (constraint): The monthly consumption of raw material A cannot exceed 2000 kg.
- U10 (constraint): The monthly consumption of raw material B cannot exceed 2500 kg.
- U11 (constraint): The monthly consumption of raw material C cannot exceed 1200 kg.

## Hidden slot scoring rules
## H1: profit_calculation
- Severity: P1
- Severity reason: Without clarification, the agent must guess which cost components are subtracted to compute profit. A wrong assumption (e.g., ignoring raw material costs or processing fees) would make the objective materially inaccurate, leading to a suboptimal or even invalid production plan.
- Problem unit ID: U3
- Semantic hit rule: The agent's question must explicitly ask how profit is calculated, specifically whether raw material costs, processing fees, or both are deducted from revenue.
- Reference acceptable questions:
  - What exactly does 'profit' include? Should we subtract raw material costs, processing fees, or both from the revenue?
  - Is monthly profit defined as total selling price minus total raw material cost and total processing fee?
- Failure modes:
  - Silently assuming profit = revenue − processing fees only, ignoring raw material costs.
  - Silently assuming profit = revenue − raw material costs only, ignoring processing fees.
  - Failing to ask for a precise formula and instead embedding an arbitrary cost subtraction rule in the model.


# Atomic Question Map

Q1 (turn 1): What is the objective for the monthly production plan: maximize profit, minimize cost, or satisfy a required demand?
Q2 (turn 2): Are there any required minimum or maximum monthly production or sales quantities for brands A, B, and C?
Q3 (turn 3): Do the monthly raw material limits apply to total consumption across all three brands combined, or separately to each brand?
Q4 (turn 4): Does brand B candy have any required minimum or maximum percentages for raw materials A, B, or C, or can it be produced from any combination of the three raw materials?
Q5 (turn 5): Must each candy brand use all three raw materials, or can a brand omit one or more raw materials entirely?
Q6 (turn 6): For the purpose of this planning model, should we assume each candy brand may omit one or more raw materials entirely, or should we assume all three raw materials must be used in every brand?
Q7 (turn 7): Since the all-three-materials policy is still pending internal confirmation, may we proceed with the working assumption that each candy brand may omit one or more raw materials entirely, and revisit if the policy differs?
Q8 (turn 8): For the percentage limits on raw materials in brands A and C, should each percentage be calculated as a share of the total candy mass, or as a share of only the raw materials actually included in that brand?
Q9 (turn 9): Should the monthly production quantities for brands A, B, and C be whole kilograms, or can they be fractional kilograms?
Q10 (turn 10): Since the whole-kilogram policy is still pending internal confirmation, may we proceed with the working assumption that monthly production quantities for brands A, B, and C can be fractional kilograms, and revisit if the policy differs?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective for the monthly production plan: maximize profit, minimize cost, or satisfy a required demand?

## Turn 1 - User Simulator

Maximize monthly profit.

## Turn 2 - Generic Agent

QUESTION: Are there any required minimum or maximum monthly production or sales quantities for brands A, B, and C?

## Turn 2 - User Simulator

There are no required minimum or maximum monthly production or sales quantities stated for brands A, B, or C.

## Turn 3 - Generic Agent

QUESTION: Do the monthly raw material limits apply to total consumption across all three brands combined, or separately to each brand?

## Turn 3 - User Simulator

They apply to total monthly consumption across all three brands combined.

## Turn 4 - Generic Agent

QUESTION: Does brand B candy have any required minimum or maximum percentages for raw materials A, B, or C, or can it be produced from any combination of the three raw materials?

## Turn 4 - User Simulator

Brand B candy has no stated minimum or maximum percentages for raw materials A, B, or C, so it can be produced from any combination of the three raw materials.

## Turn 5 - Generic Agent

QUESTION: Must each candy brand use all three raw materials, or can a brand omit one or more raw materials entirely?

## Turn 5 - User Simulator

That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the purpose of this planning model, should we assume each candy brand may omit one or more raw materials entirely, or should we assume all three raw materials must be used in every brand?

## Turn 6 - User Simulator

That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the all-three-materials policy is still pending internal confirmation, may we proceed with the working assumption that each candy brand may omit one or more raw materials entirely, and revisit if the policy differs?

## Turn 7 - User Simulator

Yes, you may proceed with that working assumption and revisit it if the policy differs.

## Turn 8 - Generic Agent

QUESTION: For the percentage limits on raw materials in brands A and C, should each percentage be calculated as a share of the total candy mass, or as a share of only the raw materials actually included in that brand?

## Turn 8 - User Simulator

Each percentage should be calculated as a share of the total candy mass.

## Turn 9 - Generic Agent

QUESTION: Should the monthly production quantities for brands A, B, and C be whole kilograms, or can they be fractional kilograms?

## Turn 9 - User Simulator

That point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Since the whole-kilogram policy is still pending internal confirmation, may we proceed with the working assumption that monthly production quantities for brands A, B, and C can be fractional kilograms, and revisit if the policy differs?

## Turn 10 - User Simulator

Yes, you may proceed with that working assumption and revisit it if the policy differs.

## Turn 11 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.820

Confidence rationale: The objective (maximize monthly profit), raw material cost and processing fee structure, selling prices, shared monthly raw material limits, brand-specific percentage constraints, percentage base (total candy mass), and continuous production quantities are all confirmed. The only unresolved policy point is whether every brand must use all three raw materials; the user has explicitly authorized proceeding with the working assumption that brands may omit one or more raw materials, to be revisited if the policy differs. This is a documented provisional assumption rather than a silent one, so a unique formulation can proceed.

Summary: Maximize monthly profit from producing brands A, B, and C. Decision variables are kilograms of each raw material used in each brand, with total brand output equal to the sum of its raw materials. Revenue uses selling prices A=3.40, B=2.85, C=2.25 Yuan/kg; costs use raw material costs A=2.00, B=1.50, C=1.00 Yuan/kg plus processing fees A=0.50, B=0.40, C=0.30 Yuan/kg. Shared monthly raw material limits: A<=2000 kg, B<=2500 kg, C<=1200 kg. Composition constraints as shares of total candy mass: brand A has raw material A>=60% and raw material B>=15%; brand C has raw material A<=20%, raw material B<=60%, and raw material C<=50%; brand B has no composition restrictions. Working assumptions, to revisit if policy differs: each brand may omit one or more raw materials, and production quantities may be fractional kilograms.