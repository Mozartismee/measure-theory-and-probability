---
type: corrige
module: signed-measures
status: canonical
td: "TD 01 — Hahn–Jordan Structure and Domination"
---

# Corrigé — TD 01: Hahn–Jordan Structure and Domination

## Exercise 1 — Positive, negative and null sets

### 1. Heredity

If $P$ is positive and $B\subseteq P$ is measurable, then every measurable $A\subseteq B$ also satisfies $A\subseteq P$, hence $\sigma(A)\ge0$. Thus $B$ is positive. The negative case is identical with the inequality reversed.

### 2. Countable unions

Let $(P_n)_{n\ge1}$ be positive and let $A$ be a measurable subset of $\bigcup_nP_n$. Define disjoint sets

$$
B_1=A\cap P_1,
$$

and, for $n\ge2$,

$$
B_n
=
A\cap
\left(
P_n\setminus\bigcup_{k<n}P_k
\right).
$$

Then $B_n\subseteq P_n$, so $\sigma(B_n)\ge0$, and

$$
A=\bigsqcup_{n\ge1}B_n.
$$

Countable additivity gives

$$
\sigma(A)=\sum_{n\ge1}\sigma(B_n)\ge0.
$$

Therefore $\bigcup_nP_n$ is positive. Applying the same construction to negative sets gives a sum of nonpositive terms, so a countable union of negative sets is negative.

### 3. Intersection of opposite signs

Every measurable subset of $P\cap N$ is contained both in a positive set and in a negative set. Its signed mass is therefore simultaneously nonnegative and nonpositive, hence zero. Thus $P\cap N$ is $\sigma$-null.

### 4. Zero total mass is insufficient

The equality $\sigma(Z)=0$ allows cancellation between positive and negative parts inside $Z$. To be $\sigma$-null, every measurable subset $A\subseteq Z$ must satisfy $\sigma(A)=0$. For example, for

$$
\sigma=\delta_0-\delta_1,
$$

the set $\{0,1\}$ has signed mass zero but is not $\sigma$-null, since $\sigma(\{0\})=1$.

## Exercise 2 — Ambiguity of Hahn sets and canonicity of Jordan measures

### 1. Ambiguity of Hahn decompositions

The set

$$
P\setminus P'=P\cap N'
$$

is contained in the positive set $P$ and in the negative set $N'$. It is therefore $\sigma$-null. Likewise,

$$
P'\setminus P=P'\cap N
$$

is $\sigma$-null. Hence $P\triangle P'$ is $\sigma$-null. The same argument applies to $N\triangle N'$.

### 2. Construction of the Jordan measures

If $(A_n)$ are pairwise disjoint, then so are $(A_n\cap P)$, and therefore

$$
\sigma^+\left(\bigcup_nA_n\right)
=
\sum_n\sigma^+(A_n).
$$

Positivity of $P$ implies $\sigma^+(A)\ge0$. Thus $\sigma^+$ is a positive measure. Similarly, $\sigma^-$ is a positive measure.

Since $A=(A\cap P)\sqcup(A\cap N)$,

$$
\sigma(A)
=
\sigma(A\cap P)+\sigma(A\cap N)
=
\sigma^+(A)-\sigma^-(A).
$$

### 3. Independence of the Hahn decomposition

The symmetric difference $P\triangle P'$ is $\sigma$-null. Hence, for every $A$,

$$
\sigma(A\cap P)
=
\sigma(A\cap P').
$$

Thus the positive measure obtained from $P$ is the same as the one obtained from $P'$. The same applies to the negative measure.

### 4. Minimality

Assume $\sigma=\alpha-\beta$ with $\alpha,\beta\ge0$. For every $A$,

$$
\begin{aligned}
\sigma^+(A)
&=\sigma(A\cap P)\\
&=\alpha(A\cap P)-\beta(A\cap P)\\
&\le\alpha(A\cap P)\\
&\le\alpha(A).
\end{aligned}
$$

Hence $\sigma^+\le\alpha$. Similarly,

$$
\begin{aligned}
\sigma^-(A)
&=-\sigma(A\cap N)\\
&=\beta(A\cap N)-\alpha(A\cap N)\\
&\le\beta(A),
\end{aligned}
$$

so $\sigma^-\le\beta$.

### 5. Uniqueness under mutual singularity

Suppose

$$
\sigma=\alpha-\beta,
\qquad
\alpha\perp\beta.
$$

Choose disjoint measurable sets $S,T$ carrying $\alpha$ and $\beta$, respectively. Then $S$ is positive for $\sigma$ and $T$ is negative, so $(S,T)$ is a Hahn decomposition up to a common null remainder. The construction above therefore gives

$$
\alpha=\sigma^+,
\qquad
\beta=\sigma^-.
$$

Thus the Jordan decomposition is the unique decomposition into mutually singular positive measures.

## Exercise 3 — Signed densities

### 1. Hahn decomposition

If $A\subseteq P=\{f\ge0\}$, then

$$
\sigma_f(A)=\int_Af\,d\mu\ge0.
$$

Thus $P$ is positive. If $A\subseteq N=\{f<0\}$, then $\sigma_f(A)\le0$, so $N$ is negative.

### 2. Jordan measures and total variation

For every $A$,

$$
\sigma_f^+(A)
=
\int_{A\cap P}f\,d\mu
=
\int_Af^+\,d\mu,
$$

and similarly

$$
\sigma_f^-(A)
=
\int_Af^-\,d\mu.
$$

Therefore

$$
\boxed{
\sigma_f^+=f^+\mu,
\qquad
\sigma_f^-=f^-\mu,
\qquad
|\sigma_f|=|f|\mu
}.
$$

### 3. Null sets of a signed density

If $f=0$ almost everywhere on $Z$, then every measurable $A\subseteq Z$ satisfies

$$
\sigma_f(A)=\int_Af\,d\mu=0.
$$

Conversely, suppose that $Z$ is $\sigma_f$-null. Taking

$$
A_+=Z\cap\{f>0\}
$$

gives

$$
0=\int_{A_+}f\,d\mu.
$$

Since the integrand is nonnegative, $f=0$ almost everywhere on $A_+$. The same argument on $A_-=Z\cap\{f<0\}$ shows that $f=0$ almost everywhere there. Hence $f=0$ almost everywhere on $Z$.

### 4. Uniqueness

The equality $\sigma_f=\sigma_g$ means

$$
\int_A(f-g)\,d\mu=0
$$

for every measurable $A$. Choosing $A=\{f>g\}$ and $A=\{f<g\}$ yields $f=g$ almost everywhere.

## Exercise 4 — From sign structure to local domination

### 1. The two inequalities

For every measurable $A$, positivity of $P_c$ gives

$$
0
\le
\tau_c(A\cap P_c)
=
\rho(A\cap P_c)-c\mu(A\cap P_c).
$$

Thus

$$
c\mathbf1_{P_c}\mu(A)
=
c\mu(A\cap P_c)
\le
\rho(A\cap P_c)
\le
\rho(A).
$$

Hence $c\mathbf1_{P_c}\mu\le\rho$.

Likewise, negativity of $N_c$ gives

$$
\rho(A\cap N_c)
\le
c\mu(A\cap N_c),
$$

which is exactly

$$
\rho|_{N_c}\le c\mu|_{N_c}.
$$

### 2. A positive Hahn set must carry mass

Let $P_n$ be positive and $N_n$ negative for

$$
\rho-\frac1n\mu.
$$

Assume for contradiction that $\mu(P_n)=0$ for every $n$. Since $\rho\ll\mu$, one also has $\rho(P_n)=0$. On $N_n$,

$$
\rho|_{N_n}
\le
\frac1n\mu|_{N_n}.
$$

Therefore, for every measurable $A$,

$$
\rho(A)
=
\rho(A\cap P_n)+\rho(A\cap N_n)
\le
\frac1n\mu(A).
$$

In particular,

$$
\rho(E)\le\frac1n\mu(E)
$$

for every $n$. Since $\mu(E)<+\infty$, it follows that $\rho(E)=0$, contradicting $\rho\ne0$.

### 3. Local fragment

Choose $n$ such that $\mu(P_n)>0$. With

$$
\varepsilon=\frac1n,
\qquad
P=P_n,
$$

the positive-set inequality gives

$$
\varepsilon\mathbf1_P\mu\le\rho.
$$

### 4. Dependence of the argument

- Absolute continuity is used to infer $\rho(P_n)=0$ from $\mu(P_n)=0$.
- Finiteness of $\mu$ is used when passing from

  $$
  \rho(E)\le\frac1n\mu(E)
  $$

  for all $n$ to $\rho(E)=0$.
- Finiteness of $\rho$ ensures that $\rho-c\mu$ lies in the finite signed-measure regime used by the stated Hahn theorem.

## Reconstruction — Proof spine

The Hahn sets encode sign but are determined only modulo $\sigma$-null sets. Restricting $\sigma$ to those sets removes cancellation and produces the canonical Jordan measures. Their minimality follows by comparing the restriction of any representation $\sigma=\alpha-\beta$ with the positive and negative Hahn regions.

For $\rho-c\mu$, positivity on $P_c$ becomes

$$
c\mathbf1_{P_c}\mu\le\rho,
$$

while negativity on $N_c$ becomes

$$
\rho|_{N_c}\le c\mu|_{N_c}.
$$

Varying $c=1/n$ and using finiteness plus absolute continuity forces one positive region to have positive $\mu$-mass. This is the local density fragment later consumed by the Radon–Nikodym construction.
