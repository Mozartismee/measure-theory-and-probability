---
type: study-packet-overview
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
start: 2026-07-23
end: 2026-07-31
sessions: 8
planned-time: 13h
math-authority: derived
canonical-sources:
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../50_Conditional-Laws/01_Cours/Cours.md
  - ../../../../../90_Review/Density and Version Ledger.md
---

# Product Integration and Conditional Density

*Séances of 23–31 July 2026 · 13 hours*

This programme condenses the first pass of the five-week ENS sequence into eight séances. It retains theorem boundaries, changes of representation, independence as product law, the discipline of choosing versions, and only the CLT interface of probability convergence. A Hahn-first proof of Radon–Nikodym, the outer-measure construction of product measure, the $L^2$ projection theorem, full convergence theory and general disintegration remain outside the present programme.

The schedule and its revision boundary are governed by the [23–31 July scope lock](../../00_Plan.md). Missing Study Log entries do not reopen the curriculum; generated material is treated as approximately mastered for planning, without creating mastery evidence.

## Mathematical line

$$
\text{product integration}
\longrightarrow
\text{joint and marginal laws with independence}
\longrightarrow
\text{conditional expectation}
\longrightarrow
\text{dominated conditional density}.
$$

The iid CLT is a separate terminal deployment branch from independent sums. It is not used to justify the product／conditional-density chain and does not import general weak-convergence theory.

Radon–Nikodym is not retaught in a single séance. It is used repeatedly in change of measure, conditional expectation, state-space densities, Bayes' formula and dominated conditional densities; the common reference is the [Density and Version Ledger](../../../../../90_Review/Density%20and%20Version%20Ledger.md).

## Programme

| Date | Time | Work | Distribution |
| --- | --- | --- | --- |
| 23 July | 19:30–21:00 | [Product measure to independence; joint law to convolution](Sessions/2026-07-23/00_Séance.md) | Two complete dependent problems; no internal time cuts; post hoc Bilan |
| 24 July | 19:30–21:00 | Product Measures TD, Exercise 2(1)–(4); marginal pushforwards and density factorization | One continuous deployment; no second reconstruction of independence |
| 25 July | 10:00–12:00 | Feuille, Exercise 3: triangular transformation | 20 min reading; 75 min attempt; 15 min unfamiliar transfer; 10 min record |
| 26 July | 10:00–12:00 | Feuille, Exercises 4–5: RN representations and variance | 20 min RN review; 25 min CE reading; 60 min attempt; 15 min record |
| 28 July | 19:30–21:00 | Feuille, Exercise 6: dominated conditional density | 20 min reading; 55 min attempt; 15 min review of versions |
| 29 July | 19:30–21:00 | Feuille, Exercise 7: mixture Bayes、moments and dependence boundaries | 15 min recall; 40 min attempt; 20 min independence diagnosis; 10 min Q382; 5 min record |
| 30 July | 19:30–20:30 | Convergence in distribution and CLT deployment | 15 min statement／standardization; 30 min approximation; 10 min continuity correction／boundary; 5 min record |
| 31 July | 19:30–21:30 | Feuille, Exercise 8 and final reconstruction | 60 min reconstruction; 40 min actuarial／independence／CLT deployment; 20 min final record |

## Order of work

Begin on 23 July with the self-contained [problem-driven feuille](Sessions/2026-07-23/00_Séance.md). It replaces the former four-interface checkpoint without changing the packet budget. Open its [Indications](Sessions/2026-07-23/01_Indications.md) only after a recorded illegal step, its [Corrigé](Sessions/2026-07-23/02_Corrig%C3%A9.md) only after both attempts and the Bilan, and its [evening reading](Sessions/2026-07-23/03_Lecture%20du%20soir.md) only after the closed-book work is fixed. The earlier self-contained [J4 feuille](Sessions/2026-07-21/00_Séance.md) remains an optional repair artifact, not a second mandatory séance. Before later séances, read only the corresponding section of the [Preparatory Notes](01_Preparatory%20Notes.md). On 24 July, complete Exercise 2(1)–(4) of the formal [Product Measures TD](../../../../../35_Product-Measures-and-Transformations/02_TD/TD%2001%20—%20Product%20Measures,%20Iterated%20Integrals,%20and%20Transformations.md): parts (1)–(3) deploy marginal pushforwards and part (4) deploys density factorization as the already-established independence interface. The [Feuille de travail](02_Feuille%20de%20travail.md) adds the common model and the later transfer problems; it is not a second TD.

For every séance without a dated session sheet, enter the first complete attempt and the first rupture in the [Carnet](03_Carnet.md) before consulting either the formal corrigé or this module's [Corrigé](04_Corrigé.md). Unassigned questions from the formal TD are reserved for later repair or mastery work.

## Completion

The first pass is complete only if one can, without notes:

1. distinguish Tonelli from Fubini and state the decisive hypotheses;
2. derive marginal laws and densities from a joint law;
3. express independence as equality with the product joint law and use it legally in factorization、convolution and independent-sum moments;
4. identify the numerator, reference measure and a.e. basis in five RN representations;
5. derive conditional expectation, the tower identity and total variance from the RN characterization;
6. construct a dominated conditional kernel, including its completion on a null set;
7. deploy the iid CLT with correct standardization、continuity correction and approximation boundary;
8. identify the measure-theoretic mechanism in Q50, Q386, Q370、Q382 and the assigned independence／CLT anchors.

A Hahn-first proof of RN is not required here. Every use of a theorem must nevertheless include its hypotheses and its measurable space.
