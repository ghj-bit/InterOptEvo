# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U8, U9, U10, U2, U3, U4
I need help planning timber purchasing, sales, and storage across quarters, aiming to maximize annual profit while ensuring that the storage amount at any time does not exceed the maximum warehouse capacity of 200,000 m³, and that seasonal sales respect their estimated maximum volumes: 100 (10,000 m³) in winter, 140 in spring, 200 in summer, and 160 in autumn.

Storage cost parameters: a = 70, b = 100. The storage cost is (a + b*u) yuan/m³, where u is the storage time in quarters.

Maximum storage capacity: 200,000 m³.

Table 1-18: Purchasing and sales prices and maximum sales volumes per quarter.

| Quarter | Purchase Price (10,000 yuan/10,000 m²) | Sale Price (10,000 yuan/10,000 m²) | Estimated Maximum Sales Volume (10,000 m³) |
|---------|----------------------------------------|------------------------------------|---------------------------------------------|
| Winter  | 410                                    | 425                                | 100                                         |
| Spring  | 430                                    | 440                                | 140                                         |
| Summer  | 460                                    | 465                                | 200                                         |
| Autumn  | 450                                    | 455                                | 160                                         |

## Problem units
- U1 (context): I need help planning timber purchasing, sales, and storage across quarters.
- U2 (data): Storage cost parameters: a = 70, b = 100. The storage cost is (a + b*u) yuan/m³, where u is the storage time in quarters.
- U3 (data): Maximum storage capacity: 200,000 m³.
- U4 (data): Table 1-18: Purchasing and sales prices and maximum sales volumes per quarter.

| Quarter | Purchase Price (10,000 yuan/10,000 m²) | Sale Price (10,000 yuan/10,000 m²) | Estimated Maximum Sales Volume (10,000 m³) |
|---------|----------------------------------------|------------------------------------|---------------------------------------------|
| Winter  | 410                                    | 425                                | 100                                         |
| Spring  | 430                                    | 440                                | 140                                         |
| Summer  | 460                                    | 465                                | 200                                         |
| Autumn  | 450                                    | 455                                | 160                                         |
- U5 (objective): Maximize annual profit.
- U6 (constraint): The storage amount at any time must not exceed the maximum warehouse capacity of 200,000 m³.
- U7 (constraint): Winter sales cannot exceed the estimated maximum sales volume of 100 (10,000 m³).
- U8 (constraint): Spring sales cannot exceed the estimated maximum sales volume of 140 (10,000 m³).
- U9 (constraint): Summer sales cannot exceed the estimated maximum sales volume of 200 (10,000 m³).
- U10 (constraint): Autumn sales cannot exceed the estimated maximum sales volume of 160 (10,000 m³).
- U11 (constraint): All inventory must be sold by the end of autumn (i.e., ending inventory after autumn sales is zero).

## Hidden slot scoring rules
## H1: zero_ending_inventory
- Severity: P1
- Severity reason: Without this constraint, the model might allow ending inventory beyond autumn, violating the business rule that timber cannot be stored long‑term and leading to an inaccurate profit calculation.
- Problem unit ID: U11
- Semantic hit rule: The Agent's question must explicitly ask about the requirement that ending inventory must be zero, or about the need to sell all timber by the end of the horizon.
- Reference acceptable questions:
  - Is it mandatory that all timber be sold by the end of autumn?
  - What happens to any inventory that is left unsold after the autumn quarter?
- Failure modes:
  - Assuming inventory can be held indefinitely without any terminal selling obligation.
  - Ignoring the liquidation requirement and allowing positive ending inventory in the model.


# Atomic Question Map

Q1 (turn 1): Can timber purchased in a quarter be sold in that same quarter, or must it be held in storage for at least one full quarter before it can be sold?
Q2 (turn 2): If timber is purchased and sold in the same quarter, is its storage time u equal to 0, 0.5, or 1 quarter for storage cost purposes?
Q3 (turn 3): Until the same-quarter storage-time convention is confirmed internally, should we model same-quarter purchases and sales as incurring zero storage cost, or should we exclude same-quarter resale from the model entirely?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Can timber purchased in a quarter be sold in that same quarter, or must it be held in storage for at least one full quarter before it can be sold?

## Turn 1 - User Simulator

Timber purchased in a quarter can be sold in that same quarter. It does not have to be held in storage for a full quarter first.

## Turn 2 - Generic Agent

QUESTION: If timber is purchased and sold in the same quarter, is its storage time u equal to 0, 0.5, or 1 quarter for storage cost purposes?

## Turn 2 - User Simulator

That point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Until the same-quarter storage-time convention is confirmed internally, should we model same-quarter purchases and sales as incurring zero storage cost, or should we exclude same-quarter resale from the model entirely?

## Turn 3 - User Simulator

That point still needs internal confirmation.