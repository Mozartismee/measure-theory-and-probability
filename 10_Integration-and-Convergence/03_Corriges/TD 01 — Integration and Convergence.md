---
type: corrige
module: integration-and-convergence
status: canonical
td: "TD 01 — Integration and Convergence"
---

# Corrigé — TD 01: Integration and Convergence

## Exercise 0 — Pointwise convergence is insufficient

Let

$$
f_n=n\mathbf1_{(0,1/n)}.
$$

### 1. Almost-everywhere convergence

Fix $x\in(0,1)$. For $n>1/x$, one has $1/n<x$, so $x\notin(0,1/n)$. Hence

$$
f_n(x)=0
$$

for all sufficiently large $n$. Therefore $f_n\to0$ pointwise on $(0,1)$.

### 2. Integrals

For every $n$,

$$
\int_0^1f_n\,d\lambda
=
n\lambda((0,1/n))
=1.
$$

Thus the integrals do not converge to the integral of the pointwise limit.

### 3. No common integrable dominator

Suppose $g\ge f_n$ almost everywhere for every $n$. On

$$
I_n=\left(\frac1{n+1},\frac1n\right),
$$

one has $f_n=n$, hence $g\ge n$ almost everywhere on $I_n$. Since the intervals are disjoint,

$$
\begin{aligned}
\int_0^1g\,d\lambda
&\ge
\sum_{n\ge1}n\lambda(I_n)\\
&=
\sum_{n\ge1}
n\left(\frac1n-\frac1{n+1}\right)\\
&=
\sum_{n\ge1}\frac1{n+1}
=+\infty.
\end{aligned}
$$

Therefore no common integrable dominator exists.

### 4. The theorem-selection failure

MCT does not apply because $(f_n)$ is not increasing. DCT does not apply because there is no common $L^1$ dominator. Pointwise convergence alone has no integral consequence.

## Exercise 1 — MCT as a measure-construction engine

Let

$$
\nu(A)=\int_Af\,d\mu,
\qquad f\ge0.
$$

### 1. Finite additivity

If $A\cap B=\varnothing$, then

$$
\mathbf1_{A\cup B}f
=
\mathbf1_Af+\mathbf1_Bf.
$$

Linearity of the nonnegative integral gives

$$
\nu(A\cup B)=\nu(A)+\nu(B).
$$

### 2–3. Countable additivity

For pairwise disjoint $(A_n)$ and

$$
B_N=\bigcup_{n=1}^NA_n,
$$

one has

$$
\mathbf1_{B_N}f
=
\sum_{n=1}^N\mathbf1_{A_n}f.
$$

Moreover,

$$
\mathbf1_{B_N}f
\uparrow
\mathbf1_{\bigcup_{n\ge1}A_n}f.
$$

MCT gives

$$
\begin{aligned}
\nu\left(\bigcup_{n\ge1}A_n\right)
&=
\lim_{N\to\infty}\int_E\mathbf1_{B_N}f\,d\mu\\
&=
\lim_{N\to\infty}\sum_{n=1}^N\nu(A_n)\\
&=
\sum_{n\ge1}\nu(A_n).
\end{aligned}
$$

### 4. Absolute continuity

If $\mu(A)=0$, then every nonnegative measurable function has integral zero over $A$. Hence

$$
\nu(A)=\int_Af\,d\mu=0,
$$

so

$$
\nu\ll\mu.
$$

## Exercise 2 — Fatou from MCT

### 1. Derivation

Define

$$
g_n=\inf_{k\ge n}f_k.
$$

Then $(g_n)$ is measurable and

$$
g_n\uparrow\liminf_{n\to\infty}f_n.
$$

For every $k\ge n$, $g_n\le f_k$, hence

$$
\int_Eg_n\,d\mu
\le
\inf_{k\ge n}\int_Ef_k\,d\mu.
$$

MCT gives

$$
\int_E\liminf_nf_n\,d\mu
=
\lim_n\int_Eg_n\,d\mu
\le
\lim_n\inf_{k\ge n}\int_Ef_k\,d\mu.
$$

The last term is $\liminf_n\int f_n$, proving Fatou.

### 2. Strict inequality

On $(\mathbb R,\mathcal B(\mathbb R),\lambda)$, let

$$
f_n=\mathbf1_{[n,n+1]}.
$$

Then $f_n(x)\to0$ for every $x$, while

$$
\int_{\mathbb R}f_n\,d\lambda=1.
$$

Thus

$$
0
=
\int\liminf_nf_n,d\lambda
<
\liminf_n\int f_n,d\lambda
=1.
$$

### 3. Sets

Since

$$
\mathbf1_{\liminf A_n}
=
\liminf_n\mathbf1_{A_n},
$$

Fatou gives

$$
\mu(\liminf A_n)
\le
\liminf_n\mu(A_n).
$$

### 4. Signed lower bounds

If there exists $h\in L^1(\mu)$ such that

$$
f_n\ge h
$$

almost everywhere for every $n$, apply Fatou to the nonnegative sequence $f_n-h$. Since

$$
\liminf_n(f_n-h)
=
\liminf_nf_n-h,
$$

one obtains

$$
\int_E\liminf_nf_n\,d\mu
\le
\liminf_n\int_Ef_n\,d\mu,
$$

whenever the displayed integrals are defined. The integrable lower bound prevents an undefined negative part.

## Exercise 3 — DCT from Fatou

Since $f_n\to f$ almost everywhere and $|f_n|\le g$, one has $|f|\le g$, hence $f\in L^1$.

### 1–2. Convergence of integrals

Apply Fatou to $g+f_n$:

$$
\int_E(g+f)\,d\mu
\le
\liminf_n\int_E(g+f_n)\,d\mu.
$$

After subtracting $\int g$,

$$
\int_Ef\,d\mu
\le
\liminf_n\int_Ef_n\,d\mu.
$$

Apply Fatou to $g-f_n$:

$$
\int_E(g-f)\,d\mu
\le
\liminf_n\int_E(g-f_n)\,d\mu.
$$

This rearranges to

$$
\limsup_n\int_Ef_n\,d\mu
\le
\int_Ef\,d\mu.
$$

Therefore

$$
\int_Ef_n\,d\mu
\longrightarrow
\int_Ef\,d\mu.
$$

### 3. $L^1$ convergence

One has

$$
|f_n-f|
\longrightarrow0
$$

almost everywhere and

$$
|f_n-f|
\le
2g
\in L^1.
$$

DCT gives

$$
\|f_n-f\|_1
=
\int_E|f_n-f|\,d\mu
\longrightarrow0.
$$

### 4. A nonintegrable dominator is insufficient

Again take

$$
f_n=n\mathbf1_{(0,1/n)}
$$

on $(0,1)$. The sequence converges pointwise to zero and satisfies

$$
f_n(x)
\le
\frac1x,
$$

but $x\mapsto1/x$ is not integrable on $(0,1)$. The integrals of $f_n$ remain equal to one.

## Exercise 4 — Uniform absolute continuity of the integral

### 1. Tail integral

The functions

$$
|f|\mathbf1_{\{|f|>M\}}
$$

converge pointwise to zero as $M\to+\infty$ and are dominated by $|f|\in L^1$. Therefore DCT gives

$$
\int_{\{|f|>M\}}|f|\,d\mu
\longrightarrow0.
$$

### 2. Uniform control on small sets

Fix $\varepsilon>0$. Choose $M>0$ such that

$$
\int_{\{|f|>M\}}|f|\,d\mu
<
\frac\varepsilon2.
$$

For any measurable $A$,

$$
\begin{aligned}
\int_A|f|\,d\mu
&=
\int_{A\cap\{|f|\le M\}}|f|\,d\mu
+
\int_{A\cap\{|f|>M\}}|f|\,d\mu\\
&\le
M\mu(A)
+
\frac\varepsilon2.
\end{aligned}
$$

Taking

$$
\delta=\frac{\varepsilon}{2M}
$$

proves the assertion.

### 3. Quantitative versus qualitative absolute continuity

The relation

$$
f\mu\ll\mu
$$

only says that $\mu(A)=0$ implies $(f\mu)(A)=0$. Uniform absolute continuity says that sufficiently small positive $\mu(A)$ forces uniformly small

$$
\int_A|f|\,d\mu.
$$

The latter is quantitative and uses integrability of $f$.

## Exercise 5 — Series and exchange of integral

### 1. Nonnegative series

Let

$$
S_N=\sum_{n=1}^Nf_n.
$$

If $f_n\ge0$, then $S_N\uparrow\sum_{n\ge1}f_n$. MCT gives

$$
\int_E\sum_{n\ge1}f_n\,d\mu
=
\lim_N\int_ES_N\,d\mu
=
\sum_{n\ge1}\int_Ef_n\,d\mu.
$$

### 2. Absolute convergence and $L^1$ convergence

Apply the preceding result to $|f_n|$:

$$
\int_E\sum_{n\ge1}|f_n|\,d\mu
=
\sum_{n\ge1}\int_E|f_n|\,d\mu
<+\infty.
$$

Hence

$$
\sum_{n\ge1}|f_n|<+\infty
$$

almost everywhere. Define $S=\sum_nf_n$ on this full-measure set. Then

$$
|S-S_N|
\le
\sum_{n>N}|f_n|,
$$

so

$$
\|S-S_N\|_1
\le
\sum_{n>N}\|f_n\|_1
\longrightarrow0.
$$

Thus the series converges absolutely almost everywhere and in $L^1$.

### 3. Exchange of sum and integral

Since $S_N\to S$ in $L^1$,

$$
\left|
\int_ES_N\,d\mu
-
\int_ES\,d\mu
\right|
\le
\|S_N-S\|_1
\longrightarrow0.
$$

But

$$
\int_ES_N\,d\mu
=
\sum_{n=1}^N\int_Ef_n\,d\mu.
$$

Therefore

$$
\boxed{
\int_E\sum_{n\ge1}f_n\,d\mu
=
\sum_{n\ge1}\int_Ef_n\,d\mu
}.
$$

## Reconstruction

MCT is built into the nonnegative integral and supplies countable additivity for density-generated measures. Fatou is MCT applied to the increasing tail infima

$$
g_n=\inf_{k\ge n}f_k.
$$

DCT is obtained by applying Fatou to the two nonnegative sequences

$$
g+f_n,
\qquad
g-f_n,
$$

and then to $|f_n-f|\le2g$.

For $f\ge0$, countable additivity of

$$
A\longmapsto\int_Af\,d\mu
$$

is MCT applied to the partial unions of disjoint sets. The convergence theorem is not an ornament attached after measure construction; it is the engine of the construction itself.
