---
type: td
module: conditional-laws
status: canonical
solutions-policy: attempt-before-corrige
---

# TD 02 — Dominated Conditional Densities

The product-measure Cours and the abstract characterization of conditional expectation may be used. Every division by a marginal density must specify its domain. Every equality of densities must specify its almost-everywhere reference measure.

## Exercise 1 — Constructing a common kernel

Let $(X,Z)$ be an $\mathbb R^d\times\mathbb R^m$-valued random vector with joint density $f$ with respect to $\lambda_d\otimes\lambda_m$. Define

$$
f_X(x)=\int_{\mathbb R^m}f(x,z)\,dz,
\qquad
D_X=\{0<f_X<+\infty\}.
$$

Fix a probability density $q$ on $\mathbb R^m$ and define, piecewise,

$$
k(x,z)
=
\begin{cases}
\dfrac{f(x,z)}{f_X(x)},&x\in D_X,\\[1ex]
q(z),&x\notin D_X.
\end{cases}
$$

1. Prove that $f_X$ and $k$ are measurable and that $\mu_X(D_X^c)=0$.
2. Prove that $k(x,\cdot)$ is a probability density for every $x$.
3. Define $K(x,B)=\int_Bk(x,z)\,dz$. Prove both defining measurability properties of a probability kernel.
4. For Borel sets $A\subseteq\mathbb R^d$ and $B\subseteq\mathbb R^m$, prove

   $$
   \int_AK(x,B)\,\mu_X(dx)
   =
   \mathbb P(X\in A,Z\in B).
   $$

5. Deduce that

   $$
   K(X,B)
   =
   \mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)]
   \qquad\mathbb P\text{-a.s.}
   $$

6. Extend the result to $h(Z)$ for nonnegative measurable $h$. For signed $h$ with $h(Z)\in L^1$, identify the $\mu_X$-null set on which $\int |h(z)|k(x,z)\,dz$ may be infinite and make an explicit version choice there before subtracting positive and negative parts.

## Exercise 2 — A triangular law

Let $(X,Z)$ have joint density

$$
f(x,z)=2\mathbf1_{\{0<z<x<1\}}.
$$

1. Verify that $f$ is a probability density and determine $f_X$ and $f_Z$.
2. Construct an everywhere-defined conditional density $k(x,z)$ of $Z$ given $X=x$.
3. Define a Borel function $m$ on the state space by $m(x)=x/2$ for $x\in(0,1)$ and make an explicit choice outside $(0,1)$. Prove the almost-sure identity

   $$
   \mathbb E[Z\mid\sigma(X)]=m(X)=\frac X2
   \qquad\mathbb P\text{-a.s.}
   $$

4. For $a\in(0,1)$, determine a Borel function $g_a$ such that

   $$
   g_a(X)
   =
   \mathbb P(Z\le a\mid\sigma(X))
   \qquad\mathbb P\text{-a.s.}
   $$

5. Explain why the value assigned at $x=0$ is mathematically necessary for an everywhere-defined kernel but probabilistically invisible after composition with $X$.

## Exercise 3 — Bayes as a state-space density ratio

Let $I$ take values in $\{1,\ldots,r\}$ with $\mathbb P(I=i)=p_i>0$. Assume that, conditionally on $I=i$, the random vector $X\in\mathbb R^d$ has density $f_i$. Set

$$
f_X(x)=\sum_{j=1}^rp_jf_j(x).
$$

1. Prove that $f_X$ is the density of $X$.
2. For each $i$, construct a Borel version of

   $$
   \mathbb P(I=i\mid\sigma(X)).
   $$

3. Prove that on $D_X=\{0<f_X<+\infty\}$ one may take

   $$
   \mathbb P(I=i\mid X=x)
   =
   \frac{p_if_i(x)}{\sum_jp_jf_j(x)}.
   $$

4. If $c_1,\ldots,c_r\in\mathbb R$, determine $\mathbb E[c_I\mid\sigma(X)]$.
5. Identify the numerator measure, reference measure, density, and almost-everywhere relation in the preceding formula.

## Exercise 4 — Boundary audit

1. Explain why choosing, for every Borel $B$, one representative of

   $$
   \mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)]
   $$

   does not by itself produce a probability kernel.
2. Identify the additional structure supplied by the joint density $k(x,z)$ in Exercise 1.
3. Give two distinct choices of the auxiliary density $q$ on $D_X^c$ and prove that the resulting conditional expectations agree almost surely after composition with $X$.
4. State exactly which part of this TD would fail if only the marginal densities $f_X$ and $f_Z$ were known.

## Reconstruction

Without notes, recover

$$
f_{X,Z}
\longmapsto
f_X
\longmapsto
k(x,z)
\longmapsto
K(x,B)
\longmapsto
K(X,B),
$$

and assign one theorem or verification responsibility to each arrow.
