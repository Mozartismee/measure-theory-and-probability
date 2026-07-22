---
type: lemma
module: lemmas
status: canonical
---

# Lemma 5 — Counting Measure and the Radon–Nikodym Boundary

This lemma separates three facts which must not be conflated: counting measure is always a measure, its $\sigma$-finiteness depends on the underlying measurable space, and absolute continuity alone does not guarantee a Radon–Nikodym density.

The constructive countable regime, including the integral-series formula and the canonical representation of atomic measures, is isolated in [Lemma 6 — Atomic Measures and Integration on Countable Spaces](Atomic%20Measures%20and%20Integration%20on%20Countable%20Spaces.md).

## Proposition 5.1 — Counting Measure

Let $(E,\mathcal E)$ be a measurable space. Define

$$
\#_E:\mathcal E\longrightarrow[0,+\infty]
$$

by

$$
\#_E(A)
:=
\begin{cases}
\operatorname{card}(A),&A\text{ is finite},\\
+\infty,&A\text{ is infinite}.
\end{cases}
$$

Then $\#_E$ is a positive measure on $(E,\mathcal E)$.

### Proof

Clearly, $\#_E(\varnothing)=0$. Let $(A_n)_{n\ge1}\subseteq\mathcal E$ be pairwise disjoint.

If some $A_n$ is infinite, then both

$$
\#_E\left(\bigsqcup_{n\ge1}A_n\right)
$$

and

$$
\sum_{n\ge1}\#_E(A_n)
$$

are equal to $+\infty$.‘

Suppose next that every $A_n$ is finite but infinitely many $A_n$ are nonempty. The disjoint union is then infinite, while the series contains infinitely many positive integer terms. Both sides are again equal to $+\infty$.

In the remaining case, only finitely many $A_n$ are nonempty and all of them are finite. Finite additivity of cardinality gives

$$
\#_E\left(\bigsqcup_{n\ge1}A_n\right)
=
\sum_{n\ge1}\#_E(A_n).
$$

These cases are exhaustive; hence $\#_E$ is countably additive. $\square$

## Proposition 5.2 — The Sigma-Finiteness Criterion

Let $(E,\mathcal E)$ be a measurable space equipped with counting measure $\#_E$. The following assertions are equivalent:

1. $\#_E$ is $\sigma$-finite;
2. there exists a sequence $(F_n)_{n\ge1}\subseteq\mathcal E$ of finite sets such that

   $$
   E=\bigcup_{n\ge1}F_n.
   $$

Consequently, $\sigma$-finiteness of $\#_E$ implies that $E$ is at most countable. If every singleton of $E$ is measurable, then

$$
\#_E\text{ is }\sigma\text{-finite}
\quad\Longleftrightarrow\quad
E\text{ is at most countable}.
$$

### Proof

By definition, $\#_E$ is $\sigma$-finite if and only if there exists $(F_n)_{n\ge1}\subseteq\mathcal E$ such that

$$
E=\bigcup_{n\ge1}F_n
\qquad\text{and}\qquad
\#_E(F_n)<+\infty
\quad(n\ge1).
$$

By the definition of counting measure,

$$
\#_E(F_n)<+\infty
\quad\Longleftrightarrow\quad
F_n\text{ is finite}.
$$

This proves the equivalence. A countable union of finite sets is at most countable, so $\sigma$-finiteness implies that $E$ is at most countable.

Conversely, suppose that every singleton is measurable and that $E$ is at most countable. If $E$ is finite, the constant cover $F_n=E$ proves $\sigma$-finiteness. If $E$ is countably infinite, write

$$
E=\{x_1,x_2,\ldots\}
$$

and set

$$
F_n:=\{x_1,\ldots,x_n\}.
$$

Each $F_n$ is measurable and finite, and $E=\bigcup_{n\ge1}F_n$. Thus $\#_E$ is $\sigma$-finite. $\square$

## Corollary 5.3 — Uncountable Counting Measure

Counting measure on

$$
([0,1],\mathcal B([0,1]))
$$

is not $\sigma$-finite.

### Proof

If it were $\sigma$-finite, Proposition 5.2 would imply that $[0,1]$ is at most countable. This is false. $\square$

## Proposition 5.4 — Absolute Continuity without a Density

Let $\#$ denote counting measure and let $\lambda$ denote Lebesgue measure on

$$
([0,1],\mathcal B([0,1])).
$$

Then

$$
\lambda\ll\#,
$$

but there exists no Borel-measurable function

$$
f:[0,1]\longrightarrow[0,+\infty]
$$

such that

$$
\lambda(A)=\int_A f\,d\#
\qquad
\text{for every }A\in\mathcal B([0,1]).
$$

### Proof

If $A\in\mathcal B([0,1])$ and $\#(A)=0$, then $A=\varnothing$. Hence $\lambda(A)=0$, which proves $\lambda\ll\#$.

Assume, for a contradiction, that such a function $f$ exists. For every $x\in[0,1]$, the singleton $\{x\}$ is Borel and

$$
0
=
\lambda(\{x\})
=
\int_{\{x\}}f\,d\#
=
f(x)\#(\{x\})
=
f(x).
$$

The penultimate equality is the simple-function formula when $f(x)<+\infty$; when $f(x)=+\infty$, it follows by applying monotone convergence to $n\mathbf 1_{\{x\}}\uparrow f\mathbf 1_{\{x\}}$.

Thus $f=0$ pointwise on $[0,1]$. Applying the assumed representation to $[0,1]$ gives

$$
1
=
\lambda([0,1])
=
\int_{[0,1]}f\,d\#
=
0,
$$

a contradiction. $\square$

## Radon–Nikodym Boundary

In Proposition 5.4, the measure $\lambda$ is finite and therefore $\sigma$-finite, whereas the dominating measure $\#$ is not $\sigma$-finite by Corollary 5.3. Hence the $\sigma$-finite Radon–Nikodym theorem is unavailable.

The example proves the precise failure:

$$
\nu\ll\mu
\quad\not\Longrightarrow\quad
\nu=f\mu
$$

for arbitrary positive measures. Absolute continuity does not replace the missing $\sigma$-finiteness hypothesis.

## Reconstruction

The mechanism is the chain

$$
\#(A)=0\Longleftrightarrow A=\varnothing
\longrightarrow
\lambda\ll\#
\longrightarrow
\lambda(\{x\})=0=f(x)
\longrightarrow
f=0
\longrightarrow
\lambda([0,1])=0,
$$

whose final equality contradicts $\lambda([0,1])=1$.
