---
type: reconstruction
module: review
status: canonical
---

# Reconstruction Problems — $L^1$, Signed Measures, and Conditional Expectation

## 1. Reconstruction problems

Let \((E,\mathcal A,\mu)\) be a measure space.

### Exercise 1 — The endpoint pairing

Let \(f\in L^1(\mu)\) and let \(Z\) be measurable.

1. Prove that \(Z\in L^\infty(\mu)\) implies \(fZ\in L^1(\mu)\).
2. Assume that \(\mu(E)<\infty\). Establish the inclusion

   $$
   L^\infty(\mu)\subseteq L^q(\mu)\subseteq L^p(\mu)\subseteq L^1(\mu),
   \qquad
   1\leq p\leq q\leq\infty.
   $$

3. Give examples of infinite-measure spaces and functions showing that the displayed chain need not hold.

---

### Exercise 2 — Separation by test functions

Let \(f,g\in L^1(\mu)\), and let \(\mathcal G\subseteq\mathcal A\) be a sub-\(\sigma\)-field.

Prove the equivalence of the following assertions:

1. For every \(A\in\mathcal G\),

   $$
   \int_A f\,d\mu
   =
   \int_A g\,d\mu.
   $$

2. For every bounded \(\mathcal G\)-measurable \(Z\),

   $$
   \int_EZf\,d\mu
   =
   \int_EZg\,d\mu.
   $$

Assume in addition that \(f\) and \(g\) are \(\mathcal G\)-measurable. Deduce that

$$
f=g
\qquad\mu\text{-a.e.}
$$

---

### Exercise 3 — Hahn decomposition and domination

Let \(\mu\) and \(\rho\) be finite positive measures, let \(c>0\), and set

$$
\sigma_c=\rho-c\mu.
$$

Let

$$
E=P_c\sqcup N_c
$$

be a Hahn decomposition for \(\sigma_c\).

1. Prove that

   $$
   c\mathbf 1_{P_c}\mu\leq\rho
   $$

   and

   $$
   \rho|_{N_c}\leq c\mu|_{N_c}.
   $$

2. Assume that \(\rho\ll\mu\). Prove that

   $$
   \mu(P_c)=0
   \quad\Longleftrightarrow\quad
   \rho(P_c)=0.
   $$

3. Determine the Jordan decomposition of \(\sigma_c\) in terms of \(P_c\) and \(N_c\).

---

### Exercise 4 — Conditional expectation from Radon–Nikodym

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space, let \(X\in L^1(\mathbb P)\), and let \(\mathcal G\subseteq\mathcal F\) be a sub-\(\sigma\)-field.

1. Construct \(\mathbb E[X\mid\mathcal G]\) using only the positive Radon–Nikodym theorem.
2. Prove uniqueness.
3. Extend the characteristic property from indicators to bounded \(\mathcal G\)-measurable test functions.
4. Prove that

   $$
   \left|
   \mathbb E[X\mid\mathcal G]
   \right|
   \leq
   \mathbb E[|X|\mid\mathcal G].
   $$

   \(\mathbb P\)-almost surely.

5. Deduce that conditional expectation is a contraction on \(L^1(\mathbb P)\).

---

## 2. Structural summary

The constructions tested by this review reduce to the following chain:

$$
f\in L^1(\mu)
\quad\Longrightarrow\quad
A\longmapsto\int_Af\,d\mu
\text{ is a finite signed measure}.
$$

For \(\sigma\)-finite positive measures \(\mu\) and \(\nu\) satisfying

$$
\nu\ll\mu,
$$

the Radon–Nikodym theorem reverses this passage:

$$
\nu(A)
=
\int_A\frac{d\nu}{d\mu}\,d\mu.
$$

For \(X\in L^1(\mathbb P)\), restriction to a sub-\(\sigma\)-field gives the finite signed measure

$$
A\in\mathcal G
\longmapsto
\mathbb E[X\mathbf 1_A].
$$

If \(X\geq0\), its Radon–Nikodym derivative with respect to \(\mathbb P|_{\mathcal G}\) is

$$
\mathbb E[X\mid\mathcal G].
$$

For general \(X\in L^1(\mathbb P)\), the same object is constructed as the difference of the two positive Radon–Nikodym derivatives associated with \(X^+\) and \(X^-\); equivalently, it is the density in the signed Radon–Nikodym sense.

Finally,

$$
\text{indicator tests}
\quad\Longleftrightarrow\quad
\text{bounded }\mathcal G\text{-measurable tests}
$$

through simple approximation and dominated convergence.

These are the functional and measure-theoretic interfaces required for the Radon–Nikodym construction of conditional expectation.
