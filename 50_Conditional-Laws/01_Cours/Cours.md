---
type: cours
module: conditional-laws
status: canonical
---

# Cours — Conditional Laws as State-Space Representations

This module depends on [Pushforwards and Laws](../../30_Pushforwards-and-Laws/01_Cours/Cours.md), [Product Measures and Transformations](../../35_Product-Measures-and-Transformations/01_Cours/Cours.md), and [Conditional Expectation](../../40_Conditional-Expectation/01_Cours/Cours.md).

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space.

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

## 4. Dominated conditional densities

Let

$$
X:\Omega\to\mathbb R^d,
\qquad
Z:\Omega\to\mathbb R^m
$$

be random vectors. Assume that the joint law has a Lebesgue density:

$$
\mu_{X,Z}(dx,dz)
=
f_{X,Z}(x,z)\,dx\,dz.
$$

Define the marginal density

$$
f_X(x)
=
\int_{\mathbb R^m}f_{X,Z}(x,z)\,dz
$$

and the set

$$
D_X=\{x\in\mathbb R^d:0<f_X(x)<+\infty\}.
$$

Since $f_X$ is an integrable density,

$$
\mu_X(D_X^c)=0.
$$

Fix once and for all a probability density $q$ on $\mathbb R^m$, for example the standard Gaussian density, and set

$$
k(x,z)
=
\begin{cases}
\dfrac{f_{X,Z}(x,z)}{f_X(x)},&x\in D_X,\\[1.1ex]
q(z),&x\notin D_X.
\end{cases}
$$

The function $k$ is jointly measurable and

$$
\int_{\mathbb R^m}k(x,z)\,dz=1
$$

for every $x\in\mathbb R^d$. Consequently,

$$
K(x,B)
=
\int_Bk(x,z)\,dz,
\qquad B\in\mathcal B(\mathbb R^m),
$$

defines a probability kernel from $\mathbb R^d$ to $\mathbb R^m$: $B\mapsto K(x,B)$ is a probability measure for every $x$, and $x\mapsto K(x,B)$ is Borel measurable for every Borel $B$.

### Theorem 4.1 — Identification of the kernel

For every Borel set $B\subseteq\mathbb R^m$,

$$
\boxed{
K(X,B)
=
\mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)]
}
\qquad\mathbb P\text{-almost surely}.
$$

### Proof

Let $A\in\mathcal B(\mathbb R^d)$. Since $\mu_X(D_X^c)=0$, Tonelli gives

$$
\begin{aligned}
\mathbb E[\mathbf1_{\{X\in A\}}K(X,B)]
&=
\int_{A\cap D_X}K(x,B)f_X(x)\,dx\\
&=
\int_{A\cap D_X}\int_Bf_{X,Z}(x,z)\,dz\,dx\\
&=
\mathbb P(X\in A,Z\in B).
\end{aligned}
$$

The candidate $K(X,B)$ is $\sigma(X)$-measurable and satisfies the defining integral identities. Conditional-expectation uniqueness concludes.

### Corollary 4.2 — Conditional integration

Let $h:\mathbb R^m\to\overline{\mathbb R}$ be measurable. If $h\ge0$, set

$$
G_h(x)=\int_{\mathbb R^m}h(z)k(x,z)\,dz
\in[0,+\infty].
$$

If instead $h(Z)\in L^1(\mathbb P)$, let

$$
A_h
=
\left\{x:\int_{\mathbb R^m}|h(z)|k(x,z)\,dz<+\infty\right\}.
$$

Then $\mu_X(A_h^c)=0$. Define $G_h(x)=\int h(z)k(x,z)\,dz$ on $A_h$ and, for example, $G_h(x)=0$ on $A_h^c$. In the corresponding nonnegative or integrable regime,

$$
\boxed{
\mathbb E[h(Z)\mid\sigma(X)]
=
G_h(X)
}.
$$

For $h\ge0$, this follows first for indicators, then for simple functions, and finally by monotone convergence. In the signed case, conditional integration applied to $|h|$ gives $\mu_X(A_h^c)=0$; positive and negative parts may then be subtracted on $A_h$ without creating $+\infty-+\infty$.

The ratio

$$
f_{Z\mid X=x}(z)
=
\frac{f_{X,Z}(x,z)}{f_X(x)}
$$

is therefore legitimate on $D_X$. Outside $D_X$, the joint law does not determine a conditional value; the chosen density $q$ completes one everywhere-defined version of the kernel.

## 5. Version discipline

The objects on the state space and the probability space are compared in [Version Discipline](../../15_Lp-Interface/06_Supplements/Version%20Discipline.md).

Different versions of $f_{X,Z}$ or different choices of $q$ may produce different pointwise kernels. Tonelli shows that the resulting kernels agree outside one $\mu_X$-null set, hence give the same random variables after composition with $X$.

## 6. Boundary

For each fixed event $D$, the function $g_D$ represents the conditional probability of $D$ given $X$.

The dominated construction of Section 4 produces a kernel because one jointly measurable density $k(x,z)$ simultaneously defines

$$
B\longmapsto K(x,B)=\int_Bk(x,z)\,dz
$$

for all Borel sets $B$. By contrast, choosing one Radon–Nikodym representative of

$$
\mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)]
$$

separately for every $B$ does not provide a common exceptional set, countable additivity in $B$, or joint measurability. Thus the eventwise construction of Section 3 does not by itself produce a probability kernel.

For a general random element

$$
Z:(\Omega,\mathcal F)\longrightarrow(T,\mathcal T),
$$

a regular conditional law of $Z$ given $X$ would require one simultaneous choice

$$
K:S\times\mathcal T\longrightarrow[0,1]
$$

with, for every $B\in\mathcal T$,

$$
K(X,B)
=
\mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)]
\qquad\mathbb P\text{-a.s.},
$$

such that $x\mapsto K(x,B)$ is $\mathcal S$-measurable for every $B\in\mathcal T$, while $B\mapsto K(x,B)$ is a probability measure for every $x$. The dominated Euclidean construction above supplies such a kernel. General existence and disintegration require additional hypotheses, typically standard Borel structure, and remain outside this module.

## 7. Reconstruction

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

### Dominated conditional density

$$
f_{X,Z}
\xrightarrow{\text{Tonelli}}
f_X
\xrightarrow{\text{normalize on }D_X}
k
\xrightarrow{\text{test identities}}
K(X,\cdot).
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

for $Y\in L^1(\mathbb P)$, where $Y\mathbb P$ is a finite signed measure and the derivative is obtained from the signed Radon–Nikodym corollary.
