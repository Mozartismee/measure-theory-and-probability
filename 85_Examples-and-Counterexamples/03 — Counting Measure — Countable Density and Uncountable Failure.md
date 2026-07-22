---
type: example-pair
module: examples-and-counterexamples
status: canonical
example-pair: 3
competency-keys:
  - PF.counting-measure
  - PF.atomic-laws
  - RN.hypotheses
---

# Example Pair 3 — Counting Measure: Countable Density and Uncountable Failure

## Setup

The two regimes use the same kind of reference measure—counting measure—but on different measurable spaces.

In the countable regime, let

$$
E=\mathbb N=\{1,2,\ldots\},
\qquad
\mathcal E=2^{\mathbb N},
$$

and let $\#_{\mathbb N}$ be counting measure. Define

$$
p(n)=2^{-n},
\qquad n\ge1.
$$

In the uncountable regime, use

$$
([0,1],\mathcal B([0,1]))
$$

with counting measure $\#$ and Lebesgue probability measure $\lambda$.

## Positive regime

The sets

$$
F_k=\{1,\ldots,k\},
\qquad k\ge1,
$$

have finite counting measure and satisfy $\mathbb N=\bigcup_{k\ge1}F_k$. Hence $\#_{\mathbb N}$ is $\sigma$-finite. Also

$$
\int_{\mathbb N}p\,d\#_{\mathbb N}
=
\sum_{n=1}^{\infty}2^{-n}
=
1.
$$

Therefore

$$
\mu(A)
:=
\int_Ap\,d\#_{\mathbb N}
=
\sum_{n\in A}2^{-n},
\qquad A\subseteq\mathbb N,
$$

defines a probability measure and

$$
\boxed{
p=\frac{d\mu}{d\#_{\mathbb N}}.
}
$$

The reference measure is $\#_{\mathbb N}$. Its only null set is $\varnothing$, so $\#_{\mathbb N}$-almost-everywhere equality is pointwise equality; the density is determined at every $n$ by

$$
p(n)=\mu(\{n\}).
$$

## Failure regime

Remove countability of the state space. Counting measure on $[0,1]$ is not $\sigma$-finite: a set of finite counting measure is finite, while a countable union of finite sets is countable and therefore cannot cover $[0,1]$.

Nevertheless,

$$
\lambda\ll\#,
$$

because $\#(A)=0$ implies $A=\varnothing$. Suppose that a Borel function $f:[0,1]\to[0,+\infty]$ represented $\lambda$ with respect to $\#$:

$$
\lambda(A)=\int_Af\,d\#
\qquad
\text{for every }A\in\mathcal B([0,1]).
$$

For every $x\in[0,1]$, the singleton test gives

$$
0
=
\lambda(\{x\})
=
\int_{\{x\}}f\,d\#.
$$

The last integral equals $f(x)$ when $f(x)<+\infty$; if $f(x)=+\infty$, monotone convergence applied to $n\mathbf1_{\{x\}}$ makes the integral $+\infty$, also impossible. Hence $f(x)=0$ for every $x$. It follows that

$$
1
=
\lambda([0,1])
=
\int_{[0,1]}f\,d\#
=
0,
$$

a contradiction.

## Decisive mechanism

On a countable space, singleton masses assemble into a countable sum and counting measure is $\sigma$-finite. On the uncountable space, absolute continuity is vacuous because the reference measure has no nonempty null set; singleton tests then force any proposed density of a nonatomic measure to vanish pointwise.

The measure $\lambda$ is finite, but the dominating measure $\#$ is not $\sigma$-finite. Thus the missing hypothesis is on the reference measure, exactly where the $\sigma$-finite Radon–Nikodym theorem requires it.

## Boundary

This pair does not maintain a second general theorem. The complete proof that counting measure is a measure, the exact $\sigma$-finiteness criterion, and the general Radon–Nikodym boundary are canonical in [Lemma 5 — Counting Measure and the Radon–Nikodym Boundary](../80_Lemmas/Counting%20Measure%20and%20the%20Radon–Nikodym%20Boundary.md). The countable density representation is also developed in the [Atomic Laws Cours](../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md).

The failure proves that $\nu\ll\mu$ alone need not yield $\nu=f\mu$ for arbitrary positive measures. It does not weaken the finite or $\sigma$-finite Radon–Nikodym theorem.

## Reconstruction

$$
\mathbb N=\bigcup_kF_k
\longrightarrow
\#_{\mathbb N}\text{ is }\sigma\text{-finite}
\longrightarrow
p(n)=2^{-n}
\longrightarrow
\mu=p\#_{\mathbb N},
$$

but

$$
[0,1]\text{ uncountable}
\longrightarrow
\#\text{ not }\sigma\text{-finite}
\longrightarrow
\lambda\ll\#
\longrightarrow
f(x)=0\text{ for every }x
\longrightarrow
1=0.
$$
