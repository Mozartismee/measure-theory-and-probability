---
type: study-session-corrige
date: 2026-07-21
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
session: J4
solutions-policy: attempt-before-corrige
math-authority: derived
canonical-sources:
  - ../../../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
---

# Corrigé — Feuille J4

This corrigé is independent of the working sheet. It is to be opened only after the complete written attempt, the exit and the Bilan have been fixed.

## Question de cours

For two $\sigma$-finite measure spaces, the product $\sigma$-field is

$$
\mathcal A\otimes\mathcal B
=
\sigma\bigl(\{A\times B:A\in\mathcal A,\ B\in\mathcal B\}\bigr).
$$

There exists a unique $\sigma$-finite measure $\mu\otimes\nu$ on it satisfying

$$
(\mu\otimes\nu)(A\times B)=\mu(A)\nu(B),
$$

with the convention $0\cdot(+\infty)=(+\infty)\cdot0=0$.

On the ring $\mathcal R$ of finite disjoint unions of measurable rectangles, set

$$
m_0\!\left(\bigsqcup_{j=1}^r A_j\times B_j\right)
=
\sum_{j=1}^r\mu(A_j)\nu(B_j).
$$

The construction interface is

$$
\text{well-defined premeasure on }\mathcal R
\longrightarrow
\text{Carathéodory extension to }\sigma(\mathcal R)
\longrightarrow
\sigma\text{-finite uniqueness}.
$$

If $E_n\uparrow E$ and $F_n\uparrow F$ have finite measure, then $E_n\times F_n$ exhausts $E\times F$ by sets of finite product measure; this is where $\sigma$-finiteness enters uniqueness. No outer-measure proof is required here.

## Problème

### 1. Measurable sections

Define

$$
\mathfrak S
=
\left\{
C\subseteq E\times F:
C_x\in\mathcal B\text{ for every }x\in E,
\quad
C^y\in\mathcal A\text{ for every }y\in F
\right\}.
$$

The empty set belongs to $\mathfrak S$. For every $x\in E$ and $y\in F$,

$$
(C^c)_x=F\setminus C_x,
\qquad
(C^c)^y=E\setminus C^y,
$$

and, for every sequence $(C_n)$,

$$
\left(\bigcup_nC_n\right)_x=\bigcup_n(C_n)_x,
\qquad
\left(\bigcup_nC_n\right)^y=\bigcup_nC_n^y.
$$

Hence $\mathfrak S$ is a $\sigma$-field. If $A\in\mathcal A$ and $B\in\mathcal B$, then

$$
(A\times B)_x
=
\begin{cases}
B,&x\in A,\\
\varnothing,&x\notin A,
\end{cases}
\qquad
(A\times B)^y
=
\begin{cases}
A,&y\in B,\\
\varnothing,&y\notin B.
\end{cases}
$$

Thus every measurable rectangle lies in $\mathfrak S$. By the minimality of the generated $\sigma$-field,

$$
\mathcal A\otimes\mathcal B\subseteq\mathfrak S.
$$

This proves the measurability of all sections. No product measure or integral identity has been used.

### 2(a). Indicator identity in the finite regime

Assume $\mu(E)<+\infty$ and $\nu(F)<+\infty$. Let $\mathfrak D$ consist of the sets $C\in\mathcal A\otimes\mathcal B$ such that $x\mapsto\nu(C_x)$ is measurable and

$$
(\mu\otimes\nu)(C)
=
\int_E\nu(C_x)\,\mu(dx).
$$

For a measurable rectangle $A\times B$,

$$
\nu((A\times B)_x)=\mathbf1_A(x)\nu(B),
$$

and therefore

$$
\int_E\nu((A\times B)_x)\,\mu(dx)
=
\mu(A)\nu(B)
=
(\mu\otimes\nu)(A\times B).
$$

Thus the generating $\pi$-system of measurable rectangles is contained in $\mathfrak D$.

If $C\in\mathfrak D$, then

$$
\nu((C^c)_x)=\nu(F)-\nu(C_x).
$$

The right-hand side is a finite-valued measurable function. Moreover,

$$
\begin{aligned}
\int_E\nu((C^c)_x)\,\mu(dx)
&=\mu(E)\nu(F)-\int_E\nu(C_x)\,\mu(dx)\\
&=(\mu\otimes\nu)(E\times F)-(\mu\otimes\nu)(C)\\
&=(\mu\otimes\nu)(C^c).
\end{aligned}
$$

The finiteness of $\mu(E)$ and $\nu(F)$ makes every subtraction above finite and prevents $+\infty-\infty$. Hence $C^c\in\mathfrak D$.

If $(C_n)$ is a pairwise disjoint sequence in $\mathfrak D$, then

$$
\nu\!\left(\left(\bigcup_nC_n\right)_x\right)
=
\sum_n\nu((C_n)_x).
$$

The partial sums are measurable and increase pointwise. Monotone convergence and countable additivity give

$$
\begin{aligned}
\int_E\nu\!\left(\left(\bigcup_nC_n\right)_x\right)\mu(dx)
&=\sum_n\int_E\nu((C_n)_x)\,\mu(dx)\\
&=\sum_n(\mu\otimes\nu)(C_n)\\
&=(\mu\otimes\nu)\!\left(\bigcup_nC_n\right).
\end{aligned}
$$

Therefore $\mathfrak D$ is a Dynkin system containing the generating $\pi$-system. The $\pi$-$\lambda$ theorem yields

$$
\mathfrak D=\mathcal A\otimes\mathcal B.
$$

Repeating the same argument with the variables exchanged gives

$$
(\mu\otimes\nu)(C)
=
\int_F\mu(C^y)\,\nu(dy).
$$

### 2(b). $\sigma$-finite localization

Choose increasing exhaustions $E_n\uparrow E$ and $F_n\uparrow F$ such that $\mu(E_n)<+\infty$ and $\nu(F_n)<+\infty$. Define

$$
\mu_n(A)=\mu(A\cap E_n),
\qquad
\nu_n(B)=\nu(B\cap F_n).
$$

The finite measures $\mu_n\otimes\nu_n$ and

$$
D\longmapsto(\mu\otimes\nu)(D\cap(E_n\times F_n))
$$

agree on every measurable rectangle. Uniqueness in the finite regime therefore identifies them. Applying the finite indicator identity to $C$ gives

$$
\int_E
\mathbf1_{E_n}(x)\nu(C_x\cap F_n)\,\mu(dx)
=
(\mu\otimes\nu)(C\cap(E_n\times F_n)).
$$

For every $x\in E$,

$$
\mathbf1_{E_n}(x)\nu(C_x\cap F_n)
\uparrow
\nu(C_x),
$$

while

$$
C\cap(E_n\times F_n)\uparrow C.
$$

The left-hand functions are measurable by the finite result. Monotone convergence on $E$ and continuity from below for $\mu\otimes\nu$ now yield

$$
(\mu\otimes\nu)(C)
=
\int_E\nu(C_x)\,\mu(dx).
$$

In particular, $x\mapsto\nu(C_x)$ is measurable as a pointwise limit of measurable functions. The symmetric localization gives

$$
(\mu\otimes\nu)(C)
=
\int_F\mu(C^y)\,\nu(dy).
$$

### 3. From indicators to Tonelli

Let

$$
s=\sum_{j=1}^r a_j\mathbf1_{C_j},
\qquad
 a_j>0,
\quad
C_j\in\mathcal A\otimes\mathcal B
\text{ pairwise disjoint},
$$

be a nonnegative simple function. For each $x$,

$$
\int_Fs(x,y)\,\nu(dy)
=
\sum_{j=1}^r a_j\nu((C_j)_x),
$$

which is measurable in $x$. Linearity and the indicator identity give

$$
\int_{E\times F}s\,d(\mu\otimes\nu)
=
\int_E\left(\int_Fs(x,y)\,\nu(dy)\right)\mu(dx),
$$

and symmetrically in the other order.

Now let $f:E\times F\to[0,+\infty]$ be product-measurable. Its sections are measurable: for fixed $x$ and $t\ge0$,

$$
\{y:f(x,y)>t\}=(\{f>t\})_x\in\mathcal B,
$$

and the other variable is symmetric. Choose nonnegative simple functions $s_n\uparrow f$. For every $x$, monotone convergence on $F$ gives

$$
\int_Fs_n(x,y)\,\nu(dy)
\uparrow
\int_Ff(x,y)\,\nu(dy).
$$

Thus the limiting section integral is measurable. Monotone convergence on $E\times F$ and then on $E$ gives

$$
\begin{aligned}
\int_{E\times F}f\,d(\mu\otimes\nu)
&=\lim_n\int_{E\times F}s_n\,d(\mu\otimes\nu)\\
&=\lim_n\int_E\left(\int_Fs_n(x,y)\,\nu(dy)\right)\mu(dx)\\
&=\int_E\left(\int_Ff(x,y)\,\nu(dy)\right)\mu(dx).
\end{aligned}
$$

The symmetric argument proves the reversed iterated identity. This is Tonelli's theorem.

### 4. Boundary

Positivity is decisive. Every quantity in Tonelli's theorem lies in $[0,+\infty]$, so equality remains meaningful when the common value is $+\infty$; no subtraction occurs.

For a signed measurable function, the positive and negative parts may both have infinite integral. Subtracting their Tonelli identities would then produce the undefined expression $+\infty-\infty$. If instead

$$
\int_{E\times F}|f|\,d(\mu\otimes\nu)<+\infty,
$$

Tonelli applied to $|f|$ supplies almost-everywhere section integrability, and Fubini may then be invoked. Without that absolute-integrability hypothesis, no exchange for a signed function has been authorized.

## Épreuve de sortie

The first requested proof is the argument of §1, reproduced without notes. Applied to $(S,\mathscr S)$ and $((0,+\infty),\mathcal B((0,+\infty)))$, it uses the $\sigma$-field of sets whose two families of sections are measurable, the rectangle computation and generated-$\sigma$-field minimality.

To prove that $H_g$ is product-measurable without invoking a comparison theorem, use the countable representation

$$
H_g
=
\bigcup_{q\in\mathbb Q_{>0}}
\{g>q\}\times(0,q).
$$

Indeed, if $0<t<g(s)$, a rational $q$ can be chosen with $t<q<g(s)$; the converse is immediate. Each set in the union is a measurable rectangle.

For $s\in S$ and $t>0$,

$$
(H_g)_s=(0,g(s)),
\qquad
H_g^t=\{s:g(s)>t\},
$$

where $(0,+\infty)$ is understood when $g(s)=+\infty$. Therefore

$$
\lambda((H_g)_s)=g(s),
\qquad
\rho(H_g^t)=\rho(g>t).
$$

Tonelli applied to the nonnegative measurable function $\mathbf1_{H_g}$ yields

$$
\begin{aligned}
\int_S g\,d\rho
&=\int_S\left(\int_0^\infty\mathbf1_{H_g}(s,t)\,dt\right)\rho(ds)\\
&=\int_{S\times(0,+\infty)}\mathbf1_{H_g}\,d(\rho\otimes\lambda)\\
&=\int_0^\infty\left(\int_S\mathbf1_{H_g}(s,t)\,\rho(ds)\right)dt\\
&=\int_0^\infty\rho(g>t)\,dt.
\end{aligned}
$$

Both sides are nonnegative extended integrals, so the identity remains meaningful when their common value is $+\infty$.

## Prolongement facultatif

This section answers the [optional prolongement](03_Prolongement%20facultatif.md). It is independent of the verdict of the timed séance.

Set

$$
h(x,y)=\min\{u(x),v(y)\}.
$$

For every $t\ge0$,

$$
\{h>t\}
=
\{u>t\}\times\{v>t\}.
$$

This is a measurable rectangle. Hence $h$ is $\mathcal A\otimes\mathcal B$-measurable. Since $\mu$ and $\nu$ are $\sigma$-finite, so is $\mu\otimes\nu$. Applying the tail-integral identity on $(E\times F,\mathcal A\otimes\mathcal B,\mu\otimes\nu)$ gives

$$
\begin{aligned}
\int_{E\times F}h\,d(\mu\otimes\nu)
&=
\int_0^\infty(\mu\otimes\nu)(h>t)\,dt\\
&=
\int_0^\infty\mu(u>t)\nu(v>t)\,dt.
\end{aligned}
$$

The rectangle prescription uses the convention

$$
0\cdot(+\infty)=(+\infty)\cdot0=0.
$$

All functions are nonnegative, so Tonelli and the tail-integral identity take values in $[0,+\infty]$; the common value may equal $+\infty$.

Now let $X$ and $Y$ be independent nonnegative random variables. Independence identifies their joint law with $\mu_X\otimes\mu_Y$. Applying the preceding formula to the coordinate maps yields

$$
\mathbb E[\min\{X,Y\}]
=
\int_0^\infty
\mathbb P(X>t)\mathbb P(Y>t)\,dt.
$$

Since $\min\{X,Y\}\le X$ and $\min\{X,Y\}\le Y$, finiteness of either $\mathbb E[X]$ or $\mathbb E[Y]$ is sufficient. It is not necessary. Let $U,V$ be independent uniform random variables on $(0,1)$ and set

$$
X=U^{-4/3}-1,
\qquad
Y=V^{-4/3}-1.
$$

Then, for $t\ge0$,

$$
\mathbb P(X>t)=\mathbb P(Y>t)=(1+t)^{-3/4}.
$$

Consequently,

$$
\mathbb E[X]
=
\int_0^\infty(1+t)^{-3/4}\,dt
=+\infty,
$$

and likewise $\mathbb E[Y]=+\infty$, whereas

$$
\mathbb E[\min\{X,Y\}]
=
\int_0^\infty(1+t)^{-3/2}\,dt
<+\infty.
$$

Thus marginal integrability is sufficient but not necessary; the exact criterion is the finiteness of the product-tail integral.
