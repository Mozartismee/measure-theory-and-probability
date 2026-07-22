---
type: bibliography
module: project
status: canonical
---

# Bibliography and Source Use

## Primary cours reference

- [Jean-François Le Gall, *Intégration, Probabilités et Processus Aléatoires*](../99_Sources/ENS/Le%20Gall（法文原版%20建議使用）.pdf), FIMFA, ENS Paris, 2006.
  - Chapter 4: $L^p$ spaces and the $L^2$ proof of Radon–Nikodym.
  - Chapter 6: signed measures and Jordan decomposition.
  - Chapter 11: conditional expectation and its structural properties.

Le Gall supplies theorem architecture, proof density and probability applications. The later English book *Measure Theory, Probability, and Stochastic Processes* remains a bibliographic reference, but it is not locally mirrored here. The project does not copy Le Gall's dependency order when using the independent Hahn-first proof of Radon–Nikodym.

## ENS TD sequence

- [TD 1 — Espaces mesurés](../99_Sources/ENS/TD%201%20–%20Espaces%20mesurés.pdf): measurable spaces, generated $\sigma$-fields and elementary ruptures.
- [TD 2 — Integration and convergence](../99_Sources/ENS/TD%202%20–%20Intégration%20et%20théorèmes%20de%20convergence.pdf): convergence theorems and absolute continuity of the integral.
- [TD 3 — Lebesgue measure and construction of measures](../99_Sources/ENS/TD%203%20–%20Mesure%20de%20Lebesgue%20et%20construction%20de%20mesures.pdf).
- [TD 4 — $L^p$ spaces](../99_Sources/ENS/TD%204%20–%20Espaces%20Lp.pdf).
- [TD 5 — Fubini and change of variables](../99_Sources/ENS/TD%205%20–%20Théorèmes%20de%20Fubini%20et%20changement%20de%20variables.pdf).
- [TD 6 — Absolute continuity and parameter integrals](../99_Sources/ENS/TD%206%20–%20Absolue%20continuité%20et%20intégrales%20à%20paramètres.pdf): failure of RN without $\sigma$-finiteness.
- [TD 7 — Radon–Nikodym and approximations](../99_Sources/ENS/TD%207%20–%20Théorème%20de%20Radon-Nikodym,%20approximations.pdf): counterexample-first structure and corrigé density.
- [TD 8 — $L^p$–$L^q$ duality](../99_Sources/ENS/TD%208%20–%20Dualité%20Lp−Lq,%20transformation%20de%20Fourier.pdf).

The source directory also contains the corresponding `td1-corrige.pdf` through `td6-corrige.pdf`. They are used to audit proof density and admissible compression after the exercises have been attempted.

## Conditional expectation

- [Thomas Budzinski, TD 5 — Espérance conditionnelle](../99_Sources/ENS/TD%205%20-%20Espérance%20conditionnelle.pdf): counterexamples, concrete calculations and nontrivial conditional distributions.

## Extended ENS calibration corpus

- [ENS Paris DMA — Analyse fonctionnelle](../99_Sources/ENS/Paris-DMA/Analyse-Fonctionnelle/INDEX.md): Baire, Hahn–Banach, weak and weak-* topologies, distributions, Fourier analysis, Sobolev spaces and spectral theory. Use it to calibrate functional-analytic proof responsibility and endpoint handling; its presence does not authorize expanding the Exam P route into a full Banach-space curriculum.
- [ENS Paris DMA — Statistique](../99_Sources/ENS/Paris-DMA/Statistique/INDEX.md): dominated statistical models, likelihood, estimation, concentration, testing and regression. Use it to preserve model specification, domination, parameterization and the inferential object before calculation.
- [ENS Paris DMA — Processus aléatoires](../99_Sources/ENS/Paris-DMA/Processus-Aleatoires/INDEX.md): path-space measurability, Gaussian processes, conditional expectation, martingales and Markov chains. Conditional-expectation material is a direct structural reference; martingale and Markov-chain material remains outside the current core unless a later module explicitly consumes it.
- [ENS Paris DMA — Intégration et probabilités annales](../99_Sources/ENS/Paris-DMA/Integration-et-Probabilites/INDEX.md): timed synthesis and correction density at the L3 boundary.
- [ENS de Lyon — Intégration et probabilités](../99_Sources/ENS/Lyon/Integration-et-Probabilites/INDEX.md): an independent L3 corpus containing TDs, DM and recent assessment pairs. Use it to cross-check that a construction or exercise progression is not merely an idiosyncrasy of the Paris sequence.
- [ENS de Lyon — Processus stochastiques](../99_Sources/ENS/Lyon/Processus-Stochastiques/INDEX.md): recent M1 assessment and answer-key morphology.

The extended corpus is for calibration and lawful adaptation, not bulk reproduction. A generated note must still cite the exact source used and identify whether an exercise is adapted, combined or independently reconstructed.

## SOA Exam P deployment sources

- [SOA, *Probability Exam — July 2026 Syllabus*](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf): official scope for discrete univariate families, discrete multivariate laws, independent sums and the CLT.
- [SOA, *Exam P Sample Questions*](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf): terminal problem depth and distractor logic; question numbers are snapshot-specific.
- [SOA, *Exam P Sample Solutions*](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-sol.pdf): verification of intended computational routes after a complete attempt.

The SOA sources determine the deployment boundary, not the proof standard. The formal construction and failure analysis remain governed by this project's ENS specification.

## Citation rule

Every adapted exercise should identify its source and the nature of the adaptation. A source is used to determine prerequisites, responsibility distribution, counterexample placement and proof density—not to lend institutional perfume to an otherwise ordinary worksheet.
