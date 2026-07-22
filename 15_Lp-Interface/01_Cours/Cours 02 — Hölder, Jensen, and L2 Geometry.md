---
type: cours
module: lp-interface
status: canonical
---

# Cours 02 — Hölder, Jensen, and $L^2$ Geometry

This Cours supplies the part of the $L^p$ interface not contained in the endpoint $L^1$–$L^\infty$ pairing: general Hölder, Cauchy–Schwarz, Jensen and the minimum Hilbert-space geometry later used by conditional expectation.

It does not develop full $L^p$ duality, weak convergence or spectral theory.

## 1. Conjugate exponents and Young's inequality

Let

$$
1<p<+\infty,
\qquad
q=\frac{p}{p-1}.
$$

Then

$$
\frac1p+\frac1q=1.
$$

The numbers $p$ and $q$ are conjugate exponents.

### Proposition 1.1 — Young's inequality

For $a,b\ge0$,

$$
ab
\le
\frac{a^p}{p}
+
\frac{b^q}{q}.
$$

Equality holds if and only if

$$
a^p=b^q.
$$

### Proof

The weighted arithmetic–geometric mean inequality gives, for $u,v\ge0$,

$$
u^{1/p}v^{1/q}
\le
\frac{u}{p}+\frac{v}{q}.
$$

Apply this with $u=a^p$ and $v=b^q$. Equality in weighted AM–GM holds exactly when $u=v$.

Young's inequality is the scalar mechanism behind Hölder. The exponents are not decorative: they are chosen so that normalization converts the product into a sum of integrable powers.

## 2. Hölder and Minkowski

### Theorem 2.1 — Hölder

Let $f\in L^p(\mu)$ and $g\in L^q(\mu)$, where $1<p<+\infty$ and $q$ is conjugate to $p$. Then $fg\in L^1(\mu)$ and

$$
\boxed{
\|fg\|_1
\le
\|f\|_p\|g\|_q
}.
$$

The endpoint case $p=1$, $q=+\infty$ is the $L^1$–$L^\infty$ estimate established in Cours 01.

### Proof

If one of the norms is zero, the conclusion is immediate. Otherwise define

$$
F=\frac{|f|}{\|f\|_p},
\qquad
G=\frac{|g|}{\|g\|_q}.
$$

Young's inequality gives

$$
FG
\le
\frac{F^p}{p}+\frac{G^q}{q}.
$$

After integration,

$$
\int_EFG\,d\mu
\le
\frac1p\int_EF^p\,d\mu
+
\frac1q\int_EG^q\,d\mu
=1.
$$

Multiplying by $\|f\|_p\|g\|_q$ proves the result.

When both norms are nonzero, equality requires

$$
\frac{|f|^p}{\|f\|_p^p}
=
\frac{|g|^q}{\|g\|_q^q}
\qquad\mu\text{-a.e.}
$$

and compatible signs if the inequality is applied without absolute values.

### Theorem 2.2 — Minkowski

For $1\le p<+\infty$ and $f,g\in L^p(\mu)$,

$$
\|f+g\|_p
\le
\|f\|_p+\|g\|_p.
$$

### Proof for $1<p<+\infty$

The elementary bound

$$
|f+g|^p
\le
2^{p-1}\bigl(|f|^p+|g|^p\bigr)
$$

first shows that $f+g\in L^p(\mu)$. Let $q=p/(p-1)$. If $\|f+g\|_p=0$, there is nothing to prove. Otherwise,

$$
\begin{aligned}
\|f+g\|_p^p
&=
\int_E|f+g|^p\,d\mu\\
&\le
\int_E|f|\,|f+g|^{p-1}\,d\mu
+
\int_E|g|\,|f+g|^{p-1}\,d\mu.
\end{aligned}
$$

Hölder applies because

$$
(p-1)q=p.
$$

Hence

$$
\|f+g\|_p^p
\le
(\|f\|_p+\|g\|_p)
\|f+g\|_p^{p-1}.
$$

Division gives the result. The case $p=1$ is the triangle inequality for the integral.

## 3. The $L^2$ structure

Let $f,g\in L^2(\mu)$. Cauchy–Schwarz, which is Hölder with $p=q=2$, gives

$$
\int_E|fg|\,d\mu
\le
\|f\|_2\|g\|_2.
$$

Therefore

$$
\langle f,g\rangle
=
\int_Efg\,d\mu
$$

is well defined on equivalence classes in $L^2(\mu)$.

### Proposition 3.1 — Cauchy–Schwarz

For $f,g\in L^2(\mu)$,

$$
|\langle f,g\rangle|
\le
\|f\|_2\|g\|_2.
$$

If $f$ and $g$ are nonzero, equality holds if and only if they are linearly dependent in $L^2(\mu)$.

### Geometric identities

If $f\perp g$, meaning $\langle f,g\rangle=0$, then

$$
\|f+g\|_2^2
=
\|f\|_2^2+\|g\|_2^2.
$$

For arbitrary $f,g\in L^2(\mu)$,

$$
\|f+g\|_2^2
+
\|f-g\|_2^2
=
2\|f\|_2^2+2\|g\|_2^2.
$$

This is the parallelogram identity.

The standard completeness theorem for $L^p$ implies that $L^2(\mu)$ is a Hilbert space. Completeness is used below only to pass from a minimizing sequence to an actual projection.

## 4. Orthogonal projection

Let $H$ be a real Hilbert space and let $M\subseteq H$ be a closed linear subspace.

### Theorem 4.1 — Projection theorem

For every $x\in H$, there exists a unique $m\in M$ such that

$$
\|x-m\|
=
\inf_{v\in M}\|x-v\|.
$$

This minimizer is characterized by

$$
x-m\perp M.
$$

It is denoted by

$$
P_Mx=m.
$$

### Proof

Set

$$
d=\inf_{v\in M}\|x-v\|
$$

and choose $(m_n)\subset M$ such that $\|x-m_n\|\to d$. The parallelogram identity gives

$$
\|m_n-m_k\|^2
=
2\|x-m_n\|^2
+
2\|x-m_k\|^2
-
4\left\|x-\frac{m_n+m_k}{2}\right\|^2.
$$

Since $(m_n+m_k)/2\in M$, the last norm is at least $d$. Thus $(m_n)$ is Cauchy. Completeness of $H$ and closedness of $M$ give a limit $m\in M$, necessarily satisfying $\|x-m\|=d$.

For $v\in M$ and $t\in\mathbb R$, minimality gives

$$
\|x-m\|^2
\le
\|x-m-tv\|^2.
$$

Expanding the right-hand side yields

$$
0
\le
-2t\langle x-m,v\rangle
+
t^2\|v\|^2
$$

for every $t$. Hence $\langle x-m,v\rangle=0$. Conversely, if $x-m\perp M$, then for every $v\in M$,

$$
\|x-v\|^2
=
\|x-m\|^2+\|m-v\|^2,
$$

so $m$ is the unique minimizer.

The decomposition

$$
x=P_Mx+(x-P_Mx)
$$

is therefore the orthogonal decomposition relative to

$$
H=M\oplus M^\perp.
$$

The map $P_M$ is linear and contractive:

$$
\|P_Mx-P_My\|
\le
\|x-y\|.
$$

## 5. Jensen's inequality

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space. Let $I\subseteq\mathbb R$ be an interval and let $\Phi:I\to\mathbb R$ be convex.

### Theorem 5.1 — Jensen

Let $X\in L^1(\mathbb P)$ take values in $I$ almost surely, and assume that $\Phi(X)$ is integrable. Then

$$
\boxed{
\Phi(\mathbb E[X])
\le
\mathbb E[\Phi(X)]
}.
$$

### Proof architecture

Set $m=\mathbb E[X]$. A convex function admits a supporting affine function at every interior point of its domain: there exists $a\in\mathbb R$ such that

$$
\Phi(x)
\ge
\Phi(m)+a(x-m),
\qquad x\in I.
$$

Applying this pointwise to $X$ and integrating gives

$$
\mathbb E[\Phi(X)]
\ge
\Phi(m)+a\mathbb E[X-m]
=
\Phi(m).
$$

Endpoint cases reduce either to the same one-sided support argument or to the fact that an integrable random variable with mean at an endpoint of its range must equal that endpoint almost surely.

If $\Phi$ is strictly convex, equality holds if and only if $X$ is almost surely constant.

## 6. Moment comparison on probability spaces

Let $1\le p<q<+\infty$ and $X\in L^q(\mathbb P)$. Jensen applied to

$$
U=|X|^p
$$

and the convex function

$$
t\longmapsto t^{q/p}
$$

gives

$$
\mathbb E|X|^q
\ge
\left(\mathbb E|X|^p\right)^{q/p}.
$$

Therefore

$$
\boxed{
\|X\|_p
\le
\|X\|_q
}.
$$

This is the probability-space form of the finite-measure embedding. On a general finite measure space the factor

$$
\mu(E)^{1/p-1/q}
$$

must be restored. On an infinite measure space no exponent-only inclusion survives.

## 7. Projection onto constants and finite-dimensional models

Let $X\in L^2(\mathbb P)$. The constants form the one-dimensional closed subspace

$$
\operatorname{span}\{1\}.
$$

Since

$$
\langle X-\mathbb E[X],1\rangle=0,
$$

the orthogonal projection of $X$ onto the constants is

$$
P_{\operatorname{span}\{1\}}X
=
\mathbb E[X].
$$

Equivalently, $\mathbb E[X]$ is the unique minimizer of

$$
c\longmapsto\mathbb E[(X-c)^2].
$$

More generally, for $Y_1,\ldots,Y_n\in L^2(\mathbb P)$, projection onto the finite-dimensional space generated by $1,Y_1,\ldots,Y_n$ is characterized by the normal equations

$$
\mathbb E
\left[
\left(X-a_0-\sum_{k=1}^na_kY_k\right)Y_j
\right]
=0,
\qquad j=0,\ldots,n,
$$

with $Y_0=1$.

Conditional expectation will later replace the finite-dimensional model space by the closed subspace

$$
L^2(\Omega,\mathcal G,\mathbb P)
\subseteq
L^2(\Omega,\mathcal F,\mathbb P).
$$

That identification belongs to the conditional-expectation module; the Hilbert geometry used by it belongs here.

## 8. Boundary of the interface

The following distinctions must remain visible:

1. Hölder proves integrability of a product from conjugate powers; it does not assert full duality.
2. Jensen requires a probability measure, or a normalized finite measure. Without normalization, the formula changes.
3. Moment monotonicity $\|X\|_p\le\|X\|_q$ depends on total mass one.
4. Orthogonal projection uses completeness and closedness. A nonclosed subspace may have an infimum with no minimizer.
5. An equality in $L^2$ is an almost-everywhere statement relative to the ambient measure.

## 9. Reconstruction

The analytic chain is

$$
\text{Young}
\Longrightarrow
\text{Hölder}
\Longrightarrow
\text{Cauchy–Schwarz and Minkowski}.
$$

The convex chain is

$$
\text{supporting affine function}
\Longrightarrow
\text{Jensen}
\Longrightarrow
\text{moment comparison}.
$$

The geometric chain is

$$
\text{parallelogram identity}
\Longrightarrow
\text{projection theorem}
\Longrightarrow
\text{normal equations}.
$$
