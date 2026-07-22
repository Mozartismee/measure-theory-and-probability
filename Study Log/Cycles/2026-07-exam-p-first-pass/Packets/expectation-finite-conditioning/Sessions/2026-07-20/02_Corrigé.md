---
type: study-session-corrige
date: 2026-07-20
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session: J3bis
solutions-policy: attempt-before-corrige
math-authority: derived
canonical-sources:
  - ../../../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 01 — RN Construction.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields.md
  - ../../../../../../../60_Applications/Exam-P-Bridges/Expectation and Conditioning — Exam P Deployment Bridge.md
---

# Corrigé — Feuille J3bis

This corrigé is independent of the working sheet. It is to be opened only after a complete written attempt, the exit and the Bilan.

## I. Normalized restriction and a finite $\sigma$-field

Let $A\in\mathcal F$ with $\mathbb P(A)>0$. Define

$$
\mathbb P_A(C)=\frac{\mathbb P(C\cap A)}{\mathbb P(A)},
\qquad C\in\mathcal F.
$$

Countable additivity follows from that of $\mathbb P$, and

$$
\mathbb P_A(\Omega)=1.
$$

Hence $\mathbb P_A$ is a probability measure. Moreover,

$$
\mathbb P_A(C)
=
\int_C\frac{\mathbf1_A}{\mathbb P(A)}\,d\mathbb P,
$$

so

$$
\frac{d\mathbb P_A}{d\mathbb P}
=
\frac{\mathbf1_A}{\mathbb P(A)}
\qquad\mathbb P\text{-almost surely}.
$$

For $Y\in L^1(\mathbb P)$,

$$
\int_\Omega |Y|\,d\mathbb P_A
=
\frac{\mathbb E[|Y|\mathbf1_A]}{\mathbb P(A)}
<\infty.
$$

Thus $Y\in L^1(\mathbb P_A)$ and

$$
\mathbb E_{\mathbb P_A}[Y]
=
\frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}
=:
\mathbb E[Y\mid A].
$$

If $\mathbb P(A)=0$, neither $\mathbb P_A$ nor the scalar ratio $\mathbb E[Y\mid A]$ is defined. The random variable $\mathbb E[Y\mid\sigma(A)]$ still exists: its value on the null set $A$ is arbitrary, while on $A^c$ it equals $\mathbb E[Y]$ almost surely.

Now let $(B_i)_{1\le i\le r}$ be a finite measurable partition and $\mathcal G=\sigma(B_1,\ldots,B_r)$. Every real-valued $\mathcal G$-measurable function is of the form

$$
Z=\sum_{i=1}^r c_i\mathbf1_{B_i}.
$$

For $p_i=\mathbb P(B_i)>0$, the defining identity on $B_i$ forces

$$
c_i
=
\frac{\mathbb E[Y\mathbf1_{B_i}]}{p_i}.
$$

If $p_i=0$, the coefficient $c_i$ may be any real number. Thus every version is

$$
\boxed{
\mathbb E[Y\mid\mathcal G]
=
\sum_{i:p_i>0}
\frac{\mathbb E[Y\mathbf1_{B_i}]}{p_i}\mathbf1_{B_i}
+
\sum_{i:p_i=0}c_i\mathbf1_{B_i}
}.
$$

This function is $\mathcal G$-measurable and integrable because

$$
\sum_{i:p_i>0}
\left|
\frac{\mathbb E[Y\mathbf1_{B_i}]}{p_i}
\right|p_i
\le
\sum_{i=1}^r\mathbb E[|Y|\mathbf1_{B_i}]
=
\mathbb E[|Y|].
$$

Every $C\in\mathcal G$ is a union of partition elements. Summing the identities on those elements gives

$$
\int_C\mathbb E[Y\mid\mathcal G]\,d\mathbb P
=
\int_CY\,d\mathbb P.
$$

Apply the formula to $Y=\mathbf1_D$. Summing the joint masses gives

$$
\mathbb P(D)
=
\sum_{i:p_i>0}\mathbb P(D\mid B_i)p_i.
$$

If $\mathbb P(D)>0$ and $p_j>0$, then

$$
\boxed{
\mathbb P(B_j\mid D)
=
\frac{\mathbb P(D\mid B_j)p_j}
{\sum_{i:p_i>0}\mathbb P(D\mid B_i)p_i}
}.
$$

At a null $B_i$, the likelihood ratio $\mathbb P(D\mid B_i)$ is undefined; at a null $D$, posterior normalization is undefined. The joint mass itself remains meaningful in both cases.

## II. Radon–Nikodym construction

Let $Y\in L^1_+(\mathbb P)$. On $(\Omega,\mathcal G)$ define

$$
\nu_Y(C)=\mathbb E[Y\mathbf1_C].
$$

For pairwise disjoint $(C_n)$ in $\mathcal G$, monotone convergence gives

$$
\nu_Y\left(\bigcup_nC_n\right)
=
\mathbb E\left[Y\sum_n\mathbf1_{C_n}\right]
=
\sum_n\nu_Y(C_n).
$$

Also

$$
\nu_Y(\Omega)=\mathbb E[Y]<\infty.
$$

Thus $\nu_Y$ is a finite positive measure. If $\mathbb P(C)=0$, then $Y\mathbf1_C=0$ almost surely, so $\nu_Y(C)=0$ and

$$
\nu_Y\ll\mathbb P|_{\mathcal G}.
$$

The permitted Radon–Nikodym theorem yields a nonnegative $\mathcal G$-measurable $Z$ such that

$$
\nu_Y(C)=\int_CZ\,d\mathbb P,
\qquad C\in\mathcal G.
$$

Taking $C=\Omega$ gives

$$
\mathbb E[Z]=\nu_Y(\Omega)=\mathbb E[Y]<\infty,
$$

so $Z\in L^1_+(\mathbb P)$ and $Z=\mathbb E[Y\mid\mathcal G]$.

For general $Y\in L^1(\mathbb P)$, apply the positive construction to $Y^+$ and $Y^-$. If the resulting densities are $Z^+$ and $Z^-$, set

$$
Z=Z^+-Z^-.
$$

Both terms are integrable; hence $Z\in L^1(\mathbb P)$, is $\mathcal G$-measurable, and satisfies

$$
\int_CZ\,d\mathbb P
=
\mathbb E[Y\mathbf1_C],
\qquad C\in\mathcal G.
$$

The ledger is therefore

| Object | Numerator | Reference measure | Measurable space | Uniqueness basis |
| --- | --- | --- | --- | --- |
| $\mathbb E[Y\mid\mathcal G]$ | $C\mapsto\mathbb E[Y\mathbf1_C]$ | $\mathbb P|_{\mathcal G}$ | $(\Omega,\mathcal G)$ | $\mathbb P|_{\mathcal G}$-a.e., equivalently $\mathbb P$-a.s. for $\mathcal G$-measurable versions |

## III. Test functions, uniqueness and contraction

The event identities imply the test identity first for $\mathcal G$-measurable simple functions by linearity. If $0\le H\le M$, choose nonnegative $\mathcal G$-measurable simple functions $H_n\to H$ pointwise with $0\le H_n\le M$. Since

$$
|H_nY|\le M|Y|,
\qquad
|H_nZ|\le M|Z|,
$$

dominated convergence gives

$$
\mathbb E[HY]=\mathbb E[HZ].
$$

Decompose a bounded signed $H$ into positive and negative parts. Conversely, take $H=\mathbf1_C$ to recover every event identity.

If $Z_1,Z_2$ are two candidates, then

$$
D=\{Z_1>Z_2\}\in\mathcal G
$$

and

$$
\int_D(Z_1-Z_2)\,d\mathbb P=0.
$$

The integrand is nonnegative, hence it vanishes almost surely. Therefore $\mathbb P(D)=0$. Exchanging $Z_1$ and $Z_2$ proves

$$
Z_1=Z_2
\qquad\mathbb P\text{-almost surely}.
$$

The positive construction and linearity give

$$
\mathbb E[|Y|\pm Y\mid\mathcal G]
=
\mathbb E[|Y|\mid\mathcal G]
\pm
\mathbb E[Y\mid\mathcal G]
\ge0.
$$

Hence

$$
\left|\mathbb E[Y\mid\mathcal G]\right|
\le
\mathbb E[|Y|\mid\mathcal G]
\quad\mathbb P\text{-almost surely}.
$$

Taking expectations yields

$$
\left\|\mathbb E[Y\mid\mathcal G]\right\|_1
\le
\mathbb E[\mathbb E[|Y|\mid\mathcal G]]
=
\mathbb E[|Y|]
=
\lVert Y\rVert_1.
$$

## IV. Calculus by uniqueness

Write $W=\mathbb E[Y\mid\mathcal G]$. If $H$ is bounded and $\mathcal G$-measurable, then $HW\in L^1$. For $C\in\mathcal G$, the bounded test identity applied to $H\mathbf1_C$ gives

$$
\mathbb E[\mathbf1_CHW]
=
\mathbb E[\mathbf1_CHY].
$$

Thus

$$
\mathbb E[HY\mid\mathcal G]
=
H\mathbb E[Y\mid\mathcal G]
\quad\mathbb P\text{-almost surely}.
$$

Now let $\mathcal H\subseteq\mathcal G$. For every $C\in\mathcal H$,

$$
\int_C\mathbb E[Y\mid\mathcal G]\,d\mathbb P
=
\int_CY\,d\mathbb P.
$$

Therefore both $\mathbb E[\mathbb E[Y\mid\mathcal G]\mid\mathcal H]$ and $\mathbb E[Y\mid\mathcal H]$ are $\mathcal H$-measurable integrable candidates with the same event identities. Uniqueness gives

$$
\mathbb E[\mathbb E[Y\mid\mathcal G]\mid\mathcal H]
=
\mathbb E[Y\mid\mathcal H].
$$

The remaining properties follow by the same legal pattern.

- A linear combination of two candidates is measurable, integrable and has the correct event integrals; this proves linearity.
- Positivity follows from the positive Radon–Nikodym construction, and monotonicity follows by applying positivity to $Y_2-Y_1$.
- If $Y$ is $\mathcal G$-measurable and integrable, then $Y$ itself satisfies the defining identities; this is the fixed-point property.
- Since an $\mathcal H$-measurable variable is also $\mathcal G$-measurable,

  $$
  \mathbb E[\mathbb E[Y\mid\mathcal H]\mid\mathcal G]
  =
  \mathbb E[Y\mid\mathcal H].
  $$

- Taking $C=\Omega$ gives preservation of the mean.
- If $Y$ is independent of $\mathcal G$, the constant $\mathbb E[Y]$ satisfies

  $$
  \mathbb E[Y\mathbf1_C]
  =
  \mathbb E[Y]\mathbb P(C),
  \qquad C\in\mathcal G,
  $$

  so $\mathbb E[Y\mid\mathcal G]=\mathbb E[Y]$ almost surely.

## V. Exam P transfer

The joint masses are

$$
\mathbb P(B_1\cap D)
=
\frac13\cdot\frac34
=
\frac14,
$$

$$
\mathbb P(B_2\cap D)
=
\frac23\cdot\frac14
=
\frac16.
$$

Therefore

$$
\mathbb P(D)=\frac14+\frac16=\frac5{12}
$$

and

$$
\boxed{
\mathbb P(B_1\mid D)
=
\frac{1/4}{5/12}
=
\frac35
}.
$$

The forward mixture forms the marginal $\mathbb P(D)$; posterior normalization divides one joint mass by that marginal.

Since $\mathcal G=\sigma(B_1,B_2)$,

$$
\mathbb E[Y\mid\mathcal G]
=
\mathbf1_{B_1}+4\mathbf1_{B_2},
$$

and

$$
\operatorname{Var}(Y\mid\mathcal G)
=
2\mathbf1_{B_1}+5\mathbf1_{B_2}.
$$

Let

$$
M=\mathbb E[Y\mid\mathcal G].
$$

Here $M$ is bounded and hence belongs to $L^2(\mathbb P)$. By definition,

$$
\operatorname{Var}(Y\mid\mathcal G)
=
\mathbb E[(Y-M)^2\mid\mathcal G].
$$

Since

$$
Y-\mathbb E[Y]
=
(Y-M)+(M-\mathbb E[Y]),
$$

Cauchy–Schwarz makes the cross term integrable, and the pull-out and tower properties give

$$
\begin{aligned}
\mathbb E[(Y-M)(M-\mathbb E[Y])]
&=
\mathbb E\!\left[
\mathbb E[(Y-M)(M-\mathbb E[Y])\mid\mathcal G]
\right]\\
&=
\mathbb E\!\left[
(M-\mathbb E[Y])
\mathbb E[Y-M\mid\mathcal G]
\right]
=0.
\end{aligned}
$$

Therefore

$$
\operatorname{Var}(Y)
=
\mathbb E[\operatorname{Var}(Y\mid\mathcal G)]
+
\operatorname{Var}(\mathbb E[Y\mid\mathcal G]).
$$

The tower property gives

$$
\mathbb E[Y]
=
\frac13\cdot1+\frac23\cdot4
=
3.
$$

Moreover,

$$
\mathbb E[\operatorname{Var}(Y\mid\mathcal G)]
=
\frac13\cdot2+\frac23\cdot5
=
4,
$$

while

$$
\operatorname{Var}(\mathbb E[Y\mid\mathcal G])
=
\frac13(1-3)^2+\frac23(4-3)^2
=
2.
$$

Hence

$$
\boxed{
\operatorname{Var}(Y)=4+2=6
}.
$$

The assumption $Y\in L^2(\mathbb P)$ guarantees that $Y^2$, the conditional second moment and every displayed square are integrable. It is not needed for total expectation.

## Model exit reconstruction

For $Y\in L^1(\mathbb P)$, a conditional expectation given $\mathcal G$ is an element $Z\in L^1(\Omega,\mathcal G,\mathbb P|_{\mathcal G})$ satisfying

$$
\int_CZ\,d\mathbb P
=
\int_CY\,d\mathbb P,
\qquad C\in\mathcal G.
$$

The construction is

$$
Y
\longmapsto
\nu_Y(C)=\mathbb E[Y\mathbf1_C]
\longmapsto
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
\longmapsto
\mathbb E[Y\mid\mathcal G],
$$

with positive and negative parts used when $Y$ is signed. Indicator tests extend to bounded $\mathcal G$-measurable tests by simple approximation and dominated convergence. The set $\{Z_1>Z_2\}$ gives almost-sure uniqueness. If $\mathcal H\subseteq\mathcal G$, the defining identities restricted to $\mathcal H$ give the tower property.

For a finite partition $(B_i)$, measurability determines the piecewise-constant form and the event identities determine the coefficients on positive-probability atoms. Coefficients on null atoms are arbitrary. Conditioning on a null event is not defined by an event ratio; outside $L^1$, the present signed finite-measure construction is unavailable; and a family of eventwise representatives does not by itself produce a probability kernel or a general disintegration.
