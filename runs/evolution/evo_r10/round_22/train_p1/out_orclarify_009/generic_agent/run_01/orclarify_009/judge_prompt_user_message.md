# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U8, U9, U10, U11, U2, U3, U4, U5, U6
I need help planning the manufacture of toy trucks, toy airplanes, toy boats, and toy trains, where total wood consumption cannot exceed 890 units and total steel consumption cannot exceed 500 units. Additionally, if trucks are manufactured, then trains are not manufactured, and if boats are manufactured, then airplanes are also manufactured.

Profit per toy: truck $5, airplane $10, boat $8, train $7.

Available wood: 890 units.

Wood required per toy: truck 12 units, airplane 20 units, boat 15 units, train 10 units.

Available steel: 500 units.

Steel required per toy: truck 6 units, airplane 3 units, boat 5 units, train 4 units.

## Problem units
- U1 (context): I need help planning the manufacture of toy trucks, toy airplanes, toy boats, and toy trains.
- U2 (data): Profit per toy: truck $5, airplane $10, boat $8, train $7.
- U3 (data): Available wood: 890 units.
- U4 (data): Wood required per toy: truck 12 units, airplane 20 units, boat 15 units, train 10 units.
- U5 (data): Available steel: 500 units.
- U6 (data): Steel required per toy: truck 6 units, airplane 3 units, boat 5 units, train 4 units.
- U7 (objective): Maximize total profit.
- U8 (constraint): Total wood consumption cannot exceed 890 units.
- U9 (constraint): Total steel consumption cannot exceed 500 units.
- U10 (constraint): If trucks are manufactured, then trains are not manufactured.
- U11 (constraint): If boats are manufactured, then airplanes are also manufactured.
- U12 (constraint): Number of toy boats manufactured cannot exceed number of toy trains manufactured.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without an objective function, the optimization problem is undefined. A modeling agent cannot proceed to formulate a meaningful model unless the objective is clarified.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must explicitly ask about the objective of the optimization, specifically whether profit should be maximized.
- Reference acceptable questions:
  - What are we trying to maximize? Should we maximize total profit?
  - Is the goal to maximize profit, or something else like revenue or number of toys produced?
- Failure modes:
  - Silently assuming the objective is to maximize production volume or market share.
  - Assuming the goal is to minimize cost without asking.

## H2: boat_not_exceed_train
- Severity: P2
- Severity reason: The optimization model remains well-defined and solvable without this constraint. The missing rule is a specific business preference that would make the solution more accurate, but its omission does not make the model impossible or fundamentally ill-posed.
- Problem unit ID: U12
- Semantic hit rule: The agent must inquire about a constraint that limits the number of boats relative to the number of trains, specifically asking if boats must be less than or equal to trains.
- Reference acceptable questions:
  - Is there any rule linking the number of boats and trains, like boats can't exceed trains?
  - Do we have any production restriction tying the number of boats to the number of trains?
- Failure modes:
  - Silently assuming no relationship between boats and trains and building the model without this constraint.
  - Assuming that boats cannot exceed airplanes instead.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are the production quantities of the four toy types required to be whole numbers (you can only make an integer number of each toy), or is it acceptable to treat them as continuous values in the plan?

## Turn 1 - User Simulator

Yes, the production quantities must be whole numbers. You can only make an integer number of each toy.

## Turn 2 - Generic Agent

QUESTION: For the rule "if trucks are manufactured, then trains are not manufactured" — does this mean that producing even a single truck forces train production to be exactly zero, or is it only that you cannot produce both in positive amounts at the same time (i.e., trucks > 0 implies trains = 0, but trucks = 0 would allow trains)?

## Turn 2 - User Simulator

It means that producing even a single truck forces train production to be exactly zero. If trucks are manufactured (trucks > 0), then trains must be zero. If trucks are zero, trains can be produced.

## Turn 3 - Generic Agent

QUESTION: For the rule "if boats are manufactured, then airplanes are also manufactured" — does this mean that producing even a single boat forces airplane production to be at least one (boats > 0 implies airplanes >= 1), or does it only require airplanes to be positive in the same sense (boats > 0 implies airplanes > 0)?

## Turn 3 - User Simulator

It means that producing even a single boat forces airplane production to be at least one. If boats are manufactured (boats > 0), then airplanes must be at least 1.

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize total profit from the toys produced, subject to the wood and steel limits and the two rules?

## Turn 4 - User Simulator

Yes, the goal is to maximize total profit from the toys produced, subject to the wood and steel limits and the two rules.

## Turn 5 - Generic Agent

QUESTION: Are there any upper limits on how many of each toy type can be produced (for example, a maximum number of trucks, airplanes, boats, or trains), or is the only limit on each type the wood and steel availability?

## Turn 5 - User Simulator

There are no specific upper limits on how many of each toy type can be produced. The only limits on each type are the wood and steel availability.

## Turn 6 - Generic Agent

QUESTION: If no boats are manufactured, is it still allowed to produce airplanes on their own (i.e., airplanes > 0 with boats = 0), or does airplane production require boat production as well?

## Turn 6 - User Simulator

Yes, it is allowed to produce airplanes on their own. Airplane production does not require boat production.

## Turn 7 - Generic Agent

QUESTION: If no trucks are manufactured, is it still allowed to produce trains on their own (i.e., trains > 0 with trucks = 0), or does train production require truck production as well?

## Turn 7 - User Simulator

Yes, it is allowed to produce trains on their own. Train production does not require truck production.

## Turn 8 - Generic Agent

QUESTION: Are the wood and steel limits hard caps (total consumption must be at most 890 wood and at most 500 steel, with any leftover simply unused), or must the available wood and steel be used up exactly?

## Turn 8 - User Simulator

The wood and steel limits are hard caps. Total consumption must be at most 890 wood and at most 500 steel, with any leftover simply unused.

## Turn 9 - Generic Agent

QUESTION: Is there any minimum production requirement for any toy type (for example, you must produce at least one of some type), or is it acceptable to produce zero of any or all types?

## Turn 9 - User Simulator

There are no minimum production requirements. It is acceptable to produce zero of any or all types.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Four non-negative integer variables — number of trucks (T), airplanes (A), boats (B), and trains (R) to produce. No upper bounds other than the resource limits; zero production of any type is allowed.

- **Objective:** Maximize total profit = 5·T + 10·A + 8·B + 7·R.

- **Resource constraints (hard caps, leftover unused):**
  - Wood: 12·T + 20·A + 15·B + 10·R ≤ 890
  - Steel: 6·T + 3·A + 5·B + 4·R ≤ 500

- **Conditional rules:**
  - Trucks vs. trains: T > 0 ⇒ R = 0 (equivalently, T and R cannot both be positive; if trucks are produced, trains must be exactly zero; if trucks are zero, trains may be produced).
  - Boats ⇒ airplanes: B > 0 ⇒ A ≥ 1 (if boats are produced, at least one airplane must also be produced; airplanes may be produced without boats).

- **Integrality:** All four variables are integers.

- **No other constraints:** No minimums, no per-type caps, no other business rules.