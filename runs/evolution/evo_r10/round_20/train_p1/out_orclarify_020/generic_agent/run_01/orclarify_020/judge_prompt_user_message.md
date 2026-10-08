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

QUESTION: If they manufacture model cars, they will also manufacture building blocks — does this mean that producing any positive number of model cars forces the building-blocks production to be at least as large as the model-car production (i.e., building blocks ≥ model cars), or does it simply mean that if model cars are produced at all, building blocks must also be produced in some positive amount (with no specific ratio between the two)?

## Turn 1 - User Simulator

It simply means that if model cars are produced at all, building blocks must also be produced in some positive amount. There is no specific ratio or requirement that building blocks must be at least as large as model cars.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities of the four toys required to be whole numbers (you can only make integer units of each toy), or is it acceptable to treat them as continuous quantities (e.g., producing 2.5 robots)?

## Turn 2 - User Simulator

The production quantities must be whole numbers. You can only make integer units of each toy.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum or maximum production limits for any of the four toys (for example, a required minimum number of dolls, or a cap on how many robots can be made), or is the only restriction on each toy's quantity that it be a non-negative integer?

## Turn 3 - User Simulator

There are no minimum or maximum production limits for any of the four toys. The only restriction on each toy's quantity is that it be a non-negative integer.

## Turn 4 - Generic Agent

QUESTION: The brief says "if they manufacture model cars, they will also manufacture building blocks" — is this rule one-way only (producing model cars forces building blocks to be positive, but building blocks can be produced freely without any model cars), or does it work both ways (producing building blocks would also force model cars to be positive)?

## Turn 4 - User Simulator

The rule is one-way only. Producing model cars forces building blocks to be positive, but building blocks can be produced freely without any model cars.

## Turn 5 - Generic Agent

QUESTION: The brief states total plastic used cannot exceed 1200 units and total electronic components cannot exceed 800 units — are these hard ceilings (you may use less than the full amount, and any leftover is simply unused/discarded), or must the full 1200 plastic and 800 components be used up exactly?

## Turn 5 - User Simulator

These are hard ceilings. You may use less than the full amount, and any leftover is simply unused/discarded.

## Turn 6 - Generic Agent

QUESTION: The profit figures ($15, $8, $12, $5) — are these the net profit per unit already after subtracting all material costs, or are they the selling price per unit from which I would still need to subtract the cost of the plastic and electronic components used?

## Turn 6 - User Simulator

These are the net profit per unit, already after subtracting all material costs.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or business rules I should include in the model besides the two resource ceilings (plastic ≤ 1200, electronic components ≤ 800), the one-way model-cars-forces-building-blocks rule, and the non-negative integer requirement — for example, any demand limits, labor constraints, or other rules I haven't asked about yet?

## Turn 7 - User Simulator

Yes, there are two additional constraints:

1. If we decide to manufacture robots, we will not produce any dolls at all.
2. The number of dolls we produce cannot be more than the number of model cars we produce.

## Turn 8 - Generic Agent

QUESTION: For the rule "if we decide to manufacture robots, we will not produce any dolls at all" — is this one-way only (producing robots forces dolls to be zero, but dolls can be produced freely without any robots), or does it work both ways (producing dolls would also force robots to be zero)?

## Turn 8 - User Simulator

The rule is one-way only. Producing robots forces dolls to be zero, but dolls can be produced freely without any robots.

## Turn 9 - Generic Agent

QUESTION: For the rule "the number of dolls we produce cannot be more than the number of model cars we produce" — does this apply in all cases, including when no model cars are produced (which would then force dolls to also be zero), or does this rule only apply when model cars are actually being produced?

## Turn 9 - User Simulator

This rule applies in all cases, including when no model cars are produced. If no model cars are produced, dolls must also be zero.

## Turn 10 - Generic Agent

QUESTION: Are there any further constraints or business rules I should include in the model, or is the complete set now: (1) plastic ≤ 1200, (2) electronic components ≤ 800, (3) model cars > 0 forces building blocks > 0, (4) robots > 0 forces dolls = 0, (5) dolls ≤ model cars, and (6) all quantities are non-negative integers?

## Turn 10 - User Simulator

Yes, that is the complete set of constraints and business rules.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total profit.

**Decision variables:** Non-negative integer production quantities for four toys:
- R = number of robots
- C = number of model cars
- B = number of building blocks
- D = number of dolls

**Profit per unit (net, after material costs):**
- Robot: $15
- Model car: $8
- Building blocks: $12
- Doll: $5

**Resource constraints (hard ceilings, leftover discarded):**
- Plastic: 30R + 10C + 20B + 15D ≤ 1200
- Electronic components: 8R + 5C + 3B + 2D ≤ 800

**Logical constraints:**
1. If C > 0 then B > 0 (one-way: model cars force building blocks to be positive; building blocks can be produced without model cars).
2. If R > 0 then D = 0 (one-way: robots force dolls to zero; dolls can be produced without robots).
3. D ≤ C (applies in all cases, so if C = 0 then D = 0).

**Other:**
- No minimum or maximum production limits beyond non-negativity.
- All quantities must be whole numbers (integers).
- The profit figures are net profit per unit (material costs already deducted).
- This is the complete set of constraints; no other rules apply.