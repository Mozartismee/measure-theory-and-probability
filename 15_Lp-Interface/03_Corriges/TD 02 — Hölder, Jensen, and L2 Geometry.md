---
type: corrige
module: lp-interface
status: canonical
td: "TD 02 — Hölder, Jensen, and L2 Geometry"
---

# Corrigé — TD 02: Hölder, Jensen, and $L^2$ Geometry

## Exercise 1 — From Young to Hölder and Minkowski

### 1. Young's inequality

Weighted AM–GM with weights $1/p$ and $1/q$ gives

$$
u^{1/p}v^{1/q}
\le
\frac{u}{p}+\frac{v}{q}.
$$

Taking $u=a^p$ and $v=b^q$ yields

$$
ab
\le
\frac{a^p}{p}+\frac{b^q}{q}.
$$

Equality holds exactly when

$$
u=v,
$$

that is,

$$
a^p=b^q.
$$

### 2. Hölder

If $\|f\|_p=0$ or $\|g\|_q=0$, the product vanishes almost everywhere. Otherwise define

$$
F=\frac{|f|}{\|f\|_p},
\qquad
G=\frac{|g|}{\|g\|_q}.
$$

Young gives

$$
FG
\le
\frac{F^p}{p}+\frac{G^q}{q}.
$$

Since $\int F^p=\int G^q=1$,

$$
\int_EFG\,d\mu\le1.
$$

Therefore

$$
\int_E|fg|\,d\mu
\le
\|f\|_p\|g\|_q.
$$

### 3. Equality in Hölder

Equality in the integrated Young inequality requires pointwise equality almost everywhere on the relevant support. Hence

$$
\frac{|f|^p}{\|f\|_p^p}
=
\frac{|g|^q}{\|g\|_q^q}
\qquad\mu\text{-a.e.}
$$

Equivalently, $|f|^p$ and $|g|^q$ are proportional almost everywhere. If one studies

$$
\left|\int fg\,d\mu\right|
$$

rather than $\int|fg|$, the signs must also be compatible almost everywhere.

### 4. Minkowski

For $1<p<+\infty$, the elementary estimate

$$
|f+g|^p
\le
2^{p-1}\bigl(|f|^p+|g|^p\bigr)
$$

first shows that $f+g\in L^p(\mu)$. Set $q=p/(p-1)$. Then

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

Hölder gives

$$
\int_E|f|\,|f+g|^{p-1}\,d\mu
\le
\|f\|_p
\left(
\int_E|f+g|^{(p-1)q}\,d\mu
\right)^{1/q}.
$$

Since $(p-1)q=p$, the last factor is $\|f+g\|_p^{p-1}$. The same estimate holds for $g$, hence

$$
\|f+g\|_p^p
\le
(\|f\|_p+\|g\|_p)
\|f+g\|_p^{p-1}.
$$

If $\|f+g\|_p>0$, division proves Minkowski. The case of zero norm is immediate; $p=1$ follows directly from $|f+g|\le|f|+|g|$.

### 5. Boundary

Hölder constructs, for every $g\in L^q$, a bounded linear functional

$$
f\longmapsto\int_Efg\,d\mu
$$

on $L^p$. It does not prove that every bounded linear functional has this form. Surjectivity of the representation map is the missing content of the duality theorem.

## Exercise 2 — Cauchy–Schwarz, covariance and moments

### 1. Product integrability

Hölder with $p=q=2$ gives

$$
\mathbb E|XY|
\le
\left(\mathbb E[X^2]\right)^{1/2}
\left(\mathbb E[Y^2]\right)^{1/2}.
$$

Thus $XY\in L^1$ and

$$
|\mathbb E[XY]|
\le
\|X\|_2\|Y\|_2.
$$

### 2. Covariance

Apply Cauchy–Schwarz to the centered variables

$$
X_0=X-\mathbb E[X],
\qquad
Y_0=Y-\mathbb E[Y].
$$

Then

$$
|\operatorname{Cov}(X,Y)|
=
|\mathbb E[X_0Y_0]|
\le
\|X_0\|_2\|Y_0\|_2,
$$

which is the stated inequality. If either variance is zero, equality holds automatically. When both variances are positive, equality holds exactly when

$$
X-\mathbb E[X]
=
c\bigl(Y-\mathbb E[Y]\bigr)
$$

almost surely for some constant $c$.

### 3. Moment comparison

#### Hölder proof

Let $a=s/r>1$ and let $a'=s/(s-r)$ be its conjugate. Since $\mathbb P(\Omega)=1$,

$$
\begin{aligned}
\mathbb E|X|^r
&=\mathbb E[|X|^r\mathbf1]\\
&\le
\left(\mathbb E|X|^{ra}\right)^{1/a}
\left(\mathbb E1^{a'}\right)^{1/a'}\\
&=
\left(\mathbb E|X|^s\right)^{r/s}.
\end{aligned}
$$

Taking the $r$-th root yields $\|X\|_r\le\|X\|_s$.

#### Jensen proof

Set $U=|X|^r$ and use the convex function $\Phi(t)=t^{s/r}$ on $[0,+\infty)$. Jensen gives

$$
\left(\mathbb E|X|^r\right)^{s/r}
\le
\mathbb E|X|^s.
$$

The same conclusion follows.

### 4. Infinite-measure counterexample

On $((1,+\infty),\lambda)$ choose $a$ such that

$$
\frac1s<a\le\frac1r
$$

and set $f(x)=x^{-a}$. Then

$$
as>1,
\qquad
ar\le1.
$$

Thus $f\in L^s$ but $f\notin L^r$. The probability-space monotonicity is therefore a finite-mass statement, not an intrinsic ordering of exponents.

## Exercise 3 — Jensen and its equality boundary

### 1. Supporting-line proof

Let $m=\mathbb E[X]$. If $m$ is an endpoint of the interval, the fact that $X$ takes values on only one side of $m$ forces $X=m$ almost surely, and Jensen is immediate. Otherwise $m$ is an interior point. Convexity then provides a supporting affine function at $m$: there exists $a\in\mathbb R$ such that

$$
\Phi(x)
\ge
\Phi(m)+a(x-m)
$$

for every $x$ in the interval. Substitution of $X$ and integration give

$$
\mathbb E[\Phi(X)]
\ge
\Phi(m)+a\mathbb E[X-m]
=
\Phi(\mathbb E[X]).
$$

### 2. Strict convexity

If $X$ is not almost surely constant, choose $c$ such that

$$
0<\mathbb P(X\le c)<1.
$$

Set $A=\{X\le c\}$, $p=\mathbb P(A)$ and

$$
m_1=
\frac{\mathbb E[X\mathbf1_A]}{\mathbb P(A)},
\qquad
m_2=
\frac{\mathbb E[X\mathbf1_{A^c}]}{\mathbb P(A^c)}.
$$

Then $m_1<m_2$. Jensen applied to the two normalized restrictions gives

$$
\mathbb E[\Phi(X)]
\ge
p\Phi(m_1)+(1-p)\Phi(m_2).
$$

Strict convexity now gives

$$
p\Phi(m_1)+(1-p)\Phi(m_2)
>
\Phi(pm_1+(1-p)m_2)
=
\Phi(\mathbb E[X]).
$$

Hence equality under strict convexity forces $X$ to be almost surely constant. The converse is immediate.

### 3. Quadratic Jensen

Apply Jensen to $\Phi(x)=x^2$:

$$
|\mathbb E[X]|^2
\le
\mathbb E[X^2].
$$

Since $x^2$ is strictly convex, equality holds exactly when $X$ is almost surely constant.

### 4. Reciprocal Jensen

The function $\Phi(x)=1/x$ is strictly convex on $(0,+\infty)$. Therefore

$$
\frac1{\mathbb E[X]}
\le
\mathbb E\left[\frac1X\right].
$$

Multiplication by $\mathbb E[X]>0$ gives

$$
\mathbb E[X]\,\mathbb E[X^{-1}]
\ge1.
$$

Equality holds if and only if $X$ is almost surely constant.

### 5. Finite nonprobability measures

If $0<\mu(E)<+\infty$, apply Jensen to the probability measure

$$
\overline\mu
=
\frac{\mu}{\mu(E)}.
$$

The correct formula is

$$
\Phi\left(
\frac1{\mu(E)}\int_Ef\,d\mu
\right)
\le
\frac1{\mu(E)}\int_E\Phi(f)\,d\mu.
$$

The normalization cannot be silently omitted.

## Exercise 4 — Projection onto an affine linear model

### 1–3. Normal equations

Let

$$
Q(a,b)=\mathbb E[(X-a-bY)^2].
$$

At the minimizing projection, the residual

$$
R=X-a-bY
$$

must be orthogonal to the model space $\operatorname{span}\{1,Y\}$. Thus

$$
\mathbb E[R]=0,
\qquad
\mathbb E[RY]=0.
$$

The first equation gives

$$
a=\mathbb E[X]-b\mathbb E[Y].
$$

Substituting into the second gives

$$
0
=
\operatorname{Cov}(X,Y)
-
b\operatorname{Var}(Y).
$$

Since $\operatorname{Var}(Y)>0$,

$$
\boxed{
b=
\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)},
\qquad
a=
\mathbb E[X]-b\mathbb E[Y]
}.
$$

The Gram matrix of $1$ and $Y$ is nonsingular exactly because $Y$ is not almost surely constant, so the pair is unique.

### 4. Minimum error

After centering, the residual is

$$
R
=
X-\mathbb E[X]
-
b\bigl(Y-\mathbb E[Y]\bigr).
$$

Hence

$$
\begin{aligned}
\mathbb E[R^2]
&=
\operatorname{Var}(X)
-2b\operatorname{Cov}(X,Y)
+b^2\operatorname{Var}(Y)\\
&=
\operatorname{Var}(X)
-
\frac{\operatorname{Cov}(X,Y)^2}{\operatorname{Var}(Y)}.
\end{aligned}
$$

If both variances are positive and

$$
\rho_{X,Y}
=
\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}},
$$

then

$$
\min Q
=
\operatorname{Var}(X)(1-\rho_{X,Y}^2).
$$

### 5. Degenerate predictor

If $\operatorname{Var}(Y)=0$, then $Y$ is almost surely constant. Consequently

$$
\operatorname{span}\{1,Y\}
=
\operatorname{span}\{1\}.
$$

The projected random variable remains uniquely equal to $\mathbb E[X]$, but the coefficients $(a,b)$ are not uniquely identifiable and the quotient defining $b$ is meaningless.

## Exercise 5 — Closed-subspace projection

### 1. A minimizing sequence is Cauchy

Let

$$
d=d(x,M).
$$

The parallelogram identity yields

$$
\|m_n-m_k\|^2
=
2\|x-m_n\|^2
+
2\|x-m_k\|^2
-
4\left\|x-\frac{m_n+m_k}{2}\right\|^2.
$$

Since $(m_n+m_k)/2\in M$, the last norm is at least $d$. Therefore

$$
\|m_n-m_k\|^2
\le
2\|x-m_n\|^2
+
2\|x-m_k\|^2
-4d^2,
$$

which tends to zero as $n,k\to\infty$.

### 2. Existence and uniqueness

Completeness of $H$ gives $m_n\to m$ for some $m\in H$. Closedness of $M$ gives $m\in M$, and continuity of the norm gives

$$
\|x-m\|=d.
$$

If $m,m'\in M$ are both minimizers, their midpoint is in $M$. The same parallelogram identity gives

$$
\|m-m'\|^2
=
2d^2+2d^2
-4\left\|x-\frac{m+m'}2\right\|^2
\le0.
$$

Thus $m=m'$.

### 3. Orthogonal characterization

If $m=P_Mx$, then for every $v\in M$ and $t\in\mathbb R$,

$$
\|x-m\|^2
\le
\|x-m-tv\|^2.
$$

Expansion gives

$$
0
\le
-2t\langle x-m,v\rangle+t^2\|v\|^2
$$

for every $t$, hence $\langle x-m,v\rangle=0$.

Conversely, if $x-m\perp M$, then for $v\in M$,

$$
\|x-v\|^2
=
\|x-m\|^2+\|m-v\|^2
\ge
\|x-m\|^2.
$$

### 4. Linearity and contraction

The orthogonal characterization implies that

$$
P_M(ax+by)
=
aP_Mx+bP_My,
$$

because the candidate lies in $M$ and the residual is orthogonal to $M$.

Let $z=x-y$. Since $P_M$ is linear and $z-P_Mz\perp M$,

$$
\|P_Mz\|^2
=
\langle P_Mz,z\rangle
\le
\|P_Mz\|\|z\|.
$$

Thus

$$
\|P_Mx-P_My\|
=
\|P_Mz\|
\le
\|z\|
=
\|x-y\|.
$$

### 5. Why closedness matters

Let $M$ be a proper dense linear subspace of a Hilbert space $H$, and choose $x\in H\setminus M$. Then

$$
d(x,M)=0,
$$

but no $m\in M$ attains the distance, since attainment would force $x=m\in M$. Closedness is therefore an existence hypothesis, not a cosmetic regularity condition.

## Reconstruction — Proof spine

The three mechanisms are distinct:

$$
\text{normalization plus Young}
\Longrightarrow
\text{Hölder},
$$

$$
\text{supporting affine minorant}
\Longrightarrow
\text{Jensen},
$$

$$
\text{parallelogram plus completeness}
\Longrightarrow
\text{projection}.
$$

Jensen's unnormalized form requires a probability measure. Projection requires a Hilbert space and a closed subspace. Every equality in an $L^p$ space is equality modulo the null sets of the ambient measure.
