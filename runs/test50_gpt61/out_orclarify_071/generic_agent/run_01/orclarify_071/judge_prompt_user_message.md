# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U2, U3, U4
I need help creating a factory-to-location assignment plan where each factory must be assigned to exactly one location.

Number of factories: 2, number of locations: 2.

Transportation volume between factory i and factory j is denoted d_{ij}. Unit transportation cost from location p to location q is denoted c_{pq}.

|        | Transportation volume to Location 1 | Transportation volume to Location 2 | Transportation cost to Location 1 | Transportation cost to Location 2 |
| :----: | :---------------------------------: | :---------------------------------: | :-------------------------------: | :-------------------------------: |
| Factory 1 | 10 | 20 | 5 | 8 |
| Factory 2 | 30 | 40 | 6 | 7 |

## Problem units
- U1 (context): I need help creating a factory-to-location assignment plan.
- U2 (data): Number of factories: 2, number of locations: 2.
- U3 (data): Transportation volume between factory i and factory j is denoted d_{ij}. Unit transportation cost from location p to location q is denoted c_{pq}.
- U4 (data): |        | Transportation volume to Location 1 | Transportation volume to Location 2 | Transportation cost to Location 1 | Transportation cost to Location 2 |
| :----: | :---------------------------------: | :---------------------------------: | :-------------------------------: | :-------------------------------: |
| Factory 1 | 10 | 20 | 5 | 8 |
| Factory 2 | 30 | 40 | 6 | 7 |
- U5 (objective): Minimize the total transportation cost.
- U6 (constraint): Each factory must be assigned to exactly one location.
- U7 (constraint): Each location must be assigned exactly one factory.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without the objective, the agent cannot define a meaningful optimization model; the problem is incomplete and impossible to formulate.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must explicitly ask about the optimization objective or the specific cost to be minimized.
- Reference acceptable questions:
  - What is our goal here? Are we minimizing total transportation cost?
  - What cost should we minimize?
- Failure modes:
  - Agent assumes a different objective, such as minimizing maximum distance or maximizing throughput, without clarification.
  - Agent tries to formulate a feasibility problem with no objective function.

## H2: bijection_constraint_locations
- Severity: P1
- Severity reason: Without this explicit constraint, the model may assign multiple factories to the same location, violating the intended one-to-one matching and producing an invalid assignment.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must explicitly ask whether each location must have exactly one assigned factory, or whether the assignment is a bijection.
- Reference acceptable questions:
  - Do we need to ensure each location gets exactly one factory?
  - Is it a one-to-one assignment where each location receives a factory?
- Failure modes:
  - Agent assumes locations can be left empty or that multiple factories can be placed at the same location.
  - Agent formulates only the constraint that each factory goes to one location, ignoring the location coverage requirement.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Should the volume values be interpreted as flows between factories and the cost values as costs between locations, or does each row instead give each factory’s volume and cost for shipping directly to each location?

## Turn 1 - User Simulator

Each row gives that factory’s transportation volume and unit transportation cost for shipping directly to each location.

## Turn 2 - Generic Agent

QUESTION: Must each location receive exactly one factory, or may both factories be assigned to the same location?

## Turn 2 - User Simulator

Each location must be assigned exactly one factory.

## Turn 3 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- There are 2 factories and 2 locations.
- Each factory must be assigned to exactly one location.
- Each location must receive exactly one factory.
- The given volume and unit cost are specific to each factory-location pair.
- Total assignment cost is calculated as `transportation volume × unit transportation cost`.
- Assumption: the goal is to minimize total transportation cost.

| Assignment | Factory 1 | Factory 2 | Total cost |
|---|---:|---:|---:|
| Factory 1 → Location 1; Factory 2 → Location 2 | `10 × 5 = 50` | `40 × 7 = 280` | **330** |
| Factory 1 → Location 2; Factory 2 → Location 1 | `20 × 8 = 160` | `30 × 6 = 180` | **340** |

**Recommended assignment**

- Factory 1 → Location 1
- Factory 2 → Location 2
- Minimum total transportation cost: **330**

Using binary decision variables `xᵢₚ`, where `xᵢₚ = 1` if factory `i` is assigned to location `p`:

\[
\min \; 50x_{11} + 160x_{12} + 180x_{21} + 280x_{22}
\]

Subject to:

\[
x_{11}+x_{12}=1
\]

\[
x_{21}+x_{22}=1
\]

\[
x_{11}+x_{21}=1
\]

\[
x_{12}+x_{22}=1
\]

\[
x_{ip}\in\{0,1\}
\]