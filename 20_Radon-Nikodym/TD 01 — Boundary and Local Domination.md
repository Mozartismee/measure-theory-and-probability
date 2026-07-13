---
type: td
module: radon-nikodym
status: canonical
---

# TD 01 — Boundary and Local Domination

Let $(E,\mathcal A)$ be a measurable space. All measures are positive and finite unless otherwise stated. Hahn decomposition for finite signed measures may be used without proof.

Exercise 0 fixes the boundary of the theorem before the finite construction begins.

## Exercise 0 — Failure without $\sigma$-finiteness

*[ENS original — translated]*

Let $\mu$ be counting measure on $([0,1],\mathcal B([0,1]))$ and let $\lambda$ be Lebesgue measure.

1. Prove that

   $$
   \lambda\ll\mu.
   $$

2. Prove that there is no measurable function $f:[0,1]\to[0,+\infty]$ such that

   $$
   \lambda=f\mu.
   $$

   Conclude.

Source: ENS Paris, *Intégration et probabilités*, TD 6, Exercise 1, 2017–2018.

## Exercise 1 — Hahn decomposition and domination

*[Supplementary warm-up]*

Let $\mu$ and $\rho$ be finite positive measures, let $c>0$, and set

$$
\sigma_c=\rho-c\mu.
$$

Let

$$
E=P_c\sqcup N_c
$$

be a Hahn decomposition for $\sigma_c$.

1. Prove that

   $$
   c\mathbf1_{P_c}\mu\le\rho
   $$

   and

   $$
   \rho|_{N_c}\le c\mu|_{N_c}.
   $$

2. Assume in addition that $\rho\ll\mu$. Prove that

   $$
   \mu(P_c)=0
   \quad\Longrightarrow\quad
   \rho\le c\mu.
   $$

## Exercise 2 — Extraction and improvement

*[Supplementary warm-up]*

Let $\mu$ and $\nu$ be finite positive measures such that $\nu\ll\mu$. Let $g:E\to[0,+\infty]$ be measurable and assume that

$$
g\mu\le\nu.
$$

Set

$$
\rho=\nu-g\mu.
$$

1. Assume that $\rho\ne0$. Using the signed measures

   $$
   \rho-\frac1n\mu,
   \qquad n\ge1,
   $$

   prove that there exist $\varepsilon>0$ and $P\in\mathcal A$ such that

   $$
   \mu(P)>0,
   \qquad
   \varepsilon\mathbf1_P\mu\le\rho.
   $$

2. Prove that exactly one of the following alternatives holds:

   $$
   \nu=g\mu,
   $$

   or there exists a measurable function $h\ge0$ such that

   $$
   h\mu\le\nu
   $$

   and

   $$
   \int_Eh\,d\mu
   >
   \int_Eg\,d\mu.
   $$

## Reconstruction — Local domination

Let $\mu$ and $\nu$ be finite positive measures such that $\nu\ll\mu$, and let $g\ge0$ satisfy $g\mu\le\nu$.

Without consulting the preceding exercises, reconstruct the implication

$$
\nu\ne g\mu
\quad\Longrightarrow\quad
\exists\,h\ge0:
h\mu\le\nu,
\qquad
\int_Eh\,d\mu>
\int_Eg\,d\mu.
$$

Only Hahn decomposition may be used as a black box.
