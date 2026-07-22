---
type: study-session-corrige
date: 2026-07-18
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session: J2
session-kind: rupture-repair
access-policy: after-complete-attempt
math-authority: derived
canonical-sources:
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../80_Lemmas/Counting Measure and the Radon–Nikodym Boundary.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
---

# Corrigé — Generated $\sigma$-Fields and Counting Measures

Do not read this file before a complete attempt at all three exercises and exit tests. Locate the first illegal step; do not replace the attempt with this solution.

## Exercice 1 — Measurable sections

For $C\subseteq E\times F$ and fixed $x\in E$,

$$
(C^c)_x
=
\{y:(x,y)\notin C\}
=
F\setminus C_x.
$$

Likewise,

$$
\left(\bigcup_{n\ge1}C_n\right)_x
=
\{y:(x,y)\in C_n\text{ for some }n\}
=
\bigcup_{n\ge1}(C_n)_x.
$$

The analogous identities hold for vertical sections:

$$
(C^c)^y=E\setminus C^y,
\qquad
\left(\bigcup_{n\ge1}C_n\right)^y
=
\bigcup_{n\ge1}C_n^y.
$$

Define

$$
\mathcal D
=
\left\{
C\subseteq E\times F:
C_x\in\mathcal B\ \forall x,
\quad
C^y\in\mathcal A\ \forall y
\right\}.
$$

The empty set belongs to $\mathcal D$. The section identities and the
closure of $\mathcal A$ and $\mathcal B$ under complements and
countable unions show that $\mathcal D$ is a $\sigma$-field.

For a measurable rectangle $A\times B$,

$$
(A\times B)_x
=
\begin{cases}
B,&x\in A,\\
\varnothing,&x\notin A,
\end{cases}
$$

and

$$
(A\times B)^y
=
\begin{cases}
A,&y\in B,\\
\varnothing,&y\notin B.
\end{cases}
$$

Thus every measurable rectangle belongs to $\mathcal D$. By the
minimality of the generated $\sigma$-field,

$$
\mathcal A\otimes\mathcal B
\subseteq
\mathcal D.
$$

Hence every product-measurable set has measurable horizontal and
vertical sections. No measure, product-measure construction, Tonelli
theorem, or integral identity has been used.

## Exercice 2 — Counting measure and failure of RN representation

First, $\#(\varnothing)=0$. Let $(A_n)_{n\ge1}$ be pairwise disjoint
Borel sets. If one $A_n$ is infinite, both
$\#(\bigsqcup_nA_n)$ and $\sum_n\#(A_n)$ are $+\infty$. If infinitely
many $A_n$ are nonempty, disjointness makes their union infinite and
the series contains infinitely many terms at least one, so again both
sides are $+\infty$. Otherwise only finitely many nonempty finite sets
occur, and the equality is finite additivity of cardinality. Thus
$\#$ is a measure on $([0,1],\mathcal B([0,1]))$.

A Borel set $A\subseteq[0,1]$ satisfies $\#(A)<+\infty$ exactly when
$A$ is finite. Suppose that $\#$ were $\sigma$-finite. Then there
would exist Borel sets $A_n$ such that

$$
[0,1]=\bigcup_{n\ge1}A_n,
\qquad
\#(A_n)<+\infty.
$$

Every $A_n$ would be finite, so their union would be countable. This
contradicts the uncountability of $[0,1]$. Therefore $\#$ is not
$\sigma$-finite.

The only $\#$-null set is $\varnothing$. Consequently,

$$
\#(A)=0
\Longrightarrow
A=\varnothing
\Longrightarrow
\lambda(A)=0,
$$

so $\lambda\ll\#$.

Assume that a measurable $f:[0,1]\to[0,+\infty]$ satisfies

$$
\lambda(A)=\int_Af\,d\#
$$

for every Borel set $A$. Applying this identity to $\{x\}$ gives

$$
0
=
\lambda(\{x\})
=
\int_{\{x\}}f\,d\#
=
f(x)
$$

for every $x\in[0,1]$. Hence $f=0$ pointwise. Applying the identity to
$[0,1]$ would then give

$$
1=\lambda([0,1])=0,
$$

a contradiction.

The dominating measure $\#$ is not $\sigma$-finite, so the stated
$\sigma$-finite Radon–Nikodym theorem is unavailable. The example
shows directly that absolute continuity alone does not imply a
density outside that theorem regime.

## Exercice 3 — Atomic integration

The empty-set case is immediate. If
$A=\{x_1,\ldots,x_m\}$ is finite, then

$$
p\mathbf1_A
=
\sum_{n=1}^mp(x_n)\mathbf1_{\{x_n\}},
$$

so the definition of the integral of a nonnegative simple function
gives

$$
\int_Ap\,d\#_E
=
\sum_{n=1}^mp(x_n)\#_E(\{x_n\})
=
\sum_{n=1}^mp(x_n).
$$

Now let $A=\{x_1,x_2,\ldots\}$ be enumerated without repetitions and define

$$
s_N
=
\sum_{n=1}^Np(x_n)\mathbf1_{\{x_n\}}.
$$

For each $x\in E$, the sequence $s_N(x)$ is increasing and converges
to $p(x)\mathbf1_A(x)$. Moreover,

$$
\int s_N\,d\#_E
=
\sum_{n=1}^Np(x_n)\#_E(\{x_n\})
=
\sum_{n=1}^Np(x_n).
$$

Monotone convergence therefore yields

$$
\int_Ap\,d\#_E
=
\lim_{N\to\infty}\int s_N\,d\#_E
=
\lim_{N\to\infty}\sum_{n=1}^Np(x_n)
=
\sum_{x\in A}p(x).
$$

If $\mu$ is a probability measure on $(E,2^E)$ and
$p(x)=\mu(\{x\})$, countable additivity gives

$$
\mu(A)
=
\mu\left(\bigsqcup_{x\in A}\{x\}\right)
=
\sum_{x\in A}\mu(\{x\})
=
\sum_{x\in A}p(x).
$$

Combining the two identities,

$$
\mu(A)
=
\int_Ap\,d\#_E
$$

for every $A\subseteq E$. Thus $\mu=p\#_E$. Since
$E$ is countable, $\#_E$ is $\sigma$-finite: it is finite when $E$ is
finite, and if $E=\{x_1,x_2,\ldots\}$ then

$$
E=\bigcup_{n\ge1}\{x_n\},
\qquad
\#_E(\{x_n\})=1.
$$

Moreover $\mu$ is finite and $\mu\ll\#_E$. Hence the notation
$p=d\mu/d\#_E$ lies inside the stated RN regime, although the density
was obtained here by direct construction. Finally,
$\#_E(A)=0$ implies $A=\varnothing$, so equality
$\#_E$-almost everywhere is equality at every point. The density is
therefore pointwise unique.

## Exit-test verdict

- **Test A passes** only if the auxiliary class is defined, proved to
  be a $\sigma$-field, shown to contain every measurable rectangle,
  and used with generated-$\sigma$-field minimality in the correct
  direction.
- **Test B passes** only if counting measure is proved to be a measure,
  its failure of $\sigma$-finiteness is proved, $\lambda\ll\#$ is
  verified, nonexistence of a density is proved by the singleton test,
  and the unavailable RN hypothesis is identified separately.
- **Test C passes** only if the finite simple approximants, their
  pointwise monotone limit, their integrals and the MCT passage to the
  unordered sum are all explicit.

If any required step is absent or circular, record the first failure
rather than replacing the attempt with this corrigé.
