# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U9, U2, U3, U4
I need help creating a production plan for toys to maximize profit. The objective is to maximize total profit. Total plastic used cannot exceed 1200 units, and total electronic components used cannot exceed 800 units. However, if they manufacture model cars, they will also manufacture building blocks.

Profit per unit: robot $15, model car $8, building blocks $12, doll $5.

Plastic: 1200 units available. Each robot requires 30 units, model car 10 units, building blocks 20 units, doll 15 units.

Electronic components: 800 units available. Each robot requires 8 units, model car 5 units, building blocks 3 units, doll 2 units.

## Problem units
- U1 (context): I need help creating a production plan for toys to maximize profit.
- U2 (data): Profit per unit: robot $15, model car $8, building blocks $12, doll $5.
- U3 (data): Plastic: 1200 units available. Each robot requires 30 units, model car 10 units, building blocks 20 units, doll 15 units.
- U4 (data): Electronic components: 800 units available. Each robot requires 8 units, model car 5 units, building blocks 3 units, doll 2 units.
- U5 (objective): Maximize total profit.
- U6 (constraint): Total plastic used cannot exceed 1200 units.
- U7 (constraint): Total electronic components used cannot exceed 800 units.
- U8 (constraint): If Bright Future Toys manufactures robots, they will not manufacture dolls.
- U9 (constraint): However, if they manufacture model cars, they will also manufacture building blocks.
- U10 (constraint): The number of dolls manufactured cannot exceed the number of model cars manufactured.

## Hidden slot scoring rules
## H1: robot_doll_mutual_exclusion
- Severity: P1
- Severity reason: Without this conditional constraint, the optimization model would allow simultaneous production of robots and dolls, which is prohibited by the business rule, leading to an invalid production plan.
- Problem unit ID: U8
- Semantic hit rule: Agent's question must express the need to know whether manufacturing robots prevents making dolls, or inquire about production restrictions between robots and dolls.
- Reference acceptable questions:
  - Are there any restrictions on producing robots and dolls together?
  - Is it possible to make both robots and dolls, or must we choose one?
- Failure modes:
  - Assuming robots and dolls can both be manufactured simultaneously
  - Assuming no mutual exclusivity between any product types

## H2: doll_model_car_quantity_limit
- Severity: P1
- Severity reason: Without this constraint, the model would allow manufacturing more dolls than model cars, violating the business rule and producing an infeasible production plan.
- Problem unit ID: U10
- Semantic hit rule: Agent's question must explicitly mention the relationship between the quantities of dolls and model cars, specifically whether doll count is capped by model car count.
- Reference acceptable questions:
  - Is there any limit on how many dolls we can produce compared to model cars?
  - Must doll production be less than or equal to model car production?
- Failure modes:
  - Assuming doll production can be arbitrarily higher than model car production
  - Assuming no linking constraint between dolls and model cars


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are the production quantities for each toy type required to be whole numbers, or can they be fractional?

## Turn 1 - User Simulator

The production quantities for each toy type must be whole numbers.

## Turn 2 - Generic Agent

QUESTION: Is the rule "if they manufacture model cars, they will also manufacture building blocks" a requirement that the number of building blocks produced must be at least equal to the number of model cars produced, or is it simply that if any model cars are produced then at least one building block must also be produced?

## Turn 2 - User Simulator

It is simply that if any model cars are produced, then at least one building block must also be produced.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum production requirements for any of the four toy types, or is it acceptable to produce zero units of any given toy?

## Turn 3 - User Simulator

It is acceptable to produce zero units of any given toy.

## Turn 4 - Generic Agent

QUESTION: Are there any upper limits on how many units of each individual toy type can be produced, or are the only limits the total plastic and electronic component constraints?

## Turn 4 - User Simulator

The only limits are the total plastic and electronic component constraints.

## Turn 5 - Generic Agent

QUESTION: Are there any other requirements or constraints on the production plan, such as minimum demand levels, labor limits, or storage capacity, that are not already covered by the plastic and electronic component limits?

## Turn 5 - User Simulator

Yes, there are two additional constraints:

1. If we decide to manufacture robots, we will not produce any dolls at all.
2. The number of dolls we produce cannot be more than the number of model cars we produce.

## Turn 6 - Generic Agent

QUESTION: Is the constraint that the number of dolls produced cannot exceed the number of model cars produced a hard limit that must always be satisfied, or is it a soft target that can be violated if it helps maximize profit?

## Turn 6 - User Simulator

It is a hard limit that must always be satisfied.

## Turn 7 - Generic Agent

QUESTION: Is the constraint that if robots are manufactured then no dolls are produced a hard limit that must always be satisfied, or is it a soft target that can be violated if it helps maximize profit?

## Turn 7 - User Simulator

It is a hard limit that must always be satisfied.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total profit.

**Decision Variables:**
- Let R = number of robots produced (non-negative integer)
- Let C = number of model cars produced (non-negative integer)
- Let B = number of building blocks produced (non-negative integer)
- Let D = number of dolls produced (non-negative integer)

**Profit Coefficients (confirmed):**
- Robot: $15 per unit
- Model car: $8 per unit
- Building blocks: $12 per unit
- Doll: $5 per unit

**Objective Function:** Maximize 15R + 8C + 12B + 5D

**Resource Constraints (confirmed):**
- Plastic: 30R + 10C + 20B + 15D ≤ 1200
- Electronic components: 8R + 5C + 3B + 2D ≤ 800

**Logical Constraints (confirmed):**
1. If C > 0, then B ≥ 1 (if any model cars are produced, at least one building block must also be produced).
2. If R > 0, then D = 0 (if any robots are produced, no dolls may be produced).
3. D ≤ C (the number of dolls produced cannot exceed the number of model cars produced).

**Variable Domains (confirmed):**
- All variables are non-negative integers.

**No other constraints (confirmed):**
- No minimum production requirements for any toy type.
- No upper limits on individual toy types beyond the resource constraints.
- No labor, storage, or demand constraints.

**No open assumptions.** All formulation-critical facts have been confirmed by the client.