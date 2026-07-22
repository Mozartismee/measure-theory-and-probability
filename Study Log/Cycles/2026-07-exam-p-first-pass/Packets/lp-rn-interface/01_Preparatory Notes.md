---
type: study-packet-notes
date: 2026-07-14
cycle: 2026-07-exam-p-first-pass
packet: lp-rn-interface
math-authority: derived
canonical-sources:
  - ../../../../../15_Lp-Interface/01_Cours/Cours.md
  - ../../../../../15_Lp-Interface/01_Cours/Cours 02 — Hölder, Jensen, and L2 Geometry.md
  - ../../../../../15_Lp-Interface/02_TD/TD 01 — Integrability, Test Functions, and Change of Measure.md
  - ../../../../../20_Radon-Nikodym/01_Cours/Cours.md
---

# Preparatory Notes

*$L^p$ spaces and Radon–Nikodym representations*

These notes contain only what is needed for the séance of 14 July. Full definitions, proofs, and theorem statements remain in the formal $L^p$ Cours, TD, and Radon–Nikodym Cours.

## 1. Ambient measure and the $L^p$ object

Let $(E,\mathcal A,\mu)$ be a measure space. For $1\le p<+\infty$,

$$
L^p(\mu)
=
\left\{
f:E\to\mathbb R\text{ measurable}:
\int_E|f|^p\,d\mu<+\infty
\right\}\big/\!\sim_\mu,
$$

where

$$
f\sim_\mu g
\quad\Longleftrightarrow\quad
f=g
\qquad\mu\text{-almost everywhere}.
$$

Thus the measure is part of the object. Changing the ambient measure may change:

1. integrability;
2. the norm;
3. the null sets;
4. the equivalence class represented by the same pointwise formula.

On a probability space,

$$
X\in L^p(\mathbb P)
\quad\Longleftrightarrow\quad
\mathbb E[|X|^p]<+\infty.
$$

Read §§1.1–1.3 of the [$L^1$ Cours](../../../../../15_Lp-Interface/01_Cours/Cours.md). Reconstruct the object and its hypotheses; do not merely memorize the direction of an inclusion.

## 2. Probability-space hierarchy and pairings

If $1\le p<q\le+\infty$, then

$$
\|X\|_p\le\|X\|_q
\qquad
\text{for }X\in L^q(\mathbb P).
$$

In particular,

$$
L^\infty(\mathbb P)
\subseteq
L^2(\mathbb P)
\subseteq
L^1(\mathbb P).
$$

The hierarchy has distinct probabilistic uses:

| Space | Later use |
| --- | --- |
| $L^1(\mathbb P)$ | finite expectation and finite signed RN numerator |
| $L^\infty(\mathbb P)$ | indicators, bounded payments and bounded tests |
| $L^2(\mathbb P)$ | second moments, covariance and variance decomposition |
| $L^q(\mathbb P)$, $q>1$ | a sufficient moment regime for entry into $L^1$ |

Hölder supplies two products used repeatedly later:

$$
Y\in L^1,\ Z\in L^\infty
\Longrightarrow
YZ\in L^1,
$$

and

$$
U,V\in L^2
\Longrightarrow
UV\in L^1.
$$

The first legitimizes bounded tests. The second legitimizes covariance and the cross term in total variance. Full Hilbert-space projection is not required here.

Read only the Cauchy–Schwarz statement in §3 of [Hölder, Jensen, and $L^2$ Geometry](../../../../../15_Lp-Interface/01_Cours/Cours%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md). Do not enter the projection theorem.

## 3. Indicators and bounded tests

Let $f\in L^1(\mu)$ and $Z\in L^\infty(\mu)$. Then

$$
\int_E|fZ|\,d\mu
\le
\|Z\|_\infty\|f\|_1.
$$

If two $L^1$ functions have equal integrals over every event in a sub-$\sigma$-field $\mathcal G$, the equality extends:

$$
\text{indicator tests}
\longrightarrow
\text{bounded simple tests}
\longrightarrow
\text{bounded }\mathcal G\text{-measurable tests}.
$$

The last passage uses dominated convergence. This is the direct $L^p$ input to conditional-expectation characterization and tower arguments.

Complete Exercise 2(1)–(2), (4) in the formal [$L^p$ TD 01](../../../../../15_Lp-Interface/02_TD/TD%2001%20—%20Integrability,%20Test%20Functions,%20and%20Change%20of%20Measure.md).

## 4. Density generation and RN reversal

For measurable $h\ge0$,

$$
(h\mu)(A)=\int_Ah\,d\mu
$$

defines a positive measure and $h\mu\ll\mu$. No integrability or $\sigma$-finiteness is needed for this forward construction.

For $f\in L^1(\mu)$,

$$
\nu_f(A)=\int_Af\,d\mu
$$

defines a finite signed measure satisfying $\nu_f\ll\mu$. Its total variation is

$$
|\nu_f|=|f|\mu.
$$

The reverse direction is Radon–Nikodym. In the standard positive regime,

$$
\mu,\nu\text{ are }\sigma\text{-finite},
\qquad
\nu\ll\mu
\Longrightarrow
\nu=\frac{d\nu}{d\mu}\,\mu.
$$

The derivative is unique $\mu$-almost everywhere. For a finite signed numerator, apply the positive theorem to its Jordan parts; do not silently apply a positive-measure theorem to a signed object.

The construction of the Radon–Nikodym theorem is prior knowledge. Read only §§1–3 and the uniqueness statement in the [Radon–Nikodym Cours](../../../../../20_Radon-Nikodym/01_Cours/Cours.md). The Hahn local argument is not part of this séance.

## 5. Change of measure

If $\nu=h\mu$, then for every nonnegative measurable $\varphi$, and for every signed $\varphi$ satisfying the corresponding integrability condition,

$$
\int_E\varphi\,d\nu
=
\int_E\varphi h\,d\mu.
$$

Consequently,

$$
\varphi\in L^1(\nu)
\quad\Longleftrightarrow\quad
\varphi h\in L^1(\mu).
$$

The relation $\nu\ll\mu$ transfers $\mu$-a.e. identities to $\nu$-a.e. identities. It does not, by itself, transfer every $L^1(\mu)$ function into $L^1(\nu)$.

Complete Exercise 3(3), (5) and Exercise 4(1) in the formal $L^p$ TD 01.

## 6. Four later uses of Radon–Nikodym

The same theorem is used on different measurable spaces:

| Date | Numerator | Reference measure | Use |
| --- | --- | --- | --- |
| 07-14 | $f\mu$ | $\mu$ | density generation and uniqueness |
| 07-17 | law $\mu_X=X_\#\mathbb P$ | none until a dominating reference is chosen | LOTUS and law-level expectation |
| 07-19 | $\mathbb P_B$ | $\mathbb P$ | normalized event restriction |
| 07-24 | $\mu_X$, $\mu_{X,Z}$ | Lebesgue or product Lebesgue measure | density, joint density, marginalization |
| 07-26 | $A\mapsto\mathbb E[Y\mathbf1_A]$ on $\mathcal G$ and $X_\#(Y\mathbb P)$ | $\mathbb P|_{\mathcal G}$ and $\mu_X$ | probability-space and state-space conditional representatives |
| 07-28 | conditional kernel $K(x,\cdot)$ | $\lambda_m$ after domination | conditional density and version completion |
| 07-29 | $p_i\mu_i$ | mixture law $\mu_X$ | Bayes posterior |

A law is already a measure. It becomes a density only after a reference measure and an absolute-continuity relation have been supplied.

For this module, complete only the general row and three preview rows. Each later séance must prove its own numerator measure, absolute continuity, and version statement.
