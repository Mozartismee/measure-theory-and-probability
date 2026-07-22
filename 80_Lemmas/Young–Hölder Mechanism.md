---
type: lemma
module: lemmas
status: canonical
---

# Lemma 3 — The Young–Hölder Mechanism

Let $(E,\mathcal A,\mu)$ be a measure space. The purpose of this lemma is to isolate the scalar inequality and the normalization argument from which Hölder's inequality is reconstructed.

## Definition 3.1 — Conjugate Exponents

Let

$$
1<p<+\infty,
\qquad
q=\frac{p}{p-1}.
$$

Then

$$
\frac1p+\frac1q=1,
$$

and $p,q$ are called conjugate exponents.

## Proposition 3.2 — Young's Inequality

Let $p,q$ be conjugate exponents. For every $a,b\ge0$,

$$
ab
\le
\frac{a^p}{p}
+
\frac{b^q}{q}.
$$

Equality holds if and only if

$$
a^p=b^q.
$$

### Proof

The weighted arithmetic–geometric mean inequality gives, for $u,v\ge0$,

$$
u^{1/p}v^{1/q}
\le
\frac{u}{p}+\frac{v}{q}.
$$

Apply it with

$$
u=a^p,
\qquad
v=b^q.
$$

Then $u^{1/p}v^{1/q}=ab$, which proves the inequality. Equality in weighted arithmetic–geometric mean holds exactly when $u=v$, hence exactly when $a^p=b^q$. $\square$

## Theorem 3.3 — Hölder's Inequality

Let $p,q$ be conjugate exponents. If

$$
f\in L^p(\mu),
\qquad
g\in L^q(\mu),
$$

then $fg\in L^1(\mu)$ and

$$
\boxed{
\|fg\|_1
\le
\|f\|_p\|g\|_q
}.
$$

If neither $f$ nor $g$ is zero in its respective equivalence class, equality holds if and only if

$$
\frac{|f|^p}{\|f\|_p^p}
=
\frac{|g|^q}{\|g\|_q^q}
\qquad
\mu\text{-a.e.}
$$

### Proof

If one of the two norms is zero, then $fg=0$ $\mu$-a.e., and the conclusion is immediate. Assume therefore that both norms are nonzero, and define

$$
F:=\frac{|f|}{\|f\|_p},
\qquad
G:=\frac{|g|}{\|g\|_q}.
$$

By Proposition 3.2,

$$
FG
\le
\frac{F^p}{p}
+
\frac{G^q}{q}.
$$

Integration gives

$$
\int_E FG\,d\mu
\le
\frac1p\int_EF^p\,d\mu
+
\frac1q\int_EG^q\,d\mu
=
\frac1p+\frac1q
=1.
$$

Multiplying by $\|f\|_p\|g\|_q$ yields

$$
\int_E|fg|\,d\mu
\le
\|f\|_p\|g\|_q.
$$

In particular, $fg\in L^1(\mu)$.

Set

$$
H:=\frac{F^p}{p}+\frac{G^q}{q}-FG.
$$

Then $H\ge0$, and equality in the integrated estimate is equivalent to

$$
\int_EH\,d\mu=0.
$$

By [Lemma 1.1](Vanishing%20Integral%20Criterion.md), this holds if and only if $H=0$ $\mu$-a.e. Proposition 3.2 then shows that equality holds precisely when

$$
F^p=G^q
\qquad
\mu\text{-a.e.}
$$

This is exactly the stated equality condition. $\square$

## Proposition 3.4 — Endpoint Hölder Inequality

If

$$
f\in L^1(\mu),
\qquad
g\in L^\infty(\mu),
$$

then $fg\in L^1(\mu)$ and

$$
\boxed{
\|fg\|_1
\le
\|f\|_1\|g\|_\infty
}.
$$

### Proof

By the definition of the essential supremum,

$$
|g|
\le
\|g\|_\infty
\qquad
\mu\text{-a.e.}
$$

Therefore

$$
|fg|
\le
\|g\|_\infty |f|
\qquad
\mu\text{-a.e.}
$$

and integration gives the result. $\square$

## Reconstruction

The non-endpoint argument is the chain

$$
\frac1p+\frac1q=1
\longrightarrow
ab\le\frac{a^p}{p}+\frac{b^q}{q}
\longrightarrow
F=\frac{|f|}{\|f\|_p},\quad
G=\frac{|g|}{\|g\|_q}
\longrightarrow
\int_EFG\,d\mu\le1
\longrightarrow
\|fg\|_1\le\|f\|_p\|g\|_q.
$$

The endpoint case does not use Young's inequality. It follows directly from

$$
|g|\le\|g\|_\infty
\qquad
\mu\text{-a.e.}
$$
