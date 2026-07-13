---
type: td
module: foundations
status: canonical
---

# TD 01 — Integration and Convergence

Let $(E,\mathcal A,\mu)$ be a measure space. The construction of the nonnegative integral and MCT may be used.

## Exercise 0 — Pointwise convergence is insufficient

On $((0,1),\mathcal B((0,1)),\lambda)$, define

$$
f_n=n\mathbf1_{(0,1/n)}.
$$

1. Prove that $f_n\to0$ almost everywhere.
2. Compute $\int_0^1f_n\,d\lambda$.
3. Prove that no common integrable dominator can exist.
4. Identify precisely why neither MCT nor DCT applies.

## Exercise 1 — MCT as a measure-construction engine

Let $f:E\to[0,+\infty]$ be measurable and define

$$
\nu(A)=\int_Af\,d\mu,
\qquad A\in\mathcal A.
$$

1. Prove finite additivity.
2. Let $(A_n)$ be pairwise disjoint and set $B_N=\bigcup_{n=1}^NA_n$. Express $\mathbf1_{B_N}f$ as a finite sum.
3. Apply MCT to prove

   $$
   \nu\!\left(\bigcup_{n\ge1}A_n\right)
   =
   \sum_{n\ge1}\nu(A_n).
   $$

4. Prove that $\nu\ll\mu$.

## Exercise 2 — Fatou from MCT

Let $(f_n)$ be nonnegative measurable functions.

1. Define $g_n=\inf_{k\ge n}f_k$ and derive Fatou's lemma from MCT.
2. Give an example in which Fatou's inequality is strict.
3. For measurable sets $(A_n)$, prove

   $$
   \mu(\liminf A_n)
   \le
   \liminf_n\mu(A_n).
   $$

4. State the additional hypothesis under which the same argument may be applied to signed functions bounded below by an integrable function.

## Exercise 3 — DCT from Fatou

Let $f_n\to f$ almost everywhere and suppose that $|f_n|\le g$ for some $g\in L^1(\mu)$.

1. Apply Fatou to $g+f_n$ and $g-f_n$.
2. Deduce convergence of the integrals.
3. Apply DCT to $|f_n-f|$ and obtain $L^1$ convergence.
4. Construct an example showing that the conclusion may fail if the dominator is not integrable.

## Exercise 4 — Uniform absolute continuity of the integral

Let $f\in L^1(\mu)$.

1. Prove

   $$
   \int_{\{|f|>M\}}|f|\,d\mu
   \longrightarrow0
   \qquad(M\to\infty).
   $$

2. Deduce that for every $\varepsilon>0$ there exists $\delta>0$ such that

   $$
   \mu(A)<\delta
   \quad\Longrightarrow\quad
   \int_A|f|\,d\mu<\varepsilon.
   $$

3. Explain how this property differs from the statement $f\mu\ll\mu$.

Source: ENS Paris, *Intégration et probabilités*, TD 2, Exercise 1, 2017–2018.

## Exercise 5 — Series and exchange of integral

Let $(f_n)$ be measurable.

1. If $f_n\ge0$, prove

   $$
   \int_E\sum_{n\ge1}f_n\,d\mu
   =
   \sum_{n\ge1}\int_Ef_n\,d\mu.
   $$

2. Assume

   $$
   \sum_{n\ge1}\int_E|f_n|\,d\mu<+\infty.
   $$

   Prove that $\sum_n f_n$ converges absolutely almost everywhere and in $L^1$.

3. Deduce

   $$
   \int_E\sum_{n\ge1}f_n\,d\mu
   =
   \sum_{n\ge1}\int_Ef_n\,d\mu.
   $$

## Reconstruction

Without consultation, reconstruct

$$
\mathrm{MCT}
\Longrightarrow
\mathrm{Fatou}
\Longrightarrow
\mathrm{DCT}.
$$

Close by proving that $A\mapsto\int_Af\,d\mu$ is a measure for every measurable $f\ge0$.
