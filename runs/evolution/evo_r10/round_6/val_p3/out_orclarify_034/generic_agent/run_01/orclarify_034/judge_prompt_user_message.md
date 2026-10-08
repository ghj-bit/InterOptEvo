# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U7, U8, U9, U10, U2, U3, U4, U5
I need help creating a container packing plan to transport a batch of goods, where any container that is used must be loaded with at least 18 tons and no more than 60 tons of goods, each container must contain at least 12 units of type D goods, if a container contains any type A then it must also contain at least one type C (but loading C alone does not require A), and the total units of each goods type across all containers cannot exceed the available quantities of 120 for A, 90 for B, 300 for C, 90 for D, and 120 for E.

Goods types, available quantities, and unit weights: A: 120 units, 0.5 tons/unit; B: 90 units, 1 ton/unit; C: 300 units, 0.4 tons/unit; D: 90 units, 0.6 tons/unit; E: 120 units, 0.65 tons/unit.

Maximum weight capacity per container: 60 tons.

Minimum weight per used container: 18 tons.

Minimum number of D goods per container: 12.

## Problem units
- U1 (context): I need help creating a container packing plan to transport a batch of goods.
- U2 (data): Goods types, available quantities, and unit weights: A: 120 units, 0.5 tons/unit; B: 90 units, 1 ton/unit; C: 300 units, 0.4 tons/unit; D: 90 units, 0.6 tons/unit; E: 120 units, 0.65 tons/unit.
- U3 (data): Maximum weight capacity per container: 60 tons.
- U4 (data): Minimum weight per used container: 18 tons.
- U5 (data): Minimum number of D goods per container: 12.
- U6 (constraint): Total weight of goods in any container must not exceed 60 tons.
- U7 (constraint): If a container is used, it must be loaded with at least 18 tons of goods.
- U8 (constraint): The total number of units of each goods type loaded across all containers cannot exceed the available quantities (A: 120, B: 90, C: 300, D: 90, E: 120).
- U9 (constraint): If a container contains any units of type A, then it must contain at least one unit of type C. Loading C alone does not require loading A.
- U10 (constraint): Each container must contain at least 12 units of type D goods.
- U11 (objective): Minimize the total number of containers used.

## Hidden slot scoring rules
## H1: missing_objective_minimize_containers
- Severity: P0
- Severity reason: Without knowing the objective, a modeling agent cannot formulate a meaningful optimization model. The problem statement implies minimizing containers, but if this is hidden, the agent might assume a different objective (e.g., maximize space utilization, minimize cost), leading to a fundamentally different model. This is a fatal gap that must be clarified before modeling.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must explicitly mention the objective of minimizing the number of containers or ask what the optimization goal is (e.g., 'What are we trying to optimize?', 'Should we minimize the number of containers?').
- Reference acceptable questions:
  - What is the goal of the packing plan? Are we trying to minimize the number of containers used?
  - Should we aim to use as few containers as possible, or is there another objective like minimizing cost or maximizing utilization?
- Failure modes:
  - Assuming the objective is to minimize total cost or maximize space utilization instead of minimizing container count.
  - Assuming a multi-objective model without clarifying that the primary goal is fewest containers.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective of the plan — are we minimizing the number of containers used, minimizing total transportation cost, or maximizing the total amount of goods shipped?

## Turn 1 - User Simulator

We are minimizing the number of containers used.

## Turn 2 - Generic Agent

QUESTION: Do all available goods have to be shipped, or is it acceptable to leave some units of any type unshipped?

## Turn 2 - User Simulator

All available goods have to be shipped.

## Turn 3 - Generic Agent

QUESTION: Is the number of containers available unlimited, or is there a fixed fleet size that we must work within?

## Turn 3 - User Simulator

The number of containers is unlimited; we just want to use as few as possible.

## Turn 4 - Generic Agent

QUESTION: Are the goods units indivisible (each unit must be whole, so container loads are integer numbers of units), or can units be split fractionally?

## Turn 4 - User Simulator

The goods units are indivisible; each container must contain whole units of each goods type.

## Turn 5 - Generic Agent

QUESTION: The rule "if a container contains any type A then it must also contain at least one type C" — does this apply to every container that has A, including the case where a container has A but zero of every other type?

## Turn 5 - User Simulator

Yes, that rule applies to every container that contains any type A. If a container has A, it must also contain at least one unit of type C, regardless of what else is in that container.

## Turn 6 - Generic Agent

QUESTION: The minimum of 12 units of type D per container — does this apply to every container that is used, or only to containers that actually contain type D?

## Turn 6 - User Simulator

This applies to every container that is used.

## Turn 7 - Generic Agent

QUESTION: The 18-ton minimum applies to every used container — does this mean a container that is opened must be filled to at least 18 tons, and we cannot leave a container partially loaded below 18 tons?

## Turn 7 - User Simulator

Yes, any container that is used must be loaded with at least 18 tons of goods.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many units of a single goods type can go into one container, or can a container hold all of one type as long as the weight and the other rules are satisfied?

## Turn 8 - User Simulator

There is no limit on how many units of a single goods type can go into one container, as long as the weight and the other rules are satisfied.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Minimize the number of containers used.

**Goods (all must be shipped, units indivisible/integer):**
- A: 120 units, 0.5 tons/unit
- B: 90 units, 1 ton/unit
- C: 300 units, 0.4 tons/unit
- D: 90 units, 0.6 tons/unit
- E: 120 units, 0.65 tons/unit

**Container constraints (apply to every used container):**
- Weight between 18 tons (min) and 60 tons (max).
- At least 12 units of type D.
- If it contains any type A (≥1 unit), it must also contain at least 1 unit of type C. (C alone does not require A.)

**Global constraints:**
- Total units of each type across all containers ≤ available quantity (and since all must be shipped, = available quantity).
- Number of containers is unlimited; we minimize how many are opened.

**Variables:** For each container i and type t, integer units x[i,t] ≥ 0; binary y[i] indicating container i is used. Coupling: x[i,t] ≤ M·y[i] for all t; weight = Σ_t w_t·x[i,t] with 18·y[i] ≤ weight ≤ 60·y[i]; D: x[i,D] ≥ 12·y[i]; A→C: x[i,A] ≤ M·z[i] and x[i,C] ≥ z[i] (or equivalent big-M formulation).

**Note on feasibility:** Total goods weight = 120(0.5)+90(1)+300(0.4)+90(0.6)+120(0.65) = 60+90+120+54+78 = 402 tons. With 60-ton max per container, at least 7 containers are needed by weight. With 12 D-units (7.2 tons) per container and only 90 D units total, at most 7 containers can each take 12 D (90/12 = 7.5, so 7 containers). This is a tight coupling that the model will resolve.