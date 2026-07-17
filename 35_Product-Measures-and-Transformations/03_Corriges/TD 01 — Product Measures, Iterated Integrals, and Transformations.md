---
type: corrige
module: product-measures-and-transformations
status: canonical
corresponds-to: TD 01 — Product Measures, Iterated Integrals, and Transformations
---

# Corrigé — TD 01: Product Measures, Iterated Integrals, and Transformations

## Exercise A

For fixed $x\in E$, let

$$
\mathcal C_x
=
\{C\in\mathcal A\otimes\mathcal B:C_x\in\mathcal B\}.
$$

Sections commute with complements and countable unions, so $\mathcal C_x$ is a $\sigma$-field. It contains every measurable rectangle because

$$
(A\times B)_x
=
\begin{cases}
B,&x\in A,\\
\varnothing,&x\notin A.
\end{cases}
$$

Hence $\mathcal C_x=\mathcal A\otimes\mathcal B$. The proof for $C^y$ is symmetric.

Assume now that $\mu(E)$ and $\nu(F)$ are finite. Let $\mathcal D$ be the class of $C\in\mathcal A\otimes\mathcal B$ such that $x\mapsto\nu(C_x)$ is measurable and

$$
(\mu\otimes\nu)(C)
=
\int_E\nu(C_x)\,\mu(dx).
$$

For a rectangle $A\times B$,

$$
\nu((A\times B)_x)=\mathbf1_A(x)\nu(B),
$$

so measurable rectangles belong to $\mathcal D$. If $C\in\mathcal D$, finiteness gives

$$
\nu((C^c)_x)=\nu(F)-\nu(C_x)
$$

and

$$
\int_E\nu((C^c)_x)\,\mu(dx)
=
\mu(E)\nu(F)-(\mu\otimes\nu)(C)
=
(\mu\otimes\nu)(C^c).
$$

Thus $C^c\in\mathcal D$. If $(C_n)$ is disjoint in $\mathcal D$, then

$$
\nu\!\left(\left(\bigcup_nC_n\right)_x\right)
=
\sum_n\nu((C_n)_x).
$$

Monotone convergence and countable additivity show that $\bigcup_nC_n\in\mathcal D$. Therefore $\mathcal D$ is a Dynkin system containing the generating $\pi$-system of measurable rectangles. The $\pi$-$\lambda$ theorem gives $\mathcal D=\mathcal A\otimes\mathcal B$.

For the $\sigma$-finite case, take increasing exhaustions $E_n\uparrow E$ and $F_n\uparrow F$ of finite measure. By uniqueness on measurable rectangles, the product of the restricted measures is the restriction of $\mu\otimes\nu$ to $E_n\times F_n$. Applying the finite result yields

$$
\int_E
\mathbf1_{E_n}(x)\nu(C_x\cap F_n)\,\mu(dx)
=
(\mu\otimes\nu)\bigl(C\cap(E_n\times F_n)\bigr).
$$

The left-hand integrands increase to $\nu(C_x)$, and the sets on the right increase to $C$. Hence

$$
(\mu\otimes\nu)(C)
=
\int_E\nu(C_x)\,\mu(dx).
$$

The same argument with the variables exchanged gives

$$
(\mu\otimes\nu)(C)
=
\int_F\mu(C^y)\,\nu(dy).
$$

If $s=\sum_{j=1}^ra_j\mathbf1_{C_j}$ is a nonnegative simple function, linearity of the indicator identities gives

$$
\int_{E\times F}s\,d(\mu\otimes\nu)
=
\int_E\left(\int_Fs(x,y)\,\nu(dy)\right)\mu(dx),
$$

and symmetrically in the other order. Finally, for measurable $f\ge0$, choose simple functions $s_n\uparrow f$. Monotone convergence applies to the product integral, to every section integral and to both outer integrals. This proves Tonelli's theorem, with all integrals allowed to equal $+\infty$.

## Exercise 0

For fixed $m$,

$$
\sum_{n\ge1}a(m,n)=1-1=0,
$$

hence

$$
\sum_{m\ge1}\sum_{n\ge1}a(m,n)=0.
$$

For fixed $n$, one has

$$
\sum_{m\ge1}a(m,1)=1,
$$

whereas, for $n\ge2$, the positive term at $m=n$ and the negative term at $m=n-1$ cancel. Therefore

$$
\sum_{n\ge1}\sum_{m\ge1}a(m,n)=1.
$$

Moreover, every row contains two nonzero terms of absolute value one, so

$$
\sum_{m,n\ge1}|a(m,n)|=+\infty.
$$

The function is signed, so Tonelli does not apply to $a$; it is not integrable, so Fubini does not apply either.

## Exercise 1

The map $(x,t)\mapsto f(x)-t$ is measurable as an extended-real comparison map, and

$$
H_f=\{(x,t):f(x)-t>0\}
$$

is measurable. Equivalently, one may verify the claim first for simple $f$ and pass to an increasing simple approximation.

For every $x$,

$$
\int_0^\infty\mathbf1_{H_f}(x,t)\,dt=f(x).
$$

Tonelli gives

$$
\int_Ef\,d\mu
=
\int_0^\infty\left(\int_E\mathbf1_{\{f>t\}}\,d\mu\right)dt
=
\int_0^\infty\mu(f>t)\,dt.
$$

Applying the same identity to $f^p$ and substituting $s=t^p$ yields

$$
\int_Ef^p\,d\mu
=
p\int_0^\infty t^{p-1}\mu(f>t)\,dt.
$$

For $0<q<p$, split the integral at $1$:

$$
\int_Ef^q\,d\mu
\le
q\mu(E)\int_0^1t^{q-1}\,dt
+
qC\int_1^\infty t^{q-p-1}\,dt
<+\infty.
$$

The endpoint need not hold. On $E=(0,1)$ with Lebesgue measure, let $f(x)=x^{-1/p}$. Then $\lambda(f>t)\le t^{-p}$ for $t\ge1$, but

$$
\int_0^1f(x)^p\,dx=\int_0^1\frac{dx}{x}=+\infty.
$$

## Exercise 2

Tonelli gives the measurability of $f_X,f_Y$ and

$$
\int_{\mathbb R^d}f_X(x)\,dx
=
\int_{\mathbb R^{d+m}}f(x,y)\,dx\,dy
=1,
$$

with the analogous identity for $f_Y$.

For a Borel set $A\subseteq\mathbb R^d$,

$$
(\pi_X)_\#\mu(A)
=
\mu(A\times\mathbb R^m)
=
\int_A\int_{\mathbb R^m}f(x,y)\,dy\,dx
=
\int_Af_X(x)\,dx.
$$

This proves the first pushforward identity; the second is symmetric. Applying Tonelli to $(x,y)\mapsto\varphi(x)f(x,y)$ gives the test-function identity.

If $f=f_Xf_Y$ almost everywhere, then for Borel $A,B$,

$$
\mu(A\times B)
=
\int_Af_X(x)\,dx\int_Bf_Y(y)\,dy
=
\mu_X(A)\mu_Y(B).
$$

The measurable rectangles form a generating $\pi$-system, so the joint law equals $\mu_X\otimes\mu_Y$ and the coordinates are independent.

## Exercise 3

The inverse map is

$$
T^{-1}(s,u)=(su,s(1-u)).
$$

Its derivative has determinant

$$
\det
\begin{pmatrix}
u&s\\
1-u&-s
\end{pmatrix}
=-s,
$$

so $|\det DT^{-1}(s,u)|=s$. The change of variables gives

$$
\begin{aligned}
\Gamma(a)\Gamma(b)
&=
\int_0^\infty\int_0^\infty
x^{a-1}y^{b-1}e^{-(x+y)}\,dx\,dy\\
&=
\int_0^\infty\int_0^1
s^{a+b-1}e^{-s}u^{a-1}(1-u)^{b-1}\,du\,ds.
\end{aligned}
$$

The integrand is nonnegative, so Tonelli factors the last integral:

$$
\Gamma(a)\Gamma(b)
=
\Gamma(a+b)
\int_0^1u^{a-1}(1-u)^{b-1}\,du.
$$

Change of variables produces the Jacobian and the separated integrand; Tonelli authorizes the separation and exchange of the nonnegative integrals.

## Exercise 4

1. Tonelli applies because $h$ is measurable and nonnegative; finiteness is not required.
2. Tonelli applied to $|h|$ proves almost-everywhere section integrability; Fubini then applies because $h\in L^1(\mu\otimes\nu)$.
3. The subgraph indicator is nonnegative, so Tonelli yields the tail formula, possibly with value $+\infty$.
4. The marginal law is the pushforward by a coordinate projection, and Tonelli integrates the joint density along the discarded coordinate.
5. Marginalization determines identities only for $f_X(x)\,dx$-almost every $x$. On $\{f_X=0\}$, division by $f_X$ is undefined and the joint law imposes no conditional value. A version must be chosen separately.
