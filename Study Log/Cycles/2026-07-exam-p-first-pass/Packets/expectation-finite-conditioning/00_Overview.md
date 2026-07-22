---
type: study-packet-overview
start: 2026-07-17
end: 2026-07-20
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
sessions: 4
planned-time: 450m
math-authority: derived
canonical-sources:
  - ../../../../../15_Lp-Interface/01_Cours/Cours.md
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Pushforward Integration Formula.md
  - ../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../90_Review/Density and Version Ledger.md
---

# Overview — Expectation and Finite Conditioning

*Séances of 17–20 July 2026 · 450 minutes*

This module follows the [14 July prerequisite module](../lp-rn-interface/00_Overview.md). It assumes no completed record there and does not reteach Radon–Nikodym. The aim is to recover four distinct interfaces:

$$
\begin{aligned}
Y\in L^1(\mathbb P)
&\Longrightarrow
\mathbb E[Y]\text{ is finite and }Y\mathbb P\text{ is finite signed},\\
X\longmapsto\mu_X=X_\#\mathbb P
&\Longrightarrow
\mathbb E[\varphi(X)]=\int\varphi\,d\mu_X,\\
\mathbb P_B\text{ and finite partitions}
&\Longrightarrow
\text{Bayes and finite-partition conditional expectation},\\
C\longmapsto\mathbb E[Y\mathbf1_C]\text{ on }\mathcal G
&\Longrightarrow
\text{general conditional expectation by Radon--Nikodym}.
\end{aligned}
$$

The first is an admissibility gate, the second a pushforward representation, the third normalized restriction, and the fourth a probability-space Radon–Nikodym representation. The additional 20 July certification séance brings the fourth interface forward; state-space transfer remains scheduled later. RN is not an intermediate definition of a law or an unconditional expectation.

## Aim

Work at ENS L3+/M1 theorem boundaries. Exam P problems serve only as terminal tests. The expected work is a closed-book proof, an exact density ledger, the first rupture, and its minimal repair.

## Séance 1 — Friday, 17 July, 19:30–21:00

1. **15 min.** Complete Exercise 0 in the [Feuille de travail](02_Feuille%20de%20travail.md). Recover only
   $L^q\to L^1\to$ finite signed numerator $\to$ RN representative.
2. **25 min.** Read §§1–2 of the [Preparatory Notes](01_Preparatory%20Notes.md).
3. **40 min.** Complete Exercise 1.
4. **10 min.** Enter the law $\mu_X=X_\#\mathbb P$ in the density ledger. Add
   $d\mu_X/d\lambda$ only under the extra hypothesis $\mu_X\ll\lambda$.

At the board: reconstruct LOTUS from the pushforward definition; distinguish nonnegative, defined signed, and $L^1$ expectations; explain why a law need not have a Lebesgue density.

## Séance 2 — Saturday, 18 July, 10:00–12:00

The first product-space and counting-measure ruptures take priority. Complete the self-contained [Séance — Generated $\sigma$-Fields and Counting Measures](Sessions/2026-07-18/00_Séance.md).

This séance replaces the former 18 July programme. Tail integration remains as Exercise 2 in the module worksheet; Q50 and Q386 remain deferred deployment anchors in the Carnet. The unresolved repair mechanisms remain explicit homework debts; they are not treated as resolved and do not consume J3 beyond its capped retrieval.

At the board: prove measurable sections by a stable-class argument; locate the $\sigma$-finiteness boundary for counting measure; derive the atomic integral from simple functions and monotone convergence.

## Séance 3 — Sunday, 19 July, 10:00–12:00

Complete the self-contained [Feuille J3 — Restriction normalisée, tribu finie et Bayes](Sessions/2026-07-19/00_Séance.md). It uses ten minutes for bounded rupture retrieval, then treats normalized restriction, finite-partition conditional expectation, Bayes, a Q370-type analogue and a fresh closing exit.

At the board: derive Bayes from normalized restriction and total expectation from finite-partition conditional expectation.

## Séance 4 — Monday, 20 July, 120 minutes

The second half of J3 was not completed, and the learner's subsequent reconstruction of the conditional-expectation skeleton has no timed exit evidence. Complete the self-contained [Feuille J3bis — Reconstruction de l'espérance conditionnelle et déploiement Exam P](Sessions/2026-07-20/00_Séance.md).

The séance first closes normalized restriction, finite partitions and Bayes, then certifies the general $L^1$ Radon–Nikodym construction, test functions, uniqueness, tower, finite-mixture transfer and total variance. It does not introduce state-space conditional expectation, conditional densities or kernels.

## References

- [Integration and Convergence](../../../../../10_Integration-and-Convergence/01_Cours/Cours.md)
- [Pushforward Integration Formula](../../../../../30_Pushforwards-and-Laws/01_Cours/Pushforward%20Integration%20Formula.md)
- [Product Measures Cours](../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md) §5
- [Product Measures TD](../../../../../35_Product-Measures-and-Transformations/02_TD/TD%2001%20—%20Product%20Measures,%20Iterated%20Integrals,%20and%20Transformations.md) Exercise 1(1)–(2)
- [Conditional Expectation Cours](../../../../../40_Conditional-Expectation/01_Cours/Cours.md) §6
- [Density and Version Ledger](../../../../../90_Review/Density%20and%20Version%20Ledger.md)
- [Exam P Deployment Bridge](../../../../../60_Applications/Exam-P-Bridges/Expectation%20and%20Conditioning%20—%20Exam%20P%20Deployment%20Bridge.md)

## Polycopiés

- [Student Handout](Polycopiés/Student%20Handout.pdf)
- [Independent Corrigé](Polycopiés/Independent%20Corrigé.pdf)
- [Overleaf Sources](Polycopiés/Overleaf%20Sources.zip)
- [LaTeX source notes](Sources/LaTeX/README.md)

The legacy Student Handout predates the 18–20 July session replacements and is not the J3 or J3bis working document.

## Rule

Do not read the corrigé before a complete attempt. At a rupture, repair the first illegal step only; a weekend spent ceremonially re-proving Radon–Nikodym would miss the object.
