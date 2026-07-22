---
type: study-session-sheet
date: 2026-07-19
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session-kind: progression-with-retrieval
session: J3
planned-time: 120m
actual-time:
solutions-policy: attempt-before-corrige
state: rupture
math-authority: derived
canonical-sources:
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../80_Lemmas/Counting Measure and the Radon–Nikodym Boundary.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields.md
  - ../../../../../../../60_Applications/Exam-P-Bridges/Expectation and Conditioning — Exam P Deployment Bridge.md
  - ../../../../../../../90_Review/Density and Version Ledger.md
---

# Feuille J3 — Restriction normalisée, tribu finie et Bayes

*Durée : deux heures. Sans documents.*

## Session status

Learner report recorded on 20 July: the second half of this séance was not completed. No precise first illegal step, closing exit or Bilan was preserved, so this session supplies no `reconstructible` or `deployable` evidence. The unresolved finite-conditioning responsibility is carried into the [J3bis certification séance](../2026-07-20/00_Séance.md).

數學作答全部另紙完成。正文應是一份可連續閱讀的 démonstration：定義物件、使用假設、選擇表示、證明結論，並指出結論的邊界。

某一 Partie 停滯五分鐘且已寫下論證中斷的精確位置後，才可閱讀 [Indications](01_Indications.md) 中對應的唯一 relance。Question de cours 與 épreuve de sortie 沒有提示。[Corrigé](02_Corrigé.md) 只能在整份 copie 與頁尾 bilan 完成後開啟。

## Question de cours — Trois mécanismes (0–10 minutes)

For each of the following three situations, give only the proof architecture: the auxiliary object, the decisive stability or approximation mechanism, the conclusion, and the exact boundary. No detail may exceed what is needed to reconstruct the argument later.

1. For measurable spaces $(E,\mathcal A)$ and $(F,\mathcal B)$ and for $C\in\mathcal A\otimes\mathcal B$, prove the measurability of every section by passing from rectangles to the generated $\sigma$-field.
2. On $([0,1],\mathcal B([0,1]))$, locate the $\sigma$-finiteness obstruction for counting measure and the singleton contradiction excluding a Radon–Nikodym density of Lebesgue measure with respect to it.
3. For countable $E$, $A\subseteq E$ and $p:E\to[0,+\infty)$, recover
   $$
   \int_A p\,d\#_E=\sum_{x\in A}p(x)
   $$
   from the simple-function identity and monotone convergence, separating finite $A$ from countably infinite $A$.

At the tenth minute, mark the three architectures clean, partial or absent in the margin and continue. These marks neither resolve yesterday's ruptures nor enter the J3 verdict.

## Problème — From restriction to finite conditioning

The four parts form a single argument. Objects constructed in one part remain available in the next.

### I. Restriction normalisée (10–30 minutes)

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $A\in\mathcal F$ satisfy $\mathbb P(A)>0$. Define

$$
\mathbb P_A(C)
:=
\frac{\mathbb P(C\cap A)}{\mathbb P(A)},
\qquad C\in\mathcal F.
$$

Prove that $\mathbb P_A$ is a probability measure and determine its Radon–Nikodym derivative with respect to $\mathbb P$, with the correct domain and almost-sure basis. Deduce the change-of-measure formula for $Y\in L^1(\mathbb P)$.

Conclude by distinguishing the measure $\mathbb P_A$, the scalar $\mathbb E[Y\mid A]$, and the $L^1$ equivalence class $\mathbb E[Y\mid\sigma(A)]$. State exactly what survives, and what ceases to be defined, when $\mathbb P(A)=0$.

### II. Espérance conditionnelle sur une tribu finie (30–55 minutes)

Let $(B_i)_{1\le i\le r}$ be a finite measurable partition of $\Omega$, possibly containing null atoms, and set

$$
\mathcal G=\sigma(B_1,\ldots,B_r).
$$

For $Y\in L^1(\mathbb P)$, determine all versions of $\mathbb E[Y\mid\mathcal G]$. The proof must characterize the real-valued $\mathcal G$-measurable functions, establish integrability, and verify the defining identity for every $C\in\mathcal G$, not merely on the individual atoms. Explain the freedom on null atoms.

Deduce total expectation and total probability. Finally identify the finite signed numerator, the reference measure, the domain and the almost-sure uniqueness basis in the Radon–Nikodym representation.

### III. Renversement bayésien (55–75 minutes)

Let $A\in\mathcal F$ be an observed event. Apply Part II to $\mathbf1_A$, then use the normalized restriction of Part I to derive Bayes' formula for every positive-probability atom $B_j$ when $\mathbb P(A)>0$.

The proof must pass through the joint masses and the total-probability marginal before normalization. Close the argument by locating the failure at a null atom, at a null observed event, and in the attempted event ratio on $\{X=x\}$ for a continuous law. Conditional kernels and continuous conditional densities lie beyond the present problem.

### IV. Inversion d'un mélange fini (75–100 minutes)

A policy belongs to exactly one of two latent classes $B_1,B_2$, both of positive probability. Write

$$
u=\mathbb P(A\mid B_1),
\qquad
v=\mathbb P(A\mid B_2),
\qquad
m=\mathbb P(A),
\qquad
\alpha=\mathbb P(B_1).
$$

Establish the affine relation between $m$ and $\alpha$. Then take

$$
u=\frac45,
\qquad
v=\frac3{10},
\qquad
m=\frac12.
$$

Determine the latent-class proportions, reconstruct the complete joint law of class and observation, and compute $\mathbb P(B_1\mid A)$. Your conclusion must distinguish inversion of the forward mixture from posterior normalization.

This is a new Q370-type problem; it uses no external statement or solution.

## Épreuve de sortie — Sans retour au problème (100–115 minutes)

### A. Restitution symbolique (9 minutes)

On one page, reconstruct

$$
\text{normalized restriction}
\longrightarrow
\text{finite-partition conditional expectation}
\longrightarrow
\text{total probability}
\longrightarrow
\text{Bayes}.
$$

The page must contain the positivity and integrability hypotheses, the relevant reference measures and almost-sure bases, the verification for arbitrary $C\in\mathcal G$, and the null-atom version boundary.

### B. Transfert numérique inédit (6 minutes)

Let $(B_1,B_2)$ be a partition with

$$
\mathbb P(B_1)=\frac13,
\qquad
\mathbb P(A\mid B_1)=\frac34,
\qquad
\mathbb P(A\mid B_2)=\frac14.
$$

Construct the two joint masses, then determine $\mathbb P(A)$ and $\mathbb P(B_1\mid A)$.

## Fin de séance (115–120 minutes)

Before opening the Corrigé, write a five-line note at the bottom of the copie: actual duration; the three question-de-cours marks; the exact indications consulted; the result of the two exit questions and the precise point where a proof ceased to be legal; what must be revisited later and the J3 verdict.

The verdict reconstructible requires a complete attempt and a legal, hint-free exit. The opening question does not enter this verdict, and one successful séance does not make the whole packet deployable.

## Références après la séance

- [Conditional Expectation Cours](../../../../../../../40_Conditional-Expectation/01_Cours/Cours.md), §§1, 4 and 6.
- [Finite Sigma-Fields TD](../../../../../../../40_Conditional-Expectation/02_TD/TD%2002%20—%20Finite%20Sigma-Fields.md), Exercises 1 and 3.
- [Density and Version Ledger](../../../../../../../90_Review/Density%20and%20Version%20Ledger.md).
- [Expectation and Conditioning — Exam P Deployment Bridge](../../../../../../../60_Applications/Exam-P-Bridges/Expectation%20and%20Conditioning%20—%20Exam%20P%20Deployment%20Bridge.md), §3.
- [18 July rupture séance](../2026-07-18/00_Séance.md), for deferred homework only.
