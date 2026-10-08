## Turn 1 - Generic Agent

QUESTION: How is the probability of destroying a key part computed from the bombs assigned to it — is it 1 minus (1 minus the per-bomb probability) raised to the number of bombs of that type assigned, with heavy and light bombs combined multiplicatively (i.e., independent per-bomb destruction attempts)?

## Turn 1 - User Simulator

Yes, that is correct. The probability of destroying a key part is computed by treating each bomb's attempt as independent. For a given key part, you take the per-bomb destruction probability for each heavy bomb assigned and each light bomb assigned, and combine them multiplicatively. Specifically, the probability that the part is destroyed is 1 minus the product of (1 minus the per-bomb probability) for every bomb assigned to that part, regardless of whether the bomb is heavy or light.

## Turn 2 - Generic Agent

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits?

## Turn 2 - User Simulator

Yes, the mission objective is to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits.

## Turn 3 - Generic Agent

QUESTION: How does the aircraft deliver bombs to the targets — does it carry all bombs for a single key part on one round trip, or can it make multiple trips to the same part, and can it carry both heavy and light bombs on the same trip?

## Turn 3 - User Simulator

The aircraft can make multiple trips to the same key part. However, it can carry only one bomb per trip, so it cannot carry both heavy and light bombs on the same trip.

## Turn 4 - Generic Agent

QUESTION: When the aircraft carries a bomb on a trip, is the fuel efficiency for the entire round trip determined by the bomb being carried (2 km/L for heavy, 3 km/L for light), or does the return leg use the empty-aircraft efficiency of 4 km/L?

## Turn 4 - User Simulator

The fuel efficiency for the entire round trip is determined by the bomb being carried. If carrying a heavy bomb, the efficiency is 2 km/L for the whole round trip. If carrying a light bomb, the efficiency is 3 km/L for the whole round trip.

## Turn 5 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel cost incurred once per round trip (i.e., once per bomb delivered), in addition to the fuel for the distance flown?

## Turn 5 - User Simulator

Yes, the 100-liter takeoff-and-landing fuel cost is incurred once per round trip, in addition to the fuel for the distance flown.

## Turn 6 - Generic Agent

QUESTION: Are the 28 heavy and 12 light bombs hard upper bounds on how many can be used (i.e., you may use fewer), or must all available bombs be used?

## Turn 6 - User Simulator

The 28 heavy and 12 light bombs are hard upper bounds. You may use fewer than the available amounts.

## Turn 7 - Generic Agent

QUESTION: Can a key part be assigned zero bombs (left untouched), and is it acceptable for the optimal plan to leave some parts with no bombs at all?

## Turn 7 - User Simulator

Yes, a key part can be assigned zero bombs. It is acceptable for the optimal plan to leave some parts with no bombs at all.

## Turn 8 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a total across all trips combined (i.e., the sum of fuel for every round trip plus every takeoff/landing cost must be at most 10,000), rather than a per-trip limit?

## Turn 8 - User Simulator

Yes, the 10,000-liter fuel limit is a total across all trips combined. The sum of fuel for every round trip plus every takeoff/landing cost must be at most 10,000 liters.

## Turn 9 - Generic Agent

QUESTION: For the fuel calculation, is the round-trip distance simply twice the one-way distance to the key part (e.g., 2 × 450 km for part 1), with no additional distance components?

## Turn 9 - User Simulator

Yes, the round-trip distance is simply twice the one-way distance to the key part, with no additional distance components.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on the number of trips the aircraft can make, other than the bomb and fuel constraints?

## Turn 10 - User Simulator

No, there is no limit on the number of trips the aircraft can make, other than the bomb and fuel constraints.

## Turn 11 - Generic Agent

QUESTION: When computing the probability that at least two of the four key parts are destroyed, are the destruction events of the different key parts treated as independent of each other?

## Turn 11 - User Simulator

Yes, the destruction events of the different key parts are treated as independent of each other.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.

**Decision variables:** For each key part i (1–4), the number of heavy bombs h_i and light bombs l_i assigned to it (non-negative integers).

**Destruction probability per part:** For part i, p_i = 1 − (1 − p_hi)^{h_i} × (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs respectively. Parts with zero bombs have p_i = 0.

**Success probability:** The four parts' destruction events are independent, so P(at least 2 destroyed) = 1 − P(0 destroyed) − P(exactly 1 destroyed), computed from the p_i values.

**Constraints:**
- Σ h_i ≤ 28 (heavy bomb limit)
- Σ l_i ≤ 12 (light bomb limit)
- Total fuel ≤ 10,000 liters

**Fuel model:** Each bomb delivered requires one round trip. The aircraft carries exactly one bomb per trip. Fuel for a trip to part i:
- Heavy bomb: (2 × d_i) / 2 + 100 liters (where d_i is one-way distance)
- Light bomb: (2 × d_i) / 3 + 100 liters

Total fuel = Σ over all heavy bombs to part i of (d_i + 100) + Σ over all light bombs to part i of (2d_i/3 + 100).

**Distances:** d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600 km.

**Per-bomb probabilities:**
| Part | Heavy | Light |
|------|-------|-------|
| 1    | 0.03  | 0.08  |
| 2    | 0.10  | 0.11  |
| 3    | 0.05  | 0.12  |
| 4    | 0.05  | 0.09  |

**Other notes:** Parts may receive zero bombs. No limit on number of trips beyond bomb/fuel constraints. Bomb limits are upper bounds (may use fewer).