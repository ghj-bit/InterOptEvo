# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U6, U2
I need help establishing a communication link in a network to maximize the bandwidth, where the bandwidth of a link is defined as the minimum bandwidth value among its constituent connections, and the link must not contain any loops (i.e., it must be a simple path).

Bandwidth communication table between nodes A, B, C, D, E:

|   | A  | B  | C  | D  | E  |
|---|----|----|----|----|----|
| A | 0  | 90 | 85 | 0  | 65 |
| B | 95 | 0  | 70 | 65 | 34 |
| C | 60 | 0  | 0  | 88 | 80 |
| D | 67 | 30 | 25 | 0  | 84 |
| E | 0  | 51 | 0  | 56 | 0  |

## Problem units
- U1 (context): I need help establishing a communication link in a network to maximize the bandwidth.
- U2 (data): Bandwidth communication table between nodes A, B, C, D, E:

|   | A  | B  | C  | D  | E  |
|---|----|----|----|----|----|
| A | 0  | 90 | 85 | 0  | 65 |
| B | 95 | 0  | 70 | 65 | 34 |
| C | 60 | 0  | 0  | 88 | 80 |
| D | 67 | 30 | 25 | 0  | 84 |
| E | 0  | 51 | 0  | 56 | 0  |
- U3 (objective): Maximize the bandwidth of the link, where the bandwidth of a link is defined as the minimum bandwidth value among its constituent connections.
- U4 (constraint): The link must connect node A to node E.
- U5 (constraint): The link must pass through service node C.
- U6 (constraint): The link must not contain any loops (i.e., it must be a simple path).

## Hidden slot scoring rules
## H1: missing_endpoints
- Severity: P0
- Severity reason: Without specifying which two nodes are to be connected, the objective 'maximize the bandwidth of a link' is undefined; any modeling attempt would be meaningless.
- Problem unit ID: U4
- Semantic hit rule: The agent must explicitly ask for the start and end nodes of the link, indicating that the endpoints are unclear.
- Reference acceptable questions:
  - Which two nodes should the link connect? The problem statement only mentions 'a link' but doesn't specify the end nodes.
  - From which source node to which destination node should the link be established?
- Failure modes:
  - Silently assuming the link is between any two nodes that yield the maximum possible min bandwidth (like a max bottleneck path problem without fixed endpoints)
  - Assuming all nodes are potential endpoints and selecting the pair with the highest bottleneck value
  - Interpreting the problem as a maximum spanning tree or a connectivity problem without specific endpoints

## H2: must_pass_through_node_C
- Severity: P1
- Severity reason: Missing this constraint still yields a coherent A-to-E simple path maximum bandwidth problem; but the intended business rule requires the link to go through service node C, which substantially alters the feasible set and optimal solution.
- Problem unit ID: U5
- Semantic hit rule: The agent must ask whether the link must pass through a specific intermediate node or any mandatory waypoint (especially service node C).
- Reference acceptable questions:
  - Is there any required intermediate node that the link must traverse?
  - Does the link have to go through any specific service node, like C?
- Failure modes:
  - Silently assuming the link can use any simple path from A to E without requiring a specific intermediate node
  - Assuming the problem is simply a maximum bottleneck path problem from A to E without any waypoint constraints


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Should the communication link be a simple path between two specific nodes (and if so, which two), or should I choose the pair of endpoints myself in order to maximize the path's bandwidth?

## Turn 1 - User Simulator

The link must connect node A to node E.

## Turn 2 - Generic Agent

QUESTION: The table gives different values in opposite directions (for example, A→B is 90 but B→A is 95), so should the path be treated as directed (the bandwidth of each hop depends on the direction you travel it), or should I treat each pair as a single undirected connection and use one value per pair?

## Turn 2 - User Simulator

The table values are directional. The bandwidth of each hop depends on the direction you travel it.

## Turn 3 - Generic Agent

QUESTION: Since the path's bandwidth is the minimum over its hops, should I maximize that minimum (i.e., find the path from A to E whose weakest hop is as strong as possible), or is there a different objective you have in mind?

## Turn 3 - User Simulator

Yes, maximize the minimum bandwidth value among the hops in the path from A to E.

## Turn 4 - Generic Agent

QUESTION: If multiple A-to-E paths achieve the same best minimum-hop bandwidth, do you need me to pick a single tie-breaking rule (for example, the path with the fewest hops, or the one with the largest total bandwidth), or is any optimal path acceptable?

## Turn 4 - User Simulator

Any optimal path is acceptable.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Problem:** Find a simple (loop-free) path from node A to node E in a 5-node network (A, B, C, D, E).
- **Objective:** Maximize the path's bandwidth, where the path's bandwidth is defined as the **minimum** bandwidth value among its constituent hops (the "widest path" / max-min problem).
- **Directionality:** The table is **directed** — the bandwidth of a hop depends on the direction of travel (e.g., A→B = 90 but B→A = 95).
- **Arcs:** Only entries with a positive value in the table exist as directed arcs; zero entries mean no direct connection in that direction.
- **Path constraint:** The path must be a simple path (no repeated nodes / no loops).
- **Tie-breaking:** None required — any path achieving the optimal minimum-hop bandwidth is acceptable.

I will formulate this as a max-min path problem (e.g., via a binary flow formulation with a variable representing the minimum hop bandwidth, or equivalently as a widest-path computation) and report the optimal A→E path and its bandwidth value.