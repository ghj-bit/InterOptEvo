## Turn 1 - Generic Agent

```json
{
  "action": "ASK",
  "question": "How should the hiring decision treat each candidate?",
  "options": [
    {
      "id": "A",
      "text": "Each candidate can be hired at most once, so the choice is simply hire or not hire."
    },
    {
      "id": "B",
      "text": "A candidate can be hired multiple times if that helps meet the team requirements."
    },
    {
      "id": "C",
      "text": "A candidate can be hired partially, such as for a fraction of their salary and contribution."
    }
  ],
  "allow_other": true
}
```

Question:
How should the hiring decision treat each candidate?

Options:
A. Each candidate can be hired at most once, so the choice is simply hire or not hire.
B. A candidate can be hired multiple times if that helps meet the team requirements.
C. A candidate can be hired partially, such as for a fraction of their salary and contribution.
D. None of the above — I'd like to explain in my own words.

## Turn 1 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 2 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "Confirmed: choose a subset of the five candidates F, G, H, I, J to hire, with each candidate hired at most once. Minimize total salary. Constraints: total salary <= $40,000; number hired <= 4; total skill >= 8; total project management experience >= 8 years. All candidate data and parameter values are given. No remaining material assumptions."
}
```

Confirmed: choose a subset of the five candidates F, G, H, I, J to hire, with each candidate hired at most once. Minimize total salary. Constraints: total salary <= $40,000; number hired <= 4; total skill >= 8; total project management experience >= 8 years. All candidate data and parameter values are given. No remaining material assumptions.