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
9. conditional expectation and conditional laws.

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

Therefore $L^p$ remains a foundation interface rather than an independent top-level module.

## Necessary next module

The remaining structural gap is

$$
\text{product measures}
\longrightarrow
\text{Tonelli/Fubini}
\longrightarrow
\text{joint and marginal laws}
\longrightarrow
\text{change of variables}.
$$

This should be built as a formal module after Integration and Convergence. It must not be hidden inside a supplement.

## Excluded from the current core

- full outer-measure construction of Lebesgue measure;
- regular conditional probabilities and disintegration;
- uniform integrability and martingale convergence;
- Banach-space duality and weak compactness.

These topics are legitimate continuations, but they are not prerequisites for the current Exam P bridge.
