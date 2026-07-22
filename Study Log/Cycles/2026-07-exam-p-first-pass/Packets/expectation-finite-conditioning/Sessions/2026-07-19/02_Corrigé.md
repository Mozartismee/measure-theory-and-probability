---
type: study-session-corrige
date: 2026-07-19
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session: J3
session-kind: progression-with-retrieval
access-policy: after-complete-attempt-and-bilan
math-authority: derived
canonical-sources:
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../80_Lemmas/Counting Measure and the Radon–Nikodym Boundary.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields.md
  - ../../../../../../../60_Applications/Exam-P-Bridges/Expectation and Conditioning — Exam P Deployment Bridge.md
  - ../../../../../../../90_Review/Density and Version Ledger.md
---

# Corrigé rédigé — Restriction, tribu finie et Bayes

Open this file only after all four parts, both final tests and the Bilan in the [Feuille J3](00_Séance.md) have been locked. Repair the exact point where the argument ceased to be legal; do not replace the attempt by transcription. Each solution follows the same public discipline: define the object, verify its legitimacy, invoke the relevant result with hypotheses, then conclude with the correct boundary.

## Question de cours — Trois mécanismes

These skeletons identify yesterday's mechanisms. Reading them does not resolve the corresponding rupture.

### Sections mesurables

Set

$$
\mathcal D
=
\{C\subseteq E\times F:
C_x\in\mathcal B\ \forall x,
C^y\in\mathcal A\ \forall y\}.
$$

Sections commute with complements and countable unions:

$$
(C^c)_x=F\setminus C_x,
\qquad
\left(\bigcup_n C_n\right)_x=\bigcup_n(C_n)_x,
$$

and symmetrically for $C^y$. Hence $\mathcal D$ is a $\sigma$-field. For a rectangle $A\times B$, each section is either the corresponding factor or the empty set, so every measurable rectangle lies in $\mathcal D$. Minimality of the generated $\sigma$-field gives

$$
\mathcal A\otimes\mathcal B\subseteq\mathcal D.
$$

No product measure or Tonelli theorem is used.

### Mesure de comptage

On $([0,1],\mathcal B([0,1]))$ define

$$
\#(C)=
\begin{cases}
\operatorname{card}(C),&C\text{ finite},\\
+\infty,&C\text{ infinite}.
\end{cases}
$$

Finite-$\#$ sets are finite. A countable union of finite sets is countable and therefore cannot cover the uncountable interval $[0,1]$; thus $\#$ is not $\sigma$-finite. Moreover $\lambda\ll\#$ because the only $\#$-null set is $\varnothing$. If $\lambda=f\#$, then testing each singleton gives $f(x)=0$ for every $x$, while testing $[0,1]$ gives $1=0$. The unavailable hypothesis in the stated RN theorem is the $\sigma$-finiteness of the dominating measure $\#$.

### Intégration atomique

If $A$ is finite, then $p\mathbf1_A$ is a nonnegative simple function and the finite simple-function identity gives

$$
\int_Ap\,d\#_E
=
\sum_{x\in A}p(x).
$$

If $A$ is countably infinite, choose a repetition-free enumeration $A=\{x_1,x_2,\ldots\}$ and define

$$
s_N=\sum_{n=1}^N p(x_n)\mathbf1_{\{x_n\}}.
$$

Then $s_N\uparrow p\mathbf1_A$ pointwise and

$$
\int s_N\,d\#_E
=
\sum_{n=1}^N p(x_n).
$$

Monotone convergence therefore yields

$$
\int_Ap\,d\#_E
=
\lim_{N\to\infty}\sum_{n=1}^Np(x_n)
=
\sum_{x\in A}p(x).
$$

## Partie I — Construction: normalized restriction

Because $\mathbb P(A)>0$, the map

$$
\mathbb P_A(C)=\frac{\mathbb P(C\cap A)}{\mathbb P(A)}
$$

is well defined. It vanishes at $\varnothing$, and for pairwise disjoint $(C_n)$ the sets $(C_n\cap A)$ are pairwise disjoint, so

$$
\mathbb P_A\left(\bigcup_nC_n\right)
=
\frac{\sum_n\mathbb P(C_n\cap A)}{\mathbb P(A)}
=
\sum_n\mathbb P_A(C_n).
$$

Also $\mathbb P_A(\Omega)=1$. Hence $\mathbb P_A$ is a probability measure on $(\Omega,\mathcal F)$.

If $\mathbb P(C)=0$, then $\mathbb P(C\cap A)=0$, so $\mathbb P_A\ll\mathbb P$. For every $C\in\mathcal F$,

$$
\int_C\frac{\mathbf1_A}{\mathbb P(A)}\,d\mathbb P
=
\frac{\mathbb P(C\cap A)}{\mathbb P(A)}
=
\mathbb P_A(C).
$$

Thus

$$
\frac{d\mathbb P_A}{d\mathbb P}
=
\frac{\mathbf1_A}{\mathbb P(A)}
\qquad
\mathbb P\text{-almost surely}.
$$

For $Y\in L^1(\mathbb P)$,

$$
\int |Y|\,d\mathbb P_A
=
\frac{\mathbb E[|Y|\mathbf1_A]}{\mathbb P(A)}
\le
\frac{\mathbb E[|Y|]}{\mathbb P(A)}
<\infty.
$$

Hence $Y\in L^1(\mathbb P_A)$ and

$$
\int Y\,d\mathbb P_A
=
\frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}
=
\mathbb E[Y\mid A].
$$

Here $\mathbb P_A$ is a measure, $\mathbb E[Y\mid A]$ is a scalar, and $\mathbb E[Y\mid\sigma(A)]$ is an $L^1$ equivalence class of random variables. If $0<\mathbb P(A)<1$, one representative is

$$
\mathbb E[Y\mid A]\mathbf1_A
+
\mathbb E[Y\mid A^c]\mathbf1_{A^c}.
$$

When $\mathbb P(A)=0$, the event-ratio construction divides by zero and defines neither $\mathbb P_A$ nor the scalar $\mathbb E[Y\mid A]$. The object $\mathbb E[Y\mid\sigma(A)]$ nevertheless remains well defined: for example,

$$
\mathbb E[Y]\mathbf1_{A^c}+c\mathbf1_A,
\qquad c\in\mathbb R,
$$

is a version, and the arbitrary coefficient lies on the null atom.

The RN numerator is $\mathbb P_A$, the reference measure is $\mathbb P$, the domain is $(\Omega,\mathcal F)$, and uniqueness is on a $\mathbb P$-almost-sure basis.

## Partie II — Représentation on a finite partition

Set

$$
I_+=\{i:\mathbb P(B_i)>0\},
\qquad
I_0=\{i:\mathbb P(B_i)=0\}.
$$

Every set in $\mathcal G=\sigma(B_1,\ldots,B_r)$ is a union of the partition atoms. If a real-valued $\mathcal G$-measurable function $Z$ took two distinct values at points of the same nonempty $B_i$, a Borel set separating those values would have a preimage in $\mathcal G$ containing one point of $B_i$ but not the other. No union of atoms has this property. Thus

$$
Z=\sum_{i=1}^r a_i\mathbf1_{B_i}
$$

for suitable constants $a_i$.

For $i\in I_+$, the defining conditional-expectation identity on $B_i$ requires

$$
a_i\mathbb P(B_i)
=
\int_{B_i}Z\,d\mathbb P
=
\int_{B_i}Y\,d\mathbb P
=
\mathbb E[Y\mathbf1_{B_i}],
$$

so

$$
a_i
=
\frac{\mathbb E[Y\mathbf1_{B_i}]}{\mathbb P(B_i)}.
$$

Choose arbitrary finite constants $c_i$ for $i\in I_0$ and define

$$
Z
=
\sum_{i\in I_+}
\frac{\mathbb E[Y\mathbf1_{B_i}]}{\mathbb P(B_i)}
\mathbf1_{B_i}
+
\sum_{i\in I_0}c_i\mathbf1_{B_i}.
$$

This finite sum is $\mathcal G$-measurable. Moreover,

$$
\mathbb E[|Z|]
\le
\sum_{i\in I_+}
\left|\mathbb E[Y\mathbf1_{B_i}]\right|
\le
\mathbb E[|Y|]
<\infty,
$$

because the null-atom terms integrate to zero. Hence $Z\in L^1(\mathbb P)$.

For arbitrary $C\in\mathcal G$, there is a set $J\subseteq\{1,\ldots,r\}$ such that $C=\bigcup_{i\in J}B_i$. Therefore

$$
\int_CZ\,d\mathbb P
=
\sum_{i\in J\cap I_+}
\mathbb E[Y\mathbf1_{B_i}]
=
\mathbb E\left[
Y\mathbf1_{\bigcup_{i\in J}B_i}
\right]
=
\int_CY\,d\mathbb P.
$$

Thus $Z$ is a version of $\mathbb E[Y\mid\mathcal G]$. On a null atom the defining identity is $0=0$, so the coefficient is undetermined. Any two choices differ only on a $\mathbb P$-null set and define the same $L^1$ class.

Taking expectations gives

$$
\mathbb E[Y]
=
\sum_{i\in I_+}
\mathbb E[Y\mid B_i]\mathbb P(B_i),
$$

where each event-ratio conditional mean is used only for $\mathbb P(B_i)>0$. With $Y=\mathbf1_D$,

$$
\mathbb P(D)
=
\sum_{i\in I_+}
\mathbb P(D\mid B_i)\mathbb P(B_i).
$$

The missing null-atom terms have joint mass zero.

Define $\nu_Y(C)=\mathbb E[Y\mathbf1_C]$ for $C\in\mathcal G$. Since $Y\in L^1(\mathbb P)$,

$$
\nu_Y=\nu_{Y^+}-\nu_{Y^-}
$$

is a finite signed measure on $(\Omega,\mathcal G)$. If $(\mathbb P|_{\mathcal G})(C)=0$, then $\nu_Y(C)=0$, so $\nu_Y\ll\mathbb P|_{\mathcal G}$. The reference measure $\mathbb P|_{\mathcal G}$ is finite; the signed Radon–Nikodym theorem therefore yields a density unique $\mathbb P$-almost surely. Thus the numerator finite signed measure is $\nu_Y$, the reference measure is $\mathbb P|_{\mathcal G}$, the domain is $(\Omega,\mathcal G)$, and

$$
\mathbb E[Y\mid\mathcal G]
=
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}.
$$

## Partie III — Transfert et défaut: Bayes from joint masses

Retain $I_+$ from Part II. For $i\in I_+$ set

$$
p_i=\mathbb P(B_i),
\qquad
q_i=\mathbb P(A\mid B_i).
$$

Part II applied to $Y=\mathbf1_A$ gives a version

$$
\mathbb E[\mathbf1_A\mid\mathcal G]
=
\sum_{i\in I_+}q_i\mathbf1_{B_i}
+
\sum_{i\notin I_+}c_i\mathbf1_{B_i},
$$

where the constants on null atoms are arbitrary. Taking expectations yields the total-probability marginal

$$
\mathbb P(A)
=
\sum_{i\in I_+}q_ip_i.
$$

For each $i\in I_+$, the corresponding joint mass is

$$
\mathbb P(A\cap B_i)=q_ip_i.
$$

If $\mathbb P(A)>0$, Part I now permits normalization. For $j\in I_+$,

$$
\mathbb P(B_j\mid A)
=
\mathbb P_A(B_j)
=
\frac{\mathbb P(A\cap B_j)}{\mathbb P(A)}
=
\frac{q_jp_j}{\sum_{i\in I_+}q_ip_i}.
$$

The numerator is a joint mass and the denominator is the total mass of the observed event. If $\mathbb P(A)=0$, posterior normalization is undefined. If a class $B_i$ is null, the event ratio $\mathbb P(A\mid B_i)$ is likewise undefined and must not be inserted into the formula.

When a continuously distributed $X$ satisfies $\mathbb P(X=x)=0$, the ratio

$$
\frac{\mathbb P(C\cap\{X=x\})}{\mathbb P(X=x)}
$$

does not define $\mathbb P(C\mid X=x)$. State-space versions or conditional kernels require a different construction and lie outside this séance.

## Partie IV — Application et inversion

The forward mixture map is

$$
m
=
u\alpha+v(1-\alpha)
=
v+(u-v)\alpha,
\qquad
0<\alpha<1.
$$

For

$$
u=\frac45,
\qquad
v=\frac3{10},
\qquad
m=\frac12,
$$

we have $u-v=1/2\ne0$, so the affine equation has at most one solution. It is

$$
\alpha
=
\frac{1/2-3/10}{4/5-3/10}
=
\frac25,
$$

which lies in $(0,1)$ and therefore keeps both event-ratio conditionals legitimate. Hence

$$
\mathbb P(B_2)=\frac35.
$$

The joint table is

|  | $A$ | $A^c$ | Total |
| --- | ---: | ---: | ---: |
| $B_1$ | $\frac8{25}$ | $\frac2{25}$ | $\frac25$ |
| $B_2$ | $\frac9{50}$ | $\frac{21}{50}$ | $\frac35$ |
| Total | $\frac12$ | $\frac12$ | $1$ |

Therefore

$$
\mathbb P(B_1\mid A)
=
\frac{\mathbb P(B_1\cap A)}{\mathbb P(A)}
=
\frac{8/25}{1/2}
=
\frac{16}{25}.
$$

The forward problem maps a prior $\alpha$ to the marginal $m$. The inverse-mixture problem recovers $\alpha$ only when the affine map is compatible and injective. Posterior normalization is a later operation on the already reconstructed joint law; it does not identify the prior by itself.

This original problem retains the Q370 structural reversal without reproducing an official statement or solution.

## Colle finale

### Test A — symbolic reconstruction

For $A\in\mathcal F$ with $\mathbb P(A)>0$,

$$
\mathbb P_A(C)
=
\frac{\mathbb P(C\cap A)}{\mathbb P(A)},
\qquad
\frac{d\mathbb P_A}{d\mathbb P}
=
\frac{\mathbf1_A}{\mathbb P(A)}
\quad\mathbb P\text{-a.s.}
$$

For a finite partition $(B_i)$, $Y\in L^1(\mathbb P)$ and $\mathcal G=\sigma(B_1,\ldots,B_r)$,

$$
\mathbb E[Y\mid\mathcal G]
=
\sum_{i\in I_+}
\frac{\mathbb E[Y\mathbf1_{B_i}]}{\mathbb P(B_i)}
\mathbf1_{B_i}
+
\sum_{i\in I_0}c_i\mathbf1_{B_i},
$$

where the $c_i$ are arbitrary finite constants. Measurability gives the atomwise form; testing positive atoms determines the first coefficients; every $C\in\mathcal G$ is a union of atoms, which verifies the full defining identity. Null-atom coefficients are invisible to the integrals and all choices are $\mathbb P$-almost surely equal.

For a positive-probability observed event $D$ and a positive-probability partition,

$$
\mathbb P(B_j\mid D)
=
\frac{\mathbb P(D\mid B_j)\mathbb P(B_j)}
{\sum_i\mathbb P(D\mid B_i)\mathbb P(B_i)}.
$$

The denominator is $\mathbb P(D)>0$.

### Test B — fresh numerical transfer

Because $\mathbb P(B_2)=2/3$, the joint masses are

$$
\mathbb P(A\cap B_1)
=
\frac13\cdot\frac34
=
\frac14,
$$

and

$$
\mathbb P(A\cap B_2)
=
\frac23\cdot\frac14
=
\frac16.
$$

Thus

$$
\mathbb P(A)
=
\frac14+\frac16
=
\frac5{12},
$$

and

$$
\mathbb P(B_1\mid A)
=
\frac{1/4}{5/12}
=
\frac35.
$$

## Critère de clôture

The opening question is retrieval only: clean / partial / absent neither determines the J3 verdict nor resolves the old rupture ledger. For the J3 proof, missing positivity, a wrong reference measure, verification only on atoms rather than arbitrary $C\in\mathcal G$, or ratio conditioning on a null event is a structural rupture. An isolated arithmetic slip after the correct joint-law construction is recorded separately.

The state reconstructible requires both parts of the colle finale without hints and all preceding theorem boundaries. This single session cannot promote the whole packet to deployable.
