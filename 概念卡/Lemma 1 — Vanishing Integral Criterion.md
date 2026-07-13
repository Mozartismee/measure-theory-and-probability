# Lemma 1 — Vanishing Integral Criterion

Let $(E,\mathcal A,\mu)$ be a measure space.

## Lemma 1.1 — Vanishing Nonnegative Functions

Let $h:E\to[0,+\infty]$ be measurable. Then

$$
\int_E h\,d\mu=0
\quad\Longleftrightarrow\quad
h=0
\quad\mu\text{-a.e.}
$$

### Proof

If $h=0$ $\mu$-a.e., then

$$
\int_E h\,d\mu=0.
$$

Conversely, suppose that

$$
\int_E h\,d\mu=0.
$$

For every $n\ge 1$, set

$$
A_n:=\left\{h\ge\frac1n\right\}.
$$

Since $h\ge 1/n$ on $A_n$,

$$
0
=
\int_E h\,d\mu
\ge
\int_{A_n}h\,d\mu
\ge
\frac1n\mu(A_n).
$$

Hence

$$
\mu(A_n)=0
\qquad
\text{for every }n\ge1.
$$

Moreover,

$$
\{h>0\}
=
\bigcup_{n\ge1}A_n.
$$

Therefore

$$
\mu(\{h>0\})=0,
$$

so $h=0$ $\mu$-a.e. $\square$

## Corollary 1.2 — Almost-Everywhere Equality

Let $f,g:E\to\mathbb R$ be measurable. Then

$$
f=g
\quad\mu\text{-a.e.}
\quad\Longleftrightarrow\quad
\int_E |f-g|\,d\mu=0.
$$

### Proof

The function

$$
h:=|f-g|
$$

is measurable and nonnegative. By Lemma 1.1,

$$
\int_E |f-g|\,d\mu=0
\quad\Longleftrightarrow\quad
|f-g|=0
\quad\mu\text{-a.e.},
$$

which is equivalent to

$$
f=g
\quad\mu\text{-a.e.}
$$

$\square$

## Reconstruction

For $h=|f-g|$,

$$
\int_E |f-g|\,d\mu=0
\quad\Longleftrightarrow\quad
h=0
\quad\mu\text{-a.e.}
\quad\Longleftrightarrow\quad
f=g
\quad\mu\text{-a.e.}
$$

The only non-formal step is Lemma 1.1, whose mechanism is

$$
\int_E h\,d\mu=0
\Longrightarrow
\mu\!\left(\left\{h\ge\frac1n\right\}\right)=0
\quad(n\ge1)
\Longrightarrow
\mu(\{h>0\})=0.
$$
