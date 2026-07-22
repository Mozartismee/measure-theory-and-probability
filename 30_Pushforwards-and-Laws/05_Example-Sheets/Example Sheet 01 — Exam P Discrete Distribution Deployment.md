---
type: example-sheet
module: pushforwards-and-laws
status: canonical
exam-snapshot: 2026-07
---

# Example Sheet 01 — Exam P Discrete Distribution Deployment

## 1. One representation, several notations

For a countable state space $E$,

$$
\mu_X=X_\#\mathbb P
=
p_X\#_E,
\qquad
p_X=\frac{d\mu_X}{d\#_E},
$$

and, for every admissible $\varphi$,

$$
\boxed{
\mathbb E[\varphi(X)]
=
\int_E\varphi\,d\mu_X
=
\sum_{x\in E}\varphi(x)p_X(x)
}.
$$

The sum is not a second definition of expectation. It is the atomic representation of the pushforward integral.

---

## 2. Canonical families

Write $q=1-p$.

| Law | Support | Probability mass | Mean | Variance | Construction |
| --- | --- | --- | --- | --- | --- |
| Bernoulli$(p)$ | $\{0,1\}$ | $p^xq^{1-x}$ | $p$ | $pq$ | one success indicator |
| Binomial$(n,p)$ | $0,\ldots,n$ | $\binom nkp^kq^{n-k}$ | $np$ | $npq$ | sum of $n$ iid Bernoulli$(p)$ |
| Geometric$(p)$, trial convention | $1,2,\ldots$ | $q^{k-1}p$ | $1/p$ | $q/p^2$ | trial of first success |
| Negative binomial$(r,p)$, trial convention | $r,r+1,\ldots$ | $\binom{k-1}{r-1}p^rq^{k-r}$ | $r/p$ | $rq/p^2$ | trial of $r$-th success |
| Hypergeometric$(N,K,n)$, $N>1$ | $\max(0,n-N+K),\ldots,\min(n,K)$ | $\binom Kk\binom{N-K}{n-k}/\binom Nn$ | $nK/N$ | $n(K/N)(1-K/N)(N-n)/(N-1)$ | $n$ draws without replacement |
| Poisson$(\lambda)$ | $0,1,\ldots$ | $e^{-\lambda}\lambda^k/k!$ for $\lambda>0$; $\delta_0$ at $\lambda=0$ | $\lambda$ | $\lambda$ | Poisson count law |
| Uniform on finite $A$ | $A$ | $1/|A|$ | support-dependent | support-dependent | normalized counting measure |

The parameter regimes are $0\le p\le1$ for Bernoulli and binomial laws, $0<p\le1$ for the finite geometric and negative-binomial waiting laws, $0\le K,n\le N$ for the hypergeometric law, and $\lambda\ge0$ for the Poisson law. At degenerate endpoints, the construction determines the point mass.

For $U$ uniform on $\{a,a+1,\ldots,b\}$ with $m=b-a+1$,

$$
\mathbb E[U]=\frac{a+b}{2},
\qquad
\operatorname{Var}(U)=\frac{m^2-1}{12}.
$$

For $N=1$, every admissible hypergeometric variable is deterministic and has variance $0$; the displayed variance quotient is not used. The displayed family is not identified by its formula alone. Its support, parameter convention, and construction are part of the object.

---

## 3. Structural reversals

| Wording or data | Reverse to | Do not replace it by |
| --- | --- | --- |
| fixed number of independent trials with common success probability | binomial pushforward of a product Bernoulli law | binomial merely because outcomes are binary |
| trials until a success or the $r$-th success | geometric or negative-binomial hitting time | a binomial count with a random number of trials |
| sample from a finite population without replacement | hypergeometric image of a uniform sample law | independent Bernoulli trials |
| independent Poisson counts over disjoint periods | convolution and parameter addition | addition of parameters without independence |
| two independent Poisson components observed only through their total | conditional binomial allocation | unconditional independence after conditioning |
| heterogeneous risk classes | mixture of class-conditional laws | one family with the averaged parameter |
| observation $X\in A$ with positive probability | restriction to $A$ followed by normalization | deletion of excluded masses without renormalization |
| payment $Y=g(X)$ | fibre pushforward and $\mathbb E[g(X)]$ | $g(\mathbb E[X])$ |
| joint probability table | atomic measure on a product space | two unrelated marginal tables |
| large iid aggregate | CLT approximation, possibly with continuity correction | an exact normal identity |

---

## 4. Moment mechanisms

For an integer-valued $N$,

$$
N^2=(N)_2+N.
$$

For $N\sim\operatorname{Pois}(\lambda)$,

$$
\mathbb E[(N)_2]=\lambda^2,
\qquad
\mathbb E[N^2]=\lambda^2+\lambda.
$$

Thus, for any constants $a,b,c$,

$$
\mathbb E[aN^2+bN+c]
=
a(\lambda^2+\lambda)+b\lambda+c.
$$

For a sum $S=\sum_{i=1}^nX_i$ with finite second moments,

$$
\operatorname{Var}(S)
=
\sum_{i=1}^n\operatorname{Var}(X_i)
+
2\sum_{i<j}\operatorname{Cov}(X_i,X_j).
$$

The covariance sum disappears under independence, becomes negative under sampling without replacement, and can reappear as positive between-class variation under a mixture.

For a latent state $I$,

$$
\operatorname{Var}(X)
=
\mathbb E[\operatorname{Var}(X\mid I)]
+
\operatorname{Var}(\mathbb E[X\mid I]).
$$

This is the fastest legitimate distinction between one Poisson law and a Poisson mixture.

---

## 5. Closure and failure table

| Input | Additional hypothesis | Output | Failure when removed |
| --- | --- | --- | --- |
| $\operatorname{Bin}(m,p)$ and $\operatorname{Bin}(n,p)$ | independence | $\operatorname{Bin}(m+n,p)$ | dependence changes the sum law |
| Bernoulli$(p_i)$ variables | independence, but unequal $p_i$ | Poisson-binomial | generally not binomial |
| $\operatorname{Pois}(\lambda_i)$ variables | independence | $\operatorname{Pois}(\sum_i\lambda_i)$ | Poisson marginals alone do not determine the sum |
| Poisson count with independent type labels | conditional independent thinning | independent Poisson type counts | dependent labels destroy splitting |
| finite sample without replacement | uniform sample | hypergeometric | binomial variance misses the finite-population correction |
| Poisson$(\Lambda)$ conditional on random $\Lambda$ | non-degenerate mixing | mixed Poisson | variance exceeds mean |
| Poisson$(\lambda)$ conditioned on positivity | $\lambda>0$ | zero-truncated Poisson | not Poisson because support and normalization changed |

---

## 6. Official SOA anchors

Question numbers refer to the [SOA Exam P Sample Questions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf) linked from the [July 2026 Exam P syllabus](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf). Use the [official sample solutions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-sol.pdf) only after a complete attempt. The sample bank is versioned and renumbered; the structural classification is stable, the question number is snapshot-specific.

| Official anchors | Structural object to identify |
| --- | --- |
| Q13 | normalization and tail summation of an atomic law |
| Q30, Q172 | binomial construction; Q172 adds conditioning through a discrete transition law |
| Q94, Q96, Q146, Q303, Q322 | geometric or negative-binomial waiting structure and convention |
| Q90, Q128, Q149, Q233, Q382 | sampling without replacement; Q149 is a finite waiting law, Q382 a conditional hypergeometric fibre |
| Q150, Q243, Q616 | discrete uniform law, product law, transformation, or comparison with continuous uniform |
| Q29, Q47, Q124, Q302, Q355, Q505 | Poisson parameter recovery, transformed count, and independent-period aggregation |
| Q227, Q314 | Poisson mixture, total variance, and Bayes reversal |
| Q228, Q499, Q566 | normalized restriction of a Poisson law |
| Q246 | independent Poisson components conditioned through their sum |
| Q386, Q512 | factorial moments and the failure of $g(\mathbb E[N])$ |
| Q89, Q171, Q244, Q248, Q514 | joint atomic law, marginalization, covariance, and nonlinear expectation |

The point is not to memorize a question-number taxonomy. It is to make the first valid mathematical object appear before the arithmetic begins.

---

## 7. CLT endpoint

For iid $X_i$ with mean $m$ and variance $0<\sigma^2<\infty$,

$$
\frac{\sum_{i=1}^nX_i-nm}{\sigma\sqrt n}
\Longrightarrow
\mathcal N(0,1).
$$

For a unit-lattice integer-valued sum $S_n$,

$$
\mathbb P(a\le S_n\le b)
\approx
\Phi\!\left(\frac{b+\tfrac12-nm}{\sigma\sqrt n}\right)
-
\Phi\!\left(\frac{a-\tfrac12-nm}{\sigma\sqrt n}\right).
$$

The continuity correction belongs to the approximation map. It is not part of the exact discrete law, and the CLT statement alone gives no finite-$n$ error bound.

---

## 8. Minimal reconstruction

A deployable solution should expose, in this order:

$$
\boxed{
\text{state space}
\to
\text{law construction}
\to
\text{support}
\to
\text{required pushforward or restriction}
\to
\text{finite sum}
}.
$$

If an independence, replacement, or positive-denominator hypothesis is used, it must be visible at the step where it acts. Naming the distribution after the calculation is too late.
