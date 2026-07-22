---
type: td
module: pushforwards-and-laws
status: canonical
exam-snapshot: 2026-07
---

# TD 03 — Atomic Laws, Counting Models, and Structural Failures

The exercises form the dependency chain

$$
\text{failure of representation}
\to
\text{atomic density}
\to
\text{pushforward}
\to
\text{product law}
\to
\text{named constructions}
\to
\text{mixture and conditioning}.
$$

The companion corrigé is [Corrigé TD 03](../03_Corriges/Corrigé%20TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md). It should remain closed until a complete written attempt has been made.

---

## Exercise 0 — Two ruptures in counting measure

1. Prove that there is no probability measure $\mu$ on $\mathbb N$ such that

   $$
   \mu(\{n\})=c
   $$

   for every $n\in\mathbb N$ and one fixed constant $c$.

2. Let $\#$ denote counting measure on $[0,1]$, now regarded as an uncountable measurable space with its Borel $\sigma$-field. Prove that $\#$ is not $\sigma$-finite.

3. Let $\lambda$ be Lebesgue measure restricted to $[0,1]$. Prove that

   $$
   \lambda\ll\#,
   $$

   but that there is no measurable $f:[0,1]\to[0,\infty]$ satisfying

   $$
   \lambda(A)=\int_Af\,d\#
   $$

   for every Borel set $A$.

4. Identify exactly which hypothesis of the Radon–Nikodym theorem is unavailable. Explain why the implication

   $$
   \nu\ll\mu
   \Longrightarrow
   \nu=f\mu
   $$

   is therefore illegitimate in this example.

---

## Exercise 1 — Construction of an atomic law

Let $E$ be countable and let $a:E\to[0,\infty)$.

1. Determine the necessary and sufficient condition under which there exists a constant $c>0$ such that

   $$
   p(x)=ca(x)
   $$

   is a probability mass function on $E$. Determine $c$.

2. Assuming that condition, define

   $$
   \mu(A):=\sum_{x\in A}p(x),
   \qquad A\subseteq E.
   $$

   Prove countable additivity without appealing to a pre-existing random variable.

3. Let $\#_E$ be counting measure. Identify $d\mu/d\#_E$ and state the uniqueness basis precisely.

4. Prove directly, first for nonnegative $\varphi$ and then for integrable signed $\varphi$, that

   $$
   \int_E\varphi\,d\mu
   =
   \sum_{x\in E}\varphi(x)p(x).
   $$

5. Conversely, let $\mu$ be a probability measure on $E$. Recover $p$ from $\mu$, and prove that no information is lost.

---

## Exercise 2 — Fibres and a transformed payment

Let $X$ take values in $\{0,1,2,4\}$ with

$$
\mathbb P(X=0)=\frac1{10},
\quad
\mathbb P(X=1)=\frac2{10},
\quad
\mathbb P(X=2)=\frac3{10},
\quad
\mathbb P(X=4)=\frac4{10}.
$$

Define

$$
g(x):=\min\{(x-1)_+,2\},
\qquad
Y:=g(X).
$$

1. Determine the fibres of $g$ on the support of $X$ and construct the law of $Y$ from the pushforward definition.

2. Compute $\mathbb E[Y]$ and $\operatorname{Var}(Y)$ from that law.

3. Compute $g(\mathbb E[X])$. Compare it with $\mathbb E[g(X)]$ and identify the invalid interchange.

4. Let $E,F$ be countable, let $X$ have pmf $p$, and let $g:E\to F$. Prove the general fibre formula

   $$
   p_{g(X)}(y)
   =
   \sum_{x\in g^{-1}(\{y\})}p(x).
   $$

5. Determine the necessary and sufficient condition on the restriction of $g$ to $\operatorname{supp}_{\mathrm a}(\mu_X)$ under which the law of $g(X)$ determines the law of $X$.

---

## Exercise 3 — A sum remembers the joint law

Let $(X,Y)$ be integer-valued.

1. Starting from the addition map $a(x,y)=x+y$, prove

   $$
   \mathbb P(X+Y=n)
   =
   \sum_{k\in\mathbb Z}p_{X,Y}(k,n-k).
   $$

2. Derive the convolution formula under independence.

3. Construct two pairs $(X_1,Y_1)$ and $(X_2,Y_2)$ such that all four one-dimensional marginals are Bernoulli$(1/2)$, while

   $$
   \mu_{X_1+Y_1}
   \ne
   \mu_{X_2+Y_2}.
   $$

4. Let $U\sim\operatorname{Bin}(m,p)$ and $V\sim\operatorname{Bin}(n,p)$ be independent. Prove from their Bernoulli constructions that

   $$
   U+V\sim\operatorname{Bin}(m+n,p).
   $$

5. Let $B_p$ and $B_q$ be independent Bernoulli variables with respective parameters $p$ and $q$. Prove that $B_p+B_q$ has a binomial law with two trials if and only if $p=q$.

---

## Exercise 4 — Replacement is a covariance decision

### A. With replacement

Let $B_1,\ldots,B_n$ be independent Bernoulli$(p)$ variables and set

$$
S_n:=\sum_{i=1}^nB_i.
$$

1. Derive the pmf of $S_n$ by partitioning $\{S_n=k\}$ into configurations.
2. Compute $\mathbb E[S_n]$ and $\operatorname{Var}(S_n)$ from the indicator representation.
3. Determine $\mathbb E[(S_n)_2]$ without expanding the binomial pmf.

### B. Without replacement

A population has size $N$, of which $K$ objects are labelled successes. A sample of size $n\le N$ is selected uniformly without replacement. Let $H$ be the number of successes in the sample.

4. Construct the underlying uniform probability measure on the set of $n$-subsets and derive the support and pmf of $H$.
5. By using ordered draws and success indicators $I_1,\ldots,I_n$, prove

   $$
   \mathbb E[I_j]=\frac KN
   $$

   and, for $i\ne j$,

   $$
   \operatorname{Cov}(I_i,I_j)
   =
   -\frac KN\left(1-\frac KN\right)\frac1{N-1}.
   $$

6. Deduce the mean and variance of $H$, including the finite-population correction.
7. Let $n$ be fixed and let $N\to\infty$ along a sequence for which $K_N/N\to p$. Prove pointwise on $\{0,\ldots,n\}$ that the hypergeometric pmf converges to the binomial$(n,p)$ pmf.
8. Locate the precise step at which replacing sampling without replacement by independent Bernoulli trials changes the model.

---

## Exercise 5 — Waiting times in infinite and finite populations

Let $(B_n)_{n\ge1}$ be independent Bernoulli$(p)$ variables with $0<p\le1$.

1. For

   $$
   G:=\min\{n\ge1:B_n=1\},
   $$

   derive the geometric pmf and prove its memoryless property.

2. For $r\ge1$, define

   $$
   T_r:=\min\left\{n\ge r:\sum_{i=1}^nB_i=r\right\}.
   $$

   Derive the pmf of $T_r$ by isolating the last trial.

3. Decompose $T_r$ into independent geometric waiting blocks. Deduce its mean and variance.

4. Prove the event identity

   $$
   \{T_r\le n\}
   =
   \left\{\sum_{i=1}^nB_i\ge r\right\}.
   $$

5. Let $1\le r\le K$. A finite sequence of $N$ positions contains exactly $K$ successes, and the set of success positions is uniform among the $K$-subsets of $\{1,\ldots,N\}$. Let $T_r^{(N)}$ be the position of the $r$-th success. Prove

   $$
   \mathbb P(T_r^{(N)}=t)
   =
   \frac{\binom{t-1}{r-1}\binom{N-t}{K-r}}{\binom NK},
   $$

   on its exact support.

6. Explain why $T_r^{(N)}$ is not negative binomial. Identify the finite-population constraint absent from $T_r$.

---

## Exercise 6 — Poisson superposition and splitting

Let $N\sim\operatorname{Pois}(\lambda)$.

1. Verify normalization and compute $\mathbb E[N]$, $\mathbb E[(N)_2]$, and $\operatorname{Var}(N)$ by index shifts.

2. Let $N_1$ and $N_2$ be independent Poisson variables with parameters $\lambda_1$ and $\lambda_2$. Prove by convolution that

   $$
   N_1+N_2
   \sim
   \operatorname{Pois}(\lambda_1+\lambda_2).
   $$

3. Conditional on $N=n$, label each of the $n$ counted events independently as type A with probability $p$ and type B with probability $1-p$. Let $K$ and $L$ be the two resulting counts. Compute the joint pmf of $(K,L)$ and prove that

   $$
   K\sim\operatorname{Pois}(\lambda p),
   \qquad
   L\sim\operatorname{Pois}(\lambda(1-p)),
   $$

   with $K$ and $L$ independent.

4. Conversely, assume $\lambda_1+\lambda_2>0$. Determine the conditional law of $N_1$ given $N_1+N_2=n$.

5. In each preceding conclusion, identify where independence enters. State what remains true if only the marginal Poisson laws are known.

---

## Exercise 7 — A mixture is usually not a named family

Let $I$ be Bernoulli$(\alpha)$ with $0<\alpha<1$. Conditional on $I=i$, let

$$
N\mid I=i
\sim
\operatorname{Pois}(\lambda_i),
\qquad i\in\{0,1\}.
$$

1. Derive the unconditional pmf of $N$.
2. Compute $\mathbb E[N]$ and $\operatorname{Var}(N)$ by conditioning on $I$.
3. Prove that if $\lambda_0\ne\lambda_1$, then the unconditional law of $N$ is not Poisson.
4. Compute

   $$
   \mathbb P(I=1\mid N=0).
   $$

5. For a non-degenerate $M\sim\operatorname{Pois}(\lambda)$, derive the pmf, mean, and variance of the zero-truncated law

   $$
   \mathcal L(M\mid M\ge1).
   $$

6. Explain why both the mixture and the truncation retain a Poisson formula in their numerators while failing to be Poisson laws.

---

## Exercise 8 — Integrated actuarial count model

Let $I\in\{0,1\}$ be a latent policy class with

$$
\mathbb P(I=1)=\alpha.
$$

Conditional on $I=i$, the number of reported claims is Poisson with parameter $\lambda_i$. Independently for each reported claim, the claim survives a contractual filter with probability $p\in(0,1]$. Let $K$ be the number of surviving claims and define the annual charge

$$
Y:=\frac{K(K+1)}2.
$$

1. Prove that

   $$
   K\mid I=i
   \sim
   \operatorname{Pois}(p\lambda_i).
   $$

2. Determine the unconditional law of $K$, and compute its mean and variance.
3. Compute the posterior probability

   $$
   \mathbb P(I=1\mid K=0).
   $$

4. Compute $\mathbb E[Y\mid I=i]$ using factorial moments, and then compute $\mathbb E[Y]$.
5. Let $\Lambda:=\lambda_I$. Prove

   $$
   \mathbb E[Y]
   -
   \frac{\mathbb E[K]\,(\mathbb E[K]+1)}2
   =
   \frac12\left(
   p\,\mathbb E[\Lambda]
   +
   p^2\operatorname{Var}(\Lambda)
   \right).
   $$

6. Interpret separately the two positive terms on the right: one comes from conditional Poisson fluctuation, the other from latent heterogeneity.
7. State the minimal changes required if the filter probability depends on the class.

---

## Source calibration

All problems in this TD are original constructions. Their deployment targets were calibrated against the [July 2026 Exam P syllabus](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf) and the [SOA Exam P Sample Questions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf), without reproducing official problem statements.

- Exercise 2 abstracts the transformed-payment mechanism represented by Q49 and Q50.
- Exercises 4 and 5 abstract the replacement and waiting-time distinctions represented by Q90, Q128, Q146, Q149, Q303, Q322, and Q382.
- Exercises 6–8 abstract Poisson superposition, truncation, mixture, Bayes reversal, and nonlinear moments represented by Q124, Q227, Q228, Q246, Q314, Q386, and Q512.
- Discrete-uniform and joint-law deployment are represented by Q150, Q243, Q244, and Q514.

The adaptation is structural: the official questions calibrate the terminal calculation and distractor logic; the TD retains responsibility for constructing the measure, representation, and failure boundary.
