---
type: lemma
module: lemmas
status: canonical
---

# Lemma 2 — Null Sets and Integral Invariance

Let $(\Omega,\mathcal F,\mu)$ be a measure space.

## Lemma 2.1 — Integration over Null Sets

Let $f:\Omega\to[0,+\infty]$ be $\mathcal F$-measurable, and let $A\in\mathcal F$ satisfy

$$
\mu(A)=0.
$$

Then

$$
\int_A f\,d\mu
:=
\int_\Omega f\mathbf 1_A\,d\mu
=0.
$$

### Proof

By the definition of the integral of a nonnegative measurable function,

$$
\int_\Omega f\mathbf 1_A\,d\mu
=
\sup\left\{
\int_\Omega \varphi\,d\mu:
0\le\varphi\le f\mathbf 1_A,
\ \varphi\text{ simple}
\right\}.
$$

Let $\varphi$ be admissible. Write

$$
\varphi
=
\sum_{i=1}^m a_i\mathbf 1_{E_i},
$$

where $a_i>0$ and the sets $E_i\in\mathcal F$ are pairwise disjoint. Since

$$
0\le\varphi\le f\mathbf 1_A
$$

and $f\mathbf 1_A=0$ on $A^c$, one has

$$
\varphi=\varphi\mathbf 1_A.
$$

Therefore

$$
\int_\Omega\varphi\,d\mu
=
\int_\Omega\varphi\mathbf 1_A\,d\mu
=
\sum_{i=1}^m a_i\mu(E_i\cap A)
=0,
$$

because $\mu(E_i\cap A)=0$ for every $i$. Taking the supremum over all admissible $\varphi$ gives

$$
\int_A f\,d\mu=0.
$$

$\square$

No finiteness or integrability assumption on $f$ is required; in particular, $f$ may take the value $+\infty$ on $A$.

## Lemma 2.2 — Invariance under Almost-Everywhere Equality

Let $f,g:\Omega\to[0,+\infty]$ be $\mathcal F$-measurable. If

$$
f=g
\quad\mu\text{-a.e.},
$$

then

$$
\int_\Omega f\,d\mu
=
\int_\Omega g\,d\mu
$$

as an equality in $[0,+\infty]$.

### Proof

Set

$$
N:=\{f\ne g\}.
$$

Since $f$ and $g$ are measurable, $N\in\mathcal F$; by hypothesis,

$$
\mu(N)=0.
$$

Decompose

$$
f=f\mathbf 1_N+f\mathbf 1_{N^c},
\qquad
g=g\mathbf 1_N+g\mathbf 1_{N^c}.
$$

By additivity of the integral for nonnegative measurable functions and Lemma 2.1,

$$
\int_\Omega f\,d\mu
=
\int_\Omega f\mathbf 1_N\,d\mu
+
\int_\Omega f\mathbf 1_{N^c}\,d\mu
=
\int_\Omega f\mathbf 1_{N^c}\,d\mu,
$$

and similarly,

$$
\int_\Omega g\,d\mu
=
\int_\Omega g\mathbf 1_{N^c}\,d\mu.
$$

Since

$$
f\mathbf 1_{N^c}
=
g\mathbf 1_{N^c}
$$

pointwise on $\Omega$, the two integrals are equal. Hence

$$
\int_\Omega f\,d\mu
=
\int_\Omega g\,d\mu.
$$

$\square$

For signed measurable functions, the same conclusion holds whenever the two integrals are defined; in particular, it holds for $f,g\in L^1(\mu)$. The qualification is necessary because the expression $+\infty-\infty$ is undefined.

## Reconstruction

Lemma 2.1 follows the chain

$$
\text{supremum}
\longrightarrow
\text{simple functions}
\longrightarrow
\text{restriction to }A
\longrightarrow
\text{supremum}.
$$

Lemma 2.2 follows the chain

$$
\text{exceptional null set}
\longrightarrow
\text{decomposition over }N\text{ and }N^c
\longrightarrow
\text{Lemma 2.1}.
$$
