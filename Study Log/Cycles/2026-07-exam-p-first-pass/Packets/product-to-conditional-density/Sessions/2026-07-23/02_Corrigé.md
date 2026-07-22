---
type: study-session-corrige
date: 2026-07-23
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
session: J4c
solutions-policy: attempt-before-corrige
math-authority: derived
canonical-sources:
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../../../30_Pushforwards-and-Laws/02_TD/TD 03 — Atomic Laws, Counting Models, and Structural Failures.md
  - ../../../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../../../80_Lemmas/Dynkin Systems and the Pi-Lambda Transfer Principle.md
---

# Corrigé — Feuille J4c

This corrigé is independent of the working sheet. It is to be opened only after both complete written attempts and the Bilan have been fixed.

## Problème I — De la mesure produit à l'indépendance

### 1. Sections and the indicator identity

Define

$$
\mathfrak S
:=
\left\{
C\subseteq E\times F:
C_x\in\mathcal B\text{ for every }x,
\quad
C^y\in\mathcal A\text{ for every }y
\right\}.
$$

Sections commute with complements and countable unions:

$$
(C^c)_x=F\setminus C_x,
\qquad
\left(\bigcup_{n\ge1}C_n\right)_x
=
\bigcup_{n\ge1}(C_n)_x,
$$

and symmetrically for $C^y$. Hence $\mathfrak S$ is a $\sigma$-field. For a measurable rectangle,

$$
(A\times B)_x
=
\begin{cases}
B,&x\in A,\\
\varnothing,&x\notin A,
\end{cases}
\qquad
(A\times B)^y
=
\begin{cases}
A,&y\in B,\\
\varnothing,&y\notin B.
\end{cases}
$$

Thus $\mathfrak S$ contains the rectangles. Generated-$\sigma$-field minimality gives

$$
\mathcal A\otimes\mathcal B\subseteq\mathfrak S.
$$

For the first integral identity, let $\mathfrak D_E$ be the class of all $C\in\mathcal A\otimes\mathcal B$ such that $x\mapsto\nu(C_x)$ is measurable and

$$
m(C)=\int_E\nu(C_x)\,\mu(dx).
$$

If $C=A\times B$, then

$$
\nu(C_x)=\mathbf1_A(x)\nu(B),
$$

so every measurable rectangle belongs to $\mathfrak D_E$.

The full space belongs to $\mathfrak D_E$. If $C\in\mathfrak D_E$, then, because $\nu(F)=m(E\times F)=1$,

$$
\nu((C^c)_x)=1-\nu(C_x)
$$

and

$$
\int_E\nu((C^c)_x)\,d\mu
=
1-m(C)
=
m(C^c).
$$

All subtractions are between finite numbers; no expression $+\infty-\infty$ occurs. Finally, if $(C_n)$ is pairwise disjoint in $\mathfrak D_E$, then

$$
\nu\!\left(\left(\bigcup_{n\ge1}C_n\right)_x\right)
=
\sum_{n\ge1}\nu((C_n)_x).
$$

The partial sums are measurable and increase pointwise. Monotone convergence and countable additivity give

$$
\begin{aligned}
\int_E\nu\!\left(\left(\bigcup_{n\ge1}C_n\right)_x\right)d\mu
&=
\sum_{n\ge1}\int_E\nu((C_n)_x)\,d\mu\\
&=
\sum_{n\ge1}m(C_n)
=
m\!\left(\bigcup_{n\ge1}C_n\right).
\end{aligned}
$$

Therefore $\mathfrak D_E$ is a Dynkin system containing the generating $\pi$-system of rectangles. The $\pi$--$\lambda$ theorem yields

$$
\mathfrak D_E=\mathcal A\otimes\mathcal B.
$$

Exchanging $E$ and $F$ gives the second identity. Hence, for every $C\in\mathcal A\otimes\mathcal B$,

$$
m(C)
=
\int_E\nu(C_x)\,d\mu
=
\int_F\mu(C^y)\,d\nu.
$$

The probability assumption is doing real work here. For general $\sigma$-finite measures, the complement argument may contain $+\infty-\infty$; one must first localize to finite rectangles and use uniqueness of the restricted product measures.

### 2. Construction of nonnegative Tonelli

Let

$$
s=\sum_{j=1}^r a_j\mathbf1_{C_j},
\qquad
a_j\ge0,
$$

where the $C_j$ are pairwise disjoint product-measurable sets. For every $x$,

$$
\int_Fs(x,y)\,\nu(dy)
=
\sum_{j=1}^r a_j\nu((C_j)_x).
$$

This is measurable in $x$, and the indicator identity gives

$$
\int_{E\times F}s\,dm
=
\int_E\left(\int_Fs(x,y)\,\nu(dy)\right)\mu(dx).
$$

The reversed identity is symmetric.

Now choose nonnegative simple functions $s_n\uparrow f$. For every fixed $x$, monotone convergence on $(F,\mathcal B,\nu)$ gives

$$
\int_Fs_n(x,y)\,\nu(dy)
\uparrow
\int_Ff(x,y)\,\nu(dy).
$$

Thus the limiting section integral is measurable. Monotone convergence first on $(E\times F,m)$ and then on $(E,\mu)$ yields

$$
\begin{aligned}
\int_{E\times F}f\,dm
&=
\lim_{n\to\infty}\int_{E\times F}s_n\,dm\\
&=
\lim_{n\to\infty}
\int_E\left(\int_Fs_n(x,y)\,\nu(dy)\right)\mu(dx)\\
&=
\int_E\left(\int_Ff(x,y)\,\nu(dy)\right)\mu(dx).
\end{aligned}
$$

The same argument with the variables exchanged gives the other order. Positivity makes every quantity well-defined in $[0,+\infty]$; the common value need not be finite.

### 3. Factorization

Set

$$
u_n:=u\wedge n,
\qquad
v_n:=v\wedge n.
$$

Each map $(x,y)\mapsto u_n(x)v_n(y)$ is product-measurable, because the coordinate maps are measurable and multiplication on $[0,n]^2$ is continuous. Moreover,

$$
u_n(x)v_n(y)\uparrow u(x)v(y),
$$

where the limit at $(0,+\infty)$ and $(+\infty,0)$ is $0$. Hence the extended product with the prescribed convention is product-measurable.

We first isolate the scalar rule. If $a\in[0,+\infty]$ and $w\ge0$ is measurable, then

$$
\int aw\,d\rho
=
a\int w\,d\rho,
$$

with $0\cdot(+\infty)=0$. The assertion is standard for $a<+\infty$. If $a=+\infty$, then $aw$ is $+\infty$ on $\{w>0\}$ and $0$ on $\{w=0\}$; both sides are $0$ when $w=0$ almost everywhere and $+\infty$ otherwise.

Tonelli and the scalar rule now give

$$
\begin{aligned}
\int_{E\times F}u(x)v(y)\,dm
&=
\int_E
\left(\int_Fu(x)v(y)\,\nu(dy)\right)\mu(dx)\\
&=
\int_Eu(x)\left(\int_Fv\,d\nu\right)\mu(dx)\\
&=
\left(\int_Eu\,d\mu\right)
\left(\int_Fv\,d\nu\right).
\end{aligned}
$$

In particular, if $\int_Eu\,d\mu=0$ and $\int_Fv\,d\nu=+\infty$, then $u=0$ $\mu$-almost everywhere. The product integrand is therefore $0$ $m$-almost everywhere, its integral is $0$, and the right-hand side is also $0$ by convention. The case with the two factors reversed is symmetric.

Suppose now that $u\in L^1(\mu)$ and $v\in L^1(\nu)$ are real-valued. Applying the nonnegative result to $|u|$ and $|v|$ gives

$$
\int_{E\times F}|u(x)v(y)|\,dm
=
\lVert u\rVert_{L^1(\mu)}
\lVert v\rVert_{L^1(\nu)}
<+\infty.
$$

Thus $uv\in L^1(m)$. Write

$$
u=u^+-u^-,
\qquad
v=v^+-v^-.
$$

The four nonnegative products $u^+v^+$, $u^+v^-$, $u^-v^+$ and $u^-v^-$ have finite integrals by the nonnegative factorization already proved. Consequently their finite linear combination may be integrated term by term, and

$$
\begin{aligned}
\int_{E\times F}u(x)v(y)\,dm
&=
\int u^+v^+\,dm-
\int u^+v^-\,dm-
\int u^-v^+\,dm+
\int u^-v^-\,dm\\
&=
\left(\int_Eu\,d\mu\right)
\left(\int_Fv\,d\nu\right).
\end{aligned}
$$

The $L^1$ hypothesis is the boundary: separate conditionally convergent signed expressions do not license this argument.

### 4. Coordinate projections

The coordinate projections are measurable by the definition of the product $\sigma$-field. For $A\in\mathcal A$ and $B\in\mathcal B$,

$$
m(\pi_E\in A)
=
m(A\times F)
=
\mu(A),
$$

and similarly $m(\pi_F\in B)=\nu(B)$. Hence the marginal laws are $\mu$ and $\nu$. Moreover,

$$
\begin{aligned}
m(\pi_E\in A,\pi_F\in B)
&=
m(A\times B)\\
&=
\mu(A)\nu(B)\\
&=
m(\pi_E\in A)m(\pi_F\in B).
\end{aligned}
$$

Thus $\pi_E$ and $\pi_F$ are independent.

### 5. Independence as a product joint law

The class

$$
\mathfrak M
:=
\{C\subseteq E\times F:(X,Y)^{-1}(C)\in\mathcal F\}
$$

is a $\sigma$-field. It contains every rectangle because

$$
(X,Y)^{-1}(A\times B)
=
X^{-1}(A)\cap Y^{-1}(B).
$$

Therefore $(X,Y)$ is $\mathcal F/(\mathcal A\otimes\mathcal B)$-measurable.

If $X\perp Y$, then for every measurable rectangle,

$$
\begin{aligned}
\mu_{X,Y}(A\times B)
&=
\mathbb P(X\in A,Y\in B)\\
&=
\mathbb P(X\in A)\mathbb P(Y\in B)\\
&=
(\mu_X\otimes\mu_Y)(A\times B).
\end{aligned}
$$

The rectangles form a generating $\pi$-system, and both measures are probability measures. Uniqueness on a generating $\pi$-system gives

$$
\mu_{X,Y}=\mu_X\otimes\mu_Y.
$$

Conversely, equality of these measures evaluated on $A\times B$ gives the eventwise factorization defining independence. No topological or standard-Borel hypothesis is needed.

### 6. Minimum and a heavy-tail boundary

For any nonnegative random variable $Z$, the set

$$
H_Z:=\{(\omega,t)\in\Omega\times(0,+\infty):0<t<Z(\omega)\}
$$

is product-measurable. Indeed,

$$
H_Z
=
\bigcup_{q\in\mathbb Q_{>0}}
\{Z>q\}\times(0,q).
$$

For $N>0$, let $\nu_N$ be normalized Lebesgue measure on $(0,N)$:

$$
\nu_N:=\frac1N\lambda|_{(0,N)}.
$$

This is a probability measure, so the probability-space Tonelli theorem proved in part 2 applies to $\mathbf1_{H_Z}$ on $\Omega\times(0,N)$. Since

$$
Z(\omega)\wedge N
=
\int_0^N\mathbf1_{\{t<Z(\omega)\}}\,dt,
$$

it gives, after multiplication by $N$,

$$
\begin{aligned}
\mathbb E[Z\wedge N]
&=
N\int_\Omega\int_{(0,N)}
\mathbf1_{\{t<Z(\omega)\}}\,\nu_N(dt)\,\mathbb P(d\omega)\\
&=
N\int_{(0,N)}\mathbb P(Z>t)\,\nu_N(dt)\\
&=
\int_0^N\mathbb P(Z>t)\,dt.
\end{aligned}
$$

Letting $N\uparrow+\infty$ and applying monotone convergence to both sides gives the layer-cake identity

$$
\mathbb E[Z]
=
\int_0^\infty\mathbb P(Z>t)\,dt
$$

in $[0,+\infty]$. For $Z=\min(X,Y)$,

$$
\{Z>t\}=\{X>t\}\cap\{Y>t\}.
$$

Independence therefore yields

$$
\mathbb E[\min(X,Y)]
=
\int_0^\infty
\mathbb P(X>t)\mathbb P(Y>t)\,dt.
$$

For the counterexample, take

$$
\bigl((0,1)^2,
\mathcal B((0,1))\otimes\mathcal B((0,1)),
\lambda\otimes\lambda\bigr)
$$

and let $U$ and $V$ be the coordinate projections. Set

$$
X:=\frac1U-1,
\qquad
Y:=\frac1V-1.
$$

The coordinate projections are independent. With $g(s)=s^{-1}-1$, for Borel sets $A,B\subseteq[0,+\infty)$ one has

$$
\begin{aligned}
\mathbb P(X\in A,Y\in B)
&=
\mathbb P(U\in g^{-1}(A),V\in g^{-1}(B))\\
&=
\mathbb P(U\in g^{-1}(A))
\mathbb P(V\in g^{-1}(B))\\
&=
\mathbb P(X\in A)\mathbb P(Y\in B).
\end{aligned}
$$

Thus $X$ and $Y$ are independent. For $t\ge0$,

$$
\mathbb P(X>t)
=
\mathbb P\!\left(U<\frac1{1+t}\right)
=
\frac1{1+t},
$$

and the same formula holds for $Y$. Consequently,

$$
\mathbb E[X]
=
\mathbb E[Y]
=
\int_0^\infty\frac{dt}{1+t}
=
+\infty,
$$

whereas

$$
\mathbb E[\min(X,Y)]
=
\int_0^\infty\frac{dt}{(1+t)^2}
=
1.
$$

Thus finiteness of one marginal mean is sufficient for integrability of the minimum, but it is not necessary.

## Problème II — Une somme se souvient de la loi jointe

### 1. Addition as a pushforward

The measurable space $\mathbb Z$ is discrete, so $a:\mathbb Z^2\to\mathbb Z$ is measurable. Since

$$
X+Y=a\circ(X,Y),
$$

functoriality of pushforwards gives

$$
\mu_{X+Y}
=
a_\#\mu_{X,Y}.
$$

For $n\in\mathbb Z$,

$$
a^{-1}(\{n\})
=
\bigsqcup_{k\in\mathbb Z}\{(k,n-k)\}.
$$

Countable additivity therefore gives

$$
\boxed{
\mathbb P(X+Y=n)
=
\sum_{k\in\mathbb Z}p_{X,Y}(k,n-k)
}.
$$

The series is nonnegative and hence always well-defined.

### 2. Convolution and its boundary

If $X\perp Y$, then

$$
\mu_{X,Y}=\mu_X\otimes\mu_Y,
$$

so, for every $k,n\in\mathbb Z$,

$$
p_{X,Y}(k,n-k)
=
p_X(k)p_Y(n-k).
$$

Substitution into the joint-law formula gives

$$
\boxed{
\mathbb P(X+Y=n)
=
\sum_{k\in\mathbb Z}p_X(k)p_Y(n-k)
}.
$$

The replacement of $p_{X,Y}$ by $p_Xp_Y$ is the unique step licensed by independence. Everything before it is valid for an arbitrary coupling.

### 3. Two Bernoulli couplings

Let $B$ be the identity map on $\{0,1\}$ equipped with the uniform probability measure.

For the first pair, take

$$
(X_1,Y_1):=(B,B).
$$

Its joint law and sum law are

$$
\mu_{X_1,Y_1}
=
\frac12\delta_{(0,0)}+\frac12\delta_{(1,1)},
$$

and

$$
\mu_{X_1+Y_1}
=
\frac12\delta_0+\frac12\delta_2.
$$

For the second pair, take

$$
(X_2,Y_2):=(B,1-B).
$$

Then

$$
\mu_{X_2,Y_2}
=
\frac12\delta_{(0,1)}+\frac12\delta_{(1,0)},
$$

and

$$
\mu_{X_2+Y_2}=\delta_1.
$$

Each of the four marginal laws is Bernoulli$(1/2)$, but the joint laws and the sum laws differ.

### 4. What the substitutes fail to determine

Marginals are only the two coordinate pushforwards of a joint law. They fix its row and column masses but not the coupling inside those constraints. A named one-dimensional family, together with its parameters, supplies the same marginal information and nothing more. The preceding Bernoulli pairs already disprove both substitutions.

Zero covariance tests only the single product function $(x,y)\mapsto xy$. Independence requires factorization for all measurable rectangles, equivalently for a determining class of product tests.

For an explicit uncorrelated but dependent pair, use the product of the uniform laws on $\{-1,0,1\}$ and $\{-1,1\}$. Let $W$ and $\varepsilon$ be the coordinate projections and define

$$
X:=W,
\qquad
Y:=\varepsilon W.
$$

Both $X$ and $Y$ are uniform on $\{-1,0,1\}$. Moreover,

$$
\mathbb E[X]=\mathbb E[Y]=0
$$

and, by independence of $W$ and $\varepsilon$,

$$
\mathbb E[XY]
=
\mathbb E[\varepsilon W^2]
=
\mathbb E[\varepsilon]\mathbb E[W^2]
=
0.
$$

Thus $\operatorname{Cov}(X,Y)=0$. Nevertheless,

$$
\mathbb P(X=0,Y=0)
=
\frac13
\ne
\frac19
=
\mathbb P(X=0)\mathbb P(Y=0),
$$

so the pair is not independent. The missing statement in every failed substitute is exactly

$$
\mu_{X,Y}=\mu_X\otimes\mu_Y.
$$

For Bernoulli marginals specifically, zero covariance does force the remaining $2\times2$ joint table to factorize; that special fact cannot be promoted to general random variables.

### 5. Independent Bernoulli blocks

First assume $0<p<1$ and write $q:=1-p$. A configuration

$$
(b_1,\ldots,b_m,c_1,\ldots,c_n)\in\{0,1\}^{m+n}
$$

containing exactly $k$ entries equal to $1$ has probability

$$
p^kq^{m+n-k}
$$

by mutual independence. The event $\{U+V=k\}$ is the disjoint union of all such configurations. There are $\binom{m+n}{k}$ of them when $0\le k\le m+n$, and none otherwise. Hence

$$
\mathbb P(U+V=k)
=
\begin{cases}
\displaystyle
\binom{m+n}{k}p^kq^{m+n-k},
&0\le k\le m+n,\\[1ex]
0,&\text{otherwise}.
\end{cases}
$$

Equivalently, partitioning first according to the number $r$ of successes in the first block gives

$$
\mathbb P(U+V=k)
=
p^kq^{m+n-k}
\sum_{r\in\mathbb Z}
\binom mr\binom n{k-r},
$$

and counting the same $k$-element subsets of an $(m+n)$-element set yields Vandermonde's identity

$$
\sum_{r\in\mathbb Z}
\binom mr\binom n{k-r}
=
\binom{m+n}{k}.
$$

The two blocks are independent because every event determined by the first block factors from every event determined by the second. Thus $U$ and $V$ are independent, but the displayed law was obtained from the underlying product construction rather than from a stability slogan. The endpoint cases $p=0$ and $p=1$ are deterministic and give the same formula directly.

Only now do we name the conclusion:

$$
U+V\sim\operatorname{Bin}(m+n,p).
$$
