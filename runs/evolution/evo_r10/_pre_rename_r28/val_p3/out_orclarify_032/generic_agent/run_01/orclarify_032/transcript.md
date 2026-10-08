## Turn 1 - Generic Agent

QUESTION: What is the objective of this production plan — for example, maximize the number of complete products (each requiring one unit of each of the three components) that can be assembled, or maximize total profit given some per-component or per-product revenue?

## Turn 1 - User Simulator

The objective is to maximize the number of complete products that can be assembled. Each complete product requires one unit of each of the three components.

## Turn 2 - Generic Agent

QUESTION: Are there any demand limits or minimum production requirements for the components, or is the only constraint the workshop capacity (i.e., we can produce as many components as the workshops allow, up to what's needed for complete products)?

## Turn 2 - User Simulator

The only constraint is the workshop capacity. There are no demand limits or minimum production requirements.

## Turn 3 - Generic Agent

QUESTION: Can a single component be produced by multiple workshops simultaneously (e.g., Component 1 produced partly by Workshop A and partly by Workshop B), or is each component assigned to exactly one workshop?

## Turn 3 - User Simulator

A single component can be produced by multiple workshops simultaneously.

## Turn 4 - Generic Agent

QUESTION: Are the production rates constant (i.e., linear — producing 20 units of Component 1 at Workshop A always takes exactly 2 hours regardless of how many other components are also being produced there), or is there any setup time, batch requirement, or nonlinearity I should account for?

## Turn 4 - User Simulator

The production rates are constant. There is no setup time, batch requirement, or nonlinearity.

## Turn 5 - Generic Agent

QUESTION: Do the component production quantities need to be whole numbers (integer units), or can they be fractional (e.g., producing 12.5 units of Component 2)?

## Turn 5 - User Simulator

The component production quantities need to be whole numbers.

## Turn 6 - Generic Agent

QUESTION: If a workshop has leftover capacity after producing the components needed for the complete products, is that simply unused (no penalty, no requirement to fill it), or is there any cost or constraint on leaving capacity idle?

## Turn 6 - User Simulator

Leftover capacity is simply unused. There is no penalty or requirement to fill it.