---
type: td
module: pushforwards-and-laws
status: canonical
---

# TD 01 — Laws, Densities, and Mixtures

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

where $\alpha\in[0,1]$ and both component measures have finite second moments.

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

Let $\alpha\in(0,1)$, and let $I$ be a $\{1,2\}$-valued random variable with

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
