---
type: cours
module: conditional-laws
status: canonical
---

# Cours — Conditional Laws as State-Space Representations

This module depends on [[30_Pushforwards-and-Laws/Cours|Pushforwards and Laws]] and [[40_Conditional-Expectation/Cours|Conditional Expectation]].

## 1. State-space representation

Let $(S,\mathcal S)$ be a measurable space and let

$$
X:(\Omega,\mathcal F)
\longrightarrow
(S,\mathcal S)
$$

be measurable. Set

$$
\mu_X=X_\#\mathbb P.
$$

For every nonnegative measurable $\varphi$,

$$
\int_\Omega\varphi(X)\,d\mathbb P
=
\int_S\varphi\,d\mu_X.
$$

Consequently,

$$
T:L^1(\mu_X)\longrightarrow L^1(\mathbb P),
\qquad
Tg=g(X),
$$

is a linear isometry.

For arbitrary measurable $g,h:S\to\overline{\mathbb R}$,

$$
g=h
\quad\mu_X\text{-almost everywhere}
\quad\Longleftrightarrow\quad
g(X)=h(X)
\quad\mathbb P\text{-almost surely},
$$

since

$$
\mathbb P(g(X)\ne h(X))
=
\mu_X(\{g\ne h\}).
$$

## 2. Conditional expectation given a random variable

Let $Y\in L^1_+(\mathbb P)$ and define

$$
\eta_Y(A)
=
\mathbb E[Y\mathbf1_A],
\qquad A\in\mathcal F.
$$

Push this measure to the state space:

$$
\rho_Y=X_\#\eta_Y.
$$

Thus

$$
\rho_Y(B)
=
\mathbb E\!\left[
Y\mathbf1_{\{X\in B\}}
\right],
\qquad B\in\mathcal S.
$$

Then $\rho_Y$ is finite and

$$
\rho_Y\ll\mu_X.
$$

Let

$$
g_Y
=
\frac{d\rho_Y}{d\mu_X}.
$$

For every nonnegative measurable $\varphi:S\to[0,+\infty]$,

$$
\mathbb E[Y\varphi(X)]
=
\int_S\varphi g_Y\,d\mu_X
=
\mathbb E[\varphi(X)g_Y(X)].
$$

Therefore

$$
\boxed{
\mathbb E[Y\mid\sigma(X)]
=
g_Y(X)
}.
$$

The construction extends to $Y\in L^1(\mathbb P)$ by positive and negative parts.

## 3. Conditional event laws

Let $D\in\mathcal F$ with $\mathbb P(D)>0$. Define

$$
\mathbb P_D(A)
=
\frac{\mathbb P(A\cap D)}{\mathbb P(D)}
$$

and

$$
\mu_D=X_\#\mathbb P_D.
$$

Set

$$
g_D
=
\frac{d\rho_{\mathbf1_D}}{d\mu_X}.
$$

Then one may choose $0\le g_D\le1$ and

$$
g_D(X)
=
\mathbb E[\mathbf1_D\mid\sigma(X)].
$$

Moreover,

$$
\rho_{\mathbf1_D}
=
\mathbb P(D)\mu_D,
$$

hence

$$
\boxed{
\mathbb P(D)
\frac{d\mu_D}{d\mu_X}
=
g_D
}.
$$

The following equivalences hold:

$$
D\text{ is independent of }\sigma(X)
\quad\Longleftrightarrow\quad
g_D=\mathbb P(D)
\quad\mu_X\text{-a.e.},
$$

and

$$
D\in\sigma(X)
\quad\text{modulo null sets}
\quad\Longleftrightarrow\quad
g_D\in\{0,1\}
\quad\mu_X\text{-a.e.}
$$

## 4. Version discipline

The objects on the state space and the probability space are compared in [[10_Foundations/Version Discipline|Version Discipline]].

## 5. Boundary

For each fixed event $D$, the function $g_D$ represents the conditional probability of $D$ given $X$.

This does not by itself construct a regular conditional law

$$
x\longmapsto K(x,\cdot).
$$

Joint measurability in the state variable and the event variable belongs to the theory of Markov kernels and disintegration. It requires additional hypotheses, typically standard Borel state spaces, and is not part of the present module.

## 6. Reconstruction

### Conditioning given $X$

$$
Y
\longmapsto
\eta_Y
\longmapsto
\rho_Y=X_\#\eta_Y
\longmapsto
g_Y=\frac{d\rho_Y}{d\mu_X}
\longmapsto
g_Y(X).
$$

### Conditional event law

$$
D
\longmapsto
\mathbb P_D
\longmapsto
\mu_D=X_\#\mathbb P_D
\longmapsto
\mathbb P(D)\frac{d\mu_D}{d\mu_X}
=
g_D.
$$

### Semantic closure

$$
\boxed{
\text{conditional expectation}
=
\text{Radon–Nikodym representation on the observed }\sigma\text{-field}
}
$$

and

$$
\boxed{
\mathbb E[Y\mid\sigma(X)]
=
\left(
\frac{d\,X_\#(Y\mathbb P)}{d\,X_\#\mathbb P}
\right)(X)
}
$$

for $Y\ge0$, with extension to $L^1$ by positive and negative parts.
