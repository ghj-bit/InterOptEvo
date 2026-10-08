# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U6, U7, U9, U2, U3
I need help creating a warehouse space rental plan for the next 4 months. Each contract must cover consecutive months starting from the beginning of the period, and if a 4-month contract is chosen, then no 1-month contract may be chosen (mutual exclusion). The company may rent multiple warehouses in parallel, and the available capacity of each warehouse is unlimited (i.e., any contract can cover the full required area or part of it).

Table 1-14:
| Month | 1    | 2    | 3    | 4    |
|-------|------|------|------|------|
| Required area | 1500 | 1000 | 2000 | 1200 |

Table 1-15:
| Contract length (months) | 1  | 2  | 3  | 4  |
|--------------------------|----|----|----|----|
| Rental fee per 100㎡ (yuan) | 4000 | 7500 | 10500 | 13000 |

## Problem units
- U1 (context): I need help creating a warehouse space rental plan for the next 4 months.
- U2 (data): Table 1-14:
| Month | 1    | 2    | 3    | 4    |
|-------|------|------|------|------|
| Required area | 1500 | 1000 | 2000 | 1200 |
- U3 (data): Table 1-15:
| Contract length (months) | 1  | 2  | 3  | 4  |
|--------------------------|----|----|----|----|
| Rental fee per 100㎡ (yuan) | 4000 | 7500 | 10500 | 13000 |
- U4 (constraint): Each contract must cover consecutive months starting from the beginning of the period.
- U5 (constraint): Each warehouse contract must fully cover the selected months.
- U6 (assumption): The company may rent multiple warehouses in parallel.
- U7 (assumption): The available capacity of each warehouse is unlimited (i.e., any contract can cover the full required area or part of it).
- U8 (constraint): At least two different contracts (with different lengths) must be signed over the 4 months.
- U9 (constraint): If a 4-month contract is chosen, then no 1-month contract may be chosen (mutual exclusion).
- U10 (constraint): The number of distinct warehouse contracts signed cannot exceed 3.
- U11 (constraint): The demand for each month must be fully satisfied without shortage or excess.
- U12 (objective): Minimize the total rental cost over the 4 months.

## Hidden slot scoring rules
## H1: contract_full_coverage
- Severity: P2
- Severity reason: Without this rule, the remaining constraints (consecutive months and exact demand satisfaction) already implicitly force that a contract must be used for its entire term if it is signed, so the missing statement primarily adds clarity but does not fundamentally alter the feasible solution space. The optimization problem remains coherent and solvable.
- Problem unit ID: U5
- Semantic hit rule: The agent’s question must explicitly ask whether a contract, once signed for a certain length, must be kept (or remain active) for all months in that period, or whether partial usage is allowed.
- Reference acceptable questions:
  - If I sign a 2‑month contract, am I obligated to keep that warehouse for both months, or can I use it for only one of them?
  - Does a signed contract force me to use the space for every month in its coverage period?
- Failure modes:
  - Assuming a 2‑month contract can be used to cover only month 1 while month 2 is covered by a different contract, without any penalty.
  - Modeling contracts without linking rental commitment to the entire term, which could lead to solutions that do not respect the mandatory full‑period obligation.

## H2: contract_length_diversity
- Severity: P1
- Severity reason: Without this risk‑management rule, the model remains a valid cost‑minimization problem, but the resulting solution is likely to ignore a deliberate business requirement and may be materially different from the intended plan. The agent can still formulate a coherent MILP, so it is not a fatal gap, but it should be clarified to avoid a business‑irrelevant answer.
- Problem unit ID: U8
- Semantic hit rule: The agent must ask whether the rental plan is forced to include contracts of at least two distinct lengths, or whether a single contract type is acceptable.
- Reference acceptable questions:
  - Is there any requirement to diversify the contract lengths, or can I use only one type of contract for the whole period?
  - Do I have to sign contracts with at least two different durations, or is it okay to use just 2‑month contracts all the way?
- Failure modes:
  - Assuming any combination of contracts is allowed, including using only 2‑month contracts throughout the horizon.
  - Ignoring the diversification constraint entirely, which could produce a solution that violates the risk‑management policy.

## H3: max_distinct_contracts
- Severity: P2
- Severity reason: This operational simplification rule limits the number of distinct contract types. The problem remains a well‑defined optimization even without it; removing the limit simply yields a potentially larger set of feasible solutions. The core modeling structure is unaffected, so it is a low‑impact detail.
- Problem unit ID: U10
- Semantic hit rule: The agent must inquire about a limit on the count of distinct contract lengths (or types) that can be used.
- Reference acceptable questions:
  - Is there a maximum on how many different types of contracts I can sign?
  - Can I sign more than three distinct warehouse contracts, or is there a limit?
- Failure modes:
  - Assuming there is no cap on the number of different contracts, possibly leading to solutions with four or more distinct contract lengths.
  - Modeling without a variable‑count constraint, missing the operational preference for simplicity.

## H4: demand_exact_satisfaction
- Severity: P0
- Severity reason: Without the requirement that demand must be met exactly each month (no shortage, no excess), the model has no constraint that connects rented space to the given required areas. The cost objective would drive rented quantities to zero, making the problem ill‑posed and impossible to formulate meaningfully.
- Problem unit ID: U11
- Semantic hit rule: The agent must ask whether the monthly rental amounts must exactly match the given required areas, or whether oversupply/undersupply is allowed.
- Reference acceptable questions:
  - Do I have to cover exactly the required area each month, or can I rent extra space or fall short?
  - Is it mandatory to meet the monthly demands precisely, with no surplus and no deficit?
- Failure modes:
  - Omitting the balance constraints entirely, leading to a trivial solution of renting nothing.
  - Assuming excess capacity is permitted at no cost, which would produce a different feasible set than intended.

## H5: objective_minimize_cost
- Severity: P0
- Severity reason: The objective is the core driver of the optimization; without knowing that the goal is to minimize total rental cost, the agent cannot define a meaningful objective function. The problem would be ill‑posed because no performance criterion is given.
- Problem unit ID: U12
- Semantic hit rule: The agent must explicitly ask for the optimization goal or confirm that the objective is to minimize total rental cost.
- Reference acceptable questions:
  - What is the main goal – are we trying to minimize total rental expenditure, or something else?
  - Is the objective simply to spend as little as possible on rent over the whole period?
- Failure modes:
  - Formulating a model without an objective function, or assuming a different objective such as minimizing the number of contracts.
  - Treating the problem as a feasibility exercise rather than a cost‑driven optimization.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: For a k-month contract, does the rental fee in Table 1-15 represent the total cost for the entire k-month period, or is it the cost per month that must be multiplied by k?

## Turn 1 - User Simulator

The rental fee in Table 1-15 is the total cost for the entire k-month period. It is not a per-month rate.

## Turn 2 - Generic Agent

QUESTION: The brief says "each contract must cover consecutive months starting from the beginning of the period" — does this mean every contract must start in month 1 (so the only possible contracts are 1-month, 2-month, 3-month, or 4-month, all beginning at month 1), or can a contract start in any month as long as it covers consecutive months (e.g., a 2-month contract covering months 2–3)?

## Turn 2 - User Simulator

Every contract must start in month 1. The only possible contracts are 1-month, 2-month, 3-month, or 4-month, all beginning at month 1.

## Turn 3 - Generic Agent

QUESTION: The brief says "the company may rent multiple warehouses in parallel" — does this mean the company can rent multiple separate warehouses (each with its own contract), or does it mean the company can hold multiple contracts (of different lengths) simultaneously for the same warehouse?

## Turn 3 - User Simulator

The company can rent multiple separate warehouses, each with its own contract.

## Turn 4 - Generic Agent

QUESTION: The brief says "if a 4-month contract is chosen, then no 1-month contract may be chosen (mutual exclusion)" — does this mutual exclusion apply globally (i.e., if ANY 4-month contract is chosen, then NO 1-month contract of any length can be chosen across ALL warehouses), or does it apply per warehouse (i.e., within a single warehouse, you can't have both a 4-month and a 1-month contract, but different warehouses can have different contract types)?

## Turn 4 - User Simulator

The mutual exclusion applies globally. If any 4-month contract is chosen, no 1-month contract can be chosen across all warehouses.

## Turn 5 - Generic Agent

QUESTION: Since each warehouse's capacity is unlimited and contracts can cover any area, is the decision simply how many warehouses to rent at each contract length (1, 2, 3, or 4 months), with each warehouse providing a fixed unit of area, or is the decision how much total area to rent at each contract length, where the area can be any continuous quantity?

## Turn 5 - User Simulator

The decision is how much total area to rent at each contract length, where the area can be any continuous quantity.

## Turn 6 - Generic Agent

QUESTION: Since each contract must start in month 1 and can be 1, 2, 3, or 4 months long, a 2-month contract covers months 1–2, a 3-month contract covers months 1–3, and a 4-month contract covers months 1–4. Does this mean that for each month, the total rented area from all active contracts must be at least the required area for that month, or must it exactly equal the required area?

## Turn 6 - User Simulator

It must exactly equal the required area for that month. No shortages and no excess space are allowed.

## Turn 7 - Generic Agent

QUESTION: The rental fee in Table 1-15 is given per 100㎡. If the company rents, say, 1500㎡ under a 1-month contract, is the cost calculated as (1500/100) × 4000 = 60,000 yuan, i.e., the fee scales linearly with the area rented?

## Turn 7 - User Simulator

Yes, the cost scales linearly with the area rented. For 1500㎡ under a 1-month contract, the cost is (1500/100) × 4000 = 60,000 yuan.

## Turn 8 - Generic Agent

QUESTION: The mutual exclusion rule says "if a 4-month contract is chosen, then no 1-month contract may be chosen." Does this mean that if the company rents any positive area under a 4-month contract, it cannot rent any area under a 1-month contract, or does it mean that if the company chooses to use a 4-month contract at all (even for a tiny amount), it must not use any 1-month contracts?

## Turn 8 - User Simulator

It means that if the company rents any positive area under a 4-month contract, it cannot rent any area under a 1-month contract.

## Turn 9 - Generic Agent

QUESTION: The objective is to minimize total rental cost over the 4 months, correct?

## Turn 9 - User Simulator

Yes, the objective is to minimize the total rental cost over the 4 months.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Time horizon:** 4 months.
- **Required area per month:** Month 1 = 1500㎡, Month 2 = 1000㎡, Month 3 = 2000㎡, Month 4 = 1200㎡.
- **Contract types:** 1-month (covers month 1), 2-month (covers months 1–2), 3-month (covers months 1–3), 4-month (covers months 1–4). All contracts start in month 1.
- **Decision variables:** Continuous area rented under each contract length (1, 2, 3, or 4 months).
- **Cost:** Linear in area. Total cost for a k-month contract of area A is (A/100) × fee_k, where fees are: 1-month = 4000, 2-month = 7500, 3-month = 10500, 4-month = 13000 (yuan per 100㎡ for the entire contract period).
- **Capacity constraints:** For each month, the sum of areas from all contracts active in that month must **exactly equal** the required area for that month.
- **Mutual exclusion (global):** If any positive area is rented under a 4-month contract, then no area may be rented under a 1-month contract.
- **Objective:** Minimize total rental cost over the 4 months.