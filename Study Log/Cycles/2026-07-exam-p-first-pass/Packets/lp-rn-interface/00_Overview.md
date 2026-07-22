---
type: study-packet-overview
date: 2026-07-14
cycle: 2026-07-exam-p-first-pass
packet: lp-rn-interface
role: prerequisite
session: P0
sessions: 1
planned-time: 90m
supplementary: true
math-authority: derived
canonical-sources:
  - ../../../../../15_Lp-Interface/01_Cours/Cours.md
  - ../../../../../15_Lp-Interface/01_Cours/Cours 02 — Hölder, Jensen, and L2 Geometry.md
  - ../../../../../15_Lp-Interface/02_TD/TD 01 — Integrability, Test Functions, and Change of Measure.md
  - ../../../../../20_Radon-Nikodym/01_Cours/Cours.md
---

# $L^p$ Spaces and Density Measures

*Séance of 14 July 2026 · 90 minutes*

This module does not reconstruct the Radon–Nikodym theorem. It assumes the theorem and recalls only its hypotheses, reference measure, signed extension, and almost-everywhere uniqueness. Its object is the $L^p$ framework used later for expectation, conditioning, conditional expectation, and variance.

## Aim

Work with:

- the measure-dependent nature of $L^p(\mu)$;
- the hierarchy of moments on a probability space;
- bounded test functions;
- measures defined by densities;
- change of measure and the uses of Radon–Nikodym.

The order is

$$
L^p(\mu)\text{ as a measure-dependent object}
\longrightarrow
\text{moment control on a probability space}
\longrightarrow
\text{bounded tests}
\longrightarrow
\text{measures defined by densities}
\longrightarrow
\text{Radon--Nikodym representations}.
$$

There is no implication

$$
L^q(\mu)\subseteq L^p(\mu)
\Longrightarrow
\text{Hahn local domination}.
$$

These statements belong to different proofs.

## Programme

1. **15 minutes — objects.** Read [Preparatory Notes](01_Preparatory%20Notes.md) §§1–2 and complete Exercise 0 in the [Feuille de travail](02_Feuille%20de%20travail.md). Recover the ambient measure, equivalence relation, moment interpretation, and
   $$
   L^\infty(\mathbb P)\subseteq L^2(\mathbb P)\subseteq L^1(\mathbb P).
   $$
2. **20 minutes — finite-measure embeddings.** Complete Exercise 1(1)–(2) in the formal [$L^p$ TD 01](../../../../../15_Lp-Interface/02_TD/TD%2001%20—%20Integrability,%20Test%20Functions,%20and%20Change%20of%20Measure.md). Retain the Hölder exponents and the exact norm constant. Defer the long counterexamples.
3. **20 minutes — bounded tests.** Complete Exercise 2(1)–(2), (4) of the same TD. Distinguish indicators, bounded simple functions, and the passage by dominated convergence.
4. **20 minutes — densities and change of measure.** Complete Exercise 3(3), (5) and Exercise 4(1) of the same TD. Recover the finite signed numerator, almost-everywhere uniqueness, and integration under a density.
5. **10 minutes — later uses.** Complete Exercise 1 in the Feuille de travail. For each case, identify the numerator, reference measure, measurable space, almost-everywhere basis, and mathematical use.
6. **5 minutes — conclusion.** Enter the first rupture and its minimal repair in the [Carnet](03_Carnet.md).

## Required reconstruction

At the end of the séance, recover without notes:

$$
L^\infty(\mathbb P)
\subseteq
L^2(\mathbb P)
\subseteq
L^1(\mathbb P),
$$

$$
L^1(\mu)\times L^\infty(\mu)
\longrightarrow
L^1(\mu),
\qquad
L^2(\mathbb P)\times L^2(\mathbb P)
\longrightarrow
L^1(\mathbb P),
$$

and

$$
f\in L^1(\mu)
\longmapsto
\nu_f=f\mu
\ll\mu,
$$

$$
\nu=h\mu
\Longrightarrow
\int\varphi\,d\nu
=
\int\varphi h\,d\mu.
$$

For Radon–Nikodym, retain four distinctions:

1. constructing a measure from a density and recovering a density from a measure are opposite directions;
2. the standard positive theorem requires the stated absolute-continuity and $\sigma$-finiteness hypotheses;
3. a finite signed numerator is treated through its Jordan decomposition;
4. $d\nu/d\mu$ is unique only $\mu$-almost everywhere.

## Beyond this séance

The following remain part of the [extended programme](../../../../../00_Project/Training%20Route%20—%20RN%20Reconstruction%20to%20Conditional%20Expectation.md):

- sharpness of the finite-measure embedding constant;
- two counterexamples on infinite measure spaces;
- the full Young–Hölder–Minkowski reconstruction;
- the Hahn local-density argument, maximal represented mass, residue elimination, and $\sigma$-finite gluing;
- the full $L^2$ projection theory.

## Polycopié

The five Markdown files are the reference edition. The [typesetting notes](Sources/LaTeX/README.md) produce an A4 polycopié and an independent Corrigé; the same sources are available as an [Overleaf archive](Polycopiés/Overleaf%20Sources.zip).

## Working rule

Do not consult either the formal corrigé or this module’s [Corrigé](04_Corrigé.md) before a complete written attempt. Failure to recall the Hahn-first proof is recorded as later work. The relevant rupture here is failure to identify the $L^p$ regime, numerator, reference measure, or almost-everywhere basis.
