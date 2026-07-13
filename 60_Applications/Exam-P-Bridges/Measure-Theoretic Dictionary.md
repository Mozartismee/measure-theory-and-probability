---
type: application
module: applications
status: canonical
---

# Measure-Theoretic Dictionary for Exam P

This file translates the structural language of the project into the calculation regimes that recur in Exam P.

| Structural object | Exam P manifestation | Canonical identity |
| --- | --- | --- |
| Pushforward law $X_\#\mathbb P$ | distribution of a transformed random variable | $\mathbb E[\varphi(X)]=\int\varphi\,d\mu_X$ |
| Density $d\mu_X/d\lambda$ | pdf | $\mathbb E[\varphi(X)]=\int\varphi(x)f_X(x)\,dx$ |
| Mixture of measures | total probability / mixed population | $\mu=\sum_i p_i\mu_i$ |
| Mixture expectation | law of total expectation | $\mathbb E[X]=\sum_i p_i\mathbb E[X\mid I=i]$ |
| Mixture variance | conditional variance decomposition | $\operatorname{Var}(X)=\mathbb E[\operatorname{Var}(X\mid I)]+\operatorname{Var}(\mathbb E[X\mid I])$ |
| Conditional expectation on a finite $\sigma$-field | conditioning on a partition | constant on each atom of the partition |
| State-space RN derivative | conditional density / Bayes factor | $\mathbb P(D)\,d\mu_D/d\mu_X=g_D$ |

## Study direction

The theory files should be read from object to representation. Exam P problems are usually solved in the reverse direction: recognize the representation already hidden in a density, mixture or conditional formula, then calculate.

## Boundary

This bridge does not replace the Exam P syllabus with abstract measure theory. It identifies which abstract representation controls a familiar calculation, then returns immediately to the admissible computational regime.
