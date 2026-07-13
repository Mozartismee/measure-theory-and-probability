# TD 2 — Construction and Reconstruction of the Density

Let $(E,\mathcal A)$ be a measurable space.

The following result, established in TD 1, may be used.

### Local density fragment lemma

If $\mu$ and $\rho$ are finite positive measures such that

$$
0\ne\rho\ll\mu,
$$

then there exist $\varepsilon>0$ and $P\in\mathcal A$ such that

$$
\mu(P)>0,
\qquad
\varepsilon\mathbf1_P\mu\le\rho.
$$

## Exercise 1 — Maximal representable submeasure

*[Supplementary warm-up]*

Let $\mu$ and $\nu$ be finite positive measures such that $\nu\ll\mu$. Define

$$
\mathcal C
=
\left\{
f:E\to[0,+\infty]\text{ measurable}:
f\mu\le\nu
\right\}
$$

and

$$
\alpha
=
\sup_{f\in\mathcal C}
\int_Ef\,d\mu.
$$

1. Prove that $\mathcal C$ is nonempty and stable under finite maxima. Prove that

   $$
   0\le\alpha\le\nu(E)<+\infty.
   $$

2. Choose $(f_n)_{n\ge1}\subset\mathcal C$ such that

   $$
   \int_Ef_n\,d\mu\longrightarrow\alpha.
   $$

   Define

   $$
   g_n=f_1\vee\cdots\vee f_n,
   \qquad
   g=\sup_{n\ge1}g_n.
   $$

   Prove that

   $$
   g\in\mathcal C,
   \qquad
   \int_Eg\,d\mu=\alpha.
   $$

3. Prove that

   $$
   g<+\infty
   \qquad\mu\text{-almost everywhere}.
   $$

## Exercise 2 — Elimination of the residue and uniqueness

*[Supplementary warm-up]*

Retain the notation of Exercise 1 and set

$$
\rho=\nu-g\mu.
$$

1. Prove that $\rho$ is a finite positive measure and that

   $$
   \rho\ll\mu.
   $$

2. Assume that $\rho\ne0$. Apply the local density fragment lemma and construct $h\in\mathcal C$ such that

   $$
   \int_E h\,d\mu>\alpha.
   $$

3. Conclude that

   $$
   \nu=g\mu.
   $$

4. Let $f_1,f_2:E\to[0,+\infty]$ be measurable and assume that the common measure

   $$
   f_1\mu=f_2\mu
   $$

   is finite. Prove that

   $$
   f_1=f_2
   \qquad\mu\text{-almost everywhere}.
   $$

## Exercise 3 — $\sigma$-finite gluing

*[Supplementary warm-up]*

Let $\mu$ and $\nu$ be $\sigma$-finite positive measures such that $\nu\ll\mu$.

1. Construct a measurable partition

   $$
   E=\bigsqcup_{n\ge1}E_n
   $$

   such that

   $$
   \mu(E_n)<+\infty,
   \qquad
   \nu(E_n)<+\infty
   $$

   for every $n$.

2. Apply the finite theorem on each measurable space

   $$
   (E_n,\mathcal A|_{E_n})
   $$

   and obtain a measurable density $f_n$ on $E_n$.

3. Define

   $$
   f=\sum_{n\ge1}f_n\mathbf1_{E_n}.
   $$

   Prove that

   $$
   \nu(A)=\int_Af\,d\mu,
   \qquad A\in\mathcal A.
   $$

4. Prove uniqueness $\mu$-almost everywhere by localization to the sets $E_n$.

## Exercise 4 — Equivalent finite measures

*[Adapted from ENS]*

Let $\mu$ and $\nu$ be $\sigma$-finite positive measures such that $\nu\ll\mu$. Set

$$
\eta=\mu+\nu.
$$

Prove that $\eta$ is $\sigma$-finite, then choose measurable sets $(A_n)_{n\ge1}$ such that

$$
E=\bigcup_{n\ge1}A_n,
\qquad
\eta(A_n)<+\infty.
$$

Define

$$
w_\eta
=
\sum_{n\ge1}
\frac{2^{-n}}{1+\eta(A_n)}\mathbf1_{A_n}
$$

and

$$
\eta^*=w_\eta\eta,
\qquad
\mu^*=w_\eta\mu,
\qquad
\nu^*=w_\eta\nu.
$$

1. Prove that

   $$
   0<w_\eta<+\infty
   $$

   everywhere, and that $\eta^*$, $\mu^*$ and $\nu^*$ are finite positive measures.

2. Prove that

   $$
   \eta^*\sim\eta,
   \qquad
   \mu^*\sim\mu,
   \qquad
   \nu^*\sim\nu,
   \qquad
   \nu^*\ll\mu^*.
   $$

3. Apply the finite Radon–Nikodym theorem to $\nu^*$ and $\mu^*$. If

   $$
   \nu^*=f\mu^*,
   $$

   prove that

   $$
   \nu=f\mu.
   $$

4. Compare this reduction with the disjoint gluing of Exercise 3.

Principal source: ENS Paris, *Mesures signées, Théorème de Radon–Nikodym, Dualité $L^p$–$L^q$*, TD 10, Exercise 3.2(a); the common finite weight for $(\mu,\nu)$ is an adaptation.

## Reconstruction

Reconstruct the finite Radon–Nikodym theorem with no consultation and no intermediate lemma other than Hahn decomposition and the monotone convergence theorem.

The following objects must arise from the argument rather than be announced in advance:

$$
\mathcal C,
\qquad
\alpha,
\qquad
g_n,
\qquad
g,
\qquad
\rho,
\qquad
\varepsilon\mathbf1_P.
$$

Close the proof by stating the exact hypothesis under which uniqueness is established. Then pass to the $\sigma$-finite theorem by one of the two reductions above.
