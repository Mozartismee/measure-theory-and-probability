---
type: example-pair
module: examples-and-counterexamples
status: canonical
example-pair: 2
competency-keys:
  - CE.rn-construction
  - CE.finite-sigma-fields
---

# Example Pair 2 — Event Conditioning: Positive-Mass Normalization and Null-Event Failure

## Setup

Let

$$
(\Omega,\mathcal F,\mathbb P)
=
([0,1],\mathcal B([0,1]),\lambda),
$$

where $\lambda$ is Lebesgue probability measure on $[0,1]$. Set

$$
A=\left[0,\frac12\right],
\qquad
N=\{0\},
\qquad
Y(x)=x.
$$

Then $Y\in L^1(\lambda)$, $\lambda(A)=1/2$, and $\lambda(N)=0$.

## Positive regime

Because $\lambda(A)>0$, the normalized restriction

$$
\mathbb P_A(C)
=
\frac{\lambda(C\cap A)}{\lambda(A)}
=
2\lambda(C\cap A),
\qquad C\in\mathcal B([0,1]),
$$

is a probability measure: countable additivity is inherited from $\lambda$, and

$$
\mathbb P_A([0,1])=2\lambda(A)=1.
$$

Moreover $\mathbb P_A\ll\lambda$ and

$$
\frac{d\mathbb P_A}{d\lambda}
=
2\mathbf1_A
$$

as an element of $L^1([0,1],\mathcal B([0,1]),\lambda)$, unique $\lambda$-almost everywhere. Thus, for every $Y\in L^1(\lambda)$,

$$
\int Y\,d\mathbb P_A
=
2\int_A Y\,d\lambda.
$$

For the present $Y(x)=x$,

$$
\mathbb E[Y\mid A]
=
\frac{\int_0^{1/2}x\,dx}{1/2}
=
\frac14,
$$

whereas

$$
\mathbb E[Y\mid A^c]
=
\frac{\int_{1/2}^{1}x\,dx}{1/2}
=
\frac34.
$$

Since both atoms of $\sigma(A)$ have positive mass,

$$
\boxed{
\mathbb E[Y\mid\sigma(A)]
=
\frac14\mathbf1_A
+
\frac34\mathbf1_{A^c}
}
$$

as an $L^1(\Omega,\sigma(A),\lambda|_{\sigma(A)})$ class, unique $\lambda$-almost surely.

## Failure regime

Remove the hypothesis of positive event mass and replace $A$ by $N$. The expressions

$$
\mathbb P_N(C)
=
\frac{\lambda(C\cap N)}{\lambda(N)}
$$

and

$$
\mathbb E[Y\mid N]
=
\frac{\mathbb E[Y\mathbf1_N]}{\lambda(N)}
$$

are undefined: both denominators are zero. There is no normalized event restriction obtained from these ratios.

Conditional expectation on the sub-$\sigma$-field still exists. Indeed,

$$
\sigma(N)=\{\varnothing,N,N^c,\Omega\}.
$$

On this measurable space the numerator

$$
\nu_Y(C)=\int_CY\,d\lambda
$$

is a finite positive measure and the reference measure $\lambda|_{\sigma(N)}$ is finite. Since

$$
\frac{\int_{N^c}x\,d\lambda}{\lambda(N^c)}
=
\frac12,
$$

all versions are

$$
\boxed{
\mathbb E[Y\mid\sigma(N)]
=
\frac12\mathbf1_{N^c}+c\mathbf1_N,
\qquad c\in\mathbb R.
}
$$

They are equal $\lambda$-almost surely and therefore define one $L^1$ class.

## Decisive mechanism

Normalized restriction divides a finite restricted measure by its total mass; the scalar event conditional mean uses the same denominator. Conditional expectation instead applies Radon–Nikodym on the observed sub-$\sigma$-field:

$$
\nu_Y
\ll
\lambda|_{\sigma(N)}.
$$

Finiteness of the reference measure remains available even though one atom is null, so the derivative exists; only its representative value on that null atom is undetermined.

## Boundary

$\mathbb P_A$, $\mathbb E[Y\mid A]$, and $\mathbb E[Y\mid\sigma(A)]$ are respectively a probability measure, a scalar, and an $L^1$ equivalence class. The first two require $\mathbb P(A)>0$; the third does not.

This is an eventwise statement only. A ratio on a null event is not repaired by calling it a conditional probability, and no measurable kernel, regular conditional law, or disintegration theorem is asserted. The governing sources are the [Conditional Expectation Cours](../40_Conditional-Expectation/01_Cours/Cours.md) and the normalized-restriction discussion in the [Atomic Laws Cours](../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md).

## Reconstruction

$$
\mathbb P(A)>0
\longrightarrow
\text{restriction divided by mass}
\longrightarrow
\frac{d\mathbb P_A}{d\mathbb P}
\longrightarrow
\mathbb E[Y\mid A],
$$

whereas

$$
\mathbb P(N)=0
\longrightarrow
\text{event ratios undefined}
\quad\text{but}\quad
\nu_Y\ll\mathbb P|_{\sigma(N)}
\longrightarrow
\mathbb E[Y\mid\sigma(N)]\text{ exists modulo }\mathbb P.
$$
