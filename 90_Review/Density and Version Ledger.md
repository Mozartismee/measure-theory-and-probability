---
type: cross-module-review
module: review
status: canonical
---

# Density and Version Ledger

A density is not identified by its formula alone. Its numerator measure, reference measure, state space and almost-everywhere relation are part of the object.

## 0. Function-space admissibility

Before entering a density row, verify that the intended numerator and tests are integrable in the correct ambient measure.

| Input | Legitimate output | Later use |
| --- | --- | --- |
| $Y\in L^1(\mathbb P)$ | $A\mapsto\mathbb E[Y\mathbf1_A]$ is a finite signed measure | conditional-expectation numerator |
| $Y\in L^1(\mathbb P)$ and $Z\in L^\infty(\mathbb P)$ | $YZ\in L^1(\mathbb P)$ | bounded tests and tower identities |
| $U,V\in L^2(\mathbb P)$ | $UV\in L^1(\mathbb P)$ | covariance and total-variance cross terms |
| $\nu=h\mu$ with $h\ge0$ | $\varphi\in L^1(\nu)$ if and only if $|\varphi|h\in L^1(\mu)$ | change of measure |

On a probability space, $L^\infty\subseteq L^2\subseteq L^1$. This hierarchy supplies admissible inputs; it does not identify a Radon–Nikodym derivative. The latter still requires a numerator measure, a reference measure, an absolute-continuity relation and an almost-everywhere basis.

## 1. Canonical ledger

| Density or representative | Numerator measure | Reference measure | Domain | Uniqueness basis | Deployment |
| --- | --- | --- | --- | --- | --- |
| $f=d\nu/d\mu$ | $\nu$ | $\mu$ | $(E,\mathcal A)$ | $\mu$-a.e. | Radon–Nikodym representation |
| $f=d(f\mu)/d\mu$ | $A\mapsto\int_Af\,d\mu$ | $\mu$ | $(E,\mathcal A)$ | $\mu$-a.e. | density-generated measure |
| $\mathbf1_B/\mathbb P(B)$, for $\mathbb P(B)>0$ | $\mathbb P_B(A)=\mathbb P(A\cap B)/\mathbb P(B)$ | $\mathbb P$ | $(\Omega,\mathcal F)$ | $\mathbb P$-a.s. | conditioning on a positive-probability event |
| $\mathbb E[Y\mid\mathcal G]$, for $Y\in L^1(\mathbb P)$ and a sub-$\sigma$-field $\mathcal G\subseteq\mathcal F$ | $A\mapsto\mathbb E[Y\mathbf1_A]$, $A\in\mathcal G$ | $\mathbb P|_{\mathcal G}$ | $(\Omega,\mathcal G)$ | $\mathbb P$-a.s. | conditional expectation |
| $g_Y=d\rho_Y/d\mu_X$ | $\rho_Y=X_\#(Y\mathbb P)$ for $Y\in L^1(\mathbb P)$ | $\mu_X=X_\#\mathbb P$ | state space of $X$ | $\mu_X$-a.e. | $\mathbb E[Y\mid\sigma(X)]=g_Y(X)$ |
| $g_D=\mathbb P(D)d\mu_D/d\mu_X$, for $\mathbb P(D)>0$ | $B\mapsto\mathbb P(D\cap\{X\in B\})$ | $\mu_X$ | state space of $X$ | $\mu_X$-a.e. | conditional event probability given $X$ |
| $f_X=d\mu_X/d\lambda_d$ | law $\mu_X$ | Lebesgue measure $\lambda_d$ | $\mathbb R^d$ | $\lambda_d$-a.e. | probability density function |
| $f_{X,Z}=d\mu_{X,Z}/d(\lambda_d\otimes\lambda_m)$ | joint law $\mu_{X,Z}$ | $\lambda_d\otimes\lambda_m$ | $\mathbb R^{d+m}$ | product-Lebesgue-a.e. | joint density |
| $f_X(x)=\int f_{X,Z}(x,z)\,dz$ | $(\pi_X)_\#\mu_{X,Z}$ | $\lambda_d$ | $\mathbb R^d$ | $\lambda_d$-a.e. | marginalization by Tonelli |
| $k(x,\cdot)=dK(x,\cdot)/d\lambda_m$ | conditional kernel $K(x,\cdot)$ | $\lambda_m$ | $\mathbb R^m$, for each selected $x$ | the joint law determines the kernel for $\mu_X$-a.e. $x$; for each fixed selected $x$, its density is determined $\lambda_m$-a.e. in $z$ | conditional density in a dominated model |
| $r_i=d(p_i\mu_i)/d\mu_X$ | $A\mapsto\mathbb P(I=i,X\in A)$ | mixture law $\mu_X=\sum_jp_j\mu_j$ | state space of $X$ | $\mu_X$-a.e. | Bayes posterior $\mathbb P(I=i\mid X)$ |

The same algebraic expression may occupy different rows. Equality of formulas does not identify the measures being compared.

## 2. Probability-space and state-space transfer

Let $D\in\mathcal F$ with $\mathbb P(D)>0$ and let $X:\Omega\to S$ be measurable. On the probability space,

$$
\frac{d\mathbb P_D}{d\mathbb P}
=
\frac{\mathbf1_D}{\mathbb P(D)}.
$$

Pushforward by $X$ gives the conditional law $\mu_D=X_\#\mathbb P_D$. On the state space,

$$
\mathbb P(D)
\frac{d\mu_D}{d\mu_X}
=
g_D,
$$

where

$$
g_D(X)
=
\mathbb E[\mathbf1_D\mid\sigma(X)].
$$

The first derivative lives on $\Omega$ and is unique $\mathbb P$-almost surely. The second lives on $S$ and is unique $\mu_X$-almost everywhere. Composition with $X$ transfers the state-space version back to the probability space.

## 3. Conditional expectation as a density

Let $Y\in L^1(\mathbb P)$ and let $\mathcal G\subseteq\mathcal F$ be a sub-$\sigma$-field. Define the finite signed measure

$$
\nu_Y(A)=\mathbb E[Y\mathbf1_A],
\qquad A\in\mathcal G.
$$

Then

$$
\mathbb E[Y\mid\mathcal G]
=
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}.
$$

If $\mathcal G=\sigma(X)$, pushing the numerator measure to the state space gives

$$
\rho_Y(B)
=
\mathbb E[Y\mathbf1_{\{X\in B\}}],
$$

and

$$
\mathbb E[Y\mid\sigma(X)]
=
\left(\frac{d\rho_Y}{d\mu_X}\right)(X).
$$

Thus the abstract and state-space constructions represent the same conditional expectation on different measurable spaces.

## 4. Dominated joint laws

Suppose

$$
\mu_{X,Z}(dx,dz)=f_{X,Z}(x,z)\,dx\,dz.
$$

Tonelli first produces

$$
f_X(x)=\int f_{X,Z}(x,z)\,dz.
$$

On

$$
D_X=\{0<f_X<+\infty\},
$$

normalization gives

$$
k(x,z)=\frac{f_{X,Z}(x,z)}{f_X(x)}.
$$

The complement $D_X^c$ is $\mu_X$-null. A fixed auxiliary probability density completes $k$ there and produces an everywhere-defined kernel. The completion is a version choice, not information recovered from the joint law.

## 5. Version audit

For every density statement, record:

1. the numerator measure;
2. the reference measure;
3. the measurable space on which both live;
4. the measure defining the almost-everywhere relation;
5. whether the density is later composed with a random variable;
6. the set on which a ratio is defined;
7. any arbitrary completion on a null set.

An expression such as $f_{X,Z}/f_X$ without items 2, 4 and 6 is not yet a conditional density. It is a fraction awaiting jurisdiction.

## 6. Reconstruction

Without consultation, reconstruct the following transfers and fill one ledger row for every arrow:

$$
Y\mathbb P
\longrightarrow
X_\#(Y\mathbb P)
\longrightarrow
\frac{dX_\#(Y\mathbb P)}{dX_\#\mathbb P}
\longrightarrow
\mathbb E[Y\mid\sigma(X)],
$$

and

$$
f_{X,Z}
\longrightarrow
f_X
\longrightarrow
k(x,z)
\longrightarrow
K(X,\cdot).
$$
