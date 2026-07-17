---
type: corrige
module: conditional-expectation
status: canonical
td: "TD 01 — RN Construction"
---

# Corrigé — TD 01: Conditional Expectation as a Radon–Nikodym Derivative

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $\mathcal G\subseteq\mathcal F$ be a sub-$\sigma$-field.

## Exercise 1 — Construction on a sub-$\sigma$-field

### 1. The nonnegative case

Let $Y\in L^1_+(\mathbb P)$ and define, for $A\in\mathcal G$,

$$
\nu_Y(A)
=
\mathbb E[Y\mathbf1_A].
$$

For pairwise disjoint $(A_n)\subseteq\mathcal G$, the functions

$$
Y\mathbf1_{\bigcup_{k=1}^nA_k}
$$

increase to

$$
Y\mathbf1_{\bigcup_{k\ge1}A_k}.
$$

MCT therefore gives

$$
\nu_Y\left(\bigcup_{k\ge1}A_k\right)
=
\sum_{k\ge1}\nu_Y(A_k).
$$

Thus $\nu_Y$ is a positive measure on $(\Omega,\mathcal G)$. Notice that $Y$ need not be $\mathcal G$-measurable; the construction uses its $\mathcal F$-measurability and restricts only the test sets to $\mathcal G$.

The measure is finite since

$$
\nu_Y(\Omega)=\mathbb E[Y]<+\infty.
$$

If $(\mathbb P|_{\mathcal G})(A)=0$, then $\mathbb P(A)=0$, so

$$
\nu_Y(A)=0.
$$

Thus

$$
\nu_Y\ll\mathbb P|_{\mathcal G}.
$$

The finite Radon–Nikodym theorem gives a nonnegative $\mathcal G$-measurable function

$$
Z_Y
=
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
$$

such that

$$
\mathbb E[Z_Y\mathbf1_A]
=
\mathbb E[Y\mathbf1_A],
\qquad A\in\mathcal G.
$$

Taking $A=\Omega$ gives

$$
\mathbb E[Z_Y]
=
\mathbb E[Y]
<+\infty.
$$

Hence $Z_Y\in L^1_+(\mathbb P)$, and by definition

$$
\boxed{
Z_Y=\mathbb E[Y\mid\mathcal G]
}.
$$

The derivative lives in

$$
L^1(\Omega,\mathcal G,\mathbb P|_{\mathcal G}),
$$

with uniqueness relative to $\mathbb P|_{\mathcal G}$, equivalently $\mathbb P$-almost surely.

### 2. The integrable signed case

For $Y\in L^1(\mathbb P)$, write

$$
Y=Y^+-Y^-.
$$

Construct

$$
Z^+
=
\frac{d\nu_{Y^+}}{d(\mathbb P|_{\mathcal G})},
\qquad
Z^-
=
\frac{d\nu_{Y^-}}{d(\mathbb P|_{\mathcal G})}.
$$

Both functions belong to $L^1_+$. Set

$$
Z=Z^+-Z^-.
$$

Then $Z$ is $\mathcal G$-measurable, integrable, and for every $A\in\mathcal G$,

$$
\begin{aligned}
\mathbb E[Z\mathbf1_A]
&=
\mathbb E[Z^+\mathbf1_A]
-
\mathbb E[Z^-\mathbf1_A]\\
&=
\mathbb E[Y^+\mathbf1_A]
-
\mathbb E[Y^-\mathbf1_A]\\
&=
\mathbb E[Y\mathbf1_A].
\end{aligned}
$$

Now suppose

$$
Y=U-V
$$

is another decomposition with $U,V\in L^1_+$. The corresponding difference of RN derivatives satisfies the same integral identity. If $Z_1,Z_2$ are two $\mathcal G$-measurable integrable candidates, then

$$
\mathbb E[(Z_1-Z_2)\mathbf1_A]=0,
\qquad A\in\mathcal G.
$$

Taking $A=\{Z_1>Z_2\}$ and then $A=\{Z_2>Z_1\}$ gives

$$
Z_1=Z_2
\qquad\mathbb P\text{-a.s.}
$$

Thus the construction is independent of the chosen positive decomposition.

### 3. Bounded-test characterization

Suppose first that $Z=\mathbb E[Y\mid\mathcal G]$. The defining identity holds for indicators of sets in $\mathcal G$, hence by linearity for bounded $\mathcal G$-measurable simple functions.

Let $H$ be bounded and $\mathcal G$-measurable. Choose simple $H_n$ such that

$$
H_n\to H
\quad\text{pointwise},
\qquad
|H_n|\le\|H\|_\infty.
$$

Since

$$
|H_n(Y-Z)|
\le
\|H\|_\infty(|Y|+|Z|)
\in L^1,
$$

DCT gives

$$
\mathbb E[HY]
=
\mathbb E[HZ].
$$

Conversely, if this equality holds for every bounded $\mathcal G$-measurable $H$, take $H=\mathbf1_A$ for $A\in\mathcal G$. The defining conditional-expectation identity follows.

### 4. $L^1$ contraction

Let

$$
Z=\mathbb E[Y\mid\mathcal G]
$$

and define the bounded $\mathcal G$-measurable sign function

$$
S=\operatorname{sgn}(Z).
$$

Then

$$
\mathbb E|Z|
=
\mathbb E[SZ]
=
\mathbb E[SY]
\le
\mathbb E|Y|.
$$

Therefore

$$
\boxed{
\|\mathbb E[Y\mid\mathcal G]\|_1
\le
\|Y\|_1
}.
$$

## Exercise 2 — Identification on a generating class

Define two finite signed measures on $(\Omega,\mathcal G)$ by

$$
\alpha(A)=\mathbb E[Y\mathbf1_A],
\qquad
\beta(A)=\mathbb E[Z\mathbf1_A].
$$

Let

$$
\mathcal D
=
\{A\in\mathcal G:\alpha(A)=\beta(A)\}.
$$

By hypothesis,

$$
\Pi\subseteq\mathcal D.
$$

Also $\Omega\in\Pi$, so $\alpha(\Omega)=\beta(\Omega)$.

If $A\in\mathcal D$, then

$$
\alpha(A^c)
=
\alpha(\Omega)-\alpha(A)
=
\beta(\Omega)-\beta(A)
=
\beta(A^c).
$$

If $(A_n)$ are pairwise disjoint members of $\mathcal D$, countable additivity of the finite signed measures gives

$$
\alpha\left(\bigcup_nA_n\right)
=
\sum_n\alpha(A_n)
=
\sum_n\beta(A_n)
=
\beta\left(\bigcup_nA_n\right).
$$

Thus $\mathcal D$ is a Dynkin system. Since $\Pi$ is a $\pi$-system and $\sigma(\Pi)=\mathcal G$, the $\pi$-$\lambda$ theorem yields

$$
\mathcal D=\mathcal G.
$$

Therefore

$$
\mathbb E[Y\mathbf1_A]
=
\mathbb E[Z\mathbf1_A]
$$

for every $A\in\mathcal G$. Since $Z$ is $\mathcal G$-measurable and integrable,

$$
\boxed{
Z=\mathbb E[Y\mid\mathcal G]
\qquad\mathbb P\text{-a.s.}
}.
$$

## Exercise 3 — Calculus by uniqueness

Write

$$
Z_Y=\mathbb E[Y\mid\mathcal G].
$$

### 1. Fixed points and independence

If $Y$ is $\mathcal G$-measurable, then $Y$ itself is an admissible candidate and

$$
\mathbb E[Y\mathbf1_A]
=
\mathbb E[Y\mathbf1_A]
$$

for every $A\in\mathcal G$. Uniqueness gives

$$
\mathbb E[Y\mid\mathcal G]=Y.
$$

If $Y$ is independent of $\mathcal G$, then for every $A\in\mathcal G$,

$$
\mathbb E[Y\mathbf1_A]
=
\mathbb E[Y]\mathbb P(A)
=
\mathbb E[\mathbb E[Y]\mathbf1_A].
$$

The constant $\mathbb E[Y]$ is $\mathcal G$-measurable, so

$$
\mathbb E[Y\mid\mathcal G]
=
\mathbb E[Y].
$$

### 2. Pull-out property

Let $H$ be bounded and $\mathcal G$-measurable. The candidate

$$
HZ_Y
$$

is $\mathcal G$-measurable and integrable. For $A\in\mathcal G$, the bounded-test characterization applied to $H\mathbf1_A$ gives

$$
\mathbb E[HY\mathbf1_A]
=
\mathbb E[HZ_Y\mathbf1_A].
$$

Hence

$$
\boxed{
\mathbb E[HY\mid\mathcal G]
=
H\mathbb E[Y\mid\mathcal G]
}.
$$

### 3. Tower identities

Let $\mathcal H\subseteq\mathcal G$.

For every $A\in\mathcal H$,

$$
\mathbb E[\mathbb E[Y\mid\mathcal G]\mathbf1_A]
=
\mathbb E[Y\mathbf1_A].
$$

Thus

$$
\boxed{
\mathbb E[\mathbb E[Y\mid\mathcal G]\mid\mathcal H]
=
\mathbb E[Y\mid\mathcal H]
}.
$$

On the other hand, $\mathbb E[Y\mid\mathcal H]$ is $\mathcal H$-measurable and therefore $\mathcal G$-measurable. The fixed-point property gives

$$
\boxed{
\mathbb E[\mathbb E[Y\mid\mathcal H]\mid\mathcal G]
=
\mathbb E[Y\mid\mathcal H]
}.
$$

### 4. Linearity, positivity and monotonicity

For $a,b\in\mathbb R$, the random variable

$$
a\mathbb E[Y_1\mid\mathcal G]
+
b\mathbb E[Y_2\mid\mathcal G]
$$

is $\mathcal G$-measurable, integrable and has the defining integrals of $aY_1+bY_2$. Hence conditional expectation is linear.

If $Y\ge0$ and $Z=\mathbb E[Y\mid\mathcal G]$, let $A=\{Z<0\}\in\mathcal G$. Then

$$
\mathbb E[Z\mathbf1_A]
=
\mathbb E[Y\mathbf1_A]
\ge0.
$$

But the left-hand side is nonpositive. Therefore it is zero, and the nonnegative variable $(-Z)\mathbf1_A$ has expectation zero. Hence $Z\ge0$ almost surely.

If $Y_1\le Y_2$, then $Y_2-Y_1\ge0$. Positivity and linearity give

$$
\mathbb E[Y_1\mid\mathcal G]
\le
\mathbb E[Y_2\mid\mathcal G].
$$

## Reconstruction

For $Y\in L^1$, form on $(\Omega,\mathcal G)$ the two finite positive measures

$$
\nu_{Y^+}(A)=\mathbb E[Y^+\mathbf1_A],
\qquad
\nu_{Y^-}(A)=\mathbb E[Y^-\mathbf1_A].
$$

Both are absolutely continuous with respect to $\mathbb P|_{\mathcal G}$. Their RN derivatives are integrable and $\mathcal G$-measurable. Their difference is the conditional expectation.

Uniqueness is separation by $\mathcal G$-measurable indicators. Bounded tests follow by simple approximation and DCT. Tower properties follow by observing that the defining integral identity remains valid when the test sets are restricted from $\mathcal G$ to $\mathcal H$.
