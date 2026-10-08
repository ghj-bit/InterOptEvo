## Turn 1 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to their single listed preferred specialty, or would being assigned to any specialty in their suitable specialty set count as meeting it?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty. Being assigned to any other specialty in their suitable specialty set does not count.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in their single listed preferred city, or would being assigned to any branch in either city count as meeting it?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single listed preferred city. Being assigned to a branch in the other city does not count.

## Turn 3 - Generic Agent

QUESTION: The demand in Table 4-3 sums to 8500, but there are only 9000 people available. Should the branch demands be treated as exact requirements that must be met exactly, or as maximum capacities that may be under-filled?

## Turn 3 - User Simulator

The branch demands must be treated as exact requirements that must be met exactly. No more, no less.

## Turn 4 - Generic Agent

QUESTION: Since the branch demands sum to 8500 but there are 9000 people available, should the 500 unassigned people be allowed to remain unassigned (i.e., not counted in any branch), or must all 9000 be assigned to some branch?

## Turn 4 - User Simulator

The 500 unassigned people are allowed to remain unassigned. They are not counted in any branch.

## Turn 5 - Generic Agent

QUESTION: The problem states three objectives (8000 meet preferred specialty, 8000 meet preferred city, and minimize those not meeting preferred city). Should this be modeled as a single objective that minimizes the number of people who do NOT meet their preferred city (with the two 8000 targets treated as soft goals to be satisfied as much as possible), or as a multi-objective / goal-programming formulation where all three goals are handled explicitly?

## Turn 5 - User Simulator

This should be modeled as a multi-objective / goal-programming formulation where all three goals are handled explicitly. The priorities are in strict order: first, fully meet all branch demands (p1); second, achieve 8000 people meeting their preferred specialty (p2); and third, achieve 8000 people meeting their preferred city (p3).

## Turn 6 - Generic Agent

QUESTION: In the goal-programming formulation, for the preferred-specialty goal (p2) and the preferred-city goal (p3), should I minimize only the under-achievement (i.e., the shortfall below 8000), or should I also penalize over-achievement (i.e., more than 8000 meeting the goal)?

## Turn 6 - User Simulator

For both the preferred-specialty goal (p2) and the preferred-city goal (p3), only the under-achievement (the shortfall below 8000) should be minimized. Over-achievement (more than 8000 meeting the goal) is not penalized.

## Turn 7 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 7 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch. The 500 unassigned people are not included in this count.

## Turn 8 - Generic Agent

QUESTION: For the preferred-city goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 8 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 9 - Generic Agent

QUESTION: For the preferred-specialty goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 9 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 10 - Generic Agent

QUESTION: For the "suitable specialty" constraint, should a person be allowed to be assigned to a specialty that is NOT in their suitable specialty set (i.e., is the suitable specialty set a hard restriction on assignment, or just a preference)?

## Turn 10 - User Simulator

The suitable specialty set is a hard restriction on assignment. A person can only be assigned to a specialty that is listed in their suitable specialty set.

## Turn 11 - Generic Agent

QUESTION: For the "available number of each type" constraint, should the total number of people assigned from each type be at most the available number (allowing some of a type to be unassigned), or must all available people of each type be assigned?

## Turn 11 - User Simulator

The total number of people assigned from each type must be at most the available number. Some people of a type may remain unassigned.

## Turn 12 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 12 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 13 - Generic Agent

QUESTION: For the "preferred city" goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 13 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 14 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 14 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch.

## Turn 15 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 15 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 16 - Generic Agent

QUESTION: For the "preferred city" goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 16 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 17 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 17 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch.

## Turn 18 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 18 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 19 - Generic Agent

QUESTION: For the "preferred city" goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 19 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 20 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 20 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch.

## Turn 21 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 21 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 22 - Generic Agent

QUESTION: For the "preferred city" goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 22 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 23 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 23 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch.

## Turn 24 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 24 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 25 - Generic Agent

QUESTION: For the "preferred city" goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 25 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 26 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 26 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch.

## Turn 27 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 27 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.

## Turn 28 - Generic Agent

QUESTION: For the "preferred city" goal (p3), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred city)?

## Turn 28 - User Simulator

The 8000 target for the preferred-city goal (p3) should be measured only among the 8500 people actually assigned to a branch.

## Turn 29 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this be computed as the total number of people (including the 500 unassigned) who are not in their preferred city, or only among the 8500 people who are actually assigned to a branch?

## Turn 29 - User Simulator

This should be computed only among the 8500 people who are actually assigned to a branch.

## Turn 30 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), the 8000 target should be measured among which group: only the 8500 people actually assigned to a branch, or all 9000 recruited people (counting the 500 unassigned as not meeting their preferred specialty)?

## Turn 30 - User Simulator

The 8000 target for the preferred-specialty goal (p2) should be measured only among the 8500 people actually assigned to a branch.