---
type: study-packet-notes
start: 2026-07-17
end: 2026-07-19
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
math-authority: derived
canonical-sources:
  - ../../../../../15_Lp-Interface/01_Cours/Cours.md
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Pushforward Integration Formula.md
  - ../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../90_Review/Density and Version Ledger.md
---

# Preparatory Notes — Representation Chains

These notes prescribe the shortest reading order across the canonical Cours; they do not replace them. First recover, without notes, the $L^q\subseteq L^1$ embedding, bounded-test pairing, and density-generation/RN-reversal boundary from the [14 July Preparatory Notes](../lp-rn-interface/01_Preparatory%20Notes.md). Stop at the first rupture rather than turning this module into a second RN course.

## 1. From $L^1$ to a measure

For $Y\in L^q(\mathbb P)$ with $q>1$, the probability-space embedding gives $Y\in L^1(\mathbb P)$. Hence, for every sub-$\sigma$-field $\mathcal G\subseteq\mathcal F$,

$$
\nu_Y^{\mathcal G}(A)=\int_AY\,d\mathbb P,
\qquad A\in\mathcal G,
$$

defines a finite signed measure satisfying $\nu_Y^{\mathcal G}\ll\mathbb P|_{\mathcal G}$. Signed Radon–Nikodym therefore supplies a representative in $L^1(\mathbb P|_{\mathcal G})$, unique $\mathbb P$-almost surely. The present package retrieves this interface; it does not re-prove density generation, maximal represented mass or residue elimination.

Read [The $L^1$–$L^\infty$ Interface](../../../../../15_Lp-Interface/01_Cours/Cours.md) §§1.4–2.2. Every $L^1$ statement must name its ambient measure; every RN derivative must name its numerator, reference measure, and a.e. basis.

## 2. Expectation and law

Let $X:\Omega\to\overline{\mathbb R}$ be measurable.

- If $X\ge0$, then $\mathbb E[X]\in[0,+\infty]$ is defined.
- For signed $X$, $\mathbb E[X]$ is defined unless both $\mathbb E[X^+]$ and $\mathbb E[X^-]$ are infinite.
- If $X\in L^1$, then $\mathbb E[X]$ is finite.

For $\mu_X=X_\#\mathbb P$,

$$
\mathbb E[\varphi(X)]
=
\int\varphi\,d\mu_X.
$$

Read the [Pushforward Integration Formula](../../../../../30_Pushforwards-and-Laws/01_Cours/Pushforward%20Integration%20Formula.md). Close the file, then reconstruct the proof in the order indicators $\to$ simple functions $\to$ nonnegative functions $\to$ signed functions.

## 3. Tail integration and transformations

For $X\ge0$,

$$
\mathbb E[X]
=
\int_0^\infty\mathbb P(X>t)\,dt.
$$

This is a Tonelli identity for the subgraph indicator.

Read Theorem 3.1 and §5 of the [Product Measures Cours](../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md), then complete Exercise 1(1)–(2) in the formal [Product Measures TD](../../../../../35_Product-Measures-and-Transformations/02_TD/TD%2001%20—%20Product%20Measures,%20Iterated%20Integrals,%20and%20Transformations.md). This is the only proof of the tail formula assigned here; Exercise 2 merely deploys it. This work is deferred from 18 July until the repair séance is closed.

For a deductible $d$ and cap $u$,

$$
\mathbb E[(X-d)_+]
=
\int_d^\infty\mathbb P(X>t)\,dt,
$$

and

$$
\mathbb E[X\wedge u]
=
\int_0^u\mathbb P(X>t)\,dt.
$$

Both are consequences of the same tail formula applied to a transformed random variable.

## 4. Conditioning as normalized restriction

For $B\in\mathcal F$ with $\mathbb P(B)>0$,

$$
\mathbb P_B(A)
=
\frac{\mathbb P(A\cap B)}{\mathbb P(B)},
\qquad
\frac{d\mathbb P_B}{d\mathbb P}
=
\frac{\mathbf1_B}{\mathbb P(B)}.
$$

The ratio formula does not condition on a null event. Continuous conditioning requires a state-space representation and a version choice, which belongs to the second July package.

Read §6 of the [Conditional Expectation Cours](../../../../../40_Conditional-Expectation/01_Cours/Cours.md).

## 5. Finite partitions

Let $(B_i)_{1\le i\le r}$ be a measurable partition with $\mathbb P(B_i)>0$ and let $\mathcal G=\sigma(B_1,\ldots,B_r)$. A $\mathcal G$-measurable candidate must be constant on each atom. The integral identities determine the constants:

$$
\mathbb E[Y\mid\mathcal G]
=
\sum_{i=1}^r
\frac{\mathbb E[Y\mathbf1_{B_i}]}{\mathbb P(B_i)}
\mathbf1_{B_i}.
$$

Thus measurability determines the form; integration determines the coefficients. Bayes and total expectation are consequences of this partition structure, not additional axioms.

Only after a complete attempt at Exercise 3 may the [Finite Sigma-Fields TD](../../../../../40_Conditional-Expectation/02_TD/TD%2002%20—%20Finite%20Sigma-Fields.md) be used as a repair reference. It is not an additional assignment.

## 6. Ledger closure

A density without its numerator and reference measures is not compressed notation; it is missing data.

After each section, enter the corresponding evidence in the [Carnet](03_Carnet.md). Consult the canonical [Density and Version Ledger](../../../../../90_Review/Density%20and%20Version%20Ledger.md) only after a complete attempt. The Study Log does not rewrite that ledger.
