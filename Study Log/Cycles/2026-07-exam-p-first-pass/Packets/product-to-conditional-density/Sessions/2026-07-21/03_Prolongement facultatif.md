---
type: study-session-prolongement
date: 2026-07-21
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
session: J4
solutions-policy: attempt-before-corrige
math-authority: derived
canonical-sources:
  - ../../../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours.md
---

# Prolongement facultatif — Minimum et couches de niveau

*Durée indicative : 20–25 minutes. Hors des 90 minutes.*

Open this file only after the J4 Bilan has been fixed. Attempt it before opening the Corrigé. No indication is provided, and the result does not alter the verdict of the timed séance.

Let $(E,\mathcal A,\mu)$ and $(F,\mathcal B,\nu)$ be $\sigma$-finite measure spaces, and let

$$
u:E\to[0,+\infty],
\qquad
v:F\to[0,+\infty]
$$

be measurable. Prove that $(x,y)\mapsto\min\{u(x),v(y)\}$ is $\mathcal A\otimes\mathcal B$-measurable and establish

$$
\int_{E\times F}\min\{u(x),v(y)\}\,d(\mu\otimes\nu)
=
\int_0^\infty \mu(u>t)\nu(v>t)\,dt.
$$

The identity must be justified in $[0,+\infty]$, including the convention governing a product of a zero and an infinite measure.

Let now $X$ and $Y$ be independent nonnegative random variables. Translate the preceding identity into a formula for $\mathbb E[\min\{X,Y\}]$. Prove that finiteness of either $\mathbb E[X]$ or $\mathbb E[Y]$ is sufficient for this expectation to be finite, and decide whether that condition is necessary.
