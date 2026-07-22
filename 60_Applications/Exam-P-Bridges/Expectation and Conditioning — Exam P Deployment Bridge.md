---
type: application-bridge
module: applications
status: canonical
exam-snapshot: 2026-07
---

# Expectation and Conditioning — Exam P Deployment Bridge

This document translates the canonical measure-theoretic constructions into the computational forms used in Exam P. It does not replace the proofs in the formal modules.

The theoretical deployment has three function-space inputs:

$$
\begin{aligned}
L^1(\mathbb P)&\longrightarrow \text{finite expectations and finite signed RN numerators},\\
L^\infty(\mathbb P)&\longrightarrow \text{bounded payments and bounded tests},\\
L^2(\mathbb P)&\longrightarrow \text{second moments and integrable cross terms}.
\end{aligned}
$$

Because $\mathbb P$ is finite,

$$
L^\infty(\mathbb P)
\subseteq
L^2(\mathbb P)
\subseteq
L^1(\mathbb P).
$$

These inputs feed the representation chain

$$
\mathbb E[\varphi(X)]
\longleftrightarrow
X_\#\mathbb P
\longrightarrow
\text{product integration}
\longrightarrow
\text{conditioning}
\longrightarrow
\text{conditional density}.
$$

Radon–Nikodym is a representation engine inside this chain. It consumes a numerator measure, a reference measure, an absolute-continuity relation and the relevant theorem hypotheses. No $L^p$ embedding by itself produces an RN derivative. Exam questions are read in the opposite direction: identify the hidden measure, moment regime or transformation, then select the corresponding integral.

## 1. Expectation is an integral

Let $X:\Omega\to\overline{\mathbb R}$ be measurable.

- If $X\ge0$, then $\mathbb E[X]\in[0,+\infty]$ is defined.
- For general $X$, the expression

  $$
  \mathbb E[X]
  =
  \mathbb E[X^+]-\mathbb E[X^-]
  $$

  is defined provided the right-hand side is not $+\infty-+\infty$.
- If $X\in L^1(\mathbb P)$, then $\mathbb E[X]$ is finite.

Let $\mu_X=X_\#\mathbb P$. For every nonnegative measurable $\varphi$, and for every signed $\varphi$ for which the integral is defined,

$$
\boxed{
\mathbb E[\varphi(X)]
=
\int\varphi\,d\mu_X
}.
$$

If $\mu_X$ has density $f_X$ with respect to Lebesgue measure, this becomes

$$
\mathbb E[\varphi(X)]
=
\int\varphi(x)f_X(x)\,dx.
$$

The discrete sum and continuous integral are representations of the same pushforward identity, not separate definitions of expectation.

## 2. Tail integration and transformed payments

For $X\ge0$, Tonelli gives

$$
\boxed{
\mathbb E[X]
=
\int_0^\infty\mathbb P(X>t)\,dt
}.
$$

For $p>0$,

$$
\mathbb E[X^p]
=
p\int_0^\infty t^{p-1}\mathbb P(X>t)\,dt.
$$

Insurance payments are transformed random variables. Standard forms include

$$
(X-d)_+,
\qquad
X\wedge u,
\qquad
\min\{(X-d)_+,u\}.
$$

The correct object is

$$
\mathbb E[g(X)],
$$

not $g(\mathbb E[X])$. If $X\in L^1$, $g(X)\in L^1$ and $g$ is convex, Jensen gives $g(\mathbb E[X])\le\mathbb E[g(X)]$; the concave case reverses the inequality. It does not replace the expectation calculation.

## 3. Conditioning on events and finite partitions

For $B\in\mathcal F$ with $\mathbb P(B)>0$, define

$$
\mathbb P_B(A)
=
\frac{\mathbb P(A\cap B)}{\mathbb P(B)}.
$$

Then

$$
\frac{d\mathbb P_B}{d\mathbb P}
=
\frac{\mathbf1_B}{\mathbb P(B)}.
$$

If $B_1,\ldots,B_r$ is a measurable partition with $\mathbb P(B_i)>0$ and $\mathcal G=\sigma(B_1,\ldots,B_r)$, then for $Y\in L^1$,

$$
\boxed{
\mathbb E[Y\mid\mathcal G]
=
\sum_{i=1}^r
\frac{\mathbb E[Y\mathbf1_{B_i}]}{\mathbb P(B_i)}
\mathbf1_{B_i}
}.
$$

If a partition contains null atoms, their coefficients may be chosen arbitrarily; the conditional expectation is an almost-sure equivalence class.

For a partition $(B_i)$ and an event $A$,

$$
\mathbb P(A)
=
\sum_i\mathbb P(A\mid B_i)\mathbb P(B_i),
$$

and, whenever $\mathbb P(A)>0$,

$$
\mathbb P(B_j\mid A)
=
\frac{\mathbb P(A\mid B_j)\mathbb P(B_j)}
{\sum_i\mathbb P(A\mid B_i)\mathbb P(B_i)}.
$$

These are mixture and normalization identities.

## 4. Conditional expectation as Radon–Nikodym deployment

Let $Y\in L^1(\mathbb P)$ and let $\mathcal G\subseteq\mathcal F$ be a sub-$\sigma$-field. On $(\Omega,\mathcal G)$ define

$$
\nu_Y(A)=\mathbb E[Y\mathbf1_A].
$$

Then

$$
\boxed{
\mathbb E[Y\mid\mathcal G]
=
\frac{d\nu_Y}{d(\mathbb P|_{\mathcal G})}
}.
$$

For a random element $X$ with law $\mu_X$, push the numerator measure to the state space:

$$
\rho_Y(B)
=
\mathbb E[Y\mathbf1_{\{X\in B\}}].
$$

Then

$$
\boxed{
\mathbb E[Y\mid\sigma(X)]
=
\left(\frac{d\rho_Y}{d\mu_X}\right)(X)
}.
$$

The first derivative lives on $(\Omega,\mathcal G)$; the second lives on the state space of $X$. Their formulas cannot be interchanged without transporting the measures.

The relevant density contexts are recorded in [Density and Version Ledger](../../90_Review/Density%20and%20Version%20Ledger.md).

## 5. Total expectation and total variance

For $Y\in L^1(\mathbb P)$, the tower property gives

$$
\mathbb E[Y]
=
\mathbb E[\mathbb E[Y\mid\mathcal G]].
$$

If $Y\in L^2$, write

$$
Y-\mathbb E[Y]
=
\bigl(Y-\mathbb E[Y\mid\mathcal G]\bigr)
+
\bigl(\mathbb E[Y\mid\mathcal G]-\mathbb E[Y]\bigr).
$$

Set $H=\mathbb E[Y\mid\mathcal G]-\mathbb E[Y]\in L^2(\mathcal G)$. Apply the conditional-expectation test identity first to the bounded truncations of $H$, then pass to $H$ by $L^2$ convergence and Cauchy–Schwarz. The cross term has expectation zero. Hence

$$
\boxed{
\operatorname{Var}(Y)
=
\mathbb E[\operatorname{Var}(Y\mid\mathcal G)]
+
\operatorname{Var}(\mathbb E[Y\mid\mathcal G])
}.
$$

Here

$$
\operatorname{Var}(Y\mid\mathcal G)
:=
\mathbb E\!\left[
\left(Y-\mathbb E[Y\mid\mathcal G]\right)^2
\middle|
\mathcal G
\right].
$$

The $L^2$ assumption is not decorative: every displayed square must be integrable.

## 6. Dominated conditional densities

Suppose $(X,Z)$ has joint density $f_{X,Z}$ on $\mathbb R^d\times\mathbb R^m$. Tonelli gives

$$
f_X(x)
=
\int f_{X,Z}(x,z)\,dz.
$$

On $D_X=\{0<f_X<+\infty\}$, define

$$
k(x,z)
=
\frac{f_{X,Z}(x,z)}{f_X(x)}.
$$

Complete $k$ on $D_X^c$ with any fixed probability density. Then

$$
K(x,B)=\int_Bk(x,z)\,dz
$$

is an everywhere-defined probability kernel and

$$
K(X,B)
=
\mathbb E[\mathbf1_{\{Z\in B\}}\mid\sigma(X)]
$$

almost surely. In particular,

$$
\mathbb E[h(Z)\mid\sigma(X)]
=
\int h(z)k(X,z)\,dz
$$

for nonnegative $h$. If $h(Z)\in L^1$ is signed, the integral is absolutely finite for $\mu_X$-almost every state $x$; define it there and complete the resulting function, for example by zero, on the exceptional $\mu_X$-null set before composing with $X$.

Continuous conditional density is a transferable extension of the Exam P core. The July 2026 syllabus restricts its multivariate conditional and marginal outcomes to the discrete setting.

## 7. Official sample-question anchors

The following question numbers refer to the July 2026 snapshot of the [SOA Exam P Sample Questions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf). The problem statements are not reproduced here.

| Question | Hidden structural object | Required reversal |
| --- | --- | --- |
| Q50 | capped payment $g(X)=X\wedge u$ | identify the transformed variable, then compute $\mathbb E[g(X)]$ |
| Q386 | $g(N)=N(N+1)/2$ for a Poisson count | compute the required nonlinear moment, not $g(\mathbb E[N])$ |
| Q370 | finite mixture and Bayes inversion | form joint masses, normalize by the observed event |
| Q382 | conditional variance in a discrete joint model | normalize the relevant row or fiber before taking moments |

The [July 2026 Exam P syllabus](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf) determines the exam boundary; the measure-theoretic modules determine why the formulas are legitimate.

## 8. Reconstruction

A first-pass deployment is complete only if the following can be recovered without consultation:

1. the roles of $L^1$, $L^\infty$ and $L^2$, including why $L^2(\mathbb P)\subseteq L^1(\mathbb P)$ before conditional second moments are used;
2. expectation as an integral against a pushforward law;
3. the tail formula and its Tonelli regime;
4. conditioning on a positive-probability event as normalized restriction;
5. finite-partition conditional expectation;
6. conditional expectation as an RN density;
7. state-space transfer of that density;
8. marginalization and dominated conditional density;
9. the reference measure and almost-everywhere basis in every step.
