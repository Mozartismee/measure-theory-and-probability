---
type: study-packet-notes
cycle: 2026-07-exam-p-first-pass
packet: discrete-laws
start: 2026-07-18
end: 2026-07-24
math-authority: derived
canonical-sources:
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../30_Pushforwards-and-Laws/02_TD/TD 03 — Atomic Laws, Counting Models, and Structural Failures.md
  - ../../../../../30_Pushforwards-and-Laws/05_Example-Sheets/Example Sheet 01 — Exam P Discrete Distribution Deployment.md
---

# Preparatory Notes

These notes give the minimum reading order and the object to be reconstructed after each session. Definitions, theorem statements and proofs remain canonical in the [Atomic Laws Cours](../../../../../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md); substantial constructions remain the responsibility of [TD 03](../../../../../30_Pushforwards-and-Laws/02_TD/TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md). After a rupture, read only the section needed to repair the first illegitimate step.

## Global dependency

$$
\begin{aligned}
&\text{countable state space and counting measure}\\
&\qquad\Downarrow\\
&\text{atomic density and discrete LOTUS}\\
&\qquad\Downarrow\\
&\text{fibre pushforward and joint atomic law}\\
&\qquad\Downarrow\\
&\text{addition pushforward; convolution under product law}\\
&\qquad\Downarrow\\
&\text{binomial, hypergeometric, waiting, and Poisson constructions}\\
&\qquad\Downarrow\\
&\text{restriction, mixture, posterior normalization, nonlinear payment}.
\end{aligned}
$$

Each arrow produces an object required by the next one. A family name is not a premise; it is the conclusion of a recognised construction.

## J1 — Counting measure and atomic density

Read Atomic Laws Cours §§1–3, then complete TD 03, Exercises 0–1.

Let $E$ be finite or countably infinite with counting measure $\#_E$. For every probability measure $\mu$ on $(E,2^E)$,

$$
p(x):=\mu(\{x\}),
\qquad
\mu(A)=\sum_{x\in A}p(x),
\qquad
\mu=p\#_E.
$$

The density is unique $\#_E$-almost everywhere; since the only $\#_E$-null set is empty, uniqueness is pointwise. For admissible $\varphi$,

$$
\int_E\varphi\,d\mu
=
\sum_{x\in E}\varphi(x)p(x).
$$

With the Cours closed, reconstruct separately:

1. countability $\Rightarrow\sigma$-finiteness of $\#_E$；
2. countable additivity $\Rightarrow$ atomic representation；
3. pushforward integration $\Rightarrow$ discrete LOTUS；
4. integrability $\Leftrightarrow\sum|\varphi|p<\infty$ for signed $\varphi$。

### Boundary

On an uncountable space, full counting measure is not $\sigma$-finite. Absolute continuity with respect to it is vacuous: every measure is absolutely continuous because only the empty set is null. A nonatomic probability measure therefore supplies the decisive counterexample to an illegitimate RN invocation.

## J2 — Fibres, joint laws, and convolution

Read Atomic Laws Cours §§4–5, then complete TD 03, Exercises 2–3.

For $Y=g(X)$ with countable state spaces,

$$
p_Y(y)
=
\sum_{x\in g^{-1}(\{y\})}p_X(x).
$$

This is the singleton form of $\mu_Y=g_\#\mu_X$. It handles coarsening, truncation, deductibles, caps, maxima and nonlinear payments. It does not authorize

$$
\mathbb E[g(X)]=g(\mathbb E[X]).
$$

For integer-valued $(X,Y)$,

$$
p_{X+Y}(n)
=
\sum_{k\in\mathbb Z}p_{X,Y}(k,n-k).
$$

The reduction to

$$
p_{X+Y}(n)=\sum_kp_X(k)p_Y(n-k)
$$

requires $\mu_{X,Y}=\mu_X\otimes\mu_Y$. Marginals alone do not determine the sum law.

### Reconstruction test

Construct two Bernoulli$(1/2)$ pairs with identical marginals and different sums. If the counterexample cannot be produced without notes, the word “convolution” has not yet acquired a legitimate domain.

## J3 — Replacement as a dependence decision

Read Atomic Laws Cours §§6.1, 6.4 and 6.5, then complete TD 03, Exercise 4.

With replacement or under iid trials,

$$
S_n=\sum_{j=1}^nB_j,
\qquad
B_j\overset{\mathrm{iid}}\sim\operatorname{Bernoulli}(p),
$$

produces the binomial law. Without replacement, the probability space is a uniform law on finite subsets or ordered samples; the indicators have common mean $K/N$ but negative covariance. Hence, for $N>1$,

$$
\operatorname{Var}(H)
=
n\frac KN\left(1-\frac KN\right)\frac{N-n}{N-1}.
$$

The last factor is not a correction remembered after the fact. It is the trace of the off-diagonal covariance terms.

### Endpoints

- $n=0$ or $K=0$ gives the point mass at $0$.
- $K=N$ gives the point mass at $n$.
- For $N=1$, every admissible hypergeometric law is deterministic; the displayed quotient with $N-1$ is not used.
- A countably infinite set admits no uniform probability assigning the same mass to every point.

## J4 — Waiting times and convention control

Read Atomic Laws Cours §6.3, then complete TD 03, Exercise 5.

For iid Bernoulli$(p)$ trials with $0<p\le1$,

$$
G=\min\{n\ge1:B_n=1\},
\qquad
T_r=\min\left\{n\ge r:\sum_{j=1}^nB_j=r\right\}.
$$

The trial convention gives

$$
\mathbb P(T_r=n)
=
\binom{n-1}{r-1}p^r(1-p)^{n-r},
\qquad n\ge r.
$$

The failures-before-success convention is $T_r-r$ and has support $\mathbb N$. The family name alone does not determine which variable is being used.

The event identity

$$
\{T_r\le n\}
=
\left\{\sum_{j=1}^nB_j\ge r\right\}
$$

is the transfer interface between waiting-time questions and binomial tails.

### Boundary

If $p=0$, the hitting time is $+\infty$ almost surely and is not an $\mathbb N^*$-valued geometric variable. At $p=1$, $G=1$ and $T_r=r$ almost surely. A finite population with exactly $K$ successes has a terminal horizon and negative dependence; its $r$-th success position is not negative binomial.

## J5 — Poisson mechanisms

Read Atomic Laws Cours §6.2 and complete TD 03, Exercise 6. Only then consult [Example Sheet 01](../../../../../30_Pushforwards-and-Laws/05_Example-Sheets/Example%20Sheet%2001%20—%20Exam%20P%20Discrete%20Distribution%20Deployment.md) §§2–5 for support, moments and closure boundaries.

For $N\sim\operatorname{Pois}(\lambda)$,

$$
\mathbb E[N]=\lambda,
\qquad
\mathbb E[(N)_2]=\lambda^2,
\qquad
\operatorname{Var}(N)=\lambda.
$$

These identities follow from index shifts and $N^2=(N)_2+N$; no generating function is needed.

If $N_1,N_2$ are independent Poisson variables, convolution gives

$$
N_1+N_2\sim\operatorname{Pois}(\lambda_1+\lambda_2).
$$

If each point of a Poisson count is independently labelled A with probability $p$, joint-pmf factorization gives independent counts

$$
K\sim\operatorname{Pois}(\lambda p),
\qquad
L\sim\operatorname{Pois}(\lambda(1-p)).
$$

Conversely,

$$
N_1\mid(N_1+N_2=n)
\sim
\operatorname{Bin}\left(n,\frac{\lambda_1}{\lambda_1+\lambda_2}\right)
$$

when $\lambda_1+\lambda_2>0$.

### Boundary

Poisson marginals do not determine the sum law. Splitting requires independent labels conditional on the total. Conditioning on the total destroys the unconditional independence of the components.

## J6 — Restriction, mixture, and posterior normalization

Read Atomic Laws Cours §7 and complete TD 03, Exercise 7; then read the structural anchors in Example Sheet §6.

For a positive-mass event $A$ in a countable state space,

$$
p_A(x)
=
\frac{p(x)\mathbf1_A(x)}{\sum_{z\in A}p(z)}.
$$

The denominator must be positive. Restriction without normalization is a subprobability measure, not a conditional law.

For a latent state $I$ with weights $\alpha_i$ and conditional pmfs $p_i$,

$$
p_X(x)=\sum_i\alpha_ip_i(x).
$$

If $X\in L^2$,

$$
\operatorname{Var}(X)
=
\mathbb E[\operatorname{Var}(X\mid I)]
+
\operatorname{Var}(\mathbb E[X\mid I]).
$$

Thus, for $N\mid\Lambda\sim\operatorname{Pois}(\Lambda)$ and $\Lambda\in L^2$,

$$
\operatorname{Var}(N)
=
\mathbb E[\Lambda]+\operatorname{Var}(\Lambda).
$$

A non-degenerate Poisson mixture is therefore not Poisson. A zero-truncated Poisson law is also not Poisson: its support and normalizing constant have changed.

## J7 — Integrated chain and terminal deployment

Complete TD 03, Exercise 8; choose one sujet from [Colle 01](../../../../../30_Pushforwards-and-Laws/04_Colles/Colle%2001%20—%20Discrete%20Laws%20and%20Structural%20Diagnosis.md); open the SOA audit only afterwards.

The integrated object is

$$
I
\longrightarrow
N\mid I
\longrightarrow
K\mid(N,I)
\longrightarrow
K\mid I
\longrightarrow
\mu_K
\longrightarrow
\mathbb E\!\left[\frac{K(K+1)}2\right].
$$

Each arrow has a distinct justification:

1. latent-class conditioning specifies the component law;
2. independent thinning gives the conditional Poisson count;
3. mixing removes the latent state;
4. Bayes normalizes joint masses on the observed fibre;
5. factorial moments evaluate the nonlinear payment.

The official audit tests whether this architecture can be compressed to exam speed. It does not lower the proof standard that made the compression legitimate.

## Repair routing

| First rupture | Minimal repair source |
| --- | --- |
| Cannot define the state-space measure or counting density | Atomic Laws Cours §§1–2 |
| Cannot compute a transformed law | Atomic Laws Cours §3; TD Exercise 2 |
| Uses convolution from marginals alone | Atomic Laws Cours §§4–5; TD Exercise 3 |
| Confuses replacement regimes | Atomic Laws Cours §6.4; TD Exercise 4 |
| Cannot state waiting support or convention | Atomic Laws Cours §6.3; TD Exercise 5 |
| Recalls Poisson closure without its hypotheses | Atomic Laws Cours §6.2; TD Exercise 6 |
| Treats mixture or truncation as the same family | Atomic Laws Cours §7; TD Exercise 7 |
| Computes $g(\mathbb E[K])$ instead of $\mathbb E[g(K)]$ | Example Sheet §4; TD Exercise 8 |
