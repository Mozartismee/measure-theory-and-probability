---
type: td
module: lp-interface
status: canonical
---

# TD 02 — Hölder, Jensen, and $L^2$ Geometry

Let $(E,\mathcal A,\mu)$ be a measure space. General Hölder, Jensen and the Hilbert projection theorem may be used only after they have been reconstructed in the corresponding exercise.

## Exercise 1 — From Young to Hölder and Minkowski

Let $1<p<+\infty$ and let $q=p/(p-1)$.

1. Prove Young's inequality

   $$
   ab\le\frac{a^p}{p}+\frac{b^q}{q},
   \qquad a,b\ge0,
   $$

   and determine the equality case.

2. Deduce Hölder's inequality for $f\in L^p(\mu)$ and $g\in L^q(\mu)$.

3. Assume that neither function is zero in its $L^p$-class. Determine the equality condition in Hölder.

4. Use Hölder to prove Minkowski's inequality

   $$
   \|f+g\|_p
   \le
   \|f\|_p+\|g\|_p.
   $$

5. Explain why none of these arguments proves the representation

   $$
   (L^p)^*=L^q.
   $$

## Exercise 2 — Cauchy–Schwarz, covariance and moments

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $X,Y\in L^2(\mathbb P)$.

1. Prove that $XY\in L^1(\mathbb P)$ and

   $$
   |\mathbb E[XY]|
   \le
   \|X\|_2\|Y\|_2.
   $$

2. Prove

   $$
   |\operatorname{Cov}(X,Y)|
   \le
   \sqrt{\operatorname{Var}(X)}
   \sqrt{\operatorname{Var}(Y)}.
   $$

   Determine the equality case.

3. Let $1\le r<s<+\infty$ and $X\in L^s(\mathbb P)$. Prove

   $$
   \|X\|_r\le\|X\|_s
   $$

   first by Hölder and then by Jensen.

4. Give a counterexample to this monotonicity on an infinite measure space.

## Exercise 3 — Jensen and its equality boundary

Let $X\in L^1(\mathbb P)$ and let $\Phi$ be a finite convex function on an interval containing the essential range of $X$. Assume $\Phi(X)\in L^1$.

1. Prove Jensen's inequality from a supporting affine function at $\mathbb E[X]$.

2. Assume that $\Phi$ is strictly convex. Prove that equality implies that $X$ is almost surely constant.

3. Deduce

   $$
   |\mathbb E[X]|^2
   \le
   \mathbb E[X^2]
   $$

   for $X\in L^2$ and identify the equality case.

4. If $X>0$ almost surely, $X\in L^1$ and $X^{-1}\in L^1$, prove

   $$
   \mathbb E[X]\,\mathbb E[X^{-1}]
   \ge1.
   $$

5. Explain how Jensen must be modified when $0<\mu(E)<+\infty$ and $\mu(E)\ne1$.

## Exercise 4 — Projection onto an affine linear model

Let $X,Y\in L^2(\mathbb P)$ and assume $\operatorname{Var}(Y)>0$.

1. Determine the unique pair $(a,b)\in\mathbb R^2$ minimizing

   $$
   \mathbb E[(X-a-bY)^2].
   $$

2. Prove that the residual

   $$
   R=X-a-bY
   $$

   is orthogonal in $L^2$ to both $1$ and $Y$.

3. Show that

   $$
   b
   =
   \frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)},
   \qquad
   a
   =
   \mathbb E[X]-b\mathbb E[Y].
   $$

4. Compute the minimum error and express it using the correlation coefficient when both variances are positive.

5. Identify precisely which part fails when $\operatorname{Var}(Y)=0$.

## Exercise 5 — Closed-subspace projection

Let $H$ be a real Hilbert space, let $M\subseteq H$ be a closed linear subspace and let $x\in H$.

1. Let $(m_n)\subseteq M$ satisfy

   $$
   \|x-m_n\|
   \longrightarrow
   d(x,M).
   $$

   Use the parallelogram identity to prove that $(m_n)$ is Cauchy.

2. Prove existence and uniqueness of a minimizer $P_Mx\in M$.

3. Prove the equivalence

   $$
   m=P_Mx
   \quad\Longleftrightarrow\quad
   m\in M,
   \quad
   x-m\perp M.
   $$

4. Prove that $P_M$ is linear and that

   $$
   \|P_Mx-P_My\|
   \le
   \|x-y\|.
   $$

5. Explain why closedness of $M$ cannot simply be deleted from the statement.

## Reconstruction

Without consulting the Cours, reconstruct:

$$
\text{Young}
\Longrightarrow
\text{Hölder}
\Longrightarrow
\text{Cauchy–Schwarz},
$$

$$
\text{supporting line}
\Longrightarrow
\text{Jensen}
\Longrightarrow
\|X\|_r\le\|X\|_s,
$$

and

$$
\text{parallelogram identity}
\Longrightarrow
\text{orthogonal projection}
\Longrightarrow
\text{normal equations}.
$$

Close by stating which assertions require a probability measure, which require completeness, and which are only almost-everywhere statements.
