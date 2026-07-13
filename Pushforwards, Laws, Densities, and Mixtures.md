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

If

$$
X_\#\mathbb P=Y_\#\mathbb Q,
$$

then, for every admissible measurable $\varphi$,

$$
\int_\Omega \varphi(X)\,d\mathbb P
=
\int_{\Omega'}\varphi(Y)\,d\mathbb Q.
$$

In particular, whenever finite,

$$
\mathbb E[X^k]=\mathbb E[Y^k].
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

If

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

In particular,

$$
\mathbb E[X]
=
\int_{\mathbb R}x f_X(x)\,dx,
$$

and

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

Then $\mu$ is a probability measure, and for every nonnegative measurable or integrable $\varphi$,

$$
\int_S\varphi\,d\mu
=
\alpha\int_S\varphi\,d\mu_1
+
(1-\alpha)\int_S\varphi\,d\mu_2.
$$

---

## Corollary 3 — Mixture Densities

Assume

$$
\mu_i\ll\lambda,
\qquad
f_i=\frac{d\mu_i}{d\lambda},
\quad i=1,2.
$$

Then

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

Let $\mu_1,\mu_2$ be probability measures on $\mathbb R$ with finite second moments. Set

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
(\{1\}\times S)\sqcup(\{2\}\times S),
$$

define

$$
\mathbb P(\{1\}\times A)
=
\alpha\mu_1(A),
$$

$$
\mathbb P(\{2\}\times A)
=
(1-\alpha)\mu_2(A),
$$

and set

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

$$
X
\longmapsto
\mu_X=X_\#\mathbb P
\longmapsto
f_X=\frac{d\mu_X}{d\lambda}
$$

with the last arrow available only when

$$
\mu_X\ll\lambda.
$$

The corresponding integration chain is

$$
\int_\Omega \varphi(X)\,d\mathbb P
=
\int_S\varphi\,d\mu_X
=
\int_S\varphi f_X\,d\lambda,
$$

whenever the density representation exists.

---

# Exercises

## Exercise 1 — Pushforward Formula

Let

$$
X:(\Omega,\mathcal F,\mathbb P)\to(S,\Sigma)
$$

be measurable.

Prove the pushforward integration formula

$$
\int_\Omega\varphi\circ X\,d\mathbb P
=
\int_S\varphi\,d\mu_X
$$

for every nonnegative measurable $\varphi$.

Your proof must explicitly pass through:

$$
\text{indicators}
\to
\text{simple functions}
\to
\text{nonnegative measurable functions}.
$$

---

## Exercise 2 — Equality in Law

Let $X$ and $Y$ be real-valued random variables, possibly defined on different probability spaces, and assume

$$
\mu_X=\mu_Y.
$$

Prove that, whenever finite,

$$
\mathbb E[|X|^p]
=
\mathbb E[|Y|^p]
$$

for every $p>0$.

Show also that

$$
\mathbb P(X\le t)
=
\mathbb P(Y\le t)
$$

for every $t\in\mathbb R$.

---

## Exercise 3 — Density Is Not a Measure

Let

$$
f(x)=2x\mathbf 1_{[0,1]}(x).
$$

1. Show that $f$ is a probability density.
2. Define the corresponding probability measure $\mu$.
3. Compute

$$
\mu([0,a])
$$

for $a\in[0,1]$.
4. Explain precisely why $f$ itself is not a measure on $\mathcal B(\mathbb R)$.

---

## Exercise 4 — Mixture of Densities

Let

$$
f_1(x)=e^{-x}\mathbf 1_{(0,\infty)}(x),
$$

and

$$
f_2(x)=2e^{-2x}\mathbf 1_{(0,\infty)}(x).
$$

Define

$$
f=\frac12f_1+\frac12f_2.
$$

1. Prove that $f$ is a probability density.
2. Compute

$$
\mathbb E[X]
$$

and

$$
\mathbb E[X^2].
$$

3. Deduce

$$
\operatorname{Var}(X).
$$

4. Verify the mixture variance formula directly.

---

## Exercise 5 — Variance Defect

Let

$$
\mu=\alpha\mu_1+(1-\alpha)\mu_2,
$$

where both component measures have finite second moments.

Prove that

$$
\operatorname{Var}_\mu
-
\left[
\alpha\operatorname{Var}_{\mu_1}
+
(1-\alpha)\operatorname{Var}_{\mu_2}
\right]
=
\alpha(1-\alpha)(m_1-m_2)^2.
$$

Determine exactly when equality holds between the mixture variance and the weighted average of component variances.

---

## Exercise 6 — Same Marginals, Different Joint Laws

Construct two pairs of random variables

$$
(X_1,X_2)
$$

and

$$
(Y_1,Y_2)
$$

such that

$$
\mu_{X_1}=\mu_{Y_1},
\qquad
\mu_{X_2}=\mu_{Y_2},
$$

but

$$
\mu_{X_1+X_2}
\neq
\mu_{Y_1+Y_2}.
$$

Interpret the result as evidence that marginal laws do not determine joint operations.

Hint: use Bernoulli random variables with different dependence structures.

---

## Exercise 7 — Mixture Realization by a Selector

Let $I$ be Bernoulli with

$$
\mathbb P(I=1)=\alpha,
\qquad
\mathbb P(I=2)=1-\alpha.
$$

Suppose that conditionally on $I=i$, the random variable $X$ has law $\mu_i$.

Prove that

$$
\mu_X
=
\alpha\mu_1+(1-\alpha)\mu_2.
$$

Then derive

$$
\mathbb E[\varphi(X)]
=
\alpha\int\varphi\,d\mu_1
+
(1-\alpha)\int\varphi\,d\mu_2.
$$

---

## Exercise 8 — Singular Law

Let $X$ be uniformly distributed on the Cantor set with respect to the standard Cantor probability measure.

1. Explain why $\mu_X$ is a probability measure on $\mathbb R$.
2. State why $\mu_X$ does not admit a density with respect to Lebesgue measure.
3. Explain why the pushforward integration formula remains valid even without a pdf.

The point is to separate the law from one particular representation of the law.