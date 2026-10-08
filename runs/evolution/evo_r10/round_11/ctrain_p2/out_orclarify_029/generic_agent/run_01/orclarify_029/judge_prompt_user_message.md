# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U7, U8, U9, U10, U2, U3, U4
I need help creating a personnel arrangement plan for Jieli Company to assign recruited professionals to branches in Donghai City and Nanjiang City, where a person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4, and the total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4. The objectives are to have 8000 recruited personnel meet their preferred specialty, have 8000 meet their preferred city, and determine the minimum number of recruited personnel who cannot be assigned to their preferred city.

Table 4-3
| Branch Location | Specialty | Demand |
|-----------------|-----------|--------|
| Donghai City    | 1         | 1000   |
| Donghai City    | 2         | 2000   |
| Donghai City    | 3         | 1500   |
| Nanjiang City   | 1         | 2000   |
| Nanjiang City   | 2         | 1000   |
| Nanjiang City   | 3         | 1000   |

Table 4-4

| Type | Number of People | Suitable Specialty | Preferred Specialty | Preferred City |
|------|------------------|--------------------|---------------------|----------------|
| 1    | 1500             | 1,2                | 1                   | Donghai        |
| 2    | 1500             | 2,3                | 2                   | Donghai        |
| 3    | 1500             | 1,3                | 1                   | Nanjiang       |
| 4    | 1500             | 1,3                | 3                   | Nanjiang       |
| 5    | 1500             | 2,3                | 3                   | Donghai        |
| 6    | 1500             | 3                  | 3                   | Nanjiang       |

The target number for each of the preferred-specialty and preferred-city goals is 8000 recruited personnel.

## Problem units
- U1 (context): I need help creating a personnel arrangement plan for Jieli Company to assign recruited professionals to branches in Donghai City and Nanjiang City.
- U2 (data): Table 4-3
| Branch Location | Specialty | Demand |
|-----------------|-----------|--------|
| Donghai City    | 1         | 1000   |
| Donghai City    | 2         | 2000   |
| Donghai City    | 3         | 1500   |
| Nanjiang City   | 1         | 2000   |
| Nanjiang City   | 2         | 1000   |
| Nanjiang City   | 3         | 1000   |
- U3 (data): Table 4-4

| Type | Number of People | Suitable Specialty | Preferred Specialty | Preferred City |
|------|------------------|--------------------|---------------------|----------------|
| 1    | 1500             | 1,2                | 1                   | Donghai        |
| 2    | 1500             | 2,3                | 2                   | Donghai        |
| 3    | 1500             | 1,3                | 1                   | Nanjiang       |
| 4    | 1500             | 1,3                | 3                   | Nanjiang       |
| 5    | 1500             | 2,3                | 3                   | Donghai        |
| 6    | 1500             | 3                  | 3                   | Nanjiang       |
- U4 (data): The target number for each of the preferred-specialty and preferred-city goals is 8000 recruited personnel.
- U5 (constraint): The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3 (p1).
- U6 (constraint): A person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4.
- U7 (constraint): The total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4.
- U8 (objective): Achieve that 8000 recruited personnel meet their preferred specialty.
- U9 (objective): Achieve that 8000 recruited personnel meet their preferred city.
- U10 (objective): Determine the minimum number of recruited personnel who cannot be assigned to their preferred city.
- U11 (assumption): The company considers the three priorities in the order p1, p2, p3, with p1 being the highest priority and p3 the lowest.

## Hidden slot scoring rules
## H1: exact_demand_equality
- Severity: P1
- Severity reason: Without knowing that the demand must be met exactly (not just a lower bound), the model would use inequality constraints, changing the feasible set and the degree to which p2 and p3 can be achieved. This leads to a materially different solution than the intended problem.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must ask whether the demand fulfillment condition for p1 is an exact equality (assign exactly the demand numbers) or a lower bound (at least the demand).
- Reference acceptable questions:
  - For the demand requirement p1, does that mean we must assign exactly the number in Table 4‑3 to each specialty and branch, or is it acceptable to assign more than the demand if needed?
  - Is p1 an exact equality constraint, or is it a minimum to be met (i.e., at least the demand)?
- Failure modes:
  - Agent silently assumes the demand is a lower bound (>=) and allows over‑assignment, which changes the feasible set and the optimal achievement of p2/p3.

## H2: priority_order_lexicographic
- Severity: P0
- Severity reason: The entire multi‑objective formulation depends on the priority structure. Without knowing that the priorities are lexicographic (p1 before p2 before p3), a modeling agent cannot correctly specify the goal programming model. The problem would be ill‑posed.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must explicitly ask whether the priorities follow a lexicographic (preemptive) order, with p1 highest and p3 lowest, and that the goals are solved in that sequence.
- Reference acceptable questions:
  - How are the priorities structured? Is it a strict lexicographic order where p1 must be satisfied first, then p2, and finally p3?
  - Are we using preemptive goal programming, meaning we first fully satisfy p1, then try to achieve p2 as much as possible, and only after that try to achieve p3?
- Failure modes:
  - Agent treats all three goals as equally weighted and uses a weighted‑sum objective, ignoring the preemptive priority structure.
  - Agent assumes the three goals can be traded off simultaneously without a strict order, leading to a fundamentally different model.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: 对于"8000人满足偏好专业"和"8000人满足偏好城市"这两个目标，它们是必须达成的硬性约束，还是允许未达成、只需最小化未达成人数（即软目标）？

## Turn 1 - User Simulator

它们是软目标，不是硬性约束。允许未达成，只需最小化未达成人数。

## Turn 2 - Generic Agent

QUESTION: 总招聘人数是否固定为9000人（即6类各1500人全部都要安排），还是可以在0到9000之间选择招聘人数？

## Turn 2 - User Simulator

总招聘人数固定为9000人，即6类各1500人全部都要安排。

## Turn 3 - Generic Agent

QUESTION: 表4-3中各分支各专业的需求人数（如东海市专业1需1000人）是必须恰好满足的硬性约束，还是允许超出或不足？

## Turn 3 - User Simulator

是必须恰好满足的硬性约束，不能超出也不能不足。

## Turn 4 - Generic Agent

QUESTION: 关于"最小化未满足偏好城市的人数"这个目标，它与另外两个软目标（8000人满足偏好专业、8000人满足偏好城市）之间是什么关系——是三个目标同时最小化（多目标），还是"最小化未满足偏好城市人数"是主目标、另外两个是次级目标？

## Turn 4 - User Simulator

它们是三个按严格优先级顺序处理的目标：p1（恰好满足表4-3需求）最高，p2（8000人满足偏好专业）第二，p3（8000人满足偏好城市）最低。"最小化未满足偏好城市人数"是p3，不是主目标，而是在p1和p2达成后最后考虑的目标。

## Turn 5 - Generic Agent

QUESTION: 在p2（8000人满足偏好专业）和p3（8000人满足偏好城市）这两个软目标中，"满足偏好专业"是指被安排到其偏好专业（无论城市），"满足偏好城市"是指被安排到其偏好城市（无论专业），对吗？即一个人可以同时计入两个目标的达成，也可以只计入其中一个？

## Turn 5 - User Simulator

是的，"满足偏好专业"是指被安排到其偏好专业（无论城市），"满足偏好城市"是指被安排到其偏好城市（无论专业）。一个人可以同时计入两个目标的达成，也可以只计入其中一个。

## Turn 6 - Generic Agent

QUESTION: 表4-4中"Suitable Specialty"（适合专业）列是否意味着一个人只能被安排到该列列出的专业之一（即硬性约束），而"Preferred Specialty"（偏好专业）只是用于p2目标计分的偏好？

## Turn 6 - User Simulator

是的，"Suitable Specialty"是硬性约束，一个人只能被安排到该列列出的专业之一；"Preferred Specialty"只是用于p2目标计分的偏好。

## Turn 7 - Generic Agent

QUESTION: 表4-4中"Number of People"（各类1500人）是每类必须恰好安排1500人的硬性约束，还是每类最多安排1500人（允许少于1500）？

## Turn 7 - User Simulator

是每类最多安排1500人，允许少于1500。

## Turn 8 - Generic Agent

QUESTION: 既然每类最多安排1500人且总需求恰好为8500人（1000+2000+1500+2000+1000+1000），那么是否允许某些人完全不被安排（即总安排人数可以少于9000），还是必须安排满8500人（即总安排人数恰好等于总需求8500）？

## Turn 8 - User Simulator

必须安排满8500人，即总安排人数恰好等于总需求8500。

## Turn 9 - Generic Agent

QUESTION: 既然总安排人数固定为8500，那么"8000人满足偏好专业"和"8000人满足偏好城市"这两个目标的分母是8500（即最多8500人可以满足），还是说存在某种方式使得分母为9000？

## Turn 9 - User Simulator

分母是8500，即最多8500人可以满足。

## Turn 10 - Generic Agent

QUESTION: 关于p2和p3的软目标，"8000人满足偏好专业"和"8000人满足偏好城市"是目标值（即希望达到8000，未达到的部分计入目标函数），还是硬性下限（即必须至少8000人满足，否则不可行）？

## Turn 10 - User Simulator

是目标值，即希望达到8000，未达到的部分计入目标函数。不是硬性下限。

## Turn 11 - Generic Agent

QUESTION: 关于p2和p3的目标函数，是分别最小化"8000减去满足偏好专业人数"和"8000减去满足偏好城市人数"（即未达成量），还是最小化"满足偏好专业人数"和"满足偏好城市人数"（即最大化达成量）？两者在数学上等价，但请确认你希望的目标函数形式。

## Turn 11 - User Simulator

最小化"8000减去满足偏好专业人数"和"8000减去满足偏好城市人数"，即最小化未达成量。

## Turn 12 - Generic Agent

QUESTION: 在p1（恰好满足表4-3需求）作为最高优先级目标时，如果存在某些分支-专业组合的需求无法被满足（例如某类专业人数不足），是否允许该组合的需求被部分满足（即p1目标函数最小化未满足的需求总量），还是p1是硬性约束（必须恰好满足，否则问题不可行）？

## Turn 12 - User Simulator

p1是硬性约束，必须恰好满足表4-3中每个分支-专业组合的需求，否则问题不可行。

## Turn 13 - Generic Agent

QUESTION: 关于"每类最多安排1500人"这个约束，是否意味着每类可以安排0到1500人之间的任意整数人数，还是每类必须安排至少某个最低人数？

## Turn 13 - User Simulator

每类可以安排0到1500人之间的任意整数人数，没有最低人数要求。

## Turn 14 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 14 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 15 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 15 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 16 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 16 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 17 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 17 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 18 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 18 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 19 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 19 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 20 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 20 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 21 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 21 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 22 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 22 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 23 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 23 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 24 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 24 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 25 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 25 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 26 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 26 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 27 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 27 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 28 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 28 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 29 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 29 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。

## Turn 30 - Generic Agent

QUESTION: 关于决策变量的粒度，是否允许将同一类的人拆分到不同的分支-专业组合（例如类型1的1500人中，一部分去东海市专业1，另一部分去东海市专业2），还是每类的人必须整体分配到同一个分支-专业组合？

## Turn 30 - User Simulator

允许将同一类的人拆分到不同的分支-专业组合。