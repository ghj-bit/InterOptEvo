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

QUESTION: If they manufacture model cars, they will also manufacture building blocks — does this mean that producing any model cars (even one unit) requires producing at least one unit of building blocks, or does it mean the number of building blocks produced must be at least as large as the number of model cars produced?

## Turn 1 - User Simulator

It means that producing any model cars (even one unit) requires producing at least one unit of building blocks.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities for each toy type required to be whole numbers (you can't make half a robot), or can they be treated as continuous values?

## Turn 2 - User Simulator

The production quantities for each toy type must be whole numbers.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many units of each toy type can be produced, or is the only restriction the plastic and electronic component availability?

## Turn 3 - User Simulator

The only restrictions are the plastic and electronic component availability.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum production requirements for any of the toy types, or can the production of any toy type be zero?

## Turn 4 - User Simulator

There are no minimum production requirements. The production of any toy type can be zero.

## Turn 5 - Generic Agent

QUESTION: Regarding the model car / building blocks rule — if no model cars are produced, is it still allowed to produce building blocks on their own?

## Turn 5 - User Simulator

Yes, if no model cars are produced, it is still allowed to produce building blocks on their own.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Non-negative integer production quantities for four toy types: robot (R), model car (C), building blocks (B), doll (D).
- **Objective:** Maximize total profit = 15R + 8C + 12B + 5D.
- **Constraints:**
  - Plastic: 30R + 10C + 20B + 15D ≤ 1200
  - Electronic components: 8R + 5C + 3B + 2D ≤ 800
  - Conditional rule: If C > 0 then B ≥ 1 (i.e., producing any model cars requires producing at least one building block). If C = 0, building blocks may still be produced freely.
- **No other restrictions:** No per-product upper bounds, no minimum production requirements, no other resource constraints.
- **Integrality:** All production quantities must be whole numbers (non-negative integers).