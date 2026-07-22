---
type: corrige
module: radon-nikodym
status: canonical
td: "TD 01 — Boundary and Local Domination"
---

# Corrigé — TD 01: Boundary and Local Domination

## Exercise 0 — Failure without $\sigma$-finiteness

### 1. Absolute continuity

Let $B\in\mathcal B([0,1])$. If $\mu(B)=0$ for counting measure, then $B=\varnothing$. Hence

$$
\lambda(B)=0.
$$

Therefore

$$
\lambda\ll\mu.
$$

### 2. Nonexistence of a density

Assume that $\lambda=f\mu$ for some measurable $f\ge0$. For every $x\in[0,1]$,

$$
0
=
\lambda(\{x\})
=
\int_{\{x\}}f\,d\mu
=
f(x).
$$

Thus $f=0$ pointwise. It follows that $f\mu=0$, contradicting

$$
\lambda([0,1])=1.
$$

### 3. The broken hypothesis

Counting measure on the uncountable set $[0,1]$ is not $\sigma$-finite. Indeed, every set of finite counting measure is finite, and a countable union of finite sets is countable. It cannot cover $[0,1]$.

Thus absolute continuity alone does not produce a density outside the $\sigma$-finite regime used by the theorem.

## Exercise 1 — Hahn decomposition and domination

Let

$$
\sigma_c=\rho-c\mu
$$

and let $E=P_c\sqcup N_c$ be a Hahn decomposition.

### 1. The two regional inequalities

For every $A\in\mathcal A$, positivity of $P_c$ gives

$$
0
\le
\sigma_c(A\cap P_c)
=
\rho(A\cap P_c)-c\mu(A\cap P_c).
$$

Hence

$$
c\mu(A\cap P_c)
\le
\rho(A\cap P_c)
\le
\rho(A),
$$

which means

$$
\boxed{
c\mathbf1_{P_c}\mu\le\rho
}.
$$

Likewise, negativity of $N_c$ gives

$$
0
\ge
\sigma_c(A\cap N_c)
=
\rho(A\cap N_c)-c\mu(A\cap N_c),
$$

so

$$
\boxed{
\rho|_{N_c}\le c\mu|_{N_c}
}.
$$

### 2. Vanishing of the positive region

Assume $\rho\ll\mu$ and $\mu(P_c)=0$. Then $\rho(P_c)=0$. Therefore, for every $A$,

$$
\begin{aligned}
\rho(A)
&=\rho(A\cap P_c)+\rho(A\cap N_c)\\
&=\rho(A\cap N_c)\\
&\le c\mu(A\cap N_c)\\
&\le c\mu(A).
\end{aligned}
$$

Thus

$$
\boxed{
\rho\le c\mu
}.
$$

## Exercise 2 — Extraction and improvement

Let

$$
\rho=\nu-g\mu.
$$

Since $g\mu\le\nu$, the set function $\rho$ is a finite positive measure. Moreover, if $\mu(A)=0$, then both $\nu(A)$ and $(g\mu)(A)$ vanish, so

$$
\rho\ll\mu.
$$

### 1. Extraction of a local fragment

Assume $\rho\ne0$. For each $n\ge1$, choose a Hahn decomposition

$$
E=P_n\sqcup N_n
$$

for

$$
\rho-\frac1n\mu.
$$

Suppose, for contradiction, that $\mu(P_n)=0$ for every $n$. Absolute continuity gives

$$
\rho(P_n)=0.
$$

On the negative region $N_n$,

$$
\rho|_{N_n}
\le
\frac1n\mu|_{N_n}.
$$

Hence, for every $A$,

$$
\rho(A)
=
\rho(A\cap N_n)
\le
\frac1n\mu(A).
$$

Taking $A=E$ gives

$$
0<\rho(E)
\le
\frac1n\mu(E)
$$

for every $n$, impossible because $\mu(E)<+\infty$.

Therefore $\mu(P_n)>0$ for some $n$. Set

$$
\varepsilon=\frac1n,
\qquad
P=P_n.
$$

Positivity of $P_n$ gives

$$
\boxed{
\mu(P)>0,
\qquad
\varepsilon\mathbf1_P\mu\le\rho
}.
$$

### 2. Strict improvement

If $\nu\ne g\mu$, then $\rho\ne0$. Choose $\varepsilon$ and $P$ as above and define

$$
h=g+\varepsilon\mathbf1_P.
$$

Then

$$
h\mu
=
g\mu+\varepsilon\mathbf1_P\mu
\le
g\mu+\rho
=
\nu.
$$

Moreover,

$$
\int_Eh\,d\mu
=
\int_Eg\,d\mu
+
\varepsilon\mu(P)
>
\int_Eg\,d\mu.
$$

Conversely, if $\nu=g\mu$ and $h\mu\le\nu$, then

$$
\int_Eh\,d\mu
=(h\mu)(E)
\le
\nu(E)
=(g\mu)(E)
=
\int_Eg\,d\mu.
$$

Thus the two alternatives are mutually exclusive and exhaustive.

## Reconstruction — Local domination

Starting from

$$
\nu\ne g\mu,
$$

form the nonzero residue

$$
\rho=\nu-g\mu.
$$

For each $n$, the sign of

$$
\rho-\frac1n\mu
$$

produces a positive Hahn region $P_n$. If every such region were $\mu$-null, absolute continuity would remove it and negativity on the complement would force

$$
\rho\le\frac1n\mu
$$

for every $n$. Finiteness would then force $\rho=0$. Hence one region satisfies

$$
\frac1n\mathbf1_{P_n}\mu\le\rho,
\qquad
\mu(P_n)>0.
$$

Adding this fragment to $g$ gives a strictly larger representable submeasure. The roles of the hypotheses are exact:

- Hahn decomposition supplies the sign region;
- $\rho\ll\mu$ removes a $\mu$-null positive region;
- finiteness turns $\rho\le n^{-1}\mu$ for every $n$ into $\rho=0$.
