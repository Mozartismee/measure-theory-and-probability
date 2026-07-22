---
type: corrige
module: pushforwards-and-laws
status: canonical
exam-snapshot: 2026-07
---

# Corrigé TD 03 — Atomic Laws, Counting Models, and Structural Failures

## Exercise 0 — Two ruptures in counting measure

1. If $\mu(\{n\})=c$ for every $n$, then countable additivity gives

   $$
   1=\mu(\mathbb N)=\sum_{n\ge0}c.
   $$

   For $c=0$ the sum is $0$; for $c>0$ it is $+\infty$. No such probability measure exists.

2. Suppose $[0,1]=\bigcup_{n\ge1}A_n$ with $\#(A_n)<\infty$. Then every $A_n$ is finite, so their union is countable, contradicting the uncountability of $[0,1]$. Thus $\#$ is not $\sigma$-finite.

3. Since $\#(A)=0$ implies $A=\varnothing$, one has $\lambda\ll\#$. If $\lambda=f\#$, then for every $x\in[0,1]$,

   $$
   f(x)
   =
   \int_{\{x\}}f\,d\#
   =
   \lambda(\{x\})
   =0.
   $$

   Hence $f=0$ pointwise and

   $$
   1=\lambda([0,1])=\int_{[0,1]}f\,d\#=0,
   $$

   a contradiction.

4. The reference measure $\#$ is not $\sigma$-finite. The $\sigma$-finite Radon–Nikodym theorem therefore does not apply. Absolute continuity alone is insufficient outside its theorem regime.

---

## Exercise 1 — Construction of an atomic law

1. Set

   $$
   Z:=\sum_{x\in E}a(x).
   $$

   A normalized multiple exists exactly when

   $$
   0<Z<\infty.
   $$

   Necessity follows from $1=cZ$ with $c>0$; sufficiency holds with

   $$
   c=Z^{-1}.
   $$

2. Let $(A_j)_{j\ge1}$ be pairwise disjoint subsets of $E$. Since all summands are nonnegative,

   $$
   \begin{aligned}
   \mu\!\left(\bigcup_{j\ge1}A_j\right)
   &=
   \sum_{x\in E}p(x)\mathbf1_{\cup_jA_j}(x)\\
   &=
   \sum_{x\in E}\sum_{j\ge1}p(x)\mathbf1_{A_j}(x)\\
   &=
   \sum_{j\ge1}\sum_{x\in A_j}p(x)\\
   &=
   \sum_{j\ge1}\mu(A_j).
   \end{aligned}
   $$

   The interchange is Tonelli for nonnegative series. Moreover, $\mu(E)=1$.

3. For every $A\subseteq E$,

   $$
   \mu(A)=\sum_{x\in A}p(x)=\int_Ap\,d\#_E.
   $$

   Hence

   $$
   \frac{d\mu}{d\#_E}=p.
   $$

   Uniqueness holds $\#_E$-a.e.; since only $\varnothing$ is $\#_E$-null, this is pointwise uniqueness.

4. For a nonnegative simple function $s=\sum_{j=1}^mc_j\mathbf1_{A_j}$ with disjoint $A_j$,

   $$
   \int_Es\,d\mu
   =
   \sum_{j=1}^mc_j\mu(A_j)
   =
   \sum_{x\in E}s(x)p(x).
   $$

   If $0\le s_n\uparrow\varphi$, monotone convergence on both sides gives

   $$
   \int_E\varphi\,d\mu
   =
   \sum_{x\in E}\varphi(x)p(x).
   $$

   For integrable signed $\varphi$, apply the nonnegative identity to $\varphi^+$ and $\varphi^-$; both sums are finite.

5. Given $\mu$, define $p(x)=\mu(\{x\})$. Since $E$ is countable,

   $$
   \mu(A)
   =
   \mu\!\left(\bigsqcup_{x\in A}\{x\}\right)
   =
   \sum_{x\in A}p(x).
   $$

   Thus the singleton masses determine $\mu$ on all of $2^E$.

---

## Exercise 2 — Fibres and a transformed payment

1. On the support of $X$,

   $$
   g(0)=g(1)=0,
   \qquad
   g(2)=1,
   \qquad
   g(4)=2.
   $$

   Hence

   $$
   g^{-1}(\{0\})\cap\operatorname{supp}_{\mathrm a}(\mu_X)=\{0,1\},
   $$

   while the other two nonempty fibres are $\{2\}$ and $\{4\}$. Therefore

   $$
   \mathbb P(Y=0)=\frac3{10},
   \qquad
   \mathbb P(Y=1)=\frac3{10},
   \qquad
   \mathbb P(Y=2)=\frac4{10}.
   $$

2. One obtains

   $$
   \mathbb E[Y]
   =
   \frac3{10}+2\frac4{10}
   =
   \frac{11}{10},
   $$

   and

   $$
   \mathbb E[Y^2]
   =
   \frac3{10}+4\frac4{10}
   =
   \frac{19}{10}.
   $$

   Thus

   $$
   \operatorname{Var}(Y)
   =
   \frac{19}{10}-\left(\frac{11}{10}\right)^2
   =
   \frac{69}{100}.
   $$

3. Since

   $$
   \mathbb E[X]
   =
   \frac{2+6+16}{10}
   =
   \frac{12}{5},
   $$

   one has

   $$
   g(\mathbb E[X])
   =
   \min\left\{\frac75,2\right\}
   =
   \frac75
   \ne
   \frac{11}{10}
   =
   \mathbb E[g(X)].
   $$

   Expectation is linear; it does not commute with a general nonlinear $g$.

4. By the pushforward definition,

   $$
   \begin{aligned}
   p_{g(X)}(y)
   &=\mathbb P(g(X)=y)\\
   &=\mathbb P\bigl(X\in g^{-1}(\{y\})\bigr)\\
   &=\sum_{x\in g^{-1}(\{y\})}p(x).
   \end{aligned}
   $$

5. The condition is that $g$ be injective on $\operatorname{supp}_{\mathrm a}(\mu_X)$. Under injectivity, every nonzero output mass has one preimage in the support, so it recovers the corresponding input mass. If two support points $x_1\ne x_2$ lie in one fibre, the output law records only

   $$
   p_X(x_1)+p_X(x_2),
   $$

   and a small redistribution between these two positive masses leaves the pushforward unchanged. The input law is then not identifiable from the output law.

---

## Exercise 3 — A sum remembers the joint law

1. Since

   $$
   \{(x,y)\in\mathbb Z^2:x+y=n\}
   =
   \bigsqcup_{k\in\mathbb Z}\{(k,n-k)\},
   $$

   countable additivity gives

   $$
   \mathbb P(X+Y=n)
   =
   \sum_{k\in\mathbb Z}p_{X,Y}(k,n-k).
   $$

2. Under independence,

   $$
   p_{X,Y}(k,n-k)=p_X(k)p_Y(n-k),
   $$

   hence

   $$
   p_{X+Y}(n)
   =
   \sum_{k\in\mathbb Z}p_X(k)p_Y(n-k).
   $$

3. Let $B\sim\operatorname{Bernoulli}(1/2)$. Set

   $$
   (X_1,Y_1)=(B,B),
   \qquad
   (X_2,Y_2)=(B,1-B).
   $$

   All marginals are Bernoulli$(1/2)$, but

   $$
   \mathbb P(X_1+Y_1=0)
   =
   \mathbb P(X_1+Y_1=2)
   =
   \frac12,
   $$

   whereas

   $$
   X_2+Y_2=1
   \quad\text{a.s.}
   $$

4. Write

   $$
   U=\sum_{i=1}^mB_i,
   \qquad
   V=\sum_{i=m+1}^{m+n}B_i,
   $$

   where all $B_i$ are independent Bernoulli$(p)$. Then

   $$
   U+V=\sum_{i=1}^{m+n}B_i
   \sim
   \operatorname{Bin}(m+n,p).
   $$

5. If $B_p+B_q\sim\operatorname{Bin}(2,r)$, then equality of means and the mass at $2$ give

   $$
   p+q=2r,
   \qquad
   pq=r^2.
   $$

   Hence

   $$
   \frac{p+q}{2}=\sqrt{pq}.
   $$

   Equality in the arithmetic–geometric mean inequality forces $p=q=r$. Conversely, if $p=q$, the sum of the two iid Bernoulli variables is binomial$(2,p)$.

---

## Exercise 4 — Replacement is a covariance decision

### A. With replacement

1. For a subset $J\subseteq\{1,\ldots,n\}$ of size $k$, the event

   $$
   \{B_i=1\text{ exactly for }i\in J\}
   $$

   has probability $p^k(1-p)^{n-k}$. These $\binom nk$ events are disjoint and exhaust $\{S_n=k\}$. Thus

   $$
   \mathbb P(S_n=k)
   =
   \binom nkp^k(1-p)^{n-k}.
   $$

2. Linearity gives

   $$
   \mathbb E[S_n]=\sum_{i=1}^n\mathbb E[B_i]=np.
   $$

   Independence gives zero covariance between distinct indicators, hence

   $$
   \operatorname{Var}(S_n)
   =
   \sum_{i=1}^n\operatorname{Var}(B_i)
   =
   np(1-p).
   $$

3. Since $B_i^2=B_i$,

   $$
   (S_n)_2
   =
   \sum_{i\ne j}B_iB_j.
   $$

   Therefore

   $$
   \mathbb E[(S_n)_2]
   =
   \sum_{i\ne j}\mathbb E[B_i]\mathbb E[B_j]
   =
   n(n-1)p^2.
   $$

### B. Without replacement

4. Let the population be $\{1,\ldots,N\}$ and let $C$ be the fixed set of $K$ successes. Put

   $$
   \Omega=\{A\subseteq\{1,\ldots,N\}:|A|=n\},
   $$

   with the uniform law, and define $H(A)=|A\cap C|$. For $H=k$, choose $k$ objects from $C$ and $n-k$ from $C^c$. Thus

   $$
   \mathbb P(H=k)
   =
   \frac{\binom Kk\binom{N-K}{n-k}}{\binom Nn},
   $$

   for

   $$
   \max\{0,n-(N-K)\}
   \le k\le
   \min\{n,K\}.
   $$

5. Every draw position is symmetric, so

   $$
   \mathbb P(I_j=1)=\frac KN.
   $$

   For $i\ne j$,

   $$
   \mathbb P(I_i=1,I_j=1)
   =
   \frac KN\frac{K-1}{N-1}.
   $$

   Hence

   $$
   \begin{aligned}
   \operatorname{Cov}(I_i,I_j)
   &=
   \frac{K(K-1)}{N(N-1)}-\frac{K^2}{N^2}\\
   &=
   -\frac KN\left(1-\frac KN\right)\frac1{N-1}.
   \end{aligned}
   $$

6. Since $H=\sum_{j=1}^nI_j$,

   $$
   \mathbb E[H]=n\frac KN.
   $$

   Writing $u=K/N$,

   $$
   \begin{aligned}
   \operatorname{Var}(H)
   &=
   n u(1-u)+n(n-1)\left(-\frac{u(1-u)}{N-1}\right)\\
   &=
   n u(1-u)\frac{N-n}{N-1}.
   \end{aligned}
   $$

7. Using falling factorials,

   $$
   \frac{\binom{K_N}{k}\binom{N-K_N}{n-k}}{\binom Nn}
   =
   \binom nk
   \frac{(K_N)_k(N-K_N)_{n-k}}{(N)_n}.
   $$

   For fixed $n$ and $k$, each factor in the first falling-factorial ratio tends to $p$, and each factor in the second tends to $1-p$. Hence the expression tends to

   $$
   \binom nkp^k(1-p)^{n-k}.
   $$

8. With replacement, the joint mass of a success pattern factors into a product of constant Bernoulli probabilities. Without replacement,

   $$
   \mathbb P(I_j=1\mid I_i=1)=\frac{K-1}{N-1}\ne\frac KN
   $$

   in the non-degenerate regime. The product-law step fails, and the covariance term survives.

---

## Exercise 5 — Waiting times in infinite and finite populations

1. For $k\ge1$,

   $$
   \{G=k\}
   =
   \{B_1=\cdots=B_{k-1}=0,B_k=1\},
   $$

   so

   $$
   \mathbb P(G=k)=(1-p)^{k-1}p.
   $$

   With $q=1-p$,

   $$
   \mathbb P(G>m+n\mid G>m)
   =
   \frac{q^{m+n}}{q^m}
   =q^n
   =\mathbb P(G>n),
   $$

   whenever the conditioning event has positive probability. For $p=1$, the statement is read on the only positive-probability conditioning event.

2. For $T_r=n$, the $n$-th trial is a success and exactly $r-1$ successes occur among the first $n-1$ trials. Hence

   $$
   \mathbb P(T_r=n)
   =
   \binom{n-1}{r-1}p^r(1-p)^{n-r},
   \qquad n\ge r.
   $$

3. Let $G_j$ be the number of trials from the $(j-1)$-st success, excluded, to the $j$-th success, included. Independence of disjoint Bernoulli blocks and stationarity of the iid sequence give iid geometric$(p)$ variables $G_1,\ldots,G_r$ with

   $$
   T_r=G_1+\cdots+G_r.
   $$

   The tail-sum formula gives

   $$
   \mathbb E[G_1]
   =
   \sum_{n\ge0}\mathbb P(G_1>n)
   =
   \sum_{n\ge0}q^n
   =
   \frac1p.
   $$

   Differentiating the geometric series yields

   $$
   \operatorname{Var}(G_1)=\frac q{p^2}.
   $$

   Therefore

   $$
   \mathbb E[T_r]=\frac rp,
   \qquad
   \operatorname{Var}(T_r)=\frac{rq}{p^2}.
   $$

4. The $r$-th success occurs by time $n$ exactly when at least $r$ successes have occurred among the first $n$ trials. Thus

   $$
   \{T_r\le n\}
   =
   \left\{\sum_{i=1}^nB_i\ge r\right\}.
   $$

5. Assume $1\le r\le K$. A success-position set has $T_r^{(N)}=t$ exactly when it contains $t$, contains $r-1$ positions among $\{1,\ldots,t-1\}$, and contains $K-r$ positions among $\{t+1,\ldots,N\}$. Since all $K$-subsets are equiprobable,

   $$
   \mathbb P(T_r^{(N)}=t)
   =
   \frac{\binom{t-1}{r-1}\binom{N-t}{K-r}}{\binom NK},
   $$

   for

   $$
   r\le t\le N-K+r.
   $$

6. In the finite model, exactly $K$ successes and $N-K$ failures exist. Draws are dependent and the waiting time is bounded by $N-K+r$. The negative-binomial construction uses independent Bernoulli trials with an unbounded supply of failures, so its support is unbounded and its product probabilities do not match the finite-population law.

---

## Exercise 6 — Poisson superposition and splitting

1. For $\lambda\ge0$,

   $$
   \sum_{k\ge0}e^{-\lambda}\frac{\lambda^k}{k!}=1.
   $$

   For $\lambda>0$,

   $$
   \mathbb E[N]
   =
   e^{-\lambda}\sum_{k\ge1}k\frac{\lambda^k}{k!}
   =
   \lambda e^{-\lambda}\sum_{j\ge0}\frac{\lambda^j}{j!}
   =\lambda,
   $$

   and

   $$
   \mathbb E[(N)_2]
   =
   \lambda^2e^{-\lambda}\sum_{j\ge0}\frac{\lambda^j}{j!}
   =\lambda^2.
   $$

   Since $N^2=(N)_2+N$,

   $$
   \operatorname{Var}(N)
   =
   \lambda^2+\lambda-\lambda^2
   =\lambda.
   $$

   The case $\lambda=0$ is $N=0$ almost surely.

2. For $n\ge0$, independence gives

   $$
   \begin{aligned}
   \mathbb P(N_1+N_2=n)
   &=
   \sum_{k=0}^n
   e^{-\lambda_1}\frac{\lambda_1^k}{k!}
   e^{-\lambda_2}\frac{\lambda_2^{n-k}}{(n-k)!}\\
   &=
   e^{-(\lambda_1+\lambda_2)}\frac1{n!}
   \sum_{k=0}^n\binom nk\lambda_1^k\lambda_2^{n-k}\\
   &=
   e^{-(\lambda_1+\lambda_2)}
   \frac{(\lambda_1+\lambda_2)^n}{n!}.
   \end{aligned}
   $$

3. The event $\{K=k,L=\ell\}$ forces $N=k+\ell$. Conditional on that total, the labels have a binomial allocation. Thus

   $$
   \begin{aligned}
   \mathbb P(K=k,L=\ell)
   &=
   e^{-\lambda}\frac{\lambda^{k+\ell}}{(k+\ell)!}
   \binom{k+\ell}{k}p^k(1-p)^\ell\\
   &=
   \left[e^{-\lambda p}\frac{(\lambda p)^k}{k!}\right]
   \left[e^{-\lambda(1-p)}\frac{(\lambda(1-p))^\ell}{\ell!}\right].
   \end{aligned}
   $$

   This factorization proves both marginal Poisson laws and independence.

4. Put $\lambda=\lambda_1+\lambda_2>0$. For $0\le k\le n$,

   $$
   \begin{aligned}
   \mathbb P(N_1=k\mid N_1+N_2=n)
   &=
   \frac{
   e^{-\lambda_1}\lambda_1^k/k!\,
   e^{-\lambda_2}\lambda_2^{n-k}/(n-k)!
   }{
   e^{-\lambda}\lambda^n/n!
   }\\
   &=
   \binom nk
   \left(\frac{\lambda_1}{\lambda}\right)^k
   \left(\frac{\lambda_2}{\lambda}\right)^{n-k}.
   \end{aligned}
   $$

   Hence

   $$
   N_1\mid(N_1+N_2=n)
   \sim
   \operatorname{Bin}\!\left(n,\frac{\lambda_1}{\lambda_1+\lambda_2}\right).
   $$

5. Superposition uses independence to replace the joint pmf by a product. Splitting uses conditional independence of the labels. With only the two marginal Poisson laws, one still has

   $$
   \mathbb E[N_1+N_2]=\lambda_1+\lambda_2,
   $$

   but neither a Poisson sum law nor the binomial conditional allocation follows. The variance also contains $2\operatorname{Cov}(N_1,N_2)$.

---

## Exercise 7 — A mixture is usually not a named family

1. For $k\ge0$,

   $$
   \mathbb P(N=k)
   =
   (1-\alpha)e^{-\lambda_0}\frac{\lambda_0^k}{k!}
   +
   \alpha e^{-\lambda_1}\frac{\lambda_1^k}{k!}.
   $$

2. Let

   $$
   \bar\lambda=(1-\alpha)\lambda_0+\alpha\lambda_1.
   $$

   Then

   $$
   \mathbb E[N]
   =
   \mathbb E[\mathbb E[N\mid I]]
   =\bar\lambda.
   $$

   The conditional-variance decomposition gives

   $$
   \begin{aligned}
   \operatorname{Var}(N)
   &=
   \mathbb E[\operatorname{Var}(N\mid I)]
   +
   \operatorname{Var}(\mathbb E[N\mid I])\\
   &=
   \bar\lambda
   +
   \alpha(1-\alpha)(\lambda_1-\lambda_0)^2.
   \end{aligned}
   $$

3. If $\lambda_0\ne\lambda_1$, then

   $$
   \operatorname{Var}(N)>\mathbb E[N].
   $$

   Every Poisson law has equality of mean and variance, so the mixture is not Poisson.

4. Bayes' formula gives

   $$
   \mathbb P(I=1\mid N=0)
   =
   \frac{\alpha e^{-\lambda_1}}
   {(1-\alpha)e^{-\lambda_0}+\alpha e^{-\lambda_1}}.
   $$

5. Put $d=1-e^{-\lambda}>0$. For $k\ge1$,

   $$
   \mathbb P(M=k\mid M\ge1)
   =
   \frac{e^{-\lambda}\lambda^k}{k!d}.
   $$

   Since the omitted state $0$ contributes nothing to the first two moments,

   $$
   \mathbb E[M\mid M\ge1]
   =
   \frac{\lambda}{d},
   $$

   and

   $$
   \mathbb E[M^2\mid M\ge1]
   =
   \frac{\lambda^2+\lambda}{d}.
   $$

   Therefore

   $$
   \operatorname{Var}(M\mid M\ge1)
   =
   \frac{\lambda}{d}
   -
   \frac{\lambda^2e^{-\lambda}}{d^2}.
   $$

6. A mixture is a weighted sum of several Poisson measures; its mass ratios are not those of one parameter. Truncation restricts a Poisson measure to $\{1,2,\ldots\}$ and renormalizes it; the missing mass at $0$ changes both normalization and support. A familiar numerator is not a family characterization.

---

## Exercise 8 — Integrated actuarial count model

Let

$$
\Lambda:=\lambda_I,
\qquad
\bar\lambda:=\mathbb E[\Lambda]
=(1-\alpha)\lambda_0+\alpha\lambda_1.
$$

1. Conditional on $I=i$, the reported count is Poisson$(\lambda_i)$ and each report is retained independently with probability $p$. Poisson splitting gives

   $$
   K\mid I=i
   \sim
   \operatorname{Pois}(p\lambda_i).
   $$

2. Hence, for $k\ge0$,

   $$
   \mathbb P(K=k)
   =
   (1-\alpha)e^{-p\lambda_0}\frac{(p\lambda_0)^k}{k!}
   +
   \alpha e^{-p\lambda_1}\frac{(p\lambda_1)^k}{k!}.
   $$

   Moreover,

   $$
   \mathbb E[K]=p\bar\lambda,
   $$

   and

   $$
   \operatorname{Var}(K)
   =
   p\bar\lambda
   +
   p^2\operatorname{Var}(\Lambda)
   =
   p\bar\lambda
   +
   p^2\alpha(1-\alpha)(\lambda_1-\lambda_0)^2.
   $$

3. Since $\mathbb P(K=0\mid I=i)=e^{-p\lambda_i}$,

   $$
   \mathbb P(I=1\mid K=0)
   =
   \frac{\alpha e^{-p\lambda_1}}
   {(1-\alpha)e^{-p\lambda_0}+\alpha e^{-p\lambda_1}}.
   $$

4. If $Z\sim\operatorname{Pois}(\theta)$, then

   $$
   \mathbb E[Z^2]
   =
   \mathbb E[(Z)_2]+\mathbb E[Z]
   =
   \theta^2+\theta.
   $$

   Therefore

   $$
   \mathbb E\!\left[\frac{Z(Z+1)}2\right]
   =
   \theta+\frac{\theta^2}{2}.
   $$

   With $\theta=p\lambda_i$,

   $$
   \mathbb E[Y\mid I=i]
   =
   p\lambda_i+\frac{p^2\lambda_i^2}{2}.
   $$

   Averaging over $I$ gives

   $$
   \mathbb E[Y]
   =
   p\,\mathbb E[\Lambda]
   +
   \frac{p^2}{2}\mathbb E[\Lambda^2].
   $$

5. Since $\mathbb E[K]=p\mathbb E[\Lambda]$,

   $$
   \begin{aligned}
   \mathbb E[Y]
   -
   \frac{\mathbb E[K]\,(\mathbb E[K]+1)}2
   &=
   p\mathbb E[\Lambda]
   +\frac{p^2}{2}\mathbb E[\Lambda^2]
   -\frac12\left(p^2\mathbb E[\Lambda]^2+p\mathbb E[\Lambda]\right)\\
   &=
   \frac12\left(
   p\mathbb E[\Lambda]
   +
   p^2\operatorname{Var}(\Lambda)
   \right).
   \end{aligned}
   $$

6. The term $p\mathbb E[\Lambda]/2$ is the contribution of within-class Poisson variance to the nonlinear moment. The term $p^2\operatorname{Var}(\Lambda)/2$ is the additional contribution of between-class heterogeneity. Replacing $\mathbb E[h(K)]$ by $h(\mathbb E[K])$ deletes both.

7. If the retention probability is $p_i$ in class $i$, replace the conditional parameter $p\lambda_i$ by

   $$
   \theta_i:=p_i\lambda_i.
   $$

   The unconditional count is the mixture of Poisson$(\theta_i)$ laws, the posterior zero-count weights use $e^{-\theta_i}$, and all moment formulas are written in terms of the latent parameter $\Theta=\theta_I$. Conditional independent thinning within each class remains required.

---

## Deployment boundary

The formulas above justify the discrete mechanisms behind the [SOA Exam P Sample Questions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf). They do not assert that every verbal count model is binomial, Poisson, geometric, or hypergeometric. The family name is earned by the construction and its dependence regime.
