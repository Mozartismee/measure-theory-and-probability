---
type: corrige
module: conditional-expectation
status: canonical
td: "TD 02 — Finite Sigma-Fields"
---

# Corrigé — TD 02: Conditioning on Events and Finite Sigma-Fields

The law of $X$ has density

$$
f_X(x)=2x\mathbf1_{(0,1)}(x)
$$

with respect to Lebesgue measure.

## Exercise 1 — Conditioning on an event

### 1. Conditional probability measures on $\Omega$

Since

$$
A=\left\{X\le\frac12\right\},
$$

one has

$$
\mathbb P(A)
=
\int_0^{1/2}2x\,dx
=
\frac14,
$$

and therefore

$$
\mathbb P(A^c)=\frac34.
$$

For $H\in\{A,A^c\}$,

$$
\mathbb P_H(E)
=
\frac{\mathbb P(E\cap H)}{\mathbb P(H)}
=
\int_E
\frac{\mathbf1_H}{\mathbb P(H)}
\,d\mathbb P.
$$

Hence

$$
\boxed{
\frac{d\mathbb P_A}{d\mathbb P}
=
4\mathbf1_A
},
$$

and

$$
\boxed{
\frac{d\mathbb P_{A^c}}{d\mathbb P}
=
\frac43\mathbf1_{A^c}
}.
$$

These derivatives belong to $L^1(\mathbb P)$ and are determined $\mathbb P$-almost surely.

### 2. Conditional laws on the state space

For $B\in\mathcal B(\mathbb R)$,

$$
\begin{aligned}
\mu_A(B)
&=\mathbb P_A(X\in B)\\
&=\frac{\mathbb P(X\in B,A)}{\mathbb P(A)}\\
&=\frac{\mathbb P(X\in B\cap C)}{\mathbb P(X\in C)}\\
&=\frac{\mu_X(B\cap C)}{\mu_X(C)}.
\end{aligned}
$$

Similarly,

$$
\mu_{A^c}(B)
=
\frac{\mu_X(B\cap C^c)}{\mu_X(C^c)}.
$$

Thus

$$
\boxed{
\frac{d\mu_A}{d\mu_X}
=
4\mathbf1_C
},
$$

and

$$
\boxed{
\frac{d\mu_{A^c}}{d\mu_X}
=
\frac43\mathbf1_{C^c}
}.
$$

Multiplying by $d\mu_X/d\lambda=f_X$ gives the Lebesgue densities

$$
\boxed{
\frac{d\mu_A}{d\lambda}(x)
=
8x\mathbf1_{(0,1/2)}(x)
},
$$

and

$$
\boxed{
\frac{d\mu_{A^c}}{d\lambda}(x)
=
\frac83x\mathbf1_{(1/2,1)}(x)
}.
$$

Values at the endpoints may be changed because they are $\lambda$-null.

### 3. Distribution functions and means

The distribution function of $\mu_A$ is

$$
F_A(t)
=
\begin{cases}
0, & t\le0,\\
4t^2, & 0<t\le\frac12,\\
1, & t>\frac12.
\end{cases}
$$

The distribution function of $\mu_{A^c}$ is

$$
F_{A^c}(t)
=
\begin{cases}
0, & t\le\frac12,\\
\dfrac{4t^2-1}{3}, & \frac12<t<1,\\
1, & t\ge1.
\end{cases}
$$

The conditional means are

$$
\int_{\mathbb R}x\,\mu_A(dx)
=
\int_0^{1/2}8x^2\,dx
=
\frac13,
$$

and

$$
\int_{\mathbb R}x\,\mu_{A^c}(dx)
=
\int_{1/2}^1\frac83x^2\,dx
=
\frac79.
$$

### 4. Density ledger

| Derivative | Reference measure | Ambient space | Uniqueness |
| --- | --- | --- | --- |
| $d\mathbb P_A/d\mathbb P$ | $\mathbb P$ on $(\Omega,\mathcal F)$ | $L^1(\mathbb P)$ | $\mathbb P$-a.s. |
| $d\mathbb P_{A^c}/d\mathbb P$ | $\mathbb P$ on $(\Omega,\mathcal F)$ | $L^1(\mathbb P)$ | $\mathbb P$-a.s. |
| $d\mu_A/d\mu_X$ | $\mu_X$ on $(\mathbb R,\mathcal B(\mathbb R))$ | $L^1(\mu_X)$ | $\mu_X$-a.e. |
| $d\mu_{A^c}/d\mu_X$ | $\mu_X$ | $L^1(\mu_X)$ | $\mu_X$-a.e. |
| $d\mu_A/d\lambda$ | $\lambda$ | $L^1(\lambda)$ | $\lambda$-a.e. |
| $d\mu_{A^c}/d\lambda$ | $\lambda$ | $L^1(\lambda)$ | $\lambda$-a.e. |

The formulas are related, but the equivalence classes are not interchangeable without an explicit change-of-measure argument.

## Exercise 2 — Decomposition of the law

### 1. Measure identity

For every Borel set $B$,

$$
\begin{aligned}
\mathbb P(A)\mu_A(B)
+
\mathbb P(A^c)\mu_{A^c}(B)
&=
\mathbb P(X\in B,A)
+
\mathbb P(X\in B,A^c)\\
&=
\mathbb P(X\in B)\\
&=
\mu_X(B).
\end{aligned}
$$

Therefore

$$
\boxed{
\mu_X
=
\frac14\mu_A
+
\frac34\mu_{A^c}
}.
$$

### 2. Integration and transfer of $L^1$

Equality of positive measures implies, first for nonnegative Borel $\varphi$,

$$
\int\varphi\,d\mu_X
=
\frac14\int\varphi\,d\mu_A
+
\frac34\int\varphi\,d\mu_{A^c}.
$$

If $\varphi\in L^1(\mu_X)$, apply the formula to $|\varphi|$. Since both coefficients are strictly positive and the left side is finite, both terms on the right are finite. Hence

$$
L^1(\mu_X)
\subset
L^1(\mu_A)\cap L^1(\mu_{A^c}).
$$

More precisely,

$$
\|\varphi\|_{L^1(\mu_A)}
\le
4\|\varphi\|_{L^1(\mu_X)},
$$

and

$$
\|\varphi\|_{L^1(\mu_{A^c})}
\le
\frac43\|\varphi\|_{L^1(\mu_X)}.
$$

The maps on equivalence classes are well defined because

$$
\mu_A\ll\mu_X,
\qquad
\mu_{A^c}\ll\mu_X.
$$

Applying the nonnegative identity to $\varphi^+$ and $\varphi^-$ gives the signed integral identity for every $\varphi\in L^1(\mu_X)$.

### 3. Three test functions, one decomposition

For $\varphi=\mathbf1_B$,

$$
\mu_X(B)
=
\frac14\mu_A(B)
+
\frac34\mu_{A^c}(B).
$$

For $\varphi=\mathbf1_{(-\infty,t]}$,

$$
F_X(t)
=
\frac14F_A(t)
+
\frac34F_{A^c}(t).
$$

For $\varphi(x)=x$,

$$
\mathbb E[X]
=
\frac14\cdot\frac13
+
\frac34\cdot\frac79
=
\frac23.
$$

These are not three different principles. They are the same equality of measures tested against three different functions.

## Exercise 3 — Conditional expectation on a finite $\sigma$-field

### 1. Measurable functions on the two atoms

Since

$$
\mathcal G=\sigma(A)
=
\{\varnothing,A,A^c,\Omega\},
$$

every real-valued $\mathcal G$-measurable function is constant on each atom. Thus

$$
Z=c_A\mathbf1_A+c_{A^c}\mathbf1_{A^c}.
$$

### 2. Determination of the coefficients

Let

$$
Z=\mathbb E[Y\mid\mathcal G]
=
c_A\mathbf1_A+c_{A^c}\mathbf1_{A^c}.
$$

Testing the defining identity on $A$ gives

$$
\mathbb E[Y\mathbf1_A]
=
c_A\mathbb P(A),
$$

so

$$
c_A
=
\frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}.
$$

Testing on $A^c$ gives

$$
c_{A^c}
=
\frac{\mathbb E[Y\mathbf1_{A^c}]}{\mathbb P(A^c)}.
$$

Therefore

$$
\boxed{
\mathbb E[Y\mid\mathcal G]
=
\frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}\mathbf1_A
+
\frac{\mathbb E[Y\mathbf1_{A^c}]}{\mathbb P(A^c)}\mathbf1_{A^c}
}.
$$

On $(\Omega,\mathcal G)$, the signed measure

$$
\nu_Y(E)=\mathbb E[Y\mathbf1_E]
$$

has this function as its RN derivative with respect to $\mathbb P|_{\mathcal G}$.

### 3. Two applications

For $Y=X$, the coefficients are the conditional means already computed:

$$
\boxed{
\mathbb E[X\mid\mathcal G]
=
\frac13\mathbf1_A
+
\frac79\mathbf1_{A^c}
}.
$$

For

$$
Y=\mathbf1_{\{X\le t\}},
$$

one has

$$
\frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}
=
\mathbb P_A(X\le t)
=
F_A(t),
$$

and similarly on $A^c$. Hence

$$
\boxed{
\mathbb E[\mathbf1_{\{X\le t\}}\mid\mathcal G]
=
F_A(t)\mathbf1_A
+
F_{A^c}(t)\mathbf1_{A^c}
}.
$$

### 4. Recovery by the tower property

For $\varphi\in L^1(\mu_X)$, apply the finite-$\sigma$-field formula to $Y=\varphi(X)$:

$$
\mathbb E[\varphi(X)\mid\mathcal G]
=
\left(\int\varphi\,d\mu_A\right)\mathbf1_A
+
\left(\int\varphi\,d\mu_{A^c}\right)\mathbf1_{A^c}.
$$

Taking expectations and using the tower property gives

$$
\int\varphi\,d\mu_X
=
\mathbb P(A)\int\varphi\,d\mu_A
+
\mathbb P(A^c)\int\varphi\,d\mu_{A^c}.
$$

Choosing respectively $\mathbf1_B$, $\mathbf1_{(-\infty,t]}$ and the identity function recovers the measure, distribution-function and mean formulas of Exercise 2.

## Reconstruction

Conditioning on the event changes the probability measure on $\Omega$:

$$
\mathbb P
\longmapsto
\mathbb P_A,
\qquad
\frac{d\mathbb P_A}{d\mathbb P}
=
\frac{\mathbf1_A}{\mathbb P(A)}.
$$

Pushing forward by $X$ changes the law on the state space:

$$
\mu_A=X_\#\mathbb P_A,
\qquad
\frac{d\mu_A}{d\mu_X}
=
\frac{\mathbf1_C}{\mu_X(C)}.
$$

If $\mu_X$ has a Lebesgue density, the chain rule for densities gives $d\mu_A/d\lambda$.

For conditional expectation on $\sigma(A)$, measurability first restricts the candidate to two coefficients. The defining integral identity on the two atoms determines them. For a finite partition $(A_i)_{i=1}^n$ with positive probabilities, the same argument gives

$$
\mathbb E[Y\mid\sigma(A_1,\ldots,A_n)]
=
\sum_{i=1}^n
\frac{\mathbb E[Y\mathbf1_{A_i}]}{\mathbb P(A_i)}
\mathbf1_{A_i}.
$$
