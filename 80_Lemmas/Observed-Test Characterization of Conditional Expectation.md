---
type: lemma
module: lemmas
status: canonical
---

# Lemma 7 — Observed-Test Characterization of Conditional Expectation

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space, let
$\mathcal G\subseteq\mathcal F$ be a sub-$\sigma$-field, and let
$Y,Z\in L^1(\mathbb P)$ with $Z$ $\mathcal G$-measurable.

The following assertions are equivalent:

1. $Z=\mathbb E[Y\mid\mathcal G]$;

2. for every $A\in\mathcal G$,

   $$
   \mathbb E[(Y-Z)\mathbf1_A]=0;
   $$

3. for every bounded $\mathcal G$-measurable random variable $H$,

   $$
   \mathbb E[(Y-Z)H]=0.
   $$

Equivalently, $Y$ and its conditional expectation have the same pairing
against every bounded test that uses only the information in $\mathcal G$.

## Proof

The equivalence of assertions 1 and 2 is the defining integral identity for
conditional expectation.

Assume assertion 2 and set $W=Y-Z\in L^1(\mathbb P)$. By linearity,

$$
\mathbb E[WS]=0
$$

for every $\mathcal G$-measurable simple random variable $S$.

Let $H$ be bounded and $\mathcal G$-measurable. Choose
$\mathcal G$-measurable simple random variables $(H_n)_{n\ge1}$ such that

$$
\|H_n-H\|_\infty\longrightarrow0.
$$

Then

$$
\left|
\mathbb E[WH]-\mathbb E[WH_n]
\right|
\leq
\|H-H_n\|_\infty\|W\|_1
\longrightarrow0.
$$

Since $\mathbb E[WH_n]=0$ for every $n$, assertion 3 follows. Conversely,
assertion 3 applied to $H=\mathbf1_A$ gives assertion 2.

It remains to record the uniqueness mechanism. Suppose that $Z_1,Z_2\in
L^1(\mathbb P)$ are $\mathcal G$-measurable and both satisfy assertion 2 for
the same $Y$. Set $D=Z_1-Z_2$. Then

$$
\mathbb E[D\mathbf1_A]=0
\qquad
\text{for every }A\in\mathcal G.
$$

Taking $A=\{D>0\}\in\mathcal G$ gives

$$
\mathbb E[D\mathbf1_{\{D>0\}}]=0.
$$

The integrand is nonnegative, so the [vanishing integral
criterion](Vanishing%20Integral%20Criterion.md) yields $D\leq0$ almost surely.
Applying the same argument to $-D$ gives $D\geq0$ almost surely. Hence

$$
Z_1=Z_2
\qquad
\mathbb P\text{-almost surely}.
$$

$\square$

## Structural Use

The lemma closes the chain

$$
\text{Radon--Nikodym candidate}
\longrightarrow
\text{identities against observed tests}
\longrightarrow
\text{almost-sure uniqueness}.
$$

Finite-partition formulas use indicators of the atoms; the pull-out property
absorbs a bounded $\mathcal G$-measurable factor into the test; the tower property
restricts the test class to a smaller $\sigma$-field; preservation of the mean
is the case $H=1$.

## Boundary

The $\mathcal G$-measurability of $Z$ is essential. If $\mathcal G$ is the
trivial $\sigma$-field, every nonzero centered integrable random variable $W$
satisfies

$$
\mathbb E[WH]=0
$$

for every bounded $\mathcal G$-measurable $H$, although $W$ need not vanish.
Thus observed tests determine the $\mathcal G$-measurable representative, not
an arbitrary integrable random variable.

Unbounded tests require separate integrability hypotheses on the products and
are not part of the lemma.

## Reconstruction

The mechanism is

$$
\text{indicators}
\longrightarrow
\text{simple tests}
\longrightarrow
\text{bounded observed tests}
\longrightarrow
\text{uniqueness on }L^1(\mathcal G).
$$

This is the characteristic property isolated in
[Le Gall, Theorem and Definition 11.2.1](../99_Sources/ENS/Le%20Gall（法文原版%20建議使用）.pdf),
equations (11.1)--(11.2).
