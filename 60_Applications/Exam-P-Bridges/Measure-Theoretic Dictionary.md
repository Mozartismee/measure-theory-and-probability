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
| Atomic density $d\mu/d\#_E$ | pmf on a countable state space | $\mu(A)=\sum_{x\in A}p(x)$ |
| Fibre pushforward $g_\#\mu_X$ | transformed discrete payment or coarsened category | $p_{g(X)}(y)=\sum_{x:g(x)=y}p_X(x)$ |
| Product law $\mu_X\otimes\mu_Y$ | independence of discrete variables | $p_{X,Y}(x,y)=p_X(x)p_Y(y)$ |
| Addition pushforward of a product law | sum of independent discrete variables | $p_{X+Y}(n)=\sum_kp_X(k)p_Y(n-k)$ |
| Uniform law on finite samples | hypergeometric sampling without replacement | $\binom Kk\binom{N-K}{n-k}/\binom Nn$ |
| Hitting-time pushforward of Bernoulli trials | geometric or negative-binomial waiting time | $\{T_r\le n\}=\{\sum_{i=1}^nB_i\ge r\}$ |
| Density $d\mu_X/d\lambda$ | pdf | $\mathbb E[\varphi(X)]=\int\varphi(x)f_X(x)\,dx$ |
| Mixture of measures | total probability / mixed population | $\mu=\sum_i p_i\mu_i$ |
| Mixture expectation | law of total expectation | $\mathbb E[X]=\sum_i p_i\mathbb E[X\mid I=i]$ |
| Mixture variance | conditional variance decomposition | $\operatorname{Var}(X)=\mathbb E[\operatorname{Var}(X\mid I)]+\operatorname{Var}(\mathbb E[X\mid I])$ |
| Conditional expectation on a finite $\sigma$-field | conditioning on a partition | constant on each atom of the partition |
| State-space RN derivative | conditional density / Bayes factor | $\mathbb P(D)\,d\mu_D/d\mu_X=g_D$ |

## Study direction

The theory files should be read from object to representation. Exam P problems are usually solved in the reverse direction: recognize the representation already hidden in a density, mixture or conditional formula, then calculate.

The complete expectation/conditioning first pass is organized in [Expectation and Conditioning — Exam P Deployment Bridge](Expectation%20and%20Conditioning%20—%20Exam%20P%20Deployment%20Bridge.md). The discrete-family subcycle is organized in [Discrete Distributions — One-Week Deployment Route](Discrete%20Distributions%20—%20One-Week%20Deployment%20Route.md).

## Boundary

This bridge does not replace the Exam P syllabus with abstract measure theory. It identifies which abstract representation controls a familiar calculation, then returns immediately to the admissible computational regime.
