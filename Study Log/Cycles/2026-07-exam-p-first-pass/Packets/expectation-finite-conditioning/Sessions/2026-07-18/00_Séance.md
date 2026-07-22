---
type: study-session-sheet
date: 2026-07-18
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session-kind: rupture-repair
session: J2
planned-time: 120m
actual-time:
solutions-policy: attempt-before-corrige
state: not-attempted
math-authority: derived
canonical-sources:
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../80_Lemmas/Counting Measure and the Radon–Nikodym Boundary.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
---

# Séance — Generated $\sigma$-Fields and Counting Measures

Use this file alone for the full 120 minutes. It contains every required definition, proposition, exercise, work space, exit test, and final record; no return to the Cours, TD, or parent Carnet is needed.

Open the [Indications](01_Indications.md) only after five minutes of genuine obstruction and after recording the first illegal step. Do not open the [Corrigé](02_Corrigé.md) before all three exercises and exit tests have been attempted.

## Programme

| Time | Work | Required output |
| ---: | --- | --- |
| 0–10 min | Closed-book diagnostic | First unreconstructible step for each of the three ruptures |
| 10–35 min | Sections and generated $\sigma$-fields | Auxiliary $\sigma$-field, closure proof, generators, minimality |
| 35–65 min | Counting measure and the RN boundary | Measure object, failure of $\sigma$-finiteness, precise unavailable hypothesis |
| 65–90 min | Atomic integration | Simple approximants and the integral–series formula by MCT |
| 90–115 min | Closed-book exit tests | Three complete reconstructions, without the notes above |
| 115–120 min | Bilan | Verdict and tomorrow's ten-minute retrieval |

The three objects must be repaired in this order. A downstream formula does not count as repaired while the measure or proof schema on which it depends is still missing.

## I. Diagnostic — 0–10 minutes

Do not read beyond this section before the ten-minute diagnostic is complete.

### A. Sections

Let $(E,\mathcal A)$ and $(F,\mathcal B)$ be measurable spaces. For
$C\subseteq E\times F$, define

$$
C_x=\{y\in F:(x,y)\in C\},
\qquad
C^y=\{x\in E:(x,y)\in C\}.
$$

State the claim which must be proved when
$C\in\mathcal A\otimes\mathcal B$, and write the first step of a proof.

### B. Uncountable counting measure

Let $\#$ be counting measure on
$([0,1],\mathcal B([0,1]))$. Define this map precisely and state the
exhaustive case division which proves its countable additivity. Then
state what must be shown in order to prove that $\#$ is not
$\sigma$-finite.

### C. Atomic integration

Let $E$ be countable, $A\subseteq E$, and
$p:E\to[0,+\infty)$. Write the target identity relating

$$
\int_Ap\,d\#_E
$$

to a series, and name the approximation theorem which should justify
the passage from finite support to countable support.

### Diagnostic record

- **A — first unreconstructible step:**
- **B — first unreconstructible step:**
- **C — first unreconstructible step:**

---

## II. Part A — Sections and generated $\sigma$-fields, 10–35 minutes

### Note de cours

Let $X$ be a set and let $\mathcal G\subseteq 2^X$. The generated
$\sigma$-field is

$$
\sigma(\mathcal G)
=
\bigcap\left\{
\mathcal S\subseteq 2^X:
\mathcal S\text{ is a }\sigma\text{-field and }
\mathcal G\subseteq\mathcal S
\right\}.
$$

**Proposition — Minimality of the generated $\sigma$-field.**
If $\mathcal S$ is a $\sigma$-field on $X$ and
$\mathcal G\subseteq\mathcal S$, then

$$
\sigma(\mathcal G)\subseteq\mathcal S.
$$

**Proof.**
The family defining the intersection above contains $\mathcal S$.
Hence its intersection is contained in $\mathcal S$. $\square$

For measurable spaces $(E,\mathcal A)$ and $(F,\mathcal B)$,

$$
\mathcal A\otimes\mathcal B
=
\sigma\bigl(\{A\times B:A\in\mathcal A,\ B\in\mathcal B\}\bigr).
$$

To prove that an auxiliary class $\mathcal D\subseteq2^{E\times F}$ is a
$\sigma$-field, the closure schema is exactly

$$
\varnothing\in\mathcal D,
\qquad
C\in\mathcal D\Longrightarrow C^c\in\mathcal D,
\qquad
(C_n)_{n\ge1}\subseteq\mathcal D
\Longrightarrow
\bigcup_{n\ge1}C_n\in\mathcal D.
$$

No measure is involved in this definition. The present problem is
entirely about measurable spaces and stable classes of sets.

### Exercice 1 — Measurable sections

Let

$$
\mathcal D
=
\left\{
C\subseteq E\times F:
C_x\in\mathcal B\ \forall x\in E,
\quad
C^y\in\mathcal A\ \forall y\in F
\right\}.
$$

1. Prove the section identities for complements and countable unions:

   $$
   (C^c)_x=F\setminus C_x,
   \qquad
   \left(\bigcup_{n\ge1}C_n\right)_x
   =
   \bigcup_{n\ge1}(C_n)_x,
   $$

   and their symmetric analogues for $C^y$.

2. Deduce that $\mathcal D$ is a $\sigma$-field on $E\times F$.
3. For $A\in\mathcal A$ and $B\in\mathcal B$, compute
   $(A\times B)_x$ and $(A\times B)^y$. Deduce that every measurable
   rectangle belongs to $\mathcal D$.
4. Use only the minimality proposition to prove

   $$
   C\in\mathcal A\otimes\mathcal B
   \Longrightarrow
   C_x\in\mathcal B\ \forall x,
   \quad
   C^y\in\mathcal A\ \forall y.
   $$

5. Explain why neither the existence of a product measure nor
   Tonelli's theorem has been used.

### Copie de travail

- **Complement identities:**
- **Countable-union identities:**
- **Why $\mathcal D$ is a $\sigma$-field:**
- **Sections of $A\times B$:**
- **Minimality step:**
- **First remaining rupture:**

## III. Part B — Counting measure and the RN boundary, 35–65 minutes

### Note de cours

Let $(E,\mathcal E)$ be any measurable space. Counting measure on this
space is the map

$$
\#: \mathcal E\to[0,+\infty],
\qquad
\#(A)=\operatorname{card}(A),
$$

where every infinite set is assigned $+\infty$.

**Proposition — Counting measure is a measure.**
For pairwise disjoint $(A_n)_{n\ge1}\subseteq\mathcal E$,

$$
\#\left(\bigsqcup_{n\ge1}A_n\right)
=
\sum_{n\ge1}\#(A_n).
$$

**Proof.**
If some $A_n$ is infinite, both sides are $+\infty$. If infinitely
many $A_n$ are nonempty, both sides are again $+\infty$. In the
remaining case only finitely many nonempty finite sets occur, and the
identity is ordinary finite additivity of cardinality. Also
$\#(\varnothing)=0$. $\square$

A measure $\mu$ on $(E,\mathcal E)$ is $\sigma$-finite if there exist
$E_n\in\mathcal E$ such that

$$
E=\bigcup_{n\ge1}E_n,
\qquad
\mu(E_n)<+\infty
\quad\text{for every }n.
$$

A positive measure $\nu$ is absolutely continuous with respect to
$\mu$, written $\nu\ll\mu$, if

$$
\mu(A)=0
\Longrightarrow
\nu(A)=0
\qquad
\text{for every }A\in\mathcal E.
$$

**Radon–Nikodym theorem, $\sigma$-finite form.**
Let $\mu$ and $\nu$ be $\sigma$-finite positive measures on
$(E,\mathcal E)$. If $\nu\ll\mu$, then there exists a measurable
$f:E\to[0,+\infty]$ such that

$$
\nu(A)=\int_Af\,d\mu
\qquad
\text{for every }A\in\mathcal E.
$$

The representative is unique $\mu$-almost everywhere.

### Exercice 2 — An uncountable boundary

Let $\#$ be counting measure and let $\lambda$ be Lebesgue measure on
$([0,1],\mathcal B([0,1]))$.

0. Close the note above and reconstruct the proof that $\#$ is a
   measure. Your countable-additivity argument must treat separately:
   one infinite member, infinitely many nonempty members, and only
   finitely many nonempty finite members.
1. Prove that a Borel set $A\subseteq[0,1]$ satisfies
   $\#(A)<+\infty$ if and only if $A$ is finite.
2. Prove that $\#$ is not $\sigma$-finite.
3. Prove that $\lambda\ll\#$.
4. Suppose that a measurable $f:[0,1]\to[0,+\infty]$ satisfies

   $$
   \lambda(A)=\int_Af\,d\#
   \qquad
   \text{for every Borel }A.
   $$

   Test this identity on singletons and derive a contradiction.
5. Identify the unavailable hypothesis in the stated
   Radon–Nikodym theorem. Explain why absolute continuity alone does
   not produce a density here.

### Copie de travail

- **Why $\#$ is a measure:**
- **Finite-$\#$ sets:**
- **Failure of a $\sigma$-finite cover:**
- **Proof of $\lambda\ll\#$:**
- **Singleton test:**
- **Unavailable RN hypothesis:**
- **First remaining rupture:**

## IV. Part C — From Lebesgue integration to a series, 65–90 minutes

### Note de cours

For a nonnegative measurable function $p$ and a measurable set $A$,
the restricted-integral notation means

$$
\int_Ap\,d\mu
:=
\int p\mathbf1_A\,d\mu.
$$

For a measure $\mu$ and a measurable set $B$,

$$
\int\mathbf1_B\,d\mu=\mu(B).
$$

For a nonnegative simple function

$$
s=\sum_{k=1}^m a_k\mathbf1_{B_k},
$$

written with pairwise disjoint measurable sets $B_k$,

$$
\int s\,d\mu
=
\sum_{k=1}^ma_k\mu(B_k).
$$

**Monotone convergence theorem.**
If $0\le f_n\uparrow f$ pointwise, then

$$
\int f_n\,d\mu
\uparrow
\int f\,d\mu.
$$

No new definition of a discrete integral will be introduced. The
series formula must be reconstructed from these three statements.

For a nonnegative family $(a_x)_{x\in A}$, the unordered sum means

$$
\sum_{x\in A}a_x
:=
\sup\left\{
\sum_{x\in K}a_x:K\subseteq A\text{ finite}
\right\}.
$$

If $A=\{x_1,x_2,\ldots\}$ is countable and the enumeration has no
repetitions, this supremum equals
$\lim_{N\to\infty}\sum_{n=1}^Na_{x_n}$ and is independent of the
enumeration.

### Exercice 3 — Atomic integration

Let $E$ be countable, equipped with $2^E$, and let $\#_E$ be counting
measure. Let $A\subseteq E$ and let $p:E\to[0,+\infty)$.

1. Treat the cases $A=\varnothing$ and $A$ finite.
2. If $A=\{x_1,x_2,\ldots\}$ is countably infinite, choose an
   enumeration without repetitions and define

   $$
   s_N
   =
   \sum_{n=1}^Np(x_n)\mathbf1_{\{x_n\}}.
   $$

   Prove that $s_N\uparrow p\mathbf1_A$.
3. Compute $\int s_N\,d\#_E$ from the definition of the integral of a
   simple function, then apply monotone convergence to prove

   $$
   \int_Ap\,d\#_E
   =
   \sum_{x\in A}p(x).
   $$

4. Let $\mu$ be a probability measure on $(E,2^E)$ and set
   $p(x)=\mu(\{x\})$. Deduce

   $$
   \mu(A)
   =
   \sum_{x\in A}p(x)
   =
   \int_Ap\,d\#_E.
   $$

5. Prove that $\#_E$ is $\sigma$-finite. Explain why the notation
   $p=d\mu/d\#_E$ lies inside the stated RN regime, although the
   representation above was obtained directly.
6. State the exact uniqueness basis and explain why it is pointwise
   rather than merely outside a nonempty null set.

### Copie de travail

- **Finite case:**
- **Pointwise monotone approximation:**
- **Integral of $s_N$:**
- **MCT passage:**
- **Setwise atomic representation:**
- **$\sigma$-finite cover of $E$:**
- **Uniqueness basis:**
- **First remaining rupture:**

## V. Épreuve de sortie — 90–115 minutes

Do not consult the notes above, the indications, or the corrigé during
this section.

### Test A — 8 minutes

From the definition of $\mathcal A\otimes\mathcal B$, prove in at most
ten lines that every product-measurable set has measurable sections.
Name the auxiliary class and justify every closure property used.

- **Closed-book answer:**
- **First illegal or missing step:**
- **Verdict:** passed / rupture

### Test B — 10 minutes

On $([0,1],\mathcal B([0,1]))$, define counting measure and give the
three-case proof of its countable additivity. Prove that it is not
$\sigma$-finite and that $\lambda\ll\#$. Then assume

$$
\lambda=f\#
$$

and use first the singleton sets, then $[0,1]$, to derive a
contradiction. Only afterward identify the unavailable hypothesis in
the stated RN theorem.

- **Closed-book answer:**
- **First illegal or missing step:**
- **Verdict:** passed / rupture

### Test C — 7 minutes

Let $E$ be countable and $p:E\to[0,+\infty)$. Starting from the
integral of simple functions, prove

$$
\int_Ap\,d\#_E
=
\sum_{x\in A}p(x)
$$

for every $A\subseteq E$. The phrase “by definition of the discrete
integral” is not admissible.

- **Closed-book answer:**
- **First illegal or missing step:**
- **Verdict:** passed / rupture

## VI. Bilan — 115–120 minutes

Complete only this section during the séance. Do not open the Corrigé
during these five minutes. Grade against the structural criteria below;
if any item is doubtful, record a rupture. The full Corrigé may be
opened only after the Bilan has been locked. The Daily review and the
two Carnets are synchronized afterward.

- **Test A passes only if** $\mathcal D$ is defined, all three
  $\sigma$-field obligations are proved, rectangles are included, and
  generated-$\sigma$-field minimality is invoked in the correct
  direction.
- **Test B passes only if** counting measure is proved to be a measure,
  the uncountable obstruction to $\sigma$-finiteness is proved,
  $\lambda\ll\#$ is verified, nonexistence of a density is proved by
  the singleton test, and the failed RN hypothesis is named.
- **Test C passes only if** the finite simple approximants are defined,
  their monotone limit and integrals are computed, and MCT yields the
  unordered nonnegative sum.

- **Actual time:**
- **Test A:** passed / rupture
- **Test B:** passed / rupture
- **Test C:** passed / rupture
- **First remaining rupture:**
- **Exact illegal or missing step:**
- **Minimal repair for tomorrow's 10-minute retrieval:**
- **Session state:** rupture / reconstructible

Mark the session `reconstructible` only if all three tests are completed legally, without notes. Familiarity with the page is not reconstruction; neither is an elegant transcription of its conclusion.
