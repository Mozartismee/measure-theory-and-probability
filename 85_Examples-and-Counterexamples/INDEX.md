---
type: example-pair-index
module: examples-and-counterexamples
status: canonical
---

# Examples and Counterexamples Index

This directory is the canonical library of reusable example pairs. A pair records both a legal regime and the precise failures produced by removing a decisive hypothesis or violating a compatibility condition. It consumes canonical mathematics; it is not a teaching unit, a theorem dependency, or evidence of closed-book mastery.

## Admission criteria

An entry belongs here only if it:

1. isolates a mechanism already used across the current modules or the 14–19 July 2026 study chain;
2. gives an explicit positive regime and a failure regime obtained by removing or violating named conditions;
3. states the reference measure, almost-everywhere basis, denominator conditions and theorem boundary whenever they occur;
4. follows the fixed order `Setup → Positive regime → Failure regime → Decisive mechanism → Boundary → Reconstruction`;
5. links to the canonical theorem sources instead of maintaining a second proof of a general theorem.

The initial collection is deliberately restricted to finite conditioning, normalized restriction, counting measure and the J3 two-class mixture. Unrelated pathologies do not enter merely because they exist. New material here is revision infrastructure, not learner-state evidence.

## Stable numbering

Example-pair numbers are permanent citation identifiers. Renaming a file or refining its title does not change its number. A retired number remains reserved and is never reassigned.

## Current example pairs

| No. | Example pair | Positive regime | Removed hypothesis | Failure | Competency keys | Canonical sources |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Finite Partitions — Determined Values and Null-Atom Freedom](01%20—%20Finite%20Partitions%20—%20Determined%20Values%20and%20Null-Atom%20Freedom.md) | Positive-mass atoms determine their coefficients | Positivity of one atom | The defining identity leaves that atom's point value arbitrary, although the $L^1$ class remains unique | `CE.finite-sigma-fields`, `CE.rn-construction` | [Conditional Expectation Cours](../40_Conditional-Expectation/01_Cours/Cours.md); [Finite Sigma-Fields TD](../40_Conditional-Expectation/02_TD/TD%2002%20—%20Finite%20Sigma-Fields.md) |
| 2 | [Event Conditioning — Positive-Mass Normalization and Null-Event Failure](02%20—%20Event%20Conditioning%20—%20Positive-Mass%20Normalization%20and%20Null-Event%20Failure.md) | $\mathbb P(A)>0$ permits normalized restriction and an event conditional mean | Positive event mass | The ratio and normalized probability are undefined; conditional expectation on $\sigma(N)$ still exists as an $L^1$ class | `CE.rn-construction`, `CE.finite-sigma-fields` | [Conditional Expectation Cours](../40_Conditional-Expectation/01_Cours/Cours.md); [Atomic Laws Cours](../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md) |
| 3 | [Counting Measure — Countable Density and Uncountable Failure](03%20—%20Counting%20Measure%20—%20Countable%20Density%20and%20Uncountable%20Failure.md) | A countable state space makes counting measure $\sigma$-finite and yields a pointwise density | Countability, hence $\sigma$-finiteness of the reference measure | Absolute continuity becomes vacuous and a nonatomic probability has no counting-measure density | `PF.counting-measure`, `PF.atomic-laws`, `RN.hypotheses` | [Lemma 5](../80_Lemmas/Counting%20Measure%20and%20the%20Radon–Nikodym%20Boundary.md); [Atomic Laws Cours](../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md) |
| 4 | [Two-Class Mixtures — Identification, Degeneracy, and Incompatibility](04%20—%20Two-Class%20Mixtures%20—%20Identification,%20Degeneracy,%20and%20Incompatibility.md) | $u\ne v$, compatible $m$, positive class masses and $m>0$ | Injectivity or compatibility of the affine mixture map | The prior is non-identified, inconsistent, or infeasible | `PF.mixtures`, `CE.finite-sigma-fields` | [Atomic Laws Cours](../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md); [Conditional Expectation Cours](../40_Conditional-Expectation/01_Cours/Cours.md) |

## Generated-$\sigma$-field mechanism

When an example must pass from a generating family to the generated $\sigma$-field, use [Lemma 4 — Generated Sigma-Fields and Measurable Sections](../80_Lemmas/Generated%20Sigma-Fields%20and%20Measurable%20Sections.md): identify the stable class, verify the generators, and invoke minimality. This is a reusable proof mechanism, not a new dependency arrow from this library.
