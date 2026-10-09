## Turn 1 - Generic Agent

QUESTION: What is the primary objective of this selection process, such as maximizing total work experience, minimizing total salary cost, or simply finding any valid combination that meets the constraints?

## Turn 1 - User Simulator

The primary objective is to minimize the total salary cost for the selected candidates.

## Turn 2 - Generic Agent

QUESTION: Are there any other constraints or preferences, such as requiring at least one candidate with a specific degree level, that should be included in the selection?

## Turn 2 - User Simulator

Yes, at least one of the selected candidates must hold a Master's or a Doctoral degree.

## Turn 3 - Generic Agent

READY_TO_MODEL

I have confirmed the following understanding of your recruitment problem:

**Objective:**
Minimize the total salary cost of the selected candidates.

**Candidates and Attributes:**
- **Candidate A:** Salary $8,100, Experience 3 years, Degree: Bachelor's
- **Candidate B:** Salary $20,000, Experience 10 years, Degree: Master's
- **Candidate C:** Salary $21,000, Experience 4 years, Degree: Doctoral
- **Candidate D:** Salary $3,000, Experience 3 years, Degree: No degree
- **Candidate E:** Salary $8,000, Experience 7 years, Degree: No degree

**Constraints:**
1. **Selection Count:** Select at least 2 and at most 3 candidates.
2. **Budget:** Total salary must not exceed $35,000.
3. **Experience:** Total work experience must be at least 12 years.
4. **Mutual Exclusion:** At most one of Candidate A and Candidate E can be selected.
5. **Degree Requirement:** At least one selected candidate must hold a Master's or Doctoral degree.