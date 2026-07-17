---
type: cours
module: conditional-expectation
status: canonical
---

# Cours — Conditional Expectation as a Radon–Nikodym Representation

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $\mathcal G\subset\mathcal F$ be a sub-$\sigma$-field.

This module depends on [the Radon–Nikodym construction](../../20_Radon-Nikodym/01_Cours/Cours.md).

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

## 7. Version discipline

The ambient measure, $L^1$-space and almost-everywhere relation are recorded in [Version Discipline](../../15_Lp-Interface/06_Supplements/Version%20Discipline.md).

## 8. Reconstruction

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

### Semantic closure

$$
\boxed{
\text{conditional expectation}
=
\text{Radon–Nikodym representation on the observed }\sigma\text{-field}
}
$$



## 9. Continuation

Conditioning on a random variable and conditional event laws belong to [Conditional Laws](../../50_Conditional-Laws/01_Cours/Cours.md).
