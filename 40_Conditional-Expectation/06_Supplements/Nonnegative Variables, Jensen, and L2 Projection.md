---
type: supplement
module: conditional-expectation
status: canonical
---

# Complement — Nonnegative Variables, Conditional Jensen, and $L^2$ Projection

This supplement extends [the $L^1$ construction of conditional expectation](../01_Cours/Cours.md). It is not required for the basic Radon–Nikodym representation.

## 1. Nonnegative variables

Let

$$
X:\Omega\longrightarrow[0,\infty]
$$

be measurable, without assuming integrability.

Set

$$
X_n=X\wedge n.
$$

Then \(X_n\in L^1(\mathbb P)\) and

$$
X_n\uparrow X.
$$

For each \(n\), monotonicity gives

$$
0
\leq
\mathbb E[X_n\mid\mathcal G]
\leq
\mathbb E[X_{n+1}\mid\mathcal G]
$$

almost surely. Since only countably many inequalities are involved, we may choose versions and modify them on one \(\mathcal G\)-measurable null set so that the sequence is pointwise nonnegative and increasing. Define

$$
Y
=
\lim_{n\to\infty}
\mathbb E[X_n\mid\mathcal G].
$$

Then \(Y:\Omega\to[0,\infty]\) is \(\mathcal G\)-measurable.

For every \(A\in\mathcal G\), MCT gives

$$
\begin{aligned}
\mathbb E[Y\mathbf 1_A]
&=
\lim_{n\to\infty}
\mathbb E[\mathbb E[X_n\mid\mathcal G]\mathbf 1_A]
\\
&=
\lim_{n\to\infty}
\mathbb E[X_n\mathbf 1_A]
\\
&=
\mathbb E[X\mathbf 1_A].
\end{aligned}
$$

The variable \(Y\) is denoted by

$$
\mathbb E[X\mid\mathcal G].
$$

The definition is independent of the chosen versions: two choices agree outside the countable union of the null sets on which the corresponding integrable conditional expectations differ.

Here MCT is legitimate because the approximation is nonnegative and increasing.

---

## 2. Conditional Jensen and \(L^p\)-contraction

### Proposition 2.1 — Conditional Jensen

Let \(X\in L^1(\mathbb P)\), and let \(\varphi:\mathbb R\to\mathbb R\) be convex. If

$$
\varphi(X)\in L^1(\mathbb P),
$$

then

$$
\varphi\!\left(\mathbb E[X\mid\mathcal G]\right)
\leq
\mathbb E[\varphi(X)\mid\mathcal G]
\qquad
\mathbb P\text{-a.s.}
$$

#### Proof

A finite convex function on \(\mathbb R\) is the pointwise supremum of a countable family of affine minorants:

$$
\varphi(x)
=
\sup_{k\geq1}(a_kx+b_k).
$$

For every \(k\),

$$
a_kX+b_k
\leq
\varphi(X).
$$

Linearity and monotonicity of conditional expectation therefore give

$$
a_k\mathbb E[X\mid\mathcal G]+b_k
\leq
\mathbb E[\varphi(X)\mid\mathcal G].
$$

Taking the supremum over \(k\) proves the result.

If \(1\leq p<\infty\) and \(X\in L^p(\mathbb P)\), apply the proposition to

$$
\varphi(x)=|x|^p.
$$

Then

$$
\left|
\mathbb E[X\mid\mathcal G]
\right|^p
\leq
\mathbb E[|X|^p\mid\mathcal G],
$$

and hence

$$
\left\|
\mathbb E[X\mid\mathcal G]
\right\|_p
\leq
\|X\|_p.
$$

If \(X\in L^\infty(\mathbb P)\), monotonicity applied to

$$
-\|X\|_\infty
\leq
X
\leq
\|X\|_\infty
$$

gives

$$
\left\|
\mathbb E[X\mid\mathcal G]
\right\|_\infty
\leq
\|X\|_\infty.
$$

---

## 3. The \(L^2\)-projection interpretation

Assume that \(X\in L^2(\mathbb P)\). Conditional Jensen gives

$$
\mathbb E[X\mid\mathcal G]\in L^2(\mathbb P).
$$

Let

$$
Y=\mathbb E[X\mid\mathcal G].
$$

For every bounded \(\mathcal G\)-measurable \(Z\),

$$
\mathbb E[(X-Y)Z]=0.
$$

By truncation and the Cauchy–Schwarz inequality, the identity extends to every

$$
Z\in L^2(\Omega,\mathcal G,\mathbb P|_{\mathcal G}).
$$

Thus

$$
X-Y
\perp
L^2(\Omega,\mathcal G,\mathbb P|_{\mathcal G}).
$$

Consequently,

$$
\mathbb E[X\mid\mathcal G]
$$

is the orthogonal projection of \(X\) onto the closed subspace

$$
L^2(\Omega,\mathcal G,\mathbb P|_{\mathcal G})
\subseteq
L^2(\Omega,\mathcal F,\mathbb P).
$$

For every \(Z\in L^2(\mathcal G)\),

$$
\|X-Z\|_2^2
=
\|X-Y\|_2^2+\|Y-Z\|_2^2.
$$

In particular,

$$
\|X-Y\|_2
\leq
\|X-Z\|_2.
$$

The Radon–Nikodym construction is valid in \(L^1\); the projection interpretation is specific to \(L^2\).

---
