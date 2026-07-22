---
type: study-session-hints
date: 2026-07-18
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session: J2
session-kind: rupture-repair
access-policy: after-five-minute-stall
math-authority: derived
canonical-sources:
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../80_Lemmas/Counting Measure and the Radon–Nikodym Boundary.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
---

# Indications — Generated $\sigma$-Fields and Counting Measures

Read an indication only after five minutes of genuine obstruction and after recording the first illegal step in the [Séance](00_Séance.md). Read one numbered indication at a time; the plain Markdown headings are deliberate so the file renders consistently across Obsidian, Typora and ordinary Markdown readers.

## Exercice 1 — Sections

### Indication 1

For fixed $x\in E$, taking the section commutes with complement and countable union:

$$
(C^c)_x=F\setminus C_x,
\qquad
\left(\bigcup_nC_n\right)_x
=
\bigcup_n(C_n)_x.
$$

Write the symmetric formulas for $C^y$.

### Indication 2

The property “all horizontal and vertical sections are measurable” must define a $\sigma$-field $\mathcal D$. Check $\varnothing$, complements and countable unions; do not argue separately for every product-measurable set.

### Indication 3

For a rectangle $A\times B$,

$$
(A\times B)_x
=
\begin{cases}
B,&x\in A,\\
\varnothing,&x\notin A.
\end{cases}
$$

Once all rectangles belong to $\mathcal D$, use only the minimality of $\sigma(\{A\times B\})$.

## Exercice 2 — Counting measure

### Indication 1

For pairwise disjoint $(A_n)$, separate three exhaustive cases: some $A_n$ is infinite; infinitely many $A_n$ are nonempty; only finitely many nonempty finite sets remain. Compare both sides of countable additivity in each case.

### Indication 2

Finite counting measure means finite cardinality. A countable union of finite sets is countable, whereas $[0,1]$ is uncountable.

### Indication 3

The only $\#$-null set is $\varnothing$. This settles $\lambda\ll\#$ immediately.

### Indication 4

If $\lambda=f\#$, test the identity on $\{x\}$ for every $x\in[0,1]$. After determining every value $f(x)$, test the identity on $[0,1]$. This proves nonexistence; the failed RN hypothesis is a separate statement.

## Exercice 3 — Atomic integration

### Indication 1

For

$$
s_N=\sum_{n=1}^Np(x_n)\mathbf1_{\{x_n\}},
$$

use $\#_E(\{x_n\})=1$ before invoking any convergence theorem.

### Indication 2

The sequence $s_N$ is pointwise increasing to $p\mathbf1_A$. The required theorem is monotone convergence, not dominated convergence.

### Indication 3

If $E$ is countably infinite, enumerate it without repetitions and write

$$
E=\bigcup_{n\ge1}\{x_n\},
\qquad
\#_E(\{x_n\})=1.
$$

If $E$ is finite, $\#_E(E)<+\infty$ already.

### Indication 4

For uniqueness, determine all $\#_E$-null subsets of $E$.
