---
type: corrige
module: conditional-laws
status: canonical
corresponds-to: TD 02 — Dominated Conditional Densities
---

# Corrigé — TD 02: Dominated Conditional Densities

## Exercise 1

Tonelli gives the measurability of

$$
f_X(x)=\int f(x,z)\,dz.
$$

Since $f_X$ is integrable, it is finite $\lambda_d$-almost everywhere. Moreover, $\mu_X$ has density $f_X$, so both $\{f_X=0\}$ and the $\lambda_d$-null set $\{f_X=+\infty\}$ are $\mu_X$-null. Hence $\mu_X(D_X^c)=0$.

The function $k$ is measurable. For $x\in D_X$,

$$
\int k(x,z)\,dz
=
\frac1{f_X(x)}\int f(x,z)\,dz
=1,
$$

and for $x\notin D_X$ the same conclusion follows from the choice of $q$.

For fixed $x$, $B\mapsto K(x,B)$ is the probability measure with density $k(x,\cdot)$. For fixed Borel $B$, Tonelli applied to $\mathbf1_B(z)k(x,z)$ proves that $x\mapsto K(x,B)$ is measurable.

For Borel $A,B$, using $\mu_X(D_X^c)=0$,

$$
\begin{aligned}
\int_AK(x,B)\,\mu_X(dx)
&=
\int_{A\cap D_X}\int_Bk(x,z)\,dz\,f_X(x)\,dx\\
&=
\int_A\int_Bf(x,z)\,dz\,dx\\
&=
\mathbb P(X\in A,Z\in B).
\end{aligned}
$$

Thus $K(X,B)$ is $\sigma(X)$-measurable and satisfies the defining identities of the conditional expectation of $\mathbf1_{\{Z\in B\}}$. Indicators extend to nonnegative simple functions by linearity and to nonnegative $h$ by monotone convergence.

If $h(Z)\in L^1$, set

$$
H(x)=\int |h(z)|k(x,z)\,dz.
$$

The nonnegative result gives $\int H\,d\mu_X=\mathbb E[|h(Z)|]<+\infty$, so $A_h=\{H<+\infty\}$ has full $\mu_X$-measure. On $A_h$ define $G_h(x)=\int h(z)k(x,z)\,dz$; set $G_h=0$ on $A_h^c$. Positive and negative parts may now be subtracted without an undefined $+\infty-+\infty$, and $G_h(X)$ is the desired conditional expectation.

## Exercise 2

One has

$$
\int_0^1\int_0^x2\,dz\,dx
=
\int_0^12x\,dx
=1.
$$

The marginal densities are

$$
f_X(x)=2x\mathbf1_{(0,1)}(x),
$$

and

$$
f_Z(z)=2(1-z)\mathbf1_{(0,1)}(z).
$$

For $x\in(0,1)$,

$$
k(x,z)=\frac1x\mathbf1_{(0,x)}(z).
$$

Outside $(0,1)$ choose, for definiteness, the standard Gaussian density $q$. Then

$$
\int z k(x,z)\,dz
=
\frac1x\int_0^xz\,dz
=
\frac x2.
$$

Define

$$
m(x)=
\begin{cases}
x/2,&x\in(0,1),\\
0,&x\notin(0,1).
\end{cases}
$$

The chosen $q$ has mean zero, so $m(x)=\int z k(x,z)\,dz$ for every $x$ and

$$
\mathbb E[Z\mid\sigma(X)]
=m(X)
=\frac X2
\qquad\mathbb P\text{-almost surely}.
$$

For $a\in(0,1)$, a version is

$$
g_a(x)
=
\begin{cases}
1,&0<x\le a,\\
a/x,&a<x<1,\\
\int_{(-\infty,a]}q(z)\,dz,&x\notin(0,1).
\end{cases}
$$

The law of $X$ assigns zero mass to the last region, including $x=0$; the chosen value is required only to make the kernel pointwise complete.

## Exercise 3

For every Borel $A\subseteq\mathbb R^d$,

$$
\mathbb P(X\in A)
=
\sum_i p_i\int_Af_i(x)\,dx
=
\int_A\sum_ip_if_i(x)\,dx.
$$

Thus $f_X=\sum_ip_if_i$. Let $D_X=\{0<f_X<+\infty\}$. Since $f_X$ is an integrable density, $\mu_X(D_X^c)=0$. Define

$$
r_i(x)
=
\begin{cases}
\dfrac{p_if_i(x)}{f_X(x)},&x\in D_X,\\[1ex]
p_i,&x\notin D_X.
\end{cases}
$$

Then, for every Borel $A$,

$$
\int_Ar_i(x)f_X(x)\,dx
=
p_i\int_Af_i(x)\,dx
=
\mathbb P(I=i,X\in A).
$$

Therefore $r_i(X)=\mathbb P(I=i\mid\sigma(X))$ almost surely. By linearity,

$$
\mathbb E[c_I\mid\sigma(X)]
=
\sum_ic_ir_i(X).
$$

The numerator measure is

$$
A\longmapsto\mathbb P(I=i,X\in A)=p_i\mu_i(A),
$$

the reference measure is $\mu_X$, the density is $r_i$, and uniqueness is $\mu_X$-almost everywhere.

## Exercise 4

Conditional-expectation representatives chosen separately for uncountably many Borel sets may have different exceptional sets. Such choices need not preserve countable additivity in $B$ for any fixed $x$. The joint function $k(x,z)$ supplies one common measurable object; integration in $z$ then gives countable additivity and normalization simultaneously.

If $q_1,q_2$ are two auxiliary densities, the corresponding kernels agree on $D_X$. Since $\mu_X(D_X^c)=0$, their compositions with $X$ agree almost surely for every fixed Borel event and every admissible test function.

Marginal densities alone do not determine the dependence structure. They therefore do not determine $f_{X,Z}$, $k$, or any conditional law.

## Reconstruction

Tonelli constructs $f_X$; normalization on $D_X$ constructs $k$; parameter integration constructs the kernel $K$; the defining test identities identify $K(X,B)$ by conditional-expectation uniqueness.
