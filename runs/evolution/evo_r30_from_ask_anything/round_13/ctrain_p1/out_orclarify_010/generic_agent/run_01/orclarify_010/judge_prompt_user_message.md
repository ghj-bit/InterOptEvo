# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U2
I need help planning the opening of several chain stores in a new residential area while minimizing the number of chain stores built.

| Area Code | Residential Areas within 800 m Radius |
|-----------|---------------------------------------|
| A         | A, C, E, G, H, I                      |
| B         | B, H, I                               |
| C         | A, C, G, H, I                         |
| D         | D, J                                  |
| E         | A, E, G                               |
| F         | F, J, K                               |
| G         | A, C, E, G                            |
| H         | A, B, C, H, I                         |
| I         | A, B, C, H, I                         |
| J         | D, F, J, K, L                         |
| K         | F, J, K, L                            |
| L         | J, K, L                               |

## Problem units
- U1 (context): I need help planning the opening of several chain stores in a new residential area.
- U2 (data): | Area Code | Residential Areas within 800 m Radius |
|-----------|---------------------------------------|
| A         | A, C, E, G, H, I                      |
| B         | B, H, I                               |
| C         | A, C, G, H, I                         |
| D         | D, J                                  |
| E         | A, E, G                               |
| F         | F, J, K                               |
| G         | A, C, E, G                            |
| H         | A, B, C, H, I                         |
| I         | A, B, C, H, I                         |
| J         | D, F, J, K, L                         |
| K         | F, J, K, L                            |
| L         | J, K, L                               |
- U3 (objective): Minimize the number of chain stores built.
- U4 (constraint): The distance from any residential area to at least one chain store must not exceed 800 meters.

## Hidden slot scoring rules
## H1: max_distance_800m
- Severity: P0
- Severity reason: Without this constraint, the problem reduces to minimizing an unbounded number of stores with no service coverage requirement, making the model ill-posed and the provided distance table irrelevant.
- Problem unit ID: U4
- Semantic hit rule: The Agent's question must explicitly ask about the coverage radius or maximum allowed distance for a residential area to be considered served by a chain store.
- Reference acceptable questions:
  - What is the maximum allowed distance between a residential area and the nearest chain store?
  - Do we need to ensure every residential area is within 800 meters of at least one store?
- Failure modes:
  - Assuming all residential areas are served regardless of distance
  - Assuming the data table is just for reference and not a hard constraint


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the goal to minimize the number of stores built subject to the hard requirement that every residential area (A through L) is within 800 m of at least one built store, or is there a separate service-level target (e.g., a minimum number of stores within range of each area) that also applies?

## Turn 1 - User Simulator

The goal is to minimize the number of stores built, subject to the hard requirement that every residential area (A through L) is within 800 m of at least one built store. There is no separate service-level target or minimum number of stores required within range of each area.

## Turn 2 - Generic Agent

QUESTION: Are there any other constraints on which areas can host a store, such as a maximum total number of stores, a minimum number of stores, or restrictions that certain areas cannot be selected?

## Turn 2 - User Simulator

There are no other constraints on which areas can host a store. Any of the areas A through L can be selected to host a store, and there are no maximum or minimum total number of stores, nor are there any areas that are restricted from being selected.

## Turn 3 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Objective:** Minimize the total number of chain stores built. (Confirmed)
- **Decision variables:** A binary variable for each of the 12 candidate areas (A through L), indicating whether a store is built in that area. (Confirmed)
- **Variable domain:** Binary (0 or 1) for each area. (Confirmed)
- **Constraints:** For each residential area (A through L), the sum of stores built in areas that are within 800 m of that residential area must be at least 1. This is a hard coverage requirement. (Confirmed)
- **Coverage data:** The table provided specifies which residential areas are within 800 m of each candidate store location. (Confirmed)
- **No other constraints:** No maximum or minimum number of stores, no restricted areas, no service-level targets beyond the at-least-one coverage requirement. (Confirmed)

**Open assumptions:** None. All formulation-critical facts are confirmed.

This is a classic **set covering problem**: choose the minimum number of candidate locations such that every residential area is covered by at least one selected location.