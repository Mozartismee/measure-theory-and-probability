---
type: study-packet-notes
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
start: 2026-07-21
end: 2026-07-31
math-authority: derived
canonical-sources:
  - ../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../20_Radon-Nikodym/01_Cours/Cours.md
  - ../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../50_Conditional-Laws/01_Cours/Cours.md
  - ../../../../../90_Review/Density and Version Ledger.md
---

# Preparatory Notes — Product Integration and Conditional Density

Read only the section assigned to the séance. Reconstruct the indicated statements before opening the cited Cours.

## 21 July — Product objects and Tonelli

Reconstruct the following objects without notes (10 minutes).

Let $\mathcal R$ be the ring of finite disjoint unions of measurable rectangles. Define

$$
m_0\!\left(\bigsqcup_{i=1}^r A_i\times B_i\right)
=
\sum_{i=1}^r\mu(A_i)\nu(B_i).
$$

Then mark the boundary of the construction:

$$
\text{rectangle premeasure}
\to
\text{Carathéodory extension}
\to
\sigma\text{-finite uniqueness}.
$$

Indicate where well-definedness, countable additivity, extension and $\sigma$-finite uniqueness enter. Do not reprove the extension theorem or unfold the outer-measure construction. Read [Product Measures Cours](../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md) §§1–3, then complete Exercise A of the formal [Product Measures TD](../../../../../35_Product-Measures-and-Transformations/02_TD/TD%2001%20—%20Product%20Measures,%20Iterated%20Integrals,%20and%20Transformations.md). The following chain must be reconstructible:

$$
\text{rectangles}
\to
\mathcal A\otimes\mathcal B,
\qquad
f\ge0
\xrightarrow{\text{Tonelli}}
\text{iterated integrals in }[0,+\infty].
$$

Exercise 0 of the Feuille merely assigns this question; it is not a duplicate.

## 22 July — Fubini and failure

Read Product Measures Cours §4 and complete Exercise 0 of the formal TD. Distinguish:

$$
\text{positivity}
\quad\text{versus}\quad
\int|f|<+\infty.
$$

Do not replace the counterexample by the phrase “conditionally convergent”. Compute both iterated sums and the absolute sum.

Exercise 1 of the Feuille merely assigns this question; it does not repeat it.

## 24 July — Joint law and marginalization

Read Product Measures Cours §6 and Propositions 1–2 of [Pushforwards and Laws](../../../../../30_Pushforwards-and-Laws/01_Cours/Cours.md). Complete Exercise 2(1)–(4) of the formal TD. Parts (1)–(3) supply the marginal pushforward mechanism used in the triangular model of Exercise 2 in the [Feuille de travail](02_Feuille%20de%20travail.md); part (4) is a separate density-factorization deployment and does not assert that the triangular density factorizes. Reconstruct:

$$
\mu_{X,Z}
\xrightarrow{\pi_X}
\mu_X
\xrightarrow{\ll\lambda_d}
f_X,
\qquad
f_{X,Y}=f_Xf_Y\ \text{a.e.}
\Longrightarrow
\mu_{X,Y}=\mu_X\otimes\mu_Y.
$$

The first arrow is a pushforward. The second is an RN representation. Tonelli computes the density. The final implication deploys the product-law criterion established on 23 July; it does not reconstruct that criterion again.

## 25 July — Transformation

Read Product Measures Cours §7 and complete Exercise 3 of the [Feuille de travail](02_Feuille%20de%20travail.md). In this first pass, use only $C^1$-diffeomorphisms and compute the inverse and Jacobian explicitly. Exercise 3 of the formal TD is deferred.

## 26 July — Radon–Nikodym representations

First recover the [$L^p$ preliminaries from 14 July](../lp-rn-interface/00_Overview.md) without notes: $L^1\times L^\infty\to L^1$ justifies bounded tests, while $L^2\times L^2\to L^1$ justifies the cross terms in the variance identity. If either fact is unavailable, enter the rupture in the Carnet before continuing.

Spend at most 25 minutes on §§1–2 and the theorem statement in the [Radon–Nikodym Cours](../../../../../20_Radon-Nikodym/01_Cours/Cours.md). Then read, for 20 minutes:

- [Conditional Expectation Cours](../../../../../40_Conditional-Expectation/01_Cours/Cours.md) §§1–5;
- [Density and Version Ledger](../../../../../90_Review/Density%20and%20Version%20Ledger.md) §§0–3.

Reconstruct:

$$
Y
\longmapsto
\nu_Y(A)=\mathbb E[Y\mathbf1_A]
\longmapsto
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
\longmapsto
\mathbb E[Y\mid\mathcal G].
$$

The maximal-mass proof is not part of this séance.

Complete Exercises 4–5 of the [Feuille de travail](02_Feuille%20de%20travail.md).

## 28 July — Dominated conditional density

Read §§2 and 4 of the [Conditional Laws Cours](../../../../../50_Conditional-Laws/01_Cours/Cours.md), then complete Exercise 6 of the [Feuille de travail](02_Feuille%20de%20travail.md). Consult Exercise 2 of the formal Dominated Conditional Densities TD only after a complete attempt, and only if a rupture remains.

Keep distinct:

$$
f_{X,Z},
\qquad
f_X,
\qquad
k(x,z),
\qquad
K(x,B).
$$

## 29 July — Mixture Bayes and conditional moments

Read §§5–7 of [Expectation and Conditioning for Exam P](../../../../../60_Applications/Exam-P-Bridges/Expectation%20and%20Conditioning%20—%20Exam%20P%20Deployment%20Bridge.md), then complete Exercise 7 of the [Feuille de travail](02_Feuille%20de%20travail.md). Identify the discrete conditional distribution before answering official question Q382. Exercise 3 of formal Conditional Laws TD 02 is reserved for later repair.

## 31 July — Reconstruction

No new reading. Complete the 60-minute reconstruction in the [Feuille de travail](02_Feuille%20de%20travail.md), followed by Exercise 8 and the four actuarial examples. Complete the [Carnet](03_Carnet.md) before opening any remaining corrigé.
