---
type: cours
module: pushforwards-and-laws
status: canonical
exam-snapshot: 2026-07
---

# Atomic Laws and Discrete Distribution Structures

## 1. Countable state spaces and atomic laws

Let $E$ be a finite or countably infinite set, equipped with $2^E$, and let

$$
\#_E(A):=\operatorname{card}(A),
\qquad A\subseteq E,
$$

with the value $+\infty$ allowed. The measure $\#_E$ is $\sigma$-finite because $E$ is countable.

The underlying construction and integral-series representation are isolated in [Lemma 6 — Atomic Measures and Integration on Countable Spaces](../../80_Lemmas/Atomic%20Measures%20and%20Integration%20on%20Countable%20Spaces.md).

### Proposition 1 — Atomic representation

For a probability measure $\mu$ on $(E,2^E)$, define

$$
p(x):=\mu(\{x\}),
\qquad x\in E.
$$

Then

$$
p:E\to[0,1],
\qquad
\sum_{x\in E}p(x)=1,
$$

and, for every $A\subseteq E$,

$$
\boxed{
\mu(A)=\sum_{x\in A}p(x)
}.
$$

Equivalently,

$$
\mu\ll\#_E,
\qquad
p=\frac{d\mu}{d\#_E}
\quad \#_E\text{-a.e.}
$$

and in fact pointwise, since the only $\#_E$-null set is $\varnothing$.

Conversely, every $p:E\to[0,\infty)$ satisfying $\sum_Ep=1$ defines a probability measure by the displayed formula.

#### Proof

Lemma 6 gives the canonical atomic representation

$$
\mu(A)
=
\sum_{x\in A}p(x)
=
\int_Ap\,d\#_E
$$

Since $\mu$ is finite, Proposition 6.5 of that lemma identifies $p=d\mu/d\#_E$; because $\#_E$ has no nonempty null set, the uniqueness is pointwise. Taking $A=E$ gives $\sum_Ep=1$. Conversely, Proposition 6.1 of the same lemma shows that a normalized nonnegative $p$ defines the measure $\mu_p$, and $\mu_p(E)=1$. $\square$

### Boundary 1 — Why countability matters

If $E$ is uncountable, the full counting measure is not $\sigma$-finite. Every measure $\mu$ then satisfies $\mu\ll\#_E$, because $\#_E(A)=0$ only for $A=\varnothing$. Nevertheless, a nonatomic probability measure cannot be represented as $f\#_E$: from

$$
0=\mu(\{x\})=\int_{\{x\}}f\,d\#_E=f(x)
$$

for every $x$, one would obtain $f=0$ and hence $\mu(E)=0$. Absolute continuity without the legitimate Radon–Nikodym regime produces no density. The pathology is structural, not typographical.

### Definition 2 — Support of a discrete law

The atomic support is

$$
\operatorname{supp}_{\mathrm a}(\mu)
:=
\{x\in E:p(x)>0\}.
$$

On a countable state space, the law is determined by its values on this set. A formula for $p$ is incomplete until its support is stated.

---

## 2. Integration against an atomic law

Let $X:(\Omega,\mathcal F,\mathbb P)\to(E,2^E)$ be measurable and let $p_X(x)=\mathbb P(X=x)$.

### Proposition 3 — Discrete LOTUS

For every nonnegative $\varphi:E\to[0,\infty]$,

$$
\boxed{
\mathbb E[\varphi(X)]
=
\sum_{x\in E}\varphi(x)p_X(x)
}.
$$

The series uses the convention $0\cdot(+\infty)=0$.

For a real-valued $\varphi$, the expectation is finite if and only if

$$
\sum_{x\in E}|\varphi(x)|p_X(x)<\infty.
$$

#### Proof

The law of $X$ is $\mu_X=X_\#\mathbb P=p_X\#_E$. Hence the pushforward integration formula gives

$$
\mathbb E[\varphi(X)]
=
\int_E\varphi\,d\mu_X
=
\int_E\varphi p_X\,d\#_E
=
\sum_{x\in E}\varphi(x)p_X(x).
$$

The final equality is the atomic integration formula of Lemma 6.

For signed $\varphi$, apply the nonnegative identity to $\varphi^+$ and $\varphi^-$. $\square$

### Corollary 4 — Moments and factorial moments

For an integrable real-valued $X$,

$$
\mathbb E[X]=\sum_xxp_X(x).
$$

If $X\in L^2$, then

$$
\operatorname{Var}(X)
=
\sum_x(x-\mathbb E[X])^2p_X(x)
=
\mathbb E[X^2]-\mathbb E[X]^2.
$$

For an $\mathbb N$-valued random variable and $r\ge1$, write

$$
(X)_r:=X(X-1)\cdots(X-r+1).
$$

Factorial moments are ordinary LOTUS with a basis adapted to counts. In particular,

$$
X^2=(X)_2+X.
$$

This identity is the legitimate route behind many Poisson moment calculations; substituting $\mathbb E[X]$ into a nonlinear function is not.

---

## 3. Images, fibres, and transformed payments

Let $g:E\to F$, where $F$ is countable, and let $Y=g(X)$.

### Proposition 5 — Pushforward by fibre summation

The law of $Y$ is given by

$$
\boxed{
p_Y(y)
=
\sum_{x\in g^{-1}(\{y\})}p_X(x)
},
\qquad y\in F.
$$

#### Proof

By the definition of pushforward,

$$
p_Y(y)
=
\mathbb P(g(X)=y)
=
\mathbb P\bigl(X\in g^{-1}(\{y\})\bigr),
$$

and Proposition 1 expands the last probability over the fibre. $\square$

The formula covers coarsening, truncation, deductibles, benefit limits, maxima, and nonlinear costs. For a payment $Y=g(X)$, the object to integrate is $g$ against $\mu_X$:

$$
\mathbb E[Y]
=
\sum_xg(x)p_X(x).
$$

It is generally unrelated to $g(\mathbb E[X])$.

### Boundary 2 — Information destroyed by a pushforward

If $g$ is not injective, the law of $g(X)$ does not determine the law of $X$. Pushforward preserves precisely the information measurable through $g$ and discards the rest.

---

## 4. Joint laws, products, and conditioning on atoms

Let $(X,Y)$ take values in countable sets $E\times F$. Its joint probability mass function is

$$
p_{X,Y}(x,y):=\mathbb P(X=x,Y=y).
$$

The marginals are

$$
p_X(x)=\sum_{y\in F}p_{X,Y}(x,y),
\qquad
p_Y(y)=\sum_{x\in E}p_{X,Y}(x,y).
$$

These are pushforwards by the coordinate projections.

### Proposition 6 — Independence as product measure

The following are equivalent:

1. $X$ and $Y$ are independent;
2. $\mu_{X,Y}=\mu_X\otimes\mu_Y$;
3. for every $(x,y)\in E\times F$,

   $$
   p_{X,Y}(x,y)=p_X(x)p_Y(y).
   $$

#### Proof

Independence is the equality

$$
\mathbb P(X\in A,Y\in B)
=
\mathbb P(X\in A)\mathbb P(Y\in B)
$$

for all $A\subseteq E$ and $B\subseteq F$. This is exactly equality of the two measures on measurable rectangles. On countable spaces, it is enough to test singleton rectangles and then sum. $\square$

### Proposition 7 — Conditional law on a positive-mass atom

If $p_X(x)>0$, then

$$
\boxed{
p_{Y\mid X=x}(y)
=
\frac{p_{X,Y}(x,y)}{p_X(x)}
}.
$$

The numerator is the restriction of the joint law to the fibre $\{x\}\times F$; the denominator normalizes its total mass.

If $p_X(x)=0$, this quotient is undefined. A conditional law given $X=x$ may then require a chosen version of a kernel and is not determined by the elementary ratio. Exam P discrete conditioning stays on positive-mass fibres unless extra structure is supplied.

---

## 5. Convolution as a pushforward

Let $X$ and $Y$ be integer-valued and set $S=X+Y$. The addition map

$$
a:\mathbb Z^2\to\mathbb Z,
\qquad
a(x,y)=x+y,
$$

gives

$$
\mu_S=a_\#\mu_{X,Y}.
$$

Hence

$$
p_S(n)
=
\sum_{k\in\mathbb Z}p_{X,Y}(k,n-k).
$$

If $X$ and $Y$ are independent, Proposition 6 yields

$$
\boxed{
p_S(n)
=
\sum_{k\in\mathbb Z}p_X(k)p_Y(n-k)
}.
$$

The right-hand side is the convolution $p_X*p_Y$.

### Boundary 3 — Marginals do not determine a sum

The convolution formula uses the product joint law, not merely the two marginals. If $X$ and $Y$ are dependent, replacing $p_{X,Y}$ by $p_Xp_Y$ changes the model. The resulting number may be tidy; it is still the answer to a different question.

---

## 6. Canonical discrete families as constructions

Throughout, $q:=1-p$.

### 6.1 Bernoulli and binomial laws

A Bernoulli random variable $B\sim\operatorname{Bernoulli}(p)$ has

$$
\mathbb P(B=1)=p,
\qquad
\mathbb P(B=0)=q,
\qquad 0\le p\le1.
$$

If $B_1,\ldots,B_n$ are independent Bernoulli$(p)$ variables and

$$
S_n:=\sum_{i=1}^nB_i,
$$

then

$$
S_n\sim\operatorname{Bin}(n,p),
$$

with

$$
\mathbb P(S_n=k)
=
\binom nkp^kq^{n-k},
\qquad k=0,\ldots,n.
$$

Indeed, the event $\{S_n=k\}$ is the disjoint union of $\binom nk$ configurations having exactly $k$ successes, each of mass $p^kq^{n-k}$.

Linearity and independence give

$$
\mathbb E[S_n]=np,
\qquad
\operatorname{Var}(S_n)=npq.
$$

If independent $X\sim\operatorname{Bin}(m,p)$ and $Y\sim\operatorname{Bin}(n,p)$ share the same success parameter, then

$$
X+Y\sim\operatorname{Bin}(m+n,p).
$$

With unequal success parameters, the sum is generally Poisson-binomial, not binomial.

### 6.2 Poisson law

For $\lambda>0$, a Poisson random variable $N\sim\operatorname{Pois}(\lambda)$ satisfies

$$
\mathbb P(N=k)
=
e^{-\lambda}\frac{\lambda^k}{k!},
\qquad k\in\mathbb N,
$$

The endpoint is defined by $\operatorname{Pois}(0)=\delta_0$.

For $\lambda>0$, an index shift gives

$$
\mathbb E[N]
=
e^{-\lambda}\sum_{k\ge1}k\frac{\lambda^k}{k!}
=
\lambda,
$$

and

$$
\mathbb E[(N)_2]=\lambda^2.
$$

Consequently,

$$
\operatorname{Var}(N)
=
\mathbb E[(N)_2]+\mathbb E[N]-\mathbb E[N]^2
=
\lambda.
$$

If $N_1\sim\operatorname{Pois}(\lambda_1)$ and $N_2\sim\operatorname{Pois}(\lambda_2)$ are independent, then convolution and the binomial theorem yield

$$
N_1+N_2
\sim
\operatorname{Pois}(\lambda_1+\lambda_2).
$$

The conclusion can fail without independence.

### 6.3 Geometric and negative-binomial waiting laws

Fix the convention

$$
G:=\min\{n\ge1:B_n=1\},
$$

where $(B_n)_{n\ge1}$ are independent Bernoulli$(p)$ variables and $0<p\le1$. Then

$$
\mathbb P(G=k)=q^{k-1}p,
\qquad k\ge1,
$$

and

$$
\mathbb E[G]=\frac1p,
\qquad
\operatorname{Var}(G)=\frac q{p^2}.
$$

Whenever $\mathbb P(G>m)>0$, the tail is memoryless:

$$
\mathbb P(G>m+n\mid G>m)
=
\mathbb P(G>n).
$$

For $0<p<1$ this identity is available for every $m,n\ge0$. At $p=1$, $G=1$ almost surely, and conditioning on $\{G>m\}$ is unavailable once $m\ge1$.

Let

$$
T_r:=\min\left\{n\ge r:\sum_{i=1}^nB_i=r\right\}
$$

be the trial of the $r$-th success. Then

$$
\mathbb P(T_r=n)
=
\binom{n-1}{r-1}p^rq^{n-r},
\qquad n\ge r.
$$

The last trial must be a success, and exactly $r-1$ successes occur among the first $n-1$ trials. Moreover, $T_r$ is the sum of $r$ independent geometric waiting times, so

$$
\mathbb E[T_r]=\frac rp,
\qquad
\operatorname{Var}(T_r)=\frac{rq}{p^2}.
$$

The duality

$$
\boxed{
\{T_r\le n\}
=
\left\{\sum_{i=1}^nB_i\ge r\right\}
}
$$

translates a waiting-time question into a binomial tail.

Some texts define the negative-binomial variable as the number of failures before the $r$-th success, namely $T_r-r$. A parameter name does not resolve this shift; the support does.

If $p=0$, the waiting time is $+\infty$ almost surely and is not an $\mathbb N^*$-valued geometric random variable.

At $p=1$, one has $G=1$ and $T_r=r$ almost surely; these degenerate laws determine the endpoint values without an appeal to $0^0$.

### 6.4 Hypergeometric law

Consider a population of $N$ objects, $K$ of which are labelled successes. Draw $n$ objects uniformly without replacement, where $0\le n\le N$, and let $H$ be the number of successes drawn. Then

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

Write $H=I_1+\cdots+I_n$, where $I_j$ indicates that draw $j$ is a success. The indicators have common mean $K/N$ but are not independent. For $i\ne j$,

$$
\operatorname{Cov}(I_i,I_j)
=
-\frac{K}{N}\left(1-\frac KN\right)\frac1{N-1}.
$$

Therefore

$$
\mathbb E[H]=n\frac KN,
$$

and, for $N>1$,

$$
\boxed{
\operatorname{Var}(H)
=
n\frac KN\left(1-\frac KN\right)
\frac{N-n}{N-1}
}.
$$

The finite-population correction is the variance trace of negative dependence. Replacing sampling without replacement by independent Bernoulli trials erases it.

### 6.5 Discrete uniform law

For a nonempty finite set $A$, the uniform law is normalized counting measure:

$$
\operatorname{Unif}(A)
=
\frac1{|A|}\#_A.
$$

There is no uniform probability law on a countably infinite set assigning the same mass $c$ to every point. If $c>0$, the total mass diverges; if $c=0$, the total mass is zero.

---

## 7. Restriction, mixtures, and latent heterogeneity

### Proposition 8 — Conditioning by normalized restriction

Let $X$ have pmf $p$ on $E$, and let $A\subseteq E$ satisfy

$$
\mathbb P(X\in A)=\sum_{x\in A}p(x)>0.
$$

Then the conditional law of $X$ given $X\in A$ has pmf

$$
\boxed{
p_A(x)
=
\frac{p(x)\mathbf1_A(x)}{\sum_{z\in A}p(z)}
}.
$$

This is a restriction followed by renormalization. If the denominator is zero, the elementary conditional law is undefined.

### Proposition 9 — Mixtures of atomic laws

Let $I$ be a countable latent state with probabilities $\alpha_i$. Discard zero-weight states, and suppose that the conditional law of $X$ given $I=i$ has pmf $p_i$. Then

$$
p_X(x)=\sum_i\alpha_ip_i(x).
$$

Assume now that $E\subseteq\mathbb R$ and that every component has a finite second moment. Write

$$
m_i:=\sum_{x\in E}x\,p_i(x),
\qquad
v_i:=\sum_{x\in E}(x-m_i)^2p_i(x).
$$

Assume further

$$
\sum_i\alpha_i(v_i+m_i^2)<\infty,
$$

equivalently $X\in L^2$. Then

$$
\mathbb E[X]=\sum_i\alpha_im_i,
$$

and

$$
\boxed{
\operatorname{Var}(X)
=
\sum_i\alpha_iv_i
+
\sum_i\alpha_i(m_i-\mathbb E[X])^2
}.
$$

The second term records heterogeneity between components.

In particular, if $X\mid\Lambda\sim\operatorname{Pois}(\Lambda)$ and $\Lambda\in L^2$, then

$$
\mathbb E[X]=\mathbb E[\Lambda],
\qquad
\operatorname{Var}(X)
=
\mathbb E[\Lambda]+\operatorname{Var}(\Lambda).
$$

Thus a non-degenerate Poisson mixture is overdispersed and cannot itself be Poisson. Matching the mean is not equality in law.

---

## 8. Structural characterizations used in Exam P

| Verbal regime | Mathematical construction | Decisive boundary |
| --- | --- | --- |
| fixed number of independent identical trials | sum of iid Bernoulli variables | independence and common $p$ |
| trials until the $r$-th success | hitting time $T_r$ | trials versus failures convention |
| sample from a finite population without replacement | pushforward of the uniform law on subsets or ordered samples | negative dependence |
| independent event counts over disjoint periods | convolution of Poisson laws | independent increments must be stated |
| heterogeneous policy class | mixture of conditional laws | mixture is not a family member by default |
| observed positive-mass category | normalized restriction | denominator must be positive |
| nonlinear benefit or cost | pushforward $g_\#\mu_X$ and $\mathbb E[g(X)]$ | not $g(\mathbb E[X])$ |
| joint table | atomic measure on $E\times F$ | marginals do not encode dependence |

The Exam P calculation runs from the right representation to a finite sum. The measure-theoretic analysis runs in the opposite direction and determines whether that representation is legitimate.

---

## 9. Terminal approximation: the CLT boundary

Let $X_1,X_2,\ldots$ be iid with mean $m$ and variance $0<\sigma^2<\infty$, and let $S_n=\sum_{i=1}^nX_i$. Then

$$
\frac{S_n-nm}{\sigma\sqrt n}
\Longrightarrow
\mathcal N(0,1).
$$

For a unit-lattice integer-valued sum, the Exam P normal approximation typically replaces

$$
\mathbb P(a\le S_n\le b)
$$

by

$$
\Phi\!\left(\frac{b+\tfrac12-nm}{\sigma\sqrt n}\right)
-
\Phi\!\left(\frac{a-\tfrac12-nm}{\sigma\sqrt n}\right).
$$

This is an approximation, not a pushforward identity. The theorem requires finite, nonzero variance; its statement alone supplies no universal numerical error bound. A small or severely skewed count can remain badly approximated. The present module deploys the formula but does not develop weak-convergence theory.

---

## 10. Boundary ledger

Before using a named discrete law, the following objects must be recoverable:

1. the state space and exact support;
2. the probability measure or pmf and its normalization;
3. the construction that licenses the family name;
4. the product or dependence hypothesis behind any sum;
5. the event and positive denominator behind conditioning;
6. the function whose pushforward or expectation is required;
7. the parameter convention at degenerate endpoints;
8. whether the final step is an identity or an approximation.

The companion deployment is [Discrete Distributions — One-Week Deployment Route](../../60_Applications/Exam-P-Bridges/Discrete%20Distributions%20—%20One-Week%20Deployment%20Route.md). The official boundary is the [July 2026 Exam P syllabus](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf).
