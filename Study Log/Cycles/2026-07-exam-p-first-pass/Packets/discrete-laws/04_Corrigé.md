---
type: study-packet-corrige
cycle: 2026-07-exam-p-first-pass
packet: discrete-laws
start: 2026-07-18
end: 2026-07-24
access-policy: after-complete-attempt
math-authority: derived
canonical-sources:
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../30_Pushforwards-and-Laws/02_TD/TD 03 — Atomic Laws, Counting Models, and Structural Failures.md
  - ../../../../../30_Pushforwards-and-Laws/03_Corriges/Corrigé TD 03 — Atomic Laws, Counting Models, and Structural Failures.md
---

# Corrigé — Discrete Laws

Do not use this file before a complete written attempt. The [canonical TD corrigé](../../../../../30_Pushforwards-and-Laws/03_Corriges/Corrigé%20TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md) remains the source for TD 03 Exercises 0–8; this document solves only the packet-specific Entry Gate and Exercises A–E. After locating the first rupture, close the solution and reconstruct the decisive step without notes on the following day.

## Entry Gate

1. Define

   $$
   p(x)=\mu(\{x\}),
   \qquad x\in E.
   $$

   Countable additivity on the disjoint singleton decomposition gives

   $$
   \mu(A)=\sum_{x\in A}p(x)
   =\int_Ap\,d\#_E.
   $$

   Thus $\mu=p\#_E$. The density is unique $\#_E$-almost everywhere, hence pointwise because the only $\#_E$-null subset of a countable space is empty.

2. On $[0,1]$, $\#(A)=0$ implies $A=\varnothing$, so $\lambda\ll\#$. If $\lambda=f\#$, testing the singleton $\{x\}$ gives

   $$
   f(x)=\int_{\{x\}}f\,d\#=\lambda(\{x\})=0
   $$

   for every $x$. Hence $f=0$, contradicting $\lambda([0,1])=1$. The unavailable RN hypothesis is $\sigma$-finiteness of the reference counting measure.

3. For the law $\mu_X=X_\#\mathbb P$,

   $$
   \mathbb E[g(X)]=\int g\,d\mu_X,
   $$

   or $\sum_xg(x)p_X(x)$ in the atomic representation. In general this is not $g(\mathbb E[X])$.

4. For integer-valued $(X,Y)$,

   $$
   p_{X+Y}(n)=\sum_{k\in\mathbb Z}p_{X,Y}(k,n-k).
   $$

   If $X$ and $Y$ are independent, $p_{X,Y}=p_Xp_Y$, and only then does the expression reduce to $p_X*p_Y$.

5. The constructions give, respectively: binomial; hypergeometric; negative binomial in the trial convention; a mixed Poisson law. Under the stated square-integrability hypothesis, a non-degenerate intensity contributes the strictly positive between-component term $\operatorname{Var}(\Lambda)$, so the mixture cannot be Poisson.

## Exercise A — Identical marginals, different pushforwards

Both coordinates of both pairs equal either $B$ or $1-B$, so all four marginals are Bernoulli$(1/2)$.

For the positively coupled pair,

$$
p_{X_+,Y_+}(0,0)=p_{X_+,Y_+}(1,1)=\frac12,
$$

and all other joint masses vanish. Therefore

$$
\mathbb P(X_++Y_+=0)=\mathbb P(X_++Y_+=2)=\frac12.
$$

For the negatively coupled pair,

$$
p_{X_-,Y_-}(0,1)=p_{X_-,Y_-}(1,0)=\frac12,
$$

so $X_-+Y_-=1$ almost surely. Neither pair is independent: for example,

$$
p_{X_+,Y_+}(0,0)=\frac12\ne\frac14,
\qquad
p_{X_-,Y_-}(0,1)=\frac12\ne\frac14.
$$

For $h(x,y)=\mathbf1_{\{x+y\ge1\}}$, one has

$$
h(X_+,Y_+)=B,
\qquad
h(X_-,Y_-)=1.
$$

Thus the first pushforward is Bernoulli$(1/2)$ with expectation $1/2$, whereas the second is $\delta_1$ with expectation $1$. In both cases the source measure is the joint law on $\{0,1\}^2$, not the pair of marginal laws.

More generally, every joint law with Bernoulli$(1/2)$ marginals has, for some $a\in[0,1/2]$,

$$
p_{00}=p_{11}=a,
\qquad
p_{01}=p_{10}=\frac12-a.
$$

Hence

$$
\mathbb P(X+Y=0)=a,
\quad
\mathbb P(X+Y=1)=1-2a,
\quad
\mathbb P(X+Y=2)=a.
$$

The marginals determine the support and the mean $\mathbb E[X+Y]=1$, but not the sum law.

## Exercise B — Finite-population correction

The support is $\{0,1,2,3,4,5\}$ and

$$
\mathbb P(H=k)
=
\frac{\binom7k\binom{13}{5-k}}{\binom{20}5}.
$$

For ordered-draw success indicators $I_1,\ldots,I_5$,

$$
H=\sum_{j=1}^5I_j,
\qquad
\mathbb E[I_j]=\frac7{20},
$$

so

$$
\mathbb E[H]=5\frac7{20}=\frac74.
$$

For $i\ne j$,

$$
\operatorname{Cov}(I_i,I_j)
=
-\frac7{20}\frac{13}{20}\frac1{19}
=
-\frac{91}{7600}.
$$

Therefore

$$
\operatorname{Var}(H)
=
5\frac7{20}\frac{13}{20}\frac{15}{19}
=
\frac{273}{304}.
$$

A binomial$(5,7/20)$ variable has variance

$$
5\frac7{20}\frac{13}{20}=\frac{91}{80}.
$$

The difference is

$$
\frac{91}{80}-\frac{273}{304}
=
\frac{91}{380},
$$

which is exactly the negative of

$$
2\sum_{1\le i<j\le5}\operatorname{Cov}(I_i,I_j)
=
-\frac{91}{380}.
$$

If $n=N$, then $H=K$ almost surely and the finite-population factor $N-n$ makes the variance zero. If $N=1$, every admissible model is deterministic; one uses that construction directly rather than the quotient containing $N-1$.

## Exercise C — Finite and infinite waiting structures

To have the second success at position $t$, one success must occur among the first $t-1$ positions, position $t$ must be a success, and the remaining three successes must occur among the last $12-t$ positions. Thus

$$
\mathbb P(T^{(12)}_2=t)
=
\frac{\binom{t-1}{1}\binom{12-t}{3}}{\binom{12}{5}},
$$

with exact support

$$
2\le t\le9.
$$

In the iid Bernoulli$(5/12)$ model,

$$
\mathbb P(T_2=t)
=
\binom{t-1}{1}
\left(\frac5{12}\right)^2
\left(\frac7{12}\right)^{t-2},
\qquad t\ge2.
$$

The two laws differ because the finite model has bounded support and because its draws are negatively dependent with exactly five total successes; the iid model has an infinite horizon and a fixed success probability at every trial.

For $n\ge2$,

$$
T_2\le n
$$

holds exactly when the first $n$ trials contain at least two successes. Hence

$$
\{T_2\le n\}
=
\{\operatorname{Bin}(n,5/12)\ge2\}.
$$

The failures-before-second-success variable is $F_2=T_2-2$ and has support $\mathbb N$. At $p=0$, the second success time is $+\infty$ almost surely and no finite-valued negative-binomial law results. At $p=1$, $T_2=2$ and $F_2=0$ almost surely.

## Exercise D — One Poisson model through three representations

For $k,l\in\mathbb N$,

$$
\begin{aligned}
\mathbb P(K=k,L=l)
&=
\mathbb P(N=k+l)
\binom{k+l}{k}
\left(\frac13\right)^k
\left(\frac23\right)^l\\
&=
e^{-4}
\frac{(4/3)^k}{k!}
\frac{(8/3)^l}{l!}\\
&=
\left(e^{-4/3}\frac{(4/3)^k}{k!}\right)
\left(e^{-8/3}\frac{(8/3)^l}{l!}\right).
\end{aligned}
$$

Therefore

$$
K\sim\operatorname{Pois}(4/3),
\qquad
L\sim\operatorname{Pois}(8/3),
$$

and the factorization proves independence.

Conditioning on $K+L=5$ and cancelling the common Poisson factors gives

$$
K\mid(K+L=5)
\sim
\operatorname{Bin}(5,1/3).
$$

Since

$$
\frac{K(K+1)}2
=
\frac{(K)_2}{2}+K,
$$

and $\theta=4/3$,

$$
\mathbb E[Y]
=
\frac{\theta^2}{2}+\theta
=
\frac{20}{9}.
$$

On the other hand,

$$
g(\mathbb E[K])
=
g(4/3)
=
\frac{14}{9}.
$$

The missing amount is

$$
\frac23
=
\frac12\operatorname{Var}(K).
$$

If labels cease to be conditionally independent, the binomial allocation given $N$, the joint factorization, the Poisson marginals and their independence can fail. The identity $K+L=N$ survives, and the first moments survive if each event still has the stated marginal label probability independently of $N$.

## Exercise E — Mixture and truncation

For $k\in\mathbb N$,

$$
\mathbb P(N=k)
=
\frac34e^{-1}\frac1{k!}
+
\frac14e^{-4}\frac{4^k}{k!}.
$$

Let $\Lambda=1$ when $I=0$ and $\Lambda=4$ when $I=1$. Then

$$
\mathbb E[\Lambda]=\frac74,
\qquad
\operatorname{Var}(\Lambda)
=
\frac14\frac34(4-1)^2
=
\frac{27}{16}.
$$

Consequently,

$$
\mathbb E[N]=\frac74,
\qquad
\operatorname{Var}(N)
=
\mathbb E[\Lambda]+\operatorname{Var}(\Lambda)
=
\frac{55}{16}.
$$

Since $55/16\ne7/4$, the unconditional law cannot be Poisson.

The two joint masses on the observed fibre $\{N=0\}$ are

$$
\mathbb P(I=0,N=0)=\frac34e^{-1},
\qquad
\mathbb P(I=1,N=0)=\frac14e^{-4}.
$$

Normalization gives

$$
\mathbb P(I=1\mid N=0)
=
\frac{e^{-4}}{3e^{-1}+e^{-4}}
=
\frac1{3e^3+1}.
$$

For $M\sim\operatorname{Pois}(\lambda)$ with $\lambda>0$, set $a=1-e^{-\lambda}$. The zero-truncated pmf is

$$
\mathbb P(M=k\mid M\ge1)
=
\frac{e^{-\lambda}\lambda^k}{a\,k!},
\qquad k\ge1.
$$

Because the zero term contributes nothing to the first two raw moments,

$$
\mathbb E[M\mid M\ge1]
=
\frac{\lambda}{a},
$$

and

$$
\begin{aligned}
\operatorname{Var}(M\mid M\ge1)
&=
\frac{\lambda^2+\lambda}{a}
-
\frac{\lambda^2}{a^2}\\
&=
\frac{\lambda}{1-e^{-\lambda}}
-
\frac{\lambda^2e^{-\lambda}}{(1-e^{-\lambda})^2}.
\end{aligned}
$$

The latent mixture is a convex sum of two probability measures. Truncation is restriction of one measure to $\{1,2,\ldots\}$ followed by normalization. Their numerators retain Poisson factors for different structural reasons; neither operation produces a new member of the original Poisson family in the non-degenerate regime.

## Official-audit structural key

This table classifies the mechanism only. It does not reproduce or answer the official questions.

| Question | Structural object |
| --- | --- |
| Q30 | fixed independent Bernoulli trials; binomial construction |
| Q128 | sampling without replacement; hypergeometric count |
| Q146 | finite-horizon event expressed through a negative-binomial waiting structure and conditioning |
| Q150 | discrete-uniform law followed by conditioning or finite mixing |
| Q227 | Poisson mixture and total variance |
| Q246 | independent Poisson components conditioned on their total; binomial allocation |
| Q386 | nonlinear Poisson payment evaluated through factorial moments |
| Q512 | second moment distinguished from the square of the mean |

Use the [official sample solutions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-sol.pdf) only to verify the locked numerical answers.

## Canonical TD solution map

| Canonical exercise | Decisive reconstruction |
| --- | --- |
| TD 03 Exercise 0 | uncountable counting measure is not $\sigma$-finite; $\lambda\ll\#$ has no density |
| TD 03 Exercise 1 | normalized atomic weights define a countably additive measure and its integral |
| TD 03 Exercise 2 | fibre pushforward and the injectivity boundary |
| TD 03 Exercise 3 | addition pushforward; convolution only under the product joint law |
| TD 03 Exercise 4 | binomial versus hypergeometric construction and covariance correction |
| TD 03 Exercise 5 | infinite waiting law versus finite-population order statistic |
| TD 03 Exercise 6 | Poisson factorial moments, superposition, splitting and conditional allocation |
| TD 03 Exercise 7 | mixture overdispersion, Bayes reversal and zero truncation |
| TD 03 Exercise 8 | latent class, conditional thinning, mixture and nonlinear payment |

For the complete proofs, use the corresponding section of Corrigé TD 03 after the written attempt. This packet does not maintain a second copy.
