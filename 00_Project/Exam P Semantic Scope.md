---
type: project-scope
module: project
status: canonical
---

# Exam P Semantic Scope

## Mandatory measure-theoretic core

1. measurable functions, random variables and generated $\sigma$-fields;
2. construction of the integral;
3. MCT, Fatou and DCT;
4. product measures, Tonelli and Fubini;
5. pushforwards, laws, densities and transformations;
6. change of variables;
7. mixtures and total expectation/variance;
8. Radon–Nikodym representation;
9. conditional expectation and conditional laws;
10. independence of events and random variables, including product joint laws、factorization、independent sums and their moments;
11. the iid Central Limit Theorem as a terminal approximation interface.

## Role of $L^p$

For Exam P, the deployable interface is

$$
L^1
\quad\text{for expectation and RN},
$$

$$
L^2
\quad\text{for moments, variance and projection},
$$

$$
L^\infty
\quad\text{for bounded test functions}.
$$

Hölder, Cauchy–Schwarz and Jensen are required. Completeness of $L^p$, density theorems, full duality, weak convergence and Fourier analysis belong to the advanced analysis line, not the Exam P deployment core.

Therefore $L^p$ has a visible interface module for architectural separation, but not the scope of an independent full theory. Its boundary is semantic: only the structures consumed by probability and the main proof line belong there.

## Product-integration bridge

The structural bridge is

$$
\text{product measures}
\longrightarrow
\text{Tonelli/Fubini}
\longrightarrow
\text{joint and marginal laws}
\longrightarrow
\text{change of variables}.
$$

The formal [Product Measures and Transformations](../35_Product-Measures-and-Transformations/00_Module%20Map.md) module supplies this bridge after Integration and Convergence. Its current completion state and missing training roles belong exclusively to the Module Map; this scope file does not mirror them.

## Independence and probability-convergence boundary

Independence is part of the mandatory deployment core, not an optional consequence. The required structural interface is

$$
\text{event factorization}
\longrightarrow
\text{joint law as a product law}
\longrightarrow
\text{density／pmf factorization}
\longrightarrow
\text{convolution and independent-sum moments}.
$$

The current core also retains the iid CLT with finite nonzero variance, correct standardization, continuity correction for lattice sums and the distinction between approximation and exact law identity. It does not expand this terminal interface into a general theory of almost-sure、in-probability、$L^p$ or weak convergence.

## Excluded from the current core

- full outer-measure construction of Lebesgue measure;
- general existence theory for regular conditional probabilities and disintegration;
- uniform integrability and martingale convergence;
- general probability-convergence theory beyond the iid CLT deployment interface;
- Banach-space duality and weak compactness.

These topics are legitimate continuations, but they are not prerequisites for the current Exam P bridge.
