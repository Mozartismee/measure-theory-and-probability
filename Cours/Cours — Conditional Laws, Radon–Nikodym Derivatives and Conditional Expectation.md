# Cours — Radon–Nikodym Representation and Conditional Expectation

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $\mathcal G\subset\mathcal F$ be a sub-$\sigma$-field.

## 1. Conditional expectation

#### Definition

Let $Y\in L^1(\mathbb P)$. A conditional expectation of $Y$ with respect to $\mathcal G$ is a random variable $Z\in L^1(\mathbb P)$ such that

1. $Z$ is $\mathcal G$-measurable;

2. for every $A\in\mathcal G$,

   $$
   \int_A Z\,d\mathbb P
   =
   \int_A Y\,d\mathbb P.
   $$

It is denoted by

$$
Z=\mathbb E[Y\mid\mathcal G].
$$

The notation denotes an element of $L^1(\Omega,\mathcal G,\mathbb P|_{\mathcal G})$, hence an equivalence class modulo $\mathbb P$-null sets.

## 2. Radon–Nikodym construction: the positive case

Let $Y\in L^1_+(\mathbb P)$. Define, on $(\Omega,\mathcal G)$,

$$
\nu_Y(A)
=
\mathbb E[Y\mathbf1_A],
\qquad A\in\mathcal G.
$$

Then $\nu_Y$ is a finite positive measure and

$$
\nu_Y\ll\mathbb P|_{\mathcal G}.
$$

Since $\mathbb P|_{\mathcal G}$ is finite, the Radon–Nikodym theorem gives a nonnegative $\mathcal G$-measurable function $Z$ such that

$$
\nu_Y(A)=\int_AZ\,d\mathbb P,
\qquad A\in\mathcal G.
$$

Moreover,

$$
\mathbb E[Z]=\nu_Y(\Omega)=\mathbb E[Y]<+\infty.
$$

Thus $Z\in L^1_+(\mathbb P)$ and

$$
\boxed{
\mathbb E[Y\mid\mathcal G]
=
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
}.
$$

## 3. The integrable case

Let $Y\in L^1(\mathbb P)$ and write

$$
Y=Y^+-Y^-.
$$

Define

$$
\mathbb E[Y\mid\mathcal G]
=
\mathbb E[Y^+\mid\mathcal G]
-
\mathbb E[Y^-\mid\mathcal G].
$$

Equivalently, if

$$
\nu_Y(A)=\mathbb E[Y\mathbf1_A],
\qquad A\in\mathcal G,
$$

then $\nu_Y$ is a finite signed measure absolutely continuous with respect to $\mathbb P|_{\mathcal G}$, and

$$
\mathbb E[Y\mid\mathcal G]
=
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
$$

in the signed Radon–Nikodym sense.

## 4. Characterization and uniqueness

### Proposition

Let $Y,Z\in L^1(\mathbb P)$, with $Z$ $\mathcal G$-measurable. The following assertions are equivalent:

1. $Z=\mathbb E[Y\mid\mathcal G]$;

2. for every $A\in\mathcal G$,

   $$
   \mathbb E[Y\mathbf1_A]
   =
   \mathbb E[Z\mathbf1_A];
   $$

3. for every bounded $\mathcal G$-measurable random variable $H$,

   $$
   \mathbb E[HY]
   =
   \mathbb E[HZ].
   $$

If $Y,Z\ge0$, the identity also holds for every nonnegative $\mathcal G$-measurable $H$, with values in $[0,+\infty]$.

### Demonstration

The passage from indicators to nonnegative simple functions follows by linearity, and the passage to arbitrary nonnegative $H$ follows by monotone convergence. Bounded signed functions are obtained from positive and negative parts.

If $Z_1$ and $Z_2$ satisfy the defining identity, apply it to

$$
A=\{Z_1>Z_2\}\in\mathcal G
$$

and then exchange $Z_1$ and $Z_2$. Thus

$$
Z_1=Z_2
\qquad\mathbb P\text{-almost surely}.
$$

## 5. Conditional-expectation calculus

Let $Y,Y_1,Y_2\in L^1(\mathbb P)$.

### Linearity

For $a,b\in\mathbb R$,

$$
\mathbb E[aY_1+bY_2\mid\mathcal G]
=
a\mathbb E[Y_1\mid\mathcal G]
+
b\mathbb E[Y_2\mid\mathcal G].
$$

### Positivity and monotonicity

If $Y\ge0$, then

$$
\mathbb E[Y\mid\mathcal G]\ge0
\qquad\mathbb P\text{-almost surely}.
$$

If $Y_1\le Y_2$, then

$$
\mathbb E[Y_1\mid\mathcal G]
\le
\mathbb E[Y_2\mid\mathcal G]
\qquad\mathbb P\text{-almost surely}.
$$

### Preservation of the mean

$$
\mathbb E\!\left[\mathbb E[Y\mid\mathcal G]\right]
=
\mathbb E[Y].
$$

### Fixed points

If $Y$ is $\mathcal G$-measurable, then

$$
\mathbb E[Y\mid\mathcal G]=Y
\qquad\mathbb P\text{-almost surely}.
$$

### Pull-out property

If $H$ is bounded and $\mathcal G$-measurable, then

$$
\mathbb E[HY\mid\mathcal G]
=
H\mathbb E[Y\mid\mathcal G].
$$

The same identity holds whenever the products involved are integrable.

### Tower property

If $\mathcal H\subset\mathcal G$, then

$$
\mathbb E\!\left[
\mathbb E[Y\mid\mathcal G]
\mid\mathcal H
\right]
=
\mathbb E[Y\mid\mathcal H]
$$

and

$$
\mathbb E\!\left[
\mathbb E[Y\mid\mathcal H]
\mid\mathcal G
\right]
=
\mathbb E[Y\mid\mathcal H].
$$

### $L^1$ contraction

$$
\left\|
\mathbb E[Y\mid\mathcal G]
\right\|_{L^1}
\le
\|Y\|_{L^1}.
$$

### Independence

If $Y$ is independent of $\mathcal G$, then

$$
\mathbb E[Y\mid\mathcal G]
=
\mathbb E[Y]
\qquad\mathbb P\text{-almost surely}.
$$

All these identities follow from the characterization and uniqueness theorem.

## 6. Conditioning on an event

Let $A\in\mathcal F$ with $\mathbb P(A)>0$. Define

$$
\mathbb P_A(B)
=
\frac{\mathbb P(B\cap A)}{\mathbb P(A)},
\qquad B\in\mathcal F.
$$

Then

$$
\frac{d\mathbb P_A}{d\mathbb P}
=
\frac{\mathbf1_A}{\mathbb P(A)}.
$$

For $Y\in L^1(\mathbb P)$, the scalar conditional mean is

$$
\mathbb E[Y\mid A]
=
\frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}.
$$

If $0<\mathbb P(A)<1$, then

$$
\mathbb E[Y\mid\sigma(A)]
=
\mathbb E[Y\mid A]\mathbf1_A
+
\mathbb E[Y\mid A^c]\mathbf1_{A^c}.
$$

The first object is a real number. The second is a random variable defined up to $\mathbb P$-almost sure equality.

## 7. State-space representation

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

## 8. Conditional expectation given a random variable

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

## 9. Conditional event laws

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

## 10. Version discipline

The following objects live in different spaces:

| Object                       | Space                          | Equality         |
| ---------------------------- | ------------------------------ | ---------------- |
| $d\mathbb P_D/d\mathbb P$    | $L^1(\mathbb P)$               | $\mathbb P$-a.s. |
| $d\mu_D/d\mu_X$              | $L^1(\mu_X)$                   | $\mu_X$-a.e.     |
| $\mathbb E[Y\mid\mathcal G]$ | $L^1(\mathbb P|_{\mathcal G})$ | $\mathbb P$-a.s. |
| $g_Y=d\rho_Y/d\mu_X$         | $L^1(\mu_X)$                   | $\mu_X$-a.e.     |
| $g_Y(X)$                     | $L^1(\mathbb P)$               | $\mathbb P$-a.s. |

The pullback $g\mapsto g(X)$ transports $\mu_X$-versions to $\mathbb P$-versions.

## 11. Boundary

For each fixed event $D$, the function $g_D$ represents the conditional probability of $D$ given $X$.

This does not by itself construct a regular conditional law

$$
x\longmapsto K(x,\cdot).
$$

Joint measurability in the state variable and the event variable belongs to the theory of Markov kernels and disintegration. It requires additional hypotheses, typically standard Borel state spaces, and is not part of the present module.

## 12. Reconstruction

The following chains must be recoverable without consultation.

### Abstract conditional expectation

$$
Y
\longmapsto
\nu_Y(A)=\mathbb E[Y\mathbf1_A]
\longmapsto
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
\longmapsto
\mathbb E[Y\mid\mathcal G].
$$

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