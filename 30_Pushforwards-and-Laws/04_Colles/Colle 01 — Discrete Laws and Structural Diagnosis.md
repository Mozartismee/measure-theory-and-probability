---
type: colle
module: pushforwards-and-laws
status: canonical
exam-snapshot: 2026-07
---

# Colle 01 — Discrete Laws and Structural Diagnosis

Each sujet is designed for fifteen minutes of preparation and fifteen minutes of exposition. State the objects before calculating. A family name without its construction does not count as an answer.

---

## Sujet A — Atomic density and the Radon–Nikodym boundary

Let $E$ be countable and let $\mu$ be a probability measure on $(E,2^E)$.

1. State and prove the representation of $\mu$ with respect to counting measure.
2. Derive the integration formula for a nonnegative function $\varphi:E\to[0,\infty]$.
3. Explain the meaning and uniqueness basis of the pmf.

### Relances

- What changes if $E$ is uncountable?
- Give an example of $\nu\ll\#$ for which no Radon–Nikodym density exists.
- Why does a probability density with respect to counting measure have pointwise rather than merely almost-everywhere uniqueness on a countable space?
- Can a countably infinite set carry a uniform probability law?

---

## Sujet B — Convolution is not a marginal operation

Let $(X,Y)$ be integer-valued.

1. Construct the law of $X+Y$ as a pushforward of the joint law.
2. Derive convolution under independence.
3. Give two joint laws with identical Bernoulli$(1/2)$ marginals and different sum laws.

### Relances

- Which exact equality expresses independence at the level of pmfs?
- Prove the closure of binomial laws with a common success parameter.
- Characterize when the sum of independent Bernoulli$(p)$ and Bernoulli$(q)$ variables is binomial with two trials.
- Which conclusions about $X+Y$ survive if only the marginals are known?

---

## Sujet C — Replacement, dependence, and the hypergeometric law

A population contains $N$ objects, of which $K$ are successes. A uniform sample of size $n$ is drawn without replacement.

1. Construct the probability space and derive the law of the number $H$ of sampled successes.
2. Compute $\mathbb E[H]$ and $\operatorname{Var}(H)$ from indicators.
3. Explain the sign and role of the covariance between two draw indicators.

### Relances

- State the exact support of $H$.
- Locate the finite-population correction.
- Prove the binomial limit for fixed $n$ and $K_N/N\to p$.
- Replace the count by the position of the $r$-th success. Which law appears, and why is it not negative binomial?

---

## Sujet D — Poisson mechanisms and false closure

Let $N\sim\operatorname{Pois}(\lambda)$.

1. Compute the first two factorial moments of $N$.
2. Prove Poisson splitting under independent Bernoulli labels.
3. Recover the conditional binomial allocation of two independent Poisson components given their total.

### Relances

- Where does independence enter each proof?
- If $N\mid\Lambda\sim\operatorname{Pois}(\Lambda)$, compute the unconditional mean and variance.
- Prove that a non-degenerate Poisson mixture is not Poisson.
- Compute $\mathbb E[N(N+1)/2]$ and explain precisely why evaluating the same polynomial at $\mathbb E[N]$ fails.
- What changes under zero truncation?

---

## Sujet E — Waiting laws and convention control

Let $(B_n)_{n\ge1}$ be iid Bernoulli$(p)$ with $0<p\le1$.

1. Construct the first-success time $G$ and the $r$-th-success time $T_r$.
2. Derive their pmfs and moments.
3. Prove

   $$
   \{T_r\le n\}
   =
   \left\{\sum_{i=1}^nB_i\ge r\right\}.
   $$

### Relances

- State the support before the formula.
- Convert from the trial convention to the failures-before-success convention.
- What happens at $p=0$ and $p=1$?
- Compare an infinite Bernoulli sequence with sampling without replacement from a finite population.

---

## Verdict

The oral cycle is reconstructible only if the candidate can move in both directions:

$$
\text{construction}
\longrightarrow
\text{law}
\longrightarrow
\text{calculation},
$$

and

$$
\text{verbal model}
\longrightarrow
\text{missing hypothesis}
\longrightarrow
\text{valid construction}.
$$

Fast arithmetic does not repair a false product law.
