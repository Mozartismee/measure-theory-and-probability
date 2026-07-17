---
type: td
module: signed-measures
status: canonical
---

# TD 01 — Hahn–Jordan Structure and Domination

Let $(E,\mathcal A)$ be a measurable space. All signed measures are finite. The Hahn decomposition theorem may be used without proof; everything extracted from it remains the responsibility of the argument.

## Exercise 1 — Positive, negative and null sets

Let $\sigma$ be a finite signed measure.

1. Prove that every measurable subset of a positive set is positive, and every measurable subset of a negative set is negative.

2. Prove that a countable union of positive sets is positive. State and prove the corresponding assertion for negative sets.

3. Let $P$ be positive and $N$ negative. Prove that

   $$
   P\cap N
   $$

   is $\sigma$-null.

4. Explain why the statement that $Z$ is $\sigma$-null is stronger than the single equality $\sigma(Z)=0$.

## Exercise 2 — Ambiguity of Hahn sets and canonicity of Jordan measures

Let

$$
E=P\sqcup N=P'\sqcup N'
$$

be two Hahn decompositions of $\sigma$.

1. Prove that

   $$
   P\triangle P'
   \qquad\text{and}\qquad
   N\triangle N'
   $$

   are $\sigma$-null.

2. Define

   $$
   \sigma^+(A)=\sigma(A\cap P),
   \qquad
   \sigma^-(A)=-\sigma(A\cap N).
   $$

   Prove that $\sigma^+$ and $\sigma^-$ are positive measures and that

   $$
   \sigma=\sigma^+-\sigma^-.
   $$

3. Prove that $\sigma^+$ and $\sigma^-$ do not depend on the chosen Hahn decomposition.

4. Let $\alpha$ and $\beta$ be finite positive measures satisfying

   $$
   \sigma=\alpha-\beta.
   $$

   Prove the minimality property

   $$
   \sigma^+\le\alpha,
   \qquad
   \sigma^-\le\beta.
   $$

5. Deduce the uniqueness of the Jordan decomposition among decompositions into mutually singular positive measures.

## Exercise 3 — Signed densities

Let $\mu$ be a positive measure and let $f\in L^1(\mu)$. Define

$$
\sigma_f(A)=\int_Af\,d\mu.
$$

1. Prove that

   $$
   P=\{f\ge0\},
   \qquad
   N=\{f<0\}
   $$

   form a Hahn decomposition of $\sigma_f$.

2. Compute $\sigma_f^+$, $\sigma_f^-$ and $|\sigma_f|$.

3. Prove that a measurable set $Z$ is $\sigma_f$-null if and only if

   $$
   f=0
   \qquad\mu\text{-almost everywhere on }Z.
   $$

4. Let $g\in L^1(\mu)$. Prove that

   $$
   \sigma_f=\sigma_g
   \quad\Longrightarrow\quad
   f=g
   \quad\mu\text{-almost everywhere}.
   $$

## Exercise 4 — From sign structure to local domination

Let $\mu$ and $\rho$ be finite positive measures and let $c>0$. Set

$$
\tau_c=\rho-c\mu.
$$

Let

$$
E=P_c\sqcup N_c
$$

be a Hahn decomposition of $\tau_c$.

1. Prove that

   $$
   c\mathbf1_{P_c}\mu\le\rho
   $$

   and

   $$
   \rho|_{N_c}\le c\mu|_{N_c}.
   $$

2. Assume that $\rho\ll\mu$ and $\rho\ne0$. For each $n\ge1$, choose a Hahn decomposition

   $$
   E=P_n\sqcup N_n
   $$

   for

   $$
   \rho-\frac1n\mu.
   $$

   Prove that $\mu(P_n)>0$ for at least one $n$.

3. Deduce the local density fragment

   $$
   \exists\,\varepsilon>0,\ \exists\,P\in\mathcal A:
   \quad
   \mu(P)>0,
   \qquad
   \varepsilon\mathbf1_P\mu\le\rho.
   $$

4. Identify exactly where finiteness and absolute continuity are used.

## Reconstruction — Hahn to Radon–Nikodym

Without consulting the Cours, reconstruct the chain

$$
\text{Hahn decomposition}
\Longrightarrow
\text{Jordan decomposition}
\Longrightarrow
\text{minimality}
\Longrightarrow
\text{local domination}.
$$

Your reconstruction must distinguish:

- a Hahn set, which is not canonical;
- the Jordan measures, which are canonical;
- a $\sigma$-null set, which is not merely a set of total signed mass zero;
- the sign information in $\rho-c\mu$, which becomes an inequality between positive measures.
