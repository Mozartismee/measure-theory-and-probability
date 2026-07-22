---
type: example-pair
module: examples-and-counterexamples
status: canonical
example-pair: 4
competency-keys:
  - PF.mixtures
  - CE.finite-sigma-fields
---

# Example Pair 4 — Two-Class Mixtures: Identification, Degeneracy, and Incompatibility

## Setup

Let $(B_1,B_2)$ be a measurable partition with positive class masses. For an observed event $A$, write

$$
\alpha=\mathbb P(B_1)\in(0,1),
\qquad
u=\mathbb P(A\mid B_1),
\qquad
v=\mathbb P(A\mid B_2),
\qquad
m=\mathbb P(A).
$$

The positivity of both class masses is required for the event-ratio definitions of $u$ and $v$. Total probability gives the affine mixture equation

$$
\boxed{
m=\alpha u+(1-\alpha)v=v+\alpha(u-v).
}
$$

The numerical instance is extracted from [Feuille J3 — Restriction normalisée, tribu finie et Bayes](../Study%20Log/Cycles/2026-07-exam-p-first-pass/Packets/expectation-finite-conditioning/Sessions/2026-07-19/00_Séance.md); that séance is a derived study object, while the governing mathematics remains in the canonical module sources.

## Positive regime

Assume $u\ne v$ and that $m$ is compatible with a positive two-class mixture. Then the affine map is injective and

$$
\alpha
=
\frac{m-v}{u-v}.
$$

For

$$
u=\frac45,
\qquad
v=\frac3{10},
\qquad
m=\frac12,
$$

one obtains

$$
\alpha
=
\frac{1/2-3/10}{4/5-3/10}
=
\frac25,
\qquad
1-\alpha=\frac35.
$$

The complete joint table is

|  | $A$ | $A^c$ | Total |
| --- | ---: | ---: | ---: |
| $B_1$ | $\frac25\frac45=\frac{16}{50}=\frac8{25}$ | $\frac25\frac15=\frac4{50}=\frac2{25}$ | $\frac{20}{50}=\frac25$ |
| $B_2$ | $\frac35\frac3{10}=\frac9{50}$ | $\frac35\frac7{10}=\frac{21}{50}$ | $\frac{30}{50}=\frac35$ |
| Total | $\frac{25}{50}=\frac12$ | $\frac{25}{50}=\frac12$ | $1$ |

Since $m>0$, posterior normalization is legitimate:

$$
\boxed{
\mathbb P(B_1\mid A)
=
\frac{\mathbb P(B_1\cap A)}{\mathbb P(A)}
=
\frac{8/25}{1/2}
=
\frac{16}{25}.
}
$$

## Failure regime

There are three distinct failures.

1. **Non-identification.** If $u=v$ and $m=u$, then

   $$
   m=\alpha u+(1-\alpha)u=u
   $$

   for every $\alpha\in(0,1)$. The observable marginal is compatible with every positive prior, so the prior is not identified. As an abstract mixture equation, the endpoints $\alpha\in\{0,1\}$ also solve it, but then one class is null and its event-ratio conditional probability is not defined.

2. **Incompatibility under degeneracy.** If $u=v$ and $m\ne u$, the affine equation reduces to $m=u$ and has no solution.

3. **Convex infeasibility.** For every $\alpha\in[0,1]$,

   $$
   \alpha u+(1-\alpha)v
   \in
   [\min(u,v),\max(u,v)].
   $$

   Hence $m\notin[\min(u,v),\max(u,v)]$ is impossible. If $u\ne v$ and both class masses must be positive, compatibility is sharper:

   $$
   m\in(\min(u,v),\max(u,v)).
   $$

   Endpoint values force $\alpha\in\{0,1\}$ and therefore a null class.

## Decisive mechanism

Identification is injectivity of the forward affine map

$$
\alpha\longmapsto v+\alpha(u-v),
$$

whereas feasibility is membership of $m$ in its image. These are separate questions. Posterior normalization is later: once the joint masses exist, it divides $\mathbb P(B_1\cap A)=\alpha u$ by $m$. It cannot identify $\alpha$ when the forward map has already lost injectivity.

## Boundary

The divisions defining $u$ and $v$ require $\mathbb P(B_1),\mathbb P(B_2)>0$; inversion requires $u\ne v$; posterior event conditioning requires $m=\mathbb P(A)>0$. The joint-table identities are exact scalar equalities, so no reference measure or almost-everywhere representative is involved at that stage.

If the posterior is recast as $\mathbb E[\mathbf1_{B_1}\mid\sigma(A)]$, it is an $L^1$ class unique $\mathbb P$-almost surely, and its coefficient on a null observed atom is arbitrary. This finite event calculation does not assert a conditional kernel or a disintegration theorem. The canonical sources are the [Atomic Laws Cours](../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md) and [Conditional Expectation Cours](../40_Conditional-Expectation/01_Cours/Cours.md).

## Reconstruction

$$
(\alpha,u,v)
\longrightarrow
m=v+\alpha(u-v)
\longrightarrow
\begin{cases}
\alpha=(m-v)/(u-v),&u\ne v\text{ and }m\text{ compatible},\\
\text{non-identification},&u=v,\ m=u,\\
\text{no solution},&u=v,\ m\ne u\text{ or }m\text{ outside the convex range},
\end{cases}
$$

followed, only when $m>0$, by

$$
\mathbb P(B_1\mid A)=\frac{\alpha u}{m}.
$$
