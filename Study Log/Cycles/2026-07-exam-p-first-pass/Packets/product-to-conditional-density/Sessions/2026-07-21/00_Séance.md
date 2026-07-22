---
type: study-session-sheet
date: 2026-07-21
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
session-kind: rupture-repair-with-transfer
session: J4
planned-time: 90m
actual-time:
solutions-policy: attempt-before-corrige
state: not-attempted
math-authority: derived
canonical-sources:
  - ../../../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../../../80_Lemmas/Generated Sigma-Fields and Measurable Sections.md
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
---

# Feuille J4 — Des sections mesurables au théorème de Tonelli

*Durée : 90 minutes. Sans documents.*

This is the only document permitted during the attempt. The product-measure existence theorem, the $\pi$-$\lambda$ theorem and monotone convergence may be used with their hypotheses; Tonelli and Fubini may not.

Open the [Indications](01_Indications.md) only after five minutes of genuine obstruction and a written record of the first unjustified step. Open the [Corrigé](02_Corrigé.md) only after the complete copie, the exit and the Bilan.

## Question de cours — 0–10 minutes

State the product-measure theorem for two $\sigma$-finite measure spaces, including the rectangle prescription and the uniqueness regime. Indicate, without proof, the construction from the ring of finite disjoint unions of measurable rectangles and the point at which $\sigma$-finiteness enters.

Continue at minute ten, whether or not the reconstruction is complete.

## Problème — 10–70 minutes

Let $(E,\mathcal A,\mu)$ and $(F,\mathcal B,\nu)$ be $\sigma$-finite measure spaces. Write $\mu\otimes\nu$ for their product measure. For $C\subseteq E\times F$, set

$$
C_x=\{y\in F:(x,y)\in C\},
\qquad
C^y=\{x\in E:(x,y)\in C\}.
$$

1. Prove that

   $$
   C\in\mathcal A\otimes\mathcal B
   \Longrightarrow
   C_x\in\mathcal B\text{ for every }x,
   \quad
   C^y\in\mathcal A\text{ for every }y.
   $$

2. Prove, first when $\mu$ and $\nu$ are finite and then in the $\sigma$-finite case, that the maps

   $$
   x\longmapsto\nu(C_x),
   \qquad
   y\longmapsto\mu(C^y)
   $$

   are measurable and that

   $$
   (\mu\otimes\nu)(C)
   =
   \int_E\nu(C_x)\,\mu(dx)
   =
   \int_F\mu(C^y)\,\nu(dy).
   $$

3. Deduce Tonelli's theorem for every $\mathcal A\otimes\mathcal B$-measurable function $f:E\times F\to[0,+\infty]$, including the measurability of the two section integrals. State whether the common value must be finite.

4. Identify precisely why the preceding argument does not authorize an exchange of iterated integrals for a signed measurable function outside $L^1(\mu\otimes\nu)$. State the additional hypothesis under which Fubini becomes legitimate.

## Épreuve de sortie — 70–85 minutes

Close the preceding pages and use a fresh sheet. No indication is available.

First reconstruct the complete proof that every section of a set in a product $\sigma$-field is measurable.

Then let $(S,\mathscr S,\rho)$ be a $\sigma$-finite measure space and let $g:S\to[0,+\infty]$ be measurable. On $S\times(0,+\infty)$ define

$$
H_g=\{(s,t):0<t<g(s)\}.
$$

Prove that $H_g\in\mathscr S\otimes\mathcal B((0,+\infty))$, compute both kinds of sections, and derive

$$
\int_S g\,d\rho
=
\int_0^\infty \rho(g>t)\,dt.
$$

State why the identity remains valid when both sides equal $+\infty$.

## Bilan libre — 85–90 minutes

Before opening the Corrigé, record in at most five lines the actual duration, every indication consulted, the exact first unjustified step, and whether the section proof and the tail-integral transfer were completed without notes. Do not repair the copie in the Bilan.

## Prolongement facultatif — hors séance

The timed séance ends with the Bilan above. Only after fixing it, and only if a further 20–25 minutes are genuinely available, attempt the [Prolongement facultatif](03_Prolongement%20facultatif.md) before opening the Corrigé. It is not part of the 90-minute verdict and cannot replace an incomplete exit.
