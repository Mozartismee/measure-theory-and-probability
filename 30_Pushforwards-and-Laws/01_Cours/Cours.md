---
type: cours
module: pushforwards-and-laws
status: canonical
---

# Pushforwards, Laws, Densities, and Mixtures

## Setting

Let

$$
X:(\Omega,\mathcal F,\mathbb P)\to(S,\Sigma)
$$

be measurable. Its law is the pushforward measure

$$
\mu_X:=X_\#\mathbb P,
\qquad
\mu_X(A):=\mathbb P(X^{-1}(A)),
\quad A\in\Sigma.
$$

---

## Proposition 1 — Pushforward Integration

The complete proof is isolated in [Pushforward Integration Formula](Pushforward%20Integration%20Formula.md).

For every measurable $\varphi:S\to[0,\infty]$,

$$
\int_\Omega \varphi\circ X\,d\mathbb P
=
\int_S \varphi\,d\mu_X.
$$

The same identity holds for every $\mu_X$-integrable real-valued $\varphi$.

#### Proof skeleton

Prove successively for

$$
\mathbf 1_A
\longrightarrow
\text{nonnegative simple functions}
\longrightarrow
\text{nonnegative measurable functions}
\longrightarrow
\text{integrable functions}.
$$

For $\varphi=\mathbf 1_A$,

$$
\int_\Omega \mathbf 1_A(X)\,d\mathbb P
=
\mathbb P(X^{-1}(A))
=
\mu_X(A)
=
\int_S\mathbf 1_A\,d\mu_X.
$$

---

## Corollary 1 — Expectations Depend Only on the Law

Let $(\Omega',\mathcal F',\mathbb Q)$ be a probability space and let

$$
Y:(\Omega',\mathcal F',\mathbb Q)\to(S,\Sigma)
$$

be measurable. If

$$
X_\#\mathbb P=Y_\#\mathbb Q,
$$

then, for every admissible measurable $\varphi$,

$$
\int_\Omega \varphi(X)\,d\mathbb P
=
\int_{\Omega'}\varphi(Y)\,d\mathbb Q.
$$

If $S=\mathbb R$, then for every integer $k\ge1$ such that $x\mapsto x^k$ is $\mu_X$-integrable,

$$
\mathbb E_{\mathbb P}[X^k]
=
\mathbb E_{\mathbb Q}[Y^k].
$$

Thus the concrete realization of a random variable may change while all law-determined quantities remain unchanged.

---

## Proposition 2 — Density Representation

Let $\lambda$ be Lebesgue measure on $\mathbb R$, and let $\mu$ be a probability measure on $\mathbb R$.

If

$$
\mu\ll\lambda,
$$

then there exists a measurable function

$$
f:\mathbb R\to[0,\infty)
$$

such that

$$
\mu(A)=\int_A f\,d\lambda
$$

for every Borel set $A$. Moreover,

$$
f=\frac{d\mu}{d\lambda}
$$

is unique $\lambda$-a.e., and

$$
\int_{\mathbb R}f\,d\lambda=1.
$$

Hence a pdf is not a measure. It is a Radon–Nikodym derivative of a measure with respect to a reference measure.

---

## Corollary 2 — Density Form of Expectation

Assume $S=\mathbb R$. If

$$
\mu_X\ll\lambda,
\qquad
f_X=\frac{d\mu_X}{d\lambda},
$$

then

$$
\mathbb E[\varphi(X)]
=
\int_{\mathbb R}\varphi(x)f_X(x)\,dx
$$

for every admissible measurable $\varphi$.

In particular, if $X\in L^1(\mathbb P)$,

$$
\mathbb E[X]
=
\int_{\mathbb R}x f_X(x)\,dx,
$$

and, if $X\in L^2(\mathbb P)$,

$$
\mathbb E[X^2]
=
\int_{\mathbb R}x^2 f_X(x)\,dx.
$$

The symbol $x$ is a bound variable on the state space. It is not the random variable $X$.

Equivalently, with the coordinate map

$$
\iota:\mathbb R\to\mathbb R,
\qquad
\iota(t)=t,
$$

one has

$$
\mathbb E[X]
=
\int_{\mathbb R}\iota\,d\mu_X.
$$

---

## Proposition 3 — Convex Mixtures of Measures

Let $\mu_1,\mu_2$ be probability measures on $(S,\Sigma)$, and let $\alpha\in[0,1]$. Define

$$
\mu:=\alpha\mu_1+(1-\alpha)\mu_2.
$$

Then $\mu$ is a probability measure. For every nonnegative measurable $\varphi$,

$$
\int_S\varphi\,d\mu
=
\alpha\int_S\varphi\,d\mu_1
+
(1-\alpha)\int_S\varphi\,d\mu_2.
$$

Here the endpoint cases use the convention

$$
0\cdot(+\infty)=0.
$$

The same identity holds, with all terms finite, for every real-valued measurable

$$
\varphi\in L^1(\mu_1)\cap L^1(\mu_2).
$$

---

## Corollary 3 — Mixture Densities

In the setting of Proposition 3, assume $S=\mathbb R$, let $\lambda$ denote Lebesgue measure, and suppose

$$
\mu_i\ll\lambda,
\qquad
f_i=\frac{d\mu_i}{d\lambda},
\quad i=1,2.
$$

Then the mixture defined above,

$$
\mu:=\alpha\mu_1+(1-\alpha)\mu_2
$$

satisfies

$$
\mu\ll\lambda
$$

and

$$
\frac{d\mu}{d\lambda}
=
\alpha f_1+(1-\alpha)f_2
\quad\lambda\text{-a.e.}
$$

Thus mixture formation is linear at the level of measures and densities.

---

## Proposition 4 — Mean and Variance of a Mixture

Let $\mu_1,\mu_2$ be probability measures on $\mathbb R$ with finite second moments, and let $\alpha\in[0,1]$. Set

$$
m_i:=\int_{\mathbb R}x\,d\mu_i(x),
$$

and

$$
\sigma_i^2:=\int_{\mathbb R}(x-m_i)^2\,d\mu_i(x).
$$

For

$$
\mu:=\alpha\mu_1+(1-\alpha)\mu_2,
$$

the mean is

$$
m
=
\alpha m_1+(1-\alpha)m_2,
$$

and the variance is

$$
\operatorname{Var}_\mu
=
\alpha\sigma_1^2
+
(1-\alpha)\sigma_2^2
+
\alpha(1-\alpha)(m_1-m_2)^2.
$$

Hence, in general,

$$
\operatorname{Var}_\mu
\neq
\alpha\operatorname{Var}_{\mu_1}
+
(1-\alpha)\operatorname{Var}_{\mu_2}.
$$

The defect is the between-component term

$$
\alpha(1-\alpha)(m_1-m_2)^2.
$$

---

## Lemma 5 — Realization of a Mixture Law

Let $\mu_1,\mu_2$ be probability measures on $(S,\Sigma)$, and let $\alpha\in[0,1]$.

There exists a probability space and an $S$-valued random variable $X$ such that

$$
\mu_X
=
\alpha\mu_1+(1-\alpha)\mu_2.
$$

### Construction

Take

$$
\Omega
=
\{1,2\}\times S,
\qquad
\mathcal F_\Omega
=
2^{\{1,2\}}\otimes\Sigma.
$$

For $E\in\mathcal F_\Omega$, write

$$
E_i
=
\{s\in S:(i,s)\in E\},
\qquad i=1,2,
$$

and define

$$
\mathbb P(E)
=
\alpha\mu_1(E_1)
+
(1-\alpha)\mu_2(E_2).
$$

Then $\mathbb P$ is a probability measure on $(\Omega,\mathcal F_\Omega)$; set

$$
X(i,s)=s.
$$

Then

$$
X_\#\mathbb P
=
\alpha\mu_1+(1-\alpha)\mu_2.
$$

---

## Boundary Principle — Law-Level and Random-Variable-Level Operations

If

$$
X_1:\Omega_1\to\mathbb R,
\qquad
X_2:\Omega_2\to\mathbb R,
$$

then their laws

$$
\mu_{X_1},
\qquad
\mu_{X_2}
$$

may be combined directly, since both are measures on the same state space.

Thus

$$
\alpha\mu_{X_1}+(1-\alpha)\mu_{X_2}
$$

is well-defined.

By contrast,

$$
X_1+X_2,
\qquad
X_1X_2,
\qquad
\operatorname{Cov}(X_1,X_2)
$$

are not defined unless $X_1$ and $X_2$ are placed on a common probability space.

Marginal laws determine law-level quantities, but not joint operations.

---

## Structural Chain

Let $m$ be a $\sigma$-finite measure on $(S,\Sigma)$. Whenever $\mu_X\ll m$, the chain is

$$
X
\longmapsto
\mu_X=X_\#\mathbb P
\longmapsto
f_X=\frac{d\mu_X}{dm}.
$$

The last arrow is available only under the displayed absolute-continuity hypothesis. The corresponding integration chain is

$$
\int_\Omega \varphi(X)\,d\mathbb P
=
\int_S\varphi\,d\mu_X
=
\int_S\varphi f_X\,dm,
$$

for every nonnegative measurable $\varphi$, and for every signed measurable $\varphi$ whenever the integrals are defined.
