---
type: study-packet-corrige
start: 2026-07-17
end: 2026-07-19
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
access-policy: after-complete-attempt
math-authority: derived
canonical-sources:
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Pushforward Integration Formula.md
  - ../../../../../35_Product-Measures-and-Transformations/03_Corriges/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../40_Conditional-Expectation/03_Corriges/TD 02 — Finite Sigma-Fields.md
---

# Corrigé — Expectation and Finite Conditioning

Do not read this file before a complete attempt. Use it to locate the first illegal step; do not replace the rupture record with a cleaner solution.

## Exercise 0

Since $\mathbb P(\Omega)=1$ and $q>1$, the finite-measure embedding gives

$$
\|Y\|_1
\le
\|Y\|_q,
$$

so $Y\in L^1(\mathbb P)$. The numerator is the restriction of the finite signed measure $Y\mathbb P$ to $(\Omega,\mathcal G)$, the reference measure is $\mathbb P|_{\mathcal G}$, and both live on $(\Omega,\mathcal G)$. Moreover,

$$
|\nu_Y^{\mathcal G}|(\Omega)
\le
\mathbb E[|Y|]
<+\infty,
$$

and $\mathbb P(A)=0$ implies $\nu_Y^{\mathcal G}(A)=0$. The signed Radon–Nikodym theorem therefore gives a $\mathcal G$-measurable $H\in L^1(\mathbb P|_{\mathcal G})$ such that

$$
\nu_Y^{\mathcal G}(A)
=
\int_AH\,d\mathbb P,
\qquad A\in\mathcal G,
$$

with $H$ unique $\mathbb P$-almost surely. This $H$ is $\mathbb E[Y\mid\mathcal G]$.

For a random element $X$, LOTUS is the pushforward integration identity for the measure $\mu_X=X_\#\mathbb P$ and therefore needs no dominating Lebesgue measure. A formula involving $f_X$ additionally requires $\mu_X\ll\lambda$; only then does Radon–Nikodym provide $f_X=d\mu_X/d\lambda$, unique $\lambda$-almost everywhere.

## Exercise 1

For $C\in\mathcal S$,

$$
\mathbb E[\mathbf1_C(X)]
=
\mathbb P(X\in C)
=
\mu_X(C).
$$

Linearity gives the formula for nonnegative simple functions. For $\varphi_n\uparrow\varphi$, monotone convergence applies both on $\Omega$ and on $S$. Signed functions follow by applying the nonnegative result to $\varphi^+$ and $\varphi^-$ whenever their difference is defined.

On $(0,1)$ with Lebesgue measure, $X(t)=1/t$ is nonnegative with infinite expectation. On $\mathbb R$ with a symmetric Cauchy law, $X^+$ and $X^-$ both have infinite expectation, so $\mathbb E[X]$ is undefined.

If $\mu_X$ is atomic, integration against $\mu_X$ is a weighted sum. If $\mu_X\ll\lambda$ with density $f_X$, the same integral is represented as $\int\varphi(x)f_X(x)\,dx$. Neither representation changes the definition of expectation.

## Exercise 2

The tail formula was established in the formal Product Measures TD. Apply it to $(X-d)_+$ and $X\wedge u$ to obtain

$$
\mathbb E[(X-d)_+]
=
\int_d^\infty\mathbb P(X>t)\,dt,
$$

and

$$
\mathbb E[X\wedge u]
=
\int_0^u\mathbb P(X>t)\,dt.
$$

If $X\sim\operatorname{Exp}(\lambda)$, these equal

$$
\frac{e^{-\lambda d}}{\lambda}
\quad\text{and}\quad
\frac{1-e^{-\lambda u}}{\lambda}.
$$

Also,

$$
\mathbb E[\min\{(X-d)_+,u\}]
=
\int_d^{d+u}\mathbb P(X>t)\,dt.
$$

For convex $g$ with $X\in L^1$ and $g(X)\in L^1$, Jensen gives $g(\mathbb E[X])\le\mathbb E[g(X)]$. It supplies a bound, not the value of the latter integral.

## Exercise 3

Every $\mathcal G=\sigma(B_1,\ldots,B_r)$-measurable random variable has the form $\sum_ic_i\mathbf1_{B_i}$. Testing on $B_j$ gives

$$
c_j\mathbb P(B_j)
=
\mathbb E[Y\mathbf1_{B_j}],
$$

which determines $c_j$ when $\mathbb P(B_j)>0$. Taking expectations gives

$$
\mathbb E[Y]
=
\sum_i\mathbb P(B_i)\mathbb E[Y\mid B_i].
$$

On a null atom, $c_i$ is arbitrary. For $Y=\mathbf1_A$, the same formula is the law of total probability.

## Exercise 4

Since

$$
\mathbb P(A\cap B_i)
=
\mathbb P(A\mid B_i)\mathbb P(B_i),
$$

division by

$$
\mathbb P(A)=\sum_i\mathbb P(A\mid B_i)\mathbb P(B_i)
$$

gives Bayes' formula. For $C\in\mathcal F$,

$$
\mathbb P_A(C)
=
\int_C\frac{\mathbf1_A}{\mathbb P(A)}\,d\mathbb P,
$$

so $d\mathbb P_A/d\mathbb P=\mathbf1_A/\mathbb P(A)$, uniquely $\mathbb P$-almost surely. If $X$ has a continuous law, $\mathbb P(X=x)=0$ for each $x$; the event-ratio denominator vanishes, so a conditional density or kernel version is required instead.

For the two ledger rows, the complete data are:

| Representative | Numerator measure | Reference measure | Domain | Uniqueness |
| --- | --- | --- | --- | --- |
| $d\mathbb P_A/d\mathbb P$ | $C\mapsto\mathbb P(C\cap A)/\mathbb P(A)$ | $\mathbb P$ | $(\Omega,\mathcal F)$ | $\mathbb P$-a.s. |
| $\mathbb E[Y\mid\mathcal G]$, $\mathcal G=\sigma(B_1,\ldots,B_r)$ | $C\mapsto\mathbb E[Y\mathbf1_C]$, $C\in\mathcal G$ | $\mathbb P|_{\mathcal G}$ | $(\Omega,\mathcal G)$ | $\mathbb P$-a.s. |
