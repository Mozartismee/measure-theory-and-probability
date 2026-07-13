# TD 1 — Conditional Expectation as a Radon–Nikodym Derivative

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $\mathcal G\subset\mathcal F$ be a sub-$\sigma$-field.

The positive Radon–Nikodym theorem for finite measures may be used.

## Exercise 1 — Construction on a sub-$\sigma$-field

*[Supplementary construction]*

Let $Y\in L^1_+(\mathbb P)$ and define, on $(\Omega,\mathcal G)$,

$$
\nu_Y(A)
=
\mathbb E[Y\mathbf1_A],
\qquad A\in\mathcal G.
$$

1. Prove that $\nu_Y$ is a finite positive measure and that

   $$
   \nu_Y\ll\mathbb P|_{\mathcal G}.
   $$

   Let

   $$
   Z_Y
   =
   \frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}.
   $$

   Prove that $Z_Y\in L^1_+(\mathbb P)$ and identify it as a conditional expectation.

2. Extend the construction to every $Y\in L^1(\mathbb P)$ by applying it to $Y^+$ and $Y^-$. Prove that the resulting random variable is independent, up to $\mathbb P$-almost sure equality, of the chosen decomposition of $Y$ as a difference of two integrable nonnegative random variables.

3. Establish the equivalence

   $$
   Z=\mathbb E[Y\mid\mathcal G]
   $$

   if and only if $Z$ is $\mathcal G$-measurable, integrable, and

   $$
   \mathbb E[HY]
   =
   \mathbb E[HZ]
   $$

   for every bounded $\mathcal G$-measurable random variable $H$.

4. Prove directly from this characterization that

   $$
   \left\|
   \mathbb E[Y\mid\mathcal G]
   \right\|_{L^1}
   \le
   \|Y\|_{L^1}.
   $$

## Exercise 2 — Identification on a generating class

*[Adapted from ENS]*

Let $Y,Z\in L^1(\mathbb P)$, with $Z$ $\mathcal G$-measurable. Let $\Pi\subset\mathcal G$ contain $\Omega$, be stable under finite intersections, and satisfy

$$
\sigma(\Pi)=\mathcal G.
$$

Assume that

$$
\mathbb E[Y\mathbf1_A]
=
\mathbb E[Z\mathbf1_A],
\qquad A\in\Pi.
$$

Prove that

$$
Z=\mathbb E[Y\mid\mathcal G]
\qquad\mathbb P\text{-almost surely}.
$$

The argument must identify the class of sets on which the integral identity holds and close it by a monotone-class or $\pi$-$\lambda$ theorem.

Source: ENS Paris, *Processus aléatoires*, TD 5, Exercise 8, 2018–2019.

## Exercise 3 — Calculus by uniqueness

*[Supplementary construction]*

Let $Y,Y_1,Y_2\in L^1(\mathbb P)$ and let $\mathcal H\subset\mathcal G$.

Derive the following assertions solely from the defining integral identity and uniqueness.

1. If $Y$ is $\mathcal G$-measurable, then

   $$
   \mathbb E[Y\mid\mathcal G]=Y.
   $$

   If $Y$ is independent of $\mathcal G$, then

   $$
   \mathbb E[Y\mid\mathcal G]=\mathbb E[Y].
   $$

2. If $H$ is bounded and $\mathcal G$-measurable, prove

   $$
   \mathbb E[HY\mid\mathcal G]
   =
   H\mathbb E[Y\mid\mathcal G].
   $$

3. Prove the tower identities

   $$
   \mathbb E\!\left[
   \mathbb E[Y\mid\mathcal G]
   \mid\mathcal H
   \right]
   =
   \mathbb E[Y\mid\mathcal H]
   $$

   and

   $$
   \mathbb E\!\left[
   \mathbb E[Y\mid\mathcal H]
   \mid\mathcal G
   \right]
   =
   \mathbb E[Y\mid\mathcal H].
   $$

4. Prove linearity, positivity and monotonicity of

   $$
   Y\longmapsto\mathbb E[Y\mid\mathcal G].
   $$

## Reconstruction

Without consulting the Cours, reconstruct the existence and uniqueness of

$$
\mathbb E[Y\mid\mathcal G]
$$

for arbitrary $Y\in L^1(\mathbb P)$.

The following objects must arise from the argument:

$$
\nu_{Y^+},
\qquad
\nu_{Y^-},
\qquad
\frac{d\nu_{Y^+}}{d(\mathbb P|_{\mathcal G})},
\qquad
\frac{d\nu_{Y^-}}{d(\mathbb P|_{\mathcal G})}.
$$

Close the reconstruction by proving one tower identity from the defining integral relation alone.