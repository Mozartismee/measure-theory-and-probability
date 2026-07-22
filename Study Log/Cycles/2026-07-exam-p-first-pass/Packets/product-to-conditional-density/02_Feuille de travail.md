---
type: study-packet-work-sheet
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
start: 2026-07-21
end: 2026-07-31
math-authority: derived
canonical-sources:
  - ../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../40_Conditional-Expectation/02_TD/TD 01 — RN Construction.md
  - ../../../../../50_Conditional-Laws/02_TD/TD 02 — Dominated Conditional Densities.md
---

# Feuille de travail — Product Integration and Conditional Density

This feuille is not a second formal TD. Exercises 0 and 1 assign questions from the Product Measures TD; Exercises 2–8 belong to the present module. Complete a full attempt and enter the first rupture in the [Carnet](03_Carnet.md) before opening the [Corrigé](04_Corrigé.md).

Use the same model in Exercises 2, 3 and 6. Passing one object through several representations is part of the work.

## Exercise 0 — Tonelli assignment

Complete Exercise A in the formal [Product Measures TD](../../../../../35_Product-Measures-and-Transformations/02_TD/TD%2001%20—%20Product%20Measures,%20Iterated%20Integrals,%20and%20Transformations.md). Record the first failed step, if any, in the Carnet. This is an assignment, not an additional exercise.

## Exercise 1 — Failure of Fubini

Complete Exercise 0 in the formal Product Measures TD. Record both iterated sums, the absolute sum and the first failed theorem hypothesis. This is an assignment, not an additional exercise.

## Exercise 2 — One joint law, two marginals

Let $(X,Z)$ have density

$$
f(x,z)=2\mathbf1_{\{0<z<x<1\}}.
$$

First complete Exercise 2(1)–(4) in the formal Product Measures TD. Apply parts (1)–(3) to the density above. Part (4) is the separate density-factorization transfer assigned on 24 July; use it only after checking its hypothesis.

1. Verify normalization and compute $f_X$ and $f_Z$ explicitly.
2. For every bounded Borel $\varphi$, identify the identity that yields

   $$
   \mathbb E[\varphi(X)]
   =
   \int_0^1\varphi(x)f_X(x)\,dx.
   $$

3. In the Carnet, record the representations of $f_{X,Z}$ and $f_X$, including their different reference measures and a.e. bases.

## Exercise 3 — Triangular change of variables

On the support of Exercise 2, define

$$
V=X,
\qquad
U=\frac ZX.
$$

1. Prove that $(x,z)\mapsto(v,u)=(x,z/x)$ is a $C^1$-diffeomorphism from $\{0<z<x<1\}$ onto $(0,1)^2$.
2. Compute the inverse and its Jacobian.
3. Determine the joint density of $(V,U)$.
4. Deduce that $U$ and $V$ are independent, identify their laws, and explain the probabilistic meaning of $Z=UX$.

## Exercise 4 — Radon–Nikodym on two spaces

Let $Y\in L^1(\mathbb P)$, $\mathcal G\subseteq\mathcal F$, and let $X:\Omega\to S$ be measurable.

1. Define the signed measure $\nu_Y$ on $(\Omega,\mathcal G)$ and identify its RN derivative.
2. Define the pushed numerator measure $\rho_Y$ on $S$ and identify its RN derivative with respect to $\mu_X$.
3. Prove, for every bounded measurable $\varphi:S\to\mathbb R$, the bounded-test identity

   $$
   \mathbb E[Y\varphi(X)]
   =
   \mathbb E[g_Y(X)\varphi(X)].
   $$

4. Complete the probability-space and state-space rows in the Carnet.
5. For an event $D$, relate $d\mathbb P_D/d\mathbb P$ to $\mathbb P(D)d\mu_D/d\mu_X$. State why they do not live on the same measurable space.

## Exercise 5 — Finite conditioning and variance decomposition

Let $(B_i)_{1\le i\le r}$ be a finite partition with positive probabilities, set $\mathcal G=\sigma(B_1,\ldots,B_r)$, and let $Y\in L^2$.

1. Construct $\mathbb E[Y\mid\sigma(B_1,\ldots,B_r)]$.
2. Prove the tower identity for this finite $\sigma$-field.
3. Show that

   $$
   \mathbb E\!\left[
   (Y-\mathbb E[Y\mid\mathcal G])
   (\mathbb E[Y\mid\mathcal G]-\mathbb E[Y])
   \right]=0.
   $$

4. Deduce the law of total variance and identify where $Y\in L^2$ is used.

## Exercise 6 — Conditional density in the triangular model

Return to Exercise 2.

1. Set $D_X=\{0<f_X<+\infty\}$. Determine $D_X$ and compute

   $$
   k(x,z)=\frac{f(x,z)}{f_X(x)}
   $$

   on $D_X$.
2. Complete $k$ outside $D_X$ using a fixed density $q$ and define $K(x,B)=\int_Bk(x,z)\,dz$.
3. Prove

   $$
   K(X,B)
   =
   \mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)].
   $$

4. Compute $\mathbb E[Z\mid\sigma(X)]$.
5. Complete $U=Z/X$ arbitrarily on $\{X=0\}$ and recover the independence statement of Exercise 3 from the conditional law of $U$ given $X$.

## Exercise 7 — Mixture Bayes

Let $I\in\{0,1\}$ with $\mathbb P(I=1)=p\in(0,1)$. Conditionally on $I=i$, let $X$ be exponential with rate $\lambda_i>0$.

1. Compute the mixture density $f_X$.
2. Determine a Borel version of $\mathbb P(I=1\mid\sigma(X))$.
3. Identify the numerator measure and reference measure behind the posterior density.
4. Compute $\mathbb E[\lambda_I\mid\sigma(X)]$.
5. Explain how the finite Bayes formula and the density formula are the same normalization mechanism in different state spaces.

## Exercise 8 — Actuarial examples

Using the July 2026 official sample-question PDF, and without reproducing the statements, complete the table.

| Question | Hidden random object | Reference measure or conditioning fiber | Required integral／moment |
| --- | --- | --- | --- |
| Q50 |  |  |  |
| Q386 |  |  |  |
| Q370 |  |  |  |
| Q382 |  |  |  |

## Closed-book reconstruction — 60 minutes

Without notes:

1. state Tonelli and Fubini and give the failure example;
2. derive the marginals of the triangular model;
3. perform the $(X,Z)\mapsto(X,Z/X)$ change of variables;
4. write the abstract and state-space RN constructions of conditional expectation;
5. derive total expectation and total variance;
6. construct the triangular conditional kernel, including its null-set completion;
7. reconstruct the five RN representations recorded in the Carnet.
