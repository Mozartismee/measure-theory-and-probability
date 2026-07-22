---
type: example-pair
module: examples-and-counterexamples
status: canonical
example-pair: 1
competency-keys:
  - CE.finite-sigma-fields
  - CE.rn-construction
---

# Example Pair 1 — Finite Partitions: Determined Values and Null-Atom Freedom

## Setup

Let

$$
\Omega=\{\omega_0,\omega_1,\omega_2,\omega_3\},
\qquad
\mathcal F=2^\Omega,
$$

and define a probability measure by

$$
\mathbb P(\{\omega_0\})=0,
\quad
\mathbb P(\{\omega_1\})=\mathbb P(\{\omega_2\})=\frac14,
\quad
\mathbb P(\{\omega_3\})=\frac12.
$$

Set

$$
B_0=\{\omega_0\},
\qquad
B_1=\{\omega_1,\omega_2\},
\qquad
B_2=\{\omega_3\},
\qquad
\mathcal G=\sigma(B_0,B_1,B_2),
$$

and let

$$
Y(\omega_0)=7,
\qquad
Y(\omega_1)=0,
\qquad
Y(\omega_2)=2,
\qquad
Y(\omega_3)=4.
$$

Since $\Omega$ is finite, $Y\in L^1(\mathbb P)$. On $(\Omega,\mathcal G)$ define the finite signed numerator

$$
\nu_Y(C)=\mathbb E[Y\mathbf1_C],
\qquad C\in\mathcal G.
$$

The reference measure is $\mathbb P|_{\mathcal G}$, and the Radon–Nikodym derivative is unique $\mathbb P|_{\mathcal G}$-almost everywhere, equivalently $\mathbb P$-almost surely.

## Positive regime

Every real-valued $\mathcal G$-measurable function is constant on each atom, hence has the form

$$
Z=a_0\mathbf1_{B_0}+a_1\mathbf1_{B_1}+a_2\mathbf1_{B_2}.
$$

The defining identity on the two positive-mass atoms gives

$$
a_1\mathbb P(B_1)
=
\mathbb E[Y\mathbf1_{B_1}]
=
0\cdot\frac14+2\cdot\frac14
=
\frac12,
$$

so $a_1=1$, and

$$
a_2\mathbb P(B_2)
=
\mathbb E[Y\mathbf1_{B_2}]
=
4\cdot\frac12
=
2,
$$

so $a_2=4$. Division is legitimate precisely because $\mathbb P(B_1),\mathbb P(B_2)>0$.

For every $c\in\mathbb R$, define

$$
Z_c
=
\mathbf1_{B_1}+4\mathbf1_{B_2}+c\mathbf1_{B_0}.
$$

Then $Z_c$ is $\mathcal G$-measurable and integrable. Every $C\in\mathcal G$ is an atom-union

$$
C=\bigcup_{i\in I}B_i
$$

for some $I\subseteq\{0,1,2\}$. Therefore

$$
\int_C Z_c\,d\mathbb P
=
\sum_{i\in I}\int_{B_i}Z_c\,d\mathbb P
=
\sum_{i\in I}\int_{B_i}Y\,d\mathbb P
=
\int_CY\,d\mathbb P.
$$

Thus every $Z_c$ is a version of $\mathbb E[Y\mid\mathcal G]$.

## Failure regime

The removed hypothesis is positive mass of $B_0$. Since $\mathbb P(B_0)=0$, the atomwise defining equation is only

$$
c\mathbb P(B_0)
=
\mathbb E[Y\mathbf1_{B_0}],
\qquad\text{that is,}\qquad
0=0.
$$

It imposes no pointwise value on $B_0$. Conversely, the positive-mass calculations force every version to equal $1$ on $B_1$ and $4$ on $B_2$, so the complete family of versions is

$$
\boxed{
\mathbb E[Y\mid\mathcal G]
=
\mathbf1_{B_1}+4\mathbf1_{B_2}+c\mathbf1_{B_0},
\qquad c\in\mathbb R.
}
$$

If $c,d\in\mathbb R$, then

$$
\|Z_c-Z_d\|_{L^1(\mathbb P)}
=
|c-d|\mathbb P(B_0)
=
0.
$$

Hence different pointwise representatives define the same $L^1(\mathbb P)$ equivalence class.

## Decisive mechanism

On a finite partition, conditional expectation is the Radon–Nikodym derivative of $\nu_Y$ with respect to $\mathbb P|_{\mathcal G}$. The atomwise identity

$$
a_i\mathbb P(B_i)=\nu_Y(B_i)
$$

determines $a_i$ exactly when $\mathbb P(B_i)>0$. A null atom is invisible to both measures and therefore to the derivative's almost-everywhere class.

## Boundary

The conclusion is pointwise on positive-mass atoms but only $\mathbb P$-almost sure globally. If every atom had positive mass, the representative would be pointwise unique. No conditional kernel or disintegration is constructed here; the object is the $L^1(\Omega,\mathcal G,\mathbb P|_{\mathcal G})$ conditional-expectation class.

The general formula is governed by the [Conditional Expectation Cours](../40_Conditional-Expectation/01_Cours/Cours.md) and [Finite Sigma-Fields TD](../40_Conditional-Expectation/02_TD/TD%2002%20—%20Finite%20Sigma-Fields.md).

## Reconstruction

$$
\mathcal G\text{-measurability}
\longrightarrow
\text{one coefficient per atom}
\longrightarrow
a_i\mathbb P(B_i)=\mathbb E[Y\mathbf1_{B_i}]
\longrightarrow
\begin{cases}
\text{unique coefficient},&\mathbb P(B_i)>0,\\
\text{arbitrary representative value},&\mathbb P(B_i)=0.
\end{cases}
$$
